from pathlib import Path
import base64
import mimetypes
import re

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
HTML_FILE = APP_DIR / "montessori_map.html"


st.set_page_config(
    page_title="Montessori Capstone Map",
    page_icon="○",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default top/bottom padding so the project feels like a full-page app.
st.markdown(
    """
    <style>
      .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
      }
      header, footer { visibility: hidden; }
      [data-testid="stToolbar"] { visibility: hidden; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)


def _file_to_data_uri(path: Path) -> str:
    """Convert a local image file to a base64 data URI so it works inside Streamlit's iframe."""
    mime_type, _ = mimetypes.guess_type(path.name)
    mime_type = mime_type or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def inline_local_images(html: str) -> str:
    """
    Replace src="images/..." references with embedded base64 images if the files exist.

    Put your image files in the images/ folder with these names:
      - four-planes.png
      - cosmic-education.png
      - 3-part-cards.png

    If an image file is missing, the original reference is left alone.
    """

    def replace_src(match: re.Match) -> str:
        prefix = match.group(1)
        src = match.group(2)
        suffix = match.group(3)
        image_path = APP_DIR / src
        if image_path.exists() and image_path.is_file():
            return f'{prefix}{_file_to_data_uri(image_path)}{suffix}'
        return match.group(0)

    return re.sub(r'(src=["\'])(images/[^"\']+)(["\'])', replace_src, html)


def load_project_html() -> str:
    html = HTML_FILE.read_text(encoding="utf-8")
    return inline_local_images(html)


project_html = load_project_html()

components.html(
    project_html,
    height=900,
    scrolling=False,
)

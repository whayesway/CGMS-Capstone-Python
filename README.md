# Montessori Capstone Map — Python Web App

This is a Streamlit version of the Montessori Capstone Map.

The app uses Python/Streamlit as the web-app wrapper and renders the interactive map in the browser.

## Files

```text
app.py
montessori_map.html
requirements.txt
images/
  four-planes.png
  cosmic-education.png
  3-part-cards.png
```

## Run locally

Install Streamlit:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Put these files in a GitHub repository.
2. Go to Streamlit Community Cloud.
3. Choose **New app**.
4. Select your GitHub repo.
5. Set the main file path to:

```text
app.py
```

6. Click **Deploy**.
7. Share the Streamlit link with your instructor.

Your instructor only needs the link. They do not need Python, GitHub, or Streamlit installed.

## Images

The original HTML references image files. To make those images appear, add them to the `images/` folder with these exact names:

```text
four-planes.png
cosmic-education.png
3-part-cards.png
```

The Python app automatically embeds those image files into the page when they are present.

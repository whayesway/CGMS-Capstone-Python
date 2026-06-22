#!/usr/bin/env python3
"""
Montessori Capstone Map — Python/Streamlit web app.

This version is written as a Python web app. It does not use the separate
HTML/CSS/JavaScript file from the original project. The interface is built with
Streamlit and Plotly from Python data structures and Python functions.

Run locally:
    pip install -r requirements.txt
    streamlit run app.py
"""

from __future__ import annotations

import html
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import streamlit as st

DATA: list[dict[str, Any]] = [
  {
    "id": "montessori-scientist",
    "title": "Maria Montessori",
    "children": [
      {
        "title": "Scientist",
        "content": "Maria Montessori graduated from the University of Rome with a certificate in physics - mathematics at the age of 20. She stayed at the university to study medicine, becoming an expert in pediatric medicine, and graduating as a doctor of medicine at the age of 26.\n\nShe approached education with a scientific lens. She systematically observed children in natural learning environments, and repeatedly noticed how concentration, self-discipline, and motivation emerged when obstacles were removed.",
        "contentHtml": "<p>Maria Montessori graduated from the University of Rome with a certificate in physics - mathematics at the age of 20. She stayed at the university to study medicine, becoming an expert in pediatric medicine, and graduating as a doctor of medicine at the age of 26.</p><p>She approached education with a scientific lens. She systematically observed children in natural learning environments, and repeatedly noticed how concentration, self-discipline, and motivation emerged when obstacles were removed.</p>"
      },
      {
        "title": "Reformer",
        "content": "Montessori challenged the education system that dominated the world. She rejected the idea that children need to be obedient, need external rewards, and lack the desire to good work. Her reforms extended to every part of the classroom - materials, classroom structure, schedule, the role of the teacher, and more. She replaced rigid structure with prepared environments and guided independence. She sought not to improve existing structures, but to redefine the entire concept of schooling.\n\nMontessori was also a fierce advocate for children with special needs. Her first job with children was working with special needs children, and this influenced her the rest of her life."
      },
      {
        "title": "Peacemaker",
        "content": "Montessori believed education was humanity's most powerful tool for achieving lasting peace. War and suffering were symptoms of deeper issues, ones that start as soon as we're born. The suppresion of independence, moral reasoning, empathy, and kindness are cause of suffering. Through education, Montessori believed we could foster responsibility, cooperation, and respect for our fellow human."
      },
      {
        "title": "Visionary",
        "content": "Maria Montessori created an entirely new method of education. Beyond that, she also contributed several now mainstream pedagogical ideas, such as sensitive periods, the importance of movement and environment in cognitive development, and contributions to the planes of development. Her approach to education also invoked the entire lifespan, from birth to death. She was not asking what a child needs to do right now, but rather, what does this human need to achieve their most sucessful life?"
      },
      {
        "title": "Feminist",
        "content": "Montessori was a fierce advocate for women's rights. As a woman pursuing an education in medicine, she faced daily discrimination, but persisted nonetheless. Montessori had a vision of the \"New Woman\" - one who has both equal rights, and equal responsibilities.\n\nIn the classroom, Montessori did not discriminate. Boys and girls got equal treatment. All children were expected to help out equally, and do their part. Through her classrooms, Montessori demonstrated that boys could clean, and girls could think, as long as they were given the opportunity to do so."
      }
    ]
  },
  {
    "id": "guiding-principles",
    "title": "Guiding Principles of Montessori Education",
    "contentHtml": "<ol><li>Respect the Child by allowing them to work at their own pace, correct their own mistakes, and do things for themselves.</li><li>Children go through different &quot;sensitive periods&quot; where they are more enabled to learn certain subjects and skills. Take advantage of these, by enabling them to learn what most fits their sensitive periods.</li><li>A prepared environment is crucial for the child to learn independently.</li><li>Educate each in their intellectual, physical, emotional, and social needs.</li><li>Guides are there to guide, not teach. With the proper environment, the child will learn best by teaching themself.</li><li>Embrace the uniqueness of each child by offering indivialized learning.</li><li>Mixed age classrooms encourage leadership, social growth, inclusion, and cooperation.</li><li>Give the child freedom within limits.</li><li>Learning is its own reward. There is no need for extrinsic motivation, for the child will find satisfaction in the ability to complete tasks independently.</li></ol>",
    "children": []
  },
  {
    "id": "second-plane",
    "title": "Second Plane of Development",
    "centerHtml": "<p>The Second Plane of Development is one of 4 developmental stages identified by Maria Montessori, each representing a distinct way a human interacts with the world based on their age. Each plane of development lasts 6 years, with all 4 lasting from birth to 24 years old.</p><img src=\"images/four-planes.png\" alt=\"Four planes of development\" /><p style=\"font-size: 0.9em; color: #888;\">Source: https://www.newberryhouse.com/the-montessori-method-and-planes-of-development/</p><p>The second plane is the plane of &quot;conscious imagination&quot;. Children begin to desire intellectual independence, take charge of their learning, and develop moral curiosity.</p>",
    "children": [
      {
        "title": "Sensitive periods",
        "contentHtml": "<p>In the Second Plane of Development, sensitive periods shift from unconscious absorption to <strong>heightened intellectual &amp; moral interests</strong>. Children are now showing sensitivity to justice, fairness, and the reasoning behind the way the world works. It is a period defined by the word &quot;why&quot;.</p><p>Children become deeply concerned with <strong>ethical consistency</strong>, often noticing contradictions in adult behavior or institutional structures. This is reflected in their peer relationships - children are testing social norms, often on each other.</p><p>This period is also sensitive to <strong>imagination and abstraction</strong>, which leads us to introduce subjects like history, geography, science, and mathematics, suitable for the newfound desire to find grand narratives, timelines, hierarchical structures, and other more intellectually complex concepts. Montessori accounts for this by offering impressionistic, grand narratives that weave together a comprehensive understanding of the whole of our world.</p>"
      },
      {
        "title": "Needs and Tendencies",
        "contentHtml": "<p>The Second Plane of Development is defined by a need for <strong>intellectual independence</strong>. The First Plane gives the child a need for physical independence, while the Second Plane introduces a need for cognitive independence. They resist instruction, but welcome tools that will help them think and learn. Failure to meet these needs is often the cause of disengagment, social conflict, and resistance to authority.</p><p>Children have the following needs in the Second Plane of Development:</p><ul><li>intellectual independence</li><li>social belonging</li><li>feeling useful to a group</li><li>meaningful work</li><li>collaborative learning</li><li>big picture concepts</li><li>logical structure</li><li>moral engagement</li><li>understanding societal systems</li></ul>"
      },
      {
        "title": "Characteristics",
        "contentHtml": "<p>In the second plane the child is moving from the concrete to the abstract. They still benefit from hands-on materials, but their works shifts to the mental side. The second plane has the following characteristics:</p><ul><li>increased capacity for logical reasoning</li><li>emerging critical thinking</li><li>ability to synthesize information</li><li>growing imaginitive capacity</li><li>grappling with moral reasoning, right &amp; wrong, fairness &amp; equality</li><li>desire for purpose beyond self</li><li>interest in societal roles</li><li>increased bonding with peers</li><li>awareness of group responsibilities</li><li>sensitivity to respect &amp; disrespect</li><li>heightened emotional fluctuations</li></ul>"
      }
    ]
  },
  {
    "id": "references",
    "title": "References",
    "contentHtml": "<ul><li>Montessori for Everyone. (n.d.). <em>The Five Great Lessons</em> [Episode 66]. https://montessoriforeveryone.com/The-Five-Great-Lessons_ep_66-1.html</li><li>MSL Educational Resources. (n.d.). <em>Montessori's Five Great Lessons</em>. https://www.msl-edu.org/montessoris-five-great-lessons</li><li>Midtown Montessori. (n.d.). <em>About Montessori</em>. https://midtownmontessori.org/about-montessori/</li><li>Montessori Training. (2017, May 10). <em>Montessori Today: Chapter 4 - Key Lessons</em>. https://montessoritraining.blogspot.com/2017/05/montessori-today-chapter-4-key-lessons.html</li><li>Miss Barbara. (n.d.). <em>Miss Barbara's Montessori Resources</em>. http://missbarbara.net/</li><li>Montessori Kiwi. (n.d.). <em>3 Part Cards for Montessori Elementary Grades</em>. https://montessorikiwi.com/blogs/news/3-part-cards-for-montessori-elementary-grades?srsltid=AfmBOoop7tKrxde7ITmgTBvA4dY-W35gJn4l7WLg5HYIiFd8RtNDJ_D7</li></ul>",
    "children": []
  },
  {
    "id": "lessons-montessori",
    "title": "Lessons in a Montessori Classroom",
    "children": [
      {
        "title": "The Great Lessons",
        "contentHtml": "<img src=\"images/cosmic-education.png\" alt=\"Cosmic Education\" style=\"width: min(420px, 70vw); max-height: 220px; object-fit: contain; border-radius: 12px; display: block; margin: 12px auto;\" /><p>The Great Lessons are the backbone of Montessori cosmic education. They follow an order that not only represents the flow of curriculum in the classroom, but also represent a unique, insightful way of viewing history and our place in the universe.</p><p>I have long been interested in coming up with my own ways of categorizing the studies of our universe. My thinking used to focus on considering how many categories of study we can divide human knowledge into. Shall we have a separate category for space and chemistry, or should they be one category? Should human anthropology be a sub-category of sociology, or science? But it is impossible to categorize our studies in a way that is <strong>completely exhaustive and mutually exclusive</strong>.</p><p>The Montessori approach has an answer for this: rather than looking for an ontologically perfect system of organization, we follow a structure that is much more... fractally. Like a series of bubbles that we keep zooming in on, we start with <strong>everything</strong>.</p><p><strong>The First Great Lesson: Coming of the Universe and the Earth</strong></p><p>Once we have tackled that, we ask ourselves, what is the next step? What comes next in the story of us, after we examine the whole universe? We cannot focus on categorizing everything in the universe because then we would spend the vast majority of curriculum focusing on planets we know nothing about, in places unknown, and celestial objects that remain undiscovered. This would not be a very satifying study. So we move to the next biggest, broadest category of study that we want to focus on:</p><p><strong>The Second Great Lesson: Coming of Life</strong></p><p>After this, we start to see our ultimate goal more clearly. We need to answer questions about us. We want to know, what's the deal with humans? We can capture this in 3 questions: Where did we come from? Who are we? Where are we going? We have answered the first question, and now we seek to answer the second question.</p><p><strong>The Third Great Lesson: Coming of Human Beings</strong></p><p>Finally we will answer the third question. Also, seriously, what's up with human beings? Why do we dominate the world? Why are we more advanced than aardvarks and zebras, and what does advanced even mean? The final great lessons seek to answer these questions.</p><p><strong>The Fourth Great Lesson: The Story of Writing</strong></p><p><strong>The Fifth Great Lesson: The Story of Numbers</strong></p>"
      },
      {
        "title": "Key lessons",
        "contentHtml": "<p>Key Lessons are like mini great lessons (shall we say, good lessons?). They focus on more specific points of interest introduced by each of the great lessons. An examples from the first great lesson are Grandfather Rock, or Stellar Nucleosynthesis. You might introduce these to a group of students that has a particular excitement about stars.</p><p>After the second great lesson, you could introduce key lessons of the Long Black Line to show how much time has existed without the presence of humans, or the Timeline of Life</p><p>The third great lesson has key lessons focused on history. When we talk about the study of history, we usually REALLY mean the history of humans: these key lessons could be the Timeline of Civilizations, Timeline of Life, or Fundamental Needs.</p><p>For the 4th and 5th great lessons, these introduce an entire curriculum, so lessons will more so follow what is best suited for the child to learn.</p>"
      },
      {
        "id": "three-period-lessons",
        "title": "Three-period lessons",
        "centerHtml": "<p><strong>This is</strong></p><p><strong>Show me</strong></p><p><strong> What is this?</strong></p>",
        "children": [
          {
            "title": "In the first plane of development",
            "contentHtml": "<p><strong>Period 1: This is...</strong></p><p>The first period is just focused on introducing nomenclature. The child is simply watching as the guide introduces them to the new concepts they are learning. In the first plane, this is often nomenclature.</p><p><strong>Period 2: Show me...</strong></p><p>This period is the most crucial, and should take the longest. This is about reviewing and reinforcing vocabulary. The child is now allowed to interact with material to enable a concrete, physical connection with the ideas being learned. For example, if a child is learning shapes, the guid might lay out a circle, triangle, and rectangle. The guide will then ask, \"can you hand me the triangle?\".</p><p><strong>Period 3: What is this?</strong></p><p>Now, the child is ready to identify things on their own. In the second period, they are asked to identify the object, and in the third period, they must indepently produce the name of the object. Rather than \"Show me the triangle\", we point to the triangle, and ask, \"What is this?\". This is the final step in solidifying the acquisition of a new concept.</p>"
          },
          {
            "title": "In the second plane of development",
            "contentHtml": "<p>The second plane gives way for more sophisticated learning, and as guides, we must be careful not to patronize the student. Egos are now at play, and the child demands more intellectual respect, but we ultimately still follow the framework of the three-period lesson. The main difference is in the 2nd and 3rd periods: these are done through independent and collaborative work. We often use three part cards, where the child must match terminology to it's pictures and descriptions. These are used in the first plane as well, but usually as 2 part cards (picture and term). In the second plane, we introduce more complex descriptions as a third part.</p><img src=\"images/3-part-cards.png\" alt=\"3 Part Cards\" />"
          }
        ]
      },
      {
        "title": "Follow-up work",
        "contentHtml": "<p>Follow-up work can be anything that enhances the development of the child's mind. It is on us as guides to be attuned to what our class needs. We need to be asking what gets each child excited about learning, and paying attention to the kind of engagement that each child craves.</p><p>One of my favorite follow-up works I have given was on the topic of plants. I have a class that is passionate about comics, and creating their own stories, so naturally, I though they would love an assignment that allowed them to create their own stories. I asked for them to each pick a plant, and make a character based on that plant. Once they created the plant, they needed to make a comic strip about their plant. This made them think about science in a more flexible way: If a dandelion had a personality, what would it be, and why? This encourage the students to research their plants, and draw connections between characteristics of plants and characteristics of humans.</p>"
      }
    ]
  }
]

APP_TITLE = "Montessori Capstone Map"

class HtmlToMarkdown(HTMLParser):
    """Small converter for the original contentHtml fields."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.list_stack: list[dict[str, Any]] = []
        self.strong_depth = 0
        self.em_depth = 0

    def add(self, value: str) -> None:
        if value:
            self.parts.append(value)

    def newline(self, count: int = 1) -> None:
        current = "".join(self.parts)
        target = "\n" * count
        while current and not current.endswith(target):
            self.parts.append("\n")
            current += "\n"

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v for k, v in attrs}
        if tag in {"p", "div"}:
            self.newline(2)
        elif tag == "br":
            self.newline(1)
        elif tag == "ul":
            self.newline(2)
            self.list_stack.append({"type": "ul", "n": 0})
        elif tag == "ol":
            self.newline(2)
            self.list_stack.append({"type": "ol", "n": 0})
        elif tag == "li":
            self.newline(1)
            indent = "  " * max(len(self.list_stack) - 1, 0)
            if self.list_stack and self.list_stack[-1]["type"] == "ol":
                self.list_stack[-1]["n"] += 1
                marker = f"{self.list_stack[-1]['n']}. "
            else:
                marker = "- "
            self.add(indent + marker)
        elif tag == "strong":
            self.strong_depth += 1
            self.add("**")
        elif tag == "em":
            self.em_depth += 1
            self.add("*")
        elif tag == "img":
            src = attrs_dict.get("src") or ""
            alt = attrs_dict.get("alt") or "Image"
            self.newline(2)
            self.add(f"[[IMAGE:{src}|{alt}]]")
            self.newline(2)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div"}:
            self.newline(2)
        elif tag == "li":
            self.newline(1)
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.newline(2)
        elif tag == "strong":
            if self.strong_depth > 0:
                self.add("**")
                self.strong_depth -= 1
        elif tag == "em":
            if self.em_depth > 0:
                self.add("*")
                self.em_depth -= 1

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text:
            return
        current = "".join(self.parts)
        if current and not current.endswith((" ", "\n", "**", "*", "- ")):
            self.add(" ")
        self.add(text)

    def markdown(self) -> str:
        output = html.unescape("".join(self.parts))
        output = re.sub(r"\n{3,}", "\n\n", output)
        return output.strip()


def html_to_markdown(value: str) -> str:
    parser = HtmlToMarkdown()
    parser.feed(value or "")
    return parser.markdown()


def markdown_for(item: dict[str, Any], field: str = "content") -> str:
    if field == "center" and item.get("centerHtml"):
        return html_to_markdown(str(item["centerHtml"]))
    if item.get("contentHtml"):
        return html_to_markdown(str(item["contentHtml"]))
    if item.get("content"):
        return str(item["content"])
    return ""


def render_markdown_with_images(markdown: str) -> None:
    """Render converted markdown, replacing image tokens with st.image when files exist."""
    if not markdown:
        return

    pattern = re.compile(r"\[\[IMAGE:(.*?)\|(.*?)\]\]")
    last = 0
    for match in pattern.finditer(markdown):
        text = markdown[last:match.start()].strip()
        if text:
            st.markdown(text)
        src = match.group(1).strip()
        alt = match.group(2).strip() or "Image"
        image_path = Path(src)
        if image_path.exists():
            st.image(str(image_path), caption=alt, use_container_width=True)
        else:
            st.info(f"Image placeholder: {alt} — add `{src}` to the GitHub repo to display it here.")
        last = match.end()
    remaining = markdown[last:].strip()
    if remaining:
        st.markdown(remaining)


def get_node(path: list[int]) -> dict[str, Any] | None:
    if not path:
        return None
    node = DATA[path[0]]
    for index in path[1:]:
        node = node.get("children", [])[index]
    return node


def open_item(index: int, items: list[dict[str, Any]]) -> None:
    st.session_state.path.append(index)
    st.rerun()


def go_back() -> None:
    if st.session_state.path:
        st.session_state.path.pop()
    st.rerun()


def go_home() -> None:
    st.session_state.path = []
    st.rerun()


def render_menu() -> None:
    st.sidebar.title("Menu")

    if st.sidebar.button("Home", key="menu_home", use_container_width=True):
        go_home()
    if st.session_state.path and st.sidebar.button(
        "← Back", key="menu_back", use_container_width=True
    ):
        go_back()

    st.sidebar.markdown("### Topics")
    for index, item in enumerate(DATA):
        if st.sidebar.button(
            item["title"], key=f"menu_topic_{index}", use_container_width=True
        ):
            st.session_state.path = [index]
            st.rerun()

    node = get_node(st.session_state.path)
    children = node.get("children", []) if node else []
    if children:
        st.sidebar.divider()
        st.sidebar.markdown("### Subtopics")
        for index, child in enumerate(children):
            if st.sidebar.button(
                child["title"],
                key=f"menu_subtopic_{len(st.session_state.path)}_{index}",
                use_container_width=True,
            ):
                st.session_state.path.append(index)
                st.rerun()


def render_stage() -> None:
    st.title(APP_TITLE)
    st.subheader("Explore the Montessori Capstone Map")
    st.write("Choose a topic from the menu on the left.")


def render_node(node: dict[str, Any]) -> None:
    st.title(node["title"])

    center_text = markdown_for(node, "center")
    children = node.get("children") or []

    if center_text:
        with st.container(border=True):
            render_markdown_with_images(center_text)

    if children:
        st.info("Choose a subtopic from the menu.")
    elif not center_text:
        with st.container(border=True):
            render_markdown_with_images(markdown_for(node))


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="◯", layout="wide")
    st.markdown(
        """
        <style>
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stHeader"] {
            background-color: #FFFFFF;
            color: #111111;
        }
        [data-testid="stSidebar"] {
            background-color: #F4F6F8;
        }
        [data-testid="stAppViewContainer"] h1,
        [data-testid="stAppViewContainer"] h2,
        [data-testid="stAppViewContainer"] h3,
        [data-testid="stAppViewContainer"] p {
            color: #111111;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if "path" not in st.session_state:
        st.session_state.path = []

    render_menu()
    node = get_node(st.session_state.path)
    if node is None:
        render_stage()
    else:
        render_node(node)


if __name__ == "__main__":
    main()

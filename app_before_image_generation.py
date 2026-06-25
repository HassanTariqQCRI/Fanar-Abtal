import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FANAR_API_KEY")

st.set_page_config(page_title="Fanar Abtal", page_icon="🦸", layout="wide")

st.title("🦸 Fanar Abtal")
st.subheader("AI-Powered Personalized Islamic Storybook Generator using Fanar")

st.write(
    "Fanar Abtal helps parents create personalized Islamic storybooks that teach values, character, and tarbiyah through engaging stories."
)

with st.sidebar:
    st.header("Parent Input")

    child_name = st.text_input("Child Name", "Aisha")
    age = st.number_input("Child Age", min_value=4, max_value=18, value=5)

    value = st.selectbox(
        "Value to Teach",
        [
            "Honesty",
            "Kindness",
            "Respect for Parents",
            "Patience",
            "Helping Others",
            "Generosity",
            "Trustworthiness",
            "Love of Salah",
            "Gratitude",
            "Responsibility",
        ],
    )

    theme = st.selectbox(
        "Theme",
        [
            "Ramadan in Qatar",
            "Souq Waqif",
            "Katara Cultural Village",
            "Museum of Islamic Art",
            "School",
            "Family",
            "Mosque Visit",
            "Qatar National Day",
            "Desert Adventure",
            "Helping Neighbors",
            "Eid Celebration",
            "Community Service",
        ],
    )

    language = st.selectbox("Story Language", ["English", "Arabic"])


def call_fanar(prompt):
    if not API_KEY:
        return "Error: FANAR_API_KEY is missing in .env"

    url = "https://api.fanar.qa/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "Fanar",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=180)

        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Connection error: {e}"


def generate_storybook():
    prompt = f"""
You are Fanar Abtal.

Create a personalized Islamic children's storybook.

Child Name: {child_name}
Age: {age}
Value to Teach: {value}
Theme: {theme}
Language: {language}

Requirements:
- Child-friendly
- Warm and positive
- Include Islamic manners naturally
- Include Qatari culture when relevant
- Four short scenes
- One moral lesson
- One reflection question for parents
- Keep it concise for a hackathon demo

Output format exactly:

# Story Title

Moral:
[text]

## Scene 1: [title]
[text]

## Scene 2: [title]
[text]

## Scene 3: [title]
[text]

## Scene 4: [title]
[text]

Parent Reflection:
[text]
"""
    return call_fanar(prompt)


def generate_cover_prompt():
    prompt = f"""
Create one detailed image generation prompt for a children's Islamic storybook cover.

Child Name: {child_name}
Age: {age}
Value to Teach: {value}
Theme: {theme}

Requirements:
- Child-friendly illustration
- Islamic and culturally respectful
- Warm, bright, colorful storybook style
- Include visual elements related to the value: {value}
- Include visual elements related to the theme: {theme}
- Include gentle Qatari cultural details when relevant
- No text inside the image
- No scary or inappropriate elements

Output only the image prompt, nothing else.
"""
    return call_fanar(prompt)


def story_card(text):
    return f"""
    <div style="
        background-color:#ffffff;
        padding:28px;
        border-radius:18px;
        border:1px solid #dddddd;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
        margin-top:20px;
        margin-bottom:20px;
        line-height:1.8;
        font-size:18px;
    ">
        {text.replace(chr(10), '<br>')}
    </div>
    """


if st.button("🚀 Generate Storybook with Fanar"):
    with st.spinner("Fanar is creating the storybook..."):
        storybook = generate_storybook()

    with st.spinner("Fanar is creating the personalized cover image prompt..."):
        cover_prompt = generate_cover_prompt()

    if storybook.startswith("Error") or storybook.startswith("Connection error"):
        st.error(storybook)

    else:
        st.success("Storybook generated successfully!")

        st.markdown("## 📖 Fanar Abtal Storybook")

        try:
            st.image(
                "assets/cover/cover.jpg",
                caption="Sample Storybook Cover",
                use_container_width=True,
            )
        except:
            st.warning("Cover image not found")

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg,#fff7e6,#f5f5f5);
                padding:40px;
                border-radius:22px;
                text-align:center;
                border:2px solid #e6d8ad;
                margin-bottom:30px;
            ">
                <h1>📚 Fanar Abtal</h1>
                <h2>{child_name}'s Personalized Storybook</h2>
                <h3>Value: {value}</h3>
                <p><strong>Theme:</strong> {theme}</p>
                <p><strong>Age:</strong> {age}</p>
                <p><em>Generated with Fanar</em></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 🎨 Personalized Cover Image Prompt")
        st.markdown(story_card(cover_prompt), unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Cover Prompt",
            data=cover_prompt,
            file_name=f"{child_name}_cover_image_prompt.txt",
            mime="text/plain",
        )

        st.markdown("### 📘 Full Story")
        st.markdown(story_card(storybook), unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Story Text",
            data=storybook,
            file_name=f"{child_name}_fanar_abtal_story.txt",
            mime="text/plain",
        )

else:
    st.info(
        "Enter child details from the sidebar and click 'Generate Storybook with Fanar'."
    )
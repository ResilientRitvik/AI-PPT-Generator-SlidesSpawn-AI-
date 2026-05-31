import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="api key" 
    ,
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(
    page_title="SLIDESPAWN",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 SlidesSpawn AI")
st.caption("AI-powered presentation generator")

topic = st.text_input("Enter Presentation Topic")

slides = st.slider(
    "Number of Slides",
    3,
    15,
    5
)

presentation_type = st.selectbox(
    "Presentation Type",
    ["College", "Business", "Marketing", "Seminar"]
)

if st.button("Generate Presentation"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating slides..."):

            prompt = f"""
            Create a PowerPoint presentation.

            Topic: {topic}
            Type: {presentation_type}
            Slides: {slides}

            For each slide provide:
            - Slide title
            - 4 bullet points
            """

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            output = response.choices[0].message.content

            st.subheader("Generated PPT Content")

            st.write(output)
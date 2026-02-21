import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="BrandCraft GRNA", page_icon="🚀", layout="wide")

st.title("🚀 BrandCraft GRNA")
st.subheader("AI Brand Name & Identity Generator")

# Sidebar
st.sidebar.header("Brand Inputs")
industry = st.sidebar.text_input("Industry", placeholder="e.g. Tech, Fashion, Fitness")
target_audience = st.sidebar.text_input("Target Audience", placeholder="e.g. Gen Z, Entrepreneurs")
brand_tone = st.sidebar.selectbox(
    "Brand Tone",
    ["Modern", "Luxury", "Playful", "Minimalist", "Bold", "Futuristic"]
)

generate = st.sidebar.button("Generate Brand")

def generate_brand(industry, audience, tone):
    prompt = f"""
    Create a brand identity for a {industry} company.
    Target audience: {audience}
    Brand tone: {tone}

    Provide:
    1. Brand Name
    2. Tagline
    3. Brand Story (short)
    4. Color Palette
    5. Brand Voice Description
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert brand strategist."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=800,
    )

    return response.choices[0].message.content

# Main logic
if generate:
    if industry and target_audience:
        with st.spinner("Crafting your brand... ✨"):
            result = generate_brand(industry, target_audience, brand_tone)
        st.success("Brand Generated Successfully!")
        st.markdown(result)
    else:
        st.warning("Please fill in Industry and Target Audience.")

st.markdown("---")
st.caption("Powered by LLaMA 3.3 70B via Groq")
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")

LANGUAGES = {
    "Auto": "auto", "English": "en", "Urdu": "ur",
    "Arabic": "ar", "French": "fr", "Spanish": "es",
    "German": "de", "Chinese (Simplified)": "zh-CN",
    "Hindi": "hi", "Turkish": "tr", "Russian": "ru"
}

text_input = st.text_area("Enter text to translate:", height=150)
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language:", list(LANGUAGES.keys()))
with col2:
    target_lang = st.selectbox("Target Language:", list(LANGUAGES.keys()), index=2)

if st.button("Translate 🚀"):
    if text_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Translating..."):
            result = GoogleTranslator(
                source=LANGUAGES[source_lang],
                target=LANGUAGES[target_lang]
            ).translate(text_input)
            st.success("Translation Complete!")
            st.markdown("### Translated Text:")
            st.write(result)
            st.code(result, language="")
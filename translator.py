from googletrans import Translator
import streamlit as st

translator = Translator()
target_languages = ['English', 'Spanish', 'Arabic']
st.title('Translator')
target_text = st.text_area("Enter text here")
select_language = st.sidebar.selectbox("Select Language", target_languages)
if (select_language and target_text):
    translation = translator.translate(target_text, src='en', dest=select_language)
    st.write(translation.text)



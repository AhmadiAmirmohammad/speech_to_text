import streamlit as st
import speech_recognition as sr
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="تبدیل گفتار به متن فارسی", page_icon="🎙️")

# RTL (Right-to-Left) styling for Persion Text
st.markdown("""
<style>
body {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🎙️ تبدیل گفتار به متن فارسی")
st.write("فایل صوتی با فرمت WAV را آپلود کنید")


def transcribe_farsi_audio(audio_file):
    recognizer = sr.Recognizer()

    with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_file.write(audio_file.read())
        tmp_file_path = tmp_file.name

    with sr.AudioFile(tmp_file_path) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="fa-IR")
            return text
        except sr.UnknownValueError:
            st.error("سیستم نتوانست گفتار را تشخیص دهد")
            return None
        except sr.RequestError as e:
            st.error(f"خطا در ارتباط با سرویس: {str(e)}")
            return None


uploaded_file = st.file_uploader("فایل صوتی را انتخاب کنید", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')

    if st.button("تبدیل به متن"):
        with st.spinner("در حال پردازش..."):
            transcript = transcribe_farsi_audio(uploaded_file)

        if transcript:
            st.success("متن تبدیل شده:")
            st.text_area("متن تشخیص داده شده:", transcript, height=200)

            st.download_button(
                label="دانلود متن",
                data=transcript,
                file_name="transcript.txt",
                mime="text/plain"
            )
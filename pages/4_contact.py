import streamlit as st
st.set_page_config(page_title="RetinaVision AI - Contact", page_icon="icons/braille-solid.svg", initial_sidebar_state='collapsed')

css_title = '''
<style>
.footer-title {
    font-size: 30px;
    color: #888888;
    text-align: center;
}
</style>
'''
st.markdown(css_title, unsafe_allow_html=True)
st.markdown('<H1 class="footer-title"><i class="fa-solid fa-envelope"></i>&nbsp&nbspGet in Touch!</H1>', unsafe_allow_html=True)
st.markdown('')

contact_form = """
<form action="https://formsubmit.co/shreyasdb99@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('***')

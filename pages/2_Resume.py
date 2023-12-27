import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://norwich0-my.sharepoint.com/:b:/r/personal/tolukann_norwich_edu/Documents/Official%20Career%20Docs/Standard%20Resume/Resume%20Updated.pdf?csf=1&web=1&e=zTqSaX)")

with open("images/Resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  

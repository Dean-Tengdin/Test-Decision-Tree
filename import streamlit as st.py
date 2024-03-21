import streamlit as st
from PIL import Image


if 'display_result' not in st.session_state:
    st.session_state.display_result = False
if 'reset' not in st.session_state:
    st.session_state.reset = False

def load_image(image_path):
    # Assuming the use of PIL to load and display images
    image = Image.open(image_path)
    st.image(image, caption='', use_column_width=True)
def reset():
    st.session_state.display_result=False
    st.session_state.reset=False

def btn_1_callback():
    st.button("Resectable, nonobstructing",on_click=btn_4_callback)
    st.button("Resectable, obstructing",on_click=btn_5_callback)
    st.button("Clinical T4b or Bulky nodal disease",on_click=btn_6_callback)
    st.button("Locally unresectable or medically inoperable",on_click=btn_7_callback)
def btn_2_callback():
    st.button("Tis; T1, N0, M0; T2, N0, M0",on_click=btn_8_callback)
    st.button("T3, N0, M0q,r (no high-risk features",on_click=btn_9_callback)
    st.button("T3, N0, M0 at high risk for systemic recurrence or T4, N0, M0",on_click=btn_10_callback)
    st.button("T1–3, N1 (low-risk stage III)",on_click=btn_11_callback)
    st.button("T4, N1–2; T Any, N2 (high-risk stage III)",on_click=btn_12_callback)
def btn_3_callback():
    st.button("Synchronous liver only and/ or lung only metastases",on_click=btn_13_callback)
    st.button("Synchronous abdominal/ peritoneal metastases",on_click=btn_14_callback)
    st.button("Synchronous unresectable metastases of other sites",on_click=btn_15_callback)

def btn_4_callback():
    reset()
    st.write("Treatment: Colectomy with en bloc removal of regional lymph nodes")
def btn_5_callback():
    reset()
    st.write("Treatment: One-stage colectomyh with en bloc removal of regional lymph nodes or Resection with diversion or Diversion or Stent (in selected cases)")
def btn_6_callback():
    reset()
    st.write("Treatment: Consider neoadjuvant therapy • FOLFOX or CAPEOX")
def btn_7_callback():
    reset()
    st.write("Treatment: Systemic Therapy (COL-D) and Consider radiation therapy (RT) ± infusional 5-fluorouracil (5-FU) or capecitabine prior to surgery")
def btn_8_callback():
    reset()
    st.write("Treatment: Observation")
def btn_9_callback():
    reset()
    st.write("Treatment: Observation or Consider capecitabine (6 mo) or 5-FU/leucovorin (6 mo)")
def btn_10_callback():
    reset()
    st.write("Capecitabine (6 mo) or 5-FU/leucovorin (6 mo) or FOLFOX (6 mo) or CAPEOX (3 mo) or Observation")
def btn_11_callback():
    reset()
    st.write("Treatment: Preferred: CAPEOX (3 mo) or FOLFOX (3–6 mo) or Other options include: Capecitabine (6 mo)v or 5-FU (6 mo)")
def btn_12_callback():
    reset()
    st.write("Treatment: Preferred: CAPEOX (3–6 mo)\n or\n FOLFOX (6 mo)\n or\n Other options include: Capecitabine (6 mo) or 5-FU (6 mo)")
def btn_13_callback():
    reset()
def btn_14_callback():
    reset()
def btn_15_callback():
    reset()



button_a = st.button('Start/Restart')
if button_a :
    st.session_state.display_result = True


if st.session_state.display_result:
    reset()
    st.write("pick the type of colon cancer")
    st.button("pMMR/MSS: Findings and Primary Treatment for Colon Cancer Appropriate for Resection (Non-metastatic) (COL-3)", on_click=btn_1_callback)
    st.button("pMMR/MSS: Pathologic Stage, Adjuvant Treatment (COL-4)", on_click=btn_2_callback)
    st.button("pMMR/MSS: Findings and Treatment for Suspected or Proven Metastatic Synchronous Adenocarcinoma (COL-5)", on_click=btn_3_callback)
    



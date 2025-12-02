import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'Bungee Spice', cursive !important;
        font-size: 45px;
        text-align: center;
        color: #e7b66c !important;
    }
    .stMainBlockContainer{
        padding-top: 0rem; !important}
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    .st-emotion-cache-1gcegfv h2 {
    font-size: 1.5rem;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16px !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/chapter1/chapter1.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter1/banner1.jpg", layout="full")


    text0 = """
    <h2>Adi Parva (The Book of Beginnings)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # Chapter 1.1
    with st.expander("Chapter 1.1 – Anukramanika Parva (Preface / Introduction Parva)"):

        # Section 1.1.1
        with st.expander("Section 1.1.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.2
    with st.expander("Chapter 1.2 – Sangraha Parva (Summary Parva)"):

        # Section 1.2.1
        with st.expander("Section 1.2.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.1.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.3
    with st.expander("Chapter 1.3 – Paushya Parva (Story of King Paushya)"):

        # Section 1.3.1
        with st.expander("Section 1.3.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.3.1.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.4
    with st.expander("Chapter 1.4 – Pauloma Parva (Story of the Pauloma Demons)"):

        # Section 1.4.1
        with st.expander("Section 1.4.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.2
        with st.expander("Section 1.4.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.3
        with st.expander("Section 1.4.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.4
        with st.expander("Section 1.4.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.5
        with st.expander("Section 1.4.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.6
        with st.expander("Section 1.4.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.7
        with st.expander("Section 1.4.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.8
        with st.expander("Section 1.4.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.9
        with st.expander("Section 1.4.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.4.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.5
    with st.expander("Chapter 1.5 – Astika Parva (Story of Sage Astika)"):

        # Section 1.5.1
        with st.expander("Section 1.5.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.2
        with st.expander("Section 1.5.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.3
        with st.expander("Section 1.5.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.4
        with st.expander("Section 1.5.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.5
        with st.expander("Section 1.5.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.6
        with st.expander("Section 1.5.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.7
        with st.expander("Section 1.5.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.8
        with st.expander("Section 1.5.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.9
        with st.expander("Section 1.5.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.10
        with st.expander("Section 1.5.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.11
        with st.expander("Section 1.5.11"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.12
        with st.expander("Section 1.5.12"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.12.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.13
        with st.expander("Section 1.5.13"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.13.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.14
        with st.expander("Section 1.5.14"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.14.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.15
        with st.expander("Section 1.5.15"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.15.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.16
        with st.expander("Section 1.5.16"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.16.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.17
        with st.expander("Section 1.5.17"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.17.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.18
        with st.expander("Section 1.5.18"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.18.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.19
        with st.expander("Section 1.5.19"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.19.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.20
        with st.expander("Section 1.5.20"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.20.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.21
        with st.expander("Section 1.5.21"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.21.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.22
        with st.expander("Section 1.5.22"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.22.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.23
        with st.expander("Section 1.5.23"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.23.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.24
        with st.expander("Section 1.5.24"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.24.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.25
        with st.expander("Section 1.5.25"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.25.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.26
        with st.expander("Section 1.5.26"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.26.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.27
        with st.expander("Section 1.5.27"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.27.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.28
        with st.expander("Section 1.5.28"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.28.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.29
        with st.expander("Section 1.5.29"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.29.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.30
        with st.expander("Section 1.5.30"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.30.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.31
        with st.expander("Section 1.5.31"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.31.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.32
        with st.expander("Section 1.5.32"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.32.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.33
        with st.expander("Section 1.5.33"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.33.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.34
        with st.expander("Section 1.5.34"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.34.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.35
        with st.expander("Section 1.5.35"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.35.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.36
        with st.expander("Section 1.5.36"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.36.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.37
        with st.expander("Section 1.5.37"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.37.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.38
        with st.expander("Section 1.5.38"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.38.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.39
        with st.expander("Section 1.5.39"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.39.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.40
        with st.expander("Section 1.5.40"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.40.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.41
        with st.expander("Section 1.5.41"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.41.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.42
        with st.expander("Section 1.5.42"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.42.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.43
        with st.expander("Section 1.5.43"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.43.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.44
        with st.expander("Section 1.5.44"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.44.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.45
        with st.expander("Section 1.5.45"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.45.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.46
        with st.expander("Section 1.5.46"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.5.46.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # ============================
    # Chapter 1.6
    # ============================

    with st.expander("Chapter 1.6 – Adivansavatarana Parva (Origin of the Dynasties)"):

        with st.expander("Section 1.6.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.6.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.7
    with st.expander("Chapter 1.7 – Sambhava Parva (Birth Stories / Origins)"):

        # Section 1.7.1
        with st.expander("Section 1.7.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.2
        with st.expander("Section 1.7.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.3
        with st.expander("Section 1.7.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.4
        with st.expander("Section 1.7.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.5
        with st.expander("Section 1.7.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.6
        with st.expander("Section 1.7.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.7
        with st.expander("Section 1.7.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.8
        with st.expander("Section 1.7.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.9
        with st.expander("Section 1.7.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.10
        with st.expander("Section 1.7.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.11
        with st.expander("Section 1.7.11"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.12
        with st.expander("Section 1.7.12"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.12.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.13
        with st.expander("Section 1.7.13"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.13.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.14
        with st.expander("Section 1.7.14"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.14.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.15
        with st.expander("Section 1.7.15"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.15.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.16
        with st.expander("Section 1.7.16"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.16.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.17
        with st.expander("Section 1.7.17"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.17.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.18
        with st.expander("Section 1.7.18"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.18.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.19
        with st.expander("Section 1.7.19"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.19.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.20
        with st.expander("Section 1.7.20"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.20.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.21
        with st.expander("Section 1.7.21"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.21.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.22
        with st.expander("Section 1.7.22"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.22.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.23
        with st.expander("Section 1.7.23"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.23.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.24
        with st.expander("Section 1.7.24"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.24.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.25
        with st.expander("Section 1.7.25"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.25.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.26
        with st.expander("Section 1.7.26"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.26.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.27
        with st.expander("Section 1.7.27"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.27.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.28
        with st.expander("Section 1.7.28"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.28.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.29
        with st.expander("Section 1.7.29"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.29.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.30
        with st.expander("Section 1.7.30"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.30.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.31
        with st.expander("Section 1.7.31"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.31.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.32
        with st.expander("Section 1.7.32"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.32.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.33
        with st.expander("Section 1.7.33"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.33.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.34
        with st.expander("Section 1.7.34"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.34.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.35
        with st.expander("Section 1.7.35"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.35.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.36
        with st.expander("Section 1.7.36"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.36.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.37
        with st.expander("Section 1.7.37"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.37.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.38
        with st.expander("Section 1.7.38"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.38.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.39
        with st.expander("Section 1.7.39"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.39.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.40
        with st.expander("Section 1.7.40"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.40.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.41
        with st.expander("Section 1.7.41"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.41.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.42
        with st.expander("Section 1.7.42"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.42.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.43
        with st.expander("Section 1.7.43"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.43.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.44
        with st.expander("Section 1.7.44"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.44.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.45
        with st.expander("Section 1.7.45"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.45.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.46
        with st.expander("Section 1.7.46"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.46.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.47
        with st.expander("Section 1.7.47"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.47.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.48
        with st.expander("Section 1.7.48"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.48.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.49
        with st.expander("Section 1.7.49"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.49.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.50
        with st.expander("Section 1.7.50"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.50.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.51
        with st.expander("Section 1.7.51"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.51.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.52
        with st.expander("Section 1.7.52"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.52.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.53
        with st.expander("Section 1.7.53"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.53.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.54
        with st.expander("Section 1.7.54"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.54.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.55
        with st.expander("Section 1.7.55"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.55.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.56
        with st.expander("Section 1.7.56"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.56.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.57
        with st.expander("Section 1.7.57"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.57.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.58
        with st.expander("Section 1.7.58"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.58.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.59
        with st.expander("Section 1.7.59"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.59.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.60
        with st.expander("Section 1.7.60"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.60.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.61
        with st.expander("Section 1.7.61"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.61.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.62
        with st.expander("Section 1.7.62"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.62.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.63
        with st.expander("Section 1.7.63"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.63.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.64
        with st.expander("Section 1.7.64"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.64.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.65
        with st.expander("Section 1.7.65"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.65.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.66
        with st.expander("Section 1.7.66"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.66.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.67
        with st.expander("Section 1.7.67"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.67.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.68
        with st.expander("Section 1.7.68"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.68.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.69
        with st.expander("Section 1.7.69"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.69.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.70
        with st.expander("Section 1.7.70"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.70.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.71
        with st.expander("Section 1.7.71"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.71.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.72
        with st.expander("Section 1.7.72"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.72.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.73
        with st.expander("Section 1.7.73"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.73.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.74
        with st.expander("Section 1.7.74"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.74.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.75
        with st.expander("Section 1.7.75"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.75.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.76
        with st.expander("Section 1.7.76"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.76.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.77
        with st.expander("Section 1.7.77"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.77.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.78
        with st.expander("Section 1.7.78"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.7.78.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.8
    with st.expander("Chapter 1.8 – Jatugriha Parva (The House of Lac)"):

        # Section 1.8.1
        with st.expander("Section 1.8.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.2
        with st.expander("Section 1.8.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.3
        with st.expander("Section 1.8.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.4
        with st.expander("Section 1.8.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.5
        with st.expander("Section 1.8.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.6
        with st.expander("Section 1.8.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.7
        with st.expander("Section 1.8.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.8
        with st.expander("Section 1.8.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.9
        with st.expander("Section 1.8.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.10
        with st.expander("Section 1.8.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.11
        with st.expander("Section 1.8.11"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.8.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.9
    with st.expander("Chapter 1.9 – Hidimva-vadha Parva (Slaying of Hidimva)"):

        # Section 1.9.1
        with st.expander("Section 1.9.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.9.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.2
        with st.expander("Section 1.9.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.9.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.3
        with st.expander("Section 1.9.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.9.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.4
        with st.expander("Section 1.9.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.9.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.5
        with st.expander("Section 1.9.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.9.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.10
    with st.expander("Chapter 1.10 – Vaka-vadha Parva (Slaying of the Demon Vaka)"):

        # Section 1.10.1
        with st.expander("Section 1.10.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.2
        with st.expander("Section 1.10.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.3
        with st.expander("Section 1.10.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.4
        with st.expander("Section 1.10.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.5
        with st.expander("Section 1.10.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.6
        with st.expander("Section 1.10.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.7
        with st.expander("Section 1.10.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.8
        with st.expander("Section 1.10.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.10.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.11
    with st.expander("Chapter 1.11 – Caitraratha Parva (The Chaitraratha Episode)"):

        # Section 1.11.1
        with st.expander("Section 1.11.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.2
        with st.expander("Section 1.11.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.3
        with st.expander("Section 1.11.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.4
        with st.expander("Section 1.11.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.5
        with st.expander("Section 1.11.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.6
        with st.expander("Section 1.11.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.7
        with st.expander("Section 1.11.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.8
        with st.expander("Section 1.11.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.9
        with st.expander("Section 1.11.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.10
        with st.expander("Section 1.11.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.11
        with st.expander("Section 1.11.11"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.12
        with st.expander("Section 1.11.12"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.12.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.13
        with st.expander("Section 1.11.13"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.13.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.14
        with st.expander("Section 1.11.14"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.14.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.15
        with st.expander("Section 1.11.15"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.15.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.16
        with st.expander("Section 1.11.16"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.16.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.17
        with st.expander("Section 1.11.17"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.17.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.18
        with st.expander("Section 1.11.18"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.18.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.19
        with st.expander("Section 1.11.19"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.11.19.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.12
    with st.expander("Chapter 1.12 – Swayamvara Parva (Draupadi’s Swayamvara)"):

        # Section 1.12.1
        with st.expander("Section 1.12.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.2
        with st.expander("Section 1.12.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.3
        with st.expander("Section 1.12.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.4
        with st.expander("Section 1.12.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.5
        with st.expander("Section 1.12.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.6
        with st.expander("Section 1.12.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.7
        with st.expander("Section 1.12.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.8
        with st.expander("Section 1.12.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.12.9
        with st.expander("Section 1.12.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.12.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.13
    with st.expander("Chapter 1.13 – Vaivahika Parva (The Wedding)"):

        # Section 1.13.1
        with st.expander("Section 1.13.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.2
        with st.expander("Section 1.13.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.3
        with st.expander("Section 1.13.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.4
        with st.expander("Section 1.13.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.5
        with st.expander("Section 1.13.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.6
        with st.expander("Section 1.13.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.13.7
        with st.expander("Section 1.13.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.13.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.14
    with st.expander("Chapter 1.14 – Viduragamana Parva (Coming of Vidura)"):

        # Section 1.14.1
        with st.expander("Section 1.14.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.2
        with st.expander("Section 1.14.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.3
        with st.expander("Section 1.14.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.4
        with st.expander("Section 1.14.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.5
        with st.expander("Section 1.14.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.6
        with st.expander("Section 1.14.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.7
        with st.expander("Section 1.14.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.8
        with st.expander("Section 1.14.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.9
        with st.expander("Section 1.14.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.14.10
        with st.expander("Section 1.14.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.14.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.15
    with st.expander("Chapter 1.15 – Rajya-labha Parva (Attainment of the Kingdom)"):

        # Section 1.15.1
        with st.expander("Section 1.15.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.15.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.15.2
        with st.expander("Section 1.15.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.15.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.15.3
        with st.expander("Section 1.15.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.15.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.15.4
        with st.expander("Section 1.15.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.15.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.15.5
        with st.expander("Section 1.15.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.15.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.16
    with st.expander("Chapter 1.16 – Arjuna-vanavasa Parva (Arjuna’s Exile)"):

        # Section 1.16.1
        with st.expander("Section 1.16.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.16.2
        with st.expander("Section 1.16.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.16.3
        with st.expander("Section 1.16.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.16.4
        with st.expander("Section 1.16.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.16.5
        with st.expander("Section 1.16.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.16.6
        with st.expander("Section 1.16.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.16.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.17
    with st.expander("Chapter 1.17 – Subhadra-harana Parva (Abduction of Subhadra)"):

        # Section 1.17.1
        with st.expander("Section 1.17.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.17.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.17.2
        with st.expander("Section 1.17.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.17.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.18
    with st.expander("Chapter 1.18 – Haranaharana Parva (Return After Abduction)"):

        # Section 1.18.1
        with st.expander("Section 1.18.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.18.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.19
    with st.expander("Chapter 1.19 – Khandava-daha Parva (Burning of Khandava Forest)"):

        # Section 1.19.1
        with st.expander("Section 1.19.1"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.2
        with st.expander("Section 1.19.2"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.3
        with st.expander("Section 1.19.3"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.4
        with st.expander("Section 1.19.4"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.5
        with st.expander("Section 1.19.5"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.6
        with st.expander("Section 1.19.6"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.7
        with st.expander("Section 1.19.7"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.8
        with st.expander("Section 1.19.8"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.9
        with st.expander("Section 1.19.9"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.10
        with st.expander("Section 1.19.10"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.11
        with st.expander("Section 1.19.11"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.19.12
        with st.expander("Section 1.19.12"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.19.12.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

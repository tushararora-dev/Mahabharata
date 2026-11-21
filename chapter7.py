import streamlit as st
from app import create_image_text_layout


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
        background-color: #6969691f;
    }

    .beth1 {
            font-family: 'Beth Ellen', cursive !important;
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
    create_image_text_layout("attached_assets/chapter7/chapter7.jpg", layout="full")

    text0 = """
    <h2>Book 7 - Drona Parva</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # ==================================================
    # Chapter 7.1 - Dronabhisheka Parva
    # ==================================================

    with st.expander("Chapter 7.1  Dronabhisheka Parva"):
        sections = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
                    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"]
        section_text = {
            1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
            11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
            21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: ""
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.1.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.2 - Abhimanyu-badha Parva
    # ==================================================

    with st.expander("Chapter 7.2  Abhimanyu-badha Parva"):
        sections = ["XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
                    "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
                    "LI", "LII", "LIII", "LVI", "LVII", "LVIII", "LIX", "LX", "LXI", "LXII",
                    "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX", "LXXI", "LXXII",
                    "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", "LXXX", "LXXXI",
                    "LXXXII", "LXXXIII", "LXXXIV"]
        section_text = {
            1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
            11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
            21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: "",
            31: "", 32: "", 33: "", 34: "", 35: "", 36: "", 37: "", 38: "", 39: "", 40: "",
            41: "", 42: "", 43: "", 44: "", 45: "", 46: "", 47: "", 48: "", 49: "", 50: "",
            51: "", 52: "", 53: "", 54: ""
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.2.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.3 - Jayadratha-Vadha Parva
    # ==================================================

    with st.expander("Chapter 7.3  Jayadratha-Vadha Parva"):
        sections = ["LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX", "XC", "XCI", "XCII", "XCIII", "XCIV",
                    "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", "C", "CI", "CII", "CIII", "CIV",
                    "CV", "CVI", "CVII", "CVIII", "CIX", "CX", "CXI", "CXII", "CXIII", "CXIV",
                    "CXV", "CXVI", "CXVII", "CXVIII", "CXIX", "CXX", "CXXI", "CXXII", "CXXII", "CXXIV",
                    "CXXV", "CXXVI", "CXXVII", "CXXVIII", "CXXIX", "CXXX", "CXXXI", "CXXXII", "CXXXIII", "CXXXIV",
                    "CXXXV", "CXXXVI", "CXXXVII", "CXXXVIII", "CXXXIX", "CXL", "CXLI", "CXLII", "CXLIII", "CXLIV",
                    "CXLV", "CXLVI", "CXLVII", "CXLVIII", "CXLIX", "CI", "CLI"]
        section_text = {
            1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
            11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
            21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: "",
            31: "", 32: "", 33: "", 34: "", 35: "", 36: "", 37: "", 38: "", 39: "", 40: "",
            41: "", 42: "", 43: "", 44: "", 45: "", 46: "", 47: "", 48: "", 49: "", 50: "",
            51: "", 52: "", 53: "", 54: "", 55: "", 56: "", 57: "", 58: "", 59: "", 60: "",
            61: "", 62: "", 63: "", 64: "", 65: "", 66: "", 67: ""
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.3.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.4 - Ghatotkacha-badha Parva
    # ==================================================

    with st.expander("Chapter 7.4  Ghatotkacha-badha Parva"):
        sections = ["CLII", "CLIII", "CLIV", "CLV", "CLVI", "CLVII", "CLVIII", "CLIX", "CLX", "CLXI",
                    "CLXII", "CLXIII", "CLXIV", "CLXV", "CLXVI", "CLXVII", "CLXVIII", "CLXIX", "CLXX", "CLXXI",
                    "CLXXII", "CLXXIII", "CLXXIV", "CLXXV", "CLXXVI", "CLXXVII", "CLXXVIII", "CLXXIX", "CLXXX",
                    "CLXXXI", "CLXXXII", "CLXXXIII"]
        section_text = {
            1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
            11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", 20: "",
            21: "", 22: "", 23: "", 24: "", 25: "", 26: "", 27: "", 28: "", 29: "", 30: "",
            31: "", 32: ""
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.4.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.5 - Drona-vadha Parva
    # ==================================================

    with st.expander("Chapter 7.5  Drona-vadha Parva"):
        sections = ["CLXXXIV", "CLXXXV", "CLXXXVI", "CLXXXVII", "CLXXXVIII", "CXC", "CXCI", "CXCII", "CXCIII",
                    "CXCIV", "CXCV", "CXCVI", "CXCVII", "CXCVIII", "CXCIX", "CC", "CCI", "CCII"]
        section_text = {
            1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
            11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: ""
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.5.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")
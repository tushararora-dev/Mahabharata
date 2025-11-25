# app.py
import streamlit as st
import importlib.util
import os
from pathlib import Path
import base64
import streamlit.components.v1 as components
# Clear all cached data
st.cache_data.clear()
import math

def create_image_text_layout(image_path=None, text_content=None, layout="full", image_position="left"):
    """Reusable layout for image + text blocks"""
    if layout == "full":
        if image_path:
            st.image(image_path, use_container_width=True)
        if text_content:
            st.markdown(text_content, unsafe_allow_html=True)
    elif layout == "side":
        if image_position == "left":
            col1, col2 = st.columns([1, 2])
        else:
            col1, col2 = st.columns([2, 1])
        with col1:
            if image_position == "left" and image_path:
                st.image(image_path, use_container_width=True)
            elif image_position == "right" and text_content:
                st.markdown(text_content, unsafe_allow_html=True)
        with col2:
            if image_position == "left" and text_content:
                st.markdown(text_content, unsafe_allow_html=True)
            elif image_position == "right" and image_path:
                st.image(image_path, use_container_width=True)


def load_chapter_content(chapter_num):
    """Load content from chapter file"""
    try:
        chapter_file = f"chapter{chapter_num}.py"
        if os.path.exists(chapter_file):
            spec = importlib.util.spec_from_file_location(f"chapter{chapter_num}", chapter_file)
            if spec is not None and spec.loader is not None:
                chapter_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(chapter_module)
                return chapter_module
        return None
    except Exception:
        return None


def display_chapter_content(chapter_module, chapter_num):
    """Display chapter content with custom layouts if available"""
    if chapter_module is None:
        st.markdown(f'<div class="justified-text">Stay tuned ... Chapter {chapter_num}  will be released soon ...</div>', unsafe_allow_html=True)
        return
    try:
        if hasattr(chapter_module, 'display_content'):
            chapter_module.display_content()
        elif hasattr(chapter_module, 'get_content'):
            content = chapter_module.get_content()
            st.markdown(f'<div class="justified-text">{content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="justified-text">No content available for Chapter {chapter_num}.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="justified-text">Error displaying Chapter {chapter_num}: {str(e)}</div>', unsafe_allow_html=True)


def display_home(chapter_names):

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

        h2 {
            font-family: 'Bungee Spice', cursive !important;
            font-size: 25px !important;
            color: #e7b66c !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Main image with vignette
    img_path = "attached_assets/main.jpg"
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            img_bytes = f.read()
            encoded = base64.b64encode(img_bytes).decode()
        st.markdown(
            f"""
            <div class="vignette-image">
                <img src="data:image/jpg;base64,{encoded}" style="width:100%; display:block; border-radius: 10px;"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("🛠️ Working on it...")


    st.markdown(" ## Chapters:")

    # ---------------------------
    # Chapter 1 (manual)
    # ---------------------------
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img_path = "attached_assets/chapter1/chapter1.jpg"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.markdown("🛠️ Working on it...")

    with col2:
        st.markdown(" ## Book 1 - Adi Parva")
    with col3:
        st.markdown(
            '<a href="?chapter=1#top" target="_self" '
            'style="display:inline-block;padding:10px 14px;border-radius:8px;'
            'border:2px solid orange;color:oldlace;background:#0D0B1A;'
            'text-decoration:none;">Read More ▶</a>',
            unsafe_allow_html=True
        )


  

def main():
    # Page configuration
    st.set_page_config(page_title="Mahabharata", page_icon="🏹", layout="wide")



    # Auto-scroll to top if viewing a chapter (not home)
    if st.session_state.get("selected_chapter") != "home":
        st.markdown("""
            <script>
            window.onload = function() {
                window.scrollTo({top: 0, behavior: "instant"});
            };
            </script>
        """, unsafe_allow_html=True)

    # Put a top anchor so #top works
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)

    # -----------------------
    # Handle URL query params + session state
    # -----------------------
    if "selected_chapter" not in st.session_state:
        st.session_state.selected_chapter = "home"

    params = st.query_params

    # Deep-link: /?chapter=3 loads Chapter 3 from the top
    ch = params.get("chapter")
    if ch:
        try:
            ch_num = int(ch)
            if 1 <= ch_num <= 7:
                st.session_state.selected_chapter = ch_num
        except:
            pass  # ignore bad values

    # Keep your existing 'nav' handling if you still want it
    nav = params.get("nav")
    if nav and isinstance(st.session_state.selected_chapter, int):
        if nav == "prev" and st.session_state.selected_chapter > 1:
            st.session_state.selected_chapter -= 1
        elif nav == "next" and st.session_state.selected_chapter < 11:
            st.session_state.selected_chapter += 1
        st.query_params.clear()

    # -----------------------
    # Sidebar styling + nav
    # -----------------------
    # Load PNG and convert to base64
    with open("bow.png", "rb") as f:
        img_bytes = f.read()
    b64_cursor = base64.b64encode(img_bytes).decode()

    # Inject CSS
    # Inject CSS
    st.markdown(f"""
    <style>      

    /* Apply custom cursor everywhere */
    *, body, html {{
        cursor: url("data:image/png;base64,{b64_cursor}") 16 16, auto !important;
    }}

    /* Force it even on interactive elements */
    button, a, div, span, input, textarea, [role="button"] {{
        cursor: url("data:image/png;base64,{b64_cursor}") 16 16, auto !important;
    }}
    </style>
    """, unsafe_allow_html=True)


    st.sidebar.markdown("""
    <style>
    [data-testid="stSidebar"] .stButton > button {
        justify-content: flex-start !important;
        text-align: left !important;
                        
    }
    [data-testid="stSidebar"] .stButton > button > div {
        width: 100%;
        text-align: left !important;
    }
    [data-testid="stSidebar"] .stButton > button[kind="primary"]{
        background: #0D0B1A !important;
        color: #f3a900 !important;
        border: 2px solid #e7b66c !important;
                    
        
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown(
    """
    <style>
    /* Set sidebar width */
    [data-testid="stSidebar"] {
        width: 400px !important;  /* Change this to your desired width */
    }

    /* Optional: adjust main content margin when sidebar width changes */
    [data-testid="stMainContent"] {
        margin-left: 400px !important;  /* slightly larger than sidebar width */
    }
    </style>
    """,
    unsafe_allow_html=True
    )






    st.sidebar.image("Lord1.gif", use_container_width=True)

    chapter_names = {
        1: "Adi Parva (The Book of Beginnings)",
        2: "Sabha Parva (The Book of the Assembly Hall)",
        3: "Vana Parva / Aranyaka Parva (The Book of the Forest)",
        4: "Virata Parva (The Book of Virata)",
        5: "Udyoga Parva (The Book of Effort/Preparation)",
        6: "Bhishma Parva (The Book of Bhishma)",
        7: "Drona Parva (The Book of Drona)",
        8: "Karna Parva (The Book of Karna)",
        9: "Shalya Parva (The Book of Shalya)",
        10: "Sauptika Parva (The Book of the Sleepers)",
        11: "Stri Parva (The Book of the Women)",
        12: "Shanti Parva (The Book of Peace)",
        13: "Anushasana Parva (The Book of Instructions)",
        14: "Ashvamedhika Parva (The Book of the Horse Sacrifice)",
        15: "Ashramavasika Parva (The Book of Hermitage Life)",
        16: "Mausala Parva (The Book of the Clubs)",
        17: "Mahaprasthanika Parva (The Great Journey)",
        18: "Svargarohana Parva (The Ascent to Heaven)",
    }

    # -----------------------
    # Sidebar chapter links (real navigation)
    # -----------------------
    for i in range(1, 19):
        active = (i == st.session_state.selected_chapter)
        target = "_self"  # change to "_blank" if you want new tab
        base = "display:block;width:100%;padding:10px 12px;border-radius:10px;text-decoration:none;margin-bottom:8px;"
        if active:
            style = base + "background:#0D0B1A;color:seashell;border:2px solid #f3a900; "
        else:
            style = base + "background:transparent;color:seashell;border:1px solid rgb(68, 68, 68) ; "
        st.sidebar.markdown(
            f'<a href="?chapter={i}#top" target="{target}" style="{style}">Chapter {i}: {chapter_names[i]}</a>',
            unsafe_allow_html=True
        )



    # -----------------------
    # Title + fonts
    # -----------------------
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap');
        @import url('https://fonts.googleapis.com/css2?famiily=Beth+Ellen&display=swap');

        .stApp h1 {
            font-family: 'Bungee Spice' !important;
            font-size: 100px !important;
            color: #fc7423 !important;
            text-align: center !important;
            letter-spacing: 2px !important;
        }
        p { 
            font-size: 18px !important;
            line-height: 1.6 !important;
            text-align: justify !important;
                
            color: oldlace;
        }
        .beth {
            font-family: 'Beth Ellen' !important;
            font-size: 20px;
            text-align: center;
            color: lightslategray !important;
            margin-top: 0.2em;
        }

        /* Smooth anchor scrolling */
        html {
            scroll-behavior: smooth !important;
        }

        /* -------- Responsive font sizes -------- */
        @media (max-width: 768px) {   /* tablets & small devices */
            .stApp h1 {
                font-size: 45px !important;
                text-align: center !important;
            }
            .beth {
                font-size: 18px !important;
            }
        }

        @media (max-width: 480px) {   /* mobile phones */
            .stApp h1 {
                font-size: 45px !important;
                text-align: center !important;
            }

            .beth {
                font-size: 16px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)


    st.title("Ramayana")
    st.markdown("<div class='beth' >- Tushar Arora Edition<br><br></div>", unsafe_allow_html=True)

    # -----------------------
    # Load & show chapter
    # -----------------------
    if st.session_state.selected_chapter == "home":
        display_home(chapter_names)
    else:
        chapter_num = int(st.session_state.selected_chapter)

        # Load & show chapter
        chapter_module = load_chapter_content(chapter_num)
        display_chapter_content(chapter_module, chapter_num)

        left, right = st.columns([1,1])
        with left:
            if chapter_num > 1:
                st.markdown(
                    f'<a href="?chapter={chapter_num-1}#top" target="_self" '
                    'style="display:inline-block;padding:10px 14px;border-radius:8px;'
                    'border:2px solid orange;color:oldlace;background:#0D0B1A;'
                    'text-decoration:none;">◀ Previous Chapter</a>',
                    unsafe_allow_html=True
                )
        with right:
            if chapter_num < 7:
                st.markdown(
                    f'<a href="?chapter={chapter_num+1}#top" target="_self" '
                    'style="display:inline-block;padding:10px 14px;border-radius:8px;'
                    'border:2px solid orange;color:oldlace;background:#0D0B1A;'
                    'text-decoration:none;">Next Chapter ▶</a>',
                    unsafe_allow_html=True
                )



    
    st.markdown(
        """
        <style>
        /* Wrap the whole form in a styled div */
        div[data-testid="stForm"] {
            border: 2px solid orange;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        # /* Form border */
        # div[data-testid="stForm"] {
        #     border: 2px solid orange;
        #     border-radius: 10px;
        #     padding: 20px;
        #     margin-bottom: 20px;
        # }

        # /* Submit button border */
        # div.stButton > button {
        #     border: 2px solid orange !important;
        #     border-radius: 8px;
        #     background-color: white;
        #     color: orange;
        #     font-weight: bold;
        #     padding: 0.5em 1em;
        # }

        # /* Hover effect */
        # div.stButton > button:hover {
        #     background-color: orange;
        #     color: white;
        # }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Leave a Review")
    with st.form("review_form"):
        name = st.text_input("Your Name")
        review = st.text_area("Your Review about this story")
        submitted = st.form_submit_button("Submit Review")

        if submitted:
            if name.strip() == "" or review.strip() == "":
                st.error("Please fill out both fields before submitting.")
            else:
                from google_sheets import add_review
                add_review(name, review, st.session_state.selected_chapter)
                st.success("✅ Thank you! Your review has been saved.")



    st.markdown("""
    <style>
    html {
        scroll-behavior: smooth;
    }
    .scroll-buttons {
        position: fixed;
        bottom: 60px;
        right: 20px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        z-index: 9999;
    }
    .scroll-btn {
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:48px;
        height:48px;
        border-radius:50%;
        background:#0d0b1acc;
        color:orange !important;
        border:2px solid orange;
        text-decoration:none !important;
        transition: all 0.3s ease;
    }

    .scroll-btn:hover {
        # background:orange !important;
        # color:orange !important;
    }
    .scroll-btn svg {
        width:24px;
        height:24px;
        fill:currentColor;
    }
    </style>

    <div id="top"></div>

    <div class="scroll-buttons" aria-hidden="true">
        <a class="scroll-btn" href="?chapter=home#top" title="Go to Home">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M3 9.5l9-7 9 7V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1V9.5z"/>
            </svg>
        </a>
        <a class="scroll-btn" href="#top" title="Scroll to top">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 4l-8 8h6v8h4v-8h6z"/>
            </svg>
        </a>
        <a class="scroll-btn" href="#bottom" title="Scroll to bottom">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 20l8-8h-6V4h-4v8H4z"/>
            </svg>
        </a>
    </div>

    <div id="bottom"></div>
    """, unsafe_allow_html=True)

    # Force scroll to top on each render
    st.markdown("""
        <script>
        window.addEventListener('load', function() {
            window.scrollTo(0, 0);
        });
        </script>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

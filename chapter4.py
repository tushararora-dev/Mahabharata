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
    create_image_text_layout("attached_assets/chapter4/chapter4.jpg", layout="full")


    text0 = """
    <h2>Book 4 - Virata Parva</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    # ==================================================
    # Chapter 4.1 - Pandava-Pravesa Parva
    # ==================================================

    with st.expander("Chapter 4.1  Pandava-Pravesa Parva"):

        # Section 4.1.1
        with st.expander("Section 4.1.1  Section I"):
            text1 = """ 
            Rishi Vaisampayana bole, “Jab Yudhishthira ne dharm ke vardaan se Yaksha ke pareeksha ko poora kiya aur apne bhaiyon ke saath Brahmano ko sab kuch bataya, tab unhone Brahmana ko uski churning staff aur agni ki lakdiyaan wapas de di. Phir Yudhishthira ne apne sab bhaiyon ko bulaya aur kaha:

‘Hum rajya se vanvaas mein rahe aur baarah saal beet gaye. Ab terahva saal, jo sabse kathin hai, shuru ho gaya hai. Arjuna, tum kuch aisi jagah batao jahan hum apne dushmano se bina pehchaane reh saken.’

Arjuna ne kaha, ‘Dharm ke vardaan se hum bina kisi ko pata chale kahin bhi ghoom sakte hain. Lekin rehne ke liye kuch sundar aur alag jagah batata hoon. Kuru rajya ke aaspaas bahut desh hain — Pancala, Chedi, Matsya, Surasena, Pattaccara, Dasarna, Navarashtra, Malla, Salva, Yugandhara, Saurashtra, Avanti aur Kuntirashtra. Kaunsa chuno aur kahaan hum is saal bitayenge?’"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yudhishthira ne kaha, ‘Arjuna, jo bhi Ishwar ne kaha, wahi sach hoga. Hum sab milkar ek sundar aur shubh sthaan chune. Matsya ke raja Virata buddhi aur dharm ke maalik hain, sabko unka prem hai aur woh humse bhi jude hue hain. Isliye Virata ke rajya mein hi hum is saal rahenge. Ab batao ki tum log Virata ke saamne kis roop mein apna pradarshan karoge.’

Arjuna ne poocha, ‘Bhaiya, tum Virata ke rajya mein kaun si seva karoge? Tum wahan kaise rahoge? Tum sab vinamra, dharm ke palak, aur satyavadi ho. Tumhe aayi hui musibat kaise door karoge?’

Yudhishthira ne kaha, ‘Tum sab, Vrikodara, dhyan se suno. Main apne aap ko Brahmana Kanka ke roop mein dikhaunga, jo paasa khelna jaanta hai aur shatranj mein bhi mahir hai. Main rajya ke sabhi logon ko manoranjan karunga. Is roop mein main bina kisi ko pata chale raja ke paas rahunga. Agar raja pooche, toh main kahunga, “Main pehle Yudhishthira ka mitra tha.” Is tarah main Virata ke rajya mein apna jeevan bitaoonga. Vrikodara, tum Virata ke rajya mein kaun si seva karoge?’"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.2
        with st.expander("Section 4.1.2  Section II"):
            text1 = """ 
            Bhima ne kaha,

“Main Virata ke rajya mein Vallabha naam ka rasoiya banunga. Mujhe bahut achcha bhojan banana aata hai. Main raja ke liye swadisht khaana banaunga aur sabhi purane rasoiyon se behtar kaam karunga.”

“Main bade-bade lakdi ke bojh bhi aasani se utha lunga. Yeh dekhkar raja bahut khush honge.”

Bhima muskuraakar bole, “Main haathi aur saand jaise balwaan jaanwaron ko bhi sambhaal sakta hoon. Agar koi pehelwan mujhse ladna chahe, toh main use hara dunga.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Lekin main kisi ko maarunga nahi. Sirf itna haraunga ki sab log manoranjan ka aanand le saken.”

“Aur agar koi mere baare mein poochega, toh main kahunga ki main pehle Yudhishthira ka rasoiya aur pehelwan tha.”

Yudhishthira ne phir Arjuna ki taraf dekha aur bole,

“Arjuna jaisa mahaan dhanurdhari duniya mein mushkil se koi hoga. Woh Indra ke samaan veer hai. Batao, Virata ke rajya mein woh kaunsa kaam karega?”

Arjuna ne shaant swar mein jawab diya,

“Hey Raja, main Brihannala naam se ek napunsak ka roop dharan karunga.”

“Dhanush chalane ke nishaan mere haathon par hain, isliye main unhe choodiyon se chhupa lunga.”

“Main kaan mein kundal pehnunga, baalon ki choti banaunga aur stri jaise vastra pehnkar rahunga.”

“Main Virata ke mahal ki mahilaon ko gaan, nritya aur sangeet sikhaunga.”

“Main kahaniyaan sunaakar aur manoranjan karke sabko khush rakhunga.”

“Yadi raja poochhenge, toh main kahunga ki main pehle Draupadi ki seva mein tha.”

“Is tarah main apni asli pehchaan chhupa kar Virata ke mahal mein aaram se reh lunga.”

Rishi Vaisampayana bole, “Yeh sab kehkar Arjuna chup ho gaye. Tab Yudhishthira ne apne doosre bhai ki taraf dekha aur usse poocha ki woh kaunsa roop dharan karega.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.3
        with st.expander("Section 4.1.3  Section III"):
            text1 = """ 
            Yudhishthira ne Nakula se poocha,

“Hey Nakula, tum bahut sundar, komal aur rajkumar jaise ho. Virata ke rajya mein tum kaunsa kaam karoge?”

Nakula ne vinamrata se jawab diya,

“Main Granthika naam se Raja Virata ke ghodon ki dekhbhaal karunga.”

“Mujhe ghodon ki training aur unki seva ka bahut achcha gyaan hai. Main unhe shaant aur mazboot bana sakta hoon.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Ghodon se mujhe bahut prem hai. Main pehle bhi aapke ghodon ki dekhbhaal karta tha.”

“Agar koi poochega, toh main kahunga ki main pehle Raja Yudhishthira ke yahan ghodon ka rakhwala tha.”

“Is tarah main bina pehchaane Virata ke rajya mein reh lunga.”

Phir Yudhishthira ne Sahadeva se poocha,

“Hey Sahadeva, tum kaunsa roop dharan karoge?”

Sahadeva bole,

“Main Tantripal naam se gaayon ki dekhbhaal karunga.”

“Mujhe gaayon ki seva, doodh nikaalne aur unki prakriti samajhne ka bahut gyaan hai.”

“Main pehle bhi aapki gaayon ka dhyaan rakhta tha.”

“Mujhe pata hai kaunsi gaay ya saand shubh hote hain. Main is kaam ko bahut achchi tarah kar sakta hoon.”

“Isliye mujhe koi pehchaan nahi paayega aur Raja Virata bhi mujhse khush rahenge.”

Yeh sunkar Yudhishthira ne Draupadi ki taraf dekha aur dukhi swar mein bole,

“Yeh hamari priya Draupadi hai, jo humein apni jaan se bhi zyada pyari hai.”

“Yeh ek mahaan rajkumari hai. Isne hamesha sundar vastra, phool aur sugandh mein jeevan bitaya hai.”

“Yeh kisi saadharan kaam ki aadat nahi rakhti. Virata ke mahal mein yeh kaise rahegi?”

Draupadi ne shaant aur himmat bhare swar mein kaha,

“Main Sairindhri naam ki dasi ka roop dharan karungi.”

“Mujhe baal sajaane aur raniyon ki seva karna aata hai.”

“Main Raja Virata ki patni Sudeshna ki seva karungi.”

“Agar koi poochega, toh main kahungi ki main pehle Draupadi ki seva mein thi.”

“Is tarah main chupkar apna samay bita lungi. Aap chinta mat kijiye.”

Yudhishthira bole,

“Hey Krishnaa, tumne bahut samajhdari ki baat kahi.”

“Lekin tum bahut sundar aur pavitra ho. Dhyaan rakhna ki koi dusht ya bure mann wala vyakti tumhe pareshan na kare.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.4
        with st.expander("Section 4.1.4  Section IV"):
            text1 = """ 
            Yudhishthira ne sab bhaiyon se kaha,

“Hum sabne tai kar liya hai ki Virata ke rajya mein kaunsa kaam karenge.”

“Ab hamare purohit Dhaumya ji Brahmano, rath chalane waalon aur rasoiyon ke saath Raja Drupada ke paas chale jaayenge aur hamare pavitra yagya ki agni ka dhyaan rakhenge.”

“Indrasena aur doosre log khaali rath lekar Dwaraka chale jaayenge.”

“Draupadi ki sab dasiyan bhi Panchal desh chali jaayengi.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Sab log bas itna kahenge ki Pandav Dwaitavan ke paas humein chhodkar kahin chale gaye aur humein nahi pata woh kahan hain.”

Rishi Vaisampayana bole, “Sabne milkar yeh yojana banaayi aur phir Dhaumya rishi se salah maangi.”

Dhaumya ne gambhir swar mein kaha,

“Hey Pandavo, tumne bahut samajhdari se sab vyavastha ki hai.”

“Lekin Virata ke mahal mein rehna aasaan nahi hoga. Raja ke saath rehte waqt bahut saavdhaan rehna padta hai.”

Phir Dhaumya ne unhe bahut si seekh di.

Woh bole, “Raja ke paas bina anumati ke nahi jaana chahiye.”

“Raja ke raaz kisi ko nahi batane chahiye.”

“Zyada bolna ya bina pooche salah dena theek nahi hota.”

“Raja ki patniyon ya un logon se dosti nahi karni chahiye jinse raja naraaz ho.”

“Hammesha vinamr aur saavdhaan rehna chahiye.”

“Raja ke saamne zyada hansna, gussa karna ya ghamand dikhana achcha nahi hota.”

“Jo vyakti raja ki bhalai chahta hai aur imaandari se seva karta hai, wahi rajmahal mein surakshit reh sakta hai.”

Dhaumya ne aur bhi kaha,

“Raja se kabhi jhooth ya chhal nahi karna.”

“Raja ke dushmano se dosti nahi karni.”

“Raja ke diye hue vastra aur uphaar ka samman karna.”

“Apne mann ko shaant aur niyantrit rakhna.”

“Is ek saal ko dhairya aur buddhi se poora kar lo. Phir tum apna rajya wapas paa loge.”

Yudhishthira ne haath jodkar kaha,

“Hey Dhaumya ji, aapne humein bahut achchi seekh di. Hamari maa Kunti aur buddhimaan Vidura ke alawa shayad hi koi humein itni achchi baat samjha sakta tha.”

“Ab kripya hamari yatra aur suraksha ke liye jo bhi zaroori ho, woh kariye.”

Rishi Vaisampayana bole, “Phir Dhaumya ne vidhi ke anusaar havan aur pooja ki.”

Unhone Pandavo ki suraksha aur vijay ke liye pavitra mantron se agni mein ahuti di.

Uske baad Pandav aur Draupadi Brahmano ko pranam karke Virata nagari ki taraf chal pade.

Dhaumya pavitra yagya ki agni lekar Panchal chale gaye.

Indrasena aur doosre sevak Dwaraka aur anya sthalon par chale gaye aur Pandavo ke rath aur ghodon ka dhyaan rakhne lage."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.5
        with st.expander("Section 4.1.5  Section V"):
            text1 = """ 
            Rishi Vaisampayana bole, “Pandav apni talwarein, dhanush aur hathiyaar lekar Yamuna nadi ki taraf chale. Bahut saalon tak jungle aur pahaadon mein rehne ke baad ab woh Virata nagari ki taraf badh rahe the.

Raaste mein woh shikariyon jaise kapde pehenkar chal rahe the, taaki koi unhe pehchaan na sake.

Jab woh Matsya desh ke paas pahunche, tab Draupadi ne thak kar Yudhishthira se kaha,

“Humein yahaan aas-paas kheton aur raaston ke nishaan dikh rahe hain. Lagta hai Virata ki nagari ab zyada door nahi hai. Main bahut thak gayi hoon.”

Yudhishthira ne Arjuna se kaha,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Hey Dhananjaya, tum Draupadi ko uthakar le chalo. Jungle ke baahar hi nagari aa jaayegi.”

Arjuna ne turant Draupadi ko utha liya aur haathi ke raja ki tarah mazboot kadmon se aage badhne lage.

Nagari ke paas pahunchkar Yudhishthira ne chinta bhare swar mein kaha,

“Hum apne hathiyaar kahaan chhupaayenge? Agar hum inhe lekar nagar mein gaye, toh log humein pehchaan sakte hain. Gandiva dhanush toh poori duniya jaanti hai.”

“Yadi hum mein se ek bhi pehchaan liya gaya, toh humein fir se baarah saal vanvaas jhelna padega.”

Arjuna ne aas-paas dekhkar kaha,

“Wahan dekho, shamshaan ke paas ek bada Sami ka ped hai. Woh bahut ooncha aur sunsaan jagah par hai. Wahan koi aasaani se nahi jaayega.”

“Hum apne hathiyaar wahin chhupa dete hain.”

Phir sab Pandavo ne apne dhanushon ki dor khol di.

Arjuna ne apna mahaan Gandiva sambhaal kar rakha. Bhima, Yudhishthira, Nakula aur Sahadeva ne bhi apne dhanush, talwarein aur teer ek saath baandh diye.

Nakula ped par chadh gaye aur sab hathiyaar sambhaal kar aisi jagah chhupa diye jahan baarish bhi na pahunch sake.

Phir Pandavo ne ek murda shareer us ped par latka diya, taaki log badboo se door rahen aur ped ke paas na aayein.

Jab gaay charaane waalon aur charwaahon ne poocha, “Yeh kya hai?”

Tab Pandavo ne kaha,

“Yeh hamari bahut buddhi maa ka shareer hai. Hamare kul mein isi tarah antim sanskaar ki parampara hai.”

Yeh sunkar sab log door hi rahe.

Uske baad Pandavo ne apne naye gupt naam bhi rakhe.

Yudhishthira ka naam Jaya, Bhima ka Jayanta, Arjuna ka Vijaya, Nakula ka Jayatsena aur Sahadeva ka Jayadbala rakha gaya.

Phir woh sab Virata nagari mein chupkar rehne ke liye pravesh kar gaye, taaki apna terahva saal bina pehchaane poora kar saken."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.6
        with st.expander("Section 4.1.6  Section VI"):
            text1 = """ 
            """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.7
        with st.expander("Section 4.1.7  Section VII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.8
        with st.expander("Section 4.1.8  Section VIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.9
        with st.expander("Section 4.1.9  Section IX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.10
        with st.expander("Section 4.1.10  Section X"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.11
        with st.expander("Section 4.1.11  Section XI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.12
        with st.expander("Section 4.1.12  Section XII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.1.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


    # ==================================================
    # Chapter 4.2 - Samayapalana Parva
    # ==================================================

    with st.expander("Chapter 4.2  Samayapalana Parva"):

        # Section 4.2.1
        with st.expander("Section 4.2.1  Section XIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


    # ==================================================
    # Chapter 4.3 - Kicaka-badha Parva
    # ==================================================

    with st.expander("Chapter 4.3  Kicaka-badha Parva"):

        # Section 4.3.1
        with st.expander("Section 4.3.1  Section XIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.2
        with st.expander("Section 4.3.2  Section XV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            
                # Section 4.3.3
        with st.expander("Section 4.3.3  Section XVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.4
        with st.expander("Section 4.3.4  Section XVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.5
        with st.expander("Section 4.3.5  Section XVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.6
        with st.expander("Section 4.3.6  Section XIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.7
        with st.expander("Section 4.3.7  Section XX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.8
        with st.expander("Section 4.3.8  Section XXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.9
        with st.expander("Section 4.3.9  Section XXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.10
        with st.expander("Section 4.3.10  Section XXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.11
        with st.expander("Section 4.3.11  Section XXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.12
        with st.expander("Section 4.3.12  Section XXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.3.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


    # ==================================================
    # Chapter 4.4 - Goharana Parva
    # ==================================================

    with st.expander("Chapter 4.4  Goharana Parva"):

        # Section 4.4.1
        with st.expander("Section 4.4.1  Section XXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.2
        with st.expander("Section 4.4.2  Section XXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.3
        with st.expander("Section 4.4.3  Section XXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.4
        with st.expander("Section 4.4.4  Section XXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.5
        with st.expander("Section 4.4.5  Section XXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 4.4.6
        with st.expander("Section 4.4.6  Section XXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.7
        with st.expander("Section 4.4.7  Section XXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.8
        with st.expander("Section 4.4.8  Section XXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.9
        with st.expander("Section 4.4.9  Section XXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.10
        with st.expander("Section 4.4.10  Section XXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.11
        with st.expander("Section 4.4.11  Section XXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.12
        with st.expander("Section 4.4.12  Section XXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.13
        with st.expander("Section 4.4.13  Section XXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.14
        with st.expander("Section 4.4.14  Section XXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.15
        with st.expander("Section 4.4.15  Section XL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.16
        with st.expander("Section 4.4.16  Section XLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.17
        with st.expander("Section 4.4.17  Section XLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.18
        with st.expander("Section 4.4.18  Section XLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.19
        with st.expander("Section 4.4.19  Section XLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.20
        with st.expander("Section 4.4.20  Section XLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 4.4.21
        with st.expander("Section 4.4.21  Section XLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.22
        with st.expander("Section 4.4.22  Section XLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.23
        with st.expander("Section 4.4.23  Section XLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.24
        with st.expander("Section 4.4.24  Section XLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.25
        with st.expander("Section 4.4.25  Section L"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.26
        with st.expander("Section 4.4.26  Section LI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.27
        with st.expander("Section 4.4.27  Section LII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.28
        with st.expander("Section 4.4.28  Section LIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.29
        with st.expander("Section 4.4.29  Section LIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.30
        with st.expander("Section 4.4.30  Section LV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.31
        with st.expander("Section 4.4.31  Section LVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.32
        with st.expander("Section 4.4.32  Section LVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.33
        with st.expander("Section 4.4.33  Section LVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.34
        with st.expander("Section 4.4.34  Section LIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.35
        with st.expander("Section 4.4.35  Section LX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter4/4.4.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
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
            Rishi Vaisampayana bole, “Jab Pandav Virata nagari ki taraf ja rahe the, tab Yudhishthira ne mann hi mann Devi Durga ka smaran kiya.

Unhone Devi ko pranam karte hue kaha,

‘Hey Devi Durga, aap sabko vardaan dene waali hain. Aap Yashoda ji ke ghar janmi thi aur Kans ka vinaash karne waali hain.’

‘Aap bhakton ki raksha karti hain aur unhe dukh aur sankat se bachati hain.’

Yudhishthira ne bahut bhakti se Devi ki stuti ki.

Woh bole,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            ‘Hey Devi, aapka roop suraj aur poornima ke chand ki tarah tejomay hai.’

‘Aapke haathon mein talwar, dhanush, chakra aur anek divya hathiyaar hain.’

‘Aap Mahishasur ko maarne waali mahaan shakti hain.’

‘Aap hi Vijay dene waali Jaya aur Vijaya hain.’

‘Hey Devi, iss kathin samay mein humein apni kripa dijiye aur humari raksha kijiye.’

Yudhishthira ne fir kaha,

‘Jungle, samundar, pahaad ya dushmano ke beech — jo bhi aapko yaad karta hai, uski raksha hoti hai.’

‘Aap hi Lakshmi hain, aap hi buddhi, shakti, daya aur safalta hain.’

‘Hum apna rajya kho chuke hain. Hey Mata, kripya humein apni sharan mein lijiye.’

Rishi Vaisampayana bole, “Yudhishthira ki sachchi bhakti se prasann hokar Devi Durga unke saamne prakat ho gayin.”

Devi muskuraakar boli,

‘Hey Yudhishthira, meri kripa se tum jaldi hi Kauravo ko haraoge aur apna rajya wapas paoge.’

‘Tum aur tumhare bhai fir se sukh aur samriddhi paoge.’

‘Jab tak tum Virata nagari mein rahoge, koi bhi tumhe pehchaan nahi paayega.’

‘Jo bhi vyakti bhakti se meri stuti karega, use dhan, santaan, safalta aur suraksha milegi.’

‘Jungle, yudh, samundar ya kisi bhi sankat mein jo mujhe yaad karega, main uski raksha karungi.’

‘Aur jo is pavitra stuti ko shraddha se sunega ya padhega, uske kaam safal honge.’

Itna kehkar Devi Durga ne Pandavo ko aashirvaad diya aur fir antardhyaan ho gayin.

Pandav Devi ka aashirvaad paakar aur bhi himmat se Virata nagari ki taraf badh gaye."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.7
        with st.expander("Section 4.1.7  Section VII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Yudhishthira ne apne kapde mein sundar paase baandh liye. Woh sone aur neelam se sajhe hue the. Unhe baazu ke neeche rakhkar woh Virata ki rajsabha mein pahunche.

Us samay Raja Virata apne darbaar mein baithe the.

Yudhishthira ka roop bahut tejomay lag raha tha. Woh aise chamak rahe the jaise baadalon ke peeche chhupa hua chand ya raakh se dhaki hui agni.

Raja Virata ne unhe dekhkar apne mantriyon aur sabha ke logon se kaha,

“Yeh vyakti kaun hai? Yeh kisi aam Brahman jaise nahi lagte.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh kisi mahaan raja ki tarah dikhte hain. Inke paas na sena hai, na rath aur na haathi, fir bhi inka tej Indra jaisa hai.”

“Yeh bina dare seedha meri taraf aa rahe hain.”

Tab Yudhishthira Raja Virata ke paas gaye aur vinamrata se bole,

“Hey Maharaj, main ek Brahman hoon. Maine apna sab kuch kho diya hai aur ab jeevan chalane ke liye aapki seva karna chahta hoon.”

Raja Virata unki baat sunkar khush hue aur bole,

“Tumhara yahaan swaagat hai. Batao, tumhara naam kya hai aur tum kya kaam jaante ho?”

Yudhishthira ne jawab diya,

“Mera naam Kanka hai. Main paasa khelne mein nipun hoon aur pehle Raja Yudhishthira ka mitra tha.”

Virata bole,

“Kanka, tum mujhe bahut priya lagte ho. Tum kisi devta jaise dikhte ho.”

“Tum mere saath raho. Tumhe yahaan poora samman milega.”

Yudhishthira ne kaha,

“Hey Raja, meri ek prarthana hai. Mujhe neeche soch waale logon ke saath jhagda na karna pade.”

“Aur jo vyakti mujhse paase mein haar jaaye, usse meri jeeti hui vastu wapas na li jaaye.”

Virata ne turant kaha,

“Aisa hi hoga. Jo bhi tumhe pareshaan karega, main use dand dunga.”

“Is rajya mein tum mere samaan samman paoge.”

“Tum mere mitra ki tarah rahoge. Mere mahal ke sab darwaaze tumhare liye khule rahenge.”

“Tum mere rajya ke andar aur baahar ke kaamon ko bhi dekh sakte ho.”

Rishi Vaisampayana bole, “Is tarah Yudhishthira ne Virata ke darbaar mein Kanka ke roop mein rehna shuru kiya.”

“Sab log unka bahut adar karte the, lekin koi bhi unki asli pehchaan nahi samajh paaya.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.8
        with st.expander("Section 4.1.8  Section VIII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Uske baad Bhima Raja Virata ke darbaar mein pahunche.

Unka sharir bahut balwaan tha aur unka roop suraj ki tarah chamak raha tha. Woh sher ki tarah garv se chal rahe the.

Unke haath mein rasoi ke bade chamche aur ek kaali talwar thi.

Bhima ko dekhkar Raja Virata hairaan ho gaye.

Woh apne logon se bole,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh balwaan yuva kaun hai? Iske kandhe sher jaise mazboot hain aur iska tej suraj jaisa hai.”

“Mujhe lagta hai yeh koi aam aadmi nahi. Shayad yeh Gandharvon ka raja ya swayam Indra ho sakta hai.”

“Jaldi pata karo yeh kaun hai aur kya chahta hai.”

Raja ke sevak Bhima ke paas gaye aur unhe raja ke saamne le aaye.

Bhima ne vinamrata se kaha,

“Hey Maharaj, mera naam Vallabha hai. Main ek rasoiya hoon aur bahut swadisht bhojan banana jaanta hoon.”

“Kripya mujhe apni rasoi mein kaam de dijiye.”

Raja Virata muskuraakar bole,

“Vallabha, mujhe nahi lagta ki tum sirf rasoiya ho.”

“Tumhara roop aur shakti kisi mahan raja ya devta jaise lagte hain.”

Bhima ne shaant swar mein jawab diya,

“Hey Raja, main bhojan banana achchi tarah jaanta hoon. Raja Yudhishthira bhi mere haath ka bana khaana pasand karte the.”

“Lekin main sirf rasoiya hi nahi, ek pehelwan bhi hoon.”

“Mujhse zyada balwaan shayad hi koi ho.”

“Main sher aur haathiyon se bhi lad sakta hoon aur aapka manoranjan kar sakta hoon.”

Virata yeh sunkar bahut khush hue.

Woh bole,

“Tum jo chaho woh kaam kar sakte ho. Main tumhe apni rasoi ka mukhiya banata hoon.”

“Lekin sach kahoon, tum jaise veer ko toh poori dharti ka raja hona chahiye.”

Rishi Vaisampayana bole, “Is tarah Bhima Vallabha naam se Virata ke mahal ki rasoi mein rehne lage.”

“Jaldi hi Raja Virata unse bahut prasann ho gaye. Lekin koi bhi unki asli pehchaan nahi jaan paaya.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.9
        with st.expander("Section 4.1.9  Section IX"):
            text1 = """ 
            Rishi Vaisampayana bole, “Draupadi ne apne lambe, komal aur sundar baalon ko baandhkar ek choti bana li aur use apne kapde se chhupa liya.

Unhone ek saadhaaran aur thoda maila vastra pehna, taaki koi unhe pehchaan na sake.

Sairindhri ka roop dharan karke woh Virata nagari mein idhar-udhar ghoomne lagi.

Unki sundarta dekhkar nagar ke log hairaan ho gaye.

Sab unse poochne lage,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            ‘Tum kaun ho? Aur kya chahti ho?’

Draupadi ne shaant swar mein kaha,

‘Main ek Sairindhri hoon. Main kisi ki seva karke jeevan chalana chahti hoon.’

Lekin logon ko yakeen nahi ho raha tha ki itni sundar aur komal stree ek saadharan daasi ho sakti hai.

Usi samay Raja Virata ki patni Rani Sudeshna mahal ki chhat se Draupadi ko dekh rahi thi.

Draupadi ki sundarta aur vinamrata dekhkar woh turant unhe bulane lagi.

Sudeshna ne poocha,

‘Hey sundari, tum kaun ho? Tum kisi rani ya devi jaise lagti ho.’

‘Tumhari chal, tumhari awaaz aur tumhara roop kisi saadharan stree jaisa nahi hai.’

‘Sach batao, kya tum koi devi, Gandharvi ya apsara ho?’

Draupadi ne vinamrata se jawab diya,

‘Hey Rani, main na devi hoon aur na apsara. Main ek Sairindhri hoon.’

‘Mujhe baal sajaana, sugandhit lep banana aur sundar phoolon ki mala banana aata hai.’

‘Main pehle Krishna ki priya rani Satyabhama aur Pandavo ki patni Draupadi ki seva karti thi.’

‘Draupadi mujhe Malini kehkar bulaati thi.’

Rani Sudeshna Draupadi ki baat sunkar bhi chintit ho gayin.

Woh boli,

‘Tum itni sundar ho ki Raja Virata tumhe dekhkar mujhse door ho sakte hain.’

‘Mahal ki sab stree aur sevikaayein bhi tumhe hi dekh rahi hain. Koi purush tumhari sundarta se bach nahi paayega.’

‘Mujhe darr hai ki tumhe mahal mein rakhkar kahin main khud hi museebat mein na pad jaaun.’

Draupadi ne shaant aur himmat bhare swar mein kaha,

‘Hey Rani, koi bhi purush mujhe paane ki koshish nahi kar sakta.’

‘Mere paanch Gandharva pati hamesha meri raksha karte hain.’

‘Jo bhi dusht vyakti mujhe buri nazar se dekhega ya pareshan karega, woh usi raat mar jaayega.’

‘Main sirf un logon ki seva karti hoon jo mujhe jhootha bhojan chhoone ya pair dhone ko na kahen.’

Sudeshna ne yeh sunkar rahat ki saans li aur boli,

‘Agar aisa hai, toh tum mere mahal mein reh sakti ho.’

‘Tumhe koi neecha kaam nahi karna padega.’

Rishi Vaisampayana bole, “Is tarah Draupadi Malini naam se Rani Sudeshna ke mahal mein rehne lagi.”

“Lekin Virata nagari mein koi bhi unki asli pehchaan nahi jaan paaya.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.10
        with st.expander("Section 4.1.10  Section X"):
            text1 = """ 
            Rishi Vaisampayana bole, “Uske baad Sahadeva gaay charane waale kapde pehenkar Virata nagari ke gaushala ki taraf gaye.

Woh gaayon ke rakhwaalon ki boli mein baat kar rahe the.

Jab Raja Virata ne unhe dekha, toh woh unke tej aur shaant swabhav ko dekhkar hairaan ho gaye.

Raja ne turant apne sevakon se kaha,

‘Us yuva ko mere paas bulao.’"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Jab Sahadeva raja ke saamne aaye, tab Virata ne poocha,

‘Tum kaun ho? Kahaan se aaye ho? Aur kya kaam jaante ho?’

‘Maine tumhe pehle kabhi nahi dekha.’

Sahadeva ne gehri aur shaant awaaz mein jawab diya,

‘Mera naam Arishtanemi hai. Main ek Vaishya hoon.’

‘Main pehle Pandavo ke yahan gaayon ki dekhbhaal karta tha.’

‘Ab main aapki seva mein rehna chahta hoon, kyunki mujhe nahi pata Pandav ab kahaan hain.’

‘Main bina seva ke nahi reh sakta aur aapke alawa kisi aur ki seva karna bhi nahi chahta.’

Raja Virata unki baat sunkar bole,

‘Tum kisi aam gaay charane waale jaise nahi lagte.’

‘Tumhara roop toh kisi mahan raja ya yoddha jaisa hai.’

‘Sach batao, tum kya jaante ho aur kis kaam ke badle kya chahte ho?’

Sahadeva ne vinamrata se kaha,

‘Raja Yudhishthira ke paas lakhon gaayein thi aur main un sabki dekhbhaal karta tha.’

‘Log mujhe Tantripal kehte the.’

‘Mujhe gaayon ki prakriti aur unki sehat ka poora gyaan hai.’

‘Main jaan sakta hoon ki kaunsi gaay ya saand shubh hai aur kaise gaayon ki sankhya badhaayi ja sakti hai.’

‘Mujhe unhe bimariyon se bachane ka bhi gyaan hai.’

Virata yeh sunkar bahut prasann hue.

Woh bole,

‘Mere paas bhi ek lakh gaayein hain. Aaj se un sabki zimmedaari tumhari hai.’

‘Tum unki poori dekhbhaal karoge.’

Rishi Vaisampayana bole, “Is tarah Sahadeva Tantripal ke roop mein Raja Virata ki gaayon ki dekhbhaal karne lage.”

“Woh wahan bahut shaanti se rehne lage aur koi bhi unki asli pehchaan nahi jaan paaya.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.11
        with st.expander("Section 4.1.11  Section XI"):
            text1 = """ 
            Rishi Vaisampayana bole, “Uske baad ek aur adbhut vyakti Virata ke mahal ke dwar par aaya.

Woh Arjuna the, lekin Brihannala ke roop mein.

Unhone striyon jaise gehne pehne hue the — bade kundal, sone se sajhi hui choodiyan aur lambe baal ki choti.

Unki chal haathi ki tarah shaktishaali thi aur unke kadam se zameen hilti hui lag rahi thi.

Jab Raja Virata ne unhe dekha, toh woh hairaan reh gaye."""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Woh apne darbaar mein bole,

“Yeh kaun hai? Maine ise pehle kabhi nahi dekha.”

“Yeh kisi devta ya mahaan yoddha jaise lagte hain. Mujhe vishwas nahi hota ki yeh napunsak ho sakte hain.”

Virata ne Arjuna se poocha,

“Tum kaun ho? Aur kya kaam jaante ho?”

Arjuna ne shaant swar mein jawab diya,

“Hey Raja, mera naam Brihannala hai.”

“Mujhe gaan, nritya aur sangeet ka gyaan hai.”

“Main rajkumari Uttara aur mahal ki anya kanyaon ko nritya aur sangeet sikha sakta hoon.”

“Main apni purani kahani nahi sunana chahta, kyunki use yaad karke mujhe dukh hota hai.”

“Samajh lijiye ki mera na koi pita hai aur na maa.”

Raja Virata bole,

“Hey Brihannala, tumhe wahi kaam diya jaata hai jo tum chahte ho.”

“Tum meri beti Uttara ko nritya aur sangeet sikhao.”

“Lekin sach kahoon, tum jaise vyakti ko toh poori dharti par raj karna chahiye.”

Rishi Vaisampayana bole, “Virata ne pehle Brihannala ki kalaon ki pareeksha li.”

“Mahilao ne bhi dekh liya ki Brihannala sach mein napunsak roop mein hi reh rahe hain.”

Uske baad Arjuna ko rajkumari Uttara ke mahal mein bhej diya gaya.

Wahan Arjuna ne Uttara aur uski saheliyon ko gaan, nritya aur vaadya yantra bajana sikhana shuru kiya.

Jaldi hi sab log Brihannala se bahut prasann ho gaye.

Is tarah mahaan dhanurdhari Arjuna chupkar Virata ke mahal mein rehne lage, aur koi bhi unki asli pehchaan nahi jaan paaya."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.1.12
        with st.expander("Section 4.1.12  Section XII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Kuch samay baad Nakula bhi Raja Virata ke mahal ki taraf aaye.

Unka roop bahut tejomay tha. Woh aise chamak rahe the jaise baadalon ke beech se suraj nikal aaya ho.

Mahal ke paas pahunchte hi Nakula ghodon ko dhyaan se dekhne lage.

Yeh dekhkar Raja Virata ne apne sevakon se kaha,

“Yeh yuva kaun hai? Iska tej kisi devta jaisa lagta hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.1.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh mere ghodon ko bade dhyaan se dekh raha hai. Zaroor ise ghodon ka bahut gyaan hoga.”

“Ise turant mere paas lao.”

Nakula raja ke saamne aaye aur vinamrata se bole,

“Hey Maharaj, aapki jai ho.”

“Main ghodon ko sambhaalne aur training dene mein nipun hoon. Main aapke ghodon ki dekhbhaal karna chahta hoon.”

Raja Virata bole,

“Main tumhe dhan, rehne ki jagah aur samman sab dunga.”

“Lekin pehle batao tum kaun ho aur kahaan se aaye ho?”

Nakula ne shaant swar mein jawab diya,

“Pandavo mein sabse bade Raja Yudhishthira the. Main pehle unke ghodon ki dekhbhaal karta tha.”

“Log mujhe Granthika kehte the.”

“Mujhe ghodon ki prakriti ka poora gyaan hai.”

“Main jungli aur gusse waale ghodon ko bhi shaant bana sakta hoon.”

“Main unki bimariyon ka ilaaj bhi jaanta hoon.”

“Mere haathon mein koi bhi ghoda kamzor ya beemar nahi hota.”

Virata yeh sunkar bahut khush hue.

Woh bole,

“Aaj se mere sabhi ghode tumhari dekhbhaal mein rahenge.”

“Mere ghodon ke rakhwaale aur rath chalane waale sab tumhare adheen rahenge.”

“Lekin sach kahoon, tum kisi mahan raja jaise lagte ho. Tumhe dekhkar mujhe Yudhishthira ki yaad aa gayi.”

“Pata nahi woh mahaan Pandav iss samay jungle mein kaise jee rahe honge.”

Rishi Vaisampayana bole, “Nakula ne apne kaam aur vinamr swabhav se jaldi hi sabka dil jeet liya.”

“Virata ke mahal mein rehkar bhi koi unki asli pehchaan nahi jaan paaya.”

“Is tarah Pandav apni kathin peeda ko chupate hue bhi shaanti aur dhairya se Virata nagari mein apna gupt jeevan bitaane lage.”"""
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
            text1 = """ 
            Rishi Vaisampayana bole, “Hey Raja Janamejaya, ab suno ki Pandav Virata nagari mein chupkar kaise jeevan bita rahe the.

Dharmraj Yudhishthira Raja Virata ke priya saathi ban gaye. Woh paase aur khel mein sabko manoranjan karte the.

Jo dhan woh jeette, use chupchaap apne bhaiyon mein baant dete.

Bhima bhi rasoi mein kaam karke khaane aur anya vastuon ko Yudhishthira ko de dete.

Arjuna mahal ke andar sangeet aur nritya sikhakar jo paate, use bhi sab bhaiyon mein baant dete.

Sahadeva doodh, dahi aur ghee laate aur Nakula ghodon ki seva ke badle jo paate, woh bhi sabke saath baantte."""
            create_image_text_layout(
                "attached_assets/chapter4/4.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Draupadi khud bahut dukh mein thi, lekin fir bhi sab bhaiyon ka dhyaan rakhti thi.

Is tarah sab ek doosre ki madad karte hue Virata nagari mein chupkar rehne lage, jaise maa ke garbh mein koi surakshit rehta hai.

Pandav hamesha saavdhaan rehte the, kyunki unhe darr tha ki kahin Duryodhana ke log unhe pehchaan na lein.

Kuch mahine beet gaye.

Phir Matsya desh mein Bhagwan Brahma ke samman mein ek bada utsav hua.

Us utsav mein bahut saare pehelwan aur yoddha aaye. Sab apni shakti dikhana chahte the.

Unmein Jimuta naam ka ek bahut balwaan pehelwan tha. Woh sabko yudh ke liye lalkaar raha tha.

Lekin uski shakti dekhkar koi bhi usse ladne ki himmat nahi kar paaya.

Tab Raja Virata ne Bhima, yani Vallabha ko usse ladne ka aadesh diya.

Bhima mann hi mann sochne lage ki unhe apni shakti chhupaani chahiye, lekin raja ki baat bhi taal nahi sakte the.

Isliye woh dheere-dheere sher ki chaal se akhaade mein utar gaye.

Sab log utsaah se unhe dekhne lage.

Bhima aur Jimuta dono haathi jaise balwaan lag rahe the.

Dono ne ek doosre ko pakda, dhakka diya aur zor-zor se patka.

Kabhi ek doosre ko uthaate, kabhi zameen par gira dete.

Unke mukke aur laaton ki awaaz bijli ki tarah garaj rahi thi.

Sab log bahut romanch se yeh yudh dekh rahe the.

Aakhir mein Bhima ne sher ki tarah Jimuta ko pakad liya.

Unhone use hawa mein uthaakar bahut baar ghumaya.

Phir zor se zameen par phek diya.

Jimuta wahi mar gaya.

Yeh dekhkar sab log hairaan reh gaye aur Raja Virata bahut khush hue.

Raja ne Vallabha ko bahut saare uphaar diye.

Uske baad Bhima ne aur bhi kai pehelwano aur jangli jaanwaron ko haraaya.

Kabhi woh sher se ladte, kabhi baagh aur haathiyon se.

Mahal ki mahilaayein bhi unki veerta dekhkar hairaan ho jaati thi.

Udhar Arjuna apne gaan aur nritya se mahal ki sab streeon ko khush rakhte the.

Nakula apne shikshit aur tez ghodon se Raja Virata ko prasann karte the.

Sahadeva ki sambhaal se gaayein aur bail bahut swasth aur shaant rehte the.

Raja unhe bhi dhan aur uphaar dete the.

Draupadi yeh sab dekhkar kabhi-kabhi dukhi ho jaati thi, kyunki itne mahaan yoddha ab doosron ki seva kar rahe the.

Lekin Pandav dhairya aur shaanti ke saath apna gupt jeevan bitaate rahe."""
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
            text1 = """ 
            Rishi Vaisampayana bole, “Pandav Virata nagari mein gupt roop se rehte hue das mahine bita chuke the.”

“Draupadi, jo swayam raniyon ki tarah seva paane yogya thi, ab Rani Sudeshna ki seva mein bahut dukh ke saath jee rahi thi.”

“Fir ek din Virata sena ka senapati Keechak ne Draupadi ko dekha.”

Keechak bahut balwaan tha aur Raja Virata ka priya bhi tha."""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Jab usne Draupadi ko dekha, toh woh uski sundarta par mohit ho gaya.

Uska mann kaam vasna se bhar gaya.

Woh apni behen Sudeshna ke paas gaya aur bola,

“Yeh sundar stree kaun hai? Maine ise pehle kabhi nahi dekha.”

“Iski sundarta kisi devi jaisi hai.”

“Isne toh mera mann hi chura liya hai.”

“Yeh tumhari daasi banne layak nahi. Isse mere mahal ki rani banna chahiye.”

“Main apna dhan, mahal aur sab kuch iske charanon mein rakh dunga.”

Itna kehkar Keechak Draupadi ke paas gaya.

Woh madhur shabdon mein bola,

“Hey sundari, tum kaun ho?”

“Tumhara chehra poornima ke chand jaisa chamak raha hai.”

“Tumhari aankhen kamal ki pankhudiyon jaise sundar hain.”

“Tumhari awaaz koel ki tarah madhur hai.”

“Tumhari sundarta dekhkar koi bhi tum par mohit ho jaaye.”

Keechak aur bhi adhik vasna bhari baatein karne laga.

Woh bola,

“Tum mere saath mahal mein raho.”

“Main apni sab patniyon ko tumhari daasi bana dunga.”

“Main khud bhi tumhara sevak ban jaaunga.”

“Tumhe duniya ke sab sukh aur aaraam dunga.”

Draupadi ne uski baatein sunkar shaant lekin kathor swar mein kaha,

“Hey Soot putra, tum galat raah par chal rahe ho.”

“Main ek vivaahit stree hoon.”

“Achhe log sirf apni patni se hi prem karte hain.”

“Parayi stree par buri nazar daalna paap hai.”

“Kaam vasna mein andha vyakti badnaami aur vinaash paata hai.”

Lekin Keechak par uski baaton ka koi asar nahi hua.

Woh aur bhi adhik ahankaar se bola,

“Is poore rajya ka asli swaami main hoon.”

“Mere samaan balwaan aur sundar koi nahi.”

“Tum mere saath rehkar sab sukh pa sakti ho.”

Draupadi ne gusse aur himmat se jawab diya,

“Apni maut ko mat bulao, Keechak!”

“Mere paanch Gandharva pati meri raksha karte hain.”

“Agar tumne mujhe paane ki koshish ki, toh woh tumhe maar daalenge.”

“Chahe tum dharti ke andar chhuup jaao, aasman mein udd jaao ya samundar paar chale jaao, fir bhi tum bach nahi paoge.”

“Tum ek moorkh bachche ki tarah ho jo chand ko pakadne ki koshish kar raha hai.”

“Abhi bhi samay hai, apne aapko vinaash se bacha lo.”

Rishi Vaisampayana bole, “Lekin kaam aur ahankaar mein andha hua Keechak Draupadi ki baat samajh nahi paaya.”

“Uska mann aur bhi adhik paap ki taraf badhne laga.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.2
        with st.expander("Section 4.3.2  Section XV"):
            text1 = """ 
            Rishi Vaisampayana bole, “Draupadi ke mana karne par bhi Keechak ki buri ichchha kam nahi hui.”

Woh bechain hokar apni behen Sudeshna ke paas gaya aur bola,

“Hey behen, kisi tarah apni Sairindhri ko mere paas bhejo.”

“Main uski sundarta ke moh mein jal raha hoon.”

Rani Sudeshna ne Keechak ki baatein suni.

Woh samajh gayi ki Draupadi iss baat se bahut pareshan hogi, lekin apne bhai ke liye uske mann mein daya bhi aa gayi."""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Thodi der sochne ke baad Sudeshna boli,

“Kisi utsav ke bahaane tum apne mahal mein khaane aur madira ki vyavastha karo.”

“Fir main Sairindhri ko madira lene ke bahaane tumhare paas bhej dungi.”

“Us samay tum usse akele mein manaane ki koshish kar lena.”

Keechak yeh sunkar bahut khush ho gaya.

Usne turant apne mahal mein swadisht bhojan aur madira taiyaar karwaayi.

Fir ek din Sudeshna ne Draupadi se kaha,

“Sairindhri, mujhe pyaas lagi hai. Tum Keechak ke mahal jaakar mere liye madira le aao.”

Draupadi yeh sunkar ghabra gayi.

Woh vinamrata se boli,

“Hey Rani, main Keechak ke mahal nahi jaana chahti.”

“Aap jaanti hain ki woh kitna besharam aur dusht hai.”

“Woh mujhe dekhkar zaroor mera apmaan karega.”

“Maine pehle hi kaha tha ki main apne patiyon ke prati wafadaar rahungi.”

“Kripya kisi aur daasi ko bhej dijiye.”

Lekin Sudeshna boli,

“Tum meri taraf se jaa rahi ho. Woh tumhe haani nahi pahunchayega.”

Fir usne Draupadi ko ek sone ka bartan diya aur Keechak ke mahal bhej diya.

Draupadi bahut chintit thi.

Unki aankhon mein aansu aa gaye.

Raaste mein unhone mann hi mann prarthana ki,

“Main apne pati ke alawa kisi aur ko kabhi mann se nahi jaanti.”

“Is satya ki shakti se Keechak mera kuch bhi na bigaad sake.”

Rishi Vaisampayana bole, “Draupadi ne Surya Dev ka bhi smaran kiya.”

Surya Dev ne unki pavitrata aur dukh ko samjha.

Unhone ek adrishya Rakshas ko aadesh diya ki woh Draupadi ki raksha kare.

Us din se woh adrishya rakshak hamesha Draupadi ke saath rehne laga.

Udhar Keechak Draupadi ka intezaar kar raha tha.

Jab usne Draupadi ko apne mahal mein aate dekha, toh woh bahut khush hua.

Uske mann mein paap aur vasna aur bhi badh gayi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            
                # Section 4.3.3
        with st.expander("Section 4.3.3  Section XVI"):
            text1 = """ 
            Rishi Vaisampayana bole, “Draupadi ke mana karne ke baad bhi Keechak ki buri ichchha aur badh gayi.”

Jab Draupadi uske mahal mein pahunchi, tab Keechak muskuraakar bola,

“Hey sundari, tumhara swaagat hai.”

“Aaj ka din mere liye bahut shubh hai, kyunki tum mere ghar aayi ho.”

“Tum mere saath yahan sukh se raho.”

“Main tumhe sone ke gehne, sundar vastra aur anek ratna dunga.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh sundar shayya tumhare liye taiyaar hai. Aao, mere saath baithkar madira piyo.”

Draupadi ne shaant swar mein jawab diya,

“Main yahan sirf Rani Sudeshna ke liye madira lene aayi hoon.”

“Kripya jaldi se madira de dijiye.”

Lekin Keechak bola,

“Rani ke liye koi aur madira le jaayega.”

Itna kehkar usne Draupadi ka haath pakad liya.

Draupadi gusse aur apmaan se kaamp uthi.

Woh boli,

“Hey dusht! Maine kabhi mann se bhi apne patiyon ke prati bewafai nahi ki.”

“Is satya ki shakti se tum jaldi hi zameen par giraaye jaaoge.”

Rishi Vaisampayana bole, “Jab Draupadi bhaagne lagi, tab Keechak ne unke vastra pakad liye.”

Draupadi ne krodh mein use zor se dhakka diya.

Keechak ek kate hue ped ki tarah zameen par gir gaya.

Draupadi turant bhaagkar rajsabha ki taraf gayi, jahan Yudhishthira aur Bhima baithe the.

Lekin Keechak bhi unke peeche dauda.

Sabke saamne usne Draupadi ke baal pakadkar unhe gira diya aur laat maari.

Yeh dekhkar Surya Dev dwara bheja gaya adrishya Rakshas turant krodhit ho gaya.

Usne zor se Keechak ko dhakka diya.

Keechak hilkar zameen par gir pada aur kuch der ke liye behosh ho gaya.

Yeh sab dekhkar Bhima ka krodh bhadak utha.

Unki aankhen gusse se laal ho gayin.

Woh turant Keechak ko maar dena chahte the.

Lekin Yudhishthira ko darr tha ki kahin unki pehchaan khul na jaaye.

Isliye unhone chupke se Bhima ko shaant rehne ka sanket diya.

Woh bole,

“Hey rasoiye, agar tumhe lakdi chahiye toh baahar jaakar ped kaat lao.”

Bhima samajh gaye ki bade bhai abhi unhe rukne ko keh rahe hain.

Udhar Draupadi aansuon ke saath Raja Virata ki sabha mein boli,

“Haaye! Aaj ek Soot putra ne mahaan veeron ki patni ka sabke saamne apmaan kiya hai.”

“Woh veer jo duniya ko hila sakte hain, aaj chup baithe hain.”

“Hey Raja Virata, aapke saamne mujhe laat maari gayi aur aap chup rahe.”

“Yeh kisi sachche raja ka vyavahaar nahi hai.”

“Yahaan ke sab log bhi chupchaap yeh anyaay dekh rahe hain.”

Sabha ke log Draupadi ki baatein sunkar Keechak ko dosh dene lage.

Woh bole,

“Yeh stree kisi devi jaisi lagti hai.”

“Jiske paas aisi patni ho, use aur kisi sukh ki kya zarurat?”

Yudhishthira bhi andar hi andar bahut krodhit the, lekin apna roop chhupaaye rakha.

Unhone Draupadi se shaant swar mein kaha,

“Hey Sairindhri, ab tum Sudeshna ke mahal laut jaao.”

“Veeron ki patniyan apne pati ke liye dukh sahti hain.”

“Tumhare Gandharva pati samay aane par tumhara apmaan karne waale ko dand denge.”

Draupadi samajh gayi ki Yudhishthira abhi dhairya rakhne ko keh rahe hain.

Woh boli,

“Mere pati bahut dayaalu hain.”

“Lekin kyunki unmein sabse bade paase ke khel mein lage rehte hain, isliye sab log unhe sataate hain.”

Itna kehkar Draupadi rote hue Sudeshna ke mahal laut gayi.

Sudeshna ne unhe us haal mein dekhkar poocha,

“Hey sundari, tumhare saath yeh anyaay kisne kiya?”

Draupadi boli,

“Jab main aapke liye madira lene gayi, tab Keechak ne sabke saamne mera apmaan kiya.”

Yeh sunkar Sudeshna boli,

“Agar tum chaho toh main Keechak ko marwa sakti hoon.”

Draupadi ne gehri awaaz mein jawab diya,

“Uski maut ab nishchit hai.”

“Jin logon ka usne apmaan kiya hai, wahi aaj usse Yamraj ke paas bhejenge.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.4
        with st.expander("Section 4.3.4  Section XVII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Keechak ke apmaan se Draupadi ka hriday dukh aur krodh se bhar gaya tha.”

Woh apne kaksh mein gayi, snaan kiya aur aansuon ke saath sochne lagi,

“Main kya karun? Kis se madad maangu?”

Fir unhe Bhima ki yaad aayi.

Draupadi ne mann hi mann kaha,

“Is samay sirf Bhima hi meri raksha kar sakte hain.”

Raat hone par Draupadi chupke se Bhima ke paas gayi.

Bhima rasoi ke paas so rahe the."""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Unki saans sher ki garaj jaise lag rahi thi.

Draupadi unke paas jaakar dukhi swar mein boli,

“Hey Bhimasena, aap kaise chain se so sakte hain jab woh dusht Keechak abhi bhi zinda hai?”

Rishi Vaisampayana bole, “Draupadi ne Bhima ko hilaakar jagaya.”

Bhima uthkar baith gaye.

Unhone Draupadi ka udaas aur peela chehra dekha toh bahut chintit hue.

Bhima prem aur chinta se bole,

“Hey Krishnaa, tum itni raat ko yahaan kyun aayi ho?”

“Tum bahut dukhi aur kamzor lag rahi ho.”

“Jo bhi baat hai, mujhe sach-sach batao.”

“Chahe baat sukh ki ho ya dukh ki, main tumhari madad zaroor karunga.”

“Tum jaanti ho ki har sankat mein main hi tumhari raksha karta aaya hoon.”

“Jaldi batao tumhare mann mein kya hai.”

“Lekin dhyaan rahe, subah hone se pehle tumhe wapas jaana hoga, taaki kisi ko hamare baare mein pata na chale.”

Draupadi ki aankhon mein aansu bhar aaye.

Ab unka mann Bhima ko apna saara dukh bataane ke liye taiyaar ho chuka tha.
Draupadi aansuon bhari aankhon se Bhima se boli,

“Hey Bhimasena, jis stree ke pati Yudhishthira jaise ho, uske jeevan mein dukh ki kami kaise ho sakti hai?”

“Aap sab kuch jaante hue bhi mujhse kyun pooch rahe hain?”

“Sabha mein mujhe daasi kehkar ghaseeta gaya.”

“Jungle mein Jayadrath ne mera apaharan karne ki koshish ki.”

“Aur ab Keechak ne sabke saamne mujhe laat maari.”

“Kaunsi aur rajkumari itna apmaan sahkar bhi jee sakti hai?”

Draupadi ka swar dard se bhar gaya.

Woh boli,

“Yeh sab us paase ke khel ki wajah se hua.”

“Kaunsa buddhimaan raja apna rajya, dhan aur apni patni tak ko daav par laga deta hai?”

“Yudhishthira ke paas itna dhan tha ki agar woh saalon tak bhi paase khelte, tab bhi unka khazaana khatam nahi hota.”

“Lekin aaj wahi mahaan raja doosron ke darbaar mein baithkar paase phenkte hain.”

Draupadi ne dukhi mann se kaha,

“Indraprastha mein hazaaron raja unka samman karte the.”

“Unke mahal mein har din anek mehmaan aur Brahman bhojan paate the.”

“Hazaaron gaayak aur kavi unki prashansa karte the.”

“Woh gareebon, andhon, budhon aur dukhi logon ki raksha karte the.”

“Lekin aaj wahi Dharmraj Virata ke darbaar mein Kanka bankar baithe hain.”

“Jo raja kabhi sabko aadesh dete the, aaj doosron ki seva kar rahe hain.”

Draupadi ki aankhon se aansu behne lage.

Woh boli,

“Hey Bhima, jab main Yudhishthira ko kisi aur raja ki prashansa karte dekhti hoon, mera hriday toot jaata hai.”

“Jo poori dharti ke raja the, aaj doosron par nirbhar hokar jee rahe hain.”

“Fir aap kaise keh sakte hain ki main dukhi nahi hoon?”

Draupadi ka dard aur apmaan unki har baat mein saaf dikh raha tha.

Woh ab Bhima ke saamne apna saara dukh kholkar rakh chuki thi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.5
        with st.expander("Section 4.3.5  Section XVIII"):
            text1 = """ 
            Draupadi aansuon bhari aankhon se Bhima se boli,

“Hey Bhimasena, ek aur bada dukh hai jo mere hriday ko tod deta hai.”

“Jab main aapko Virata ke rasoiye ke roop mein dekhti hoon, mera mann dukh se bhar jaata hai.”

“Log aapko Vallava naam ka ek saadhaaran rasoiya samajhte hain.”

“Yeh dekhkar mera hriday toot jaata hai, kyunki aap jaise mahaan veer is kaam ke liye nahi bane.”

“Jab aap rasoi ka kaam khatam karke vinamrata se Raja Virata ke paas baithte hain, tab mera dukh aur badh jaata hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Raja manoranjan ke liye aapko haathiyon aur jangli jaanwaron se ladaata hai.”

“Mahal ki streeon ko yeh sab dekhkar hansi aati hai.”

“Lekin mera mann darr aur dukh se bhar uthta hai.”

Draupadi boli,

“Rani Sudeshna aur uski saheliyan mujhe dekhkar kehti hain ki main aapki chinta kisi priya vyakti ki tarah karti hoon.”

“Woh mazaak udaati hain aur mujhe sharminda karti hain.”

“Yeh sab sunkar mera dukh aur badh jaata hai.”

Fir Draupadi ne Arjuna ko yaad karke gehri saans li.

Woh boli,

“Jo Arjuna ek samay devtaon ko bhi hara chuke hain, aaj wahi Brihannala bankar mahal ki ladkiyon ko nritya aur sangeet sikha rahe hain.”

“Jinke dhanush ki awaaz se dushman kaamp uthte the, aaj wahi streeon ke beech gaane gaa rahe hain.”

“Unke baalon mein chotiyaan aur haathon mein shankh ke kangan dekhkar mera hriday dukhi ho uthta hai.”

“Jo duniya ke sabse mahaan dhanurdhar the, aaj stree ka roop dhaaran karke jee rahe hain.”

“Unhe iss haal mein dekhkar meri aankhon mein aansu aa jaate hain.”

Draupadi ka swar aur bhaari ho gaya.

Woh boli,

“Fir main Sahadeva ko dekhti hoon.”

“Woh mahaan aur vinamr yoddha aaj gaayon ki dekhbhaal kar rahe hain.”

“Unhe raat ko bachhdo ki khal par sota dekhkar mujhe neend nahi aati.”

“Mata Kunti ne jungle jaate waqt mujhe kaha tha — ‘Sahadeva bahut komal aur sharmeele hain. Unka dhyaan rakhna.’”

“Yeh sab yaad karke mera mann toot jaata hai.”

Fir Draupadi ne Nakula ko yaad kiya.

Woh boli,

“Jo Nakula apni sundarta, buddhi aur veerta ke liye prasiddh the, aaj Raja Virata ke ghodon ko train kar rahe hain.”

“Jo veer yuddh mein shatru sena ko dara dete the, aaj ghodon ko daudakar raja ko khush karte hain.”

“Samay ne hum sabko kitna badal diya hai.”

Draupadi ne Bhima ki taraf dekhkar kaha,

“Hey Bhima, Yudhishthira ke dukh, Arjuna ka roop, Sahadeva ki peeda aur Nakula ki haalat dekhkar mera hriday roz toot jaata hai.”

“Fir bhi aap kaise soch sakte hain ki main sukhi hoon?”

“Jab aap sab jeevit hote hue bhi itne dukh sah rahe hain, tab mera jeevan bhi dukh se bhar gaya hai.”

Draupadi ki har baat mein gehra prem, dard aur apmaan chhupa hua tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.6
        with st.expander("Section 4.3.6  Section XIX"):
            text1 = """ 
            Draupadi aansuon ke saath Bhima se boli,

“Hey Bhimasena, us paase ke khel ki wajah se aaj main Rani Sudeshna ki daasi bankar jee rahi hoon.”

“Main ek rajkumari hokar bhi Sairindhri ke roop mein doosron ki seva kar rahi hoon.”

“Bas isi aasha mein jee rahi hoon ki ek din hamara dukh samaapt hoga aur Pandav fir se apna rajya paayenge.”

Draupadi ne dukhi swar mein kaha,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Duniya mein sukh aur dukh chakr ki tarah ghoomte rehte hain.”

“Aaj dukh hai, toh kal sukh bhi aa sakta hai.”

“Isi umeed par main ab tak jee rahi hoon.”

“Bhagya bahut balwaan hota hai.”

“Jo daan deta hai, kabhi-kabhi wahi maangne par majboor ho jaata hai.”

“Jo doosron ko haraata hai, kabhi khud bhi haar jaata hai.”

“Koi bhi apni kismat ko poori tarah nahi badal sakta.”

Fir Draupadi ne gehri saans lekar kaha,

“Main Drupad ki putri aur Pandavo ki patni hoon.”

“Fir bhi aaj itna apmaan aur dukh sah rahi hoon.”

“Mere paas pati, putra aur apne log sab hote hue bhi main akeli aur dukhi hoon.”

“Shayad maine pichhle janm mein koi bada paap kiya hoga, isi liye mujhe yeh sab dekhna pad raha hai.”

Draupadi ne Bhima ko apne haath dikhaye.

Unke komal haathon par ghisav aur kathorpan aa gaya tha.

Woh boli,

“Hey Bhima, pehle maine kabhi apne liye bhi chandan nahi peesa tha.”

“Lekin aaj main doosron ke liye chandan pees rahi hoon.”

“Dekhiye, mere haath kitne kathor ho gaye hain.”

“Jo stree kabhi kisi se nahi darti thi, aaj woh Raja Virata aur Sudeshna se bhay mein rehti hai.”

“Main hamesha darrti rehti hoon ki kahin mujhse koi galti na ho jaaye.”

Draupadi rote hue boli,

“Jo kabhi poori dharti ki rani thi, aaj doosron ke peeche chalne ko majboor hai.”

“Samay ne hamare jeevan ko kitna badal diya hai.”

Rishi Vaisampayana bole, “Apne dukh bataate-bataate Draupadi chupchaap rone lagi.”

Unki awaaz aansuon se bhar gayi.

Woh boli,

“Hey Bhima, shayad devta bhi mujhse naraaz hain.”

“Itna sab sahne ke baad bhi main abhi tak jeevit hoon.”

Yeh sunkar Bhima ka hriday dukh aur krodh se bhar gaya.

Unhone Draupadi ke kathor ho chuke haathon ko apne haathon mein liya.

Bhima ki aankhon se bhi aansu behne lage.

Woh apni priya patni ka dukh aur apmaan ab aur zyada bardasht nahi kar paa rahe the."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.7
        with st.expander("Section 4.3.7  Section XX"):
            text1 = """ 
            Bhima ka hriday Draupadi ka dukh sunkar krodh se bhar gaya.

Woh bole,

“Dhikkaar hai meri baahuon ki shakti par!”

“Dhikkaar hai Arjuna ke Gandiva dhanush par!”

“Tumhare komal haath jo pehle laal aur sundar the, aaj un par kathor ghatte pad gaye hain.”

“Jab Keechak ne sabha mein tumhe laat maari, tab mera mann hua tha ki main poori Matsya sena ka vinaash kar doon.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Lekin Yudhishthira bhaiya ne aankhon hi aankhon mein mujhe rok diya.”

“Isi liye main shaant raha.”

Bhima gusse se bole,

“Rajya khona, Duryodhana aur Dushasan ko abhi tak zinda dekhna, aur Shakuni jaise dushton ko na maar paana — yeh sab mere hriday ko roz jalaata hai.”

“Yeh dard mere andar teer ki tarah chubhta rehta hai.”

Fir Bhima ne Draupadi ko shaant karte hue kaha,

“Hey Krishnaa, itna krodh mat karo.”

“Agar Yudhishthira tumhari yeh kathin baatein sun lenge, toh unka hriday toot jaayega.”

“Aur agar Arjuna, Nakula ya Sahadeva bhi yeh sun lenge, toh woh bhi jeena nahi chahenge.”

“Tum thoda aur dhairya rakho.”

Bhima ne Draupadi ko purani mahan streeon ki yaad dilaayi.

Woh bole,

“Sukanya ne budhe Rishi Chyavan ka saath nahi chhoda.”

“Savitri ne apne pati Satyavan ko bachane ke liye Yamraj tak ka saamna kiya.”

“Sita Mata ne Bhagwan Ram ke saath vanvaas saha.”

“Waise hi tum bhi dhairya aur pavitrata ki moorti ho.”

“Bas thoda samay aur sah lo.”

“Jab yeh agyaatvaas samaapt hoga, tab tum fir se rani banogi.”

Draupadi ne aansu pochhte hue kaha,

“Hey Bhima, main Yudhishthira ko dosh nahi deti.”

“Lekin Keechak har din mujhe pareshan karta hai.”

“Main use baar-baar kehti hoon ki mere paanch Gandharva pati hain jo use maar daalenge.”

“Lekin woh hamesha hanskar kehta hai ki use Gandharvon se koi darr nahi.”

“Woh kehta hai ki woh hazaaron Gandharvon ko bhi maar sakta hai.”

Draupadi boli,

“Jab Rani Sudeshna ne mujhe uske mahal bheja, tab usne pehle meethi baatein ki.”

“Fir jab maine mana kiya, toh usne zabardasti karni chahi.”

“Main darrkar rajsabha ki taraf bhaagi.”

“Lekin usne sabke saamne mujhe gira diya aur laat maari.”

“Raja Virata aur Yudhishthira sab dekhte rahe, lekin kisi ne use roka nahi.”

Draupadi ka swar kaampne laga.

Woh boli,

“Keechak paapi, ahankaari aur kaami hai.”

“Woh doosron ka dhan cheenta hai aur kisi ki parwah nahi karta.”

“Agar woh fir se mujhe chhoone ki koshish karega, toh main apni jaan de dungi.”

“Main kabhi bhi uske saamne jhukungi nahi.”

“Hey Bhima, jaise aapne Jatasur aur Jayadrath se meri raksha ki thi, waise hi ab Keechak ko bhi maar dijiye.”

“Us dusht ko mitti ke ghade ki tarah pathar par phod dijiye.”

“Kal suraj ugne se pehle agar Keechak zinda raha, toh main vish peeke apni jaan de dungi.”

Itna kehkar Draupadi roti hui Bhima ke seene se lag gayi.

Rishi Vaisampayana bole, “Bhima ne Draupadi ko apni baahon mein sambhaala aur unke aansu pochhe.”

Lekin andar hi andar unka krodh agni ki tarah bhadak raha tha.

Woh baar-baar apne honton ko dabaa rahe the aur mann hi mann Keechak ke vinaash ka soch rahe the."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.8
        with st.expander("Section 4.3.8  Section XXI"):
            text1 = """ 
            Bhima ne Draupadi ki baat sunkar gehri awaaz mein kaha,

“Hey Krishnaa, main tumhari ichchha zaroor poori karunga.”

“Main aaj hi Keechak aur uske saathiyon ka vinaash kar dunga.”

“Tum kal shaam kisi tarah Keechak ko nritya shala mein bula lo.”

“Din mein wahan rajkumariyaan nritya karti hain, lekin raat ko woh jagah khaali rehti hai.”

“Wahin ek bada lakdi ka palang rakha hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Usi jagah main Keechak ko uske purkhon ke paas bhej dunga.”

“Lekin dhyaan rahe, kisi ko tumhari aur uski baat ka pata nahi chalna chahiye.”

Rishi Vaisampayana bole, “Dono ne poori raat dukh aur gusse mein bitaayi.”

Subah hote hi Keechak fir Draupadi ke paas gaya.

Ahankaar se bhar kar woh bola,

“Kal maine sabke saamne tumhe laat maari, lekin koi tumhari raksha nahi kar saka.”

“Virata naam ka raja hai, lekin asli shakti toh mere paas hai.”

“Tum meri patni ban jaao.”

“Main tumhe dhan, daasiyaan aur har sukh dunga.”

Draupadi ne shaant swar mein kaha,

“Thik hai, lekin hamari mulaqat ka pata kisi ko nahi chalna chahiye.”

“Mere Gandharva pati bahut bhayankar hain.”

“Raat ko nritya shala mein akele aana.”

“Koi bhi wahan nahi aata.”

Keechak yeh sunkar bahut khush ho gaya.

Woh samajh hi nahi paaya ki uski maut uska intezaar kar rahi hai.

Poora din woh sugandh, gehne aur sundar vastra pehenkar khud ko sajaata raha.

Udhar Draupadi chupke se Bhima ke paas gayi aur boli,

“Hey Bhima, maine Keechak ko nritya shala mein bula liya hai.”

“Woh raat ko akela aayega.”

“Ab aap us paapi ka ant kar dijiye.”

Bhima muskuraakar bole,

“Tumne mujhe bahut khushkhabri di hai.”

“Jitni khushi mujhe Hidimbasur ko maarte waqt hui thi, utni hi aaj ho rahi hai.”

“Main shapath leta hoon ki aaj Keechak ko zaroor maarunga.”

“Chahe chupkar ya saamne se, uska vinaash nishchit hai.”

Draupadi ne fir kaha,

“Lekin dhyaan rahe, hamara agyaatvaas tootna nahi chahiye.”

“Isliye use chupke se maarna.”

Bhima bole,

“Chinta mat karo.”

“Main us dusht ka sir haathi ki tarah kuchal dunga.”

Rishi Vaisampayana bole, “Raat hote hi Bhima pehle hi nritya shala mein pahunch gaye.”

Woh andhere mein chupkar sher ki tarah apne shikaar ka intezaar karne lage.

Kuch der baad Keechak saj-dhaj kar wahan aaya.

Woh mann hi mann Draupadi ke baare mein sochkar khush ho raha tha.

Andhere mein usne Bhima ko palang par lete dekha aur samjha ki woh Draupadi hai.

Woh madhur shabdon mein bola,

“Hey sundari, main tumhare liye dhan, mahal aur daasiyaan sab lekar aaya hoon.”

“Duniya ki streeon ne bhi meri sundarta ki prashansa ki hai.”

Tab Bhima gehri awaaz mein bole,

“Haan, tum bahut sundar ho.”

“Aur tumhe sparsh ka bhi bada gyaan hai.”

“Tumhare jaisa koi nahi.”

Itna kehkar Bhima achanak uth khade hue.

Unki aankhen krodh se jal rahi thi.

Woh garajkar bole,

“Hey paapi Keechak! Aaj tumhari behen tumhe sher ke haath se mare hue haathi ki tarah zameen par pada dekhegi!”

“Tumhare marne ke baad Draupadi aur hum sab chain se jee paayenge!”

Itna kehkar Bhima ne Keechak ke baal pakad liye.

Keechak bhi bahut balwaan tha.

Dono ke beech bhayanak yudh shuru ho gaya.

Kabhi woh ek doosre ko dhakka dete, kabhi zameen par patakte.

Unki garaj aur takkar ki awaaz se poori nritya shala kaampne lagi.

Woh do jangli haathiyon ya do sher jaise lad rahe the.

Keechak ne bhi poori shakti lagaayi aur ek baar Bhima ko gira diya.

Lekin Bhima turant uth khade hue.

Fir Bhima ne apni mahaan shakti se Keechak ko zor se pakad liya.

Unhone use baar-baar patka aur uska gala daba diya.

Keechak dheere-dheere kamzor padne laga.

Bhima ne use zor se ghumaaya aur uske sharir ki saari haddiyan tod di.

Aakhir mein Bhima ne uske haath, pair aur gardan kuchal kar uska sharir maans ke gole jaisa bana diya.

Keechak wahi mar gaya.

Bhima garajkar bole,

“Is paapi ko maar kar maine Draupadi ke apmaan ka badla le liya.”

Fir Bhima ne Draupadi ko bulaaya aur kaha,

“Hey Panchali, aakar dekho iss kaami dusht ka kya haal hua.”

Draupadi ne Keechak ka vinaash dekhkar gehri rahat mehsoos ki.

Bhima bole,

“Jo bhi tum par buri nazar daalega, uska yahi haal hoga.”

Uske baad Bhima chupchaap wapas rasoi mein chale gaye.

Draupadi ne nritya shala ke rakshakon ko bulaakar kaha,

“Aao aur dekho, jo doosron ki stree par buri nazar daalta hai, uska kya anjaam hota hai.”

Rakshak mashaal lekar andar aaye.

Keechak ki laash dekhkar sab darr gaye.

Uska sharir pehchaan mein bhi nahi aa raha tha.

Sab hairaan hokar bole,

“Yeh kaam kisi aam insaan ka nahi ho sakta.”

“Zaroor ise kisi Gandharva ne maara hai.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.9
        with st.expander("Section 4.3.9  Section XXII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Jab Keechak ke rishtedaar nritya shala mein pahunche, toh unhone uski bhayanak haalat dekhi.”

Uska sharir poori tarah kuchla hua tha.

Sab log darr aur shok se kaamp uthe.

Woh zor-zor se rote hue bole,

“Yeh zaroor kisi Gandharva ka kaam hai!”

Fir unki nazar paas khadi Draupadi par padi."""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Gusse mein bhare hue Keechak ke rishtedaar chillaye,

“Isi stree ki wajah se Keechak mara hai!”

“Isse bhi Keechak ke saath jala dena chahiye!”

“Yahi uske liye sahi dand hoga!”

Woh Raja Virata ke paas gaye aur bole,

“Hey Raja, Keechak Draupadi ke kaaran mara hai.”

“Isliye ise bhi Keechak ke saath chita par jalaane ki anumati dijiye.”

Raja Virata Keechak ke parivaar aur unki shakti se darte the.

Isliye unhone chupchaap haan kar di.

Rishi Vaisampayana bole, “Yeh sunkar Keechak ke rishtedaar Draupadi ko zabardasti pakadkar baandhne lage.”

Woh bechari Draupadi ko Keechak ki arthi par rakhkar shamshaan ki taraf le gaye.

Draupadi bahut dukhi aur bhaybheet ho gayi.

Woh zor-zor se apne patiyon ko pukaarne lagi,

“Hey Jaya! Hey Jayant! Hey Vijaya! Hey Jayatsena! Hey Jayadbala!”

“Mujhe yeh Soot log zabardasti le ja rahe hain!”

“Hey mere veer Gandharva pati, meri raksha kijiye!”

Rishi Vaisampayana bole, “Draupadi ki dard bhari awaaz Bhima ne sun li.”

Bhima turant uth khade hue aur bole,

“Hey Sairindhri, ab tumhe darrne ki zarurat nahi.”

“Main aa gaya hoon.”

Bhima ka krodh fir se agni ki tarah bhadak utha.

Woh chupke se mahal se baahar nikle aur tez gati se shamshaan ki taraf daude.

Raaste mein unhe ek bahut bada ped dikha.

Bhima ne use jad se ukhaad liya aur kandhe par rakh liya.

Woh Yamraj ki tarah gusse mein bhare hue Keechak ke rishtedaaron ki taraf badhe.

Jab Soot logon ne Bhima ko dekha, toh woh darr se kaamp uthe.

Woh ek doosre se bole,

“Yeh toh wahi bhayankar Gandharva lagta hai!”

“Jaldi Draupadi ko chhod do!”

Dar ke maare unhone Draupadi ko turant chhod diya aur bhaagne lage.

Lekin Bhima ne unhe nahi chhoda.

Woh bade ped se un par toot pade.

Ek-ek karke unhone sabko maar giraaya.

Kul milakar Bhima ne Keechak ke 105 rishtedaaron ko maar daala.

Shamshaan bhoomi unki laashon se bhar gayi.

Woh jagah aise lag rahi thi jaise aandhi mein poora jungle tootkar gir gaya ho.

Uske baad Bhima ne Draupadi ko santvana di aur bole,

“Hey Krishnaa, jo bina wajah tumhara apmaan karega, uska yahi haal hoga.”

“Ab tum bina darr ke wapas nagar jaao.”

“Main doosre raaste se rasoi mein laut jaaunga.”

Rishi Vaisampayana bole, “Keechak aur uske 105 rishtedaaron ka vinaash dekhkar sab log hairaan reh gaye.”

“Sabko poora vishwas ho gaya ki Draupadi ki raksha sach mein shaktishaali Gandharva karte hain.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.10
        with st.expander("Section 4.3.10  Section XXIII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Jab logon ne Keechak aur uske 105 rishtedaaron ki laashen dekhin, toh poori nagari darr se bhar gayi.”

Sab log Raja Virata ke paas jaakar bole,

“Hey Raja, Gandharvon ne sab Sooton ko maar daala hai.”

“Unki laashen zameen par aise padi hain jaise bijli girne se bade-bade pahaad toot gaye hon.”

“Sairindhri bhi wapas mahal ki taraf aa rahi hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Lekin agar woh yahaan rahi, toh Gandharvon ke krodh se poora rajya khatre mein pad sakta hai.”

“Woh bahut sundar hai aur Gandharva uski raksha karte hain.”

“Kripya jaldi koi upaay sochiye.”

Raja Virata yeh sunkar aur bhi darr gaye.

Unhone kaha,

“Keechak aur sab Sooton ka antim sanskaar ek saath kiya jaaye.”

“Unki chita sugandhit tel aur ratnon se sajaayi jaaye.”

Fir Virata ne darr ke saath Rani Sudeshna se kaha,

“Jab Sairindhri wapas aaye, toh usse keh dena ki woh jahaan chahe chali jaaye.”

“Main Gandharvon ke darr se usse yeh baat khud nahi keh sakta.”

“Woh bahut sundar hai aur uske rakshak bahut bhayankar hain.”

Rishi Vaisampayana bole, “Udhar Draupadi, Bhima dwara bachaye jaane ke baad, apne kapde aur sharir saaf karke dheere-dheere nagar ki taraf laut rahi thi.”

Woh aise lag rahi thi jaise koi hiran sher ke darr se bachkar aa rahi ho.

Jab nagar ke logon ne unhe dekha, toh sab Gandharvon ke darr se idhar-udhar bhaagne lage.

Kuch logon ne toh aankhen tak band kar li.

Rasoi ke dwar par Draupadi ne Bhima ko dekha.

Bhima chupchaap wahin khade the, ek krodhit haathi ki tarah.

Draupadi ne sanket bhari bhaasha mein kaha,

“Main us Gandharva rajkumar ko pranam karti hoon jisne meri raksha ki.”

Bhima samajh gaye aur dheere se bole,

“Ab jo log tumhe pareshan karte the, woh sab apne karm ka phal paa chuke hain.”

Uske baad Draupadi nritya shala ki taraf gayi.

Wahan Arjuna Brihannala ke roop mein rajkumariyon ko nritya aur sangeet sikha rahe the.

Rajkumariyaan Draupadi ke paas aakar khushi se boli,

“Hey Sairindhri, achha hua tum surakshit wapas aa gayi.”

“Achha hua un paapi Sooton ko dand mil gaya.”

Tab Brihannala bane Arjuna ne poocha,

“Hey Sairindhri, tum kaise bach gayi?”

“Aur un dushton ka vinaash kaise hua?”

Draupadi dukh bhari halki muskaan ke saath boli,

“Hey Brihannala, tum toh hamesha rajkumariyon ke beech khushi se rehti ho.”

“Tum mere dukh ko kaise samajh paogi?”

Arjuna shaant swar mein bole,

“Hey sundari, Brihannala ke apne dukh bhi bahut gehre hain.”

“Koi bhi doosre ke hriday ka poora dard nahi samajh sakta.”

“Isliye tum mere mann ki peeda nahi jaan paati.”

Rishi Vaisampayana bole, “Uske baad Draupadi Rani Sudeshna ke paas pahunchi.”

Sudeshna ne Raja Virata ka sandesh dete hue kaha,

“Hey Sairindhri, tum jahaan chaaho chali jaao.”

“Raja Gandharvon ke krodh se bahut dare hue hain.”

“Tum bahut sundar ho aur Gandharva tumhari raksha karte hain.”

Draupadi ne vinamrata se jawab diya,

“Hey Rani, bas mujhe terah din aur yahaan rehne dijiye.”

“Uske baad Gandharva mujhe yahaan se le jaayenge.”

“Agar aap itna karengi, toh Gandharva bhi Raja Virata par prasann honge aur unka bhala hoga.”

Rishi Vaisampayana bole, “Draupadi ne bahut dhairya aur buddhi se apni baat kahi, aur sab log chupchaap unki baatein sunte rahe.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.3.11
        with st.expander("Section 4.3.11  Section XXIV"):
            text1 = """ 
            Rishi Vaisampayana bole, “Keechak aur uske bhaiyon ke mare jaane ki khabar poore desh mein phail gayi.”

Log hairaan hokar ek doosre se kehne lage,

“Keechak bahut balwaan tha.”

“Lekin woh dusht aur ahankaari bhi tha.”

“Woh logon par atyachaar karta tha aur doosron ki streeon ka apmaan karta tha.”

“Isi paap ke kaaran Gandharvon ne uska vinaash kar diya.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Is tarah har jagah Keechak ki maut ki charcha hone lagi.

Udhar Duryodhana ke bheje hue guptchar bhi apni khoj poori karke laut aaye.

Unhone jungle, pahaad, gaon, nagar aur anek rajyon mein Pandavo ko dhoondha tha.

Lekin unhe Pandavo ka koi pata nahi mila.

Sab guptchar Hastinapur pahunchkar Duryodhana ke saamne khade hue.

Us samay wahan Bhishma, Dronacharya, Karna, Kripacharya aur Trigart desh ke raja bhi maujood the.

Guptchar bole,

“Hey Maharaj Duryodhana, humne Pandavo ko dhoondhne mein koi kami nahi chhodi.”

“Humne ghane jungle, pahaadi ilaake, shehar aur rajya sab jagah khoj ki.”

“Humne unke pairon ke nishaan tak dhoondhne ki koshish ki.”

“Lekin hum Pandavo tak nahi pahunch sake.”

“Lagta hai woh bina koi nishaan chhode gaayab ho gaye hain.”

Guptcharon ne aage kaha,

“Humne unke rath chalakon ka peecha bhi kiya.”

“Woh Dwaraka pahunch gaye, lekin Pandav unke saath nahi the.”

“Na Pandav aur na Draupadi Dwaraka mein mile.”

“Isliye humein samajh nahi aa raha ki woh iss samay kahaan reh rahe hain.”

Fir guptchar khush hokar bole,

“Lekin hum ek achhi khabar lekar aaye hain.”

“Matsya desh ka senapati Keechak maara gaya hai.”

“Wahi Keechak jo Trigarton ko baar-baar haraata tha.”

“Raat ke samay kisi adrishya Gandharva ne use aur uske bhaiyon ko maar daala.”

“Yeh sunkar humein bahut khushi hui, kyunki woh hamara shatru tha.”

“Ab aap humein batayein ki aage kya karna hai.”

Rishi Vaisampayana bole, “Duryodhana aur uske saathi yeh sab sunkar gehri soch mein pad gaye.”

Unhe ab bhi shaq tha ki Pandav kahin na kahin jeevit hain aur gupt roop mein reh rahe hain."""
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
            text1 = """ 
            Rishi Vaisampayana bole, “Guptcharon ki baatein sunkar Duryodhana kuch der tak gehri soch mein doob gaya.”

Fir woh apne sabha ke logon se bola,

“Pandavo ka pata lagana bahut mushkil ho raha hai.”

“Unke agyaatvaas ka adhiktar samay ab beet chuka hai.”

“Bas thoda samay hi baaki hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Agar woh yeh samay bina pehchaane poora kar lenge, toh apna vachan poora kar lenge.”

“Uske baad woh gusse se bhare hue shaktishaali haathiyon aur zehreeli saanpon ki tarah lautenge.”

“Fir woh Kauravo ko kathin dand denge.”

Duryodhana ne chinta bhare swar mein kaha,

“Isliye humein bina deri kiye aisa upaay karna hoga ki Pandav fir se jungle jaane par majboor ho jaayein.”

“Humein apne rajya ko surakshit aur shatruon se mukt rakhna hai.”

Tab Karna bola,

“Hey Maharaj, aur bhi zyada chatur aur kushal guptchar bhejne chahiye.”

“Woh alag-alag roop dhaaran karke bade rajyon aur shehron mein khoj karein.”

“Rajmahalon ke andar, mandiron mein, teerth sthalon par aur gupt jagahon par Pandavo ko dhoondha jaaye.”

“Jungle, pahaad, nadiyon ke kinaare aur rishiyon ke aashram tak sab jagah talaash honi chahiye.”

“Pandav kahin na kahin gupt roop mein zaroor reh rahe honge.”

Karna ki baat ke baad Dushasan bola,

“Hey bhaiya, mujhe bhi Karna ki baat sahi lagti hai.”

“Hum apne vishwas-paatra guptcharon ko fir se bhejte hain.”

“Unhe pehle hi inaam de diya jaaye, taaki woh poori lagan se kaam karein.”

Fir Dushasan thodi hansi ke saath bola,

“Lekin mujhe lagta hai ki Pandavo ka pata lagana aasaan nahi hoga.”

“Ho sakta hai woh kahin gehri jagah chhupe hon.”

“Ya samundar ke paar chale gaye hon.”

“Ya shayad jungle ke jaanwaron ne unhe maar diya ho.”

“Ho sakta hai woh kisi bade sankat mein padkar mar hi gaye hon.”

“Isliye, hey Maharaj, zyada chinta mat kijiye.”

“Aap apni ichchha ke anusaar rajya ka aanand lijiye.”

Rishi Vaisampayana bole, “Lekin Duryodhana ke mann se Pandavo ka darr poori tarah gaya nahi tha.”

“Usse lag raha tha ki Pandav jeevit hain aur sahi samay ka intezaar kar rahe hain.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.2
        with st.expander("Section 4.4.2  Section XXVII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Dronacharya bahut buddhimaan aur door ki soch rakhne wale the.”

Unhone Duryodhana ki sabha mein shaant swar mein kaha,

“Pandav jaise veer aasaani se naash nahi hote.”

“Woh bahadur, gyaani aur har kala mein nipun hain.”

“Unka mann aur indriyan hamesha niyantran mein rehte hain.”

“Woh satya aur dharm ka paalan karte hain.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Dronacharya ne aage kaha,

“Sabse badi baat yeh hai ki woh sab Yudhishthira ka samman aur aagya maante hain.”

“Yudhishthira apne chhote bhaiyon se pita ki tarah prem karte hain.”

“Woh kabhi kisi ka bura nahi chahte.”

“Aur unke bhai bhi unke prati poori shraddha aur wafadaari rakhte hain.”

“Jo bhai itne ekjut aur dharm par chalne wale hon, unka vinaash aasaan nahi hota.”

Drona bole,

“Yudhishthira neeti aur samay ko achhi tarah samajhte hain.”

“Pandav iss samay shaant hain, lekin woh bas sahi avsar ka intezaar kar rahe hain.”

“Jab samay aayega, woh apni shakti aur rajya fir se prapt kar lenge.”

“Isliye yeh sochna galat hoga ki woh mar gaye hain.”

Dronacharya ne gambhir swar mein kaha,

“Pandav bahut tejasvi aur pavitra hain.”

“Yudhishthira toh apni aankhon ke tej se hi shatruon ko jala dene ki shakti rakhte hain.”

“Unhe agyaatvaas ke samay dhoondhna bahut kathin hai.”

“Woh buddhi aur dhairya se kaam le rahe hain.”

Fir Drona ne salaah di,

“Isliye humein fir se unki talaash karni chahiye.”

“Is baar aise log bhejne chahiye jo buddhimaan aur anubhav se bharpoor hon.”

“Brahman, Charan aur tapasvi rishiyon ko bhi bhejna chahiye.”

“Ho sakta hai unmein se kisi ko Pandavo ke baare mein kuch pata ho.”

Rishi Vaisampayana bole, “Dronacharya ki baatein sunkar sabha mein baithe log gehri soch mein pad gaye.”

“Kuch logon ko ab bhi vishwas tha ki Pandav jaldi hi phir saamne aayenge.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.3
        with st.expander("Section 4.4.3  Section XXVIII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Dronacharya ki baat ke baad Bhishma Pitamah ne bhi sabha mein apni baat kahi.”

Bhishma bahut gyaani aur dharm ko samajhne wale the.

Unhone shaant swar mein kaha,

“Main Dronacharya ki baat se poori tarah sehmat hoon.”

“Pandav jaise veer aur dharmic log kabhi aasaani se vinaash nahi hote.”

“Woh satya, dharm aur maryada ka paalan karne wale hain.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Woh bade buzurgon ka samman karte hain aur Shri Krishna ke prati wafadaar hain.”

“Isliye mushkilon ke baad bhi woh kabhi toot nahi sakte.”

Bhishma ne Duryodhana ki taraf dekhkar kaha,

“Pandav iss samay gupt roop mein reh rahe hain.”

“Lekin woh apni shakti aur buddhi ke bal par surakshit hain.”

“Unhe dhoondhne ke liye jasoos bhejna kisi buddhimaan raja ki neeti nahi honi chahiye.”

“Main tumse bair ki wajah se nahi, balki sachchai aur dharm ke anusaar baat kar raha hoon.”

Bhishma bole,

“Jo vyakti satya aur dharm ka paalan karta hai, use sabha mein bhi sach hi bolna chahiye.”

“Isi liye main tum sabse alag soch rakhta hoon.”

Fir Bhishma ne Yudhishthira ki mahanta bataayi.

Woh bole,

“Jahaan Yudhishthira rehte hain, wahan ke log dayalu, vinamr aur sachche hote hain.”

“Wahan log apna kartavya imaandari se nibhaate hain.”

“Wahan log ek doosre se prem aur madhurta se baat karte hain.”

“Wahan jhooth, ghamand aur dvesh kam ho jaata hai.”

Bhishma ne aage kaha,

“Jahaan Yudhishthira rehte hain, wahan yagya aur daan hote hain.”

“Brahmanon ka samman hota hai.”

“Barish samay par hoti hai aur kheton mein achhi fasal ugti hai.”

“Phal ras se bhare hote hain aur phool sugandhit hote hain.”

“Gaayen swasth aur doodh se bhari hoti hain.”

“Logon ke mann shaant aur prasann rehte hain.”

“Wahan ka vaataavaran bhi sukh aur shaanti se bhara hota hai.”

Bhishma ne gehri awaaz mein kaha,

“Yudhishthira mein buddhi, daya, kshama aur sab praniyon ke prati prem hai.”

“Aise mahan vyakti ko dhoondhna bahut kathin hai.”

“Brahman aur tapasvi log bhi unhe aasaani se nahi pehchaan sakte.”

Fir Bhishma bole,

“Pandav kisi aise hi shubh aur dharmic desh mein reh rahe honge.”

“Ab tum dhairya aur buddhi se socho ki tumhe kya karna chahiye.”

Rishi Vaisampayana bole, “Bhishma Pitamah ki sachchai aur dharm bhari baatein sunkar sabha mein sannata chha gaya.”

“Kai log mann hi mann samajh gaye ki Pandav ab bhi surakshit aur jeevit hain.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.4
        with st.expander("Section 4.4.4  Section XXIX"):
            text1 = """ 
            Rishi Vaisampayana bole, “Bhishma Pitamah ke baad Kripacharya ne bhi apni baat rakhi.”

Woh bole,

“Bhishma ji ne jo kaha, woh bilkul sahi aur dharm ke anusaar hai.”

“Unki baatein buddhi aur neeti se bhari hui hain.”

“Lekin meri bhi ek salaah hai.”

Kripacharya ne Duryodhana se kaha,

“Pandavo ko halka shatru samajhne ki galti kabhi mat karna.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Jo raja apni bhalai chahta hai, woh chhote se chhote shatru ko bhi nazarandaaz nahi karta.”

“Fir Pandav toh mahaan yoddha hain aur har astra-shastra mein nipun hain.”

Woh aage bole,

“Pandavo ka agyaatvaas ab lagbhag samaapt hone wala hai.”

“Jab woh lautenge, tab bahut shakti aur utsaah ke saath lautenge.”

“Isliye abhi se taiyaari karna samajhdari hogi.”

Kripa ne samjhaaya,

“Tumhe apni sena aur khazaane ko aur mazboot banana chahiye.”

“Apne mitron aur anya rajyon ki shakti bhi jaan leni chahiye.”

“Kaun tumhare saath wafadaar hai aur kaun mann se tumhare khilaaf hai, yeh sab samajhna zaroori hai.”

“Buddhimaan raja wahi hota hai jo samay se pehle taiyaar ho jaaye.”

Fir Kripacharya ne neeti ki baat bataayi.

Woh bole,

“Kabhi prem aur vinamrata se kaam lena chahiye.”

“Kabhi daan aur uphaar se logon ko apni taraf karna chahiye.”

“Aur zarurat pade toh dand aur yuddh ka bhi sahara lena chahiye.”

“Kamzor shatru ko bal se haraya ja sakta hai, lekin apne saathiyon ko madhur shabdon se jeetna chahiye.”

Kripa bole,

“Jab sena mazboot ho aur khazaana bhara ho, tab bade se bada shatru bhi daraaya ja sakta hai.”

“Fir Pandavo se saamna karna bhi aasaan ho jaayega.”

“Isliye neeti aur dhairya ke saath kaam karo.”

“Isi mein tumhari bhalai hai.”

Rishi Vaisampayana bole, “Kripacharya ki baatein sunkar sab log gehri soch mein pad gaye.”

“Sabko samajh aa raha tha ki Pandavo ke wapas aane ka samay ab kareeb hai.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.5
        with st.expander("Section 4.4.5  Section XXX"):
            text1 = """ 
            Rishi Vaisampayana bole, “Trigart desh ka raja Susharma pehle bhi kai baar Keechak se haar chuka tha.”

Ab jab Keechak mar chuka tha, toh usse laga ki Virata par hamla karne ka yeh sahi samay hai.

Woh turant Duryodhana ki sabha mein bola,

“Hey Maharaj, Matsya desh ne kai baar mere rajya par hamla kiya tha.”

“Unki sena ka sabse bada bal Keechak tha.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Woh bahut kroor, ghamandi aur balwaan tha.”

“Lekin ab Gandharvon ne uska vinaash kar diya hai.”

“Ab Raja Virata kamzor aur dara hua hoga.”

Susharma ne lalach bhare swar mein kaha,

“Isliye humein abhi turant Matsya desh par hamla kar dena chahiye.”

“Hum unka dhan, gaayen aur rajya sab loot sakte hain.”

“Ya unhe haraakar apne adheen kar sakte hain.”

“Yeh hamare liye bahut achha avsar hai.”

Fir Karna ne bhi Susharma ki baat ka samarthan kiya.

Woh bola,

“Susharma bilkul sahi keh raha hai.”

“Yeh samay hamare liye laabhdayak hai.”

“Humein apni sena taiyaar karke turant Matsya desh ki taraf badhna chahiye.”

Karna ne ahankaar se kaha,

“Pandavo ki chinta karne ki koi zarurat nahi.”

“Woh ab na dhanwaan rahe aur na shaktishaali.”

“Ho sakta hai woh mar bhi chuke hon.”

“Isliye bina darr ke Virata ka dhan aur gaayen le leni chahiye.”

Duryodhana ko bhi yeh baat pasand aayi.

Usne turant Dushasan ko aadesh diya,

“Buzurgon se salaah lekar sena ko turant taiyaar karo.”

“Susharma pehle apni sena lekar gupt roop se Matsya desh ki taraf jaaye.”

“Hum ek din baad apni poori sena ke saath uske peeche chalenge.”

“Trigart sena achanak hamla karke Virata ki gaayen chura legi.”

“Uske baad hum bhi hazaaron gaayen apne kabze mein kar lenge.”

Rishi Vaisampayana bole, “Duryodhana ka aadesh milte hi Trigart sena yuddh ke liye nikal padi.”

Woh Matsya desh ki taraf badhne lage, taaki Virata ki gaayen loot saken.

Saptami ke din Susharma apni sena lekar nikal gaya.

Aur uske agle din Kaurav sena bhi hazaaron sainikon ke saath Matsya desh ki ओर badh chali."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 4.4.6
        with st.expander("Section 4.4.6  Section XXXI"):
            text1 = """ 
            Rishi Vaisampayana bole, “Pandavo ne Virata nagari mein apna agyaatvaas safalta se poora kar liya tha.”

“Keechak ke marne ke baad Raja Virata ko Pandavo par aur bhi adhik bharosa hone laga.”

Isi samay Trigart raja Susharma ne Virata ki hazaaron gaayen chura li.

Gaay charane waale log ghabraakar rajsabha mein aaye aur bole,

“Hey Maharaj, Trigart sena hamari gaayen lootkar le ja rahi hai!”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Kripya turant unhe bachaiye.”

Yeh sunkar Raja Virata ne turant yuddh ki taiyaari ka aadesh diya.

Poore Matsya desh mein yuddh ki taiyaari shuru ho gayi.

Rath, haathi, ghode aur sainik sajne lage.

Sab yoddha chamakte hue kavach pehenkar yuddh ke liye taiyaar ho gaye.

Virata ke bhai Shatanika ne sone se saja hua mazboot kavach pehna.

Doosre veeron ne bhi apne-apne sundar aur balwaan kavach dhaaran kiye.

Khud Raja Virata ka kavach suraj ki tarah chamak raha tha.

Unke putra aur sena ke mahaan yoddha bhi shastra aur dhanush lekar taiyaar ho gaye.

Jald hi poori sena yuddh ke utsaah se bhar gayi.

Rathon par sundar dhwaj lehra rahe the.

Haathi garaj rahe the aur ghode tez awaaz kar rahe the.

Raja Virata ne fir apne bhai Shatanika se kaha,

“Mujhe lagta hai ki Kanka, Vallava, Tantripal aur Damagranthi bhi yuddh kar sakte hain.”

“Unhe bhi rath, kavach aur hathiyaar diye jaayein.”

“Unki baahuon aur roop ko dekhkar nahi lagta ki woh saamanya log hain.”

Yeh sunkar Shatanika ne turant Pandavo ke liye rath aur shastra taiyaar karwa diye.

Yudhishthira, Bhima, Nakula aur Sahadeva ne sundar aur mazboot kavach pehne.

Woh sab rath par baithkar Raja Virata ke peeche chal diye.

Unke chehre shaant the, lekin andar se woh mahaan yoddha jaag chuke the.

Rishi Vaisampayana bole, “Virata ki sena bahut bhavya lag rahi thi.”

Us sena mein hazaaron rath, haathi aur ghode the.

Sainik balwaan hathiyaar lekar gaayon ke nishaan ka peecha karte hue aage badh rahe the.

Door se woh sena aise lag rahi thi jaise samundar ki badi lehr dharti par chal rahi ho."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.7
        with st.expander("Section 4.4.7  Section XXXII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Virata ki sena nagar se nikal kar Trigart sena ke peeche badhi.”

Dopehar beet chuki thi jab dono senaein aamne-saamne aa gayin.

Matsya aur Trigart yoddha garaj uthe.

Dono paksh yuddh ke liye utsaah aur krodh se bhare hue the.

Fir bhayanak yuddh shuru ho gaya."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Haathiyon ko ankush aur lohe ke hathiyaaron se aage badhaya gaya.

Ghode daudne lage.

Rath tez awaaz ke saath ek doosre ki taraf badhe.

Rishi Vaisampayana bole, “Woh yuddh devtaon aur asuron ke purane yuddh ki tarah bhayanak lag raha tha.”

Sainik ek doosre par talwaar, bhale, gada aur teer barsaane lage.

Dhool itni zyada uddne lagi ki kisi ko kuch saaf dikh nahi raha tha.

Aasmaan teeron se bhar gaya.

Suraj bhi teeron aur dhool ke peeche chhup gaya.

Yoddha ek haath se doosre haath mein dhanush badal-badal kar teer chala rahe the.

Rath rathon se takra rahe the.

Ghudsawar ghudsawaron se lad rahe the.

Haathi haathiyon se bhid rahe the.

Zameen par kate hue haath, pair aur sir bikharne lage.

Khoon se yuddh bhoomi laal ho gayi.

Kayi yoddha behosh hokar gir pade.

Kuch log dosti aur rishton ko bhoolkar sirf maarne mein lage hue the.

Giddh aasman se neeche utarne lage, kyunki yuddh bhoomi laashon se bhar rahi thi.

Lekin itne bhayanak yuddh ke baad bhi koi sena doosri ko hara nahi paa rahi thi.

Virata ke bhai Shatanika ne shatru ke sau yoddha maar giraaye.

Veer Vishalaksha ne chaar sau yoddhaon ko hara diya.

Dono sena ke beech ghuskar bhayanak yuddh karne lage.

Kayi yoddha toh ek doosre ke baal pakadkar aur naakhunon se bhi ladne lage.

Udhar Raja Virata bhi bade parakram se lad rahe the.

Unhone anek rath aur ghodon ko nasht kar diya.

Fir unka saamna Trigart raja Susharma se hua.

Dono raja garajte hue ek doosre ki taraf badhe, bilkul do saandhon ki tarah.

Susharma chillakar bola,

“Hey Virata! Aao, hum dono akele yuddh karein!”

Fir dono ne apne rathon se ek doosre par teeron ki baarish kar di.

Virata ne Susharma ko das teer maare.

Unhone uske ghodon ko bhi ghaayal kar diya.

Lekin Susharma bhi bahut balwaan tha.

Usne Raja Virata ko pachaas teeron se bhed diya.

Dhool aur khoon se bhari yuddh bhoomi mein sainikon ko apne aur paraye ki pehchaan karna mushkil ho gaya.

Rishi Vaisampayana bole, “Yuddh aur bhi bhayanak hota ja raha tha, aur dono senaein poori shakti se lad rahi thi.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.8
        with st.expander("Section 4.4.8  Section XXXIII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Yuddh ke dauraan dhool aur andhera itna badh gaya ki dono senaein kuch der ke liye ruk gayin.”

Fir chand nikal aaya aur uski roshni se yuddh bhoomi dobara saaf dikhne lagi.

Jaise hi sab kuch dikhne laga, yuddh fir se shuru ho gaya.

Dono paksh aur bhi zyada gusse se ladne lage."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Trigart raja Susharma apne bhaiyon aur rathon ke saath seedha Raja Virata ki taraf badha.

Dono senaein gada, talwaar, bhale aur teeron se ek doosre par toot padi.

Fir Susharma ne bhayanak hamla kiya.

Usne Raja Virata ke ghodon ko maar giraaya.

Virata ka saarathi bhi maara gaya.

Virata ka rath toot gaya aur woh akela pad gaye.

Tab Susharma ne Raja Virata ko jeevit pakad liya aur apne rath par baithakar yuddh bhoomi se le jaane laga.

Yeh dekhkar Matsya sena darr gayi.

Kai sainik bhaagne lage.

Rishi Vaisampayana bole, “Tab Yudhishthira ne Bhima se kaha,”

“Hey Bhimasena, Raja Virata hamare upkaari hain.”

“Humne unke rajya mein sukh se agyaatvaas poora kiya hai.”

“Ab hamara kartavya hai ki hum unki raksha karein.”

“Tum turant jaakar unhe shatru ke haathon se chhudao.”

Bhima garajkar bole,

“Hey Maharaj, aaj aap mera parakram dekhiye.”

“Main iss bade ped ko ukhaadkar Trigarton ka vinaash kar dunga!”

Lekin Yudhishthira ne turant roka.

Woh bole,

“Hey Bhima, aisa mat karo.”

“Agar tum ped ukhaadoge, toh sab tumhe pehchaan lenge.”

“Log samajh jaayenge ki tum Bhima ho.”

“Koi saamanya hathiyaar lo aur manushya ki tarah yuddh karo.”

“Tumhare saath Nakula aur Sahadeva bhi rahenge.”

Bhima ne bade dhanush ko uthaya aur teeron ki baarish kar di.

Fir woh garajkar Susharma ki taraf badhe.

Woh chillaye,

“Ruko Susharma! Bhaago mat!”

Bhima ko Yamraj ki tarah apni taraf aata dekhkar Susharma ghabra gaya.

Usne mudkar fir se yuddh shuru kiya.

Lekin Bhima ne kuch hi palon mein uske anek rath, ghode aur sainik tod daale.

Yuddh bhoomi mein Bhima toofaan ki tarah lad rahe the.

Udhar Yudhishthira ne hazaar shatru maare.

Nakula ne saat sau aur Sahadeva ne teen sau yoddhaon ko hara diya.

Virata ke putra bhi bahaduri se ladne lage.

Bhima ne Susharma ke ghodon ko maar giraaya.

Uska saarathi bhi zameen par gira diya.

Rath bina saarathi ke ruk gaya.

Virata bhi gada lekar Susharma ke peeche daud pade.

Bhima ne fir Susharma ko lalkar kar kaha,

“Hey rajkumar! Bhaagna tumhe shobha nahi deta.”

“Tum itne kamzor hokar gaayen lootne aaye the?”

Susharma gusse mein Bhima ki taraf dauda.

Tab Bhima rath se kood pade.

Woh sher ki tarah Susharma par toot pade.

Unhone uske baal pakadkar use zor se zameen par patak diya.

Susharma dard se cheekhne laga.

Bhima ne uske seene par ghutna rakhkar use zor-zor se maara.

Susharma behosh ho gaya.

Apne raja ko gira hua dekhkar Trigart sena darrkar bhaag gayi.

Pandavo ne gaayen aur dhan wapas le liya.

Raja Virata ki chinta door ho gayi.

Bhima ne behosh Susharma ko baandhkar Yudhishthira ke saamne laakar khada kar diya.

Bhima bole,

“Yeh dusht jeene layak nahi hai.”

“Main ise abhi maar deta hoon.”

Lekin Yudhishthira muskuraakar bole,

“Isse chhod do.”

“Yeh ab Virata ka haar chuka daas hai.”

Fir Bhima ne Susharma se kaha,

“Agar jeena chahta hai, toh har sabha mein kehna padega — ‘Main haar chuka hoon aur daas ban gaya hoon.’”

Yudhishthira ne daya se kaha,

“Ab ise mukt kar do.”

Fir unhone Susharma se kaha,

“Tum azaad ho.”

“Lekin dobara kabhi aisa anyaay mat karna.”

Rishi Vaisampayana bole, “Is tarah Pandavo ne Raja Virata ko bachaya aur Trigart sena ko hara diya, lekin fir bhi kisi ko unki asli pehchaan ka pata nahi chala.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.9
        with st.expander("Section 4.4.9  Section XXXIV"):
            text1 = """ 
            Rishi Vaisampayana bole, “Yudhishthira ki baat sunkar Susharma sharm se jhuk gaya.”

Woh chupchaap Raja Virata ke paas gaya, unhe pranam kiya aur wahan se chala gaya.

Udhar Pandavo ne apni shakti se shatruon ko hara diya tha aur Raja Virata ko bacha liya tha.

Us raat sab yoddha yuddh bhoomi mein hi aaraam se ruke.

Raja Virata Pandavo ke parakram se bahut prasann hue.

Woh bole,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Aaj meri jeet tum sabki wajah se hui hai.”

“Mera dhan, ratna aur sampatti ab tumhari bhi hai.”

“Tum yahan khushi se raho.”

“Main tumhe sundar vastra, gehne, dhan aur jo chaho dene ko taiyaar hoon.”

“Tumhare bal aur sahayata se hi main apne shatruon se bach paaya hoon.”

“Tum sab Matsya desh ke swaami banne layak ho.”

Rishi Vaisampayana bole, “Yeh sunkar Yudhishthira aur unke bhai vinamrata se haath jodkar bole,”

“Hey Maharaj, aapke prem aur samman se hum bahut prasann hain.”

“Lekin humein sabse zyada khushi iss baat ki hai ki aap surakshit hain aur shatruon se mukt ho gaye hain.”

Virata fir Yudhishthira se bole,

“Hey mahaan Brahman, aap jo chaahein le sakte hain.”

“Main aapko gaayen, sona, moti aur anek ratna dena chahta hoon.”

“Aapki wajah se hi main aaj fir se apne putron aur rajya ko dekh pa raha hoon.”

“Aap sabne mujhe bade sankat se bachaya hai.”

Tab Yudhishthira shaant swar mein bole,

“Hey Maharaj, aap sada sab logon ke saath daya aur nyaay ka vyavahaar kariye.”

“Ab aapke doot turant nagar jaakar aapki vijay ki khabar sunaayein.”

“Sab logon ko pata chalna chahiye ki aap yuddh jeet gaye hain.”

Raja Virata ko yeh baat achhi lagi.

Unhone turant dooton ko aadesh diya,

“Nagar jaakar meri vijay ki ghoshna karo.”

“Aur nagar ki sundar streeon aur gaayikaon ko sangeet ke saath mera swaagat karne bhejo.”

Rishi Vaisampayana bole, “Raja ka aadesh sunkar doot khushi-khushi nagar ki taraf chale gaye.”

Subah hote hi poori Virata nagari mein Raja Virata ki vijay ki khabar phail gayi.

Log khushi se bhar gaye aur nagar mein utsav jaisa mahaul ho gaya."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.10
        with st.expander("Section 4.4.10  Section XXXV"):
            text1 = """ 
            Rishi Vaisampayana bole, “Jab Raja Virata Trigarton se yuddh karne gaye hue the, tab Duryodhana ne mauka dekhkar Matsya desh par hamla kar diya.”

Bhishma, Dronacharya, Karna, Kripacharya, Ashwatthama, Shakuni, Dushasan aur kai bade Kaurav yoddha uske saath the.

Woh sab milkar Matsya desh ki gaayen churaane lage.

Kaurav sena ne chaaron taraf se gherkar saath hazaar gaayen apne kabze mein kar li.

Gaay charane waale log darr aur dukh se chillane lage."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Unmein se ek mukhya gopal jaldi se rath par baithkar Virata nagari pahunch gaya.

Woh seedha Rajkumar Uttar ke paas gaya, jo mahal ke andar streeon ke beech baitha tha.

Gopal ghabraaye hue swar mein bola,

“Hey Rajkumar! Kaurav hamari saath hazaar gaayen le ja rahe hain!”

“Kripya turant unhe bachaiye.”

“Aapke pita Maharaj Virata toh Trigarton se yuddh karne gaye hue hain.”

“Is samay poore rajya ki aasha sirf aap par hai.”

Gopal ne Rajkumar Uttar ka hausla badhaate hue kaha,

“Maharaj hamesha sabha mein aapki bahaduri ki tareef karte hain.”

“Woh kehte hain ki unka putra ek mahaan dhanurdhar aur veer yoddha hai.”

“Aaj woh baat sach saabit karne ka samay aa gaya hai.”

“Apne teeron se Kaurav sena ko hara dijiye.”

“Apne rath par sone ka sher waala dhwaj lagaiye aur veerta dikhaaiye.”

“Aap iss rajya ke rakshak hain, bilkul waise hi jaise Arjuna Pandavo ke rakshak hain.”

“Hum sab praja ki aasha aap par tiki hui hai.”

Rishi Vaisampayana bole, “Yeh baatein sunkar Rajkumar Uttar ke mann mein ghamand aur utsaah bhar gaya.”

Woh mahal ki streeon ke saamne apni bahaduri dikhane laga aur bade garv se baatein karne laga."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.11
        with st.expander("Section 4.4.11  Section XXXVI"):
            text1 = """ 
            Rishi Vaisampayana bole, “Rajkumar Uttar garv se bole,”

“Main dhanush chalane mein nipun hoon.”

“Agar mujhe ek achha saarathi mil jaaye, toh main abhi turant Kauravo ke peeche nikal padun.”

“Mera purana saarathi ek bade yuddh mein maara gaya tha.”

“Isi liye mere paas ab koi kushal rath chalane waala nahi hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Jaise hi mujhe ek saarathi milega, main apna dhwaj lekar yuddh ke liye nikal jaaunga.”

Uttar aur bhi ghamand se bole,

“Main akela hi Kauravo ki sena mein ghus jaaunga.”

“Bhishma, Drona, Karna aur Duryodhana sabko dara dunga.”

“Main gaayen wapas lekar aaunga aur sab log meri veerta dekhenge.”

“Woh ek doosre se kahenge — kya yeh khud Arjuna hai?”

Rishi Vaisampayana bole, “Yeh baatein sunkar Arjuna, jo Brihannala ke roop mein wahan maujood the, dheere se Draupadi se bole,”

“Hey Krishnaa, tum Rajkumar Uttar se keh do ki Brihannala pehle Arjuna ka saarathi reh chuka hai.”

“Woh bahut kushal hai aur bade-bade yuddhon ka anubhav rakhta hai.”

Draupadi Rajkumar Uttar ke paas gayi aur boli,

“Hey Rajkumar, Brihannala saamanya vyakti nahi hai.”

“Woh pehle Arjuna ka saarathi reh chuka hai.”

“Jab Agnidev ne Khandav van jalaya tha, tab bhi wahi Arjuna ka rath chala raha tha.”

“Uske jaisa saarathi dhoondhna mushkil hai.”

Rajkumar Uttar thoda jhijhak kar bole,

“Hey Sairindhri, tum use achhi tarah jaanti ho.”

“Lekin main khud us Brihannala se kaise kahun?”

Draupadi boli,

“Tumhari chhoti behen Uttara agar kahegi, toh Brihannala zaroor maan jaayega.”

“Fir tum bina chinta ke yuddh mein jaa sakoge.”

Yeh sunkar Rajkumar Uttar ne apni behen se kaha,

“Hey Uttara, tum jaakar Brihannala ko yahaan bula lao.”

Rishi Vaisampayana bole, “Bhai ka aadesh paakar Rajkumari Uttara turant nritya shala ki taraf chal padi, jahaan veer Arjuna Brihannala ke roop mein reh rahe the.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.12
        with st.expander("Section 4.4.12  Section XXXVII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Rajkumar Uttar ka sandesh paakar Rajkumari Uttara turant nritya shala ki taraf gayi.”

Woh bahut sundar lag rahi thi.

Unhone sone ka haar pehna hua tha, kamar mein motiyon ki mekhla thi, aur unka roop Devi Lakshmi ki tarah chamak raha tha.

Woh jaldi-jaldi Brihannala ke paas pahunchi, bilkul bijli ki chamak ki tarah.

Rajkumari ne Arjuna ko pranam kiya."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Arjuna ne pyaar aur muskaan ke saath poocha,

“Hey sundari, tum itni jaldi mein yahaan kyun aayi ho?”

“Tumhara chehra udaas kyun lag raha hai?”

“Mujhe bina deri sab batao.”

Rajkumari Uttara vinamrata se boli,

“Hey Brihannala, Kaurav hamare rajya ki gaayen le ja rahe hain.”

“Mere bhai Rajkumar Uttar unse yuddh karne ja rahe hain.”

“Lekin unka saarathi mar chuka hai aur ab unke paas koi kushal rath chalane waala nahi hai.”

“Sairindhri ne humein aapke baare mein bataya.”

“Usne kaha ki aap pehle Arjuna ke priya saarathi the.”

“Arjuna ne aapke saath milkar poori dharti ko jeeta tha.”

“Isliye kripya mere bhai ke saarathi ban jaiye.”

Rajkumari ne dukhi swar mein kaha,

“Agar aap meri baat nahi maanenge, toh main jeena chhod dungi.”

Rishi Vaisampayana bole, “Rajkumari ki baat sunkar Arjuna unke saath Rajkumar Uttar ke paas chale gaye.”

Rajkumari bhi unke peeche-peeche chalti rahi, bilkul maa haathi ke peeche chalne wale bachche ki tarah.

Rajkumar Uttar ne Brihannala ko dekhkar kaha,

“Sairindhri ne mujhe aapki mahanta bataayi hai.”

“Aap hi Arjuna ke saarathi the.”

“Kripya mera rath sambhaliye aur mujhe Kauravo se yuddh karne le chaliye.”

Arjuna mazaak bhare andaaz mein bole,

“Main toh sirf gaan aur nritya jaanta hoon.”

“Mujhe yuddh bhoomi mein rath chalane ka kya gyaan?”

Rajkumar Uttar bole,

“Chahe aap gaayak ho ya nritya guru, iss samay aapko mera saarathi banna hi hoga.”

Rishi Vaisampayana bole, “Arjuna sab kuch jaante hue bhi manoranjan ke liye anjaan ban rahe the.”

Jab unhone kavach pehenne ki koshish ki, toh jaan-boojhkar ulta pehenne lage.

Yeh dekhkar mahal ki sab rajkumariyaan zor-zor se hansne lagi.

Fir Rajkumar Uttar ne khud Arjuna ko kavach pehnaya.

Uske baad Uttar ne apna chamakta hua kavach pehna aur sher waala dhwaj apne rath par lagwaya.

Arjuna Brihannala ke roop mein saarathi bane aur Rajkumar Uttar ko lekar yuddh ke liye nikal pade.

Mahal ki rajkumariyaan haste hue Brihannala se boli,

“Jab aap Kauravo ko haraakar lautenge, toh hamari gudiyon ke liye sundar kapde lekar aana!”

Arjuna muskuraakar gehri awaaz mein bole,

“Agar Rajkumar Uttar Kauravo ko hara denge, toh main tum sabke liye bahut sundar vastra zaroor laaunga.”

Rishi Vaisampayana bole, “Iske baad Arjuna ne ghodon ko tez gati se Kaurav sena ki taraf badhaya.”

Nikalte samay buzurg streeon, Brahmanon aur rajkumariyon ne rath ke chaaron taraf ghoomkar Rajkumar Uttar ko aashirvaad diya.”

Woh boli,

“Jaise Arjuna ne Khandav van mein vijay paayi thi, waise hi tum bhi aaj Kauravo par vijay paao.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.13
        with st.expander("Section 4.4.13  Section XXXVIII"):
            text1 = """ 
            Rishi Vaisampayana bole, “Rajkumar Uttar ne Brihannala se kaha,”

“Mujhe seedha wahaan le chalo jahaan Kaurav sena khadi hai.”

“Main unhe haraakar hamari gaayen wapas le aaunga.”

Yeh sunkar Arjuna ne tez gati waale ghodon ko aage badhaya.

Sone ke haaron se sajae hue woh ghode hawa ki tarah daudne lage.

Kuch hi der mein dono ne Kaurav sena ko dekh liya."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Woh sena samundar ki tarah vishaal lag rahi thi.

Har taraf haathi, ghode, rath aur dhwaj hi dhwaj dikh rahe the.

Dhool ka bada baadal aasman tak chha gaya tha.

Rajkumar Uttar ne jab Bhishma, Drona, Karna, Kripa, Ashwatthama aur Duryodhana ko dekha, toh woh darr se kaamp uthe.

Unke shareer ke rom khade ho gaye.

Woh ghabraakar bole,

“Hey Brihannala, main in Kauravo se yuddh nahi kar sakta!”

“Yeh sena bahut bhayanak hai.”

“Bhishma, Drona aur Karna jaise mahaan yoddha yahaan maujood hain.”

“Main abhi bachcha hoon.”

“Mere paas itni shakti aur anubhav nahi hai.”

“Kripya rath ko wapas mod lo!”

Rishi Vaisampayana bole, “Darr ke maare Uttar ka hausla toot gaya.”

Woh rote hue bole,

“Mere pita poori sena lekar Trigarton se ladne gaye hain.”

“Main yahaan akela hoon.”

“Main iss vishaal sena ka saamna nahi kar sakta.”

Tab Brihannala bane Arjuna muskuraakar bole,

“Hey Rajkumar, abhi tak tumne yuddh kiya bhi nahi aur tum itna darr rahe ho?”

“Tumne hi sabke saamne apni veerta ki badi-badi baatein ki thi.”

“Ab peeche hatoge toh log tum par hansenge.”

“Veer Kshatriya yuddh bhoomi se bhaagte nahi.”

“Main toh bina gaayen wapas laaye lautunga hi nahi.”

Lekin Uttar ka darr aur badh gaya.

Woh bole,

“Chahe log mera mazaak udaayein, chahe gaayen chali jaayein, mujhe yuddh nahi karna!”

Itna kehkar Rajkumar Uttar rath se kood pade aur dhanush chhodkar bhaagne lage.

Tab Arjuna zor se bole,

“Yeh veeron ka kaam nahi hai!”

“Yuddh bhoomi mein darrkar bhaagna Kshatriya ko shobha nahi deta.”

“Yuddh mein mar jaana bhi bhaagne se behtar hai!”

Yeh kehkar Arjuna khud rath se utar pade aur Uttar ke peeche bhaage.

Unki lambi choti aur laal vastra hawa mein lehra rahe the.

Door se yeh drishya dekhkar Kaurav sena ke kai yoddha hansne lage.

Kuch log ek doosre se bole,

“Yeh vyakti kaun hai?”

“Yeh aadha purush aur aadha stree jaisa lagta hai.”

“Lekin iska chalna aur shareer Arjuna jaisa lag raha hai.”

“Kya yeh sach mein Dhananjaya Arjuna ho sakta hai?”

“Koi aur akela hamare saamne aane ki himmat nahi kar sakta.”

Fir bhi Kaurav kisi nishchay par nahi pahunch paaye.

Udhar Arjuna ne bhaagte hue Uttar ko pakad liya.

Rajkumar darr ke maare lagbhag behosh ho rahe the.

Woh rote hue bole,

“Hey Brihannala, mujhe chhod do!”

“Main tumhe sau sone ke sikke dunga.”

“Ratna, haathi aur sundar rath bhi dunga.”

“Bas mujhe yahaan se le chalo!”

Arjuna hans pade.

Woh Uttar ko kheenchkar wapas rath ke paas laaye aur bole,

“Hey Rajkumar, agar tum yuddh nahi kar sakte, toh koi baat nahi.”

“Tum sirf mere saarathi ban jao.”

“Main akela hi Kauravo se yuddh karunga aur gaayen wapas laaunga.”

“Tum bas ghodon ki lagaam sambhalo.”

“Darrna mat, tum ek Kshatriya ho.”

“Main tumhari raksha karunga.”

Rishi Vaisampayana bole, “Arjuna ne dheere-dheere Uttar ka hausla badhaya aur use rath par wapas bitha diya.”

“Fir veer Arjuna Kaurav sena ki taraf badhne lage.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.14
        with st.expander("Section 4.4.14  Section XXXIX"):
            text1 = """ 
            Rishi Vaisampayana bole, “Jab Kaurav yoddhaon ne Brihannala ke roop mein Arjuna ko Rajkumar Uttar ke saath Shami vriksh ki taraf jaate dekha, toh unke mann mein shanka utpann hui.”

Bhishma, Dronacharya aur anya maharathi sochne lage,

“Kya yeh sach mein Arjuna ho sakta hai?”

Us samay achanak bahut saare apashakun dikhne lage.

Tez aur garam hawa chalne lagi."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Dhool aur kankad aasman mein uddne lage.

Aasmaan raakh ke rang ka ho gaya.

Bina paani ke baadal ajeeb dikhne lage.

Yoddhaon ke hathiyaar apne aap myaan se bahar nikalne lage.

Ghode aansu bahaane lage.

Dhwaj bina hawa ke kaampne lage.

Siyar bhayanak awaaz mein cheekhne lage.

Yeh sab dekhkar Dronacharya gambhir ho gaye.

Woh bole,

“Yeh sab bahut bade sankat ke sanket hain.”

“Sab log saavdhan ho jaao.”

“Sena ko yuddh ke liye taiyaar rakho aur gaayon ki raksha karo.”

“Jo vyakti stree ke roop mein aa raha hai, woh koi aam vyakti nahi.”

“Mujhe poora vishwas hai ki yeh Arjuna hi hai.”

Fir Drona ne Bhishma se kaha,

“Yeh wahi Kiriti Arjuna hai, jiske rath par vaanar dhwaj lehraata hai.”

“Yeh Indra putra hai aur devtaon tak se ladne ki shakti rakhta hai.”

“Mahadev swayam isse prasann ho chuke hain.”

“Yeh aaj nishchit roop se hum sabko haraakar gaayen wapas le jaayega.”

Dronacharya ki baat sunkar Karna ko krodh aa gaya.

Woh ghamand se bola,

“Aap hamesha Arjuna ki hi tareef karte rehte hain.”

“Arjuna meri ya Duryodhana ki shakti ke saamne solahve bhaag ke barabar bhi nahi hai!”

Tab Duryodhana khush hokar bola,

“Agar yeh sach mein Arjuna hai, toh mera kaam aasaan ho gaya.”

“Pandavo ka agyaatvaas poora hone se pehle hi woh pakde jaayenge.”

“Fir unhe dobara baarah saal vanvaas jaana padega.”

“Lekin agar yeh koi aur vyakti hai, toh main ise apne teeron se turant gira dunga.”

Rishi Vaisampayana bole, “Duryodhana ki baat sunkar Bhishma, Drona, Kripa aur Ashwatthama ne uski veerta ki prashansa toh ki, lekin unke mann mein Arjuna ka darr ab bhi bana hua tha.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.15
        with st.expander("Section 4.4.15  Section XL"):
            text1 = """ 
            Rishi Vaisampayana bole, “Arjuna Rajkumar Uttar ko lekar Shami vriksh ke paas pahunche.”

Unhone samajh liya tha ki Uttar abhi yuddh mein anubhavheen aur komal hriday waale hain.

Tab Arjuna ne shaant swar mein kaha,

“Hey Uttar, iss vriksh par kuch mahaan dhanush aur divya astr-shastra chhipe hue hain.”

“Tumhare dhanush mere bal aur teeron ka bhaar nahi sambhaal sakte.”

“Isliye tum iss vriksh par chadhkar unhe neeche utaaro.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Arjuna ne aage kaha,

“Isi vriksh par Pandavo ke dhanush, baan, dhwaj aur kavach bandhe hue hain.”

“Yudhishthira, Bhima, Nakula, Sahadeva aur Arjuna ke divya hathiyaar yahaan surakshit rakhe gaye hain.”

Fir Arjuna ne Gandiva ka varnan kiya.

Woh bole,

“Yahaan Arjuna ka mahaan Gandiva dhanush bhi rakha hai.”

“Woh hazaaron dhanushon ke barabar shakti rakhta hai.”

“Uske bal se rajya jeete ja sakte hain.”

“Woh taad vriksh jitna bada, bahut mazboot aur sone se saja hua hai.”

“Us par koi gaanth nahi hai aur woh bahut sundar bana hua hai.”

“Uska bhaar aur tanav saamanya yoddha sambhaal bhi nahi sakte.”

“Pandavo ke anya dhanush bhi utne hi shaktishaali aur kathor hain.”

Rishi Vaisampayana bole, “Arjuna ki baatein sunkar Rajkumar Uttar aashcharya se us Shami vriksh ko dekhne lage, jahaan Pandavo ke divya astr-shastra chhupe hue the.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.16
        with st.expander("Section 4.4.16  Section XLI"):
            text1 = """ 
            Rajkumar Uttar ne Shami vriksh ko dekhkar ghabraate hue kaha,

“Hey Brihannala, maine suna hai ki iss vriksh par ek laash latkaayi gayi hai.”

“Main ek Kshatriya rajkumar hoon.”

“Main kisi shav ko haath kaise laga sakta hoon?”

“Yeh mere liye uchit nahi hai.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Tum mujhe apavitra kaam kyun karwa rahe ho?”

Tab Brihannala bane Arjuna muskuraakar bole,

“Hey Rajkumar, darrne ki koi baat nahi hai.”

“Yahaan koi shav nahi latka.”

“Sirf divya dhanush aur astr-shastra yahaan surakshit rakhe gaye hain.”

“Main tumse kabhi koi apmaan janak kaam nahi karwaunga.”

Rishi Vaisampayana bole, “Arjuna ki baat sunkar Rajkumar Uttar dheere-dheere vriksh par chadh gaye.”

Arjuna neeche rath par khade rahe aur bole,

“Jaldi un astron ki rassi aur kapde kholkar neeche utaaro.”

Rajkumar Uttar ne vriksh par bandhe hue kapde aur rassiyan khol diं.

Tab unhone wahan paanch mahaan dhanush dekhe.

Unmein Arjuna ka divya Gandiva bhi tha.

Jaise hi ve dhanush prakat hue, unka tej surya ki tarah chamakne laga.

Woh aise lag rahe the jaise aasman mein naye grah uday ho rahe hon.

Un dhanushon ka roop bhayanak saanpon ki tarah prateet ho raha tha.

Unka divya prakash dekhkar Uttar ke shareer ke rom khade ho gaye.

Woh aashcharya aur bhay se bhar gaye.

Divya astron ko sparsh karte hue Rajkumar Uttar neeche khade Arjuna ki taraf dekhkar bolne lage."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.17
        with st.expander("Section 4.4.17  Section XLII"):
            text1 = """ 
            Rajkumar Uttar ne divya astr-shastron ko dekhkar bade aashcharya se Arjuna se poocha,

“Hey Brihannala, yeh adbhut dhanush kis mahaan yoddha ka hai?”

“Is dhanush par sau sone ke kundal jaise alankaar lage hue hain aur iska tej surya ki tarah chamak raha hai.”

“Yeh doosra dhanush kiska hai, jis par sone ke haathi bane hue hain?”

“Yeh teesra dhanush kiska hai, jis par sone ke Indragop ke chinh sajae gaye hain?”

“Yeh chautha dhanush kiska hai, jo teen chamakte hue suryon se alankrit hai?”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh sundar dhanush kiska hai, jo sona aur ratnon se saja hua hai aur jis par chamakte hue keede jaise alankaar bane hain?”

Rajkumar Uttar fir teeron ko dekhkar bole,

“Yeh hazaaron teer kis yoddha ke hain?”

“Inke sir sone ke bane hue hain aur yeh sone ke tarkash mein rakhe gaye hain.”

“Yeh mote aur bhayanak teer kis ke hain, jin par giddh ke pankh lage hue hain aur jo poore lohe ke bane hue hain?”

“Yeh kaale rang ka tarkash kis ka hai, jis par paanch baaghon ki chhavi bani hai?”

“Ismein rakhe hue teer bahut bhayanak lag rahe hain.”

“Yeh saat sau bade-bade teer kis ke hain, jo khoon peene ke liye taiyaar lagte hain aur chand ki kala ki tarah chamak rahe hain?”

“Yeh sone se sajaye hue teer kis ke hain, jinmein tota ke pankhon jaise hare pankh lage hue hain?”

Fir Uttar ne talwaaron ko dekhkar poocha,

“Yeh bhayanak talwaar kis mahaan yoddha ki hai, jis par mendhak ka chinh bana hua hai?”

“Yeh baagh ki khaal waali myaan mein rakhi hui sone se saji talwaar kiski hai?”

“Yeh sundar chamakti hui talwaar kiski hai, jiska hilt sone ka bana hua hai?”

“Yeh neele aasman ki tarah kaali aur lambi talwaar kiski hai?”

“Yeh bhaari aur chaudi talwaar kis mahaan yoddha ki hai, jo aag ki tarah chamak rahi hai?”

“Yeh kaali dhaar waali aur sone ke binduon se saji bhayanak talwaar kiski hai, jo zehreeli saanp ki tarah darr paida karti hai?”

Rajkumar Uttar bade aashcharya se bole,

“Hey Brihannala, kripya mujhe sach-sach bataaiye.”

“In sab divya astr-shastron ko dekhkar mera mann chakit ho gaya hai.”

"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.18
        with st.expander("Section 4.4.18  Section XLIII"):
            text1 = """ 
            Brihannala bane Arjuna muskuraakar bole,

“Hey Rajkumar Uttar, jis dhanush ke baare mein tumne sabse pehle poocha tha, woh duniya bhar mein prasiddh Arjuna ka Gandiva hai.”

“Yeh shatru senaon ka vinaash karne waala divya dhanush hai.”

“Is par sona saja hua hai aur yeh sabhi dhanushon mein sabse mahaan hai.”

“Yeh akela hi hazaaron dhanushon ke barabar shakti rakhta hai.”

“Isi Gandiva ke bal par Arjuna ne manushyon aur devtaon tak ko yuddh mein haraaya hai.”

Arjuna ne aage kaha,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Is divya dhanush ko pehle Bhagwan Shiva ne hazaar varsh tak dhaaran kiya tha.”

“Uske baad Prajapati ne ise rakha.”

“Fir Indra, Chandradev aur Varun Dev ne ise dhaaran kiya.”

“Ant mein Varun Dev ne yeh dhanush Arjuna ko diya.”

“Isliye yeh sab dhanushon mein sarvashreshth maana jaata hai.”

Fir Arjuna ne doosre dhanush ki taraf sanket karte hue kaha,

“Yeh sundar aur mazboot dhanush Bhimasena ka hai.”

“Issi dhanush se Bhima ne poorvi deshon ko jeeta tha.”

“Yeh teesra dhanush Dharmaraj Yudhishthira ka hai.”

“Is par sone ke Indragop ke chinh bane hue hain.”

“Yeh chamakte hue suryon waala dhanush Nakula ka hai.”

“Aur yeh sona aur ratnon se saja dhanush Sahadeva ka hai.”

Fir Arjuna ne teeron ke baare mein bataya.

Woh bole,

“Yeh hazaar teekhe aur zehreeli saanp jaise bhayanak teer Arjuna ke hain.”

“Yuddh mein chalne par yeh kabhi samaapt nahi hote.”

“Yeh bade aur chand ki kala jaise teer Bhima ke hain.”

“Yeh baaghon ke chinh waala tarkash Nakula ka hai.”

“Issi ke bal par usne pashchimi deshon ko jeeta tha.”

“Yeh rang-birange aur surya ki tarah chamakne waale teer Sahadeva ke hain.”

“Aur yeh mote, mazboot aur sone ke sir waale baan Yudhishthira ke hain.”

Fir Arjuna ne talwaaron ka varnan kiya.

Woh bole,

“Yeh mendhak ke chinh waali bhayanak talwaar Arjuna ki hai.”

“Yeh baagh ki khaal waali myaan mein rakhi lambi talwaar Bhimasena ki hai.”

“Yeh sundar aur sone ki mooth waali talwaar Dharmaraj Yudhishthira ki hai.”

“Bakri ki khaal waali myaan mein rakhi yeh tez dhaar talwaar Nakula ki hai.”

“Aur yeh badi aur shaktishaali talwaar, jo gaay ki khaal waali myaan mein rakhi hai, Sahadeva ki hai.”

Rishi Vaisampayana bole, “Arjuna ke mukh se Pandavo ke divya astr-shastron ka varnan sunkar Rajkumar Uttar aur bhi adhik chakit ho gaye.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.19
        with st.expander("Section 4.4.19  Section XLIV"):
            text1 = """ 
            Rajkumar Uttar ne divya astr-shastron ko dekhkar aashcharya se kaha,

“Yeh sab Arjuna ke astr bahut adbhut lag rahe hain.”

“Lekin Pandav ab kahaan hain?”

“Yudhishthira, Bhima, Nakula, Sahadeva aur swayam Arjuna kahaan chhupe hue hain?”

“Draupadi bhi kahaan hai, jo vanvaas mein unke saath gayi thi?”

Tab Brihannala bane Arjuna shaant swar mein bole,"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Hey Rajkumar, main hi Arjuna hoon.”

“Tumhare pita ki sabha mein jo Kanka naam se rehte hain, wahi Yudhishthira hain.”

“Tumhare rajya ke rasoiya Vallava hi Bhimasena hain.”

“Ghodo ki dekhbhaal karne waale Granthika hi Nakula hain.”

“Gaayon ki raksha karne waale Tantripal hi Sahadeva hain.”

“Aur Sairindhri hi Draupadi hain, jiske liye Keechak aur uske bhai maare gaye.”

Yeh sunkar Rajkumar Uttar hairaan reh gaye.

Woh bole,

“Agar aap sach mein Arjuna hain, toh mujhe apne das naam bataaiye.”

“Maine pehle unke baare mein suna hai.”

“Tabhi mujhe vishwas hoga.”

Arjuna muskuraaye aur bole,

“Mere das naam hain — Arjuna, Phalguna, Jishnu, Kiriti, Shvetavahana, Vibhatsu, Vijaya, Krishna, Savyasachi aur Dhananjaya.”

Rajkumar Uttar ne poocha,

“Hey veer, aapko yeh sab naam kyun diye gaye?”

Tab Arjuna ne ek-ek naam ka arth bataya.

Woh bole,

“Mujhe Dhananjaya isliye kehte hain kyunki maine anek deshon ko jeetkar dhan prapt kiya.”

“Mujhe Vijaya kehte hain kyunki main yuddh bhoomi se kabhi bina vijay paaye wapas nahi lauta.”

“Mera naam Shvetavahana hai kyunki mere rath mein sada safed ghode jude rehte hain.”

“Mujhe Phalguna kaha jaata hai kyunki mera janm Uttara Phalguni nakshatra mein hua tha.”

“Mujhe Kiriti isliye kehte hain kyunki Indra ne mujhe ek chamakta hua mukut diya tha.”

“Mera naam Vibhatsu hai kyunki main kabhi yuddh mein neech ya adharm ka kaam nahi karta.”

“Mujhe Savyasachi kehte hain kyunki main dono haathon se Gandiva chala sakta hoon.”

“Mujhe Arjuna kaha jaata hai kyunki mera roop aur mere karm dono pavitra aur nirmal hain.”

“Mera naam Jishnu hai kyunki main shatruon ko haraane waala aur ajey yoddha hoon.”

“Aur Krishna naam mere pita ne prem se rakha tha, kyunki mera rang saanvla tha.”

Rishi Vaisampayana bole, “Arjuna ki baatein sunkar Rajkumar Uttar ka darr poori tarah door ho gaya.”

Woh turant Arjuna ke paas aaye aur unhe pranam kiya.

Woh vinamrata se bole,

“Hey Partha, mujhe kshama kariye.”

“Maine aapko pehchaana nahi aur agyaan mein bahut kuch keh diya.”

“Aapko dekhkar mera bhay ab samaapt ho gaya hai.”

“Aaj mera bhaagya jag gaya ki mujhe aapke darshan hue.”

“Ab mujhe poora vishwas hai ki Kaurav sena ko koi nahi bacha sakta.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.20
        with st.expander("Section 4.4.20  Section XLV"):
            text1 = """ 
            Rishi Vaisampayana bole, “Rajkumar Uttar ne Arjuna se poocha,”

“Hey veer, main aapka saarathi bankar iss vishaal Kaurav sena ke kis bhaag ki taraf rath le jaaun?”

Arjuna muskuraakar bole,

“Hey Rajkumar, tum bilkul bhi mat daro.”

“Main aaj tumhare sab shatruon ko yuddh mein hara dunga.”

“Tum sirf dhairya rakho aur mere liye rath sambhalo.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Jaldi se mere tarkash rath par baandh do aur ek sundar talwaar bhi le lo.”

Rishi Vaisampayana bole, “Arjuna ki baat sunkar Uttar ka darr dheere-dheere door ho gaya.”

Woh turant vriksh se neeche utar aaye aur Arjuna ke divya astr-shastra rath par rakh diye.

Tab Arjuna bole,

“Hey Uttar, jab tak main iss rath par hoon, tab tak yeh rath ek durg ke samaan surakshit hai.”

“Mere baan uski deewarein hain.”

“Mera dhwaj uska shikhar hai.”

“Meri dhanush ki jya us durg ke yantron ki tarah shatruon par vaar karegi.”

“Mere krodh se yeh rath ajey ho jaayega.”

“Isliye tumhara bhay ab samaapt ho jaana chahiye.”

Rajkumar Uttar vinamrata se bole,

“Hey Partha, ab mujhe koi darr nahi hai.”

“Aapka yuddh mein dhairya Indra aur Shri Krishna ke samaan hai.”

“Lekin ek baat mujhe sada hairaan karti rahi.”

“Aap jaise sundar aur divya purush ne napunsak ka roop kaise dhaaran kiya?”

Tab Arjuna bole,

“Hey Rajkumar, yeh sab maine apne bade bhai Yudhishthira ki aagya se kiya tha.”

“Main vaastav mein napunsak nahi hoon.”

“Agyaatvaas poora karne aur dharm paalan ke liye maine Brihannala ka roop dhaaran kiya tha.”

“Ab mera woh vrat samaapt ho chuka hai.”

Yeh sunkar Uttar bahut prasann hue.

Woh bole,

“Aaj mera bhaagya jaag gaya.”

“Ab mujhe poora vishwas hai ki hum devtaon se bhi lad sakte hain.”

“Aap mujhe aadesh dijiye.”

“Main aapka saarathi banunga.”

“Main Daruk aur Matali ki tarah kushalta se rath chala sakta hoon.”

Fir Uttar ne Arjuna ke ghodon ki tareef ki.

Woh bole,

“Yeh safed ghode bahut tez aur shaktishaali hain.”

“Yeh Shri Krishna aur Indra ke divya ghodon ke samaan hain.”

“Yeh rath aap jaise mahaan dhanurdhar ke yogya hai.”

Rishi Vaisampayana bole, “Uske baad Arjuna ne apne haathon se chudiyan utaar diं aur sone se kadhai ki hui divya dastane pehen liye.”

Unhone apne ghunghraale kaale baalon ko safed kapde se baandh liya.

Fir purv disha ki taraf mukh karke ve rath par baith gaye.

Unhone man hi man apne sabhi astr-shastron ka smaran kiya.

Turant saare divya astr prakat ho gaye aur bole,

“Hey Indraputra, hum aapki seva mein haazir hain.”

Arjuna ne unhe pranam kiya aur kaha,

“Tum sab mere smaran mein sadaa virajmaan raho.”

Fir Arjuna ne Gandiva dhanush uthaya aur uski jya chadhaakar zor se tan di.

Us dhanush ki awaaz do bade saandon ki takkar ki tarah goonj uthi.

Dharti kaamp uthi.

Tez aandhi chalne lagi.

Aasmaan mein ulkaayein girne lagiं.

Pakshi ghabraakar uddne lage aur bade-bade vriksh hilne lage.

Kaurav sena ne us bhayanak dhwani ko sunkar turant pehchaan liya.

Sab samajh gaye ki Arjuna ne Gandiva utha liya hai.

Rajkumar Uttar fir bhi thoda ghabraakar bole,

“Hey Partha, aap akela hain aur saamne itne saare maharathi hain.”

“Aap in sabko kaise haraayenge?”

Arjuna zor se hans pade aur bole,

“Hey Rajkumar, jab maine Gandharvon se yuddh kiya tha, tab mere saath kaun tha?”

“Khandav van mein devtaon aur daanavon se ladte samay mera sahayak kaun tha?”

“Nivatakavach aur Paulom daanavon se yuddh mein kaun mere saath tha?”

“Draupadi swayamvar mein anek rajaon ka saamna karte waqt mera saathi kaun tha?”

“Maine Dronacharya, Indra, Varun, Agni, Shri Krishna aur swayam Mahadev se astr-vidya seekhi hai.”

“Isliye in Kauravo se ladna mere liye kathin nahi hai.”

“Tum bas rath ko tez gati se aage badhao aur apna bhay chhod do.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 4.4.21
        with st.expander("Section 4.4.21  Section XLVI"):
            text1 = """ 
            Arjun ka Divya Pravesh aur Uttara ka Dar

Vaisampayana ne kaha, “Arjun ne Uttara ko apna saarathi banaya aur Sami ke ped ke paas jaakar apne divya hathiyaar nikaale.”

Usne purana jhanda hata diya aur apne rath par ek chamakta hua divya dhwaj lagaya. Us dhwaj par ek balwaan vanar ka chinh tha. Yeh Vishwakarma ki banayi hui adbhut rachna thi.

Jab Arjun ne apna Gandiva dhanush uthaya aur shankh bajaya, toh uski awaaz bahut bhayankar thi. Aisa laga jaise pahaad hil gaye hon aur aasman goonj utha ho."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Ghode darr kar ghutnon par baith gaye. Rajkumar Uttara bhi bahut ghabra gaya aur rath mein hi baith gaya.

Arjun ne use sambhalte hue kaha, “Dar mat, Uttara. Tum ek Kshatriya ho. Yudh ke beech himmat nahi haarni chahiye.”

Lekin Uttara ne kaha, “Maine pehle bhi kai shankh aur yudh ki awaazein suni hain, lekin aisi kabhi nahi. Aapka dhanush, yeh dhwaj aur yeh shankh sab alaukik lag rahe hain. Mera mann ghabra raha hai.”

Tab Arjun ne phir se apna shankh bajaya. Is baar awaaz aur bhi zyada shaktishaali thi. Dharti tak kaamp uthi.

Udhar Kaurav sena mein Dronacharya ne yeh sab dekhkar kaha, “Yeh yoddha koi aur nahi, Arjun hi hai.”

Unhone dekha ki bure sanket dikh rahe the. Ghode udaas the, pakshi ajeeb awaazein kar rahe the aur sena mein darr fail raha tha.

Drona bole, “Yeh sab bade vinash ka sanket hai. Arjun ke baan hamari sena ko bahut nuksan pahunchayenge.”

Sena ke kai yoddha ghabra gaye. Kisi mein ladne ka utsaah nahi dikh raha tha.

Lekin Arjun shaant aur nishchay se bhara hua apne rath par khada tha, yudh ke liye taiyaar."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.22
        with st.expander("Section 4.4.22  Section XLVII"):
            text1 = """ 
            Duryodhan ki Chinta aur Karna ka Gussa

Vaisampayana ne kaha, “Yudh ke maidan mein Duryodhan ne Bhishma, Dronacharya aur Kripacharya se baat ki.”

Duryodhan bola, “Pandavo ne vaada kiya tha ki woh 12 saal vanvaas aur 1 saal agyaatvaas mein rahenge. Lekin lagta hai Arjun samay poora hone se pehle hi saamne aa gaya hai.”

Usne kaha, “Agar Arjun sach mein pehle dikh gaya hai, toh Pandavo ko phir se vanvaas jaana padega.”

Duryodhan thoda confused bhi tha. Woh bola, “Ho sakta hai humse hi hisaab mein galti hui ho. Isliye Bhishma Pitamah sahi samay ka faisla karein.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Phir usne sena ko yaad dilaya ki woh Matsya desh ki gaayein churaane aaye hain aur ab chahe saamne Matsya ka raja ho ya Arjun, unhe yudh toh karna hi padega.

Duryodhan ne dekha ki bade-bade yoddha bhi shaant aur soch mein pade hue hain.

Woh bola, “Aise darr kar baithne ka samay nahi hai. Humein himmat se ladna hoga.”

Tab Karna ko gussa aa gaya.

Usne kaha, “Dronacharya hamesha Arjun ki tareef karte rehte hain. Sirf uske ghodon ki awaaz sunkar hi sabko dara diya gaya hai.”

Karna bola, “Pandav hamesha Drona ke favourite rahe hain. Isi wajah se woh Arjun ki itni prashansa kar rahe hain.”

Usne sena ko sambhalte hue kaha, “Abhi darne ka nahi, taiyaari karne ka waqt hai. Gaayon ko surakshit rakho aur sena ko yudh ke liye taiyaar karo.”

Karna ne kaha, “Sirf baatein karne se kuch nahi hoga. Humein milkar dushman ka saamna karna hoga.”

Is tarah Kaurav sena mein tension aur chinta badh gayi, lekin yudh ki taiyaari bhi tezi se hone lagi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.23
        with st.expander("Section 4.4.23  Section XLVIII"):
            text1 = """ 
            Karna ka Garv aur Arjun ko Chunauti

Karna ne Kaurav sena ko dekhkar kaha, “Tum sab itne dare hue kyun lag rahe ho? Chahe saamne Matsya ka raja ho ya Arjun, main uska saamna akela kar sakta hoon.”

Usne garv se apne baanon ki tareef ki.

Karna bola, “Mere teer tez saanpon ki tarah seedhe jaakar nishana lagate hain. Aaj main Arjun ko itne teeron se dhak dunga jaise tiddiyan kisi ped ko dhak leti hain.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Woh aur bhi ahankaar se bola, “Meri dhanush ki awaaz nagadon ki tarah goonjegi aur mere baan aasman ko jugnuon ki tarah bhar denge.”

Karna ne Arjun ko challenge dete hue kaha, “Arjun bahut mahaan yoddha hoga, lekin main bhi usse kam nahi hoon.”

Usne yaad dilaya ki usne Parashuram se divya astron ka gyaan paaya hai.

Karna bola, “Main aaj Arjun ko hara kar Duryodhan ke dil ka darr mita dunga.”

Usne Arjun ke rath ke dhwaj ki taraf dekhkar kaha, “Aaj us dhwaj par baitha vanar bhi zameen par gir jayega.”

Karna ka gussa aur garv dono badhte ja rahe the. Woh apne aap ko ek bade tufaan ki tarah samajh raha tha jo Arjun ki agni ko bujha dega.

Usne Kauravo se kaha, “Tum log bas gaayon ko lekar chale jao ya ruk kar mera yudh dekhna chaho toh dekho. Aaj main Arjun ko zaroor haraunga.”

Kaurav sena Karna ki baatein sunkar thodi himmat mein aa gayi. Lekin sabko pata tha ki saamne duniya ka ek mahaan dhanurdhar khada hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.24
        with st.expander("Section 4.4.24  Section XLIX"):
            text1 = """ 
            Kripacharya ki Samajhdari Bhari Salah

Kripacharya ne Karna se kaha, “Hey Karna, tum hamesha bina soche sirf yudh ki baat karte ho. Tum waqt aur paristhiti ka dhyaan nahi rakhte.”

Unhone samjhaya ki har kaam ka sahi samay aur jagah hoti hai. Agar samay theek na ho, toh bahaduri bhi nuksan de sakti hai.

Kripa bole, “Buddhiman log bina soche-samjhe yudh nahi karte.”

Phir unhone Arjun ki mahaanta yaad dilayi."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Arjun ne akela Gandharvon ko haraya tha. Usne Agni dev ki madad ki thi. Woh Himalaya mein kathin tapasya kar chuka hai.”

Kripa ne kaha, “Usne Shiv ji tak se yudh kiya aur Indra se divya astron ka gyaan paaya. Devta bhi usse ladne se pehle sochenge.”

Phir unhone Karna ko samjhate hue kaha, “Tum bina soche Arjun ko challenge de rahe ho. Yeh aisa hai jaise koi zahreeli saanp ke daant haath se todne ki koshish kare.”

Unhone aur misaalein diं.

“Jaise koi aadmi bina taiyaari ke jalti hui aag mein chala jaye ya gale mein patthar baandhkar samundar paar karne nikle — waise hi akela Arjun se ladna moorkhta hai.”

Kripacharya ne kaha, “Humne Pandavo ke saath anyaay kiya tha. Ab agar Arjun saamne aaya hai, toh woh bahut gusse mein hoga.”

Lekin unhone himmat nahi chhodi.

Kripa bole, “Humein darna nahi chahiye, lekin akela ladne ki zidd bhi nahi karni chahiye.”

Unhone salah di, “Hum sab milkar yudh karein — Bhishma, Drona, Karna, Ashwatthama aur baaki maharathi saath rahenge. Tabhi hum Arjun ka saamna kar paayenge.”

Is tarah Kripacharya ne gusse aur ahankaar ke beech shaanti aur samajhdari ki baat samjhayi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.25
        with st.expander("Section 4.4.25  Section L"):
            text1 = """ 
            Ashwatthama ka Teekha Jawaab

Ashwatthama ne Karna se kaha, “Hey Karna, abhi tak na toh gaayein poori tarah jeeti gayi hain aur na hi Hastinapur pahunchi hain. Phir tum itna garv kyun kar rahe ho?”

Woh bola, “Sachche veer apni tareef khud nahi karte. Agni chup-chaap jalti hai, Suraj bina shor ke chamakta hai aur Dharti shaanti se sabka bojh uthati hai.”

Ashwatthama ne samjhaya ki har vyakti ko apna dharm imaandari se nibhana chahiye.

Phir usne Pandavo ki tareef ki."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Pandav hamesha dharm aur shastron ke raaste par chale. Unhone apni shakti aur mehnat se rajya paaya.”

Uske baad Ashwatthama ka gussa badh gaya.

Woh bola, “Tumne Pandavo ko yudh mein nahi haraya. Tumne unse rajya chaal aur jua se cheena.”

Usne Draupadi ke apmaan ko yaad dilate hue kaha, “Sabse bada paap tab hua jab Draupadi ko sabha mein beizzati sehni padi. Pandav us dukh ko kabhi nahi bhoolenge.”

Ashwatthama ne kaha, “Arjun ab yahan badla lene aaya hai. Jab woh gusse mein aata hai, toh kisi ko nahi chhodta.”

Woh bola, “Arjun devtaon ke barabar dhanurdhar hai. Uske Gandiva se nikle baan pahaadon ko bhi cheer sakte hain.”

Phir usne Karna ko taana maara.

“Jaisa tumne Shakuni ke saath milkar paasay ka khel khela tha, waise hi ab yudh bhi jeet kar dikhao.”

Ashwatthama ne saaf kaha, “Main Arjun se yudh nahi karunga. Agar Matsya ka raja aaye toh alag baat hai, lekin Arjun se ladna bahut bhayankar hoga.”

Kaurav sena mein ab darr aur tension aur bhi badhne laga tha. Sabko mehsoos ho raha tha ki ek bahut bada yudh shuru hone wala hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.26
        with st.expander("Section 4.4.26  Section LI"):
            text1 = """ 
            Bhishma ki Shaanti Bhari Salah

Bhishma Pitamah ne sabko shaant karte hue kaha, “Ashwatthama aur Kripacharya dono sahi keh rahe hain. Aur Karna bhi sirf Kshatriya dharm ke kaaran yudh ki baat kar raha hai.”

Unhone kaha, “Dronacharya ko dosh dena galat hai. Arjun jaise mahaan yoddha ko dekhkar kisi ka bhi mann hil sakta hai.”

Bhishma ne samjhaya ki Pandav bahut mushkilein jhelkar ab saamne aaye hain. Isliye unki shakti aur himmat aur bhi badh gayi hai.

Woh bole, “Ab ladai ka samay hai, aapas mein jhagda karne ka nahi.”"""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Phir Bhishma ne Ashwatthama ki tareef ki.

“Tumhare andar Vedo ka gyaan aur divya astron ki shakti dono hain. Yeh bahut rare baat hai.”

Unhone sabko ekjut rehne ko kaha.

“Senapatiyon ka aapas mein ladna sena ke liye sabse bada sankat hota hai. Isliye humein milkar Arjun ka saamna karna chahiye.”

Ashwatthama ne vinamrata se jawab diya, “Pitamah, main bas itna keh raha tha ki dushman ke achhe gun bhi sachchai se maan lene chahiye.”

Tab Duryodhan ne baat sambhali.

Woh bola, “Agar Dronacharya humare saath shaant mann se khade hain, toh humein himmat milti hai.”

Uske baad Bhishma, Karna aur Kripacharya ne milkar Dronacharya ko shaant kiya.

Phir Dronacharya bole, “Main pehle hi shaant ho chuka hoon. Ab humein dhyaan dena chahiye ki Arjun Duryodhan tak na pahunch sake.”

Unhone warning di, “Arjun sirf gaayein wapas lekar nahi rukega. Woh hum par hamla bhi karega.”

Drona ne kaha, “Isliye sena ko sambhal kar taiyaar karo aur Duryodhan ki raksha karo.”

Sabko ab samajh aa gaya tha ki saamne sirf ek yoddha nahi, balki khud Arjun khada hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.27
        with st.expander("Section 4.4.27  Section LII"):
            text1 = """ 
            Bhishma ka Faisla aur Yudh ki Taiyaari

Bhishma Pitamah ne shaant swar mein kaha, “Samay ka chakra hamesha chalta rehta hai — din, mahine aur saal sab badalte rehte hain.”

Unhone hisaab samjhate hue kaha, “Pandavo ne jo 13 saal vanvaas aur agyaatvaas ka vaada kiya tha, woh poori tarah sach hai. Unka samay khatam ho chuka hai.”

Bhishma bole, “Yudhishthir jaise dharmic vyakti ke hote hue Pandav kabhi jhooth ya adharm ka raasta nahi chunenge.”

Unhone Pandavo ki imaandari ki tareef ki.

“Pandav jhooth bolne se achha maut ko chunenge. Lekin jab samay aayega, woh apna haq lene ke liye kisi se bhi ladenge.”

Bhishma ne sabko sachchai bata di."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yudh mein jeet aur haar dono ho sakte hain. Koi bhi pehle se pakka nahi keh sakta ki kaun jeetega.”

Phir unhone jaldi taiyaari karne ko kaha, kyunki Arjun bahut paas aa chuka tha.

Tab Duryodhan ne zidd se kaha, “Main Pandavo ko unka rajya kabhi wapas nahi dunga.”

Yeh sunkar Bhishma ne yudh ki yojana banayi.

Unhone kaha, “Sena ka ek hissa Duryodhan ke saath Hastinapur ki taraf jaaye. Dusra hissa gaayon ko surakshit lekar nikle.”

“Baaki aadhi sena yahin rukkar Arjun ka saamna karegi.”

Bhishma ne sabko apni jagah di.

“Dronacharya beech mein rahenge. Ashwatthama left side sambhalen. Kripacharya right side ki raksha karein. Karna aage se hamla karega.”

Aur Bhishma khud poori sena ke peeche khade hokar sabki raksha karne lage.

Is tarah Kaurav sena ne darr aur confusion ko chhodkar yudh ki poori taiyaari shuru kar di."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.28
        with st.expander("Section 4.4.28  Section LIII"):
            text1 = """ 
            Arjun ka Bhayankar Pravesh

Vaisampayana ne kaha, “Jab Kaurav sena yudh ke liye taiyaar ho gayi, tab Arjun apne rath ki zor daar awaaz ke saath tezi se unki taraf badhne laga.”

Kauravo ne door se uska vanar wala dhwaj dekha. Gandiva ki tan-tan ki awaaz aasman mein goonj rahi thi.

Dronacharya ne Arjun ko dekhkar kaha, “Yeh Parth ka dhwaj hai. Aur yeh uske rath aur Gandiva ki awaaz hai. Us dhwaj par baitha vanar bhi sena mein darr faila raha hai.”

Tabhi Arjun ne kuch baan chalaaye. Do baan Drona ke pairon ke paas gire aur do unke kaanon ke paas se nikle."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Drona muskuraaye aur bole, “Arjun mujhe pranam kar raha hai.”

Unhone Arjun ko pyaar se dekha aur kaha, “Bahut samay baad hum Dhananjay ko dekh rahe hain. Woh apne divya astron aur tej ke saath chamak raha hai.”

Udhar Arjun ne Uttara se kaha, “Rath ko aise chalao ki mere baan seedhe dushman tak pahunch sakein.”

Phir usne Duryodhan ko dhoondte hue kaha, “Mujhe sirf us dusht Duryodhan ko harana hai. Uske haarte hi baaki sab khud ko hara hua maan lenge.”

Arjun ne dekha ki Duryodhan sena se door gaayon ko lekar nikal raha hai.

Woh bola, “Chalo usi ki taraf. Wahin yudh ka asli matlab hai.”

Uttara ne turant rath mod diya aur Duryodhan ki taraf badhne laga.

Kripacharya ne yeh dekhkar sabko warning di.

Woh bole, “Arjun seedha Duryodhan ki taraf ja raha hai. Agar woh gusse mein aa gaya, toh use rokna bahut mushkil hoga.”

Tab Arjun ne apna naam pukaar kar yudh ka elan kiya aur teeron ki baarish shuru kar di.

Uske baan itne zyada the ki aasman aur zameen dono dhak gaye. Kaurav sena kuch der ke liye kuch dekh hi nahi paayi.

Kai yoddha darr kar hil gaye. Kuch toh bhaag bhi nahi pa rahe the.

Phir Arjun ne apna shankh bajaya. Gandiva ki awaaz aur vanar dhwaj ki garaj se poori dharti kaamp uthi.

Gaayein bhi darr kar mud gayin aur Duryodhan ki taraf se wapas lautne lagiं.

Us samay sabko mehsoos ho gaya tha ki Arjun sirf ek yoddha nahi, balki aandhi ki tarah yudh ke maidan mein utar chuka hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.29
        with st.expander("Section 4.4.29  Section LIV"):
            text1 = """ 
            Arjun aur Karna ka Tez Yudh

Vaisampayana ne kaha, “Arjun ne Kaurav sena ko todkar gaayon ko wapas bhej diya. Lekin uska yudh abhi khatam nahi hua tha. Woh seedha Duryodhan ki taraf badhne laga.”

Kaurav yoddha samajh gaye ki Arjun apna kaam kar chuka hai aur ab asli yudh shuru hoga.

Arjun ne Uttara se kaha, “Ghodo ko tez chalao. Mujhe Karna tak pahunchna hai. Woh bahut garv kar raha hai.”

Uttara ne rath ko bijli ki tarah sena ke beech dauda diya.

Tab Karna ki madad ke liye kai Kaurav yoddha aage aaye. Unhone Arjun par teeron ki baarish kar di."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Lekin gusse mein bhare Arjun ne apne agni jaise baanon se poori sena ko hila diya. Aisa lag raha tha jaise jungle mein bhayankar aag lag gayi ho.

Vikarna ne Arjun ko rokne ki koshish ki. Lekin Arjun ne ek hi pal mein uska dhanush aur dhwaj kaat diya.

Darr kar Vikarna yudh se bhaag gaya.

Phir Shatruntapa naam ka yoddha Arjun par toot pada. Usne bahut teer chalaaye, lekin Arjun ne use bhi maar giraaya.

Kaurav sena ab hilne lagi thi. Kai yoddha zameen par gir rahe the.

Arjun apne Gandiva ke saath yudh bhoomi mein aise ghoom raha tha jaise aandhi pedon ko uda deti hai.

Tab Karna ka bhai Sangramjit bhi Arjun se lada. Lekin Arjun ne uska sir ek teer se kaat diya.

Yeh dekhkar Karna ka gussa bhadak utha.

Woh zor se garja aur seedha Arjun par hamla kar diya.

Dono mahaan dhanurdhar ek doosre par teeron ki baarish karne lage. Aasman teeron se bhar gaya.

Kaurav sena chup-chaap yeh mahaan yudh dekhne lagi.

Karna ne Arjun ke ghodon aur rath par teer chalaaye. Lekin Arjun aur bhi gusse mein aa gaya.

Woh sher ki tarah garja aur usne Karna ke poore shareer par tez baan barsa diye.

Arjun ke teer Karna ke haath, pair, gardan aur maathe mein lage. Karna buri tarah ghaayal ho gaya.

Aakhir mein Karna Arjun ke saamne tik nahi paaya.

Woh yudh bhoomi chhodkar bhaag gaya, bilkul us haare hue haathi ki tarah jo kisi aur zyada shaktishaali haathi se haar jaata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 4.4.30
        with st.expander("Section 4.4.30  Section LV"):
            text1 = """ 
            Arjun ka Aandhi Jaisa Yudh

Vaisampayana ne kaha, “Karna ke bhaagne ke baad bhi yudh nahi ruka. Duryodhan aur dusre Kaurav yoddha apni sena ke saath Arjun par toot pade.”

Lekin Arjun samundar ke kinaare ki tarah mazboot khada raha. Woh bina dare apne divya astron se yudh karta raha.

Uske Gandiva se nikle teer aasman ko dhak rahe the. Sena mein aisa koi yoddha nahi tha jo ghaayal na hua ho.

Log Arjun ko dekhkar hairaan reh gaye. Woh pralaya ki agni ki tarah lag raha tha jo sab kuch jalakar khatam kar deti hai."""
            create_image_text_layout(
                "attached_assets/chapter4/4.4.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Kaurav sena ke ghode darr kar bhaagne lage. Haathi zameen par girne lage. Toote hue rath aur jhande poore maidan mein bikhar gaye.

Arjun ka vanar dhwaj garaj raha tha. Uska shankh aur Gandiva ki awaaz sunkar Kaurav sena ka hausla tootne laga.

Kai yoddha sochne lage, “Yeh Arjun nahi, swayam Mrityu dev aaye hain.”

Arjun itni tezi se teer chala raha tha ki uska dhanush hamesha gola jaisa dikh raha tha. Har teer seedha apne nishaan par lag raha tha.

Usne Drona, Dushasan, Ashwatthama, Kripacharya aur Duryodhan sabko teeron se ghaayal kar diya.

Phir usne Karna ke kaan par ek tez baan maara. Karna ka rath toot gaya aur uski sena darr kar tootne lagi.

Tab Uttara ne poocha, “Hey Parth, ab rath kis taraf le jaun?”

Arjun ne shaant swar mein har maharathi ki taraf ishara karke bataya.

“Wahan Kripacharya hain. Mujhe unke paas le chalo. Main unhe apni dhanurvidya dikhaunga.”

Phir Arjun ne Dronacharya ko dekha aur bola, “Woh mere guru hain. Pehle unka samman karna zaroori hai.”

Arjun ne Uttara se kaha ki Drona ke rath ke paas se samman ke saath guzarna.

Usne Ashwatthama ko bhi respect se dekha aur bola, “Woh bhi mahaan yoddha hain.”

Phir Arjun ki nazar Duryodhan par padi.

Woh bola, “Ab mujhe uske paas le chalo. Aaj main use apni asli tezi dikhaunga.”

Aakhir mein Arjun ne Bhishma Pitamah ko dekha.

Unhone sona jaisa chamakta kavach pehna tha aur poori sena ke beech Suraj ki tarah chamak rahe the.

Arjun ne dheere se kaha, “Pitamah hum sabke bade hain. Unke paas sabse aakhir mein chalenge.”

Is tarah yudh ke beech bhi Arjun ne apne guru aur buzurgon ka samman kabhi nahi chhoda."""
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
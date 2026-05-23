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
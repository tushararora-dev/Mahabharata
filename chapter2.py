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
    create_image_text_layout("attached_assets/chapter2/chapter2.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter2/banner2.jpg", layout="full")


    text0 = """
    <h2>Sabha Parva (The Book of Assembly Hall)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    
    with st.expander("Chapter 2.1 – Sabhakriya Parva (The Hall Proceedings)"):
    
        # --------------------------------------------------
        # Section 2.1.1
        # --------------------------------------------------
        with st.expander("Section 2.1.1 – Section I"):
            text1 = """ 
            Om!
Sabse pehle Narayana,
phir Nara,
aur Sarasvati ko pranam.
Iske baad “Jaya” shabd bola jaata hai.

Vaisampayana bole—
Krishna ke saamne, Maya Danava ne Arjuna ko namaskar kiya.
Uske haath jude hue the.
Uski awaaz mein vinamrata thi.

Maya bola,
“Hey Kunti-putra,
aapne mujhe Krishna ke krodh se
aur Agni ki aag se bacha liya.
Ab bataiye, main aapke liye kya karun?”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.1.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Arjuna shaant the.
Unhone muskurakar kaha,
“Tumne pooch kar hi sab kuch kar diya.
Tum swatantra ho.
Jahan chaho jao.
Bas hum par sada kripa aur mitrata rakhna.”

Par Maya ruka nahi.
Usne kaha,
“Hey veer,
main Danavon ka Vishvakarma hoon.
Kala meri shakti hai.
Main kuch banana chahta hoon—
aapke liye, khushi se.”

Arjuna ne dhairya se kaha,
“Main tumse kuch nahi maangta.
Par tumhara mann bhi todna nahi chahta.
Agar kuch karna hi hai,
to Krishna ke liye karo.
Wahi mere liye sabse bada uphaar hoga.”

Krishna ne kuch pal socha.
Phir bole,
“Maya,
agar tum sach mein kuch dena chahte ho,
to Yudhishthira ke liye
ek aisi sabha (raj-sabha) banao—
jo dev, danav aur manav
teenon ki kala ka sangam ho.

Aisi sabha banao
jise dekhkar bhi
manushya kabhi na bana paaye.”

Maya ka chehra chamak utha.
Usne turant kaam shuru kar diya.

Usne Pandavon ke liye
ek adbhut mahal banaya—
bilkul dev-lok jaisa.

Krishna aur Arjuna
sab baat Yudhishthira ko batane le gaye.
Maya ko unse milwaya.
Yudhishthira ne Maya ka
poore sammaan se swagat kiya.

Maya prasann ho gaya.
Usne Danavon ki kathayein sunayi.
Phir shubh din dekhkar,
brahmanon ko bhojan aur daan diya.
Aur 5000 haath lambai-chauda
ek sundar bhoomi chuni.

Wahin se shuru hui
mayaavi sabha ki rachna—
jo aage chal kar
itihas banne wali thi.

🌟 Is Katha ka Sandesh

Upkaar ka badla ahankar se nahi, vinamrata se hota hai

Sahi kala, sahi jagah par di jaaye to amar ho jaati hai

Sachchi mitrata mein maang nahi, samarpan hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # --------------------------------------------------
        # Section 2.1.2
        # --------------------------------------------------
        with st.expander("Section 2.1.2 – Section II"):
            text1 = """ 
            Vaisampayana bole—

Krishna, jo sabke poojya the,
Khandavaprastha mein kuch samay tak
Pandavon ke saath khushi se rahe.

Ek din unke mann mein ichha jagi—
“Ab pitaji ko dekhna chahiye.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.1.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Krishna ne sabse pehle
Yudhishthira ko pranam kiya.
Phir Pritha (Kunti) ke charan chhuye.
Kunti ne pyaar se
Krishna ka sir chooma aur gale lagaya.

Yeh pal bahut bhaavuk tha 💛

Phir Krishna apni behen
Subhadra ke paas gaye.
Unki aankhon mein aansu the.
Unhone madhur aur satya bhare shabd kahe.

Subhadra ne bhi sir jhuka kar
Krishna ko pranam kiya
aur apna sandesh
paitrik parivaar ke liye diya.

Uske baad Krishna ne
Draupadi
aur Dhaumya rishi se bhi
vidai li.

Phir Arjuna ke saath
Krishna apne bandhuon ke beech aaye.
Paachon Pandav unke ird-gird the.
Krishna aise lag rahe the
jaise Indra dev devtaon ke beech ✨

Yatra se pehle
Krishna ne snaan kiya.
Abhushan pehne.
Devtaon aur brahmanon ki pooja ki.
Phool, mantra aur sugandh se
sabko santusht kiya.

Phir Krishna apne
sone ke rath par chadhe.
Rath par Garuda dhwaj tha.
Saath mein Sudarshan chakra, gada, talwar,
aur Sharnga dhanush bhi the.

Shubh muhurat mein
yatra shuru hui 🌿

Pyaar ke kaaran
Yudhishthira khud rath par chadhe
aur Daruka ko hata kar
khud reins pakad li.

Arjuna ne Krishna ke chaaron taraf ghoom kar
unhe chamara se hawa di.

Bhima, Nakula, Sahadeva,
purohit aur nagrik—
sab peeche-peeche chale.

Krishna aise chamak rahe the
jaise guru apne priya shishyon ke saath 🙏

Thodi door jaakar
Krishna ne Yudhishthira se kaha,
“Bas yahin tak.”

Unhone Yudhishthira ke charan chhuye.
Yudhishthira ne turant
Krishna ko utha kar gale lagaya
aur sir chooma.

Pandav Krishna ko
jab tak dekh sakte the,
tab tak dekhte rahe.
Jab Krishna nazron se ojhal hue,
to mann bhi unke saath chala gaya 💔

Bina mann ke
Pandav wapas laut aaye.

Krishna apne rath mein
Dwarka pahunch gaye.
Saath mein Satyaki bhi tha.

Dwarka mein
Krishna ka bhavya swagat hua.
Unhone pita-mata ko pranam kiya.
Baladeva ko gale lagaya.

Phir apne putron aur parivaar se mile—
aur ant mein
Rukmini ke mahal mein pravesh kiya.

🌼 Is katha ka sandesh

Sachcha rishta kabhi doori se kam nahi hota

Prem aur maryada saath-saath chalte hain

Vidai mein aansu ho sakte hain, par hriday mein shanti hoti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # --------------------------------------------------
        # Section 2.1.3
        # --------------------------------------------------
        with st.expander("Section 2.1.3 – Section III"):
            text1 = """ 
            Vaisampayana bole—

Maya Danava ne
Arjuna se namrata se kaha,
“Ab main ja raha hoon.
Par bahut jaldi wapas aaunga.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.1.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """
            Maya bola,
“Kailasa parvat ke uttar mein,
Mainaka pahaadon ke paas,
Vindu naam ka ek pavitra talaab hai.
Wahin maine pehle
ratnon aur heere-jawahar se bhara
bahut saara samaan ikattha kiya tha.”

“Woh sab kabhi
Danav raja Vrishaparva ke mahal mein rakha gaya tha.
Agar woh abhi bhi maujood hai,
toh main use lekar aaunga.”

Phir Maya ne ek aur baat batayi—
“Usi Vindu talaab mein
ek bhayanak gada (mace) bhi hai.
Woh itni shaktishaali hai
jaise Bhima ke liye hi bani ho.”

“Wahin ek shankh Devadatta bhi hai,
jo Varuna dev se aaya tha.
Uski awaaz se
sab kaanp uthte hain.”

Yeh sab kehkar
Maya uttar–poorv disha mein chala gaya.
Kailasa ke paas
Hiranya-shringa naam ka
ratnon se bhara ek shikhar tha.
Uske paas hi Vindu talaab tha.

Yahin kabhi
Bhagiratha raja ne tapasya ki thi
Ganga Maa ko prithvi par laane ke liye.
Yahin Indra dev ne
sau yagya kiye the.
Yahin Mahadeva bhi nivas karte hain.

Yeh jagah
bahut pavitra aur divya thi ✨

Maya wapas lauta
aur saath mein le aaya—

bhayanak gada

Devadatta shankh

anek ratn aur heere

Usne in sab se
Pandavon ke liye
ek adbhut mahal banana shuru kiya.

Us mahal ko baad mein
Maya Sabha kaha gaya.

Maya ne
Bhima ko woh shaktishaali gada di 💪
Arjuna ko Devadatta shankh di 📯

Yeh mahal
paanch hazaar haath lamba–chauda tha.
Sone ke stambh the.
Heeron ki deewarein thi.
Itni chamak thi
ki suraj ki roshni bhi feeki lagne lagi ☀️

Mahal ke beech mein
ek jaadui sarovar tha.
Usme kamal the—
ratnon ke patte,
sone ke phool,
aur chamakdar machhliyan 🪷

Kayi raja
use zameen samajh kar
paani mein gir jaate the 😄

Charon taraf
hamesha hara-bhara van tha.
Thandi hawa chalti rehti thi.
Hans aur pakshi
sarovar mein khelte rehte the.

Is mahal ki raksha ke liye
8,000 bhayanak Rakshas tainaat the.
Par Pandavon ke liye
yeh jagah shanti aur sukh se bhari thi.

Sirf 14 mahine mein
Maya ne yeh sab taiyaar kar diya.
Phir usne jaakar
Yudhishthira ko bataya—

“Rajan,
Pandavon ka mahal
ab poori tarah taiyaar hai.”

🌼 Is katha ka sandesh

Kritagyata (gratitude) se mahaan karya janam lete hain

Kala aur buddhi sahi haathon mein ho to chamatkar hota hai

Sewa bhav se kiya kaam amar ho jaata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # --------------------------------------------------
        # Section 2.1.4
        # --------------------------------------------------
        with st.expander("Section 2.1.4 – Section IV"):
            text1 = """ 
            Vaisampayana bole—

Jab Yudhishthira,
jo Dharma ke putra aur manushyon mein shreshtha the,
Maya Sabha mein pravesh karne wale the,
toh sabse pehle unhone daana–dharma kiya 🙏"""
            create_image_text_layout(
                "attached_assets/chapter2/2.1.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            🍚 Brahmanon ka Satkar

Raja Yudhishthira ne
10,000 Brahmanon ko bhojan karaya—

doodh aur chawal

ghee aur shahad

phal–mool

anek prakaar ke shakahari aur maansahari bhojan

Unhe naye vastra,
phoolon ke haar,
aur har ek ko hazaar gaayen bhi daan mein di 🐄

Khush hokar Brahman bole—
“Kitna shubh din hai aaj!”
Unki awaaz aisi thi
jaise swarg tak pahunch gayi ho ✨

🎶 Rajya–mahotsav ka aarambh

Phir Yudhishthira ne
devtaon ki pooja ki—

sangeet

sugandhit dhoop

madhur vadya

Jab ve Sabha mein pravesh hue,
toh nartak, gavaiye,
kathavachak aur veer
apni kala se unka swagat karne lage 🎭

Pandav bhaiyon ke saath
Yudhishthira us mahal mein
aise shobhit hue
jaise Indra dev swarg mein 🌟

🧘 Rishiyon aur Mahamuniyon ki Sabha

Us Maya Sabha mein
desh–videsh se aaye
anek Rishi aur Mahamuni baithe the—
jo Vedo ke gyata,
shant, pavitra aur tapasvi the।

Unki pavitra baaton se
Raja Yudhishthira ka mann
aur bhi prasann ho gaya 🌼

👑 Maha–Rajyon ke Raja

Sirf Rishi hi nahi,
balki anek shaktishaali Kshatriya raja bhi aaye—
Anga, Vanga, Magadha, Kalinga, Madra, Yavana, Kirata
aur kai anya rajyon ke veer raja ⚔️

Sabhi
Yudhishthira ki seva
aur unki khushi ke liye
ekatra hue the।

🏹 Arjuna ke Shishya

Kai yuva rajkumaar
jo Arjuna
se shastra–vidya seekh rahe the,
ve bhi deer–charm pehne
vinamrata se Sabha mein upasthit the।

🎵 Gandharva aur Apsara

Swarg se aaye
Gandharva, Apsara aur Kinnara
madhur geet aur sangeet se
Sabha ko aur bhi divya bana rahe the 🎶

🌺 Ant mein

Yeh poori Sabha
aisi lag rahi thi
jaise Brahma lok ho—
aur Yudhishthira
uske madhya mein
Dharma ke prateek ke roop mein
virajmaan the 🌸

🌼 Is Adhyay ka Sandesh

Daan aur satkar se rajya pavitra hota hai

Gyaan aur shakti jab Dharma ke saath ho, tab hi shobha deti hai

Sahi raja wahi hai jo sabka samman kare"""
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.2 – Lokapala Sabhakhyana Parva (Assembly of the World Guardians)"):

        with st.expander("Section 2.2.1 – Section V"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.2 – Section VI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.3 – Section VII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
        with st.expander("Section 2.2.4 – Section VIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.5 – Section IX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.6 – Section X"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.7 – Section XI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.8 – Section XII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.9 – Section XIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.2.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.3 – Rajasuyarambha Parva (Commencement of the Rajasuya Sacrifice)"):

        with st.expander("Section 2.3.1 – Section XIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.2 – Section XV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.3 – Section XVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.4 – Section XVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.5 – Section XVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.6 – Section XIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.4 – Jarasandha-badha Parva (Slaying of Jarasandha)"):

        with st.expander("Section 2.4.1 – Section XX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.2 – Section XXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.3 – Section XXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.4 – Section XXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.5 – Section XXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.4.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
    
    with st.expander("Chapter 2.5 – Digvijaya Parva (The Universal Conquest)"):

        with st.expander("Section 2.5.1 – Section XXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.2 – Section XXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.3 – Section XXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.4 – Section XXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.5 – Section XXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.6 – Section XXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.7 – Section XXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.5.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
    
    with st.expander("Chapter 2.6 – Rajasuyika Parva (Performance of the Rajasuya Sacrifice)"):

        with st.expander("Section 2.6.1 – Section XXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.2 – Section XXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.3 – Section XXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.4 – Section XXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.5 – Section XXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.6 – Section XXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.7 – Section XXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter2/2.6.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.7 – Sisupala-badha Parva (Death of Sisupala)"):

        with st.expander("Section 2.7.1 – Section XXXIX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.1.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.2 – Section XL"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.2.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.3 – Section XLI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.3.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.4 – Section XLII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.4.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.5 – Section XLIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.5.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.6 – Section XLIV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.6.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.7 – Section XLV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.7.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.8 – Section XLVI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.8.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.9 – Section XLVII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.9.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.10 – Section XLVIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.10.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.11 – Section XLIX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.11.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.12 – Section L"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.12.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.13 – Section LI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.13.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.14 – Section LII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.14.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.15 – Section LIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.15.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.16 – Section LIV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.16.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.17 – Section LV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.17.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.18 – Section LVI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.18.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.19 – Section LVII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.19.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.20 – Section LVIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.20.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.21 – Section LIX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.21.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.22 – Section LX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.22.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.23 – Section LXI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.23.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.24 – Section LXII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.24.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.25 – Section LXIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.25.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.26 – Section LXIV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.26.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.27 – Section LXV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.27.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.28 – Section LXVI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.28.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.29 – Section LXVII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.29.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.30 – Section LXVIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.30.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.31 – Section LXIX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.31.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.32 – Section LXX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.32.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.33 – Section LXXI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.33.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.34 – Section LXXII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.34.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.35 – Section LXXIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.35.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.36 – Section LXXIV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.36.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.37 – Section LXXV"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.37.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.38 – Section LXXVI"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.38.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.39 – Section LXXVII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.39.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.40 – Section LXXVIII"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.40.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.41 – Section LXXIX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.41.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.42 – Section LXXX"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter2/2.7.42.jpg", text1, layout="side", image_position="left")
            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")

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
    <h2>Sabha Parva (The Book of Assembly Hall  )</h2>
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
            text1 = """ 
            Section V – Rishi Narada ka Raj-dharma Updesh
            Pandavas apni Sabha mein baithe the.
Sab shaant tha.
Sab maryada mein.

Tab achanak,
akash se Rishi Narada aaye 🌸
Veena ki madhur dhun ke saath.

Narada ji bahut gyaani the.
Vedas jaante the.
Upanishads jaante the.
Purane yugon ki kahaniyaan bhi.

Unka mann tez tha.
Buddhi gehri thi.
Sach aur galat ka antar unhe saaf dikhta tha."""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            👑 Pandavas ka Aadar

Narada ji ko dekh kar
Yudhishthira turant khade hue.

Bhaiyon ke saath
vinamrata se jhuk gaye 🙏

Unhe aasan diya.
Arghya diya.
Doodh, shahad aur ratna diye.

Narada ji prasann ho gaye 😊

🧠 Narada ka Prashn

Narada ji ne dheere se poocha:

“Rajaa,
jo dhan kama rahe ho,
kya sahi jagah kharch ho raha hai?”

“Kya tumhara mann
dharma mein lagta hai?”

“Sukh bhogte hue
mann bhari toh nahi ho jaata?”

“Kahin sukh ke liye
dharma ko toh nahi chhod rahe?”

Unhone kaha:

“Rajaa ko
Dharma – Artha – Kaam – Moksha
sabka balance rakhna chahiye.”

⚖️ Achha Raja kaise hota hai

Narada ji ne samjhaya:

Raja samay par faisla karta hai

Gupt baatein gupt rakhta hai

Galat mantriyon ko door rakhta hai

Sahi logon ko zimmedari deta hai

“Ek bhi gyaani aur imandaar mantri
poore rajya ko upar utha sakta hai.”

🌾 Praja ka Khayal

Narada bole:

“Kya kisan khush hain?”

“Kya beej aur paani mil raha hai?”

“Kya vyapari bina darr ke
rajya mein aa-ja sakte hain?”

“Kya sainikon ko
samay par vetan milta hai?”

Unhone kaha:

“Jahan praja sukhi hoti hai,
wahi rajya majboot hota hai.”

🕊️ Nyay aur Daya

Narada ji ne kaha:

Raja maa–baap jaisa ho

Ameer–gareeb sab barabar

Bina gussa, bina laalach

Bina anyaay

“Jo sharan maange,
uski raksha karo.”

📚 Gyaan ka Mahatva

Narada bole:

“Hazaar murkh se
ek gyaani behtar hota hai.”

“Vidya ka phal
vinamrata hota hai.”

“Dhan ka phal
daan hota hai.”

“Patni ka phal
parivaar aur santaan hota hai.”

🌟 Yudhishthira ka Vachan

Sab sun kar
Yudhishthira ne
Narada ji ke charan chue 🙏

Unhone kaha:

“Mera gyaan
aaj badh gaya.”

“Main aapke har updesh par
chalunga.”

Aur sach mein,
unhone wahi kiya.

🌍 Parinaam

Samay ke saath,
Yudhishthira ne
poori prithvi par
nyay se raj kiya.

Narada ji bole:

“Jo raja
chaar varno ki raksha karta hai,
woh yahan bhi sukhi hota hai
aur swarg bhi paata hai.”

🌱 Kahani ka Moral

Achha raja = dharmic raja

Dhan se zyada mahatva = nyay

Gyaan ka phal = vinamrata

Praja ki khushi = rajya ki shakti"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.2 – Section VI"):
            text1 = """ 
            Section VI – Raja Yudhishthira aur Narada ka Samvaad
Narada ji ke updesh khatam hue.
Sab shaant ho gaye.

Yudhishthira ne
vinamrata se Narada ji ko pranam kiya 🙏
aur unka poora aadar kiya."""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            🌼 Yudhishthira ka Uttar

Yudhishthira bole:

“O Mahatma,
aapne jo dharma aur maryada batayi,
woh bilkul sahi hai.”

“Main apni poori shakti se
un niyamon par chalne ki koshish karta hoon.”

“Purane dharmic raja
jo raasta chalte the,
wahi sahi raasta hai.”

“Hum bhi wahi raah chunna chahte hain,
jahan mann par poora niyantran ho.”

Narada ji muskuraye 😊

🤔 Ek Jigyaasa

Thoda soch kar,
Yudhishthira ne ek prashn poocha:

“O Narada ji,
aap mann ki gati se
anek lokon mein ghoomte ho.”

“Kya aapne kabhi
meri is Sabha jaisi
ya isse bhi shreshth
koi Sabha dekhi hai?”

Sab raja aur rishi
shaant ho kar sunne lage 👂

✨ Narada ka Muskurata Uttar

Rishi Narada bole:

“O Raja,
manushya lok mein
tumhari jaisi ratnon se bani Sabha
maine pehle kabhi nahi dekhi.”

“Par haan,
main tumhe dev-lokon ki Sabhao ka varnan kar sakta hoon.”

🏛️ Divya Sabhao ka Sanket

Narada ji bole:

Yama ki Sabha

Varuna ki Sabha

Indra ki Sabha

Kuvera ki Sabha

aur sabse upar,
Brahma ki Sabha

“In sab Sabhao mein
divya aur manav kala ka sundar sangam hota hai.”

“Wahan devta, pitra, rishi
aur shaant tapasvi
sada pooja aur yagya mein lage rehte hain.”

🙏 Sabki Vinamr Prarthana

Yeh sun kar,
Yudhishthira aur unke bhai
haath jod kar bole:

“Kripya humein
un sab Sabhao ka
poora varnan sunaiye.”

“Kaun wahan rehta hai?”
“Sabha kis cheez se bani hoti hai?”
“Kaun kis devta ki seva karta hai?”

Sabki jigyaasa badh gayi ✨

🌟 Narada ka Vachan

Narada ji ne kaha:

“O Raja,
main tumhe ek-ek karke
sabhi divya Sabhao ki kahani sunaunga.”

“Dhyaan se sunna.”

🌱 Moral

Vinamrta gyaan ka pehla darwaza hai

Sachchi jigyaasa se hi gyaan milta hai

Raja ho ya rishi,
seekhna kabhi band nahi hota"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.3 – Section VII"):
            text1 = """ 
            Section VII – Indra ki Divya Sabha (Pushkaramalini Sabha) Narada ji bole:

✨ Indra ki Sabha ka Roop

“Yudhishthira,
Indra ki Sabha
bahut chamakdar aur divya hai.”

Yeh Sabha
Indra ke apne karmon ka phal hai 🌟
Isse Indra ne khud banwaya.

Lambai: 150 yojana

Chaudai: 100 yojana

Unchai: 5 yojana"""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
           Yeh Sabha
jahaan chaho wahan ja sakti hai ✨
Budhapa, dukh, thakaan aur darr
sab yahin mit jaate hain.

Yeh jagah
bahut shubh aur mangalmay hai 🌼
Yahan sundar kamre, aasan
aur divya vriksh lage hue hain.

👑 Indra aur Sachi

Is Sabha ke beech mein,
ek shreshth singhasan par
Indra dev baithe hote hain.

Unke paas baithi hoti hain
unki patni Sachi 💛

Indra ka roop
bataya nahi ja sakta itna sundar hai ✨
Sir par mukut,
baahon par chamakte kangan,
safed vastra
aur rang-birange pushpon ki mala 🌸

Unke saath
yash, shobha aur keerti
khud baithi rehti hai.

🌬️ Kaun-kaun seva karta hai

Marut dev

Siddha aur Sadhya

Divya Rishi

Som yagya karne wale tapasvi

Sab Indra ki seva karte hain 🙏
Sabka mann shant hai.
Koi chinta nahi.
Koi dukh nahi.

🧘 Mahaan Rishi

Is Sabha mein
bahut se prasiddh rishi aate-jaate rehte hain:

Valmiki

Yajnavalkya

Gautama

Pulastya, Pulaha, Kratu

Bhrigu aur Saptarishi

Sab tej se chamakte hain 🔥
Aur Indra ka samman karte hain.

🎶 Apsara aur Gandharva

Yahan Apsaraen naachti hain 💃
Gandharva gaate hain 🎶

Unka nritya aur sangeet
Indra dev ko prasann karta hai.

Yeh Sabha
khushi aur anand se bhari rehti hai 🌈

🌍 Sab kuch yahin maujood

Is Sabha mein yeh sab bhi hote hain:

Agni aur Soma 🔥🌙

Graha aur Nakshatra ⭐

Mantra aur Yagya

Varsha ke badal aur hawayein 🌧️

Shraddha, Buddhi, Vidya, Dhan, Dharma aur Kama

Sab ek hi jagah par ✨

🏛️ Sabha ka Naam

Narada ji bole:

“Is divya Sabha ka naam hai
Pushkaramalini Sabha.”

“Yeh hai
Satakratu Indra ki Sabha
jo maine khud dekhi hai.”

🌱 Chhoti si Seekh (Moral)

Achhe karm se hi divya sthan milte hain

Seva aur vinamrata se mahanta aati hai

Sachcha sukh
shobha ke saath dharma se aata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.4 – Section VIII"):
            text1 = """ 
            Section VIII – Yama Dev ki Divya Sabha Narada ji bole:

🌟 Yama Dev ki Sabha

“Yudhishthira,
ab main tumhe Yama
ki Sabha ke baare mein batata hoon.”

Yeh Sabha
Vishvakarma
ne banayi thi 🛕
Bahut tapasya ke baad.

Yeh Sabha
pighle hue sone jaisi chamak rakhti hai ✨
Sooraj jaise tej se bhari hui."""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
           🌿 Is Sabha ka Vaatavaran

Na zyada thand ❄️

Na zyada garmi 🔥

Dil ko sukoon dene wali hawa 🌬️

Yahan:

Na bhookh hai

Na pyaas hai

Na budhaapa hai

Na dukh hai

Koi bhi bura bhaav
is jagah tik nahi paata 🌼

🍎 Sab kuch uplabdh

Is Sabha mein
har tarah ki cheez milti hai:

Meethi cheezein 🍯

Ras bhara bhojan 🍇

Peene ka amrit jaisa paani 💧

Thanda aur garam, dono prakar ka jal

Ped bhi yahan
mann-chaha phal dete hain 🌳

Phoolon ki mala
bahut sugandhit hoti hai 🌸

👑 Kaun-kaun yahan hota hai

Yama Dev ki Sabha mein
bahut se rajarshi aur maharshi aate hain.

Jaise:

Yayati

Nahusha

Mandhata

Bhagiratha

Janaka

Rama aur Lakshmana

Parashurama

Aur anek mahaan raja
jo dharma ke raaste par chale 👑

⚖️ Yama Dev ka Karya

Yahan Dharma ka raaj hota hai ⚖️
Sab log apne karm ke hisaab se pehchaane jaate hain.

Yama Dev ke saath:

Mrityu (Death)

Kaal (Time)

Pitru dev

Siddha aur Yogi

Sab milkar
nyay aur santulan banaye rakhte hain 🌍

🎶 Sangeet aur Shanti

Is Sabha mein:

Gandharva gaate hain 🎵

Apsara nritya karti hain 💃

Har taraf:

Madhur awaaz

Pavitra sugandh

Shanti aur garima ✨

🧘 Tapasvi aur Sannyasi

Yahan aate hain:

Shant sannyasi

Pavitra tapasvi

Sach bolne wale rishi

Sab safed vastron mein
apne karmon ki chamak ke saath 🌟

🌈 Narada ji ka Sandesh

“Yudhishthira,” Narada ji bole,
“Yeh Yama Dev ki Sabha hai.”

“Yahan nyay bhi hai
aur karuna bhi.”

“Jo dharma ke saath jeeta hai,
uske liye yeh jagah
shanti aur samman se bhari hoti hai.”

🌱 Chhoti si Seekh (Moral)

Karm hi pehchaan hai

Nyay sabke liye ek jaisa

Achha jeevan = shant ant 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.5 – Section IX"):
            text1 = """ 
Section IX – Varuna Dev ki Divya Sabha

Narada ji bole:

🌊 Varuna Dev ki Sabha

“O Yudhishthira,
ab main tumhe Varuna
ki Sabha ke baare mein batata hoon.”

Yeh Sabha
Yama Dev ki Sabha jitni hi vishaal hai,
par iska roop bilkul alag hai ✨

Yeh Sabha
paaani ke beech banayi gayi hai 🌊
Aur isse banaya hai
Vishvakarma ne."""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            🤍 Sabha ka Roop

Deewarein bilkul safed

Darwaze aur gumbad chamakdaar

Har taraf shanti aur thandak 🕊️

Yeh jagah:

Na zyada thandi ❄️

Na zyada garam 🔆

Bas man ko shant kar dene wali

🌳 Divya Van aur Pakshi

Sabha ke charon taraf
ratnon ke ped lage hue hain 💎🌴

In pedon par:

Sundar phal 🍎

Rang-birange phool 🌸

Pedon ke beech:

Chhoti-chhoti baariyaan 🌿

Hazaaron pakshi 🐦

Sab madhur geet gaate rehte hain 🎶

Puri jagah
sangeet aur khushboo se bhari rehti hai.

👑 Varuna Dev ka Singhasan

Is Sabha ke beech
Varuna Dev baithe hote hain 👑

Divya vastra pehne hue

Ratnon ke gehne

Haath mein pash (noose)

Saath mein unki Rani,
jo sugandhit chandan se alankrit hoti hain 🌺

🐍 Naga aur Jal Jeev

Yahan upasthit hote hain:

Vasuki

Takshaka

Karkotaka

Airavana

Sabhi Naga devta
shant mann se Varuna Dev ki seva karte hain 🐍

🌊 Nadiyon ka Sammelan

Is Sabha mein
sab pavitra nadiyaan bhi hoti hain:

Ganga

Yamuna

Narmada

Saraswati

Sindhu

Godavari

Kaveri

Aur anek aur nadiyaan 💧

Sab apne manav roop mein
Varuna Dev ko pranam karti hain 🙏

🏔️ Parvat, Samudra aur Jal Jeev

Chaaron samudra 🌊

Sabhi parvat 🏔️

Har prakar ke jal jeev 🐠

Sab Varuna Dev ki Sabha mein
adar aur shanti ke saath rehte hain.

🎶 Gandharva aur Apsara

Yahan:

Gandharva sangeet bajate hain 🎵

Apsara nritya karti hain 💃

Sab kuch
paaani ki lehron jaisa
komal aur madhur hota hai 🌊🎶

🧠 Varuna Dev ka Mantri

Varuna Dev ke
mukhya mantri Sunabha bhi yahin hote hain.

Unke saath:

Unke putra

Unke pautra

Sab milkar
Varuna Dev ki seva karte hain 🤍

🌱 Chhoti si Seekh (Moral)

Paani jeevan ka aadhaar hai

Jo prakriti ka samman karta hai,
prakriti usse ashirvaad deti hai 🌍

Shanti aur santulan
sabse badi shakti hai 🌊

Narada ji bole:
“Yudhishthira,
yeh thi Varuna Dev ki Sabha.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.6 – Section X"):
            text1 = """ 
            Section X – Kuvera Dev ki Divya Sabha (Dhan aur Samriddhi ka Lok)
            Narada ji bole:

💎 Kuvera Dev ki Sabha

“O Yudhishthira,
ab main tumhe batata hoon
Kuvera
ki Sabha ke baare mein.”

Yeh Sabha
bahut hi chamakdaar hai ✨
Aur apni roshni se
chandramā ko bhi feeka kar deti hai 🌙"""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            🏔️ Sabha ka Aakar

100 yojan lambi

70 yojan chaudi

Is Sabha ko
Kuvera Dev ne
apni tapasya ki shakti se
khud banaya tha 🙏

Yeh Sabha:

Kailasa parvat jaisi chamakti

Aasmaan se judi hui lagti ☁️

Jaise hawa mein tair rahi ho

🏰 Sona, Ratn aur Sugandh

Sabha ke andar:

Sone ke unche mahal 🏰

An-ginat ratn aur mani 💎

Har taraf divya sugandh 🌸

Yeh jagah:

Aankhon ko sukoon

Mann ko anand deti hai 😊

👑 Kuvera Dev ka Singhasan

Is Sabha ke beech:
Kuvera Dev baithe hote hain 👑

Vastra: divya aur sundar

Gehno se sajje hue

Kaanon mein chamakte kundal

Hazaaron Raniyon se ghire hue

Unka singhasan:

Suraj jaisa chamakta ☀️

Divya gaddiyon se sajja hua

🌬️ Mandara Van aur Hawa

Yahan:

Mandara ke ped 🌳

Chameli ke bagiche 🌼

Alaka nadi ke kamal 🌸

Thandi aur meethi hawa
har pal Kuvera Dev ko
prasann karti rehti hai 🍃

🎶 Gandharva aur Apsara

Is Sabha mein:

Gandharva gaate hain 🎵

Apsara nritya karti hain 💃

Jaise:

Rambha

Menaka

Urvashi

Gritachi

Sangeet aur nritya se
Sabha hamesha jeevant rehti hai ✨

🧝 Yaksha aur Guhyaka

Hazaaron Yaksha
Kuvera Dev ki seva mein lage rehte hain:

Manibhadra

Nalakuvera (Kuvera Dev ke putra)

Guhyaka

Kinnara

Sab milkar
dhan aur vyavastha ko
santulit rakhte hain ⚖️

🌺 Lakshmi Ji ki Upasthiti

Is Sabha mein
Lakshmi
hamesha virajmaan rehti hain 🌺

Jahan Lakshmi hoti hain,
wahan:

Dhan hota hai

Samriddhi hoti hai

Par saath hi maryada bhi hoti hai 🙏

🔱 Mahadeva ka Aana

Yahan kabhi-kabhi
Shiva
bhi aate hain 🔱

Apni Parvati ji ke saath

Gano aur bhuto ke saath

Yeh dikhata hai ki
sachchi mitrata
dhan se bhi upar hoti hai 🤍

🏔️ Parvat aur Ratn

Is Sabha mein:

Meru parvat

Kailasa, Vindhya, Mandara
sab apne manav roop mein aate hain 🏔️

Sankh aur Padma jaise
divya ratn bhi
Kuvera Dev ko pranam karte hain 💎

🌱 Chhoti si Seekh (Moral)

Dhan tab hi shubh hota hai
jab uske saath
vinamrata aur dharm ho 🙏

Samriddhi ka matlab
sirf sona nahi,
santulan aur seva bhi hai ⚖️

Jo dhan ko sahi maarg par rakhta hai,
wahi sachcha dhani hota hai 🌟

Narada ji bole:
“Yudhishthira,
yeh thi Kuvera Dev ki Sabha.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.7 – Section XI"):
            text1 = """ 
            Section XI – Brahma Ji ki Sabha (Srishti aur Gyaan ka Lok)
            Narada ji bole:

🌼 Suno, Yudhishthira

“O mere bachche,
ab main tumhe batata hoon
Brahma
ki Sabha ke baare mein.”

Yeh Sabha
aisi hai jiska poora varnan
koi shabdon mein
kabhi nahi kar sakta ✨"""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            ☀️ Surya Dev ka Varnan

Bahut pehle,
Krita Yuga mein,
Surya
dharti par aaye the 🌞

Unhone mujhe kaha:
“Brahma Ji ki Sabha
na naap mein bandhti hai,
na roop mein.”

Woh Sabha:

Roop badalti rehti hai

Har pal nayi lagti hai

Mann ko anand deti hai 💛

🙏 Narada Ji ki Tapasya

Yeh sun kar
mera mann hua
us Sabha ko dekhne ka 🌸

Surya Dev bole:
“Hazaar saal ka
Brahma-vrat karo.”

Main Himavat par gaya 🏔️
Aur gehri tapasya ki.

Tapasya poori hui to
Surya Dev mujhe
Brahma Ji ki Sabha le gaye ✨

🌈 Sabha ka Adbhut Swaroop

Yudhishthira,
woh Sabha:

Na thandi

Na garam

Na bhookh

Na pyaas

Jaise hi koi wahan jaata hai,
saari thakaan
aur dukh mit jaate hain 😌

Woh Sabha:

Ratnon se bani lagti hai

Koi khambhe nahi

Phir bhi hamesha khadi

Uski roshni
suraj, chand aur agni
sab se zyada tej hai 🔥

👑 Brahma Ji ka Aasan

Is Sabha ke beech:
Brahma Ji virajmaan rehte hain 👑

Wahi:

Srishti ke karta

Sabke pita

Sabke liye samaan daya rakhne wale 🤍

Unke paas:

Maharshi

Prajapati

Sab tatva

Prakriti aur Gun

sab saath baithte hain 🌍

📜 Gyaan ka Mahasagar

Yahan maujood hote hain:

Charo Veda 📖

Upanishad

Itihaas aur Puran

Mantra aur Shastra

Samay khud yahan aata hai ⏳
— din, raat, yug, kal sab ek saath.

🌺 Devi–Devta aur Shaktiyaan

Is Sabha mein:

Lakshmi

Saraswati

Ganga

Prithvi

sab apne manav roop mein
Brahma Ji ki seva karte hain 🌸

Yahan:

Prem

Kshama

Gyaan

Shaanti

sab ek saath rehte hain 🤲

🕊️ Sabhi Jeevon ka Samaan Sthan

Yahan:

Devta

Rishi

Yaksha

Gandharva

Manav

Pashu

Pakshi

sab ko barabar samman milta hai 🌍

Koi bada–chhota nahi.
Sab Brahma Ji ke bachche hain 💞

🌟 Narada Ji ka Antim Vachan

Narada ji bole:

“Yudhishthira,
jaise tumhari Sabha
manushya lok mein sabse shreshth hai,
waise hi
Brahma Ji ki Sabha
sab lokon mein sabse shreshth hai.”

🌱 Chhoti si Seekh (Moral)

Gyaan hi sabse bada dhan hai 📖

Jahan gyaan aur daya hoti hai,
wahan shanti hoti hai 🕊️

Sabhi jeev
ek hi srishti ka hissa hain 🌍"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.8 – Section XII"):
            text1 = """ 
            Section XII – Raja Harishchandra ka Rahasya (Hinglish Story Rewrite)
            Yudhishthira ne shaant mann se Narada se kaha:

“Gurudev,
aapne sab Devtaon ki Sabhas batayi.

Yama ki Sabha mein lagbhag sab raja hain.

Varuna ki Sabha mein Nag, Daitya, nadi aur samundar hain.

Kubera ki Sabha mein Yaksha, Gandharva, Rakshasa aur Apsara hain.

Brahma ki Sabha mein sab Rishi, Dev aur vidya hai.

Par Indra ki Sabha mein
aapne sirf ek hi raja ka naam liya—
Harishchandra.

Unhone aisa kya kiya
jo ve Indra ke samaan ban gaye?

Aur Gurudev,
aap mere pita Pandu se kaise mile?
Kya unhone mere liye koi sandesh diya?”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Narada ji bole (muskurate hue):

“Rajadhiraj Yudhishthira,
main sab bataata hoon.

Raja Harishchandra
bahut shaktishaali aur dharmic raja the.
Poore prithvi ke raja
unki aagya maante the.

Ve akela hi
sone se sajje rath par chadhkar
poori dharti ko jeet chuke the.

Jab sab rajya jeet liya,
to unhone Rajasuya Yagya karne ka nishchay kiya.

Is yagya ke liye
sab raja dhan lekar aaye.
Sab Brahmanon ko bhojan aur daan mila.

Par Harishchandra ne
sirf utna hi daan nahi diya
jitna maanga gaya.

👉 Unhone 5 guna zyada daan diya.

Brahman bahut prasann hue.
Ve bole:
‘Yeh raja sabse mahaan hai.’

Isi daan, satya aur dharma ke kaaran
Harishchandra
Indra Lok pahunch gaye
aur Indra ke saath
anand se rehne lage.”

Narada ji aage bole:

“Yudhishthira,
jo raja Rajasuya Yagya karta hai,
use Indra Lok milta hai.

Jo raja
yuddh mein peeth na dikha kar
veer gati paata hai,
wo bhi Indra Lok jaata hai.

Aur jo tapasya karke
shareer tyagta hai,
wo bhi wahi pahunchta hai.”

Pandu ka Sandesh 🌿

“Tumhare pita Pandu,
Harishchandra ka saubhagya dekh kar bole:

‘Mera beta Yudhishthira
apne bhaiyon ke saath
poori dharti jeet sakta hai.

Agar wo Rajasuya Yagya kare,
to main bhi
Harishchandra ki tarah
Indra Lok pahunch sakta hoon.’

Maine unse vaada kiya
ki main yeh sandesh
tum tak pahunchaaunga.”

Ek Mahatvapurn Chetavani ⚠️

Narada ji ne gambhir swar mein kaha:

“Par raja,
Rajasuya Yagya aasaan nahi hota.

Brahma Rakshas ise bigaadne ki koshish karte hain.

Yagya ke samay yuddh ho sakta hai.

Thodi si galti
poori dharti ko sankat mein daal sakti hai.

Isliye:

Satark rehna

Chaar varnon ki raksha karna

Brahmanon ko daan dena
bahut zaroori hai.”

Ant 🌸

Narada ji bole:
“Main tumhare sab prashnon ka uttar de chuka hoon.
Ab mujhe Dwaravati jaana hai.”

Itna kehkar
Narada ji rishiyon ke saath chale gaye.

Narada ji ke jaane ke baad,
Yudhishthira apne bhaiyon ke saath
Rajasuya Yagya par
gehra vichaar karne lage.

🌼 Moral / Seekh

Satya + Daan + Dharma = Devtaon jaisa maan

Raja Harishchandra ne sikhaya
ki bina laalach ke diya gaya daan
insaan ko amar bana deta hai.

Bade kaam se pehle
soch, sanyam aur zimmedari zaroori hoti hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.2.9 – Section XIII"):
            text1 = """ 
            Section XIII – Rajasuya ka Sankalp
            Vaisampayana bole:

Narada ji ke shabdon ko sun kar
Yudhishthira ne gehri saans li.
Unka mann shaant nahi tha.

Rajasuya yagya ka vichaar
unke hriday ko baar-baar gher raha tha.

Unhone socha:
“Purane mahaan rajaon ne yagya karke
svarg aur anand ke lok paaye.
Harishchandra ne bhi Rajasuya karke
Indra Lok paaya.”

Yeh soch kar
Yudhishthira ne Rajasuya yagya ki taiyaari ka
mann bana liya."""
            create_image_text_layout(
                "attached_assets/chapter2/2.2.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Raja ka Dharma-bhaav 🌿

Par Yudhishthira sirf apni mahima ke baare mein nahi sochte the.
Ve hamesha yeh sochte the:

“Mere is faisle se
mere praja ka bhala hoga ya nahi?”

Ve krodh aur ahankar se door rehte the.
Unka ek hi siddhant tha:

“Har vyakti ko uska adhikaar do.”

Isliye praja ke muh se
sirf ek hi awaaz aati thi:

“Dharma ki jai!
Yudhishthira ki jai!”

Isi kaaran
unhe Ajātaśatru kaha gaya —
jis ka koi shatru na ho.

Pandavon ka Rajya 🤍

Bhima sab par nyay se raj karte the.

Arjuna desh ko baahri shatruon se bachate the.

Sahadeva bina pakshpaat ke nyay dete the.

Nakula sabse vinamr vyavhaar karte the.

Isliye:

rajya mein koi bhay nahi tha

koi jhagda nahi tha

praja apne kaam mein santusht thi

barish samay par hoti thi

kheti, vyapar, pashupalan sab phal-phool rahe the

Na chori ka dar,
na rog ka,
na zehar ya tantra ka.

Log Yudhishthira ko
apne maa-baap se bhi zyada prem karte the.

Mantriyon ki Salah 🏛️

Yudhishthira ne apne bhaiyon aur mantriyon ko bulaya
aur Rajasuya par vichaar kiya.

Sab ne ek swar mein kaha:

“Rajasuya yagya wahi karta hai
jo samrat banne ke yogya ho.

Aapke paas:

rajya hai

shakti hai

dharma hai

Isliye abhi hi sahi samay hai.”

Mantriyon ne kaha:
“Is yagya ke baad
sab yagyon ka phal milta hai.
Aap iske poorn yogya hain.”

Yudhishthira ne yeh baat mann mein rakhi,
par turant faisla nahi liya.

Antim Soch – Krishna ko Bulana 🌸

Yudhishthira ne socha:

“Budhimaan wahi hai
jo bina poori soch ke kaam na kare.”

Isliye unhone faisla kiya:
👉 Krishna se poochna sabse uchit hoga.

Krishna:

sab jaante hain

sab sambhav kar sakte hain

ichchha se manushya roop mein aaye hain

Yudhishthira ne unhe sandesh bheja.

Krishna ka Aagman 🌼

Sandesh milte hi
Krishna ne turant prasthaan kiya.

Dwaraka se
tezi se aate hue
ve Indraprastha pahunch gaye.

Yudhishthira ne
Krishna ka pita-samaan prem se swaagat kiya.
Bhima ne bhi gale lagaya.

Krishna ne Kunti ko pranam kiya.
Twins ne unka samman kiya.
Arjuna unse milkar anandit ho utha.

Aaram ke baad
Yudhishthira ne
Rajasuya ki baat rakhi.

Yudhishthira ka Nivedan 🙏

Yudhishthira bole:

“Main Rajasuya yagya karna chahta hoon.
Par sirf iccha se yagya nahi hota.

Aap sab jaante hain, Krishna,
kaise yeh sambhav ho sakta hai.

Mantri kabhi mitrata mein
mushkilein nahi dekhte.
Kabhi swarth mein sirf acchi baat kehte hain.

Par aap:

kaamna se pare hain

krodh se pare hain

Isliye
jo sabke liye sabse uttam ho,
wahi mujhe bataiye.”

🌼 Seekh (Moral)

Sacha raja apni mahima se pehle
praja ka bhala sochta hai

Bade nirnay ke liye
gyaan aur vivek zaroori hai

Krishna jaise margdarshak
dharma ke liye anivarya hote hain"""
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

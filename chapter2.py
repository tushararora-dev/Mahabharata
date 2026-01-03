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
            text1 = """ 
            Krishna ne shaant awaaz mein kaha—

“Hey Maharaj, tum Rajasuya Yagya ke liye poori tarah yogya ho.
Tum sab kuch jaante ho.
Phir bhi, main ek baat bataana chahta hoon.”

“Pehle ke Kshatriya bahut mahaan the.
Par aaj ke Kshatriya un jaise nahi rahe.
Purane veeron ki shakti aur maryada ab kam ho chuki hai.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Krishna ne aage kaha—

“Bahut se raja apne aap ko bade vanshon ka vanshaj bolte hain.
Par asli shakti sirf naam se nahi hoti.
Sachchi shakti dharm aur sahas se aati hai.”

“Is samay ek raja hai—Jarasandha.
Uski shakti bahut zyada hai.
Usne kai rajao ko dara kar apne adheen kar liya hai.”

“Kaafi veer raja, darr ke kaaran, apne rajya chhod kar bhaag gaye.
Kuch pahadon ki taraf chale gaye.
Kuch door deshon mein sharan lene lage.”

Krishna thoda ruk kar bole—

“Hum Yadavo ne bhi ye sab saha.
Humein Mathura chhodni padi.
Hum apni suraksha ke liye Dwaraka chale gaye.”

“Humne Dwaraka ko itna majboot banaya
ki dushman wahan pahunch bhi nahi sakta.
Ab hum wahan bina darr ke rehte hain.”

Phir Krishna ne gambhir swar mein kaha—

“Hey Rajan, sach ye hai
jab tak Jarasandha zinda hai,
Rajasuya Yagya poora nahi ho sakta.”

“Usne kai nirdosh rajao ko bandi bana rakha hai.
Jaise sher gufa mein haathi ko bandh leta hai,
waise hi usne rajao ko qaid kiya hai.”

Krishna ne prem se samjhaya—

“Agar tum Rajasuya karna chahte ho,
to pehle bandi rajao ko mukt karna hoga.
Aur Jarasandha ke anyay ka ant karna hoga.”

Ant mein Krishna bole—

“Hey dharmic raja,
ab faisla tumhare haath mein hai.
Socho, samjho, aur jo tumhe sahi lage, wahi karo.”

Moral:
Sachcha samrat wahi hota hai
jo shakti se pehle dharma,
aur apne sukh se pehle dusron ki mukti ko chunta hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.2 – Section XV"):
            text1 = """ 
            Yudhishthira ne shaant aur vinamr awaaz mein kaha—

“Krishna, tum bahut gyaani ho.
Jo baat tumne kahi,
wo koi aur keh hi nahi sakta.”

“Duniya mein bahut se raja hain.
Sab apna-apna faayda dekhte hain.
Par sachcha samrat banna bahut mushkil hota hai.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            “Jo dusron ki shakti jaanta hai,
wo kabhi apni tareef nahi karta.
Aur jo yuddh mein bhi maryada rakhe,
wahi sach mein poojne yogya hota hai.”

Yudhishthira thoda soch kar bole—

“Insaan ki ichchhayein bahut hoti hain.
Par mukti aur shanti
sirf unchi soch aur dharm se milti hai.”

“Mere liye sabse badi cheez
mann ki shanti hai.
Agar main Rajasuya karun,
shayad mujhe wo shanti na mile.”

Phir unhone dheere se kaha—

“Hum sab Jarasandha se darte hain.
Uska anyay bahut bhayanak hai.”

“Krishna, jab tum jaise veer bhi
uski shakti ko gambhir maante ho,
to main khud ko kaise mahaan samjhun?”

“Mujhe baar-baar ye soch pareshaan karti hai—
kya Jarasandha ko
tum, Balram, Bhima ya Arjuna
hara paayenge?”

“Krishna, is baat par
tum hi meri aakhri aashray ho.”

Yeh sun kar Bhima aage aaye aur bole—

“Jo bina taiyaari ke
taakatwar shatru se ladta hai,
wo mitti ke dhele ki tarah toot jaata hai.”

“Par buddhi aur yojna se
kamzor bhi jeet sakta hai.”

“Krishna ke paas neeti hai.
Mere paas shakti hai.
Aur Arjuna ke paas vijay.”

“Jaise teen yagya-agni milkar
yagya poora karti hain,
waise hi hum milkar
Jarasandha ka ant karenge.”

Tab Krishna ne sabko samjhaya—

“Jo bina bhavishya soche
sirf apni ichchha dekhta hai,
wo galti karta hai.”

“Purane yug mein
bahut se raja samrat bane.
Kisi ne daya se,
kisi ne shakti se,
kisi ne tapasya se.”

“Par Yudhishthira,
tum sabhi gunon se yukt ho—
jeet, daya, dharm, samriddhi aur neeti.”

“Jarasandha bhi bahut shaktishaali hai.
Usne lagbhag sau rajao ko
apne adheen kar liya hai.”

“Par wo bachpan se hi kroor hai.
Aur uski lalach kabhi poori nahi hoti.”

Krishna ne gambhir swar mein kaha—

“Usne kai rajao ko
bandi bana kar
Shiv mandir mein qaid kar rakha hai.”

“Yuddh mein marna
ek Kshatriya ke liye
samman ki baat hoti hai.”

“Toh phir hum kyun na
Jarasandha ka saamna karein?”

“Usne ab tak chhiyaasi raja pakad liye hain.
Bas chaudah aur chahiye.”

“Jo uska raasta roke,
uska naam amar hoga.”

“Aur jo Jarasandha ko hara de,
wahi sachcha samrat kehlaayega.”

Moral:
Sachchi shakti akeli nahi hoti.
Buddhi, sahas aur dharm
jab saath aate hain,
tab anyay ka ant hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.3 – Section XVI"):
            text1 = """ 
            Yudhishthira ne udaas mann se kaha—

“Krishna,
agar main sirf rajya ki ichchha se
aur sirf himmat par bharosa karke
tumhe Jarasandha ke paas bhej doon,
to kya ye sahi hoga?”

“Bhima aur Arjuna
meri aankhon jaise hain.
Aur tum, Janardana,
mera mann ho.”

“Main aankhon aur mann ke bina
kaise jee paunga?”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            “Jarasandha ki sena bahut bhayanak hai.
Uski shakti ko toh Yama bhi
aasaani se nahi hara sakte.”

“Phir tum teen
uske saamne kaise tik paoge?”

Yudhishthira ka swar bhaari ho gaya—

“Mujhe darr lag raha hai.
Ye kaam galat bhi ho sakta hai.
Isse bada nuksaan ho sakta hai.”

“Mujhe lagta hai
Rajasuya Yagya abhi
bahut kathin hai.”

Tab Arjuna aage aaye.
Unki awaaz mein vishwas tha—

“Maharaj,
mujhe divya dhanush mila hai.
Akshay baan mile hain.
Shakti, saathi aur yash bhi mila hai.”

“Ye sab cheezein
aasaani se nahi milti.”

“Log vansh ki tareef karte hain.
Par sabse badi cheez hoti hai—
veerata.”

“Jo veer nahi,
chahe bade vansh mein janma ho,
wo adhura hota hai.”

“Par jo veer hai,
chahe chhote vansh ka ho,
wo mahaan hota hai.”

Arjuna ne shaant par dridh swar mein kaha—

“Sachcha Kshatriya wahi hai
jo apni veerata se
apna yash badhata hai.”

“Veerata ke bina
baaki sab gun bekaar ho jaate hain.”

“Jeet ke teen stambh hote hain—
dhyaan, parishram aur bhagya.”

“Par bina savdhaani ke
sirf shakti bhi kaam nahi aati.”

“Isliye humein
na kamzori chahiye,
na ghamand.”

Arjuna ne Yudhishthira ki taraf dekha—

“Agar hum Jarasandha ko hara kar
bandi rajao ko mukt karte hain,
to isse bada dharm ka kaam
koi nahi ho sakta.”

“Aur agar hum darr ke kaaran
peeche hat gaye,
to duniya humein
kamzor samjhegi.”

Unhone vishwas se kaha—

“Hum kamzor nahi hain, Maharaj.”

“Jaise sanyasi shaanti ke liye
peele vastra pa lete hain,
waise hi vijay ke baad
samrajya apne aap mil jaayega.”

“Isliye hum yuddh karenge.
Dharma ke liye.
Nyay ke liye.”

Moral:
Sirf darr se rukna bhi galat hai,
aur sirf ghamand se aage badhna bhi.
Himmat + soch + dharma
jab saath ho,
tab hi sahi faisla hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.4 – Section XVII"):
            text1 = """ 
            Vasudeva (Krishna) ne shaant par dridh awaaz mein kaha—

“Arjuna ne wahi soch batayi
jo Bharata vansh mein janme veer ki hoti hai.
Humein nahi pata
maut raat ko aayegi ya din mein.”

“Ladai se bhaag kar
kabhi amar nahi hua jaata.
Isliye dharm ke saath
dushman ka saamna karna
ek Kshatriya ka kartavya hai.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            “Jab sahi neeti saath ho
aur bhagya rukawat na bane,
to kaam safal hota hi hai.”

“Do paksh ladte hain
to dono jeet nahi sakte.
Koi ek hi jeetega.”

Krishna ne samjhaya—

“Bina neeti ke yuddh
vinaash laata hai.
Aur jab shakti barabar ho,
to parinaam anishchit hota hai.”

“Toh phir,
hum sahi yojna ke saath
Jarasandha ka saamna kyun na karein?”

“Jaise tez dhara
ped ko ukhaad deti hai,
waise hi hum use gira sakte hain.”

Krishna ne gambhir hote hue kaha—

“Bahut shaktishaali shatru se
seedha yuddh zaroori nahi.
Buddhimaan log
chalaki aur samay ka
sahi upyog karte hain.”

“Agar chhupkar uske ghar jaakar
us par prahaar karein,
to koi apmaan bhi nahi hoga.”

“Jarasandha
abhi ghamand mein jee raha hai.
Par mujhe uska ant nazar aa raha hai.”

“Apne logon ki raksha ke liye
ya to hum use maarenge,
ya phir veerta ke saath
swarg ko praapt honge.”

Yudhishthira ne poocha—

“Krishna,
ye Jarasandha kaun hai?
Usmein aisi kaunsi shakti hai
ki tumhe chhoone par bhi
jal nahi gaya?”

Krishna muskuraye aur bole—

“Sunno, main tumhe
Jarasandha ki kahani batata hoon.”

“Bahut pehle
Magadh ka raja tha—
Vrihadratha.
Bahut shaktishaali,
Indra jaisa tej.”

“Uski do raniyaan thi,
dono sundar aur pyaari.
Raja dono se barabar prem karta tha.”

“Par saalon tak
unhe koi santaan nahi hui.
Raja bahut udaas rehta tha.”

Ek din—

“Ek mahaan rishi
Chandakaushik
wahan aaye.
Raja ne unka
poora aadar-samman kiya.”

Rishi bole—

“Raja,
koi vardaan maango.”

Raja ne aansuon ke saath kaha—

“Mujhe putra chahiye.
Bina putra ke
raajya ka kya arth?”

Rishi dhyaan mein baithe.
Tab ek aam unke paas gira.

Unhone mantra padhe
aur raja ko aam de diya—

“Isse tumhara sapna poora hoga.
Wapas jao.”

Raja ne aam
dono raniyon mein baant diya.
Dono ne kha liya
aur kuch samay baad
dono garbhvati ho gayin.

Par jab bachche paida hue,
to dono adhoore the.
Raniyan darr gayin.
Un tukdon ko chhod diya gaya.

Raat ko ek Rakshasi
Jara wahan aayi.
Usne dono tukdon ko joda.

Aur achanak—
ek poora, majboot bachcha
zinda ho gaya.

Bachche ki awaaz itni tez thi
ki mahal goonj utha.

Raja aur raniyan bhaag kar aaye.
Jara ne daya dikhayi
aur bachcha unhe de diya.

“Ye tumhara putra hai,”
usne kaha.

Krishna ne ant mein kaha—

“Isi Jara ke naam par
uska naam pada—
Jarasandha.”

Moral:
Zindagi mein kabhi-kabhi
sabse bade veer bhi
ajnabi kahaniyon se janm lete hain.
Par shakti bina dharm ke
aakhirkaar ghamand ban jaati hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.5 – Section XVIII"):
            text1 = """ 
            Krishna ne kahani aage badhayi—

Raja ki baat sun kar
Rakshasi stree ne namrata se kaha—

“Rajao ke raja,
tum sada sukhi raho.”

“Main Jara hoon.
Main roop badal sakti hoon.
Main tumhare ghar mein
Grihadevi ke roop mein rehti hoon.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            “Main roz logon ke ghar jaati hoon.
Bhagwan ne mujhe
Danavo ke vinash ke liye banaya tha.”

“Jo mere chitra ko
apne ghar ki deewaar par
bachchon ke beech dikhata hai,
uske ghar mein
sukh aur samriddhi rehti hai.”

“Tumhare mahal ki deewaar par bhi
mera chitra bana hai.
Main roz wahan
phool, dhoop aur bhojan se pooji jaati hoon.”

“Isliye main hamesha sochti hoon
ki tumhara bhala kaise karun.”

Jara ne pyaar se kaha—

“Jab maine tumhare putra ke
alag-alag tukde dekhe,
to unhe jod diya.”

“Tumhare achhe bhagya se
ek jeevit aur majboot shishu bana.”

“Main sirf ek madhyam thi.
Asli kripa tumhare punya ki thi.”

“Tumhari bhakti se prasann hokar
maine ye putra tumhe diya.”

Itna keh kar
Jara wahin gaayab ho gayi.

Krishna ne aage kaha—

Raja apne putra ko lekar
khushi-khushi mahal gaye.
Bachche ke sab sanskar kiye gaye.
Poore rajya mein
utsav manaya gaya.

Raja ne kaha—

“Ye shishu Jara ke dwara
joda gaya hai.
Isliye iska naam hoga—
Jarasandha.”

Wo bachcha
din-pratidin majboot hota gaya.
Jaise aag mein ghee dalne se
aag aur tez ho jaati hai.

Chaand jaise
shukla paksh mein badhta hai,
waise hi wo shishu
maa-baap ka aanand badhata gaya.

Moral:
Kabhi-kabhi
jeevan ke sabse shaktishaali log
bhagya aur bhakti se janm lete hain.
Par shakti ka sahi upyog hi
insaan ko mahaan banata hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.3.6 – Section XIX"):
            text1 = """ 
            Krishna ne kahani aage sunayi—

Kuch samay baad
mahaan rishi Chandakaushik
phir se Magadh aaye.

Raja Vrihadratha
bahut khush hue.
Woh apne mantri, purohit,
raniyon aur putra ke saath
rishi ka swagat karne gaye."""
            create_image_text_layout(
                "attached_assets/chapter2/2.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Raja ne
charan dhoye,
arghya diya,
aur vinamrata se kaha—

“Rishi ji,
main apna poora rajya
aur apna putra
aapko samarpit karta hoon.”

Rishi muskuraye.
Unhone shaant mann se kaha—

“Raja,
mujhe sab pehle se pata tha.
Ab suno,
tumhara putra aage jaakar
kya banega.”

“Ye putra
bahut shaktishaali hoga.
Iski veerata
sab rajao se aage hogi.”

“Jaise Garuda ki gati
koi pakshi nahi pa sakta,
waise hi
koi raja
is putra ki shakti ke barabar
nahi hoga.”

“Is par pheke gaye
astra-shastra bhi
ise haani nahi pahuncha paayenge.”

“Ye sab rajao ke sir par
tej ki tarah chamkega.”

“Jaise suraj
sab roshniyon ko dhundhla kar deta hai,
waise hi
ye putra
sab rajao ki shaan
kam kar dega.”

“Bade-bade raja bhi
iske saamne
aag mein pade keede jaise
mit jaayenge.”

“Ye sab rajao ki samriddhi
samundar ki tarah
apne mein sama lega.”

“Ye prithvi ki tarah
sab varnon ka
bojh sambhalega.”

“Sab raja
iske aadesh maanenge,
jaise prani
hava par nirbhar rehte hain.”

“Ye Magadh ka rajkumar
bhagwan Rudra (Shiva)
ko bhi apni aankhon se dekhega.”

Itna keh kar
rishi apne maarg par chal diye.

Raja Vrihadratha
rajya laut aaye.
Sab ko bulaya
aur apne putra
Jarasandha
ko raja ghoshit kar diya.

Iske baad
Vrihadratha ka mann
rajya se uth gaya.
Woh apni raniyon ke saath
van mein tapasya karne chale gaye.

Kuch samay baad
tap aur dhyaan ke baad
woh swarg chale gaye.

Jarasandha ne
apne pita ke baad
rajya sambhala.
Usne rajya ko
pitaji ki tarah
shasan kiya.

Baad mein
jab Kansa
Krishna ke dwara maara gaya,
to Jarasandha ka
Krishna se bair ho gaya.

Gusse mein
Jarasandha ne
apni gada ko
99 baar ghuma kar
Mathura ki taraf phenka.

Gada
Mathura ke paas
giri.
Is jagah ka naam pada—
Gadavasan.

Mathura ke log
Krishna ke paas gaye
aur sab bataya.

Jarasandha ke do mitra the—
Hansa aur Dimvaka.
Dono itne shaktishaali the
ki astra-shastra
unhe nahi maar sakte the.

Neeti aur buddhi mein bhi
woh sabse aage the.

Isi shakti ke kaaran
Kukkura, Andhaka aur Vrishni vansh
seedha yuddh karne se
ruk gaye.

Unhone samjha—
“Har ladai
talwar se nahi jeeti jaati.
Kabhi-kabhi
buddhi hi sabse badi shakti hoti hai.”

Moral:
Bahut zyada shakti
agar ghamand ban jaaye,
to duniya mein darr failta hai.
Par buddhi aur dharm
hamesha
sahi raasta dikhate hain 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.4 – Jarasandha-badha Parva (Slaying of Jarasandha)"):

        with st.expander("Section 2.4.1 – Section XX"):
            text1 = """ 
            Krishna ne shaant par dridh awaaz mein kaha—

“Ab samay aa gaya hai.
Hansa aur Dimvaka gir chuke hain.
Kansa bhi apni sena ke saath nasht ho chuka hai.”

“Ab Jarasandha ka ant zaroori hai.
Yuddh mein use koi hara nahi paaya.
Par hum use vyaktigat muqable mein hara sakte hain.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Krishna muskuraye—

“Mere paas neeti hai.
Bhima ke paas bal hai.
Aur Arjuna ke paas vijay hai.”

“Hum teen chupke se Magadha jayenge.
Jarasandha apne ghamand se
Bhima ko hi chunega.”

“Bhima,
apni bhujon se
use gira dega.
Jaise mrityu
ghamand ko gira deti hai.”

Krishna ne Yudhishthira ki taraf dekha—

“Agar tumhe mujh par vishwas hai,
to Bhima aur Arjuna
mujhe saunp do.”

Yeh sunkar Yudhishthira bole—

“Achyuta,
tum hi hamare margdarshak ho.”

“Tumhare kehne par
mujhe lagta hai
jaise Jarasandha pehle hi mar chuka ho.
Jaise bandi raja mukt ho chuke hon.
Jaise Rajasuya poora ho chuka ho.”

“Krishna ke bina
main jee nahi sakta.
Jaise rog se peedit vyakti
bal ke bina reh jaata hai.”

“Krishna aur Arjuna saath hon
to kuch bhi asambhav nahi.
Aur Bhima saath ho
to shakti aur badh jaati hai.”

Yudhishthira ne samjhaya—

“Bina neta ke sena
bejaan hoti hai.
Sahi netritva
raasta dikhata hai.”

“Isliye hum
Govinda ke netritva mein
aage badhenge.”

“Pehle Krishna.
Phir Arjuna.
Aur phir Bhima.”

“Neeti + bhagya + bal
milkar vijay laate hain.”

Vaisampayana ne kaha—

Phir Krishna, Arjuna aur Bhima
Snataka Brahmanon ka vesh pehen kar
Magadha ki taraf nikal pade.

Log unhe dekh kar bole—

“Jarasandha ka ant
ab nischit hai.”

Teeno veer
pahadon, nadiyon aur vanon se guzre.
Ganga aur Sone ko paar kiya.
Aur aakhir
Magadha ki seema mein pahunche.

Unhone
Goratha parvat ke paas
Magadha nagari dekhi—
dhann, jal aur hariyali se bhari hui.

Teeno ke chehre par
shanti thi.
Par mann mein
nyay ka sankalp jal raha tha.

Moral (Soft Message):

Jab buddhi, shakti aur sahas
ek saath chalte hain,
to sabse bada ghamand bhi
jhuk jaata hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.2 – Section XXI"):
            text1 = """ 
            Krishna ne dheere se kaha—

“Partha,
yeh dekho Magadha ki sundar nagari.
Gaiyon, paani aur dhan se bhari hui.
Yahan kisi cheez ki kami nahi.”

Shehar ke aas-paas
paanch bade pahad the—
Vaihara, Varaha, Vrishava, Rishigiri
aur pyara sa Caitya Parvat.
Jaise yeh pahad
milkar shehar ki raksha kar rahe ho."""
            create_image_text_layout(
                "attached_assets/chapter2/2.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Thandi chhaaya dene wale ped,
phoolon se bhari daaliyan,
aur sugandhit van—
sab kuch shant aur sundar lag raha tha.

Krishna bole—
“Isi shakti aur suraksha ke bharose
Jarasandha
apne ghamand mein rehta hai.
Par aaj hum uska ghamand tod denge.”

Phir Krishna, Bhima aur Arjuna
Brahmanon ka vesh pehen kar
Magadha nagar mein pravesh kar gaye.

Shehar khushhaal tha.
Bazaaron mein phool, mithai,
aur rang-birangi cheezein thi.

Log haste-muskurate the.
Par teeno veer
apna lakshya nahi bhool rahe the.

Unhone phoolon ki mala uthayi,
rang-birange vastra pehne,
aur dheere-dheere
Jarasandha ke mahal ki taraf badhe.

Unke majboot haath
chandan se lage hue the.
Log unhe dekh kar hairaan the—
“Yeh kaun Brahman hain
jo haathi jaise balwaan lag rahe hain?”

Jab Jarasandha ne unhe dekha,
toh woh turant khada ho gaya.
Usne samman se paani, madhu
aur arghya arpit kiya.

“Swagat hai,”
raja ne kaha.

Bhima aur Arjuna chup rahe.
Tab Krishna bole—

“Rajan,
yeh dono Snataka vrat mein hain.
Aadhi raat tak
yeh maun rahenge.”

Jarasandha ne unhe
yagya-sthal mein thehra diya.

Aadhi raat ko
Jarasandha khud aaya.
Usne unhe dhyaan se dekha
aur kaha—

“Snataka Brahman
is tarah phool aur chandan se sajte nahi.
Tumhare haath par
dhanush ki rassi ke nishaan kyun hain?”

“Sach batao—
tum kaun ho?
Aur galat dwar se
shehar mein kyun aaye?”

Tab Krishna shaant awaaz mein bole—

“O rajan,
Snataka vrat
Brahman, Kshatriya aur Vaishya
sab rakh sakte hain.”

“Kshatriya
bol se nahi,
bal se apni shakti dikhate hain.”

“Shastra ka niyam hai—
dushman ke ghar
galat dwar se pravesh karo.”

“Aur jab hum
dushman ke ghar aate hain,
toh uska samman
sweekaar nahi karte.”

Krishna ki baaton mein
shaanti bhi thi
aur sankalp bhi.

Jarasandha chup ho gaya.
Woh samajh gaya—
yeh saadharan Brahman
nahi hain.

Moral (Soft Message):

Sach aur dhairya se boli gayi baat
sabse bade ghamand ko bhi
sochne par majboor kar deti hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.3 – Section XXII"):
            text1 = """ 
            Jarasandha ne shaant par garv bhari awaaz mein kaha—

“Main yaad karke bhi
yeh nahi paata
ki maine tumhara kya bigaada.
Jab maine tumhe nuksaan hi nahi diya,
to tum mujhe dushman kyun maan rahe ho?”

“Ek sacha Kshatriya
kabhi nirdosh ko nuksaan nahi pahunchata.
Jo nirdosh ki khushi aur dharma todta hai,
woh ant mein apni hi unnati kho deta hai.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Tab Krishna ne gambhir par shaant swar mein kaha—

“O rajan,
tum apne aap ko nirdosh keh rahe ho,
par sach yeh hai
ki tumne kai rajaon ko
bandi bana rakha hai.”

“Tum unhe
bhagwan Rudra ke naam par
bali dena chahte ho.
Insaanon ki bali
kabhi dharm nahi hoti.”

“Jo raja
dusre rajaon ko
pashu samajhne lage,
woh bhatak chuka hota hai.”

“Har vyakti
apne karm ka phal paata hai.
Isliye hum
bandi rajaon ko mukt karne
aur anyay rokne aaye hain.”

Krishna aage bole—

“Tum sochte ho
ki tumse bada veer koi nahi.
Yeh ghamand hai, rajan.”

“Bahut se veer
chup hote hain,
par kamzor nahi.”

“Kshatriya ke liye
yuddh sirf hinsa nahi,
kartavya hota hai.
Aur dharm ke liye
yuddh mein veer-gati
swarg ka nishchit maarg hota hai.”

“Isliye
apna ghamand chhodo.
Apni sena, putron aur mantriyon ko
anarth ki taraf mat le jao.”

“Hum Brahman nahi hain.
Main Sauri (Krishna) hoon.
Aur yeh dono
Bhima
aur Arjuna
Pandav hain.”

“Ab faisla tumhara hai—
ya to bandi rajaon ko chhod do,
ya phir yuddh ke liye
samne aao.”

Jarasandha ne garaj kar kaha—

“Main kisi raja ko
bina haraye bandi nahi banata.
Yahi Kshatriya ka dharm hai.”

“Sena se sena,
ya ek se teen—
main har tarah ke yuddh ke liye
taiyaar hoon!”

Usne turant
apne putra Sahadeva ko
rajya par bithaya.

Phir usne
apne purane veer saathi
Hansa aur Dimvaka
(jo ab Kausika aur Chitrasena ke naam se jaane jaate the)
ko yaad kiya.

Par Krishna ne mann hi mann
Brahma ka niyam yaad rakha—
Jarasandha ka ant
Krishna ke haath se nahi,
balki Bhima ke haath se hona tha.

Isliye Krishna
khud yuddh ke liye aage nahi badhe.

Moral (Soft Message):

Ghamand aankhon ko andha kar deta hai.
Aur anyaay ko dharm samajhna
sabse bada bhool hoti hai.
Sachcha bal
hamesha dharm aur vinamrata ke saath hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.4 – Section XXIII"):
            text1 = """ 
            Vaisampayana ne kaha—

Tab Krishna ne shaant awaaz mein
Jarasandha se poocha—

“O rajan,
hum teen mein se
tum kis se yuddh karna chahte ho?”

Jarasandha ne bina soche kaha—
“Main Bhima se yuddh karunga.
Shreshth veer se haarna
apmaan nahi hota.”

Yeh kehkar
Jarasandha ne apna mukut utaara.
Baalo ko baandha.
Aur samundar jaise
garajta hua khada ho gaya.

Bhima bhi
poori taiyaari ke saath
aage badhe.
Krishna ne devtaon ko smaran kiya
aur Bhima ko aashirvaad diya."""
            create_image_text_layout(
                "attached_assets/chapter2/2.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Ab dono veer
sirf apni bhujon ke sahare
ek-dusre par toot pade.

Kabhi baahon ko pakadte,
kabhi pairon ko lapet lete.
Kabhi kandhe se kandha
to kabhi maatha se maatha takra jaata.

Unke vaar se
chingaariyaan nikalti.
Zameen kaanp jaati.

Woh dono
jaise do matwale haathi
ya do gusse bhare sher
aapas mein takra rahe ho.

Kabhi Bhima
Jarasandha ko door pheinkta.
Kabhi Jarasandha
Bhima ko ghaseet leta.

Dono mahaan pehelwan
ek-dusre ko giraane,
dabane aur palatne ke
sab daav laga rahe the.

Shehar ke log—
Brahman, Kshatriya, Vaishya,
striyaan aur buzurg—
sab yeh drishya dekhne aa gaye.

Taaliyon, shor
aur bhujon ki thap-thap
se aakash goonj utha.

Yeh yuddh
ek din ka nahi tha.
Din-raat chalta raha.
Bina ruke.
Bina bhojan ke.

Kartika maas ke
pehle din se
terahvi raat tak
yeh sangharsh chalta raha.

Chaudahvi raat
Jarasandha thak gaya.

Tab Krishna ne Bhima se kaha—

“Bhima,
thake hue shatru par
poora zor lagana
uchit nahi hota.”

“Uske bal ke barabar hi
apna bal lagao.”

Bhima samajh gaye.
Unhone Jarasandha ki
sthiti pehchaan li.

Ab unhone
poori himmat
aur buddhi ke saath
antim nirnay lene ka
sankalp kiya.

Moral (Soft Message):

Sachcha veer
sirf shakti se nahi,
sanyam aur samajh se jeetta hai.
Aur jab bal ke saath
buddhi ho,
toh adbhut parinaam nikalta hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.4.5 – Section XXIV"):
            text1 = """ 
            Vaisampayana ne kaha—

Bhima ne dridh awaaz mein kaha—
“Krishna, jo anyaay karta rahe
aur abhi bhi yuddh par ada ho,
use chhodna theek nahi.”

Krishna ne pyaar se himmat badhayi—
“Bhima, aaj apni poori shakti dikhao.
Tumhe yeh bal
pavan-dev Marut se mila hai.”

Bhima ne Jarasandha ko
uthaya,
aasmaan ki taraf ghumaya,
aur apne ghutne se
uska ghamand tod diya.
Jarasandha ka ant ho gaya.

Bhima ki garaj
poore shehar mein goonj uthi.
Log bhay se chup ho gaye.
Par anyaay ka yug
wahin samaapt ho gaya."""
            create_image_text_layout(
                "attached_assets/chapter2/2.4.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Phir Krishna ne
bandi rajaon ko mukt kiya.
Sab raja khushi se
Krishna ko pranam karne lage.
Unhone kaha—
“Aapne humein
dukh ke gaddhe se nikaal liya.”

Krishna ne unse kaha—
“Yudhishthira
Rajasuya yagya karna chahte hain.
Aap sab unka saath dena.”

Sab rajaon ne
khushi se sweekaar kiya—
“Avashya!”

Jarasandha ke putra Sahadeva
bhay aur vinamrata ke saath aage aaye.
Krishna ne use aashwasan diya
aur Magadha ka raja bana diya.

Phir Krishna, Bhima aur Arjuna
Indraprastha laut aaye.
Yudhishthira ne
Krishna ka samman kiya
aur Bhima–Arjuna ko gale lagaya.

Shehar mein
khushi ka mahaul tha.
Sab raja apne-apne desh
shaanti ke saath laut gaye.

Ant mein Krishna
Dvarka ke liye prasthaan hue.
Pandavon ne unka
adar aur krtagyata se
parikrama ki.

Moral (Soft Message):

Jab shakti, buddhi aur dharm
ek saath chaltein hain,
to anyaay ka ant
aur shaanti ka aarambh hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")
    
    with st.expander("Chapter 2.5 – Digvijaya Parva (The Universal Conquest)"):

        with st.expander("Section 2.5.1 – Section XXV"):
            text1 = """ 
            Section XXV – Pandavon ka Digvijay (Hinglish Kahani)

Arjun ne jab
divya dhanush,
kabhi na khatam hone wale quiver,
special rath aur dhwaj,
aur sabha-bhavan pa liya,
tab woh Yudhishthira ke paas gaye."""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Arjun ne shaant par dridh awaaz mein kaha:

“Maharaj,
ab humare paas sab kuch hai —
shastra, bal, saathi, sena, yash aur rajya.

Ab samay aa gaya hai
raaj-kosh (treasury) ko majboot karne ka.

Main chahta hoon
ki sab rajaa humare saamne
kar (tribute) dein.

Main shubh din aur shubh nakshatra mein
Uttar disha ki vijay ke liye
prasthan karna chahta hoon.”

Yudhishthira ne muskurate hue kaha 😊

“Arjun,
tum aage badho.

Brahman tumhe aashirvaad dein,
shatruon ke liye bhay
aur mitron ke liye anand bano.

Mujhe poora vishwas hai
vijay tumhari hi hogi.”

Pandav alag-alag dishaon mein

Fir kya tha—

Arjun ne divya rath par chadhkar
Uttar disha jeeti

Bhima ne apni shakti se
Purab (East) ko jhuka diya 💪

Sahadeva ne
Dakshin (South) par vijay paayi

Nakula ne apni chaturai aur shastra-gyaan se
Paschim (West) ko jeet liya

Sab bhai apni-apni sena ke saath
nikal pade the 🚩

Yudhishthira ka dharm

Jab sab bhai yuddh aur vijay mein lage the,
tab Yudhishthira
Indraprastha mein rehkar
rajya ko dharm aur nyay se chala rahe the.

Rajya mein sukh, shanti aur samriddhi thi 🌸

Bhagadatta ka vachan

Yeh sab sun kar
Bhagadatta ne kaha:

“Arjun,
jaise tum mere apne ho,
waise hi Yudhishthira bhi mere hain.

Main poora sahyog dunga.
Bas batao,
aur kya karna hai?”

Is kahani ka moral 🌿

Sahi samay par sahi kadam zaroori hota hai

Teamwork se hi bada lakshya poora hota hai

Shakti, buddhi aur dharm — teenon ka santulan jeet dilata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.2 – Section XXVI"):
            text1 = """ 
            Section XXVI – Arjun ka Uttar Digvijay (Hinglish Kahani)

Vaisampayana bole—

Bhagadatta ki baat sun kar Arjun ne shaant mann se kaha:

“Agar tum apna vachan nibhaoge,
to mere liye wahi kaafi hai.”

Itna kehkar,
Kunti putra Arjun
Uttar disha ki taraf badh chale—
woh disha jahan dhan ke devta ka raj maana jaata hai."""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Pahadon ki jeet

Arjun ne pehle
pahadi ilaakon aur unke aas-paas ke rajyon ko jeeta.
Jo bhi raja wahan raaj karte the,
sabne uski shakti ko maana
aur kar (tribute) diya.

Arjun ne sirf jeeta hi nahi,
unke dil bhi jeet liye ❤️

Vrihanta ka yuddh

Fir Arjun
Uluka ke raja Vrihanta ke khilaaf badhe.

Nagade,
rath ke pahiye,
aur hathi ki garaj se
dharti kaanp uthi 🌍

Yuddh bhayankar tha.
Par Vrihanta
Arjun ke bal ko seh na paaya.

Ant mein,
woh apna rajya aur dhan lekar
Arjun ke saamne jhuk gaya.

Arjun ne rajya le liya,
par shanti bhi bana li 🤝

Ek ke baad ek vijay

Fir Arjun ne—

Senavindu ko rajya se bahar kiya

Modapura, Vamadeva, Sudaman, Susankula
aur kai uttar ke rajyon ko jeeta

Kuch jagah par khud gaye

Kuch jagah sirf apni sena bheji

Arjun ne Devaprastha mein apna shivir banaya
aur wahin se yuddh ka netritva kiya.

Kathin yuddh

Arjun ne—

Puru vansh ke raja Visvagasva ko haraya

Parvatiya lutere aur Utsava-sanketa naam ke saath kabile ko jhukaya

Kashmir, Lohita, aur dus rajyon ke rajon ko parajit kiya

Trigarta, Darava, Kokonada jaise veer rajyon ko bhi hara diya

Kuch yuddh itne kathin the
jaise devta aur asuron ka sangram ⚔️

Antim vijay

Sabse kathin yuddh
Rishikon ke saath hua.

Par ant mein,
Arjun jeet gaya.

Rishiyon ne kar mein diye:

Hare tota rang ke 8 ghode 🐎

Aur kai tez aur sundar ghode

Ant mein,
Arjun ne Himalaya aur Nishkuta parvat jeete
aur Safed Parvat (White Mountains) par
apna shivir lagaya 🏔️

Is kahani ka moral 🌱

Shakti ke saath vinamrata ho, to rajya tikta hai

Jeet sirf talwar se nahi, dil se bhi hoti hai

Achha neta wahi hota hai jo jeet ke baad shanti banaye"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.3 – Section XXVII"):
            text1 = """ 
            Section XXVII – Arjun ka Uttari Digvijay (Hinglish Saral Arth)

Vaisampayana kehte hain—

Mahaveer Arjuna, jo Pandavon mein sabse aage the,
Safed Parvat (White Mountains) ko paar karke
Limpurusha desh mein pravesh karte hain."""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Limpurushon par vijay

Yeh desh Durmaputra ke adheen tha.
Yahan bhayankar yuddh hua,
jismein anek Kshatriya mare gaye.

Ant mein Arjun ne:

Poore desh ko apne adheen kiya

Apni poori prabhuta sthapit ki

Harataka aur Manasarovar

Uske baad Arjun
Harataka desh gaye,
jahan Guhak raj karte the.

Yahan Arjun ne:

Yuddh nahi, balki saam–daam (conciliation) se kaam liya

Rajaon ko apna mitra banaya 🤝

Isi kshetra mein Arjun ne:

Manasa Sarovar

Aur anya Rishiyon ke pavitra sarovar dekhe

Yahin Gandharvon ke kshetron par bhi unka adhikar hua,
jahan se unhe uttam ghode kar mein mile:

Tittiri

Kalmasha

Manduka

Uttar Harivarsha aur Uttari Kuru

Ant mein Arjun Uttar Harivarsha ki taraf badhe.

Wahan ke rakshak, jo ati-balshali aur divya the,
Arjun se bole:

“O Pritha-putra,
yeh desh manushyon ke liye nahi hai.
Yahan Uttari Kuru rehte hain.
Yahan yuddh nahi hota,
aur manav aankhon se kuchh dikhai bhi nahi deta.”

Unhone Arjun ko aadar ke saath roka.

Arjun ka dharmic uttar

Arjun muskura kar bole:

“Mera uddeshya yeh desh jeetna nahi hai.
Main sirf Yudhishthira ke liye
Samrat pad (Rajasuya) ki siddhi chahta hoon.”

Is par Uttari Kurun ne:

Divya vastra

Swargiya abhushan

Divya resham

Alaukik chamde (skins)
kar ke roop mein diye ✨

Mahaan vijay ka samapan

Is prakar Arjun ne:

Uttar ke sabhi jeetne yogya deshon ko jeeta

An-ginat yuddh lade

Apaar dhan, ratna, aur tez ghode ikatthe kiye 🐎

Fir woh:

Indraprastha laut aaye

Saara dhan Yudhishthira ko arpan kar diya

Aur raja ke aadesh se vishram ke liye apne kaksh mein gaye

Is adhyaay ka saar 🌿

Shakti ke saath sanyam Arjun ki pehchaan hai

Jahan yuddh anuchit ho, wahan maryada sarvopari hoti hai

Sabhi jeete gaye rajyon ka uddeshya tha —
Dharmic Samrajya (Rajasuya) ka nirmaan"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.4 – Section XXVIII"):
            text1 = """ 
            Section XXVIII – Bhima ka Purab Digvijay (Hinglish Saral Kahani)

Vaisampayana kehte hain—

Bhima, jo apni apaar shakti ke liye mashhoor the,
Yudhishthira ki anumati lekar
Purab (East) ki taraf yatra par nikle।

Unke saath:"""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Bade-bade haathi 🐘

Tez ghode 🐎

Majboot rath

Aur shastron se sajji hui vishaal sena thi

Bhima jahan se guzarte,
dushmanon ke dil mein bhay aa jaata.

Panchal, Gandak aur Videh

Sabse pehle Bhima Panchal desh gaye.
Yahan unhone:

Saam-daam se kaam liya

Logon ko apna mitra banaya 🤝

Fir Bhima ne:

Gandaka

Videha
ko jaldi hi apne adheen kar liya.

Uske baad Dasarna desh jeeta gaya.

Dasarna ke Raja Sudharman

Dasarna mein raja Sudharman ne
nange haathon Bhima se yuddh kiya 💪

Yeh yuddh:

Kathor tha

Par veerata se bhara tha

Bhima ne Sudharman ki himmat dekh kar:

Unhe apni sena ka mukhya senapati bana diya 👑

Yeh Bhima ka gun tha —
shakti ke saath samman.

Asvamedha aur Purvi Kshetra

Fir Bhima aage badhe.
Unki sena ke kadmon se dharti kaanp uthi 🌍

Bhima ne:

Rocamana, jo Asvamedha desh ka raja tha,

Use poori sena ke saath yuddh mein hara diya

Is tarah Bhima ne:

Poora Purab ka kshetra apne adheen kar liya

Pulinda, Sukumara aur Sumitra

Uske baad Bhima:

Pulinda desh gaye

Wahan Sukumara aur Raja Sumitra ko bhi apne adheen kiya

Bhima jahan jaate,
vijay unke saath chalti.

Chedi aur Sisupala

Ant mein Bhima:

Chedi desh pahunche

Jahan raja Sisupala raj karta tha

Sisupala ne:

Bhima ka sammaan se swagat kiya

Yuddh ka raasta nahi chuna

Donon veeron ne:

Ek doosre ka kushal-mangal poocha 😊

Sisupala muskura kar bola:

“Bhima, tumhara uddeshya kya hai?”

Bhima ne:

Yudhishthira ke Rajasuya ka lakshya bataya

Yeh sunkar Sisupala ne:

Apna rajya samarpit kar diya

Bhima ko 30 raaton tak aadar aur seva di 🌙

Uske baad Bhima:

Apni sena aur rathon ke saath

Aage ki yatra par nikal pade

Is khand ka saar 🌼

Bhima sirf balwaan nahi, nyay-priya bhi the

Veerata ke saath sammaan unki pehchaan hai

Sabhi vijayon ka uddeshya ek hi tha —
Dharmic Rajasuya ke liye marg banana"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.5 – Section XXIX"):
            text1 = """ 
            Section XXIX – Bhima ka Mahaan Digvijay (Hinglish Saral Kahani)

Vaisampayana kehte hain—

Bhima, jo sabhi shatruon ke daman karne wale the,
apni poorvi–uttari digvijay ko aage badhate hue
ek ke baad ek rajyon ko apne adheen laate gaye."""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Kosala, Ayodhya aur Uttari Desh

Sabse pehle Bhima ne:

Kumara desh ke raja Srenimat ko haraaya

Fir Kosala ke raja Vrihadvala ko jeeta

Uske baad Bhima ne:

Ayodhya ke veer raja Dirghayaghna ko
apni bhayanak shakti se parajit kiya

Fir:

Gopalakaksha

Uttari Kosala

Malla desh
sab Bhima ke adheen aa gaye.

Himalaya ke neeche ke aardra (moist) kshetron mein bhi
Bhima ka ekchhatra prabhav sthapit ho gaya.

Kashi, Matsya aur Pahadi Rajya

Bhima ne aage badhkar:

Bhallata desh

Suktimanta parvat
jeet liya.

Fir Kashi ke raja Suvahu:

Yuddh mein kabhi peechhe na hatne wale the

Lekin Bhima ne unhe bhi paraajit kar diya

Uske baad:

Kratha (Suparsa kshetra)

Matsya

Malada

Pasubhumi
sab Bhima ke adheen ho gaye.

Videha, Janaka aur Mleccha Desh

Bhima ne:

Madahara, Mahidara, Somadheya jeete

Fir Vatsabhumi, Bharga, Nishada, Manimat ko bhi vash mein kiya

Yahan ek mahatvapurn baat:

Janaka, Videha ke mahan raja,
Bhima se aasani se parajit ho gaye

Isse pata chalta hai ki Bhima ka prabhav
sirf bal se hi nahi, raajneeti se bhi tha

Bhima ne:

Saka

Barbar (Mleccha) jatiyon
ko bhi yuktipoorvak apne adheen kiya.

Kirata, Magadha aur Karna

Videha se Bhima ne:

Indra parvat ke paas rehne wale
7 Kirata rajyon ko jeeta

Fir:

Subma aur Prasuhma ko jeet kar

Magadha ki taraf badhe

Raaste mein:

Danda aur Dandadhara rajaon ko vash mein kiya

Girivraja pahunche

Wahan:

Jarasandha ke putra ko
saam-daam se apna mitra banaya

Unse kar (tribute) liya

Iske baad Bhima:

Kansa ki disha mein badhe

Aur yahin unka saamna hua
Karna se

Bhima ne:

Karna ko bhi paraajit kar diya

Unhe apne adheen laaya

Vanga, Samudra-tat aur Apar Sampatti

Bhima ne aage:

Madagiri ke raja ko yuddh mein maar giraya

Pundra, Kausika-kaccha, Vanga
ke rajyon ko jeeta

Unhone:

Samudrasena

Chandrasena

Tamralipta

Karvata, Suhma
aur samudra-tat ke sabhi rajaon ko vash mein kiya

Saath hi:

Sabhi Mleccha jatiyon ko bhi parajit kiya

Aparimit Dhan aur Ant

Samudri aur marshy kshetron ke rajaon ne Bhima ko:

Chandan, agaru

Kapde, ratna, moti

sona–chandi, moonga, kambal
aur arab–kharab mudraen bhent ki

Itna dhan tha ki:

“Sankhya mein ginna mushkil tha”

Ant mein:
Bhima:

Indraprastha laut aaye

Aur saara dhan
Yudhishthira ko samarpit kar diya 🙏

Is khand ka saar 🌼

Bhima ka digvijay sabse vishaal tha

Bal + neeti + dhairya = Bhima

Sabhi vijayon ka ek hi uddeshya tha:
Dharmic Rajasuya Yajna ke liye
Yudhishthira ki samrajya sthaapna"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.6 – Section XXX"):
            text1 = """ 
            Section XXX – Sahadeva ka Dakshin Digvijay (Hinglish Moral Story)

Vaisampayana kehte hain—

Sahadeva,
Yudhishthira ke aashirvaad ke saath,
dakshin disha ki taraf nikle.
Unke saath ek badi aur majboot sena thi."""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Shuruat: Chhoti jeet, badi soch

Sabse pehle Sahadeva ne:

Surasena ko haraya

Matsya ke raja ko apne adheen kiya

Phir:

Dantavakra ko parajit kiya

Lekin daya dikhate hue,
unhe wapis singhasan par bithaya

Yeh Sahadeva ka nyay aur santulan dikhata hai.

Dakshin ke rajya

Sahadeva ne ek ke baad ek:

Sukumara, Sumitra

Nishada desh, Gosringa parvat

Navarashtra
ko apne adheen kiya.

Kuntibhoja ne khud hi
Sahadeva ka adhipatya sweekar kar liya.

Narmada aur Avanti

Narmada ke kinaare:

Avanti ke raja Vinda aur Anuvinda
ne yuddh kiya

Sahadeva ne unhe hara kar kar (tribute) liya

Phir:

Bhojakata mein
do din tak bhayanak yuddh hua

Ant mein Sahadeva jeet gaye

Kishkindha aur Vanar Raja

Aage badhte hue:

Sahadeva ne Kishkindha ki gufaen dekhi

Wahan Mainda aur Dwivida se
7 din tak yuddh hua

Lekin:

Vanar raja Sahadeva se prasann ho gaye

Unhone kaha:

“Yudhishthira ka karya safal ho”

Aur khushi se kar diya.

Mahishmati aur Agni ka rahasya 🔥

Mahishmati mein:

Sahadeva ka saamna hua Raja Nila se

Is yuddh mein Agni khud
Raja Nila ki madad kar rahe the

Agni ki aag se:

Sahadeva ki sena ghabra gayi

Sab kuch jalta hua sa lag raha tha

Sahadeva ne:

shant mann se

Agni ki stuti aur prarthana ki

Unki sachchai aur bhakti dekh kar:

Agni prasann ho gaye

Bole:

“Main tumhari pariksha le raha tha”

Raja Nila ne:

Sahadeva ko maan diya

Aur kar arpit kiya

Antim dakshini rajya

Iske baad Sahadeva ne:

Tripura, Paurava, Saurashtra

Surparaka, Dandaka van

Samudra-tat ke Mleccha rajya
sab apne adheen kiye

Unhone:

Dravida, Andhra, Kerala, Kalinga

Yavana aur anya deshon se
ratna, sona, chandan liya

Vibhishana aur shant ant

Samudra ke paas:

Sahadeva ne sandesh bheja
Vibhishana ko

Vibhishana ne:

Isse kaal ka niyam maana

Aur khushi se uphaar bheje

Wapsi aur safalta 🌸

Ant mein Sahadeva:

Indraprastha laut aaye

Saara dhan Yudhishthira ko diya

Sahadeva ne mehsoos kiya:

“Mera kartavya poora hua”

Aur woh santosh aur shanti se jeene lage.

Is khand ki seekh 🌱

Sirf bal nahi, vinamrata bhi jeet dilati hai

Bhakti + buddhi + dhairya
sabse badi shakti hoti hai

Sachcha vijeta woh hota hai
jo ahankar nahi karta"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.5.7 – Section XXXI"):
            text1 = """ 
            Section XXXI – Nakula ka Pashchim Digvijay (Hinglish Moral Story)

Vaisampayana kehte hain—

Nakula
ab apni kahani shuru karte hain.
Yeh woh yatra thi
jo pashchim disha ki taraf gayi.

Nakula:

badi sena ke saath

Khandavaprastha se nikle

Rath ke pahiyon aur yoddhaon ki garaj se
dharti kaanp uthi"""
            create_image_text_layout(
                "attached_assets/chapter2/2.5.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Pehla sangharsh

Nakula sabse pehle pahunche:

Rohitaka parvat desh

Yeh desh:

samriddh tha

gaay-dhan aur anaj se bhara tha

Yahan:

Mattamyuraka logon se
bhayanak yuddh hua

Ant mein Nakula jeet gaye

Ek ke baad ek rajya

Nakula ne:

registani pradesh

Sairishaka

Mahetta

sab apne adheen kiye.

Phir unhone:

Dasarna, Sivi, Trigarta

Malava, Ambashtha

aur anya rajyon ko
vinamrata aur bal se jeeta

Samudra ke paas

Nakula pahunche:

samudra ke kinaare

jahan Gramaniya, Abhira,
aur machhua samuday rehte the

Unhone:

kisi par anyaay nahi kiya

sabko saath lekar
kar (tribute) liya

Vasudeva aur Shalya 🤝

Nakula ne:

sandesh bheja Vasudeva ko

Sabhi Yadava:

Pandavon ka adhipatya
sweekar kar gaye

Phir Nakula pahunche:

Sakala, Madra desh

Wahan:

unke mama Shalya
ne unhe pyaar se swagat kiya

Shalya ne:

bina yuddh ke

ratna aur dhan diya

Antim vijay

Nakula ne:

Mlecca, Yavana, Shaka,
Kirata jaise rajyon ko
apne adheen kiya

Yeh jeet:

sirf talwar se nahi

buddhi aur maryada se hui

Itna dhan mila ki:

10,000 oont
mushkil se utha paaye

Wapsi aur samarpan

Nakula:

Indraprastha laut aaye

Saara dhan
Yudhishthira ko de diya

Unke mann mein:

koi ghamand nahi

sirf kartavya poora hone ka sukh

Is kahani ki seekh 🌱

Sachchi jeet mein ahankar nahi hota

Parivaar aur sambandh
yuddh se zyada shaktishaali hote hain

Jo apna kartavya nibha kar
sab kuch arpit kar de,
wahi mahaan hota hai"""
            create_image_text_layout(text_content=text2, layout="full")
    
    with st.expander("Chapter 2.6 – Rajasuyika Parva (Performance of the Rajasuya Sacrifice)"):

        with st.expander("Section 2.6.1 – Section XXXII"):
            text1 = """ 
            Section XXXII – Yudhishthira ka Dharmic Raj (Hinglish Moral Story)

Yudhishthira ek nyay-priya raja the.
Woh hamesha sach aur dharm ke raaste par chalte the.
Isliye unke rajya mein shanti aur samriddhi thi. 🌾"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Rajya ka haal

Log apna-apna kaam khushi se karte the.
Kisan kheti karte the.
Vyapari imaandari se vyapar karte the.
Pashu, kheti aur bazaar – sab phool rahe the.

Barish jitni chahiye utni hoti thi.
Na zyada, na kam.
Na akaal tha,
na baadh,
na bimaari,
na aag,
aur na hi asamay maut.

Yahan tak ki chor aur dhokebaaz bhi
aapas mein jhoot nahi bolte the.
Aisa tha Yudhishthira ka raj. 🌸

Raja ka kosh

Raj-kosh itna bhara hua tha
ki sau saal mein bhi khatam na ho.
Par yeh dhan
galat tareeke se nahi,
dharm se kamaya hua tha.

Yudhishthira ne socha—

“Ab mujhe ek mahaan yagya karna chahiye,
jisme yeh dhan
sahi jagah lag sake.”

Unke mitra aur mantri bole—
“Rajasuya Yagya ka samay aa gaya hai.”

Krishna ka aagman

Tabhi Shri Krishna aaye.
Woh apne saath
bahut saara dhan aur sena laaye.

Unke aane se
Indraprastha aisa chamak utha
jaise andhere mein suraj aa gaya ho. ☀️

Yudhishthira ne unka swagat kiya
aur poocha—
“Sab kushal mangal?”

Phir vinamrata se bole—

“Hey Krishna,
yeh rajya aur yeh dhan
sab aapki kripa se mila hai.
Main chahta hoon
is dhan ka upyog
dharm ke kaam mein ho.”

Krishna ka aashirvaad

Krishna muskuraye aur bole—

“Yudhishthira,
tum rajya ke yogya ho.
Rajasuya Yagya tum hi karo.
Main tumhare saath hoon.”

Yeh sun kar
Yudhishthira bahut prasann hue. 😊

Yagya ki taiyaari

Sab bhai milkar kaam mein lag gaye.
Sahadeva ne saman ikattha karwaya.
Brahmanon ko bulaya gaya.
Sundar yagya-mandap bane.

Door-door se—

Brahman aaye

Raja aaye

Vyapari aaye

Aam log bhi aaye

Sabka swagat barabari aur prem se hua.

Dan aur seva

Roz yagya mein gunjta tha—

👉 “Do”
👉 “Khao”

Yudhishthira ne—

Gaayen di

Sona diya

Vastra diye

Aashray diya

Koi bhookha nahi raha.
Koi udaas nahi raha.

Yeh yagya
sirf shakti ka nahi,
daya aur dharm ka yagya tha. 🌼

Ant mein seekh ✨

Sachcha rajya nyay se chalta hai

Dhan ka asli upyog daan aur seva mein hai

Jab raja dharmic hota hai,
toh poora rajya sukhi hota hai

🌸 Yudhishthira ka raj
humein sikhata hai
ki shakti se bada
dharm hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.2 – Section XXXIII"):
            text1 = """ 
            Section XXXIII – Rajasuya Yagya ka Mahaan Milan (Hinglish Moral Story)

Nakula, jo Pandu ke veer putra the,
Hastinapura pahunche.
Unhone Bhishma Pitamah aur Dhritarashtra ko
poore samman ke saath
Rajasuya Yagya ka nimantran diya. 🙏

Bhishma, Drona aur sab gurujan
khushi-khushi aaye.
Unke aage-aage
ved paath karte hue Brahman chal rahe the."""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Sab rajaon ka aagman

Jab sabko pata chala
ki Yudhishthira Rajasuya Yagya kar rahe hain,
toh desh-desh se raja aane lage.

Koi ratna laya,
koi sona,
koi anmol uphaar.

Kaurav bhai aaye,
Duryodhana bhi aaya.
Karna, Shalya, Kripa, Drona, Ashwatthama –
sab mahaan yoddha wahan the.

Gandhar, Kalinga, Vanga, Dravida, Sindhu,
Parvat ke raja,
Samudra ke paas ke deshon ke raja –
sab aaye.

Yadav vansh ke veer bhi aaye –
Pradyumna, Aniruddha, Gada aur anek yoddha.

Yeh sirf yagya nahi tha,
yeh Bharatvarsh ka maha-sammelan tha. 🌍

Mehmanon ka samman

Yudhishthira ne sabko
pyar aur maryada ke saath swagat kiya.

Har raja ko
ek sundar mahal diya gaya.
Yeh mahal:

Chand aur baraf jaise safed the

Phoolon aur sugandh se bhare hue

Sone ke jaali wale jharokhe

Motiyon se sajje hue

Mulayam farsh aur sundar seedhiyan

Door se dekhne par
woh Himalaya ke shikhar jaise lagte the. ✨

Yagya ka drishya

Thodi der vishraam ke baad
sab raja yagya-mandap mein aaye.

Wahan Yudhishthira:

Brahmanon ko daan de rahe the

Rishiyon ka samman kar rahe the

Dharm ke niyam nibha rahe the

Woh yagya-mandap
aisa lag raha tha
jaise swarg dharti par aa gaya ho. 🌸

Ant mein seekh ✨

Sachcha raja sabka samman karta hai

Shakti ka asli roop vinamrata aur seva hai

Jab sabko barabari se jagah mile,
tabhi rajya mahaan banta hai

🌼 Rajasuya Yagya
sirf shakti ka nahi,
ekta, samman aur dharm ka utsav tha."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.3 – Section XXXIV"):
            text1 = """ 
            Section XXXIV – Rajasuya Yagya: Seva, Vyavastha aur Samman (Hinglish Moral Story)

Vaisampayana bole—

Yudhishthira ne sabse pehle
Bhishma Pitamah, Dronacharya, Kripacharya
aur sab bade-buzurgon ko
vinamrata se pranam kiya. 🙏

Phir Yudhishthira ne kaha:
“Yeh yagya sirf mera nahi,
hum sabka hai.
Jo khazana yahan hai,
woh bhi aap sabka hi hai.
Aap sab milkar mujhe margdarshan dein.”

Yeh sun kar
sab bade log khush ho gaye.
Unhone mehsoos kiya
ki raja sach mein sabko apna maanta hai. 🌼"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Kaam ka sahi bantwara

Yudhishthira ne har ek ko
uski yogyaata ke hisaab se
zimmedari di:

Dushasana → bhojan aur suvidhaon ka prabandh

Ashwatthama → Brahmanon ki seva

Sanjaya → anya rajao ka samman

Bhishma aur Drona → poori vyavastha par nazar

Kripa → ratna, sona aur daan ka prabandh

Vidura → nyay aur vitran (distribution)

Duryodhana → rajao se aane wali bhent aur tributes

Aur Shri Krishna?
Woh toh khud
Brahmanon ke charan dhone mein lage the. 🌸
Itni shakti hone ke baad bhi
unka mann seva mein tha.

Rajao ka maha-samman

Jo bhi raja aaya,
woh hazaaron uphaar le kar aaya.
Koi ratna laya,
koi sona,
koi anmol vastu.

Sab soch rahe the:
“Main bhi is maha yagya mein
apna yogdan doon.”

Yagya ka poora sthal
mahalon se bhara hua tha.
Yeh mahal:

Devtaon ke rathon jaise chamakdar

Ratno se sajje hue

Rakshakon aur veeron se surakshit

Aisa lag raha tha
jaise swarg dharti par utar aaya ho. ✨

Sabka pet bhara, sabka mann bhara

Yudhishthira ne:

Sabko pet bhar kar khana diya 🍚

Brahmanon ko daan diya

Garibon, mehmanon, sabka dhyan rakha

Devta bhi khush hue
havan, hom aur mantron se.
Brahman bhi prasann hue
daan aur bhojan se.
Aur aam log bhi
khushi se bhar gaye. 😊

Ant mein seekh 🌟

Achha raja woh hota hai
jo zimmedari baantna jaane

Asli mahaanta
seva aur vinamrata mein hoti hai

Jab sabka samman ho,
tabhi koi kaam sach mein mahaan banta hai

🌼 Rajasuya Yagya
sirf ek rasam nahi,
balki ek misaal thi
ki shakti ke saath
seva aur nyay zaroori hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.4 – Section XXXV"):
            text1 = """ 
            Section XXXV – Sabse Pehla Sammaan (Hinglish Moral Story)

Vaisampayana bole—

Rajasuya yagya ka aakhri din tha.
Aaj raja Yudhishthira par
pavitra jal ka abhishek hona tha. 💧

Sab mahaan Rishi,
aur door–door se aaye raja,
milkar yagya-mandap ke
andar gaye.

Narada ji aage the.
Sab Rishi shaant baithe the.
Aisa lag raha tha
jaise Brahma-lok ho. ✨"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Gyaan bhari baatein

Rishi aapas mein baat kar rahe the:

“Yeh sahi hai.”

“Nahi, aisa nahi.”

“Ho sakta hai.”

Koi tark se baat jeet raha tha.
Koi shaant muskaan ke saath sun raha tha.
Pura mandap
taaron se bhara aakash jaisa lag raha tha. 🌌

Wahan koi bhi bina maryada ka nahi tha.
Sab shuddh mann aur vrat ke saath baithe the.

Narada ji ka gehra vichaar

Narada ji ne
Yudhishthira ki samriddhi dekhi.
Unhone sab rajaon ko dekha.

Unka mann soch mein doob gaya. 🤍
Unhe yaad aaya—
Devta dharti par aaye hain.
Aur Narayana khud
manav roop mein yahin hain.

Narada ji samajh gaye:
Yeh sab ek divya yojna ka hissa hai.
Yeh sab shaktiwaan veer
apna kaam poora karke
wapas jayenge.

Yeh soch kar
Narada ji shant ho gaye.

Bhishma Pitamah ka sujhav

Tab Bhishma Pitamah bole—

“Yudhishthira,
sab raja yahan kaafi samay se hain.
Inka samman hona chahiye.”

Unhone kaha:
“Guru, Rishi, rishtedaar, mitra aur raja—
yeh sab Arghya ke yogya hote hain.”

“Par pehle
sabse shreshtha ko Arghya dena chahiye.”

Yudhishthira ne namrata se poocha:
“Pitamah,
aapke hisaab se
sabse shreshtha kaun hai?”

Sach ka faisla

Bhishma Pitamah ne kaha—

“Jaise suraj
sab roshniyon mein sabse upar hota hai,
waise hi Krishna
hum sab mein shreshtha hain. ☀️

Yeh yagya-mandap
unhi se chamak raha hai.”

Yeh sun kar
Sahadeva aage aaye.
Unhone pehla Arghya
Krishna ko diya. 🌸

Krishna ne use
shaant muskaan ke saath sweekar kiya.
Par ghamand ko chot lagi

Lekin Shishupala
yeh dekh kar chup na reh saka. 😠
Uske mann mein
gussa bhar gaya.

Usne sabke saamne
Bhishma aur Yudhishthira par
ungli uthai.
Aur Krishna ke liye
kathor shabd bole.

Seekh 🌼

Sachcha samman
yogyaata se milta hai

Gyaan aur vinamrata
hamesha shreshtha hote hain

Ghamand
aankhon par parda daal deta hai

🌟 Jahan sach ka samman hota hai,
wahan ahankaar tik nahi paata."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.5 – Section XXXVI"):
            text1 = """ 
            Section XXXVI – Ahankaar ka Ubaal (Hinglish Moral Story)

Shishupala gusse mein bola— 😠

“O Kuru-vansh ke raja,
yeh Vrishni vansh ka Krishna
is sab mahaan rajaon ke beech
raaj-sammaan ke layak nahi hai.

Yudhishthira,
tum Pandav bachche ho.
Tumhe dharma ki gehraai samajh hi nahi aati.
Dharma bahut sookshm hota hai.

Aur Bhishma!
Aapse mujhe yeh umeed nahi thi.
Agar aap jaise gyaani
apne fayde ke liye faisla karein,
toh yeh ninda ke yogya hai.”"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Sawal par sawal

Shishupala rukha nahi.
Usne ek ke baad ek sawal daag diye—

“Krishna raja bhi nahi hai.
Phir kaise usse pehla samman?

Agar umar ki baat hai,
toh Vasudeva yahin hain.

Agar mitrata ki baat hai,
toh Drupada bhi yahin hain.

Agar guru ki baat hai,
toh Drona aur Kripa baithe hain.

Agar yagya ke rishi chahiye,
toh Vedavyasa yahin hain.

Phir bhi Krishna ko hi
pehla Arghya kyun?”

Ghamand bol raha tha

Shishupala aur tez ho gaya—

“Bhishma, Bhishmaka, Rukmi, Shalya,
Pandya, Ekalavya, Karna—
sab yahan maujood hain.

Karna jaise maha-veer ko chhod kar
Krishna ko chunna
sirf apmaan hai.

Krishna na raja hai,
na guru,
na yagya-purohit.

Phir bhi usey samman diya gaya—
yeh sab swarth ke kaaran hua hai!”

Krishna par aarop

Shishupala ne Krishna ki taraf dekha—

“Janardana,
tumne yeh samman kyun sweekar kiya?
Jo tumhare layak hi nahi tha?

Tum toh us kutte jaise ho
jo akela baith kar
ghee chaat leta hai
aur khud ko mahan samajhta hai.

Yeh raaj-sammaan
tumhare liye waisa hi hai—
jaise andhe ko rang,
ya nirbal ko shringaar.”

Ant mein apmaan

Shishupala ne kaha—

“Aaj sabka asli chehra saamne aa gaya.
Yudhishthira ka,
Bhishma ka,
aur Krishna ka bhi.”

Yeh keh kar,
Shishupala apni jagah se uth khada hua.
Uske saath kuch raja bhi uthe.
Aur woh sabha chhod kar bahar nikal gaye. 🚶‍♂️🚶‍♂️
Seekh 🌱

Ahankaar jab bolta hai,
toh gyaan chup ho jata hai

Sachcha mahan
shor nahi karta

Jo shant rehta hai,
wahi sabse shaktishaali hota hai

✨ Jahan ghamand hota hai,
wahan patan shuru ho jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.6 – Section XXXVII"):
            text1 = """ 
            Section XXXVII – Shanti, Gyaan aur Sachchai (Hinglish Moral Story)

Shishupala gusse mein sabha chhod kar ja raha tha.
Tab Raja Yudhishthira turant uske peeche gaye.
Unki awaaz shaant aur pyaar bhari thi. 🌿"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Yudhishthira bole

“O Chedi ke raja,
jo baatein tumne kahi hain
woh uchit nahi hain.

Bhishma jaise mahaan purush ko
yeh kehna ki unhe dharma nahi aata,
yeh paap aur anuchit hai.

Dekho, yahan maujood
bahut se raja
tumse bade aur anubhav-shaali hain.
Sab Krishna ke samman ko sweekar kar rahe hain.

Tum bhi unki tarah
sanyam rakho.
Bhishma Krishna ko jaante hain,
tum unhe utna nahi jaante.”

Bhishma ka gyaan

Tab Bhishma Pitamah khade hue.
Unki awaaz gambhir thi,
par shant bhi. 🕊️

“Jo Krishna ke samman ko
sweekar nahi karta,
woh samjhaane layak hi nahi hota.

Jo veer kisi shatru ko jeet kar
usey chhod deta hai,
woh uska guru ban jaata hai.

Is sabha mein
koi bhi aisa raja nahi
jo kabhi Krishna se
jeeta na gaya ho.

Isliye Krishna
sirf humare liye nahi,
teenon lokon ke liye poojniya hain.”

Krishna ka mahattva

Bhishma ne aage kaha—

“Hum Krishna ko
na rishte ke kaaran poojte hain,
na laabh ke liye.

Hum unhe poojte hain
kyunki unmein
gyaan, bal aur dharma hai.

Gyaan Brahman ka shreshth gun hai.
Bal Kshatriya ka shreshth gun hai.
Aur dono Krishna mein hain.”

Antim sach

Bhishma bole—

“Yeh poora sansaar
Krishna mein sthapit hai.
Surya, Chandra, dharti, aakash—
sab unse hi hain.

Jaise Surya sabse tejasvi hai,
waise hi Kesava sabse shreshth hain.

Shishupala abhi bachcha hai.
Isliye woh
Krishna ko samajh nahi paata.

Jo sachcha dharma chaahta hai,
usey ghamand chhodna hota hai.”

Seekh 🌼

Gussa aankhen band kar deta hai

Gyaan shant mann se aata hai

Jo sach mein mahaan hota hai,
usey apni mahaanta dikhani nahi padti

✨ Jahan ahankaar khatam hota hai,
wahi se gyaan shuru hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.6.7 – Section XXXVIII"):
            text1 = """ 
            Section XXXVIII – Ghamand ka Ubharta Toofan (Hinglish Moral Story)

Bhishma Pitamah chup ho gaye.
Sabha mein gehri shaanti chhaa gayi.
Tab Sahadeva aage badhe.
Unka chehra shaant tha,
par shabdon mein dridh nischay tha. 🌿"""
            create_image_text_layout(
                "attached_assets/chapter2/2.6.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )
            text2 = """ 
            Sahadeva ka kathor sach

Sahadeva bole—

“Jo bhi raja
Kesava ke samman ko
sahan nahi kar sakta,
jo Krishna ki pooja se jalta hai—

Mera pair uske ahankaar par hai.

Agar kisi mein himmat ho,
toh iska uttar de.
Aur jo buddhi-shaali hain,
woh jaante hain ki
Krishna guru, pita aur margdarshak hain.
Unka samman bilkul uchit hai.”

Sabha ka pratikriya

Sahadeva ne jaise hi yeh kaha,
sabhi mahaan aur ghamandi raja
chup ho gaye.

Kisi ke paas
koi uttar nahi tha. 🤐

Tab aakash se phoolon ki varsha hui. 🌸
Aur ek divya awaaz boli—

👉 “Bahut achha, bahut achha.”

Narada ka antim sandesh

Tab Narada Rishi bole.
Unki awaaz gambhir thi,
par sach se bhari hui. 🕊️

“Jo vyakti
lotus-netra Krishna ka samman nahi karta,
woh jeevit hote hue bhi
mrit samaan hai.

Usse baat karna bhi
vyarth hai.”

Shishupala ka gussa

Krishna ko Arghya mil chuka tha.
Yeh dekh kar Shishupala ka krodh bhadak utha. 🔥
Uski aankhen laal ho gayi.

Woh sab rajaon se bola—

“Jab main yahan hoon,
toh tum kya soch rahe ho?
Chalo, Pandavon aur Vrishnion ke
khilaaf yudh ki taiyaari karein!”

Ghamand ka andhaapan

Shishupala ke shabdon se
kai raja bhadak gaye.
Unke chehre pe irsha aur krodh tha.

Woh bole—

“Hum aisa kuch karenge
ki yeh yagya
poora na ho sake.
Aur Krishna ka samman
humne sweekar kiya—
yeh baat kabhi na lage!”

Doston ne samjhaya,
par gussa
samajh par bhaari pad gaya.

Unke chehre
aise lag rahe the
jaise shikaar chhin jaane par
dahaadte hue sher. 🦁
Krishna ki samajh

Krishna sab dekh rahe the.
Unhone samajh liya—

Yeh rajaon ka samuh
ab toofan banne ko tayaar hai.
Sainyon ki lahron wala
ek bada samundar
uchhalne hi wala hai… 🌊

Seekh 🌼

Ahankaar buddhi ko andha kar deta hai

Sach bolne wala akela bhi sahi hota hai

Jo dharma ke viruddh khada hota hai,
woh ant mein khud hi girta hai

✨ Jab gussa neta ban jaaye,
tab vinash raasta ban jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

    with st.expander("Chapter 2.7 – Sisupala-badha Parva (Death of Sisupala)"):

        with st.expander("Section 2.7.1 – Section XXXIX"):
            text1 = """ 
            Vaisampayana ne kaha—

Sabhi raja gusse se bhare hue the.
Woh sab ek bade samundar jaise lag rahe the,
jo tez hawa se hil raha ho.

Yudhishthira ne yeh dekha.
Unka mann chinta se bhar gaya.
Woh dheere se Bhishma Pitamah ke paas gaye."""
            create_image_text_layout("attached_assets/chapter2/2.7.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yudhishthira bole,
“Pitamah, sab raja bahut gusse mein hain.
Mujhe bataiye, main kya karun?
Mera yagya rukna nahi chahiye.
Aur meri praja ko bhi koi nuksaan na ho.”

Bhishma Pitamah shaant muskaan ke saath bole—

“Dar mat, beta.
Kya kabhi kutta sher ko hara sakta hai?”

“Yeh sab raja, gusse mein bhaukne wale kutton jaise hain.
Aur sher abhi so raha hai.”

“Woh sher hai Shri Krishna.
Jab tak woh jaagte nahi,
tab tak Shishupala apne aap ko bahut bada samajh raha hai.”

“Par sach yeh hai,
yeh sab raja sirf shor macha rahe hain.
Unke paas asli shakti nahi hai.”

“Shishupala ki buddhi bhrasht ho chuki hai.
Aur jo bhi uske saath chalna chahta hai,
uski soch bhi galat ho jaati hai.”

“Krishna hi srishti ko janam dene wale hain.
Aur wahi ant bhi karte hain.”

“Jo ahankaar mein andha ho jaata hai,
uska patan nishchit hota hai.”

Vaisampayana aage kehte hain—

Yeh baatein sun kar Shishupala aur bhi gusse mein aa gaya.
Usne Bhishma Pitamah se kathor aur kadve shabd bole.

Par sab jaante the—
Gussa shor karta hai.
Aur dharm shaant rehta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.2 – Section XL"):
            text1 = """ 
            Shishupala gusse se bola—

“Bhishma!
Tum buddhe ho gaye ho,
phir bhi itna jhooth bolte ho.

Tum sab rajaon ko bekaar ka darr dikha rahe ho.
Kya tumhe sharam nahi aati?”

“Tum Kuruvansh ke bade ho.
Par tumhari salah dharm se door hai.
Jo tumhe follow karte hain,
woh andhon ke peechhe chalne wale andhon jaise hain.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Tum baar-baar Krishna ki tareef karte ho.
Putana, vulture, Govardhan—
yeh sab suna kar
tum hamare dil dukhate ho.”

“Krishna ek gwala tha.
Ismein kaunsi badi baat hai?
Agar bachpan mein kisi ko maar diya,
ya pahad utha liya,
toh ismein kya chamatkaar hai?”

“Aur sabse galat baat yeh hai—
jis Kansa ka khana khaya,
usi ko maar diya.
Yeh toh dharm ke khilaaf hai.”

“Budhe Bhishma,
tum dharm ki baat karte ho,
par tum khud use follow nahi karte.”

“Tum kehte ho—
‘Krishna sabse gyaani hai.’
‘Krishna poore jagat ka swami hai.’

Par baar-baar bolne se
jhooth sach nahi ho jaata.”

“Har jeev apni soch ke hisaab se kaam karta hai.
Aur tumhari soch bahut chhoti hai.”

“Pandav bhi tumhari baat maante hain.
Isliye unki soch bhi bhrasht ho gayi hai.”

Phir Shishupala aur tez bola—

“Tum dharm ki baat karte ho,
par Amba ke saath kya kiya,
woh sab bhool gaye?”

“Tumhari pratigya,
tumhara brahmacharya—
sab bekaar hai.”

“Bina santaan ke
saare vrat aur pooja
vyarth ho jaate hain.”

Phir Shishupala ne ek kahani sunayi—

“Ek buddha hans tha.
Woh sabko dharm sikhata tha.
Par chupke se
sabke ande kha jaata tha.”

“Jab sach saamne aaya,
toh baaki pakshiyon ne
usse maar diya.”

Shishupala bola—

“Bhishma,
tum bhi uss hans jaise ho.
Agar gussa badha,
toh yeh raja tumhe bhi nuksaan pahuncha sakte hain.”

Kahani yahin rukti hai—

👉 Jo sirf bolta hai, par karta nahi,
uska sach ek din saamne aa jaata hai.

👉 Gussa bolta hai,
par dharm shaant rehta hai.

👉 Aur ahankaar
apna hi patan likhta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.3 – Section XLI"):
            text1 = """ 
            Shishupala phir se zor se bola—

“Jarasandha ek mahaan raja tha.
Usne Krishna se ladna bhi nahi chaha.
Usne kaha, ‘Yeh toh ek daas hai.’
Mujhe us raja par garv tha.”

“Par jo kaam Krishna, Bhima aur Arjuna ne kiya,
woh kaun sa dharm tha?”

“Woh teeno Brahman ka bhesh bana kar aaye.
Galat raaste se mahal mein ghuse.
Sirf taqat jaanchne ke liye.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Jarasandha ne pehle unke pair dhone ke liye paani diya.
Tab Krishna ne kaha,
‘Main Brahman nahi hoon.’”

“Phir jab Jarasandha ne bhojan ka nimantran diya,
toh Krishna ne mana kar diya.”

“Agar yeh sach mein poore jagat ka swami hai,
toh phir Brahman ka roop kyun nahi maanta?”

“Hairani ki baat yeh hai,
tum Pandavon ko galat raah par le ja rahe ho,
phir bhi woh tumhe sachcha maante hain.”

“Shayad yeh bhi hairani ki baat nahi hai.
Tum buddhe ho gaye ho,
aur dil se kamzor pad gaye ho.
Isliye woh tumhari har baat maan lete hain.”

—

Yeh kadve shabd sun kar Bhima ka khoon khol utha.
Uski aankhen laal ho gayi.
Chehra gusse se bhar gaya.

Woh daant peesne laga.
Aisa lag raha tha jaise
pralay ke samay Mrityu khud khadi ho.

Bhima uchhal kar aage badhne hi wala tha.
Tab Bhishma Pitamah ne
uska haath pakad liya.

Bhishma ne pyaar aur gyaan se samjhaya.
Bhima dheere-dheere shaant ho gaya.

Jaise samundar kitna bhi bhare,
phir bhi apni seema nahi todta—
waise hi Bhima ne
Bhishma ki baat maan li.

Par Shishupala bilkul nahi dara.
Usne Bhima ki taraf dekha bhi nahi.
Jaise sher chhote jaanwar ko
nazaron mein bhi na laata ho.

Woh hanste hue bola—

“Bhishma, ise chhod do.
Sab raja dekhenge
kaise meri shakti ise
aag mein pade keede jaise jala degi.”

Yeh sun kar Bhishma ne
Bhima se shaant shabdon mein kaha—

🟢 Gussa shor karta hai.
🟢 Par dhairya hi asli shakti hota hai.
🟢 Jo apne aap ko bahut bada samajhta hai,
woh aksar apni seema bhool jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.4 – Section XLII"):
            text1 = """ 
            Bhishma Pitamah bole—

“Bhima,
main tumhe Shishupala ki kahani sunata hoon.”

“Jab Shishupala paida hua,
uske teen aankhen thi
aur chaar haath the.”

“Paida hote hi
woh zor-zor se chillaya.
Uski awaaz gadhe jaisi thi.”

“Maa-baap darr gaye.
Sab rishte-naate ghabra gaye.
Unhone socha—
ise chhod dena chahiye.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Tab achanak
aakash se awaaz aayi—

“Dar mat, raja.
Yeh bachcha bhagyashaali hoga.
Bahut shaktishaali hoga.”

“Iski mrityu abhi nahi hogi.
Jo ise marega,
woh bhi janm le chuka hai.”

Yeh sun kar
maa ka dil pighal gaya.
Usne haath jod kar poocha—

“Kaun hoga
mere bete ka vinash karne wala?”

Awaaz boli—

“Jis kisi ki god mein
ise bithane par
iske extra haath gir jaayenge,
aur teesri aankh gaayab ho jaayegi—
wahi iska ant karega.”

Yeh baat sun kar
duniya ke kai raja
Chedi nagar aaye.

Raja ne apne bete ko
ek-ek karke
sabki god mein bithaya.

Par kuch bhi nahi hua.
Haath aur aankh
waise hi rahe.

Phir Dwarka se
Balarama aur Krishna aaye.
Woh rani ke bhai the.

Sabko pranam karke
woh shaant baith gaye.

Rani khushi-khushi
bachche ko
Krishna ki god mein bitha deti hai.

Aur tab—
chamatkaar ho gaya.

Extra haath gir gaye.
Teesri aankh bhi gaayab ho gayi.

Rani darr gayi.
Usne Krishna se kaha—

“Mujhe bacha lo.
Mera beta tumhare haath se
na mare.”

Krishna ne pyaar se kaha—

“Dar mat, mausi.
Bolo, kya vardaan chahiye?”

Rani boli—

“Mere bete ke aparadh
maaf kar dena.
Bas yahi vardaan chahiye.”

Krishna bole—

“Main uske sau aparadh
maaf karunga.
Tum shok mat karo.”

Bhishma Pitamah ne baat khatam karte hue kaha—

“Bhima,
yeh wahi Shishupala hai.
Krishna ke vardaan ke ghamand mein
aaj bhi ladne ko tayaar khada hai.”

🌱 Moral (Soft & Simple):

Vardaan ghamand ke liye nahi hote.

Gussa jab had paar karta hai,
toh maafi bhi khatam ho jaati hai.

Jo apni seema bhool jaata hai,
wahi apna ant bulata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.5 – Section XLIII"):
            text1 = """ 
            Bhishma Pitamah bole—

“Bhima,
jo Shishupala tumhe yudh ke liye bula raha hai,
yeh uska apna faisla nahi hai.”

“Yeh sab Krishna ki ichchha se ho raha hai.”

“Batao,
is dharti par kaunsa raja
mujhse aise baat karne ki himmat karta,
agar us par Mrityu ka saaya na hota?”"""
            create_image_text_layout("attached_assets/chapter2/2.7.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Shishupala mein
Hari ki hi shakti ka ek hissa hai.
Aur ab Bhagwan
apni shakti wapas lena chahte hain.”

“Isi liye
yeh Chedi ka raja
garaj raha hai,
bina kisi ka darr kiye.”

—

Yeh sun kar
Shishupala ka gussa aur badh gaya.
Usne zor se kaha—

“Bhishma!
Agar tumhe kisi ki tareef hi karni hai,
toh Krishna ko chhod do.”

“Dusre rajaon ki tareef karo.
Karna ki karo—
jo mahaan dhanurdhar hai.”

“Drona aur Ashwatthama ki karo—
jo dharti hila sakte hain.”

“Duryodhana, Jayadratha,
Rukmi, Bhagadatta,
Virata, Drupada—
itne veer raja hain!”

“Un sab ko chhod kar
tum Krishna ki hi pooja kyun karte ho?”

“Achhe log
na apni tareef karte hain,
na doosron ki.”

“Tum bina samjhe
Krishna ko mahaan bana rahe ho.”

Phir Shishupala ne
ek chhoti si kahani sunayi—

“Ek chhoti si chidiya hoti hai.
Woh hamesha gyaan ki baat karti hai.”

“Par khud
sher ke daant se
maans chura leti hai.”

“Woh sher ki daya par jeeti hai.”

“Bhishma,
tum bhi usi chidiya jaise ho.”

—

Yeh kadvi baatein sun kar
sab raja gusse mein aa gaye.
Kuch ne kaha—

“Bhishma bahut ghamandi ho gaye hain.
Inhe saza milni chahiye.”

Bhishma shaant rahe.
Unhone dheere se kaha—

“Haan,
main in rajaon ki daya par jeeta hoon.”

“Par sach yeh hai—
main inhe
ghaas ke tinke ke barabar bhi
nahi maanta.”

Yeh sunte hi
sab raja aur bhadak gaye.

Tab Bhishma ne
aakhri baat kahi—

“Shabd ka ant
shabd se nahi hota.”

“Yahan Krishna khade hain—
Govinda,
jo kabhi kamzor nahi hote.”

“Jise jaldi mrityu chahiye,
woh aage badhe
aur Madhava ko yudh ke liye bula le.”

—

🌱 Soft Moral:

Zyada bolna gyaan nahi hota.

Ahankaar aankhon ko andha kar deta hai.

Shaant dharm,
shor machate gusse se hamesha bada hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.6 – Section XLIV"):
            text1 = """ 
            Vaisampayana bole—

Bhishma ke shabd sunte hi
Shishupala aur bhadak gaya.
Woh Krishna ki taraf muda
aur zor se bola—

“Krishna!
Main tumhe yudh ke liye bulata hoon.
Aaj main tumhe
aur Pandavon ko
ek saath mita dunga.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Tum raja nahi ho.
Phir bhi inhone tumhari pooja ki.
Is galti ki saza
sabko milegi.”

Yeh keh kar
Shishupala gusse mein
garajne laga.

Tab Krishna shaant rahe.
Unhone sab rajaon ki taraf dekha
aur dheere se bole—

“Yeh Shishupala
mera hi rishtedaar hai.
Phir bhi hamesha
mujhse dvesh rakhta hai.”

“Isne Dwarka jalayi.
Mere pita ke yagya ka ghoda chura liya.
Nirdosh logon ko bandi banaya.
Aur anek paap kiye.”

“Main sab kuch
apni mausi ke liye
chupchaap sah leta raha.”

“Par aaj,
sab rajaon ke saamne,
iska ghamand had paar kar gaya hai.”

“Isliye
aaj ise dand milna hi chahiye.”

Yeh sun kar
sab raja Shishupala ko
daantne lage.

Par Shishupala hans pada.
Woh bola—

“Krishna,
tumhe sharam nahi aati?
Apni patni ka naam
sabke saamne le rahe ho?”

“Maafi mile ya na mile,
tum mera kya bigaad loge?”

Tab Krishna ne
man hi man
apne Sudarshan Chakra ko yaad kiya.

Krishna bole—

“Rajaon,
maine iske sau aparadh
maaf kiye the.
Yeh vaada
maine iski maa se kiya tha.”

“Aaj
woh ginti poori ho chuki hai.”

“Ab dand ka samay aa gaya hai.”

Itna keh kar
Krishna ne
Sudarshan Chakra chalaya.

Ek pal mein
Shishupala gir pada.
Bijli se gire pahad jaise.

Uske sharir se
ek tej roshni nikli.
Woh roshni
Krishna ko pranam karke
unmein sama gayi.

Aakash garaj utha.
Dharti kaanp gayi.
Bina baadal
baarish hone lagi.

Sab raja
sann reh gaye.

Kuch khamosh rahe.
Kuch gusse mein the.
Aur kuch ne mann hi mann
Krishna ki mahima ko maana.

Rishiyon ne
Krishna ki stuti ki.
Sabke dil shaant ho gaye.

Yudhishthira ne
Shishupala ke antim sanskar
poore samman ke saath karwaye.
Uske bete ko
Chedi ka raja banaya.

Rajasuya yagya
safalta se poora hua.
Krishna ne
har kadam par
raksha ki.

Sab raja
vida lene aaye.
Yudhishthira ne
sabka samman kiya.

Pandav bhai
rajaon ko
seema tak chhod kar aaye.

Phir Krishna
Dwarka jaane lage.

Yudhishthira ne kaha—

“Govinda,
aapki kripa se
sab safal hua.”

Krishna muskuraye.
Unhone aashirvaad diya—

“Raja,
apni praja ka
dhyaan rakhna.
Unke liye
chhaon ban kar rehna.”

Phir dono ne
prem se vida li.

Krishna Dwarka chale gaye.
Aur sab apne-apne ghar.

🌱 Soft Moral (Simple):

Maafi ki bhi ek seema hoti hai.

Ahankaar jab had paar kare,
toh dand zaroor milta hai.

Shaant dharm
aakhir mein jeet ta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.7 – Section XLV"):
            text1 = """ 
            Vaisampayana bole—

Jab Rajasuya Yagya poori tarah sampann ho gaya,
tab Maharshi Vyasa
apne shishyon ke saath
Yudhishthira ke paas aaye.

Yudhishthira turant
apni jagah se khade ho gaye.
Bhaiyon ke saath
Rishi ko pranam kiya.
Unke charan dhoye
aur asan diya."""
            create_image_text_layout("attached_assets/chapter2/2.7.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Vyasa ji shaant roop se baithe
aur bole—

“Beta, baitho.”

Phir unhone kaha—

“Yudhishthira,
tumne bahut bada rajya paya hai.
Yeh asaan nahi tha.”

“Tumhare kaaran
poora Kuru vansh
samriddh hua hai.”

“Mujhe tumne
poora samman diya.
Ab mujhe aage jaana hai.”

Yudhishthira ne
Vyasa ji ke charan chhuye
aur bole—

“Pitamah,
mere mann mein
ek gehra sawaal hai.”

“Rishi Narada ne kaha tha
Rajasuya ke baad
teen tarah ke apashagun aate hain.”

“Kya Shishupala ke girne se
woh sab khatam ho gaye?”

Vyasa ji gambhir ho gaye.
Unhone kaha—

“Rajya ke baad
aane wale 13 saalon mein
bade ghatnaayein hongi.”

“Samay aane par
saare Kshatriya
nasht honge.”

“Ismein
Duryodhana ke paap
aur Bhima-Arjuna ki shakti
ka kaaran hoga.”

“Tum aaj raat
sapne mein
Bhagwan Shiv ko dekhoge.”

“Woh Kailash jaise ujjwal honge.
Nandi par baithe honge.
Aur dakshin disha ki taraf dekh rahe honge.”

“Is sapne se ghabrana mat.
Samay se bada
koi nahi hota.”

“Ab main Kailash jaa raha hoon.
Tum dhairya aur satarkta se
rajya chalao.”

Itna keh kar
Vyasa ji chale gaye.

Yudhishthira ka mann
bhari ho gaya.
Woh sochne lage—

“Kya bhagya ko
mehnat se badla ja sakta hai?”

Phir unhone
apne bhaiyon se kaha—

“Rishi ke shabd sach honge.
Agar meri wajah se
sab nasht hona hai,
toh mujhe jeena hi kyun?”

Yeh sun kar
Arjuna bole—

“Bhaiya,
nirasha mat karo.
Himmat rakho.
Jo sabke liye acha ho
wahi karo.”

Tab Yudhishthira bole—

“Aaj se main ek vachan leta hoon.”

“Agale 13 saal,
main kabhi bhi
kisi se kathor shabd nahi bolunga.”

“Main apne aur paraye mein
bhed nahi karunga.”

“Jab jhagda nahi hoga,
toh yudh bhi nahi hoga.”

“Shanti hi
sabse bada dharm hai.”

Sab bhaiyon ne
is vachan ko
poori shraddha se maana.

Phir Yudhishthira ne
devtaon aur purohiton ko
prasann kiya.

Sab raja chale gaye.
Pandav apne mahal laute.

Sirf Duryodhana
aur Shakuni
sabha mein ruk gaye.

🌱 Soft Moral (Simple & Clear):

Shakti se bada hota hai dhairya.

Yudh jhagdon se janm leta hai.

Shanti aur vinamrata
sabse badi jeet hoti hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.8 – Section XLVI"):
            text1 = """ 
            Vaisampayana bole—

Duryodhana abhi bhi
Pandavon ke sabha-bhavan mein tha.
Woh Shakuni ke saath
us bhavan ko ghoom-ghoom kar dekh raha tha.

Woh bhavan bahut sundar tha.
Aisa jaisa Duryodhana ne
kabhi Hastinapur mein nahi dekha tha.

Ek din
Duryodhana ne
sheeshe ka zameen dekha.
Use laga
yeh paani hai."""
            create_image_text_layout("attached_assets/chapter2/2.7.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Usne apne kapde upar utha liye.
Par asal mein
woh zameen thi.
Galti samajh aate hi
use bahut sharm aayi.

Thodi der baad
usne sheeshe ka talaab dekha.
Use laga
yeh zameen hai.
Aur woh seedha
paani mein gir gaya.

Yeh dekh kar
Bhima zor-zor se hans pada.
Sevak bhi hansne lage.

Kapde badal kar
jab Duryodhana utha,
toh Bhima, Arjuna
aur Nakula-Sahadeva
sab hansne lage.

Duryodhana
apmaan sehna nahi jaanta tha.
Usne kuch kaha nahi.
Par dil ke andar
aag jal rahi thi.

Phir ek aur galti hui.
Kabhi darwaza band laga
jo khula tha.
Kabhi khula laga
jo band tha.

Kabhi sar takra gaya.
Kabhi gir pada.

Aakhir mein
Duryodhana
Pandavon se anumati le kar
Hastinapur ke liye nikal gaya.

Raaste bhar
uska mann dukhi tha.
Woh sirf
Pandavon ki samriddhi
aur sabha-bhavan ke baare mein
sochta raha.

Pandav khush the.
Sab raja
unhe naman kar rahe the.
Yudhishthira ka yash
har jagah phail raha tha.

Yeh sab dekh kar
Duryodhana ka chehra
peela pad gaya.

Woh itna khoya hua tha
ki Shakuni ke poochhne par bhi
kuch nahi bola.

Shakuni ne poocha—
“Bhatije,
itna chup kyun ho?”

Duryodhana bola—

“Maama,
Pandav poori dharti ke raja ban gaye hain.
Unka yagya
Indra ke yagya jaisa lagta hai.”

“Mera dil
jalan se bhar gaya hai.
Main din-raat jal raha hoon.”

“Shishupala ke marne par bhi
kisi ne virodh nahi kiya.
Sab Pandavon ke paksh mein the.”

“Sab raja
Yudhishthira ko
daan aur khazana de rahe the.
Jaise woh unke sevak hon.”

“Yeh sab dekh kar
mujhe eersha ho rahi hai.
Aur main khud se
naraz hoon.”

Phir woh aur dukhi hote hue bola—

“Maama,
mujhe jeene ka mann nahi karta.
Main aag mein kood jaun,
ya zehar pee loon.”

“Jo apne shatru ko
itna safal dekhe,
woh kaise shaant reh sakta hai?”

“Maine Pandavon ko
rokne ki koshish ki.
Par woh kamal ki tarah
aur khil gaye.”

“Lagta hai
bhagya sab kuch hai.
Aur mehnat bekaar.”

“Pandav badhte ja rahe hain.
Aur hum dheere-dheere
kamzor ho rahe hain.”

“Unka bhavan,
unke sevakon ki hansi—
sab kuch
mere dil ko jala raha hai.”

“Maama,
yeh sab pitaji ko bata dena.
Main eersha aur dukh se
bhara hua hoon.”

🌱 Soft Moral (Simple & Clear):

Eersha dil ko jala deti hai.

Doosron ki khushi dekh kar jalna,
apne sukh ko khud khatam kar deta hai.

Vinay aur mehnat
sachchi shanti laate hain."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.9 – Section XLVII"):
            text1 = """ 
            Shakuni dheere se bola—

“Duryodhana,
Yudhishthira se jalan mat rakho.”

“Pandav jo paa rahe hain,
woh unke bhagya aur mehnat ka phal hai.”

“Tumne unhe kai baar
nuksaan pahunchane ki koshish ki.
Par har baar
woh bach gaye.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Unhe Draupadi jaisi patni mili.
Drupada aur uske putra
unke saathi bane.”

“Krishna jaise shaktishaali mitra
unke saath hain.
Isliye woh aage badh rahe hain.”

“Arjuna ko Gandiva dhanush mila.
Akshay baan mile.
Usne kai rajaon ko
jeet liya.”

“Maya daanav ne
unke liye
woh adbhut sabha banayi.”

“Ismein dukhi hone ki
kya baat hai?”

“Tum kehte ho
tumhare paas saathi nahi hain.
Yeh sach nahi.”

“Tumhare bhai tumhare saath hain.
Drona, Ashwatthama, Karna,
Kripa, main,
aur Saumadatti—
sab tumhare mitra hain.”

“In sab ke saath
tum poori dharti jeet sakte ho.”

—

Duryodhana bola—

“Maama,
agar tum saath do,
toh main Pandavon ko hara sakta hoon.”

“Unka rajya,
unka dhan,
aur woh sabha—
sab mera ho jayega.”

—

Shakuni thoda ruk kar bola—

“Par yudh se
Pandav jeete nahi ja sakte.”

“Woh bahut balwaan hain.”

“Lekin
ek aur raasta hai.”

Duryodhana turant bola—

“Maama,
agar bina khoon-kharabi ke
koi upaay ho,
toh batao.”

—

Shakuni muskuraaya—

“Yudhishthira
jua khelna pasand karta hai.”

“Par use khelna
achha nahi aata.”

“Woh mana nahi kar paata.”

“Main jua mein
bahut nipun hoon.”

“Tum usse
jua khelne ke liye bulao.”

“Main uska rajya
aur saari sampatti
jeet lunga.”

“Par pehle
yeh baat
raja Dhritarashtra ko batao.”

“Unki anumati se
sab ho jayega.”

—

Duryodhana bola—

“Maama,
yeh baat
tum hi pitaji ko samjhao.”

“Main itni samajhdari se
baat nahi kar paunga.”

🌱 Soft Moral (Simple & Clear):

Eersha jab buddhi par haavi ho jaati hai,
toh galat raaste dikhne lagte hain.

Yudh se jo na mile,
chaal se lene ki soch
vinash ki shuruaat hoti hai.

Laalach aksar
adharm ka darwaza kholta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.10 – Section XLVIII"):
            text1 = """ 
            Vaisampayana bole—

Rajasuya yagya dekh kar
Shakuni ko Duryodhana ke mann ki baat
pehle hi samajh aa gayi thi.

Woh Duryodhana ke saath
sabha se nikalte hue
seedha Dhritarashtra ke paas gaya.

Raja andhe the,
par buddhi se bade the.
Shakuni ne namrata se kaha—"""
            create_image_text_layout("attached_assets/chapter2/2.7.10.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Rajaji,
aapke putra Duryodhana
andar se bahut dukhi hai.”

“Uska rang udd gaya hai.
Woh kamzor aur chintit ho gaya hai.”

“Kripya poochhiye,
uske mann ka dukh kya hai.”

Dhritarashtra ne
Duryodhana se pyaar se poocha—

“Beta,
tum itne dukhi kyun ho?”

“Tumhare paas
dhan, bhog, vastra,
ghode, mahal—
sab kuch hai.”

“Phir bhi
tum aise kyun lag rahe ho
jaise tumhare paas
kuch bhi nahi?”

Duryodhana ne kaha—

“Pitaji,
main jeete hue bhi
jal raha hoon.”

“Jab tak
shatru ka ghamand
tootta nahi,
dil ko shanti nahi milti.”

“Yudhishthira ki samriddhi
dekh kar
mera mann aur bhi jalta hai.”

“Woh hazaron Brahmanon ko
roj bhojan deta hai.”

“Raja log
uske liye
daan aur khazana laate hain.”

“Uske yagya mein
itna dhan tha
jo maine kabhi dekha bhi nahi.”

“Uski sabha
sitaaron se bhare
aakash jaisi lagti thi.”

“Sab raja
uske aage
sir jhuka rahe the.”

“Yeh sab dekh kar
mujhe neend nahi aati.”

“Mera mann maanta hai—
Pandav badhte ja rahe hain.
Aur hum ghatt rahe hain.”

“Pitaji,
yeh jalan
mujhe jeene nahi deti.”

Yeh sun kar
Shakuni dheere se bola—

“Duryodhana,
agar tumhe
Pandavon jaisi samriddhi chahiye,
toh ek upaay hai.”

“Main jua khelne mein
sabse tez hoon.”

“Yudhishthira ko
khelne ka shauk hai,
par kala nahi.”

“Agar use bulaaya jaaye,
toh woh mana nahi karega.”

“Main chaal se
uska sab kuch
jeet sakta hoon.”

Duryodhana turant bola—

“Pitaji,
Shakuni taiyaar hai.”

“Kripya
anumati de dijiye.”

Dhritarashtra ne kaha—

“Main pehle
Vidura se poochhna chahta hoon.”

Yeh sun kar
Duryodhana ghabra gaya—

“Agar aap Vidura se poochhenge,
toh woh mana kar denge.”

“Aur agar mana kiya,
toh main
jeevit nahi rahunga.”

Yeh sun kar
Dhritarashtra ka mann
hil gaya.

Unhone turant
sabha banwane ka aadesh diya.

Par andar hi andar
unhe galat hone ka
ehsaas tha.

Isliye
Vidura ko bhi bulaya.

Vidura aaye.
Unhone namrata se kaha—

“Rajaji,
yeh jua
vinash ka raasta hai.”

“Isse bhaiyon mein
bhed paida hoga.”

Par Dhritarashtra bole—

“Vidura,
shayad yeh sab
bhagya ne likha hai.”

“Main ise rok nahi paunga.”

“Tum jao
aur Yudhishthira ko
bulakar laao.”

Vidura ka dil
dukh se bhar gaya.

Unhone samajh liya—
Kali ka samay aa gaya hai.

Woh Bhishma ke paas gaye,
aankhon mein chinta liye.

🌱 Soft Moral (Simple & Deep):

Jalan buddhi ko andha kar deti hai.

Jua aur chaal
vinash ka darwaza hoti hai.

Jab galat ko bhagya keh diya jaaye,
tab patan shuru ho jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.11 – Section XLIX"):
            text1 = """ 
            Janamejaya ne poocha—

“Gurudev,
woh jua ka khel kaise hua
jisne Pandavon ko
itna dukh diya?”

“Kaun-kaun se raja wahan the?
Kaun mana kar raha tha,
aur kaun haan bol raha tha?”

“Mujhe sab kuch
detail mein sunna hai.
Kyunki wahi
duniya ke vinaash ka kaaran bana.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.11.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Sauti bole—

“Raja ke kehne par
Vyasa ji ke shishya
Vaisampayana ne
sab kuch sunaya.”

Vaisampayana bole—

“Raja Janamejaya,
agar tum sunna chahte ho,
toh dhyaan se suno.”

Dhritarashtra ne
Vidura ki baat sun kar
Duryodhana ko alag bulaaya.

Woh bole—

“Beta,
jua mat khelo.”

“Vidura gyaani hai.
Woh galat salah
kabhi nahi deta.”

“Jua
raajya ko tod deta hai.”

“Tumhare paas
sab kuch hai—
rajya, dhan, samman.”

“Phir bhi
tum itne dukhi kyun ho?”

Duryodhana ne kaha—

“Pitaji,
main jee raha hoon,
par jal raha hoon.”

“Dushman ki tarakki dekh kar
jo na jale,
woh insaan hi nahi.”

“Yudhishthira ki samriddhi
meri aankhon mein chubhti hai.”

“Poora sansaar
uske raaj mein lagta hai.”

“Sab raja
uske mahal mein
daas jaise rehte hain.”

“Sab khazana
uske paas aa raha hai.”

Duryodhana ne aage kaha—

“Pitaji,
mujhe unke yagya mein
ratna lene ka kaam diya gaya.”

“Mere haath thak gaye the,
par daan aana band nahi hua.”

“Jab main thak jaata,
log intezaar karte.”

“Maya daanav ne
unke liye sheeshe ka talaab banaya.”

“Maine use paani samajh liya.”

“Kapde upar kiye—
aur Bhima hans pada.”

“Woh hansi
aaj tak mujhe jalati hai.”

“Phir ek baar
main paani ke talaab mein gir gaya.”

“Is baar
Bhima aur Arjuna hase.”

“Draupadi bhi hansi.”

“Kapde badle gaye—
woh bhi mera apmaan bana.”

Duryodhana ki awaaz bhar aayi—

“Ek aur baar
maine darwaza samajh kar
deewar se takkar maar li.”

“Mera sir lag gaya.”

“Nakula aur Sahadeva
mujhe sambhaalne aaye.”

“Sahadeva ne
muskurate hue kaha—
‘Yahan se jaaiye.’”

“Bhima phir hansa.”

“Pitaji,
yeh sab yaadein
mera dil jala rahi hain.”

“Isi jalan mein
main jee raha hoon.”

🌱 Soft Moral (Simple & Deep):

Jalan jab mann mein bas jaati hai,
toh buddhi andhi ho jaati hai.

Apmaan ka bojh
galat raaste dikhaata hai.

Jua aur ahankaar
vinaash ka pehla kadam hote hain."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.12 – Section L"):
            text1 = """ 
            Duryodhana bola—

“Pitaji,
ab main aapko batata hoon
Pandavon ki woh daulat
jo maine apni aankhon se dekhi.”

“Woh khazana dekh kar
meri buddhi ghoom gayi.
Main apne aap ko
sambhaal nahi paaya.”

“Dharti ke har kone se
raja log
Yudhishthira ke liye
uphaar la rahe the.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.12.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Kamboja ke raja
bahut hi sundar chamde laaye.
Naram kambal laaye.
Sunehre dhaagon se bane hue.”

“Unhone
tez ghode diye.
Oont diye.
Gadhiyaan di.”

“Sab kuch itna achha tha
ki dekh kar hi
aankhen bhar jaati thi.”

“Bahut saare Brahman
gate par khade rahe.
Unke paas
bahut zyada daan tha.”

“Par jagah kam pad gayi,
isliye
unhe andar nahi jaane diya gaya.”

“Phir bhi
daan aata hi raha.”

“Samundar ke kinaare ke raja
bahut si dasiyan laaye.
Sundar vastra laaye.
Hiran ki chamdi laaye.”

“Van, pahaad,
door-door ke deshon se
log aaye.”

“Koi bakri laaya,
koi gai.
Koi shehad,
koi ratna.”

“Sab gate par hi
intezaar karte rahe.”

“Bhagadatta raja bhi aaye.
Unke saath
tez ghode the.
Sundar talwaarein thi.”

“Par unhe bhi
andar jaane ka mauka
baad mein mila.”

“Kuch log
ajeeb se the.
Kisi ki aankhen alag jagah par.
Kisi ke pair kam.”

“Par sab
Yudhishthira ke liye
uphaar la rahe the.”

“Valhika ke log
hazaaron gadhe laaye.
Tez daudne wale.
Sundar rang ke.”

“Unhone
oon ke kambal diye.
Kapde diye.
Chamdi diye.”

“Talwaarein,
kulhaadiyaan,
sugandh,
ratna—
sab kuch diya.”

“Shak, Tukhara,
aur anya jaatiyon ke raja
haathi laaye.
ghode laaye.
sone ke dher laaye.”

“Poorab ke deshon se
sundar rath aaye.
hathiyaar aaye.
sone-chandi se sajje hue.”

“Yeh sab dekh kar
mera mann jal utha.”

“Pitaji,
yeh woh daulat thi
jo maine dekhi.”

“Isi jalan ne
mere dil ko
shaant nahi rehne diya.”

🌱 Soft Moral (Simple & Deep):

Zyada daulat dekh kar
kamzor mann jal jaata hai.

Jalan aankhon ko nahi,
buddhi ko andha karti hai.

Jo doosron ki samriddhi se jalta hai,
woh apni shanti kho deta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.13 – Section LI"):
            text1 = """ 
            Duryodhana bola—

“Pitaji,
ab main aapko
aur bhi bataata hoon.”

“Yudhishthira ke paas
jo daulat thi,
woh sirf sone-chandi ki nahi thi.”

“Woh poori duniya ki
izzat aur samman thi.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.13.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Pahaadon ke paas rehne wale log
mitti ke neeche se nikla hua sona laaye.”

“Bans ke jhundon mein rehne wale
shehad laaye,
phoolon ki mala laaye.”

“Par unmein se
bahut se log
gate par hi ruk gaye.”

“Andar jagah hi nahi thi.”

“Uttar ke pahaadon se
Kirata log aaye.”

“Unke paas
chandan, agaru,
sona, chamda,
aur sundar jaanwar the.”

“Hazaaron daasiyaan bhi thi.”

“Par unhe bhi
intezaar karna pada.”

“Har disha se
raja aaye.”

“Koi Anga se,
koi Vanga se.”

“Koi Chola se,
koi Pandya se.”

“Sab apna-apna
shreshth uphaar laaye.”

“Haathi,
ghode,
rath,
kapde,
ratna,
aur sone ke dher.”

“Kuch raja
sirf tab andar ja paaye
jab unhone
hazaar-hazaar haathi diye.”

“Un haathiyon par
sunehri patte the.”

“Woh pahaad jaise majboot the.”

“Gandharva raja
tez ghode laaye.”

“Virata raja ne
hazaaron haathi diye.”

“Drupada ne
poora rajya tak
daan mein de diya.”

“Aur Krishna—
unhone Arjuna ke samman ke liye
hazaaron shreshth haathi diye.”

“Krishna aur Arjuna
ek hi aatma jaise the.”

“Jo Arjuna chahe,
Krishna poora kare.”

“Yudhishthira ke mahal mein
koi bhooka nahi tha.”

“Har jagah
khana bant raha tha.”

“Kahin anaaj tola ja raha tha,
kahin pak raha tha,
kahin baanta ja raha tha.”

“Har vyakti ke paas
vastra, bhojan,
aur aadar tha.”

“Hazaaron Brahman
roz wahan bhojan karte.”

“Yajnaseni pehle
sabko khilati,
phir khud khati.”

“Yahan tak ki
kamzor aur beemar log bhi
bhookhe nahi rehte.”

“Pitaji,
yeh sab dekh kar
mera mann toot gaya.”

“Mujhe laga—
meri zindagi bekaar hai.”

“Dusron ki itni samriddhi dekh kar
main jee nahi pa raha tha.”

“Isi jalan ne
mujhe andha kar diya.”

🌱 Soft Moral (Simple & Deep):

Daulat se zyada
samman logon ka dil jeetta hai.

Jalan jab badh jaaye,
toh sach bhi bojh lagne lagta hai.

Jo sabko saath lekar chalta hai,
usi ke paas asli samriddhi hoti hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.14 – Section LII"):
            text1 = """ 
            Duryodhana bola—

“Pitaji…
duniya ke sabse bade raja,
sabse gyaani log,
sabse pavitra log—
sab Yudhishthira ko
jhuk kar pranam kar rahe the.”

“Jo satya par chalte hain,
jo vrat rakhte hain,
jo Ved jaante hain,
jo dharm ko jeete hain—
sab unki seva karte hain.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.14.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Hazaaron gaaye aayi thi.
Har gaay ke saath
dudh ke bartan the.”

“Yeh sab
Brahmanon ko daan dene ke liye tha.”

“Rajasuya ke ant mein,
jab Yudhishthira ka
abhishek hua—
toh har raja
khud jal lekar aaya.”

“Kisi ne rath diya,
kisi ne ghode jode.”

“Kisi ne dhwaj pakda,
kisi ne kavach.”

“Kisi ne talwar,
kisi ne dhanush.”

“Sab milkar
Yudhishthira ki seva mein lage the.”

“Dhaumya Rishi,
Vyasa,
Narada—
sab mantra padh rahe the.”

“Pandav bhai
chamar hilate the.”

“Satyaki chhatra pakde tha.”

“Krishna khud
Yudhishthira ko snan kara rahe the.”

“Samudra se
Varun ka shankh aaya.”

“Us shankh se
snan hua.”

“Woh shankh dekh kar
main behosh ho gaya.”

“Poorab, paschim,
dakshin ke samudron se
log aa sakte hain.”

“Par uttar samudra
sirf pakshi hi dekh sakte hain.”

“Fir bhi…
Pandavon ka raaj
wahan tak phail chuka tha.”

“Wahan ke shankh bhi
yahan baj rahe the.”

“Jab sab shankh
ek saath baje—
mera sharir kaanp gaya.”

“Kuch raja gir gaye.”

“Mujhe bhi hosh nahi raha.”

“Aur us waqt…
Pandav,
Krishna,
Satyaki—
sab hans rahe the.”

“Unki hansi
mere dil mein
aag ban kar ghus gayi.”

“Arjuna ne
Brahmanon ko
sone ke singh wali
gaaye daan di.”

“Rajasuya poora hua.”

“Yudhishthira ko
aisa sukh mila
jo pehle kisi ko nahi mila.”

“Pitaji…
yeh sab dekh kar
mujhe laga—
jeena bekaar hai.”

“Mere andar
shanti hi nahi bachi.”

“Lagta hai jaise—
andha aadmi
jua bandhe.”

“Bade kamzor ho rahe hain,
chhote badhte ja rahe hain.”

“Main chaah kar bhi
is dukh se
baahar nahi aa pa raha.”

“Isi liye
main murjha gaya hoon.”

“Isi liye
main jal raha hoon.”

🌱 Soft Moral (Very Simple & Deep):

Jab doosron ki shanti
apne dil ko jala de,
toh dukh hi dukh bachta hai.

Sachchi samriddhi
daulat nahi,
logon ka prem hoti hai.

Jalan dheere-dheere
insaan ko andar se
kha jaati hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.15 – Section LIII"):
            text1 = """ 
            Dhritarashtra ne pyaar se kaha—

“Beta,
tum mere sabse bade putra ho.
Isliye meri baat dhyaan se suno.”

“Jo insaan jalan karta hai,
woh hamesha dukhi rehta hai.”

“Jalan
dil ko dheere-dheere
maar deti hai.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.15.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Yudhishthira
chhal nahi jaante.”

“Unke paas
utni hi sampatti hai
jitni tumhare paas.”

“Unke mitra
tumhare bhi mitra hain.”

“Woh kabhi
tumse jalan nahi karte.”

“Phir tum
unse jalan kyun karte ho?”

“Tum aur Pandav
barabar ho.”

“Phir
apne bhai ki cheez
chheen ne ka vichaar
kyun laate ho?”

“Isse ruk jao.”

“Shant ho jao.”

“Beta,
agar tum bhi
bade yagya ka maan chahte ho,
toh apna yagya karo.”

“Raja log
khud tumhare paas aayenge.”

“Daan bhi milega,
samman bhi.”

“Dusron ki cheez
chahna
bahut neecha bhav hota hai.”

“Jo apne paas jo hai
usmein santosh rakhta hai,
wahi sach mein sukhi hota hai.”

“Sachchi mahaanta
teen cheezon mein hoti hai—

Apne kaam mein mehnat

Dusron ki cheez par nazar na rakhna

Jo mila hai, uski raksha karna”

“Jo musibat mein bhi
hilta nahi,
jo vinamr rehta hai,
jo satark rehta hai—
uske paas
sampatti khud chal kar aati hai.”

“Pandav
tumhare apne haath jaise hain.”

“Apne hi haathon ko
kaatna
buddhimaani nahi hoti.”

“Daulat ke liye
ghar ke andar
aag mat lagao.”

“Apne bhaiyon se
jagda karna
bahut bada paap hai.”

“Tumhare purvaj
unke bhi purvaj hain.”

“Yagya mein daan do.
Jo mann chahe
achha kaam karo.”

“Khushi se jiyo.
Shaanti se jiyo.”

“Yahi jeevan ka
sahi raasta hai.”

🌱 Soft Moral (Simple & Clear):

Jalan se kabhi sukh nahi milta.

Santosh hi sabse badi daulat hai.

Apne logon ke saath ladkar
koi jeet nahi paata."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.16 – Section LIV"):
            text1 = """ 
            Duryodhana ne kaha—

“Pitaji,
sirf sun lene se
samajh nahi aata.”

“Jaise chamach
soup ko chhoota hai
par swaad nahi jaanta—
waise hi
bina kaam ki samajh
kuch nahi hoti.”

“Aap sab jaante ho,
phir bhi
mujhe rok rahe ho.”

“Hum dono
ek hi naav mein bandhe hain.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.16.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Kya aap
apna fayda bhool gaye ho?”

“Ya phir
aap mere viruddh ho?”

“Jo raja
sahi samay par kaam nahi karta,
uska rajya
doob jaata hai.”

“Jo aaj karna hai
use kal par chhodna—
yeh galat hai.”

“Rajaon ke niyam
aam logon jaise nahi hote.”

“Raja ko
hamesha
apna laabh dekhna chahiye.”

“Kshatriya ke liye
sirf jeet maayne rakhti hai.”

“Chahe raasta
achha ho ya bura.”

“Dushman ki chamakti hui
samriddhi ko chheen ne ke liye
har disha ko vash mein lana padta hai.”

“Hathiyaar
sirf kaatne ke liye nahi hote—
woh har tarah se
dushman ko haraane ka zariya hote hain.”

“Kaun dost hai,
kaun dushman—
yeh shakal se nahi,
kaam se tay hota hai.”

“Jo tumhe dukh deta hai,
wahi tumhara dushman hai.”

“Pitaji,
asantosha hi
tarakki ki jad hai.”

“Isliye
main asantosht rehna chahta hoon.”

“Jo zyada chahata hai,
wahi aage badhta hai.”

“Shaant rehne wala raja
zameen nigal jaati hai.”

“Jaise saanp
bil mein rehne wale
jeev ko kha jaata hai.”

“Chhota dushman bhi
agar badhne diya,
toh ped ko
deemak ki tarah
andar se kha jaata hai.”

“Pandav roz badh rahe hain.”

“Hum wahi ke wahi hain.”

“Isliye
mujhe unki samriddhi chahiye.”

“Ya toh
main woh sab paa loonga—
ya phir
yuddh mein gir jaaunga.”

“Ab mujhe
jeevan ki parvah nahi.”

🌱 Soft Moral (Warning for Children, very simple):

Jab laalach buddhi par haavi ho jaaye,
toh dharm dhundhla ho jaata hai.

Asantosha mehnat bhi bana sakta hai,
aur vinaash bhi.

Gussa aur jalan
insaan ko dheere-dheere
galat raaste par le jaate hain."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.17 – Section LV"):
            text1 = """ 
            Sakuni bola—

“Raja,
jo samriddhi tumhe dukh de rahi hai,
main woh tumhare liye
cheen lunga.”

“Bas Yudhishthira ko bula lo.”

“Jise khel aata ho,
woh bina chot khaye
jeet jaata hai.”

“Jua mera dhanush hai.
Paase mere teer.”

“Khel ki chaupat
mera rath hai.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.17.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Duryodhana turant bola—

“Pitaji,
Sakuni taiyaar hai.”

“Bas aap
anumati de do.”

Dhritarashtra bole—

“Main pehle
Vidura se poochunga.”

Duryodhana gusse se bola—

“Vidura hamesha
Pandavon ka bhala chahta hai.”

“Woh aapka mann
badal dega.”

“Do logon ki salah
kabhi ek jaisi nahi hoti.”

“Jo hamesha darr ke kaaran
ruk jaata hai,
woh keede jaisa
khud hi khatam ho jaata hai.”

“Bimari ya maut
yeh nahi dekhti
ki samay achha hai ya bura.”

“Jab tak jaan hai,
tab tak kaam kar lena chahiye.”

Dhritarashtra ne thande swar mein kaha—

“Majboot logon se dushmani
mujhe theek nahi lagti.”

“Dushmani khud
ek hathiyaar ban jaati hai.”

“Tum jis cheez ko
sukh ka darwaza keh rahe ho,
wahi yuddh ka beej hai.”

“Jab yeh shuru hota hai,
toh talwaar aur teer
khud ban jaate hain.”

Par Duryodhana ruka nahi—

“Jua purane zamane se chala aa raha hai.”

“Ismein
na khoon bahata hai,
na talwaar chalti hai.”

“Isse toh
swarg ka darwaza khulta hai.”

“Pandav aur hum
barabar ho jaayenge.”

“Isliye
juye ka khel hone do.”

Dhritarashtra thak kar bole—

“Tumhari baatein
mujhe theek nahi lagti.”

“Par jao,
jo tumhe theek lage karo.”

“Par yaad rakhna—
tumhein iska
pachtava hoga.”

“Galat raaste se
kabhi bhavishya ka sukh
nahi milta.”

“Vidura ne
yeh sab pehle hi dekh liya tha.”

“Yeh sab
bhagya ka likha hai.”

Vaisampayana kehte hain—

Dhritarashtra ne
bhagya ko sab kuch maan liya.

Aur phir
apne putra ki baat maan kar
aadesh diya—

“Turant
ek bhavya sabha bhavan banao.”

“Hazaar khambhon wala.
Sheeshe jaisa chamakta.”

“Sone aur neelam se sajja hua.”

“Sau darwaaze hon.”

“Bahut bada ho.”

Hazaaron kaarigar
lag gaye.

Jaldi hi
sabha tayaar ho gayi.

Sundar.
Chamakti hui.
Ratnon se bhari.

Phir Dhritarashtra ne
Vidura ko bulaya aur kaha—

“Jaakar
Yudhishthira ko bula lao.”

“Unke bhaiyon ke saath.”

“Woh meri sabha dekhein.”

“Aur phir
dostana juye ka khel ho.”

🌱 Soft Moral (Bahut Saral, Bachchon ke liye):

Galat salah jab mann ko bha jaaye,
toh buddhi thak jaati hai.

Jua muskaan ke saath aata hai,
par aansuon ke saath jaata hai.

Jab koi bhagya ke naam par
galat faisla karta hai,
toh kahani ka andhera shuru hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.18 – Section LVI"):
            text1 = """ 
            Vaisampayana bole—

Raja Dhritarashtra
apne bete ke mann ko samajh chuke the.
Unhe lag raha tha
ki bhagya ko
koi taal nahi sakta.

Par Vidura—
jo bahut buddhimaan the—
chup nahi rahe.

Unhone dhire par spasht shabdon mein kaha—

“Raja,
mujhe aapka yeh faisla
bilkul theek nahi lagta.”"""
            create_image_text_layout("attached_assets/chapter2/2.7.18.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Is raaste par mat chaliye.”

“Mujhe darr hai
ki yeh khel
hamare poore vansh ka
vinaash ban jaayega.”

“Jab bhai
ek-doosre se ladne lagen,
toh ghar toot jaata hai.”

“Juya
sirf khel nahi hota,
yeh phoot ka beej hota hai.”

Par Dhritarashtra ne
gambhir swar mein kaha—

“Vidura,
agar bhagya saath hoga
toh kuch bura nahi hoga.”

“Yeh poori duniya
vidhaata ke niyam se chalti hai.”

“Koi bhi
poori tarah swatantra nahi.”

“Isliye
jo likha hai
wahi hoga.”

“Tum jao,
aur Yudhishthira ko
mere aadesh se
yahaan le aao.”

Vidura chup ho gaye.
Unke mann mein
ashanka thi.
Par kartavya
unhe chalne par
majboor kar raha tha.

Aur yahin se
kahani ka
sabse kathin mod
shuru hota hai.

🌱 Soft Moral (Bachchon ke liye, bahut simple):

Jo samjhaata hai,
woh hamesha dushman nahi hota.

“Bhagya” keh kar
galat faisla lena
sahi baat nahi hoti.

Jab buddhi ki baat
nahi suni jaati,
toh dukh ka raasta
khul jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.19 – Section LVII"):
            text1 = """ 
            Vaisampayana ne kaha—

Raja Dhritarashtra ka aadesh
Vidura ke mann ke viruddh tha.
Par kartavya ke kaaran
Vidura chal pade.

Tez ghodon ke saath
woh Pandavon ki nagari pahunche.
Buddhimaan Vidura
seedhe Yudhishthira ke mahal gaye."""
            create_image_text_layout("attached_assets/chapter2/2.7.19.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yudhishthira ne
Vidura ka swagat kiya.
Pyaar se poocha—

“Kshatta,
aapka mann udaas kyun lag raha hai?”

“Kya sab theek hai
Hastinapur mein?”

Vidura bole—

“Sab theek hai, raja.”

“Dhritarashtra ne
naya sabha bhavan banwaya hai.”

“Woh chahte hain
aap bhaiyon ke saath aakar dekhein.”

“Phir
ek dostana juye ka khel ho.”

Yudhishthira ne
shant swar mein kaha—

“Vidura,
juya jhagda laata hai.”

“Jo yeh jaanta ho,
woh khelne ko
kaise raazi ho?”

“Aap hi batao,
humein kya karna chahiye?”

Vidura bole—

“Main jaanta hoon
juya dukh ka mool hai.”

“Par raja ne
aadesh diya hai.”

“Jo hitkar ho,
wahi kijiye.”

Yudhishthira ne poocha—

“Kaun-kaun se
juari wahan honge?”

Vidura ne kaha—

“Sakuni,
aur kuch aur
chalak khelne wale.”

Yudhishthira kuch der chup rahe.
Phir bole—

“Main juya pasand nahi karta.”

“Par agar
mujhe sabha mein
chunauti di gayi,
toh main mana nahi kar sakta.”

“Yeh mera vrat hai.”

Yeh keh kar
Yudhishthira ne
yatra ki taiyaari ka aadesh diya.

Agli subah
Pandav bhai,
Draupadi aur parivar ke saath
Hastinapur chal pade.

Chalte hue
Yudhishthira bole—

“Bhagya jab
aankhon ke saamne girta hai,
toh buddhi bandh jaati hai.”

Hastinapur pahunch kar
Pandavon ne
sab badon ko pranam kiya.

Gandhari ne
aashirvaad diya.

Dhritarashtra ne
pyaar se
unke sir soonghe.

Sab khush hue.

Pandavon ko
sundar kaksh diye gaye.

Raat shanti se beeti.

Subah
sabha bhavan mein
sab taiyaar the.

Aur wahan—
juye ka khel
shuru hone wala tha.

🌱 Soft Moral (Bahut Saral):

Kartavya aur bhagya
kabhi-kabhi
galat raaste par le jaate hain.

Achhe log bhi
galat khel mein
fas sakte hain.

Kahani ka andhera
yahin se gahra hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 2.7.20 – Section LVIII"):
            text1 = """ 
            Vaisampayana bole—

Dhritarashtra ka aadesh
Vidura ke mann ko pasand nahi tha.
Phir bhi kartavya ke liye
Vidura chupchaap chal pade.

Tez aur shaant ghodon ke saath
woh Pandavon ki nagari ki taraf gaye.
Raste bhar
unka mann bhaari tha,
par chehra shant."""
            create_image_text_layout("attached_assets/chapter2/2.7.20.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Pandav nagar pahunch kar
Vidura seedhe
Yudhishthira ke mahal gaye.
Mahal Indra ke ghar jaisa lag raha tha.
Brahmanon se ghira hua.

Yudhishthira ne
Vidura ka aadar se swagat kiya.
Phir pyaar se poocha—

“Kshatta,
aap kuch udaas lag rahe ho.
Sab theek toh hai na?”

“Kya Hastinapur mein
sab shanti se hai?”

Vidura bole—

“Raja Dhritarashtra theek hain.
Unke putra bhi theek hain.”

“Unhone naya sabha-bhavan banwaya hai.”

“Unki ichchha hai
aap bhaiyon ke saath wahan aayen.”

“Sabha dekhen
aur phir
ek dostana juye ka khel ho.”

Yudhishthira ne
gehri saans li.
Phir bole—

“Vidura,
juya hamesha jhagda laata hai.”

“Jo yeh jaanta ho,
woh khelne ko
kaise taiyaar ho?”

“Aap batao,
humein kya karna chahiye?”

Vidura ne kaha—

“Main bhi jaanta hoon
juya dukh ka mool hai.”

“Maine raja ko mana kiya tha.”

“Par raja ne
mujhe bheja hai.”

“Ab aap hi sochiye
jo hit mein ho.”

Yudhishthira ne poocha—

“Wahan kaun-kaun khelne wale hain?”

Vidura bole—

“Sakuni,
jo dice mein bahut chalak hai.”

“Uske saath
aur bhi kuch
tedhe khelne wale hain.”

Yudhishthira kuch pal chup rahe.
Phir shaant swar mein bole—

“Main juya nahi chahta.”

“Par agar sabha mein
mujhe chunauti di gayi,
toh main mana nahi karunga.”

“Yeh mera vrat hai.”

Itna kehkar
Yudhishthira ne
yatra ki taiyaari ka aadesh diya.

Agli subah
Pandav bhai,
Draupadi
aur parivaar ke saath
Hastinapur ke liye nikle.

Chalte hue
Yudhishthira bole—

“Jab bhagya saamne aa jata hai,
toh buddhi bandh jaati hai.”

“Insaan
bhagya ke dhage se
bandh jaata hai.”

Hastinapur pahunch kar
sab badon ko pranam hua.
Gandhari ne aashirvaad diya.
Dhritarashtra ne pyaar se
sir chhoo kar ashirvad diya.

Sab khush dikh rahe the.

Pandavon ko
sundar kamre mile.
Raat geet aur shanti mein beeti.

Subah
sabha bhavan mein
sab taiyaar the.

Aur wahin se
ek dukh bhari kahani
shuru hone wali thi…

🌱 Soft Moral (Bahut Saral):

Galat khel
achhe logon ko bhi
dukh ki taraf le ja sakta hai.

Kartavya aur zidd
kabhi-kabhi
buddhi par bhaari ho jaate hain.

Kahani yahin se
andhera mod leti hai."""
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

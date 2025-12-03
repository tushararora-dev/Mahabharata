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
            text1 = """ 
Om!
Sabse pehle, Sauti—Lomaharshana ka putra Ugraśravā—
sar jhukakar pranām karta hai Nārāyaṇa, Nara,
aur Sarasvatī devi ko,
aur phir ek shabd bolta hai—
“JAYA”
(jo is mahāgrantha ka hriday hai).

🌿 Naimishāraṇya – tapasviyon ka van, yagya ka ghar

Barah saal tak chalne wale Saunaka Kulapati ke yagya ke beech,
Naimisha ke tapasvi, Muni-lok, maun bhang karke
lotus-aankhon waale Sauti ka swāgat karte hain.

Sauti un Rishiyon ke saamne vinamra hokar baith jata hai—
thaka hua, par shraddha se bhara hua.

Ek Rishi puchte hain:

“Kahan se aaye ho, Sauti? Kya dekhkar aaye ho? Humein sab batao.”"""
            create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1, layout="side", image_position="left")

            text2 = """ 
📜 Sauti ka uttar — Vyas ki kahani lekar aaya hoon

Sauti kehta hai:

“Hey Muni-varo…
Main abhi abhi us mahān sabha se aa raha hoon
jahaan Maharishi Vyāsa dwara rachit
Mahābhārata ko
unke shishya Vaiśampāyana ne
Raja Janamejaya ke sarpa-yagya me sunaya.

Phir main tīrthon me bhatakta hua
Samantapañcaka pohoncha—
wahin jahan Kuruvansh aur Pandavon ki
maha-yuddha shuru hui thi.

Aur ab, aap sab ko dekhne ki ichchha se
yahaan aa gaya hoon.”

Phir poochta hai:

“Kaho, aap kya sunna chahte ho?
Purānon ki kathayein?
Purusharthon—Dharma, Artha, Kāma—ki baat?
Ya Vyas munirachit woh param itihaas…
Mahābhārata?”

🔱 Rishiyon ka uttar: “Humein Bharata sunaao!”

Rishiyon ne kaha:

“Vyas ji ka rachit Bharata—
jise devtā, brahmarshi sab sun chuke—
wah itihaas sarvashreshth hai.

Usme Veda ka saar, dharma ka marg,
rajneeti, niti, gyaan, yog sab samahit hai.

Humein wahi sunao—
waise hi jaise Vaiśampāyana ne Janamejaya ko sunaya.”

🌌 Sauti ka pranam— aur srishti ka gahan rahasya

Sauti bolta hai:

“Main sabse pehle pranām karta hoon
Ishaan, Brahma, Hari,
jo sabke mool, sab mein vyāpt,
jo dikhte bhi hain, adrusya bhi hain,
jo sab kuchh hain aur sabke pare bhi.

Ab main sunaoonga
Vyas muni ke pavitra vichaar.”

🌏 Srishti ki utpatti — Mahā-Anda, Brahma, Devgan

Sauti kahani shuru karta hai:

“Jab jagat andhkaar me tha—
tab ek maha-aṇḍa (cosmic egg) utpann hua,
jise Mahādivya kehte hain.

Usi se Brahma nikle—
pratham Prajāpati.

Unse Suraguru, Sthānu (Shiva ka ek roop),
21 Prajāpati, Manu, Vashishtha, Daksha,
Aur saare Dev—
Aditya, Vasu, Ashvinikumār, Yaksha, Pitri,
Brahmarshi aur Rajarshi.

Phir
akāsh, jal, dharti, vāyu, kaal,
ritu, mahine, paksha, din-raat—
sab is rachna chakra me bane.

Saara jagat—jo dikhta hai aur jo adrusya hai—
Yug ke ant me vishram karta hai,
phir ek naye yug me phir se utpann hota hai.”

👑 Dev vansh, Prajapati aur Manav kul ki shuruaat

Sauti batata hai Devon ki kulgathha—
33,333 devtā,
phir unse rajvansh—
Kuru, Yadu, Bharata, Ikshvāku—
sab isi pranvansh se nikle.

Vyāsa ne Veda, Vedang, Purāna, Shastra, Dharma,
samajh, yug, sansar, sab kuchh likha.

Phir Vyāsa sochne lage:

“Is granth ko dharti par kaun likhega?”

🌟 Brahma ka avatarn — aur Mahābhārata ka sankalp

Vyāsa ki chinta dekhkar
Brahma ji swayam bhogol ke prabhu
unke paas aaye.

Vyāsa ne pranām kiya.
Brahma ne kripa se kaha:

“Tumne jo granth rachit kiya hai—
dharma ka saar, vedon ka tattva,
purusharth ka marg—
yeh manav ko mukti dene wala hai.”

Vyāsa ne bola:

“Par prabhu…
isse likhne waala koi nahi mil raha.”

Yahaan se shuru hoti hai
Mahābhārata likhne ki divya yojnā—
(jisme aage Brahma Ganesh ko pathayenge,
jo Vyāsa ka lekhak banega)."""
            create_image_text_layout(text_content=text2, layout="full")

                # Section 1.1.2
        with st.expander("Section 1.1.2"):
            text1 = """ 
🌼 Brahmā ka Aadesh: ‘Yeh granth kabhi tulya na hoga’

Vyāsa apne rachna ke liye chintit baithe the
tab Brahmā jee swayam prakat hue—
pralay ke surya ki tarah tejomay.

Unhone Vyāsa se kaha:

**“Vyas, tum dev-vijnān ke rāj ho.
Jo granth tumne socha hai—
woh ek kavya hoga, aur aisa hoga ki
koi kavi iski barabari na kar payega.
Jaise ek gṛhastha-āśrama ki mahima
baaki āśramon se adhik hoti hai
waise hi tumhara granth sabse upar hoga.

Isse likhvāne ke liye
Ganesh ji ka dhyān karo.””

Itna kehkar Brahmā apne lok ko laut gaye."""
            create_image_text_layout("attached_assets/chapter1/1.1.2.jpg", text1, layout="side", image_position="left")

            text2 = """ 
🐘 Ganesh ka āgamana — aur anokha shart

Vyāsa ne man mein Ganesh ji ka smaran kiya
aur vighna-harata Ganapati turant prakat ho gaye.

Vyāsa ne vinamr hokar kaha:

“Hey Ganaon ke Prabhū!
Main jo Mahābhārata rach raha hoon,
kripya uske lekhak ban jao.”

Ganesh ji bole:

“Main likhunga—
lekin meri ek shart hai:
Meri kalam ek pal ke liye bhi rukni nahi chahiye.”

Vyāsa muskuraye:
“Aisa hi ho.
Par jab bhi koi shabd ya arth
tumhe samajh na aaye,
toh tum likhna rok dena.”

Ganesh ji ne ‘Om!’ कहकर shart sweekar ki.

Phir likhna shuru hua.

🔱 Vyāsa ke ‘granthi-daar’ shlok — Ganesh ka ek pal rukna

Vyāsa jaise hi bolte gaye,
Ganesh ji likhte gaye—
tez, nirav, anivārya.

Par Vyāsa, bhavishya ke paathakon ki buddhi jagane ke liye,
kabhi kabhi shlok ko granthi-daar,
gahan, sūkshma arthon se bhar dete—
aisa ki Ganesh ji ko pal bhar sochna padta.

Par Vyāsa rukte nahi the—
pehle hi agla shlok rach dete.

Sauti kehta hai:

“Un 8800 gahan shlokon ko
aaj tak koi samjha nahi—
na Suka, na Sanjaya, na koi aur.
Vyāsa aur Ganesh hi unka rahasya jaante hain.”

🌞 Mahābhārata ka tej — andhakaar mitaane wala

Sauti aage batata hai:

“Mahābhārata andhkaar me aankhon ka
anjan ban kar udgātha hota hai.
Jo manushya gyaan se vanchit hai,
ye granth uska tam mita deta hai.”

Jaise:

Surya andhkaar mitata hai

Purnima ka chand kamal ko khilata hai

Itihas ka deep jagat ko prakāshit karta hai

waise hi
Mahābhārata jeevan ka marg dikhata hai.

🌳 Mahābhārata ek Vriksha — jisme sab kuchh samaaya hai

Sauti ek divya upamaa deta hai:

Mahābhārata ek bada vriksha hai:

Contents (Anukramanika) — beej

Pauloma & Astika — jad

Sambhava — tan

Sabha & Aranya Parva — shakha-parindon ki baithak

Arani Parva — bandhan aur granthi

Virata & Udyoga — saar-rasa

Bhishma Parva — mukhya shaakha

Drona Parva — patte

Karna Parva — phool

Shalya Parva — phoolon ki sugandh

Stri & Aishika — chhaya

Shanti Parva — anmol phal

Ashvamedhika — amrit-rasa

Āshramavāsika — sthaan

Mausala — Vedon ka saar

Yeh vriksha kabhi shushk nahi hota.
Kabhi rukta nahi.
Kabhi marta nahi.

👑 Vyāsa aur Kuru vansh— Bharata ka manav-roop

Sauti aage batata hai:

Vyāsa ne Dhritarashtra, Pandu, Vidura ko janm diya
(niyoga pratha ke dwara).

Jab woh bade hue aur chale gaye,
tab unhone Bharata ka paath Janamejaya ke yahaan sunaya.

Vaisampayana ne ise yagya ke madhya paath kiya.

Vyāsa ne:

Gandhari ki pavitrata,

Vidura ki buddhi,

Kunti ki dridhta,

Pandavon ka dharma,

Kauravon ki durbuddhi,

Krishna ki divyata

sab kuchh sthir-rup se darshaya.

🌍 Mahābhārata ki sankhya — manusya aur dev lokon me

Vyāsa ne teen roop banaye:

1️⃣ Mool Bharata (24,000 shlok)
2️⃣ Sankshipt roop (150 shlok) — pehle Suka ko
3️⃣ Vishaal roop (6 lakh shlok):

Dev lok me — 3 lakh

Pitri lok me — 1.5 lakh

Gandharva lok me — 1.4 lakh

Dharti par — 1 lakh

Narada ne devatāon ko sunaya,
Devala ne pitron ko,
Suka ne Yaksha-Gandharvon ko,
Vaisampayana ne manushyon ko.

Aur Sauti kehta hai:
“Main bhi 100,000 shlok sunata hoon.”

🌺 Pandavon ka pravesh — Hastinapur ka deep jag gaya

Pandavon ka pravesh Hua—
nagar me utsav phoot padā:

Pushpo ki varsha hui

Ghanton, shankhon ki dhwani hui

Dev-lok tak unka swagat gaya

Yudhishthir ka dharma, Arjun ki veerta,
Bhima ka bal,
Nakula-Sahadev ki vinamrata—
sabko akarshit karti thi.

🎯 Draupadi swayamvar — Arjun ka vijay

Arjun ne dhanush ka divya chamatkar dikhakar
Krishnaa (Draupadi) ko jeeta—
aur dhanurvidya me jagat me apratikhya ban gaye.

Pandavon ne Jarsandha ko maara,
Rajasuya ki mahāyagya kiya,
jahan Duryodhana ne
Pandavon ki vaibhav ko dekhkar
jalan se apne hriday ko zehar bana diya.

🎲 Jua, anyaay, aur Mahāyudh ka aarambh

Dyut-krida hui—
Krishna naraaz the par ruk nahi sake.
Vidura, Bhishma, Drona sab virodh me the—
par Dhritarashtra ne Duryodhana ko rokna mana kar diya.

Aur ant me—
adharma ka phal
Mahābhārata ka yuddh bana."""
            create_image_text_layout(text_content=text2, layout="full")

                # Section 1.1.1
        with st.expander("Section 1.1.3"):
            text1 = """ 
⭐ Dhritarashtra ka Dukh Bhara Mann

Dhritarashtra ne jab Pandavon ki jeet ki khabar suni,
toh unka dil toot gaya.
Unko yaad aaya—
Duryodhana, Karna aur Shakuni ke bure iraade…
aur woh Sanjaya ko dheere se bole:

“Sanjaya, meri baat dhyaan se suno.
Main kabhi yudh nahi chahta tha.
Main kabhi apni vansh (family line) ka naash dekhna nahi chahta tha.”

Wo ruk kar bole:

“Main andha hoon, buddha hoon…
par maine kabhi Pandav aur Kaurav me bhed-bhav nahi kiya.
Mere bachche ziddi the…
aur mujhe kamzor samajh kar mujhe hi dukh dete the.”

Unki aawaaz bharayi hui thi."""
            create_image_text_layout("attached_assets/chapter1/1.1.3.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ “Mere har sapne toot rahe the…” — Dhritarashtra ke ‘I had no hope’ pal

Dhritarashtra Sanjaya ko ek-ek karke woh saare pal ginaate hain
jahan unko laga:

“Ab hamari haar nishchit hai.”

Kahani ko bachchon jaisi halki Hinglish me samjhte hain:

🌼 1. Arjun ne Draupadi ko jeeta

Jab Dhritarashtra ne suna ki Arjun ne dhanush todkar
nishaan par teer maara
aur sab rajaon ke saamne Draupadi ko jeet liya—

“Tab mujhe laga—hamari koi umeed nahi.”

🌼 2. Arjun ne Subhadra ko swayam le gaya

Jab pata chala Arjun ne Subhadra ko apne saath utha liya
aur Krishna–Balarama ne bhi dosti banaye rakhi—

“Meri umeed khatam.”

🌼 3. Arjun ne Indra ki baarish rok di

Arjun ne apne dev-astra se Indra ki baarish rok di
aur Agni dev ko Khandav van de diya—

“Tab bhi laga hum nahi jeetenge.”

🌼 4. Pandav laakh ke ghar se bache

Pandavon ke laakh ke ghar (wax-house) jalne ke bawajood
woh bach gaye—

“Tab bhi koi umeed na bachi.”

🌼 5. Pandav–Panchal ek ho gaye

Arjun ke Draupadi swayamvar ke baad
Panchalon ka saath milna—

“Hamari tabahi nishchit.”

🌼 6. Jarasandha ko Bhima ne haathon se phaad diya

Bhima ne Magadh ke maha-yoddha Jarasandha ko
khali haathon se maar diya—

“Tab mujhe pata chal gaya ki hamare din khatam hain.”

🌼 7. Pandavon ka Rajasuya yajna

Pandav itne samarth ho gaye ki
poori dharti ke rajaon ko jeet kar yajna kiya—

“Hamari haar tabhi pakki ho gayi.”

🌼 8. Draupadi ka sabha me apmaan

Jab Dhritarashtra ko pata chala ki
Draupadi ko ek vastra me ghaseet kar laya gaya,
aur Dushasan kitna bhi kheenchta raha
par vastra anant (endless) ho gaya—

“Mere mann ne kaha—yeh anyay kabhi nahi bachega.”

🌼 9. Pandavon ka vanvaas aur tapasya (penance)

Pandavon ka tapasvi jeevan—
unke saath brahman aur snataka (trained students)—

“Tab bhi umeed nahi.”

🌼 10. Arjun ka divya-astron ka prapt karna

Shiva se Pashupat astr,
Indra se dev-astr,
Rakshason ko maar kar wapas aana—

“Hum jeet hi nahi sakte.”

🌼 11. Gandharvon se Duryodhan ka pakda jaana

Duryodhan ka gandharvon ne pakad lena
aur Arjun ke haath se chhutna—

“Umeed aur zyada kam ho gayi.”

🌼 12. Virat yudh me Arjun ek hi rath me sabko hara deta hai

Ek hi rath se poori Kaurav sena ko hara dena—

“…phir se mann me andhera chha gaya.”

🌼 13. Krishna–Arjuna ko Nara–Narayana bataya gaya

Narada ne kaha ki Krishna–Arjuna
Nara–Narayana (godly pair) hain—

“…tab to yudh ka parinaam pehle hi likha tha.”

🌼 14. Krishna ka Vishvaroop

Jab Krishna ko qaid karne ki sochi
aur unhone poora brahmand sharir me dikha diya—

“Tab mujhe laga hum paap me doob chuke hain.”

🌼 15. Bhishma ka na marna Pandavon ko

Bhishma roz 10,000 yodhdha maar rahe the
par Pandav ko ek bhi nahi—

“Tab maine maan liya, humari haar tai hai.”

🌼 16. Bhishma ka swayam apni mrityu ka upaay batana

Jab Bhishma ne swayam bataya ki unko kaise haar sakte hain—
aur Pandavon ne usse kiya—

“Ab bilkul umeed nahi rahi.”

🌼 17. Arjun ne Bhishma ko shikhandi ke peechhe se gira diya

Bhishma ko teeron ki shayya par girte dekh
Dhritarashtra ke mann me akhri roshni bhi chali gayi.

🌼 18. Drona ka Ashvatthama-jhoot par girna

Drona ka man toot jana,
aur unka marna—

“Umeed gayi.”

🌼 19. Abhimanyu ka ghera kar ke maarna

Apne veer putra-jaise Arjun ke bete ko
anuchit (unfair) gherabandi me maarna—

“Is paap ka phal hum bharenge.”

🌼 20. Ghatotkacha ka marna aur Karna ka Shakti astr barbaad hona

Karna ka ek-matra Amogh (infallible) astr
Ghatotkacha par chal jana
(jo Arjun ke liye tha)—

“Tab maine jaana ki Karna ka samarthya bhi ab kam ho gaya.”

🌼 21. Duryodhana ka pani me chhipna, phir gada-yudh me girna

Duryodhan ka jalashaya me chhipna,
phir Bheem ka gadaa yudh me uski jangha todna—

“Yeh sun kar mera bas mann toot gaya.”

🌼 22. Ashvatthama ka raat me bacchon ka nishthur (cruel) hatya karna

Pandavon ke soye hue putron ka hatya—
mahapaap.

🌼 23. Uttara ke garbh me prahaar aur Kripa–Vyasa ka shaap

Ashvatthama ke agni astra se
Uttara ke garbh ko lagna
aur phir Krishna ka raksha karna.

🌼 24. Ant me bas 10 log bachna

18 akshauhini sena me se
sirf 10 log jeevit rahe:

Pandav – 5

Krishna – 1

Saatyaki – 1

Kritavarma – 1

Ashvatthama – 1

Kripacharya – 1

Is maha-nasha ko sunkar
Dhritarashtra soya hua sa bolte hain:

“Sanjaya… mere charon aur andhera hi andhera hai.”"""
            create_image_text_layout(text_content=text2, layout="full")


                # Section 1.1.1
        with st.expander("Section 1.1.4"):
            text1 = """ 
⭐ Dhritarashtra ka Dard

Sauti bolte hain:

Dhritarashtra apni kismet par royā…
Itna roya ki behosh jaise ho gaya.
Thoda sambhalne ke baad usne Sanjaya se kaha:

“Sanjaya… jo kuchh bhi ho chuka hai,
mera jeena bekaar lag raha hai.
Mera mann chahta hai main abhi apni zindagi khatam kar doon.”

⭐ Sanjaya ka Shant Aur Gyaani Jawaab

Sauti kehte hain:

Sanjaya — jo bahut buddhimaan tha —
ne rone-dhone se bhare raja Dhritarashtra ko
bahut gahri baatein kahi.

Woh bola:"""
            create_image_text_layout("attached_assets/chapter1/1.1.4.jpg", text1, layout="side", image_position="left")

            text2 = """ 
🌺 1. “Raja, aap ne un sab veero ke baare me suna hai…”

“Aapne suna hai woh mahaan rajaon ke baare me
jinhe Ved-Vyasa aur Narada ji ne yaad kiya—
jo duniya jeet kar yagna kiye,
daan diya,
aur ant me sab ko samay ne hi nigal liya.”

Sanjaya ek-ek kar ke un mahan rajaon ke naam batata hai:

Saivya, Srinjaya, Suhotra, Rantideva, Kakshivanta,
Bhagiratha, Gaya, Bharata, Raghu, Ikshvaku,
Ram (Dasharatha-putra), Yayati…

…aur hazaaron–laakhon dusre raja,
jo shaktishaali the,
dharma ke rakshak the,
janata ke pyare the—

“Un sab ko bhi samay ne hi maar diya, raja.”

🌺 2. “Aapke bete unke jaise achchhe nahi the.”

Phir Sanjaya dheere se par sacchai se kehta hai:

“Par aapke bete to un rajaon jaise sadaachari (noble) nahi the.”
“Woh to lalchi, gusse wale aur dusht (evil) the.”

🌺 3. “Jo hona tha, woh hota hi.”

Sanjaya ke shabdon me gyaan tha:

“Raja, jo hona hota hai,
use koi rok nahi sakta.
Koi bhi apni kismat ki likhi raah se bhaag nahi sakta.”

“Sab kuchh kaadta, banata, mitaata—
SAMAY hi hai.”

Samay hi sab ko banata hai.

Samay hi sab ko tod deta hai.

Samay hi sab ko sula deta hai.

Samay hi kabhi nahi sota.

“Jab sab so rahe hote hain,
tab bhi sirf Samay hi jaagta rehta hai.”

⭐ Dhritarashtra ka Dil Shant Hota Hai

Sauti kehte hain:

Sanjaya ki itni saari samajh bhari baatein sun kar
Dhritarashtra ka mann dheere dheere shaant ho gaya.
Dukh ab bhi tha,
par uss dukh me samajh aa gayi.

🌟 Mahabharata ka Mahatva – Kahani ka Antim Sandesh

Sauti phir batate hain Vyasa ji ka gyaan:

📘 Mahabharata padhna ek punyai ka kaam hai.

Ek shlok ka bhi path kare → paap dhul jaate hain.

Roz sune → dirghāyu aur yash milta hai.

Shraddha me Brahmanon ko sunaye → pitron ko sada ke liye trupti milti hai.

📘 Mahabharata sabhi granthon se bhari hai.

Swarg me devtaon ne:

ek taraf chaar Veda rakhe,

ek taraf Mahabharata…

…aur Mahabharata bhaari nikla.

Isiliye ise “Mahā–Bharata” kaha gaya —
“Sabse bada, sabse gahra granth.”

🌟 Antim Paath

Sauti kehte hain:

“Jo Mahabharata ka arth samajh le,
uska jeevan pavitra ho jata hai.”

“Tap, daan, vidya—
sab pavitra hain…
par jab inka durupyog hota hai,
tabhi bure hote hain.”"""
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

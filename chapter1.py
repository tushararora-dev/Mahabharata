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
            text1 = """ 
Rishiyon ne Sauti se poocha:

“O Suta-putra, tumne Samanta-Panchaka naam ka ek sthaan bataya.
Humein uska poora aur saaf varnan sunna hai.”

🌿 Samanta-Panchaka ki Kahani

Sauti bola:

“Suno, o Brahmano.
Main tumhe us pavitra jagah ka itihaas batata hoon.”

Treta aur Dwapara ke beech,
Jamadagni putra Parashurama, jo shastron ka maha-veer tha,
apne upar hue anyaayon se ghayal hokar
Kshatriyaon ko baar-baar maarte rahe.

Unhone pura vansh lagbhag khatam kar diya.

Jab unka krodh apne charam par tha,
unhone Samanta-Panchaka me
paanch khoon ke talaab bana diye.

Un khoon se bhare talaabon me khade hokar
unhone apne pitron ko
rakta-tarpan (blood-offering) kiya.

Tab unke purvaj—Richika aur anya Pitras—
swarg se utar aaye aur bole:

“O Parashurama, hum tumse prasann hain.
Tumhari bhakti aur tumhari shaurya dono humein khush karte hain.
Mango, kya vardaan chahiye?”"""
            create_image_text_layout("attached_assets/chapter1/1.2.1.jpg", text1, layout="side", image_position="left")

            text2 = """ 
Parashurama bole:

“Meri ek hi iccha hai—
mujhse jo paap hua hai Kshatriya-vadh ka,
wo mit jaye.
Aur ye jo talaab maine banaye hain,
ye duniya bhar me pavitra tirth ban kar mashhoor ho jayein.”

Pitron ne kaha:

“Aisa hi hoga.
Aur tumhara krodh shant ho jaye.”

Tab se wo jagah Samanta-Panchaka kehlai.
Wo teenon lokon me mashhoor hai.

Isi pavitra jagah par
Dwapara aur Kali ke beech
Pandav aur Kauravon ki
mahaan yuddh-bhoomi bani.

Yahin 18 Akshauhini senaayein ikatthi hui
aur yahin ve sab mar gaye.

⚔️ Akshauhini kya hoti hai?

Rishiyon ne poocha:

“O Sauti, ‘Akshauhini’ shabd ka matlab batao.
Ek Akshauhini me kitne ghoṛe, rath, hathi aur paidal sena hoti hai?”

Sauti bola:

📏 Sena ka hisaab (steps):

1 Patti =
• 1 rath
• 1 hathi
• 3 ghode
• 5 paidal

3 Patti = 1 Sena-mukha
3 Sena-mukha = 1 Gulma
3 Gulma = 1 Gana
3 Gana = 1 Vahini
3 Vahini = 1 Pritana
3 Pritana = 1 Chamu
3 Chamu = 1 Anikini
10 Anikini = 1 Akshauhini

📊 Ek Akshauhini me hota hai:

21,870 rath

21,870 hathi

65,610 ghode

109,350 paidal sipahi

Isi hisaab se
Kaurav aur Pandav mil kar
18 Akshauhini sena lekar
Kurukshetra pahunch gaye.

⏳ Yuddh ka samay

Time (Kaal) ne hi sabko ek jagah laa kar rakha
aur phir sabko nasht kar diya.

Bhishma ne 10 din lada.

Drona ne 5 din sena sambhali.

Karna ne 2 din yuddh kiya.

Shalya ne aadha din.

Uske baad
Duryodhana aur Bhima ka gada-yudh
aadha din chala.

Raat ke samay, jab Yudhishthir ki sena so rahi thi,
Ashwatthama, Kripa, aur Kritavarma ne
unhe nishastr aur sote hue mar dala."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.2
        with st.expander("Section 1.2.2"):
            text1 = """ 
Sauti ne Saunaka aur sab rishiyon se kaha:

“O Saunaka!
Jo Mahabharata ki maha-katha tumhare yagna me ab shuru hui hai,
ye pehle Janamejaya ke sarpa-yagna me bhi sunayi gayi thi.
Vyasa ke shishya ne use poora sunaaya tha.”

Ye granth kai parvon (sections) me banta hai.
Isme rajaon ki kahani, unka veerta, unka dharma, sab kuch varnan hai.

Ye granth itna gahra hai jaise Brahma-gyan ka marg.
Jaise saari kathayen kisi na kisi jagah is granth se judi hoti hain,
waise hi shareer ka bojh pair uthata hai.

Mahabharata ko sab kavi isliye maante hain,
kyunki jaise Vedas ke sab shabdon ka aadhar akshar hote hain,
waise hi sab gyaan ka aadhar ye granth hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.2.jpg", text1, layout="side", image_position="left")

            text2 = """ 
📖 Mahabharata ke Parva (Simplified Hinglish List)

Sauti bola:

“Suno, O tapasviyon!
Main tumhe Bharata ke saare parvaon ka saar batata hoon.”

🔹 1. Anukramanika Parva

Sampoorna granth ka prastavna.

🔹 2. Sangraha Parva

Saar-suchi. Pura granth kis tarah vibhajit hai.

🔹 3–4. Paushya & Pauloma

Prajapatis, rishis, rajon ki purani kahaniyan.

🔹 5. Astika Parva

Janamejaya ka sarpa-yagna, Astika ka nagon ko bachana.

🔹 6. Adivamsavatarana

Kuru vansh ka aarambh.

🔹 7. Sambhava Parva

Pandavon, Kauravon ka janm. Vishesh ghatnayein.

🔹 8. Jatugriha-daha

Lac-house ko jalaya jana; Pandavon ka bach kar nikalna.

🔹 9. Hidimba-badha

Bhima ka Hidimba rakshas ko marna.

🔹 10. Baka-badha

Bhima ka Baka rakshas ko marna.

🔹 11. Citraratha

Arjuna ki Chitraratha Gandharva se ladai.

🔹 12. Swayamvara of Draupadi

Arjuna ne Panchali ka swayamvara jeeta.

🔹 13. Vaivahika

Draupadi ka vivaah.

🔹 14. Viduragamana

Vidura ka Pandavo se milna.

🔹 15. Rajyalabha

Pandavon ko raj milna.

🔹 16. Arjuna-banavasa

Arjuna ka vanvaas.

🔹 17. Subhadra-harana

Arjuna ka Subhadra ko sthapaya le jaana.

🔹 18. Haranaharika

Arjuna ki yatraayein.

🔹 19. Khandava-daha

Arjuna aur Krishna ka Khandava-van jalana.
Agni ka santusht hona.

🔹 20. Maya-darsana

Maya danav ka Sabha banana.

🔹 21–24. Sabha, Mantra, Jarasandha, Digvijaya

Pandavon ka sabha bhavan, Rajasuya ki tayari, Jarasandha ka vadh.

🔹 25. Rajasuyaka

Yudhishthir ka Rajasuya Yajna.

🔹 26. Arghyaviharana

Sisupala ka apmaan, Krishna ka rosh.

🔹 27. Sisupala-badha

Krishna dwara Sisupala ko marna.

🔹 28–30. Dyuta, Anudyuta, Aranyaka

Duryodhana ka dicing game, Pandavon ka banvaas.

🔹 31. Krimira-badha

Bhima ka rakshas Krimira ko marna.

🔹 32. Arjuna-vigamana

Arjuna ka tap aur dev-lok ki yatra.

🔹 33. Kairati

Arjuna ka Shiva se sangram; Pashupata astra prapti.

🔹 34. Indra-loka-vigamana

Arjuna ka Indra-lok me pravesh.

🔹 35. Nalopakhyana

Nala–Damayanti ki dukhad–pavitra kahani.

🔹 36. Tirtha-yatra

Yudhishthir ki teerth-yatra.

🔹 37. Jatasura-vadha

Bhima ka rakshas Jatasura ko marna.

🔹 38. Yaksha-yuddha

Pandavon ka Yaksha se samvad.

🔹 39. Nivata-kavacha yuddha

Arjuna ka dev-asur yuddha.

🔹 40–41. Ajagara & Markandeya Samasya

Bhima ka ajgar se mukti; Markandeya ke updesh.

🔹 42. Draupadi–Satyabhama Samvad
🔹 43. Ghosha-yatra

Gandharvon ke dwara Duryodhana ka pakda jaana.

🔹 44–50. Brihadaranyaka, Aindradrumna, Draupadi-harana, Jayadratha-mukti, Savitri, Rama-katha

Vibhinn kathan aur upakhyan.

🔹 51. Kundala-harana

Karna ke kundalon ka adbhut varnan.

🔹 52–55. Aranya, Virata, Agnyatvas, Kichaka-vadh

Pandavon ka gupt vaas; Draupadi ke apmaan ka badla.

🔹 56. Gai-uddhar

Virat ki gaiyon ka uddhar; Arjuna ka pehchan khulna.

🔹 57. Abhimanyu Vivaah
🔹 58. Udyoga Parva

Yuddh ki tayari.

🔹 59–65. Sanjaya-yana, Prajagara, Sanatsujata, etc.

Dhritarashtra ki raaton ki bechaini, gyaan ki baatein.

🔹 66–75. Matali, Galava, Amba, Karnopakhyana, Senayatra

Pehle ke kathan aur yuddh ki tayyari.

🔹 76. Gita Parva

Krishna ka Arjuna ko Gita updesh.

🔹 77. Bhishma-vadha
🔹 78. Drona Parva
🔹 79. Sansaptaka-vadha
🔹 80. Abhimanyu-vadha
🔹 81. Arjuna ka pratigya (Jayadratha ka vadh)
🔹 82. Ghatotkacha-vadha
🔹 83. Drona-vadha
🔹 84. Narayana-astra moksha
🔹 85. Karna Parva
🔹 86. Shalya Parva
🔹 87. Duryodhana ka jal me chhupna aur gada-yuddha
🔹 88–92. Sarasvata, Tirtha, Vanshavali, Sauptika, Aishika

Raat ke paap karm, rishiyon ka gyaan.

🔹 93. Jalapradana

Mrito ko jal-daan.

🔹 94. Stri Parva

Streeon ka shok.

🔹 95. Shraddha

Pitron ke kriya–karma.

🔹 96. Charvaka-vadha

Jhoote brahmana bane rakshas ka vadh.

🔹 97. Yudhishthira ka rajyabhishek
🔹 98–101. Shanti, Rajadharma, Apaddharma, Mokshadharma

Vyasa aur Bhishma ka ati-gahra gyaan.

🔹 102–110. Suka-prashna, Durvasa-katha, Maya-samvad, Anushasan Parva

Dharma ka vistaar.

🔹 111. Bhishma ka swarg-gaman
🔹 112. Ashvamedhika Parva
🔹 113. Anugita
🔹 114–116. Ashramavasa, Putr-darshan, Narada-agman
🔹 117. Mausala Parva

Yadavo ka vinash.

🔹 118. Mahaprasthanika

Pandavon ka antim yatra.

🔹 119. Swargarohanika

Pandavon ka swarg me pravesh.

🔹 120. Khilvansa – Vishnu Parva & Bhavishya Parva

Krishna leela, Kansa-vadh, aur bhavishya ki baatein.

🌟 Ant me

Vyasa ne in sab parvon ko 100 roopon me rachit kiya.
Unme se 18 maha-parva banaye gaye.

Sauti ne ye sab Naimisharanya me
Saunaka ko krama se suna diya."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.3
        with st.expander("Section 1.2.3"):
            text1 = """ 
Parva 1 (Adi Parva Ka Saar)

(Paushya, Pauloma, Astika, Sambhava, etc.)

Mahabharat ka Adi Parva bahut bada hai.
Isme heroes ka janm, rishiyon ki kathayen, Pandav–Kaurav ki shuruaati kahani,
aur Draupadi swayamvar tak sab kuch aata hai.

Chalo ise simple Hinglish me samajhte hain:

🌿 Paushya Parva

Isme Utanka naam ke ek brahmin ki kahani hai.
Utanka bahut tapasvi (austerity-loving) aur dharmic tha.
Uski yatra aur uski shaktiyan batayi gayi hain.

🔥 Pauloma Parva

Isme Bhrigu Rishi ke vansh (lineage) ka varnan hai.
Unke putron ke janm, unki tapasya (penance) aur unke gun bataye gaye hain.

🐍 Astika Parva

Bahut important!

Is parva me:

Garuda ka janm

Nagon (snakes) ka janm

Samudra-manthan (ocean-churning)

Uchchaihshrava naam ka swargiya ghoda (divine horse) ka udgam

Janamejaya ka Sarpa-yajna (snake sacrifice)

Aur us samay Astika ne naagon ko bachaya

Sab detail me aata hai.

Aur yahi par Bharata Vansh ka shuruaati varnan milta hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.3.jpg", text1, layout="side", image_position="left")

            text2 = """ 
🌟 Sambhava Parva

Yeh Adi Parva ka sabse bada hissa hai.

Isme bataya gaya:

🔹 Bahut saare rajaaon, dev-putron aur heroes ka janm:

Danav (powerful demons)

Yaksha (nature-spirits)

Gandharva (celestial musicians)

Serpents

Pakshi (birds)

Aur manav (humans)

🔹 Krishna Dvaipayana Vyasa ka janm

Woh hi Mahabharata ke rachayita (author) hain.

👑 King Bharata ki Kahani

Bharata, Shakuntala aur Dushyanta ka beta tha.
Wahi Bharata, jiske naam par Bharat desh ka naam pada.

Isme unka jeevan, tapasya, aur rajya ki badhi kathayen hain.

🌊 Bhagirathi ki Mahima

Ganga ji ka prithvi par aana — Bhagirath ki tapasya — yeh sab bataya gaya.

⚔️ Bhisma ka Janm

Vasus ke shraap se Bhishma ka janm hota hai.
Woh apni pratigya (terrible vow) ke liye mashhoor hain —
rajya, vivaah, sab chhodkar brahmacharya ka palan.

Woh:

Citrangada ko protect karte hain

Fir Vicitravirya ko raja banate hain

Aur rajya ko sthir rakhte hain

👶 Dhritarashtra, Pandu aur Vidura ka Janm

Vyasa ki kripa se ye teen janme:

Dhritarashtra — andh

Pandu — rang se peele

Vidura — dharm-upj (born of Dharma)

Phir Pandavon ka janm — Dharma, Vayu, Indra aur Ashvini kumaron ki kripa se.

🔥 Lakshagriha (House of Lac) Khandan

Duryodhan aur uske saathi Pandavon ko jala kar marna chahte the.
Vidura ne raaste me “mleccha bhasha” (coded language) me chetavani di.

Pandav gumnaam surang se bachkar nikal gaye,
aur Purocana aur ek aurat aur uske 5 bachche waha jal gaye.

🌲 Hidimba Encounter

Jungle me Bhima ka Rakshas Hidimba se sangram hua.
Bhima ne usse maara.
Hidimba ki behen Hidimbi ne Bhima se vivah kiya.
Unke bete ka naam hua Ghatotkacha.

🏚 Ekachakra aur Vaka-vadha

Pandav Ekachakra me ek brahmin ke ghar rahte hain.
Waha Bhima ne bhayankari rakshas Vaka ko maara.

👑 Krishna & Dhrishtadyumna ka Janm

Panchal me Draupadi (Krishnaa) aur uske bhai Dhrishtadyumna ka divya janm hota hai.

🏹 Pandav Panchala Ki Or

Ek brahmin se Draupadi swayamvar ki khabar sunte hi Pandav wahin jaate hain.

Raste me Arjun ka Gandharva Angaraparna se sangram hota hai.
Fir usse mitrata hoti hai.
Woh Arjun ko Tapati, Vasishtha aur Aurva ki kahani sunata hai.

💍 Draupadi Swayamvar

Arjuna ne nishana maar kar swayamvar jeeta.
Bhima aur Arjuna ne dusre rajaon ko hara diya.
Krishna aur Balarama ne pehchana ki yeh Pandav hi hain.

Phir pottery-house me sab milte hain.

Drupada pehle dukh karta hai ki Draupadi ko 5 pati milenge…
Fir Rishi kahani batate hain ki paanch Indraon ka janm hua tha,
aur Draupadi ka vivaah dev-iccha se paanchon se ordained tha.

Draupadi ka divya vivaah hota hai.

🏰 Khandavaprastha aur Rajvibhajan

Pandavon ko aadha raj milta hai.
Wahi par woh Indraprastha basate hain.

Narada aate hain aur batate hain ki Draupadi ke saath turn-by-turn rehna chahiye.
(Yeh unki maryada-bodh ke liye tha.)

👫 Arjuna ka Vanvaas

Ek din Arjuna ne astra lene ke liye Draupadi–Yudhishthira ko saath dekha.
Vachan ke hisaab se Arjuna ko vanvaas jaana pada.

🐍 Ulupi aur Vabhruvahana

Vanvaas me Arjuna ki mulakat Naga-kanya Ulupi se hoti hai.
Unse ek putra hota hai – Vabhruvahana.

Arjuna paanch apsaraon ko bhi bachata hai jo shraap se magar (alligators) ban gayi thi.

🛕 Subhadra-Harana

Prabhasa tirth me Arjun Krishna se milta hai.
Krishna use apni behen Subhadra ko le jaane ko kehte hain.
Arjun unhe divya rath me le jata hai –
jo jal, zameen aur hawa sab me chal sakta tha.

Indraprastha lautkar Subhadra se Abhimanyu ka janm hota hai.

🌳 Khandava-daha (Forest Burning)

Arjuna aur Krishna ne ek saath Khandava van jala diya
taaki Agni dev santusht ho sake.

Agni ki ichha thi ki “koi rok na sake”,
toh Arjun–Krishna ne sab dev–asuras ko rok diya
aur van jal gaya.

Yahin se Gandiva, chariot, chakra jaise divya uphar milte hain.

🏛 Maya Danav ka Bachna

Eklauta bachne wala Asura Maya Arjun ka upkaar maanta hai.
Wahi baad me Pandavon ke liye Mayasabha banata hai –
jo Duryodhan ke liye sabse bada psychological shock ban gayi.

🕊 Mandapala aur Pakshi-katha

Ant me Mandapala rishi pakshi (bird) Stree Sarangi ke garbh se putra paida karte hain.

📘 Adi Parva ki Total Rachna

Vyasa ne ise 227 adhyay me bataya hai.
Total 8,884 shlok hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.4
        with st.expander("Section 1.2.4"):
            text1 = """ 
Parva 2 (Sabha Parva ka Saar)

Sabha Parva Mahabharat ka doosra bada parva hai.
Isme Pandavon ki rajya ki shaan, Rajasuya yagna,
Jarasandh ka vad,
aur sabse dardnaak —
dyut-krida (dice game) ka varnan hai.

Chalo ise kahani ki tarah samajhte hain:

🏛 Pandavon ka Maha-Sabha (Grand Hall)

Pandav apne naye rajya Indraprastha me ek divya sabha (assembly hall) banwate hain.
Yeh sabha Maya Danav, jo Khandav-dahan me bach gaya tha, banata hai.
Sabha me aise bhram, darpan aur alaukik designs thay
ki sab rajasamast log hairaan reh jaate the.

👥 Retainers ka Review

Iske baad Pandav apne logon, sainyo, mantriyon, aur purohiton ka review karte hain.
Ye ek rakshya-sajjata (security and organization) ka kaam tha.

🔱 Narada ka Aagaman – Lokpalo ka Varnan

Ek din Devarshi Narada aate hain.
Woh devlok ke alaukik sthanon ka varnan karte hain:

Indra ka sabha

Yama ka rajya

Varuna ka jal-mahal

Kubera ka dhan-rajya

Narada batate hain ki Pandavon ki sabha bhi in sab ki tarah tejomayi (radiant) hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.4.jpg", text1, layout="side", image_position="left")

            text2 = """ 
🔥 Rajasuya Yagna ki Taiyari

Yudhishthir Maharaj ko Rajasuya Yagna karna hai —
yeh ek sarvabhaum samrat (emperor) banne ka ritual hai.

Iske liye:

sab rajaon ka sammati

shatruon ka vinash

aur prithvi par shanti chahiye

Sabse bada badha tha:

⚔️ Jarasandh-Vadh

Magadh ka raja Jarasandh bahut balshali tha.
Woh bahut se rajaon ko pahadon me band karke rakhta tha.

Krishna, Arjuna aur Bhima,
Brahmin ke roop me jaakar use sangram ke liye ubhalte hain.

Bhima aur Jarasandh ke beech 14 din ka kushti-yuddh hota hai.
Ant me Krishna ke sanket se
Bhima use beech se phaadkar maar deta hai.

⛰ Bandhi Hue Rajo Ki Chhutkaara

Jarasandh ke marne par sab band rajaon ko azaadi milti hai.
Vasudev Krishna un sab rajao ko nikal kar bahar laate hain.
Sab Yudhishthir ko Rajasuya me sahyog dene ka vachan dete hain.

🌍 Pandavon ka Digvijay – World Conquest Campaign

Rajasuya se pehle sare dishaon me vijay chahiye:

Bhima dakshin (South) me jayate hain

Arjuna north aur west me vijay karte hain

Sahadeva dakshin-purva (SE)

Nakula uttar-purva (NE)

Sab raja haar kar ya maan kar Yudhishthir ko samraat swikar karte hain.

🎁 Tribute ka Aagaman

Rajasuya ke din duniya bhar ke raja aur maharaaj
apne-apne uphaar (tribute) lekar aate hain —
sona, ratna, godhuli, gaj, ashw, sab kuch.

⚡ Sisupala ka Vad

Arghya (respect offering) Krishna ko diya jaata hai.
Sisupal is par guse me Krishna ko gaaliyan deta hai.
100 galtiyon ka vardaan usse mila tha.
Jab 100 poori hoti hain,
Krishna ka Sudarshan Chakra uska sar udd deta hai.

Rajasuya yagna ka sabse bada kshan hota hai yeh.

😡 Bhima ki Mazak, Duryodhan ka Irsha (envy)

Sabha bhavan me ek optical illusion hota hai:
jahan pani lagta hai waha zameen hoti hai
aur jahan zameen lagti hai waha pani hota hai.

Duryodhan do jagah galti karta hai:

zameen ko samajhkar “paani” me kadam rakhta hai

paani samajhkar “zameen” par muh ke bal girta hai

Sab raja hans dete hain.
Bhima mazak udaata hai.
Duryodhan ka dil jalan aur irsha se bhar jata hai.

🎲 Dyut-krida (Game of Dice)

Apmaan se bhara hua Duryodhan Shakuni mama ke saath
Yudhishthir ko dice game ke liye bulata hai.

Shakuni apne jaadu bhare pasa se sab kuch jeet leta hai:

rajya

dhan

apne bhai

khud Yudhishthir

aur ant me Draupadi bhi

Draupadi ko sabha me kheechkar laane ka anuchit (improper) kary hota hai.

🕊 Draupadi ka Udhar – Dhritarashtra ka Intervention

Draupadi sabha me prashna karti hai:
“Jab Yudhishthir ne khud ko hi haar diya tha,
toh woh mujhe kaise daav pe rakh sakte hain?”

Iss nyay-vachan se sabh hil jaate hain.
Dhritarashtra Draupadi ko var deta hai:

Pandavo ko mukti

rajya vaapas

aur sab dhan-vaibhav lautaya jaata hai

🎲 Second Dice Game & Exile

Duryodhan phir se Yudhishthir ko doosre khel ke liye majboor karta hai.
Is baar shart hoti hai:

➡️ Pandav 12 saal vanvaas + 1 saal agyatvas (incognito exile)

Shakuni phir jeet jata hai.
Pandav vanvaas chalte hain.

📘 Sabha Parva ki Rachna

Total sections: 78

Total shlok: 2,507

Yeh parva Mahabharat ka sabse political aur emotional parva hai —
jisme shaan bhi hai, aur patan (downfall) ki shuruaat bhi."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.5
        with st.expander("Section 1.2.5"):
            text1 = """ 
🌳 Parva 3 – Aranyaka Parva (Forest Parva)

Pandavon ka 12 saal ka Vanvaas + 1 saal ka Agyatvaas ka safar
Ye Mahabharat ka sabse bada, sabse lamba, aur sabse kahaniyon se bhara parva hai.

Chalo ise simple Hinglish kahani ki tarah samajh lete hain.

🚶‍♂️ Pandavon ka Vanvaas Shuru

Dyut-krida me haarne ke baad Yudhishthir sabse pehle Indraprastha ke nagar-vaasiyon ko shant karte hain,
aur phir sab bhaiyon aur Draupadi ke saath vanvaas chal padte hain.

Dhaumya Rishi unhe mantra aur upaay batate hain ki
kaise van me bhi Brahmano ko bhojan dene ki shakti mile.
Surya-dev prakat hoke Yudhishthir ko Akshay Patra dete hain—
jis se anant bhojan milta hai.

🏰 Vidura Ka Nirvasan Aur Wapas Lautna

Dhritarashtra, Duryodhan ke dabav me aakar Vidura ko ghar se nikal deta hai.
Vidura Pandavo se milne aata hai.
Unke dukh dekh kar fir Dhritarashtra ke bulane par wapas laut jaata hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.5.jpg", text1, layout="side", image_position="left")

            text2 = """ 
🔥 Duryodhan ki Jalti Irsya – Pandavo ko Marne ki Sazish

Karna Duryodhan ko uksata hai ki
“Van me Pandavo ko maar denge.”
Vyasa Rishi aa kar use rok dete hain.

🐄 Surabhi Ki Kahani – Maitreya Ka Shraap

Maitreya Rishi aakar Dhritarashtra ko sadbuddhi ki salah dete hain.
Duryodhan unka apmaan karta hai.
Maitreya use shraap dete hain:
“Bhima ke gada prahar se tera jangha tootegi.”

⚔️ Bhima vs Kirmira

Forest me rakshas Kirmira Pandavo ko rokta hai.
Bhima use maar girata hai.

👑 Krishna, Panchal & Vrishni Princes ka Aagaman

Pandavo ki haalat sun kar:

Krishna

Panchal ke raja

Vrishni ke rath
sab van me aate hain.

Draupadi Krishna ke saamne dukh jahir karti hai.
Krishna use dhairya dete hain.

🌳 Dwaita Van Me Pravesh

Pandav Dvaita Forest pahunchte hain.
Yahaan unki baatein, dukh-sukh, aur jeevan ka safar shuru hota hai.

Vyasa aakar Yudhishthir ko Pratismriti ki shakti dete hain
(jisse woh saari cheezein turant yaad kar sakein).

Phir sab Kamyaka Forest me shift ho jaate hain.

🎯 Arjuna ki Weapon-Tapashcharya Yatra

Arjuna akela dev-astra prapt karne chala jaata hai.

Mahadev se bhent — hunter ke roop me
Arjuna unse ladta hai, phir unhe pehchan leta hai.
Shiva usse Pashupatastra deta hai.

Lokpala (Indra, Varuna, Yama, Kubera) se astra praapt

Swarg yatra – Indra ke paas shastra seekhne
Dhritarashtra ise sunkar dukhi hota hai ki van me bina Arjuna ke Pandav kamzor hain.

📖 Nala-Damayanti ki Kahani

Brihadasva Rishi Yudhishthir ko milte hain.
Unhe shant karne ke liye woh Nala aur Damayanti ki dardnaak aur sundar kahani sunate hain.
Isse Yudhishthir ko dice ka secret bhi samajhta hai.

🌍 Teerth-Yatra of Pandavas

Rishi Lomasha aate hain aur batate hain ki
Arjuna swarg me surakshit hai.
Phir Pandav teerth-yatra par nikal padte hain:

Pushkara

Prayag

Ganga-sagar

Himachal

Sarasvati

Gaya

Naimisharanya

aur anek pavitra sthaan

Is yatra me bahut purani kahaniyan sunai jaati hain:

Agastya aur Vatapi

Rishyashringa

Parashurama aur Kartavirya

Cyavana Rishi

Mandhata

Somaka aur Jantu

Sivi Raja

Ashtavakra aur Vandi

Yavakrita

Raivya

Sab kahaniyan dharma aur jivan ke rahasya batati hain.

🐒 Bhima & Hanuman ka Mahamilan

Draupadi ko ek saugandhik phool chahiye.
Bhima uski khoj me Gandhamadana Parvat chadh jaata hai.

Raste me:

Banana grove

Bhayanak van

Yaksha aur Rakshas

Jata Rakshas ka vad

Aur sabse bada kshan:

👉 Hanuman se milan (Bhima ka bada bhai)

Hanuman Bhima ko apna roop dikhata hai
aur unhe bal, maryada aur dhairya ki shiksha deta hai.

🏔 Kubera ka Darbar & Arjuna’s Return

Pandav Kubera ke van me pahunchte hain.
Arjuna bhi swarg se vaapas aata hai
aur apne divya-astra Yudhishthir ko dikhata hai.

Narada unhe rok dete hain ki
“Ye shastra be-wajah mat chalao.”

🐍 Bhima aur Ajeeb Vishal Sarpa

Ek din van me Bhima ko ek maha-saamp jakad leta hai.
Yudhishthir us serpent ke prashna ka sahi uttar dekar
Bhima ko chhudata hai.
Woh saamp ek shraapit raja tha —
Yudhishthir ke dharma-bodh se mukt ho jaata hai.

🪵 Kamyaka Wapas, Markandeya ki Kahaniyan

Krishna van me aate hain.
Rishi Markandeya bhi aate hain
aur bahut divya kathayen sunate hain:

Prithu Raja

Sarasvati

Dhundhumara

Chaste wife ki kahani

Angira

Satyabhama-Draupadi ka samvad

🐄 Duryodhan ka Bandhan

Ek baar Duryodhan gau-dekhne jaata hai
aur Gandharvon se ladkar bandi ban jaata hai.

Arjuna use bacha kar laata hai
(halaanki Duryodhan Pandavo se hamesha dvesh rakhta hai).

🦌 Yudhishthir ka Hiran-Swapna

Ek divya swapna me Yudhishthir ko
ek mriga (deer) ka sandesh milta hai
aur kaafi adhyaatmik baatein hoti hain.

🔥 Jayadratha Dwara Draupadi ka Apaharan

Jayadratha Draupadi ko van se utha le jaata hai.
Bhima piche daudta hai,
uske sena ko tod deta hai,
aur Jayadratha ko zinda chhodkar
“aadha sir mundan” ki saza deta hai.

🏹 Ramayana ki Kahani (Rama-Ravana Yuddh)

Vana Parva me Ramayana ka saar bhi diya gaya hai—
kis tarah Rama ne Ravana ko maara.

💠 Karna ka Kundal-Aabhushan Hara Jana

Indra bhiksha ke roop me aakar
Karna ke kundal aur kavach maang lete hain.
Karna deta hai.
Badle me Indra ek Shakti astra deta hai,
jo sirf ek baar kisi ko maar sakta hai.

⚖️ Dharma Raj ka Upadesh

Ek lambi kathaa me Dharma Dev
Yudhishthir ko jeevan ke niyam sikhate hain.
Pandav uske baad west ki aur chalte hain.

📘 Aranyaka Parva ke Details

Total sections: 269

Total shlokas: 11,664

Yeh Mahabharat ka sabse bada kahani-parva hai
jisme darshan, dharma, yatra, dev-astra,
aur katha-sagar sab hai."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.6
        with st.expander("Section 1.2.6"):
            text1 = """ 
Parva 4: 
⭐ Virata Parva — Hinglish Kahani Summary

Pandav log exile ke last saal mein Virata kingdom pahunchte. City ke bahar ek purana shami ka ped tha, jisme unhone apne weapons chhupa diye, taki koi unhe pehchaan na sake.
Phir sab ne disguise le liya—kisiko cook ban-na, kisiko teacher, kisiko dancer, sabne alag-alag role liya aur Virata ki rajdhani mein chupkar rehne lage.

⭐ Bhima aur Kichaka

Rani Draupadi par ek wicked aadmi Kichaka buri nazar daalne laga.
Bhima ko bohot gussa aaya aur usne Kichaka ko raakshas ki tarah maar giraya. Rani ko bacha liya.

⭐ Spies Everywhere

Duryodhan ko lagta tha Pandav yahi kahin hain.
Usne har taraf spies bhej diye, par koi Pandav ko dhoond nahi paaya. Unka disguise itna solid tha!

⭐ Trigarta Attack

Ek din, Trigarta logon ne Virata ke gai-bail (kine) chura liye.
Virata bhi pakda gaya, par Bhima ne jaake usse chhuda liya aur poora dushman sena ko hara diya.

⭐ Kauravas ka Attack

Baad mein Kaurav log ne bhi Virata ki gaayein chura li.
Is baar Arjun ne apna disguise chhod kar brave warrior ban kar sab Kurus ko akela hi hara diya.
Virata ki saari gaayein waapas mil gayi.

⭐ Uttara ka Vivaah Proposal

King Virata bohot khush hua.
Usne apni beti Uttara ko Arjun ko dena chaha, par Arjun ne bola:
“Main toh uska guru jaisa hoon. Par uska vivaah mere bete Abhimanyu se ho sakta hai.”

Is tarah Virata Parva khatam hota hai—Pandav apna gupt-vaas safal kar lete hain, koi unhe pakad nahi paata, aur Virata unka loyal dost ban jaata hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.6.jpg", text1, layout="side", image_position="left")

                # Section 1.2.7
        with st.expander("Section 1.2.7"):
            text1 = """ 
Parva 5: 
⭐ Udyoga Parva — Hinglish Kahani Summary

Pandav log Upaplavya naam ke jagah par reh rahe the, aur unhe pata tha ki ab war almost tay hai.
Duryodhan aur Arjun ek hi samay Krishna ke paas gaye. Dono ne bola:

“Humari help karo!”

⭐ Krishna ka Offer

Krishna ne muskura kar bola:

“Mere paas do cheezein hain —
1️⃣ Ek Akshauhini sena
2️⃣ Main khud… par main war mein ladunga nahi.”

Duryodhan ne bina soche-vichare poori sena chaan li.

Arjun ne shanti se kaha:
“Main aapko chunta hoon, chahe aap na ladho.”

Is tarah Krishna Arjun ke saath ho gaye.

⭐ Shalya ka Confusion

Madra ka Raja Shalya Pandavon ki help ko aa raha tha.
Raaste mein Duryodhan ne usko bahut gifts aur hospitality di.
Shalya ne khush hokar ek boon de diya… aur Duryodhan ne turant bola:"""
            create_image_text_layout("attached_assets/chapter1/1.2.7.jpg", text1, layout="side", image_position="left")

            text2 = """ 
“Mere liye war mein ladho!”

Majboori mein Shalya ne haan kehdi,
par baad mein Pandavon ko aakar unhe console kiya.

⭐ Peace Talks Begin

Pandavon ne apna purohit Kaurav court bheja — shanti ke liye.

Dhritarashtra ne uski baatein suni, par wo bohot tension mein aa gaya.
Uski neend ud gayi.
Tab Vidur ne usko wise advice di.
Phir Sanat-Sujata ne deep spiritual wisdom bataya, taaki Dhritarashtra ka fear kam ho jaye.

Next day, Sanjaya ne court mein Krishna aur Arjun ki divya unity ka secret bataya.

⭐ Krishna Goes for Peace

Krishna khud Hastinapur gaye—
“Chalo, peace karte hain.”

Lekin Duryodhan ne inkaar kar diya.
Na woh 5 gaon dene ko tayar tha, na ek zameen jitni soyi ki nok.

Shanti ki har koshish fail ho gayi.

⭐ Stories & Teachings

Is Parva mein Krishna ne rajaon ke saamne apni yogmaya dikhayi — sabko pata chal gaya ki woh koi aam aadmi nahi.

Krishna ne Karna ko alag se milkar samjhaya:

“Tum Pandavon ke bhai ho… sahi rasta chuno.”

Par Karna ne ahankaar me mana kar diya.

⭐ War is Now Certain

Krishna Pandavon ke paas laut kar sab kuch batate hain.
Pandav sun kar tay kar lete hain:
“Ab war hi antim raasta hai.”

⭐ Armies March Out

Dono taraf ki sena —
foot soldiers, horses, elephants aur chariots —
sab battlefield ki taraf chal padti hain.

Duryodhan apna messenger Uluka bhejta hai, jo Pandavon ko dhamki/ message deta hai.

Yahan Amba ki kahani bhi aati hai, jisse future mein Bhishma ka vinash jude hota hai."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.8
        with st.expander("Section 1.2.8"):
            text1 = """ 
Parva: 6:
⭐ Bhishma Parva — Hinglish Kahani Summary

Mahabharat ka asli maha-yudh isi Parva se shuru hota hai.
Dono senae—Kaurav aur Pandav—maidan mein khadi hoti hain.
Aur Sanjaya, apni divya drishti se, Dhritarashtra ko sab kuch live batata hai.

⭐ Jambu Dweep ka Varṇan

Sabse pehle Sanjaya Jambu-dweep ka formation batata hai—
jaise dharti ka ek magical map ho.

⭐ Arjun ka Dil Tootna

War shuru hone waala hota hai, tab Arjun apne rishtedaaron ko saamne dekh kar dukhi ho jata hai.

Woh bow neeche rakh deta hai:

“Main apne guru, dada, chacha… kisi ko nahi maar sakta.”

Krishna usse Geeta ka gyaan dete hain—
atma, kartavya, aur moksha ke baare mein.
Arjun fir se strong feel karta hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.8.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ 10 Din ka Bhayankar Yudh

Bhishma Pitamah Kaurav sena ke commander hain.
Unki leadership mein Pandavon par bhari nuksaan hota hai.
Yudh 10 din tak ekdum fierce rehta hai.

Yudhishthir bohot udaas ho jate hain,
aur Krishna Pandavon ki chinta dekh kar khud patience lose kar dete hain!

⭐ Krishna Ka Krodh

Ek din Krishna dekhte hain ki Bhishma sabko maar rahe hain,
toh woh apna promise todne ki soch lete hain.

Woh chariot se kud kar, whip haath mein lekar seedha Bhishma ki taraf daudte hain:

“Aaj main khud Bhishma ko maar dunga!”

Arjun shock ho jata hai aur Krishna ko rok leta hai.

⭐ Bhishma Ko Girane Ka Tareeka

Bhishma ne promise diya tha ki woh aurat ya eunuch par hath nahi uthaayenge.
Isliye Arjun Shikhandi ko apne chariot ke saamne khada karta hai.

Bhishma Shikhandi ko dekh kar apne hathiyaar neeche kar dete hain.
Tab Arjun tezi se tez-tez arrows chalata hai.

Arrows ka varsha Bhishma ko tod deta hai.
Unka poora sharir teeron ki shayya par gir jata hai.

Bhishma kehte hain:

“Aaj mera ghoshit vidhata aa gaya.”

⭐ Bhishma on the Bed of Arrows

Bhishma zameen ko touch nahi karte—
poora sharir arrows par tikka hota hai.
Yeh scene Mahabharat ka sabse emotional scene mana jata hai.

Pandav aur Kaurav dono unke paas aate hain.
Woh mrityu ka samay aane tak wahin tik kar rahte hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.9
        with st.expander("Section 1.2.9"):
            text1 = """ 
Parva 7: 
⭐ Drona Parva — Hinglish Kahani Summary

Bhishma ke girte hi, Dronacharya ko Kaurav sena ka commander banaya jata hai.
Sab log jaante hain ki Drona ek mahaan guru hain—
aur ab unka ek hi sankalp hai:

“Main Yudhishthir ko pakad kar Duryodhana ko dunga.”

Is vow ke saath yudh aur bhi khatarnak ho jata hai.

⭐ Sansaptakon ka Attack & Arjun ka Door Jaana

Ek special group hota hai—Sansaptak—
jo kasam kha kar ladte hain ki woh Arjun ko rokenge.

Arjun ko unse ladna padta hai,
isliye woh main battlefield se door chala jata hai.

Drona is moment ko use karte hain Yudhishthir ko pakadne ke liye—
lekin Pandav sena milkar unka plan fail kar deti hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.10.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Bhagadatta & Hathi Supratika

Phir aate hain Bhagadatta,
jo apne giant hathi Supratika par baith kar ladte hain—
bilkul dusre Indra ki tarah.

Arjun unhe rokta hai
aur ek tezz arrow se Bhagadatta aur hathi, dono ko gira deta hai.

⭐ Abhimanyu ka Shaurya… aur Shaheed Hone Ki Kahani

Is Parva ka sabse dardnaak hissa—
Abhimanyu, Arjun ka naujawaan beta.

Woh Chakravyuh me shandar tareeke se ghusta hai,
lekin usse bahar nikalna nahi aata.

Aur sab Kaurav Maharathi
—Drona, Karna, Dushasan, Kripacharya, Jayadratha—
milkar ek akela teenager ko maar dete hain.

Abhimanyu gir jata hai…
aur Pandavon ke dil toot jate hain.

⭐ Arjun ka Gussa – 7 Akshauhini Sena Ka Sanhaar

Jab Arjun ko pata chalta hai
ki uske bete ko aniyay se maara gaya,
toh woh kasam khata hai:

“Kal suraj dhalne se pehle, main Jayadratha ko maar dunga.”

Us gusse mein Arjun 7 Akshauhini sena tak mita deta hai!

Aur ant mein, Krishna ki madad se,
woh Jayadratha ko maar deta hai.

⭐ Bhima & Satyaki ka Rukna Mushkil

Yudhishthir chinta mein pad jata hai ki
'Arjun kab laut kar aaega?'

Toh Bhima aur Satyaki dono
Kaurav sena ko cheer kar
Arjun ko dhoondne jaate hain.

Dono ek army ke barabar ladte hain
aur Sansaptak jiski chingari bhi baaki thi—sab ko khatam kar dete hain.

⭐ Bade Warriors Ki Maut

Is Parva mein bohot saare mahaan yoddha girte hain:

Virata

Drupada

Ghatotkacha (Bhim ka beta)

Alambusha

Srutayus, Jalasandha, Shomadatta

Ghatotkacha ki maut bhi bohot emotional hoti hai.
Uske marne se Karna apna Indra ka divya astra bekar hi use kar deta hai—
jo baad mein Arjun ko bachata hai.

⭐ Ashwatthama ka Krodh & Narayan Astra

Jab Ashwatthama ko pata chalta hai
ki uske pita Drona maar diye gaye,
toh woh gusse se pagal ho jata hai.

Woh chala deta hai
Narayana Astra—
ek aisa divine weapon jo pura sena jala sakta tha.

Krishna sabko samjhate hain:

“Jo apne hathiyaar chod de aur shant ho jaye, usse yeh astra nahi marega.”

Pandav bach jate hain.

⭐ Vyasa ka Gyaan & Krishna–Arjun ki Mahima

Ant mein Rishi Vyasa aate hain
aur Krishna aur Arjun ki mahima batate hain—
ki kaise dono milkar dharma ki raksha kar rahe hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.10
        with st.expander("Section 1.2.10"):
            text1 = """ 
Parva: 8: 
⭐ Karna Parva — Hinglish Kahani (Simple & Emotional)

Yudhishthir aur Arjun ka gussa ab charam par tha,
aur Drona ki maut ke baad
Karna ko Kaurav sena ka commander banaya gaya.

Uska sarathi banaya gaya Shalya,
jo Madra ka gyani aur chalak raja tha—
par dil se woh Karna ka saath nahi deta tha.

⭐ Karna & Shalya Ki Tana-Mari

Yudh ke pehle din hi,
Karna aur Shalya ek–dusre ko
teekhe shabd bolte hain.

Shalya baar-baar Karna ka mazaak udata hai—
kabhi uski jaati ko lekar,
kabhi uski skills ko lekar.

Aur iss beech woh ek chhotti si kahani sunata hai
hansh aur kauve ki—
jisme Karna ko indirectly “kauva” bataya jata hai.
Karna yeh sab chup-chaap सहता hai,
par uska gussa badhta jata hai."""
            create_image_text_layout("attached_assets/chapter1/1.2.10.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Yudh Ka Aagaz

Asvatthaman kuch bade yoddha maar deta hai:

Pandya

Dandasena

Darda

Battlefield garam hota jata hai,
aur ab aati hai sabse bade takraar.

⭐ Karna vs Yudhishthir — Ek Khatarnaak Moment

Yudhishthir, jo shant aur dharmic the,
Karna ke saamne khade ho jate hain.

Karna ka teer itna tezz hota hai ki
Yudhishthir ka jeevan khatre mein aa jata hai.
Sab yoddha dar jaate hain.

Par kisi tarah woh bach jaate hain.

Lekin iske baad
Arjun aur Yudhishthir ke beech gussa phoot padta hai,
kyunki Arjun samay par nahi pahucha tha.

⭐ Krishna Ka Shaant Karna

Arjun gusse me shabd bol deta hai,
lekin Krishna usse shaant karte hain:

“Gusse me liya hua faisla hamesha galat hota hai.
Tum dono bhai ho. Ek doosre ka sahara bano.”

Arjun dheere-dheere shaant hota hai
aur phir se yudh me lautne ka faisla karta hai.

⭐ Bhima Ka Vachan Poora Hona

Ye Parva Bhima ki kasam ka bhi ant hai.

Bhima Dushasan ko dharti par gira deta hai,
aur apne vow ke hissaab se
uska khoon peeta hai—
ek andhera, bhayanak, par powerful scene.

Draupadi ka apmaan yahin kaat diya jata hai.

⭐ Karna vs Arjuna — Antim Yudh

Ab aata hai woh yudh jiska intezaar sab kar rahe the—
Karna aur Arjun ka ekal ladai.

Dono maha-yoddha
apne sabse shreshth astra chalaate hain.
Dhul, bijli, teeron ki aandhi—
pure battlefield me andhera cha jata hai.

Phir, Karna ka rath ka pahiya
Zameen me phas jata hai.
Woh dharma ka hawala deta hai,
“Ruko, main isse nikal loon.”

Par Krishna Arjun ko yaad dilate hain:

“Karna ne Abhimanyu ko bina niyam ke mara tha.
Adharm ka jawab dharm se nahi diya jaata.”

Arjun ek tezz teer chala kar
Karna ko girata hai.

Karna shaant ho jata hai—
uski kahani ka yeh antim adhyay hota hai."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.11"):
            text1 = """ 
⭐ Parva 9 – Shalya Parva (Hinglish Summary)

Sab maha-yoddha ek ek karke gir chuke the.
Ab Kaurav sena ka naya senapati bana King Shalya, Madra ka raja.
Woh bahut shaktishaali tha, par yudh ka waqt sab ke liye kathin tha.

⭐ Shalya Ka Ant

Chariot se chariot tak bhayankar yuddh hua.
Gadhe, ghode, rath sab garaj rahe the.

Aur phir—
Yudhishthira ne Shalya ko hara diya.
Shalya zameen par gira… aur Kaurav sena aur kamzor ho gayi."""
            create_image_text_layout("attached_assets/chapter1/1.2.11.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Shakuni Ka Ant

Phir Sahadeva ne apna pura gussa nikaala.
Shakuni, jo hamesha chalbaazi karta tha,
aaj bach nahi saka.
Sahadeva ne uska saamna kiya
aur usse maar diya.

Pandavon ka purana dushman khatam ho gaya.

⭐ Duryodhana Ka Chhupna

Ab sena me sirf kuch log bache the.
Duryodhana akela pad gaya.
Darr aur sharm se bhara hua,
woh ek talab me ghus gaya.
Pani ke andar usne ek jagah bana li
aur waha chup kar let gaya.

⭐ Bhima Ko Khabar Milti Hai

Kuch pakshi pakadne wale fowler logon ne
Duryodhana ko chhupa dekha.
Unhone yeh baat Bhima ko batayi.

Bhima ne yeh sunte hi gussa piya:
“Chalo, isko bahar nikalte hain!”

⭐ Yudhishthira Ka Teekha Vachan

Pandav us talab ke paas gaye.
Yudhishthira ne Duryodhana ko awaaz lagayi
aur kuch kadve shabd bole.
Duryodhana, jo apmaan bardasht nahi kar sakta tha,
gusse me pani se bahar aa gaya.

⭐ Mace Fight – Gada Yuddh

Bahar aate hi dono ne
gada yuddh ka chunauti di.

Duryodhana aur Bhima—
dono pahad ki tarah takraaye.
Mitti udne lagi, zameen hilne lagi.

Isi waqt Balarama bhi waha aa gaya
aur dono ka yuddh dekhne laga.

⭐ Bhima Tod Deta Hai Jaanghe

Yuddh lamba chala.
Duryodhana tej tha,
par Bhima ka sankalp aur tej tha.

Ekdum se Bhima ne
apni gada ghumayi aur
Duryodhana ki jaanghe par zor se maara.

Duryodhana cheekh ke gir gaya.
Uski taaqat toot gayi.
Mahabharat ka moti mukhya dushman
ab haar chuka tha.

⭐ Parva 9 Samapt

Is tarah Shalya Parva me—

Shalya mara

Shakuni mara

Duryodhana chhupa, phir bahar aaya

aur Bhima ne uski jaanghe tod di

Yeh sab mila kar is parva me
59 sections aur 3,220 shlokas hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.12"):
            text1 = """ 
⭐ Parva 10 – Sauptika Parva (Hinglish Summary)

Mahabharat ka yudh khatam ho chuka tha.
Pandav apne camp me laut gaye the.
Lekin raat me ek darawni kahani shuru hui…

⭐ Duryodhana Ki Dukhi Haalat

Sham ke samay,
Ashwatthama, Kripacharya aur Kritavarma
ranbhoomi me gaye.

Waha unhone Duryodhana ko zameen par pada dekha—
uski jaanghen tooti hui, poora sharir khoon se bhara.
Duryodhana jeevit tha, par bohot kamzor.

Ashwatthama ka gussa ab aasman tak pahunch gaya.
Usne kasam khayi:

“Jab tak main sab Panchalon ko, Drishtadyumna ko,
aur Pandavon ke mitron ko nahi maar deta,
tab tak apna kavach nahi utaarunga!”"""
            create_image_text_layout("attached_assets/chapter1/1.2.12.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Ullu Aur Kaawon Ka Sanket

Raat ko teeno ek bade bargad (banyan) ke ped ke neeche baithe.
Waha Ashwatthama ne ek ajeeb drishya dekha—

Ek ullu (owl) ek ek karke kaawon ko maar raha tha.

Yeh drishya uske man me aur andhera bhar gaya.
Usne socha:

“Aaj raat main bhi soye huye dushmano ko maarunga.”

⭐ Rakshas Ka Darshan

Jab Ashwatthama ne shivir ke darwaze par jaana chaha,
usne ek bhayankar rakshas dekha—
jiska chehra bohot darawna tha
aur sar aasman ko chho raha tha.

Woh rakshas uske teer-baan rok raha tha.

Tab Ashwatthama ne Mahadev (Rudra) ka dhyaan kiya.
Shivji prasann hue
aur usse andar jaane diya.

⭐ Raat Ka Nar-sanhaar (Night Massacre)

Andar sab Panchal yoddha so rahe the—
Drishtadyumna, Draupadi ke paanch putra, aur anya senapati.

Ashwatthama ne bina soch samajh
neend me doobe sab logon ko maarna shuru kiya.
Kritavarma aur Kripacharya bhi uske saath the.

Is raat ki khaufnaak ghatna ka naam hi hai—
Sauptika (soye huye ka vinaash).

Sirf Pandav paanchon aur Satyaki bach paye,
kyunki Krishna ne unhe pehle hi alag jagah sulaya tha.

⭐ Draupadi Ka Dard

Subah Drishtadyumna ka saarathi bhaagte hue Pandavon ke paas aaya.
Usne pukar kar bataya:

“Ashwatthama ne sabko raat me maar diya!”

Draupadi yeh sun kar toot gayi.
Usne kaha:

“Main bina badla liye jeena nahi chahti.”

Woh upvaas karke marne ko tayyar ho gayi.

⭐ Bhima Ka Sankalp

Draupadi ke dukh se Bhima ka khoon khol utha.
Usne apni gada uthayi aur garja:

“Ashwatthama! Tujhe main abhi dhoondh kar aaunga!”

⭐ Brahmashastra (Celestial Weapon) Ka Vinash

Dar se ghabra kar
Ashwatthama ne ek divy astra (celestial weapon) chhod diya.
Usne kaha:

“Yeh Pandavon ka vinaash karega!”

Par Krishna ne turant kaha:
“Yeh nahi hoga.”
Aur us astra ki taakat rok di.

Phir Arjun ne apna divya astra chala kar
Ashwatthama ke astra ko neutralize kiya.

⭐ Ashwatthama Par Shaap

Ashwatthama ki buri soch dekhkar
Vyasa ji aur Krishna ne use shaap diya.
Ashwatthama ne bhi badle me kuch ulte vaachan bole,
par uski taakat khatam hoti ja rahi thi.

Pandavon ne uske sir se
uska mani (head jewel) cheen liya—
jise wo bachpan se dharan kiye tha.

Ye hi Draupadi ko diya gaya
taaki uska dukh halka ho sake.

⭐ Parva 10 Samapt

Is tarah Sauptika Parva me—

Ashwatthama ne raat me soye yoddhon ko maara

Draupadi ro uthi

Bhima peeche pada

Ashwatthama ne divy astra chhoda

Krishna aur Arjuna ne use rok diya

Ashwatthama ka mani chheen liya gaya

Is parva me 18 sections aur 870 shlokas hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.13"):
            text1 = """ 
⭐ Parva 11 – Stri Parva (Women’s Lament)

(short • simple • emotional but not poetic • Hinglish)

Mahabharat ka yudh khatam ho chuka tha.
Ranbhoomi me har taraf shaant hawa chal rahi thi,
par logo ke dil me tufaan tha.

⭐ Dhritarashtra ka Gussa aur Dard

Andhe raja Dhritarashtra ko jab pata chala
ki uske saare bete mar gaye,
toh uska dard bahut gehra tha.

Usne socha Bhima uske saamne khada hai
aur gusse me usne ek aadmi ko gale lagakar
zor se kuchal diya…

Par woh Bhima nahi tha.
Krishna ne chhupkar lohe ka ek murti rakh di thi,
taaki Bhima bach jaye.

Dhritarashtra ka dard ab aur badh gaya."""
            create_image_text_layout("attached_assets/chapter1/1.2.13.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Vidura Ka Sacha Sneh

Vidura ne unke paas aa kar
pyaar se samjhaya:

“Rajaji, duniya ka saara dukh ek sapna jaisa hai.
Aap apna mann shaant rakhiye.”

Dhritarashtra dhire dhire shaant hone lage.

⭐ Ranbhoomi Par Raniyon Ka Vilap

Raja Dhritarashtra aur ghar ki saari raniyan
ranbhoomi dekhne gayi.

Waha unhone
apne bete, pati, bhai aur pita
sabko gira hua dekha.

Har taraf rone ki aawaz thi.
Sab aurate gir gir kar vilap kar rahi thi.

Is parva ko “Stri Parva”
isiliye kaha jaata hai—
kyunki yeh auraton ke dard ki kahani hai.

⭐ Gandhari ka Shraap

Apne 100 putron ki laash dekhkar
Gandhari ka dard kisi pahad jaisa tha.

Usne gusse me Krishna ko bhi dosh diya
aur behosh ho gayi.

Krishna ne dheere se unka gussa shaant kiya
aur unhe sambhala.

⭐ Antim Sanskar

Phir Yudhishthira,
jo sabse dharmic aur samajhdaar raja tha,
ne sab mare hue yoddhon ka
poore vidhi vidhan se antim sanskar karaya.

Sab rajaon ke liye paani ka tarpan bhi hua.

⭐ Kunti ka Raaz – Karna ka Janm

Isi samay ek bahut bada raaz khula.

Kunti roti hui boli:

“Karna mera pehla beta tha…
mainne use bachpan me hi chhod diya tha.”

Pandav yeh sunkar toot gaye.
Unhe pata chala ki
unhone apne hi bhai se yudh me ladai ki.

Sabki aankhon me aansu aa gaye.

⭐ Parva 11 Samapt

Stri Parva me—

Dhritarashtra ka dard

Raniyon ka vilap

Gandhari ka shraap

Yudhishthira ka dharm

Kunti ka raaz

sab kuch bahut hi dukh bhara hissa hai.

Is parva me 27 sections aur 775 shlokas hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.14"):
            text1 = """ 
⭐ Parva 12 – Shanti Parva (Shanti & Gyaan ka Parva)

(Yudhishthira ka dukh • Bhishma ka gyaan • Moksha ke rahasya)

Yudhishthira yudh jeet gaya tha,
par uske dil me shanti nahi thi.

Woh ro raha tha aur soch raha tha—

“Mainne apne hi rishtedaar kyun maar diye?
Bhai, chacha, guru, bachche… sab kho diye.”

Tab Krishna ne kaha:
“Bhishma abhi zinda hain.
Woh tumhe sahi raasta batayenge.”

Bhishma ji teeron ke bistar par pade the,
par unka gyaan pahaad jaisa mazboot tha."""
            create_image_text_layout("attached_assets/chapter1/1.2.14.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Bhishma ka Amrit-Gyaan

Bhishma ne Yudhishthira ko
dharma, nyay, raja-dharma, dayitva,
aur mushkil waqt me kya karna chahiye—
sab kuch badi pyaar se samjhaya.

Unhone bataya:

Sahi waqt pe sahi kaam karna hi dharma hai.

Raja ko daya bhi chahiye aur himmat bhi.

Gussa, lalach aur jhooth sabse bada dushman hai.

Ant me moksha ka raasta sirf gyaan aur satya se milta hai.

Shanti Parva me 339 sections
aur 14,732 shlokas hain.

Yeh Mahabharat ka sabse bada gyaan-parva maana jata hai.

⭐ Parva 13 – Anushasana Parva (Niyamon aur Dharam ka Parva)

(Daan ka gyaan • Satya ki shakti • Bhishma ka swarg gaman)

Bhishma ji ka gyaan sunkar
Yudhishthira ka mann shaant hone laga.

Is parva me Bhishma ne bataya:

Sahi daan kaise diya jata hai.

Kisko daan dena chahiye, kisko nahi.

Sachchai sabse bada dharma hai.

Brahman aur gau—dono bahut pavitra hain.

Har kaam ka ek sahi waqt aur jagah hoti hai.

Unka gyaan paakar
Yudhishthira fir se majboot ho gaya.

Aur phir ek din…
Bhishma ji ne apna shareer chhod diya aur swarg chale gaye.

Anushasana Parva me 146 sections
aur 8,000 shlokas hain.

⭐ Parva 14 – Ashwamedhika Parva (Ashwamedh ka Parva)

(Ashwamedh yagna • Arjuna ki yatra • Parikshit ka janm)

Yudhishthira ne sabse pehle
Ashwamedh Yagna karne ka faisla kiya
taaki desh me shanti ho aur rajya majboot bane.

Ek ghoda chhoda gaya,
jise rokne wala kisi bhi raja se
Arjuna ladta tha.

⭐ Arjuna ki Yatra aur Yuddh

Arjuna ne ghode ke peeche peeche
poori duniya ka chakkar lagaya.

Kayi raja gusse me aakar
ghode ko rokna chahte the,
par Arjuna ne sabko hara diya.

Ek din Arjuna ka
apne bete Vabhruvahana se hi yuddh ho gaya!
Arjuna be-hosh pad gaya, par baad me
Krishna ki kripa se sab theek hua.

⭐ Parikshit ka Janm

Is parva me ek bada chamatkar bhi hua:

Ashwatthama ke brahmastra se
Uttara ke garbh me jo bachcha jal gaya tha,
Krishna ne usse phir zinda kar diya.

Wohi bachcha tha—
Raja Parikshit,
जो आगे चलकर Mahabharat ki vansh ko badhayega.

⭐ Mongoose ki Kahani

Yagna ke dauran ek ajeeb neela-bhoora mongoose aaya
aur ek adbhut moral story sunai
ki sacha daan sirf dil se hota hai,
na ki dikhave se.

Ashwamedhika Parva me 103 sections
aur 3,320 shlokas hain."""
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.15"):
            text1 = """ 
⭐ Parva 15 – Ashramvasika Parva

(Jungle ka safar • Purani dosti • Antim shanti)

Duryodhana aur sab yudh mein mar chuke the.
Tab Dhritarashtra, Gandhari, aur Vidura—
apni bachi-kuchi zindagi jungle mein bitane ka faisla karte hain.

Yudhishthira unke liye sab kuch karna chahta tha,
par old couple ke mann me shahar ki zindagi ka koi laalsa nahi tha.

Unhe jaana hi tha.

Kunti (Pritha) ne yeh dekha
aur apne beto ka mahal chhodkar
apne devar aur devrani ke peeche jungle ki or chal padi.
Wohi to unka kartavya tha—
“Apne bade logon ka hamesha saath nibhana.”"""
            create_image_text_layout("attached_assets/chapter1/1.2.15.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Vyasa ka Chamatkar

Jungle me ek raat,
Vyasa rishi ne apni yog-shakti se
sab mare hue Rajkumar, putra, aur yodhha
ek pal ke liye wapas dikha diye.

Dhritarashtra aur Gandhari apne bachchon ko dekh kar
pal bhar ko roye bhi, Muskuraaye bhi.
Is milan se unka dard halka ho gaya.

Uske baad…
Dono ne apna sharir chhod diya
aur apne punyon ka phal paakar
param shanti me chale gaye.

Vidura bhi, jo hamesha dharma par tikke rahe,
shanti se apni yatra poori kar lete hain.

⭐ Sanjaya aur Vrishni Vansh ki Khabar

Sanjaya bhi akhir me swargiya stithi ko prapt hota hai.
Fir Narada Yudhishthira ko batata hai
ki Vrishni vansh—Krishna ka vansh—
bhi apni kismat se bach nahi paya.

Parva 15 me 42 sections aur 1506 shlokas hain.

⭐ Parva 16 – Mausala Parva

(Krishna ke vansh ka patan • Arjuna ki kamzori)

Is parva ki kahani bahut dukh bhari hai.

⭐ Shraap aur Vinash

Krishna ke vansh—Vrishnis aur Andhakas—
ek Brahmana ke shraap se pareshaan ho gaye.

Ek din sab yadu log
nasha karke samundar kinare ladne lage.
Unke haath me ek Eraka ghaas tha
jo shraap se vajra (thunderbolt) jaisa ban gaya.
Aur sabne ek-dusre ko maar dala.

⭐ Krishna aur Balarama ka Ant

Sabko marte dekhkar
Balarama ne apni pran-yatra poori kar li.
Krishna bhi samay ke niyam se
apna shareer chhod dete hain.

Samay ke saamne koi nahi tikta—even Krishna.

⭐ Arjuna ka Dwaraka Jaana

Arjuna Dwaraka pahunchta hai
par poori nagri sunsaan hoti hai.

Krishna nahi.
Balarama nahi.
Vrishni vansh khatam.

Arjuna rone lagta hai
par fir bhi zimmedari le kar
bache hue bachche aur mahilao ko le jaata hai.

Raaste me daku un par hamla karte hain.
Arjuna apna Gandiva uthane ki koshish karta hai
par bow kaam hi nahi karta.

Tab Arjuna samajh jata hai—
“Meri yoddha ki yatra ab poori ho gayi.”

Vyasa ke kehne par
Arjuna sanyas lene ka faisla karta hai.

Mausala Parva me 8 sections aur 320 shlokas hain.

⭐ Parva 17 – Mahaprasthanik Parva

(Antim yatra • Satya ka pariksha)

Pandavon ne sab rajya chhod diya.
Draupadi ko saath liya
aur Himalaya ki or
apni aakhri yatra shuru ki.

Is yatra ko hi Mahaprasthana kehte hain—
“Mahaan chhod.”

⭐ Gandiva ka Vapsi

Raste me unhe Agni dev milte hain.
Agni ke kehne par
Arjuna apna Gandiva aur dev-astra
wapas de deta hai.

Ab unhe yuddh ki nahi,
sirf shanti ki zarurat thi.

⭐ Ek-ek karke sab girte gaye

Yatra kathin thi.

Pehle Draupadi giri.
Phir Sahadeva.
Phir Nakula.
Phir Arjuna.
Phir Bhima.

Sab gir gaye…
par Yudhishthira ne kabhi peeche mudkar nahi dekha.

Kyun?

Kyuki yeh antim pariksha thi—
asakti se mukti ki.

Sirf dharma-raj hi is pariksha me safal hote hain.

Mahaprasthanik Parva me 3 sections aur 320 shlokas hain."""
            create_image_text_layout(text_content=text2, layout="full")
        with st.expander("Section 1.2.16"):
            text1 = """ 
⭐ Parva 18 – Svarga Parva (Swargarohan)

(Dharma ki antim jeet • Sachchai ka inaam)

Pandav apni last journey me ek-ek karke gir gaye the.
Sirf Yudhishthira—Dharma-raj—bacha tha.
Uske saath bas ek chota sa dog chal raha tha.

⭐ The Celestial Chariot Arrives

Swarg ka vimaan (heavenly chariot) aaya
aur devdut bole:

“Raja Yudhishthira, chaliye, aapka swarg yatra tayyar hai!”

Par Yudhishthira ne kaha:

“Main bina is dog ke nahi jaaunga.”

Devdut ne samjhaya,
“Swarg me animals allowed nahi hai.”

Par Yudhishthira ne firm karke kaha:"""
            create_image_text_layout("attached_assets/chapter1/1.2.16.jpg", text1, layout="side", image_position="left")

            text2 = """ 
“Jo mujh par bharosa karke aaya,
jiska main saathi hoon,
main usey chhod kar kabhi nahi jaaunga.”

Tab achanak…
Woh dog Dharma Devta (god of justice) ban kar saamne aaye!

Unhone kaha:

“Yudhishthira, tumne dosti aur dharma ka sabse bada imtihaan paas kar liya.
Ab tum sach me swarg ke layak ho.”

⭐ Swarg aur Narak ka Rahasya

Yudhishthira swarg ke vimaan me chadhte hi
tez dard mehsoos karta hai.
Usse ajeeb lagta hai.

Devdut usey narak (hell) ka darshan karwate hain.
Wahan usse apne bhaiyon ki dard bhari cheekhein sunayi deti hain.

Yudhishthira ka dil toot jata hai:
“Mere bhai narak me kaise?”

Woh kehta hai:

“Main yahin unke saath rahunga.
Unhe akela nahi chhodunga.”

Tab Dharma aur Indra prakat hote hain aur kehte hain:

“Yeh sab sirf tumhari pariksha (test) thi.
Tumhari karuna (compassion) dekhne ke liye.
Tumhare bhai swarg me hi hain.
Ek pal ke liye unhe dukh ka darshan karaya gaya,
taaki tumhari satyata (truthfulness) parakh sake.”

⭐ Final Liberation

Phir Yudhishthira apna sharir chhod kar
celestial Ganga me doobki leta hai
aur ek divya shareer (heavenly body) prapt karta hai.

Uske baad woh swarg me pravesh karta hai—
jahaan Indra aur sab dev uska swagat karte hain.

Woh anant shanti aur khushi me rehne lagta hai.

⭐ Mahabharata ka Ant Ka Sandesh

Sauti rishi sabhi shrotaon ko kehate hain:

“Mahabharata sab gyaan se bada hai—
dharma (righteousness), artha (wisdom), aur kama (proper desire) ka deep gyaan yahi se milta hai.

Jo Mahabharata sunta hai,
use anya kahaniyaan pheeki lagti hain—
jaise koil ki madhur aawaz ke saamne
kauwe ki kaa-ka.”

Aur:

“Jo Bharata roj padhta hai,
woh paap se mukta ho jata hai—
jaise pavitra Pushkara snaan (holy bath) se hota hai.”

Mahabharata hi sab purano ka aadhaar hai.
Ye sabse bada itihaas hai,
sabse zyada shiksha dene wala granth."""
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.3
    with st.expander("Chapter 1.3 – Paushya Parva (Story of King Paushya)"):

        # Section 1.3.1
        with st.expander("Section 1.3.1"):
            text1 = """ 
⭐ Janamejaya aur Sarama ka Shraap

(Hinglish Kahani – Children’s Story Style)

Kurukshetra ke maidan me Raja Janamejaya aur uske teen bhai—Srutasena, Ugrasena, Bhimasena—ek lamba yagna kar rahe the.

Tabhi wahan ek celestial dog ka baccha (Sarama ka putra) aa gaya.
Janamejaya ke bhaiyon ne bina wajah usse maar diya.
Bechara bachcha dard se rota-rona apni maa Sarama ke paas bhaag gaya.

Sarama ne pucha:
“Kya hua? Kisne maara tumhe?”

Baccha bola:
“Janamejaya ke bhaiyon ne! Maine kuch galat nahi kiya. Na ghee chua, na dekha.”"""
            create_image_text_layout("attached_assets/chapter1/1.3.1.jpg", text1, layout="side", image_position="left")

            text2 = """ 
Sarama ko bahut gussa aaya.
Woh seedha yagna sthal par pahunchi.

Usne Janamejaya se kaha:

“Mere bete ne koi galti nahi ki. Phir bhi tumhare bhaiyon ne use mara.
Iska phal tumhe bina bataye, achanak milega.”

Yeh sunkar Janamejaya bahut pareshaan ho gaya.

⭐ Janamejaya Ki Chinta

Yagna ke baad woh Hastinapur laut gaya aur sochne laga:

“Kaun mera paap mita sakta hai?”

Ek din shikar par, usse ek rishi ka ashram dikha—
Rishi ka naam tha Srutasrava, aur unka beta Somasrava ek tapasvi tha.

Janamejaya ne rishi se kaha:
“Aapka beta mera purohit ban jaye.”

Rishi ne kaha:

“Mera beta saarp-kanya se janma hai. Bahut pavitra aur tapasvi hai.
Woh sab paap mita sakta hai—
bas Mahadev ke khilaf ki gayi galti nahi.
Aur ek aadat hai:
Jo bhi brahman usse kuch mangega—woh de dega.”

Janamejaya bola:
“Theek hai, main manzoor karta hoon.”

Aur woh Somasrava ko apna purohit bana kar le gaya.

⭐ Guru Dhaumya aur Aruni – Sampoorna Nishaane Waali Seva

Isi samay ek mashhoor guru the—Ayodha Dhaumya.
Unke teen shishya: Upamanyu, Aruni, aur Veda.

Ek din unhone Aruni ko kaha:

“Farm ka paani bhaag raha hai. Ja, naala bandh kar de.”

Aruni gaya…
Par paani ruk hi nahi raha tha.

Kaafi koshish ke baad usne socha:
“Main hi ruk jaata hoon.”

Woh khud paani ki darar me let gaya,
aur apne sharir se paani ka rasta rok diya.

Bahut der baad Dhaumya ne poocha:
“Aruni kahan gaya?”

Shishyon ne bataya.
Rishi sabko lekar us khet me gaye aur awaaz lagayi:

“Aruni beta, kahan ho?”

Awaaz sunte hi Aruni uth kar bahar aaya,
pura bheega hua.

Woh bola:

“Guruji, rasta band nahi ho raha tha…
toh main hi wahin let gaya.
Aapki awaaz sunte hi utha.
Ab batayein, kya karna hai?”

Guru Dhaumya ne pyaar se usse gale lagaya aur kaha:

“Aaj se tumhara naam hai Uddalaka Aruni—
sacha guru-bhakt.”"""
            create_image_text_layout(text_content=text2, layout="full")
            # Section 1.3.1
        with st.expander("Section 1.3.2"):
            text1 = """ 
Guru Dhaumya ne Aruni ko aashirvaad diya aur bola:
“Ab tumhara naam Uddalaka hoga. Tumne guru ka aadesh maana, isliye tumhe gyaan aur shubh phal milega.”

Aruni khush hokar apne ghar laut gaya.

⭐ Upamanyu ko Gauon ki Seva ka Kaam

Ab Guru Dhaumya ne dusre shishya ko bulaya—
uska naam tha Upamanyu.

Guruji bole:
“Beta, jao aur gaayen charao.”

Upamanyu poora din gaayen charata,
shaam ko wapas aakar guru ko pranam karta.

Guruji ne dekha ki Upamanyu ka sharir ab bhi mota-taazaa lag raha tha.
Unhone pucha:

“Beta, tum khaate kya ho? Itne tandurust kaise ho?”

Upamanyu seedha-saadha ladka tha.
Woh bola:

“Guruji, main bhiksha maang kar kha leta hoon.”

Guruji bole:
“Bhiksha ka poora hissa pehle guru ko dena chahiye.”

Upamanyu ne haan me sir hila diya."""
            create_image_text_layout("attached_assets/chapter1/1.3.2.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Guru ki Seva – Par Badhte Imtihaan

Agli shaam, Upamanyu fir bhiksha lekar aaya,
aur saara guru ko de diya.

Par fir bhi woh taazaa hi laga.

Guruji ne pucha:
“Ab kya khaate ho?”

Upamanyu bola:
“Main dobara bhiksha maang leta hoon, guruji.”

Guruji ne samjhaya:
“Isse doosre bhikshukon ka haq chhin jata hai.
Yeh sahi nahi.”

Upamanyu ne turant sewa me swikaar kiya.

⭐ Doodh Pina bhi Mana

Kuch din baad bhi woh achha dikh raha tha.
Guruji ne pucha:

“Ab kya kha rahe ho?”

Upamanyu bola:
“Guruji, gaayon ka doodh pee leta hoon.”

Guruji bole:
“Bina humse poochhe doodh peena galat hai.”

Upamanyu ne phir ‘theek hai’ kaha.

⭐ Ab Toh Jhaag bhi Mana!

Fir ek din guruji ne dekha ki Upamanyu fir bhi taazaa lag raha hai.

Unhone pucha:
“Ab kya khaate ho?”

Upamanyu bola:
“Jab bachde doodh peete hain, jo jhaag girti hai…
main sirf wahi chaat leta hoon.”

Guruji ne kaha:
“Yeh bachdon ka haq hai. Tum isse bhi mat chhoo.”

Upamanyu ne fir haan me sir hila diya.

⭐ Bhookh Se Andha, Aur Gaddhe Me Gir Gaya

Ab bechara Upamanyu
na bhiksha kha sakta,
na doodh,
na jhaag…

Ek din bhookh se pareshaan hokar
usne jungle me Arka plant ke patte kha liye.

Patte tez aur zehrele the.
Uski aankhen jalne lagi,
aur woh andha ho gaya.

Andha hokar dhad-a-dhad chalte hue,
woh ek gaddhe me gir gaya.

⭐ Guruji Dhundne Nikle

Shaam tak Upamanyu wapas na aaya.
Guruji bole:

“Woh bechara to kuch bhi nahi kha sakta…
chalo use dhoondte hain.”

Sab shishya jungle me gaye aur pukarne lage:

“Upamanyu! Upamanyu!”

Neeche se awaaz aayi:
“Guruji, main yahan hoon! Gaddhe me gir gaya hoon!”

Upamanyu ne sab bataya—
“Patte khaye, aankhen jal gayi, main andha ho gaya.”

⭐ Asvini Kumaron ka Mahima

Guruji ne kaha:
“Beta, Asvini Devtaon ka stuti karo.
Woh dev-vaidya hain.
Tumhari aankhen wapas aa jayengi.”

Upamanyu gaddhe me baitha-baitha
poore bhakti se Asvini Kumaron ki prarthna karne laga.

Uske shabd seedhe aur pure the—
usne unka shukriya kiya, unki shakti ko yaad kiya,
aur unse apni aankhen wapas maang li."""
            create_image_text_layout(text_content=text2, layout="full")
            # Section 1.3.1
        with st.expander("Section 1.3.3"):
            text1 = """ 
⭐ Upamanyu aur Asvini Devtaon ka Ashirvaad

(Hinglish Children’s Story Version)

Upamanyu ne Asvini Devtaon ki sachchi prarthna ki.
Devta khush ho gaye. Unhone kaha:

“Beta, hum tumse prasann hain. Yeh cake lo aur kha lo.”

Upamanyu ne namrata se bola:
“Main bina guru ko diye kuch nahi kha sakta.”

Asvini Dev bole:
“Tumhare guru ne bhi humse yahi cake liya tha.
Aur bina kisi ko diye kha liya tha.
Tum bhi waise hi kar lo.”

Par Upamanyu ne phir mana kar diya.
Woh bola:

“Maaf kijiye, Devtaon.
Guru ki ijazat ke bina main kuch nahi le sakta.”

Asvini Dev uski guru-bhakti se bahut khush hue.
Unhone bola:

“Tumhare guru ke daant kaale hain,
par tumhare daant sone ke honge!
Aur hum tumhe nazar bhi wapas dete hain.
Tumhara bhavishya bhi shubh hoga!”

Aur bas—Upamanyu ki aankhen theek ho gayi.

Woh daud kar apne guru ke paas gaya,
sab kuch bataya.
Guru Dhaumya bahut khush hue.

Unhone aashirvaad diya:

“Tumhe sab Vedo ka gyaan milega.
Tumhara jeevan safal hoga.”

Yeh thi Upamanyu ki kasauti —
aur uski guru-bhakti jeet gayi."""
            create_image_text_layout("attached_assets/chapter1/1.3.3.jpg", text1, layout="side", image_position="left")

            text2 = """ 
⭐ Veda ki Pareeksha

Guru Dhaumya ka teesra shishya tha Veda.
Guruji bole:

“Veda, tum kuch samay yahan raho aur seva karo.”

Veda bina shikayat ke kaam karta:
garmi, sardi, bhookh, pyaas—sab seh leta.
Bilkul ek mazboot bail ki tarah.

Guruji usse bahut khush hue.
Unko ashirvaad mila—
gyaan, sukh aur achha bhavishya.

⭐ Veda ka Naya Shishya – Utanka

Padhaayi ke baad Veda grihastha ban gaya.
Uske teen shishya the.
Yahin se kahani me aata hai Utanka.

Veda kisi shishya pe zor-zabardasti nahi karta tha.
Woh kehta tha:

“Maine khud takleef jheli hai,
isliye main apne shishyon se kathor vyavahar nahi karunga.”

Ek din, King Janamejaya aur Paushya ne
Veda ko apna guru banaya.

Kuch samay baad Veda ko ek yatra par jaana tha.
Woh Utanka ko bolkar gaye:

“Beta, jab tak main nahi hoon,
ghar ka dhyaan tum rakhna.”

⭐ Utanka ki Imaandari

Jab Veda ghar se bahar the,
ghar ki mahilaon ne Utanka se kaha:

“Guruji ghar par nahi hain.
Guru Maa ab santaan-yogya kaal me hain.
Tum unke sthaan-parivartan ka kaam karo.”

Matlab—
Woh Utanka ko bahka rahi thi ki woh kuch anuchit kare.

Par Utanka ne sidha mana kar diya.
Woh bola:

“Guru ji ne mujhe yeh nahi kaha.
Main kuch galat nahi karunga.”

Guru ji wapas aaye aur sab suna.
Woh bahut khush hue.

“Beta, tumne maryada nibhayi.
Tumhe jo var chahiye, maang lo.”

⭐ Guru Dakshina ki Mang

Utanka bola:

“Guruji, main bina guru-dakshina diye nahi jaa sakta.
Kuch bataiye, main kya laoon?”

Veda ne kaha:

“Apni Guru Maa se pucho.”

Utanka guru-patni ke paas gaya.
Unhone kaha:

“King Paushya ki Rani ke kaan me jo jhumke hain,
woh laa do.
Chaar din baad ek pooja hai.
Mujhe woh pehenne hain.
Le aayoge toh tumhara bhala hoga.”

⭐ Utanka ka Rahasya-yatra

Raste me Utanka ne ek vishal bail aur
ek ajeeb aadmi ko dekha.

Woh aadmi bola:
“Is bail ka gobar kha lo.
Tumhare guru bhi kha chuke hain.”

Utanka ne guru-bhakti se
bina sawaal kiye gobar aur mutra grahan kar liya.
(Asli kahani me yeh divya-symbolic kriya thi.)

Phir woh King Paushya ke mahal me gaya
aur rani se jhumke le liye.

Rani ne chetavani di:

“In jhumko par saap-raja Takshak ki nazar hai.
Sambhal kar jaana!”

Utanka ne muskura kar bola:
“Woh mujhe kuch nahi kar sakta.”"""
            create_image_text_layout(text_content=text2, layout="full")
            # Section 1.3.1
        with st.expander("Section 1.3.4"):
            text1 = """ 
⭐ Utanka aur Raja Paushya: Ek Lambi Yatra Ki Kahani

(Hinglish Story Version)

Utanka ne Raja Paushya se kaha:
“Main ruk jaata hoon. Kripya saaf khaana jaldi lekar aao.”

Raja ne haan kaha aur Utanka ko bhojan diya.
Par Utanka ne dekha ki khana thanda tha aur usme baal bhi the.
Woh gussa ho gaya.

Usne Raja se kaha:
“Aapne mujhe ganda khana diya hai. Isliye aap andhe ho jaaoge!”

Paushya ne turant jawab diya:
“Aur tum, jo saaf khane ko bhi ganda keh rahe ho, tum bachon se vanchit ho jaoge!”"""
            create_image_text_layout("attached_assets/chapter1/1.3.4.jpg", text1, layout="side", image_position="left")

            text2 = """ 
Utanka bola:
“Aap khud dekh lo. Khana sach me ganda hai.”

Raja ne dekha — haan, khana sach me thanda aur baalon se bhara tha.
Woh sharminda hua.

Paushya ne kaha:
“Mujhe maaf karo. Khana dhyaan se nahi bana.”

Utanka ne kaha:
“Meri baat puri hogi. Aap andhe honge… par zyada der nahi.”

Paushya bola:
“Main apna shraap wapas nahi le sakta.
Main Kshatriya hoon — mere shabd naram hote hain, par dil sakht hota hai.”

Utanka ne shanti se jawaab diya:
“Mere upar aapka shraap nahi chalega, kyunki khana sach me ganda tha.”

Phir Utanka jhumko lekar rasta chal diya.

⭐ Takshak Ka Dhoka

Raste me Utanka ne ek aadmi ko dekha —
Nangaa, gareeb, ajeeb sa.

Woh aadmi kabhi dikhta, kabhi gayab ho jaata.
Utanka ne jhumke zameen par rakhe aur paani lene chala gaya.

Bas tabhi woh aadmi jhumke chura kar bhaag gaya.

Utanka bhaaga.
Usne us aadmi ko pakad liya.

Par jaise hi pakda —
Aadmi badal gaya!
Uski asli roop tha:

⭐ Takshaka, saapon ka raja!

Takshaka ek bade suraakh me ghus gaya.
Utanka uske peeche hilte-dulte lakdi se gadda khodta raha.

Utanka pareshaan ho gaya.
Indra ne aasman se uski mushkil dekhi.
Indra ne apna vajra (thunderbolt) bheja.

Vajra ne gadda aur bada kar diya.
Utanka andar ghus gaya.

⭐ Naagon Ka Shehar

Andar Utanka ne dekha —
Ek alag hi duniya thi.
Naagon ke mahal, shehar, badi imaratein,
Sab roshni se chamak rahi thi.

Utanka ne naagon ki prarthna ki.
Lekin jhumke fir bhi nahi mile.

Phir usne ajeeb drishya dekhe:

Do auratein — kale aur safed dhage se kapda bun rahi thi.

Ek bada chakra, 12 spokes ka,
jise 6 ladke ghumaa rahe the.

Ek sundar ghoda aur ek tej-chamakta aadmi.

Utanka ne un sab ko mantr padhkar pranaam kiya.
Ghode wale aadmi ne kaha:

“Main prasann hoon. Batao kya chahiye.”

Utanka bola:
“Mujhe saare saanp mere vash me chahiye.”

Aadmi ne kaha:
“Is ghode me foonk maaro.”

Utanka ne foonk maari.
Ghoda ekdum aag ban gaya!

Aag saapon ki nagri me phailne lagi.
Takshaka pareshaan ho kar bhaaga.
Usne jhumke laa kar Utanka ko de diye:

“Please, yeh le lo! Bas aag roko!”

Utanka ne jhumke le liye.

⭐ Utanka Ghar Wapas

Usne socha:
“Aaj meri guru-patni ka pooja ka din hai.
Main itni door hoon… kaise pahunchun?”

Tabhi ghode wala aadmi bola:
“Is ghode par chadho. Tum pal bhar me pahunch jaoge.”

Utanka chadha — aur bas,
Chutkiyon me guru ke ghar.

Guru-patni use dekh kar khush hui:
“Tum sahi waqt aa gaye, beta!
Main tumhe shraap dene hi wali thi!”

Utanka ne jhumke de diye.

Guru ne poocha:

“Beta, itni der kahan the?”

Utanka ne sab bata diya.
Guru ne kaha:

Do auratein = Dhata aur Vidhata

Kale-safed dhage = din aur raat

Chakra = saal ke 12 mahine

6 ladke = 6 ritu (seasons)

Ghoda = Agni

Aadmi = Indra

Bail = Airavata

Bail ka gobar = Amrit

“Isliye tum Nagon ki nagri se zinda wapas aaye ho.”

Guru ne aashirvaad diya aur Utanka ko bhej diya.

⭐ Takshaka se Badla

Utanka dil me gussa le kar Hastinapur gaya.
Waha Raja Janamejaya ko mila.

Raja baithak me tha, mantriyon se ghera hua.

Utanka bole:

“Raja ji, aap yahan aaram se kyun baithe ho?
Ek bahut zaroori kaam hai!”

Raja ne poocha:
“Kaunsa kaam?”

Utanka ne kaha:

**“Aapke pita Maharaj Parikshit ki maut
Takshaka saap ne ki thi.

Aapko badla lena chahiye.
Poora sarpa-yagya karo.
Takshaka ko jala daalo!”**

Raja Janamejaya gusse se bhar gaya.
Usne shraaddh ke baad sab sun kar dard me ro pada.

Yahi se shuru hota hai
Mahabharat ka Sarpa-Yagya Kand."""
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.4
    with st.expander("Chapter 1.4 – Pauloma Parva (Story of the Pauloma Demons)"):

        # Section 1.4.1
        with st.expander("Section 1.4.1"):
            text1 = """ 
⭐ Sauti aur Naimisha Ka Maha-Yagya

(Hinglish Kahani Version)

Naimisha ke gehre van me ek bahut bada 12 saal ka yagya chal raha tha.
Is yagya ke adhyaksh the Saunaka Rishi, jinko sab log Kulapati kehte the.

Us jagah ek aur prasiddh vakta aaye —
Ugrasrava Sauti, Lomaharshana ka putra.
Woh purano ke bade gyani the, aur unhe kahaniyan sunane ka vishesh vardaan tha.

Sauti Rishiyon ke samne haath jod kar bole:

“Maine aapko Utanka ki kahani batayi—jo Janamejaya ke Sarpa-Yagya ka ek karan thi.
Ab bataiye, ab aap kya sunna chahte hain?”

Sab Rishi, jo waha yagya me seva me the, bole:

“Sauti, hum tumse bahut saari kahaniyan poochna chahte hain.
Par hamare guru, Saunaka Rishi, abhi havan kund me apni kriya poori kar rahe hain.
Hum unka intezar karte hain.”"""
            create_image_text_layout("attached_assets/chapter1/1.4.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Fir unhone Sauti ko Saunaka Rishi ke gun bataye:

Bahut gyaani

Shaant aur satya-bhashi

Ved aur Aranyaka ke maharathi

Tapasvi aur anushasan ke pakke

Dev-Asur kahaniyon ke pandit

Rishiyon ne kaha:

“Woh hamare sabse bade adhyaksh hain.
Unke aane par hi tum kahani aage badhana.”

Sauti ne vinamrata se kaha:

“Aisa hi hoga.”

⭐ Saunaka Rishi Ka Wapsi

Kuch der baad Saunaka Rishi apna pooja-paath poora karke wapas aaye.
Unhone devon ko pranam kiya, pitron ko jal chadhaya,
aur phir yagya-shala me sabhi tapasviyon ke beech apni sammanit aasan par baith gaye.

Sauti unke saamne chupchaap baitha tha, haath jode hue.

Sab Rishi shaant hokar baith gaye —
jaise koi bada gurukul ka varg shuru hone wala ho.

Tab Saunaka Rishi ne madhur aur gambhir awaaz me kaha:

“Sauti, ab tum shuru karo. Hum sunne ko taiyar hain.”

Aur is tarah shuru hoti hai
Mahabharat ki asli parampara —
Sauti dwara kahi gayi sabse pracheen kathaaen."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.2
        with st.expander("Section 1.4.2"):
            text1 = """ 
⭐ Bhrigu Parivaar Ki Kahani

(Hinglish Kahani Version)

Saunaka Rishi ne Sauti se pyaar se poocha:

“Beta, tumhare pitaji ne pura Purana aur Bharata suna tha.
Kya tumne bhi sab seekh liya?
Aaj hum sabse pehle Bhrigu vansh ki kahani sunna chahte hain.”

Sauti ne vinamrata se jawab diya:

“Haṁ, Rishi-jan, jo kuchh mere pita ne padha aur seekha, maine bhi wahi sab adhyayan kiya hai.
Ab main aapko Bhrigu vansh ki pracheen kahani sunata hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.4.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Bhrigu Parivaar – Ek Pavitra Parampara

Sauti ne kahani shuru ki:

Purano me likha hai ki Maharishi Bhrigu ko Brahma ji ne ek yajna ki agni se janm diya.
Bhrigu se ek beta paida hua—Cyavana.

Cyavana ka putra tha Pramati.

Pramati ka putra hua Ruru, jinka janm apsara Ghritachi (celestial dancer) se hua.

Ruru ke ghar janmiye Sunaka—jo Saunaka Rishi ke purvaj the.

Sunaka bade hi sajjan, vidwan, aur satya-bhashi the.
Sab unka samman karte the.

⭐ Cyavana Ka Naam Kaise Pada?

Saunaka ne beech me pooch liya:

“Sauti, batao Cyavana ko Cyavana kyon kaha gaya?”

Sauti ne kahani aage badhai.

⭐ Puloma aur Rakshas Ki Kahani

Bhrigu Rishi ki patni ka naam tha Puloma.
Ek din jab Bhrigu snan karne gaye, Puloma ghar me akeli thi—aur garbhavati bhi.

Tabhi wahan aa pahuncha ek Rakshas, jiska naam bhi Puloma tha.
Usne Puloma ko dekha aur turant mohit ho gaya.
Purva me, Puloma ke pita ne is Rakshas se vivaah ka vaada kiya tha,
par baad me Puloma ko Bhrigu ko de diya tha.

Is baat ka dard aur gussa Rakshas ke dil me ab bhi tha.

Puloma ne mehman dharm nibhaate hue Rakshas ko phal-mool diye.
Par Rakshas ke mann me bure iraade jag gaye.

Woh bola:

“Aaj main ise le jaunga. Ye pehle mera vaada kiya hua vivaah tha.”

Aur bina soche-samjhe, usne Puloma ko utha liya.

⭐ Agni Se Sawal

Rakshas Puloma ne dekha ki ghar me yajna ki agni jal rahi hai.
Woh agni se poochne laga:

“Agni dev, sach-sach batao—ye aurat mere adhikar me thi ya Bhrigu ki patni hai?
Tum devtaon ke muh ho, tum jhooth nahi bol sakte.”

Rakshas baar-baar poochta raha.
Agni dev bahut pareshaan ho gaye—
Sach bolenge to Rakshas jitega…
Jhooth bolenge to Bhrigu ka shraap (curse) milega.

Par agni to satya ke devta hain.
Isliye dheere-dheere unhone jawab diya:

“Rakshas, pehle tumne ise chaha zaroor tha,
par shaadi ki pavitra vidhi (holy rites) tumne nahi ki.
Iske pita ne ise Bhrigu ko vedic rituals se vivaah me diya.
Main khud iska sakshi (witness) hoon.
Ye Bhrigu ki patni hai.”

Agni dev ne jhooth nahi bola,
aur yahi satya keh kar unhone apne dharm ko nibhaya."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.3
        with st.expander("Section 1.4.3"):
            text1 = """ 
⭐ Cyavana Ka Janm Aur Agni Ka Shraap

(Hinglish Kahani Version)

Sauti ne kahani aage badhai:

⭐ Rakshas Ka Hamla

Jab Agni dev ne sach bata diya,
Rakshas Puloma bahut gusse me aa gaya.

Woh turant soor (boar) ke roop me badal gaya,
aur Puloma ko hawa se bhi tez raftaar se utha le gaya—
jaise soch bhi nahi paati, utni tezi se.

Puloma ke garbh me Bhrigu ka bachcha tha.
Jab usne ye atyachaar mehsoos kiya,
to gusse me bachcha maa ke garbh se gir padda.

Isi liye uska naam pada Cyavana —
“jo jhat se gir kar janma le.”"""
            create_image_text_layout("attached_assets/chapter1/1.4.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Rakshas Ka Ant

Jab Rakshas ne dekha ki
maa ki kokh se ek chamakta hua bachcha nikla hai,
jo sooraj ki roshni jaisa tej rakhta hai—
to woh darr se Puloma ko chhod diya
aur patak se neeche girte hi
bhasm (ashes) ban gaya.

Puloma roti hui apne narm-narm bacche Cyavana ko godh me liye chalne lagi.

⭐ Brahma Ji Ka Aana

Tabhi Brahma ji, sab ke Pitamah,
use rote hue dekh kar aa pahunche.

Unhone Puloma ko sambhala,
aur jo aansu uski aankhon se tapak rahe the,
wo milkar ek nadi ban gaye.

Nadi unke peeche peeche chali
aur Brahma ji ne uska naam rakha Vadhusara—
bahu ke aansuon ki nadi.

Wo nadi aaj bhi Cyavana Rishi ke ashram ke paas se guzarati hai.

Is tarah Cyavana,
Bhrigu ka tejashvi aur tapasvi putra janma.

⭐ Bhrigu Ka Krodh

Jab Bhrigu wapas aaye
aur apni patni aur naye janme bachche ko dekha,
to unka hriday gusse se bhar gaya.

Unhone Puloma se poocha:

“Tumhe Rakshas ne pehchana kaise?
Kaun tha jisne tumhara raaz usse bataya?
Main use shraap dunga!”

Puloma ne sharme se kaha:

“Agni dev ne mujhe pehchana diya.
Wahi Rakshas mujhe le gaya.
Par tumhare putra ke tej se hi
main bach gayi—
Rakshas to turant jal kar bhasm ho gaya.”

⭐ Agni Ka Shraap

Sauti batata hai:

Ye sunkar Bhrigu ka gussa aur bhadak gaya.
Unhone Agni ko shraap de diya:

“Agni!
Aaj se tum sab kuchh khaoge—
achha-bura, pavitra-apavitra sab!”

Agni dev behad dukhi hue,
par shraap ho chuka tha."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.4
        with st.expander("Section 1.4.4"):
            text1 = """ 
⭐ Agni Ka Shraap Aur Brahma Ji Ka Samadhan

(Hinglish Kahani Version)

Sauti ne aage kahani batayi:

⭐ Agni Dev Ka Dard

Bhrigu ke shraap se Agni dev bahut dukhi aur gusse ho gaye.
Unhone Bhrigu se kaha:

“Hey Brahmana, maine kya galti ki?
Mujhse sach poocha gaya, to maine sach bola.
Jo sakshi sach chupata hai, wo apne purvajon ko dukh deta hai.
Aur jo galat bayan deta hai, wo paap karta hai.
Main to sirf nyay kar raha tha!”

Agni ne ye bhi kaha:

“Main to devtaon aur pitron ka muh hoon.
Meri aag par hi unki bali di jaati hai.
Main sab kuchh kaise kha sakta hoon?”"""
            create_image_text_layout("attached_assets/chapter1/1.4.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Agni Dev Ka Antardhaan

Gusse aur dukh se bhar kar, Agni dev
sab yajnaon se gaayab ho gaye—
na havan me aaye,
na shaadi-vivaah me,
na kisi pooja me.

Jahan “Om”, “Svaha”, aur “Svadha” ki dhwani hoti thi,
wahan ab shanti aur andhera chhaa gaya.

Sab log—rishiyon se lekar devataon tak—
bahut pareshan ho gaye.

⭐ Rishiyon Aur Devataon Ki Fariyad

Rishi log devataon ke paas gaye:

“Agni ke bina koi pooja poori nahi hoti!
Kripa karke kuchh upaay batao!”

Phir sab mil kar Brahma ji ke paas gaye
aur unko puri baat batayi.

⭐ Brahma Ji Ka Bachan

Brahma ji ne Agni ko bulaya
aur bahut hi komal shabdon me kaha:

“Agni, tum jagat ke rakshak ho.
Tumhare bina yajna ruk jaayega.
Isliye samajhdaari se kaam lo.
Bhrigu ka shraap poora hoga—
par tum poore shreer se
‘bhojan karne wale’ nahi banoge.”

Fir Brahma ji ne samjhaaya:

**“Tumhari aag ka sirf ek chhota sa hissa
sab kuchh khaayega—
jaise jangli jaanwaron ke andar jo aag hai.

Par tumhari pavitra aag,
jo yajnaon me jalti hai,
woh hamesha shuddh rahegi.
Tumhara kaam hamesha ki tarah chalega.”**

Aur ant me kaha:

“Sooraj ki roshni sab kuchh shuddh kar deti hai—
waise hi tumhari aag bhi
jo chhuye use pavitra bana degi.”

⭐ Agni Dev Ka Sammaan Wapas

Agni dev ne shant hokar kaha:

“Jaise aap kahete hain, vaise hi hoga.”

Phir woh wapas yajnaon me aa gaye—
aur poora sansaar
khushi se bhar gaya.

Rishiyon ne phir se havan kiya,
devta prasann hue,
aur sabhi logon ne sukoon ki saans li.

⭐ Kahani Ka Saar

Aise hua Bhrigu ka shraap,
Puloma rakshas ka vinaash,
aur Cyavana Rishi ka janm."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.5
        with st.expander("Section 1.4.5"):
            text1 = """ 
⭐ Ruru Aur Pramadvara Ki Karun Kahani

(Hinglish Kahani Version)

Sauti ne aage bataya:

⭐ Ek Pavitra Vansh Ki Kahani

Bhrigu ke putra Cyavana ke ghar ek beta hua—Pramati.
Pramati ke ghar paida hua Ruru,
aur Ruru ka beta bana Sunaka.

Par kahani ka sabse dard bhara hissa
Ruru aur Pramadvara se juda hai."""
            create_image_text_layout("attached_assets/chapter1/1.4.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Pramadvara Ka Janm

Ek samay ek mahan Rishi the—Sthulakesa.
Bahut dayavaan, bahut shant.

Usi samay Gandharva raja Vishvavasu
aur Menaka Apsara ke sambandh se
ek nanhi bachchi janmi.

Menaka ne, bina daya ke,
wo bachchi nadike kinare chhod di
aur wapas swarg chali gayi.

Rishi Sthulakesa ne jab
us chhodi hui bachchi ko dekha,
to unka hriday pighal gaya.

Woh boli jaise devlok ka phool,
masoom aur roshni se bhari.

Rishi ne use godh le liya
aur uska palan-poshan kiya
jaise apni hi beti ho.

Unhone uska naam rakha—
Pramadvara,
kyonki uski achchai, sundarta
aur shanti sabse alag thi.

⭐ Ruru Ka Prem

Jab Ruru ne pehli baar Pramadvara ko dekha,
to unke hriday me prem ki jyoti jal uthi.

Woh bas usi ko jeevan-sangini banana chahte the.

Unhone apne pita Pramati se kaha,
aur Rishi Sthulakesa ne
khushi se Pramadvara ka vivaah Ruru se tai kar diya.

Sabhi log utsahit the.
Vivaah ki tithi bhi nirdharit ho gayi.

⭐ Vidhata Ki Likhi Rekha

Lekin byaah se kuchh din pehle
Pramadvara apni saheliyon ke saath khel rahi thi.

Bechari ne dekha hi nahi
ki ghaas ke neeche
ek zehreela saanp coil banaye pada tha.

Usne us par pair rakh diya.

Saanp ne turant
apne zehreelay daant uske sharir me utaar diye—
jaise kismet ka bijli-wala vaar.

Ek pal me hi
Pramadvara ka rang udh gaya.
Woh gir padi… behti hawa jaise sust.

Uski saheliyan cheekh uthi.
Rishiyon ke hriday toot gaye.

Woh Pramadvara,
jo kuchh pal pehle chamakti thi
suraj ki kiranon ki tarah,
ab wahan sthir padhi thi—
phool jaise, par sundarta me dard mila hua.

⭐ Ruru Ka Tootna

Jab Ruru ne yeh drishya dekha,
to unka dil patthar ki tarah bhar gaya.

Duniya unke liye ruk si gayi.

Unhone chupchaap
bheed se door jaakar
apne dard ko akela jhela—
jaise koi toda hua pankhi
jungle ke kone me ro raha ho."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.6
        with st.expander("Section 1.4.6"):
            text1 = """ 
⭐ Ruru Aur Pramadvara – Jeevan Ka Vachan

(Hinglish Kahani Version Continued)

Sauti ne kaha:

⭐ Ruru Ka Dard

Sabhi Brahman log
Pramadvara ke nishchetf shareer ke paas baithe the.

Ruru ka dil toot chuka tha.
Woh chup-chap gehre jungle me chala gaya
aur zor-zor se ro padā—
jaise dard ki aandhi chal rahi ho.

Woh baar-baar kehta:

“Haaye…
Meri komal, sundar Pramadvara
thandi zameen par padhi hai.

Agar maine kabhi daan kiya ho,
agar kabhi satya aur tapasya ki ho,
agar maine guru aur bado ka samman kiya ho—
toh meri Pramadvara laut aaye.

Agar bachpan se maine apne mann ko niyantran me rakha ho,
toh woh uth jaaye…
meri taraf ek baar muskura kar dekhe…”

Ruru ka har shabd
jungle me dard ki tarah goonj raha tha."""
            create_image_text_layout("attached_assets/chapter1/1.4.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Swarg ka Sandeshvahak

Tabhi aasman se
ek divya sandeshvahak aaya.

Usne komal vaani me kaha:

“O Ruru,
tum jo shabd dukh me bol rahe ho,
unse kisi mrityu-paye ko jeevan nahi mil sakta.

Pramadvara ki umr poori ho chuki thi.
Isliye tumhe apne dukh ko sambhalna chahiye.

Lekin…
devon ne pehle se hi
uske jeevan ka ek raasta rakha hai.

Agar tum chaho,
toh Pramadvara wapas jeevit ho sakti hai.”

Ruru ne aansuon bhari aawaz me poocha:

“Batayiye!
Kya karna hoga?
Main kuchh bhi karne ko taiyaar hoon.”

Sandeshvahak bola:

“Tum apni aadhi aayu
Pramadvara ko de do.

Tab woh uth jaayegi.”

⭐ Jeevan ka Ardhy-Hissa

Ruru ne bina pal bhar sochhe kaha:

“Main apni aadhi zindagi deta hoon.
Bas meri Pramadvara
phir se zinda ho jaaye.”

Tab Gandharva Raja
aur dev-doot
Dharma Dev ke paas gaye
aur prarthana ki.

Dharma Dev bole:

“Agar yeh sab ki ichchha hai,
toh Pramadvara
Ruru ki aadhi aayu lekar
punah jeevit ho jaaye.”

Aur vah hua.

⭐ Pramadvara Ka Wapas Aana

Pramadvara dheere-dheere uthi—
jaise gehri neend se jaagi ho.
Uska rang, uski komalta,
sab wapas aa gaya.

Ruru ne use dekha
toh unki aankhon se
khushi ke aansu beh nikle.

Us din, shubh muhurat me,
dono ka vivaah hua.
Dono ek-dusre ke saath
pyaar aur shanti se jeene lage.

⭐ Ruru Ka Saanpon se Vaada

Lekin Ruru ke mann me
ek gehra gussa baitha tha.

Unhone pratigya ki:
“Jo bhi saanp dikhega,
main use maar dunga.”

Isliye jab jab koi saanp milta,
Ruru gusse me usse mar deta.

⭐ Ek Purana Saanp Ka Sawal

Ek din Ruru ek bade jungle me ghoom raha tha.
Wahan usne ek bahut buddha saanp dekha—
Dundubha jaati ka.

Ruru ne turant apna danda uthaya
usko maarne ke liye.

Lekin buddhe saanp ne
komal aawaz me kaha:

“O Brahmana,
maine tumhara kya bigaada hai?
Tum mujhe kyon maarna chahte ho?”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.7
        with st.expander("Section 1.4.7"):
            text1 = """ 
⭐ Ruru Aur Sahasrapat – Saanp Ka Raaz

(Hinglish Kahani Rewrite)

Sauti ne kaha:

⭐ Ruru Ka Gussa

Buddhe saanp ki baat sun kar
Ruru ne dant bhincho kar jawab diya:

“Sun, saanp!
Meri patni Pramadvara—
jo meri saanson jaisi pyaari thi—
use ek saanp ne dasta tha.

Us din se maine kasam khayi:
Jitne saanp milenge,
sabko maarunga!

Isliye aaj tum bhi bacho ge nahi!”

Ruru ka gussa
jalti aag ki tarah tha."""
            create_image_text_layout("attached_assets/chapter1/1.4.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Dundubha Ka Vinamra Jawaab

Dundubha saanp dara hua tha,
par phir bhi shaant bolaa:

“O Brahmana,
jo saanp insaan ko daste hain
unse hum bilkul alag hote hain.

Hum Dundubha keval naam ke saanp hain—
hamari zindagi mushkilein bhari hai,
par hamme un bissile saap jaise
chaal-bhaag ka koi faayda nahi milta.

Dukh humara same hai,
par sukh kabhi nahi.

Isliye, Ruru,
galatfehmi me aakar
hume mat maaro.”

⭐ Ruru Ka Mann Badalta Hai

Ruru ne dekha ki saanp sach me dara hua hai,
aur koi burai bhi nahi kar raha.

Uska gussa dheere se thanda pad gaya.
Usne danda neeche kar diya
aur naram aawaz me bola:

“Thik hai…
Main tumhe nahi maarunga.

Par mujhe batao,
tum ho kaun?
Saanp hote hue bhi
insaan ki tarah baat kaise kar rahe ho?”

⭐ Ek Chhupa Sach

Dundubha ne gahri saans li
aur bola:

“O Ruru…
main asal me saanp nahi hoon.

Main ek Rishi tha—
Sahasrapat naam ka.

Par ek Brahmana ke shraap se
main is roop me aa gaya.”

Ruru hairaan reh gaya.

Usne poocha:

“Achha?
Par tumhe shraap kyon mila?
Aur kitni der tak
tumhe is tarah saap ki tarah rehna padega?”

Dundubha chup ho gaya—
jaise bhari yaadon me dub gaya ho.
Kahani ab uske shraap ki taraf badhne lagi..."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.8
        with st.expander("Section 1.4.8"):
            text1 = """ 
⭐ Ruru Aur Sahasrapat Ka Shraap – Saanp Ka Sach

(Hinglish Kahani)

Sauti ne kaha:

⭐ Sahasrapat Ki Purani Kahani

Dundubha—jo asal me Rishi Sahasrapat tha—
ne Ruru ko apni dukhbhari kahani batani shuru ki:

“Ruru… bahut saal pehle,
mera ek dost tha—Khagama.
Woh teekhi zubaan wala tha
par tapasya ki wajah se bahut shaktishaali bhi.”

Ek din Khagama Agni-hotra kar raha tha.
Main mazaak karne ke mood me tha…
to maine kanto wali ghaas se
ek nakli saanp bana liya
aur use daraane ki koshish ki.

Khagama ne jaise hi use dekha—
woh behosh ho gaya!"""
            create_image_text_layout("attached_assets/chapter1/1.4.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Shraap Ka Gussa

Hosh me aate hi,
woh gusse se kaanp utha:

“Tu ne mujhe nakli saanp se daraaya?
Toh sun!
Tu khud ek saanp ban jaa—
par zehre ke bina, ek bechaara saanp!”

Mere pairon tale zameen khisak gayi.
Mujhe pata tha uski tapasya kitni shakti rakhti hai.
Main ghabra kar pair pakad kar bola:

“Dost, maine toh mazaak me kiya!
Maaf kar do… apna shraap wapas le lo.”

Khagama ka saans tez tha,
par dil me daya aa gayi.

Usne kaha:

“Shraap to lagega hi.
Par sun—
Jab Ruru, Pramati ka pavitra beta dikhega,
uski pehli jhalak me hi
tu apne purane roop me laut aayega.”

Phir usne mujhe pehchaan kar kaha:

“Ruru… tumhi woh ho.
Tumhari wajah se
mera shraap ab khatam ho gaya.”

⭐ Rishi Ka Upadesh – Ek Brahmana Ka Dharam

Jaise hi shraap khatam hua,
Sahasrapat ne apna asli roop le liya—
tej aur prakash se bhara hua.

Phir usne Ruru ko
pyaar aur samajh bhare shabdon me kaha:

“Ruru, dhyaan se suno…

⭐ Sabse bada dharm kya hai?

Jeevon ki raksha karna.

Ek Brahmana ka kaam
kisi ka jeevan lena nahi hota.

Ek Brahmana ko hamesha:

naram dil ka hona chahiye,

Vedo ka gyaan rakhna chahiye,

sabme bhagwan par shraddha jagani chahiye,

kisi ko dukh nahi dena chahiye,

satya aur kshama ka marg pakadna chahiye.

⭐ Kshatriya ka kaam alag hota hai

Sakta dikhana,
rajya chalana,
shastra uthana—
ye sab Kshatriyon ka dharm hai.
Tumhara nahi.

Isliye, beta,
saanpon ko maarne ki kasam chhod do.”

⭐ Aage Ki Kahani Ka Sanket

Phir Sahasrapat ne kaha:

“Ab suno Ruru…
mai tumhe ek purani ghatna bataunga—

Janamejaya ka Sarp–Yagya,
jisme saari nag jati vinash hone wali thi…

Aur kaise ek mahaan Brahmana,
Astika,
ne un sab saanpon ki jaan bachayi.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.4.9
        with st.expander("Section 1.4.9"):
            text1 = """ 
⭐ Ruru Aur Astika Ki Kahani Ka Raaz

(Hinglish Kahani)

Sauti ne kaha:

⭐ Ruru Ka Sawal

Sahasrapat Rishi ke jaane ke baad,
Ruru ke mann me ek hi sawaal baar-baar aane laga:

“Janamejaya ne saare saanpon ko kyun maarna chaha?
Aur unki jaan Astika ne kaise bachayi?
Ye sab main poori tarah samajhna chahta hoon!”

Isliye Ruru ne Rishi se poocha:

“Hey Dwijaraj, meri jigyaasa door karo.
Ye sab kaise hua? Mujhe batao na!”"""
            create_image_text_layout("attached_assets/chapter1/1.4.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Rishi Ka Uttar

Rishi muskuraye,
aur shant swar me bole:

“Ruru…
Astika ki kahani bahut mahan hai.
Ye kahani tumhe
‘vidvaan Brahmano ke mukh se’ hi sunni chahiye.

Woh hi is pavitra ghatna ko
poori tarah jaante hain.”

Itna kehkar Rishi
achanak hawa ki tarah gaayab ho gaye.

⭐ Ruru Ka Dhoondhna

Ruru ghabra gaya.
Woh idhar-udhar bhaaga,
pedon ke peeche dekha,
gheray jangal me jaakar pukara—

“Hey Rishi!
Kahan chale gaye aap?”

Par Rishi kahin nahi mile.
Aakhir thak kar
Ruru zameen par gir gaya.
Uska mann uljhan se bhar gaya tha.

Unke shabd uske kaan me gunguna rahe the:
“Brahmano se poochna…”

⭐ Ghar Laut kar Sach Ko Jaana

Hosh sambhalte hi
Ruru ghar gaya
aur apne pita Pramati se bola:

“Pitashri…
Mujhe Astika ki puri kahani sunni hai.
Janamejaya ne saanpon ka nash kyun karna chaaha?
Aur unhe kisne bachaya?”

Pramati ne apne bete ki vyagra jigyaasa dekhi
aur bola:

“Beta, theek hai…
Main tumhe sab kuch bataata hoon.
Dhyaan se suno.”

Aur fir Pramati ne
Astika ka janm,
Takshaka ki kahani,
aur Janamejaya ke Sarp-Yagya ki puri gatha
sunaani shuru ki."""
            create_image_text_layout(text_content=text2, layout="full")


    # Chapter 1.5
    with st.expander("Chapter 1.5 – Astika Parva (Story of Sage Astika)"):

        # Section 1.5.1
        with st.expander("Section 1.5.1"):
            text1 = """
⭐ Astika Ki Kahani — Jaratkaru Aur Unke Purvaj

(Hinglish Kahani — Section XIII)

Ek din Saunaka Rishi ne Sauti se pucha—

“Janamejaya raja ne saapon ka yagna kyun rakha?
Aur Astika ne un saap ko bachaya kaise?
Astika kaun tha?
Janamejaya kaun tha? Pura sach batao.”

Sauti bole—

“Yeh bahut lambi aur rochak kahani hai.
Yeh sab Vyasa ji ne pehle sunaya tha,
aur mere pita Lomaharshana ne bhi Naimish ke rishiyon ko sunaya tha.
Main wahan tha.
Ab main aapko wahi kahani jaisi suni, waisi sunaata hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Jaratkaru Rishi ka Tapasya Bhara Jeevan

Astika ke pitaji Jaratkaru naam ke mahan tapasvi the.
Bahut kathor vrat rakhte, bahut kam khate,
aur poori duniya mein teerth yatra karte rehte.

Ek din, ghoomte ghoomte, unhone ek ajeeb drishya dekha—

⭐ Purvaj Ulte Latke Hue!

Ek gehri surang mein, kuch rishiyan ke purvaj
sar niche, pair upar latke hue the,
aur unhe ek patli si ghaas ki rassi sambhale hui thi.

Us rassi ko ek chuha chaba raha tha!
Agar rassi toot jaati toh purvaj gir jaate.

Jaratkaru ghabra gaye—

“Aap kaun hain? Aise kyun latke ho?”

Purvaj bole—

**“Hum Yayavara rishi hain.
Hum isliye latke hain kyunki humari vansh ruk rahi hai.
Humara ek hi aakhri vanshaj hai—
Jaratkaru!

Woh tapasya mein laga rehta hai,
shaadi nahi karta,
iska matlab humari kul-pankti khatam ho jaayegi.
Isliye hum yahan latak kar apni nasht hoti vansh ka dukh saha rahe hain.”**

Jaratkaru shock ho kar bole—

“Main hi Jaratkaru hoon!
Bataaiye main aapki kaise madad karoon?”

Purvaj bole—

“Bas ek kaam karo—
shaadi karo aur ek putra paida karo.
Wahi humari mukti ka kaaran banega.”

⭐ Jaratkaru Ka Sankalp

Jaratkaru sad ho gaye, aur bola—

**“Main kabhi apne liye shaadi nahi karunga…
par aapke liye jaroor karunga.

Par shart yeh hai—
ladki ka naam Jaratkaru hi hona chahiye
aur uske parivar wale khud mujhe daan mein dene chahen.
Main gareeb hoon, mujhe kaun beti dega?
Par agar koi de diya toh main pratigya karta hoon—
main aapke liye vansh ko aage badhaunga.”**

Purvaj khush ho gaye.
Unhone Jaratkaru ko aashirvaad diya.

⭐ Yehi Se Astika Ki Kahani Shuru Hoti Hai…

Yahin se kahani aage badhti hai,
aur Jaratkaru ki shaadi, unke putra Astika ka janm
aur saap-yagya ko rokne ki Astika ki himmat ki gatha
aage aati hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.2
        with st.expander("Section 1.5.2"):
            text1 = """ 
⭐ Astika Ki Kahani – Jaratkaru Ki Shaadi

(Hinglish Kahani — Section XIV)

Jaratkaru Rishi ne apne purvajon से वादा किया था—
“Main shaadi karunga, par sirf us ladki se jiska naam bhi Jaratkaru ho.”

Lekin duniya bhar ghoomne ke baad bhi,
unhe koi aisi kanya nahi mili."""
            create_image_text_layout("attached_assets/chapter1/1.5.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Rishi Ka Prarthana Karna

Ek din, thak kar Rishi Jaratkaru ek jungle mein ruk gaye.
Purvajon ke shabd yaad karke,
unhone teen baar dheemi si awaaz mein prarthana ki—

“Mujhe ek patni mile… Jaratkaru naam wali… daan mein.”

Unki prarthana sachchi thi, dil se nikli thi.

⭐ Vasuki Ka Aana

Tabhi saap-race ke naayak Vasuki unke saamne aaye.

Vasuki ne kaha—

“Rishi ji, main apni behen ko aapko patni ke roop mein dena chahta hoon.”

Par Jaratkaru Rishi ne turant mana kar diya.
Unhone socha—

“Agar iska naam Jaratkaru nahi hua toh main shaadi nahi kar sakta.”

Isliye unhone Vasuki se poocha—

“Sach batao, tumhari behen ka naam kya hai?”

⭐ Vasuki Ka Vachan Pura Hona

Vasuki muskura diye aur bole—

“Rishi ji, meri behen ka naam bhi Jaratkaru hi hai.
Main usey aapke liye hi sambhal kar rakha tha.
Kripya ise svikaar karo.”

Yeh sunkar Rishi ka mann shaant ho gaya.

Rishi Jaratkaru ne Vasuki ki behen,
slender-waisted aur vinamra Jaratkaru,
ko vidhi-vidhan se patni ke roop mein apna liya.

Unki shaadi dharm ke anusaar, shanti se poori hui.

⭐ Yahi se Astika ka janm hoga…

Is pavitra vivah se
Astika naam ka mahan Rishi paida hoga—
jo aage chal kar saap-yagya rok kar saap-jati ko bachayega।"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.3
        with st.expander("Section 1.5.3"):
            text1 = """ 
⭐ Astika Ki Kahani – Saapon Ka Rakshak

(Hinglish Kahani — Section XV)

Bahut pehle, saapon ki maa ne apne bachchon ko shraap diya tha:

“Agni, jiska rath-vaahak hawa hogi, Janamejaya ke yagya mein tumhe jala dega!”

Is shraap ko rokne ke liye hi
saap-naresh Vasuki ne apni behen ki shaadi
Rishi Jaratkaru se karwayi thi."""
            create_image_text_layout("attached_assets/chapter1/1.5.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Astika ka Janm

Shaadi ke baad, Rishi Jaratkaru aur unki patni se
ek tejasvi putra paida hua—Astika।

Astika bahut hi gyaani tha—
Vedas ka vidvaan, shaant-swaroop, sabko ek samaan nazar se dekhne wala.
Woh apni maa aur papa, dono ke dar ko door karta tha.

⭐ Janamejaya ka Saap–Yagya

Samay guzar gaya.
Pandav vansh ka ek raja, Janamejaya,
ne ek mahaan yagya shuru kiya—
Saap–Yagya, jisme saare saapon ko aag mein daal kar maarna tha.

Jab yagya shuru hua,
saap ek ek karke aag mein girne lage.
Vasuki aur saap-jati ka bhay badhta gaya.

⭐ Astika Ka Vachan Nibhana

Astika ko pata tha—
yeh saap uske mama, bhai aur parivar hain.
Agar woh na rukega toh saap-jati khatam ho jayegi.

Isliye Astika ne apna gyaan, tapasya aur dharm ka sahara liya
aur Janamejaya ke yagya ko beech mein rok diya.

Meetha, samajhdar vaachan dekar
Astika ne raja ka dil jeet liya.

Aur raja ne ghoshna ki:

“Aaj se saap–yagya roka jata hai!”

Is tarah Astika ne apne parivaar ko bacha liya.

⭐ Rishi Jaratkaru Ka Kartavya Pura Hua

Astika ne:

Devon ko yagyon se santusht kiya,

Rishiyon ko brahmacharya se prasann kiya,

Purvajon ko apni santan se moksh diya,

Aur saapon ko aag se bachaya.

Is prakar Rishi Jaratkaru ka sab karz—
dev-karz, pitra-karz, rishi-karz—
poora ho gaya।

Ant mein, bahut saal tapasya ke baad,
Rishi Jaratkaru swarg ko prapt ho gaye,
Astika ko dharti par chhod kar."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.4
        with st.expander("Section 1.5.4"):
            text1 = """ 
⭐ Astika Ki Kahani – Vinata, Kadru aur Garuda Ka Janm

(Hinglish Kahani — Section XVI)

Saunaka ne Sauti se kaha:
“Humein Astika ki kahani aur detail mein sunao. Tumhari boli madhur hai. Jaise tumhare pita sunate the, vaise hi sunao.”

Sauti ne kaha:
“Achha, main wahi kahani sunata hoon jo maine apne pita se suni thi.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Kadru aur Vinata – Do Behen, Do Patniyan

Satyug ke samay, Prajapati ki do khoobsurat betiyan thi—
Kadru aur Vinata.

Dono ne Rishi Kashyapa se vivaah kiya.
Kashyapa un dono se bahut prasann the.
Isliye unhone bola:

“Maango, kya vardaan chahiye?”

Kadru boli:
“Mujhe ek hazaar saap-putra chahiye. Sab ek jaise roopwale.”

Vinata boli:
“Mujhe do putra chahiye. Par woh dono Kadru ke hazaar bachchon se bhi zyada shaktishaali, bade aur prabhavshaali hon.”

Kashyapa ne dono ko “Tathastu” kaha,
aur dono vardaan poore kiye.

⭐ Ande aur Intezaar

Kadru ne 1000 ande diye.
Vinata ne sirf 2 ande diye.

Dasiyon ne sab ande garam kalashon mein rakhe.

500 saal beet gaye.

Kadru ke sab ande toot gaye—
aur hazaar saap-putra janam le liye.

Lekin Vinata ke dono ande abhi tak nahi toote.
Vinata ko jalan hui.

⭐ Vinata ki Galti Aur Shraap

Bechain hokar Vinata ne
pehla anda tod diya.

Andar ek bachcha tha—
upar ka hissa bana hua,
neeche ka hissa adhura.

Us bachche ne gusse mein shraap diya:

“Maa! Tumne mujhe jaldi nikala.
Isliye tum dusron ki daasi banogi.
Par agar tum dusre ande ko 500 saal aur na chhedo,
to mera bhai tumhe azaad karega.”

Wahi bachcha baad mein
Surya ka rath chalane wala bani—
Arun!

⭐ Garuda Ka Janm

Agla 500 saal beetne ke baad,
Vinata ka doosra anda apne aap toota.

Usme se nikla—

🌟 Garuda! 🌟
Sampo ka shatru, pakshiyon ka raja, tejasvi aur adbhut.

Janam ke turant baad,
Garuda hawa mein uda—
kyonki usse bhook lagi thi
aur uske liye khaana Bhagwan ne pehle se nirdharit kiya tha.

Usne apni maa Vinata se pyaar kiya,
par turant apni udaan par nikal gaya—
kyonki uska karyarambh usi din se tha.

Bas, yeh tha Kadru, Vinata, Arun aur Garuda ka janm ka adhyay—
jo aage chal kar Astika ki kahani se juda hua hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.5
        with st.expander("Section 1.5.5"):
            text1 = """ 
⭐ Astika Ki Kahani – Samudra Manthan Ka Aarambh

(Hinglish Kahani — Section XVII)

Sauti ne kaha:
“Isi samay Kadru aur Vinata ne ek divya ghoda aate dekha.”

Woh ghoda tha—
🌟 Uchhaihshravas 🌟
Devtaon ka priya,
hamesha jawaan,
chamak se bhara hua,
aur tejon se yukt.

Yeh ghoda Samudra Manthan ke samay nikla tha.
Iska roop itna sundar tha ki dono behne use hairaan hokar dekh rahi thi."""
            create_image_text_layout("attached_assets/chapter1/1.5.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Saunaka ka Prashna

Saunaka ne turant poocha:

“Devtaon ne samudra ko kyon matha?
Aur kab Uchhaihshravas jaise shaktishaali ghode ka janm hua?”

⭐ Sauti Ka Uttar – Meru Parvat Aur Devtaon Ki Sabha

Sauti ne kaha:

“Is pracheen katha ka aarambh Meru Parvat se hota hai.”

Meru ek adbhut pahaad hai—
sunehri chamak wala,
surya ki kirne jismein toot kar chamakti hain.
Uske shikhar aasman ko chhoote hain.

Wahan devta, gandharva, aur divya jeev baste hain.
Yeh pahaad paapiyon ke liye aprapya hai.
Yahan ajeebo-gareeb janwar ghoomte hain.
Yahan lakhsaan upchaarik jari-bootiyan ugti hain.

Ek din devta sab Meru ke ratna-jadit shikhar par ikattha huye.
Woh sab bahut bechain aur chintit the—
kyonki sabko amrit chahiye tha,
par amrit kahin bhi nahi mil raha tha.

⭐ Narayana Ki Salah

Tab Bhagwan Narayana ne Brahma se kaha:

“Hey Brahma, devtaon aur asuron ko lekar
Samudra ko matho.
Usse amrit niklega.
Uske saath bahut saari aushadhiyan aur ratna bhi prakat honge.
Yeh hi tarika hai amrit paane ka.”

Devta sun kar utsahit ho gaye.
Sab ne man banaya:

🌊 Samudra Manthan hoga! 🌊
Amrit payenge!
Aur ussi manthan ke dauran
niklega—Uchhaihshravas,
devtaon ka divya ghoda!"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.6
        with st.expander("Section 1.5.6"):
            text1 = """ 
⭐ Astika Ki Kahani – Samudra Manthan (Bhag II)

(Hinglish Kahani — Section XVIII)

Sauti ne kaha:

Ek pahaad tha—
🌄 Mandara Parvat.
Badalon jaisa shikhar,
sugandhit jari-bootiyon se dhaka,
panchhiyon ki madhur awaazon se gunjta,
aur jangli janwaron se bhara hua.

Devta, apsarayein aur kinnar bhi wahaan aate-jate the.
Yeh parvat 11,000 yojan upar aur 11,000 yojan neeche tak faila hua tha!

Devta chahte the ki iss pahaad ko mathani bana kar samudra manthan karein.
Par woh isey ukhaad nahi pa rahe the.
Thake-haare woh Brahma aur Vishnu ke paas gaye.

Unhone vinati ki:

“Bhagwan! Kuch upay bataiye. Mandara ko ukhaadna humse sambhav nahi!”"""
            create_image_text_layout("attached_assets/chapter1/1.5.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Vishnu Ka Aadesh – Ananta Ki Shakti

Vishnu aur Brahma dono raazi hue.

Vishnu ne kaha:

“Yeh kaam sirf ek hi kar sakta hai —
shaktishaali saap-raj, Ananta.”

Ananta ko aadesh mila.
Usne apni ati-balshali shakti se
Mandara Parvat ko jad se ukhaad diya,
saath hi uske saare ped, pakshi, aur prani upar hi rehte gaye!

Sab milkar samudra ke kinare aaye
aur samudra se kaha:

“Hum tumhein mathna chahte hain. Amrit chahiye.”

Samudra bola:

“Theek hai. Par mujhe bhi amrit ka hissa milega.”

⭐ Kachhua Raja – Kurma Avatar ki Tyari

Devta phir kachhua-raja ke paas gaye.

Unhone kaha:

“Parvat ko apni peeth par sambhaliye!”

Kachhua-raja maanak gaya.
Indra ne Mandara ko uski peeth par rakha.

Aur phir—

🗻 Mandara bani mathani
🐍 Vasuki bana rassi
Devta Vasuki ki poonch pakde
Asur uska hood pakde

Ananta kabhi Vasuki ka sar upar uthaye,
kabhi neeche dabaye.

Us tanav se Vasuki ke muh se
kala dhuaan aur aag nikli—
jo badal ban gaya
aur tez bijli ke saath barsa,
jisse thake hue devta ko thandak mili.

Upar se ped tod-tod kar phool gir rahe the.
Devta khush ho gaye.

⭐ Samudra Manthan ka Haadsa

Par manthan aasaan nahi tha.

🌊 Samudra ghoom raha tha.
Bade-bade jaljeev kuchle ja rahe the.
Neeche ki naglok tak halchal mach rahi thi.

Ped jado se ukhad kar samudra mein gir rahe the.
Unki ghis-ghis se aag lag jaati.
Pahaad dekhne mein aisa lagta
jaise bijli se chhata hua andhera baadal.

Aag chale toh
Indra ne baarish kar ke bujha di.

⭐ Dhire-Dhire Amrit Ki Mahak

Manthan chalti rahi.
Jari-bootiyon ka ras samudra mein ghul gaya.
Samudra ka doodhiya paani
ghee jaisa hone laga.

Par amrit abhi tak nahi nikla tha!

Thake hue devta
Brahma ke paas gaye:

“Hum mein shakti nahi bachi.
Ab amrit ke bina mathna mushkil hai.”

Brahma ne Vishnu se kaha:

“Hey Narayana, inhe shakti do.”

Vishnu ne kaha:

“Main tumhein shakti deta hoon.
Fir se matho.”

⭐ Divya Ratnon Ka Udbhav

Manthan dobara shuru hua.
Aur phir ek-ek karke nikalne lage:

🌙 1. Cool, thousand-rayed Moon
🌼 2. Shwet vastra wali Lakshmi
🍶 3. Soma (divya sharbat)
🐎 4. Uchhaihshravas, divya ghoda
💎 5. Kaustubha Mani — Vishnu ka hamsaathi

Aur phir—

👨‍⚕️ Dhanvantari
haath mein amrit kalash lekar prakat hue!

Danav cheekh uthe:

“Amrit humara hai!”

Phir aaya—

🐘 Airavata, Indra ka gajraj.

⭐ Vish Ka Udgam – Shiva Ka Bal

Aur tab—

☠️ Halahal Vish nikla.
Teenon lok girne lage.
Dharti jal uthi.

Brahma ne Shiva ko bulaya.
Shiva ne saara vish pee liya
aur use gale mein roka.
Tabhi se unka naam hua:

💙 Neelkanth.

⭐ Mohini Avatar — Amrit Ka Bantar

Ab Asur gusse mein the.
Lakshmi aur amrit dono chahiye the.

Tab Narayana ne apni Maya ko bulaya.
Unhone ek divya sundari ka roop dharan kiya —
✨ Mohini ✨

Danav uski sundarta dekh kar
buddhi-heen ho gaye.
Sab ne amrit ka kalash
usi ke haath mein de diya."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.7
        with st.expander("Section 1.5.7"):
            text1 = """ 
⭐ Astika Ki Kahani – Samudra Manthan ka Maha-Yuddh (Bhag III)

(Hinglish Kahani — Section XIX)

Sauti ne kahaa:

Samudra manthan se amrit nikalte hi
Daitya aur Danav,
jo chamakdar kavach aur teekhe hathiyaar pehene hue the,
devtaon par toot pade.

Us waqt
Bhagwan Vishnu, jo abhi bhi Mohini roop mein the,
Nara ke saath milkar
chal se Danavo ko bhaatkar
unke haath se amrit ka kalash cheen le gaye.

Devtaon ne dara-dara kar,
khushi se bhar kar,
Mohini se amrit liya
aur pee liya."""
            create_image_text_layout("attached_assets/chapter1/1.5.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Rahu Ka Dhoka

Jab devta amrit pee rahe the,
ek Danav— Rahu—
devta ka roop dharan karke
chupke se line mein khada ho gaya
aur amrit pee diya.

Par jaise hi amrit uski gardan tak pahucha,
Surya aur Chandra ne use pehchaan liya
aur devtaon ko bata diya.

Vishnu ne turant
apna Sudarshan Chakra chala diya—
ek tej chamak,
ek ghoomte hua bijli-jaisa chakr.

Chakra ne
Rahu ka sar kaat diya.

Sar to amrit chakh chuka tha,
isliye amar ho gaya
aur asmaan mein jaa kar
darravna cheekhne laga.

Rahu ka dhad zameen par gir kar
idhar-udhar luhatta raha,
dharti hil uthi,
pahaad aur jangelein kamp uthi.

Tab se
Rahu ka sar
Surya aur Chandra se bair rakhta hai—
isliye wo unhe grahan ke dauraan nigal leta hai.

⭐ Mohini Gayab, Yuddh Shuru

Amrit baantne ke baad
Vishnu ne apna Mohini roop chhod diya
aur asli roop lekar
Danavo par divya astra barsa diye.

Samudra ke kinaare
bhayankar yuddh shuru ho gaya.

Javelin, bhala, talwar, gada—
laakho hathiyaar
aasmaan mein chamak rahe the.

Danavon ke sar
sunehri kundalon se sajjey hua,
do-dhaar talwaron se kat-kar
zameen par girtay ja rahe the.
Rakt se bhari dharti
jaise laal pahaadon se dhak gayi ho.

Yoddha door se
teer-chala rahe the.
Paas aate hi
munh, mukko aur lohe ke ghusso se
ek-doosre ko gira rahe the.

Charo taraf cheekhne ki awaaz:

“Kaato!”
“Bano!”
“Aage badho!”
“Neeche pheko!”

⭐ Nara–Narayana Ka Aagman

Tab Nara aur Narayana
ranbhoomi mein prakat hue.

Narayana ne
Nara ke haath mein ek divya dhanush dekha
aur turant
apne man mein
Sudarshan Chakra ko yaad kiya—

Chakra bina deri
aasmaan se utar aaya,
bijli se chamakta hua,
shivanta ki aag jaisa bhayankar.

Narayana ne use
hathi ke soond jaise baahoon se
tej gati se fenk diya.

Chakra kabhi aag ban kar
Danavo ko jala deta,
kabhi aasman mein ghoom kar
unhe kaat deta,
kabhi zameen choo kar
unke khoon ka paani pee jaata
jaise koi bhoot ho.

⭐ Danav Aasman Chadh Gaye

Danavon ne bhi jawaab diya.

Badal jaisi safed tvacha,
apar shakti,
woh aasman mein udd gaye
aur pahaad utha-utha kar
devtaon par phenka.

Pahaadon ke takraane ki garaj
bijli se bhi zyada daravni thi.
Dharti, pahaad, jangalein—
sab kaanp uthe.

Tab
Nara agility se
soorne-tir chala kar
gir rahe pahaadon ko
dhool mein badal diya.

Chakra ki aag dekhkar
bahut se Danav
zameen ke neeche bhaag gaye,
kuch samudra mein doob gaye.

⭐ Devtaon Ki Vijay

Devta jeet gaye.
Unhone Mandara Parvat ko
Narak ke tortoise se utar kar
wapis uski jagah rakh diya.

Amrit saath lekar
devta apne lokon ko laut gaye.

Aur Indra ne
amrit ka kalash
Narayana ko suraksha ke liye
saupa."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.8
        with st.expander("Section 1.5.8"):
            text1 = """ 
⭐ Astika Ki Kahani – Uccaiḥśravas aur Kadru–Vinata ka Shraap (Bhag IV)

(Hinglish Kahani – Section XX)

Sauti ne kahaa:

“Mainne tumhe puraa katha suna di — kaise samudra manthan hua aur kaise amrit nikla…
Aur isi manthan mein
Uccaiḥśravas, sab ghodon ka raja,
janm hua —
jiski sundarta aur shakti ka koi tulna nahi.”

Usi ghode ko dekh kar
Kadru ne apni behen Vinata se sawaal kiya:"""
            create_image_text_layout("attached_assets/chapter1/1.5.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Kadru–Vinata Ka Wager

Kadru boli:

“Priye behen, batao, Uccaiḥśravas ka rang kya hai?”

Vinata ne turant kaha:

“Arre, woh toh bilkul safed hai! Tum kya sochti ho?”

Kadru muskurayi aur boli:

“Main kehti hoon uske poonch ke baal kaale hain.
Chalo, ek shart lagate hain—

Jo haaregi,
woh doosri ki daasi (slave) ban jayegi!”

Vinata, bina soche, haan bol gayi.

Dono behne agle din ghode ko dekhne ka vaada karke
apne-apne ghar chali gayin.

⭐ Kadru Ka Dhoka

Kadru ne apne hazaar saap-putron ko aadesh diya:

“Jao!
Apne aap ko kaale baalon mein badal lo
aur Uccaiḥśravas ki poonch par chipak jao,
taaki woh kaala lage.
Bas!
Main jeet jaungi!”

Par
saap—jo garv se bhare, shaktishaali aur zehreeli the—
ye kaam karne se mana kar gaye.

Kadru ko gussa aa gaya.

Usne apne bachchon ko shraap de diya:

“Jab Pandav vansh ke raja Janamejaya
sarp-yagya karenge,
tab Agni tum sab ko jala kar khatam kar dega!”

⭐ Brahma Ka Faisla

Kadru ka shraap
Brahma ji ne khud suna.

Devtaon ne bhi kaha:

“Yeh saap bahut zehreeli, bahut shakti-shaali
aur hamesha dusron ko dasti rehte hain.
Prachuran sankhya mein badhte ja rahe hain.
Isliye un par aisi saja hona
srishti ke hit mein hi hai.”

Yeh sun kar
Pitamaha Brahma ne
Kadru ke shraap ko anumati de di.
Faisla tay ho gaya:

➡️ Saapon ka vinaash ek din Yagya mein hoga.

⭐ Kasyapa Ko Santvana

Phir Brahma ji ne
saapon ke pita, Maharishi Kasyapa, ko bulaya:

“Ae tapasvi,
tumhare jo saap putra paida hue—
jo zehreeli, prabal aur hamesha dadhna chahte hain—
unka vinaash Kab Se Niyat tha.
Unki maa ne jo kaha, woh samay ke anuroop hai.
Tum shok mat karo.

Aur lo—
main tumhe vish-shanti ka gyaan deta hoon,
taaki tum aage kisi jeev ko bachaa sako.”

Aur is prakar
Kasyapa ko
zehar ko shant karne ka divya vidya pradan ki gayi."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.9
        with st.expander("Section 1.5.9"):
            text1 = """ 
⭐ Astika Ki Kahani – Kadru aur Vinata ka Samudra-Yatra (Bhag V)

(Hinglish Kahani – Section XXI)

Sauti ne kaha:

“Agli subah, jab raat beet chuki thi
aur suraj apni laalima lekar ug aaya—
tab woh dono behne, Kadru aur Vinata,
jo pichhle din
Uccaiḥśravas ke rang par shart laga chuki thi,
bahut utsukta aur bechaini se
us divya ghode ko dekhne
nikal padi.”

Dono jaldi-jaldi kadam badhate hue
aage badh rahi thi—
kyunki jiski shart galat niklegi,
use dusri ki daasi banna tha!"""
            create_image_text_layout("attached_assets/chapter1/1.5.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Samudra Ka Divya Darshan

Raaste mein
dono behno ne dekha
Vishaal Samudra—
paani ka woh anant sanchay,
jiska varnan shabdon mein mushkil tha.

Sauti ne us samudra ka roop
is tarah bataya:

Gehra aur apar,
jisme aise machhliyan thi
jo bhi whale jaisi badi praniyon ko bhi nigal sakti thi!

Wahan makar, ajgar,
aur darawne roop ke
anek jalajeewan the—
jo dekhne walon ko kampaa dein.

Wahi samudra
Varuna dev ka ghar hai,
aur Nagon ka sundar vasasthal bhi.

Wahi samudra
ratnon ka bhandaar hai,
aur Asuron ka ashray bhi.

Kabhi shaant, kabhi bhayanak—
uski garajti leherein
aise lagti jaise
aasman ki taraf
apne haath uthaakar
nritya kar rahi hon!

Chand ki kiranon se
uska paani kabhi uthta, kabhi girta—
aur uski gehrai mein
Panchajanya,
Lord Krishna ka divya shankh,
janma liya tha.

Pehle, Bhagwan Vishnu ne
jab varaha avatar liya
aur doobi hui prithvi ko uthaya,
tab samudra
bhayanak roop se hil utha tha.

Samudra itna vishaal tha
ki Maharishi Atri ne bhi
sau saal tak prayas karke
uski gehrai naap nahi paayi!

Jab pralay ka samay aata hai,
yahi samudra
Vishnu ka shayan sthal ban jata hai—
jahan ve yoga-nidra mein
anant yugon tak vishraam karte hain.

Yahi woh sthaan hai
jahan parvat Mainaka
Indra ke vajra se bachne
chhup gaya tha…

Is tarah ka samudra—
anant, gahra, apar,
bhayankar aur adbhut!

⭐ Nadiyon ka Samudra Mein Milan

Kadru aur Vinata ne dekha:

Hazaaron nadiyan—
garv se bhari,
tezi se behati,
aapas mein pratiyogita karti—
samudra ki taraf daud rahi thi.

Jaise koi prem-pyaasi
apne priya se milne
utavli ho!

Samudra un sab nadiyon ko
apni lehron mein samete hue
lehrata, garajta,
aur anant seema tak phela hua
prakriti ka ek adbhut chamatkar lag raha tha.

⭐ Uccaiḥśravas Ka Drishya Dekhne Ki Pratiksha

Iss jalvishwas ko dekhte hue
dono behne
aage badhti gayin—
mann mein ek hi vichaar:

🔸 Kaun jeetegi? Kaun haaregi?
🔸 Ghoda safed hi niklega… ya uski poonch kaali hogi?
🔸 Kya Kal ka dhokha kaam karega?
🔸 Kya Vinata daasi ban jayegi?

Is prakar
samudra ka adbhut darshan karte hue
dono behne
Uccaiḥśravas ki taraf
badhti chali gayin..."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.10
        with st.expander("Section 1.5.10"):
            text1 = """ 
⭐ Astika Ki Kahani – Kadru Ki Chaal (Bhag VI)

(Hinglish Retelling – Section XXII)

Sauti ne kaha:

“Jab Kadru ne apne saupon se
Uccaiḥśravas ki poonch ko
kaala dikhane ka aadesh diya,
to pehle toh Nag log ghabra gaye.

Unhone socha:

‘Agar humne Maa ki baat na maani,
toh woh hum par naraaz hokar
humein jala bhi sakti hai!’

Lekin agar Maa prasann ho gayi,
to woh unhe apne shraap se bhi
mukta kar sakti thi.

Isliye saare Nag ek saath bole:

“Hum zaroor ghode ki poonch ko kaala banayenge.”

Aur turant—
jaise kisi jaduyi khel mein—
saare Nag
ghode ki poonch ke baal ban kar
usme chipak gaye,
taaki door se dekhne par
poonch kaali dikhe."""
            create_image_text_layout("attached_assets/chapter1/1.5.10.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Kadru aur Vinata – Shart Ka Faisla

Ab dono behne—
Kadru aur Vinata—
jo Daksha ki pyaari betiyan thi,
aur ab pati Kasyapa ki patniyan—
khushi-khushi
aasmaan ki raah se
samudra ke doosre kinare ki taraf
badhti gayin.

Kyuki aaj shart ka faisla hona tha!

⭐ Samudra Ka Mahasundar Roop (Phir se)

Raaste mein
dono behne ne phir dekha
woh apar, gehra,
adbhut Samudra,
jiska varnan
shabdon mein samana mushkil tha.

Samudra:

hawa ke jhonkon se
ek dum behosh ho uthta,
phir bhayanak garajne lagta,

itna gehra
ki whale jaise praniyon ko bhi
nigalne wale jeevon se bhara tha,

makaron, ajgaron,
aur anek darawne praniyon ka ghar tha,

nagon ki adbhut nagri bhi wahi thi,

Varuna dev ka shandar mahal tha,

Asuron ki gupt gufaayein bhi wahi,

aur neeche kahi
prithvi ko garam rakhne wali
paataal-agni rehti thi.

Aur samudra ki lehron mein tha
ek ajeeb sa nritya—
jaise paani ki haath jhulas kar
aakash ko chhoo lene ka prayas kar rahe hon.

Hazaaron nadirayan—
apni shaan ko darshaati hui—
samudra ki taraf bhaag rahi thi,
jaise koi var-vadhu
apne saajan ke paas daudti ho!

Samudra
itna roopavaan,
itna vishaal,
itna ajeeb
ki lagta tha jaise
poora aakash zameen par utar aaya ho.

Dono behnen
aise mahaan samudra ko paar karti hui
us ghode ko dekhne ja rahi thi
jis par unki zindagi ki sabse badi shart
lagi hui thi…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.11
        with st.expander("Section 1.5.11"):
            text1 = """ 
⭐ Section XXIII – Garud ka Janm aur Devtaon ka Dar

(Hinglish Retelling)

Kadru aur Vinata ne samundra paar kiya
aur Ucchaihshravas ghode ke paas jaakar ruk gayi.

Ghoda sach-much chaand jaisa safed tha,
lekin uski poonch mein kaale baal the.
Ye dekhkar Vinata ka dil toot gaya…
Kyuki ab shart ke mutabik
use Kadru ki daasi banna tha.

Vinata bahut dukh se jhuk gayi.
Uska mann bilkul nirash ho gaya."""
            create_image_text_layout("attached_assets/chapter1/1.5.11.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Garud ka adbhut janm

Tabhi, samay poora hote hi,
Vinata ke bache hue ande se ek tejomay roshni phooti—
aur Garud janm le liya!

Woh aag ki lahu-laal jwala jaisa chamak raha tha—
jaise kisi ne aasman mein ek chalta hua agni-parvat chhod diya ho.

Janam ke saath hi,
Garud itna bada ho gaya ki
aasman tak pahunch gaya,
zor-zor se garajta hua,
poori duniya ko hilaata hua.

Devtaon ne jab uski teevra chamak dekhi,
toh dar kar socha—

“Agni Dev gussa mein pura jag jalane wale hain!”

Woh turant Agni ki sharan mein bhaage.

⭐ Devtaon ka bhram

Agni ne unhe sambhaala aur bola:

“Darro mat!
Ye aag ka dher nahi…
Ye Garud hai!
Vinata ka putra.
Samarth, tejomay, aadi-shakti se bharpur.
Nagon ka shatru, devtaon ka mitra.”

Devta thoda shaant hue,
par Garud ki chamak itni tej thi
ki unki aakhon tak meethi jalan hone lagi.

Phir devta door se Garud ko pranam karne lage
aur bole:

⭐ Devtaon ki stuti

“O Garud, tum tej ho, bal ho, gyaan ho.
Tum sabka rakshak ho.
Tum sab roopon ke swami ho.
Tumhari chamak surya ko bhi dheema kar deti hai.
Tum aasman ko hila dete ho,
aur tumhari garaj se hamare hriday kampne lagte hain.
O maha-pakshi, humari raksha karo!”

Devta vinati karte rahe,
aur dheere-dheere
Garud ne apna tej neeche utar diya—
taaki poori srishti shant ho jaaye."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.12
        with st.expander("Section 1.5.12"):
            text1 = """ 
⭐ Section XXIV – Garud, Aruna aur Surya ka Krodh

(Hinglish Story Retelling)

Garud ne jab devtaon ka darr dekha,
toh woh bohot vinamr ho gaya.

Usne kaha:

“Darro mat!
Mera roop tumhe dara raha hai,
toh main apni shakti kam kar deta hoon.”

Aur turant hi
Garud ne apna bada, tej roop chhota kar liya.

Phir woh apne bhai Aruna ko peeth par bithakar
aasman mein udd gaya
aur apni maa Vinata ke paas laut aaya."""
            create_image_text_layout("attached_assets/chapter1/1.5.12.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Aruna ka kaam – Surya ko shaant rakhna

Garud ne Aruna ko purva disha mein bithaya—
usi samay jab Surya bhayanak rosh mein tha.

Saunaka ne pucha:

“Surya kyun gussa tha?
Woh duniya ko jalana kyun chahta tha?”

⭐ Surya ka krodh – Rahu ki wajah se

Sauti ne bataya:

Jab samudra manthan hua tha,
Rahu chori-chhupke amrit peene lag gaya.
Surya aur Chandra ne use pakad liya.

Tab se Rahu un dono ka dushman ban gaya.

Ek din Rahu ne socha:

“Surya ne mujhe sabke saamne sharminda kiya.
Main use nigal jaunga!”

Is soch se Surya bhayanak roop se gussa ho gaya.
Woh bol उठा:

“Maine devtaon ki madad ki,
aur mujhe hi dushmani mili!
Ab main poori duniya ko jala doonga!”

Phir Surya paschim parvaton par gaya
aur bina ugiye hi
apni teevra garmi se sabko darane laga.

⭐ Devta ghabra gaye

Rishiyon ne dekha ki
aadhi raat mein hi teekhi garmi aa rahi thi.
Sab log bhaag kar Brahma ji ke paas gaye:

“Prabhu, Surya abhi uggā bhi nahi,
par duniya jal rahi hai!
Agar woh ugg gaya toh kya hoga?”

Brahma ji bole:

“Haan, Surya gusse mein duniya jala denge.
Par maine ek upay kar diya hai.
Kashyap ka putra Aruna
Surya ke saamne khaada hoga.
Aur woh Surya ki garmi ko rok lega.”

⭐ Aruna ban gaya Surya ka saarathi

Aruna ne Brahma ji ka aadesh maana.
Agli subah Surya uthe,
par Aruna unke saamne khada tha,
jaise ek suraksha-dhal.

Isliye Surya ki garmi
duniya ko jalane se pehle hi kam ho gayi.

Is tarah
duniya bach gayi,
devta shaant ho gaye,
aur Surya ka krodh thanda pad gaya."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.13
        with st.expander("Section 1.5.13"):
            text1 = """ 
⭐ Section XXV – Vinata ki Gulami aur Indra se Prarthna

(Hinglish Story Retelling)

Garud, apni teevra shakti aur tej ke saath,
door samundar ke paar
apni maa Vinata ke paas laut aaya.

Vinata abhi bhi bohot dukh mein thi—
kyunki woh apni behen Kadru se shart haar kar
gulam ban chuki thi."""
            create_image_text_layout("attached_assets/chapter1/1.5.13.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Kadru ka kahehna – “Mujhe Nagalok le chalo!”

Ek din Kadru ne Vinata ko bulaya.
Vinata bechari uske saamne jhuk kar khadi ho gayi.

Kadru boli:

“Vinata, mujhe samundar ke beech
ek bohot hi sundar jagah —
Nagalok — le chalo!”

Vinata majboor thi.
Usne Kadru ko apne kandhon par uthaya.

Garud ko bhi maa ne hukm diya,
toh Garud ne
saare saamp apni peeth par bitha liye.

Phir Garud aasman ki or udd chala—
seedha Surya ke paas se guzar kar.

⭐ Saanp jalne lage Surya ki garmi se

Jaise hi Garud upar utha,
Surya ki tej garmi se
saare saamp jhulsa kar behosh hone lage.

Kadru bohot ghabra gayi
aur Indra dev ko pukarne lagi:

⭐ Kadru ki Indra se lambi prarthna

Kadru bol padi:

“Indra Dev! Devtaon ke raja!
Aap humein bachaiye!
Mere bachche Surya ki garmi se jal rahe hain!
Aap hi baarish barsa kar
saampo ki raksha kar sakte hain.”

Phir Kadru ne Indra ki
lambe, sundar stuti ke shabdon mein prarthna ki—

“Aap Vritra ko maarne wale ho!”

“Aap badalon ko chalane wale,
bijli, hawa aur agni ke swami ho!”

“Aap hi srishti banate aur mitate ho.”

“Aap saari prakriti ho—
din, raat, saal, mahine, mausam.”

“Aap samundar ho, parvat ho, ped ho, aasman ho.”

“Aap Vedas mein gaaye jaate ho.”

“Aap yajna ka ghee aur soma ras swikaar karte ho.”

“Aap sabki raksha karne wale ho!”

Kadru ne apni poori shraddha ke saath
Indra se vinti ki:

“Baadal bhej dijiye, Surya ki garmi ko shaant kijiye!
Mere bachchon ko bachaiye!”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.14
        with st.expander("Section 1.5.14"):
            text1 = """ 
⭐ Section XXVI – Indra ki Baarish aur Saampon ki Raksha

(Hinglish Story Retelling)

Kadru ne jab Indra dev se
apne saamp bachchon ke liye
madad maangi,

Indra Dev,
devtaon ke raja,
apne shandaar ghode Uchchaihshravas par savar,
turant kripaalu ho gaye."""
            create_image_text_layout("attached_assets/chapter1/1.5.14.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Indra ka aadesh – “Badalo, barso!”

Kadru ki prarthna sun kar
Indra ne aasman bhar diya
gadha-neele, motay badalon se.

Unhone hukm diya:

“O badalo,
jeevan dene wali boondon ko zameen par barsaao!”

Phir kya tha—
bijli chamki,
badal garje,
hawayein tez ho gayin.

Duniya bhar mein aisa lag raha tha
jaise Yug ka ant aa gaya ho!

⭐ Aasman ki “paagal taandav” jaisi halchal

Baarish itni tezzz thi ki:

laakhon paani ke lehron ki aawaaz,

garajte badal,

chamakti bijli,

tez aandhi…

sab milkar aasman ko
pagal si naach karne wala bana rahe the!

Surya aur Chandrama ke
rays poori tarah gayab ho gaye—
aasman bas kaale badalon mein doob gaya.

⭐ Saamp bach gaye — aur khushi manaayi!

Indra ki is zabardast baarish se
dharti paani se bhar gayi—
itna ki thande, saaf paani ki lehrain
paataalon tak pahunch gayi.

Saamp jo Surya ke tej se
behosh ho rahe the,
ab baarish se thande pad gaye
aur hosh mein aa gaye.

Saare saamp
aur unki maa Kadru,
surakshit tarah pahunch gaye
Ramaniyaka naam ke khubsurat dweep par.

Woh sab bohot khush hue
aur Indra ko dhanyavaad dene lage."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.15
        with st.expander("Section 1.5.15"):
            text1 = """ 
⭐ Section XXVII – Garuda ka Prashna aur Saampon ki Shart

(Hinglish Story Rewrite)

Indra ki tez baarish se saamp bach gaye
aur phir Garuda, apne sundar pankh phailaye,
un sab ko lekar aasman chीरते hue
ek door ke sundar dweep par pahunch gaya."""
            create_image_text_layout("attached_assets/chapter1/1.5.15.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Ek khoobsurat naya dweep

Yeh dweep Bhagwan ne khud banaya tha
aur yahaan makar (samundri prani) rahte the.
Wahaan pahunch kar saamp ekdam khush ho gaye.

Is dweep par:

samundar ki lahron se dhula hua haseen jungle,

har taraf phoolon aur falon se lade hue vriksh,

komal hawa jo sugandh failati thi,

kamalon se bhare huye talaab,

aur pahaadon par milne wale
Malaya ke unche, khushbu-dar ped,

sab milkar us jagah ko
swarg jaise sundar bana rahe the.

Pakshiyon ke madhur gaan se
poora van goonj raha tha.
Beechon ke madhosh gunj
aur Gandharvon ki pasand ki jagah—
yeh dweep dekhne layak tha.

Saamp wahan ghoomte, khelte,
aur man hi man khush hote rahe.

⭐ Saampon ka agla hukm

Kuch der baad saamp Garuda se bole:

“O Garuda, humein ek aur achha dweep dikhao.
Tum ne aasman mein safar karte hue
bahut sundar jagahen dekhi hongi.”

Garuda ne kuch pal socha
aur phir apni maa Vinata se poocha:

“Maa, main saampon ke hukum kyun maan raha hoon?
Main unki seva kyun kar raha hoon?”

⭐ Vinata ka dukh: “Main unki daasi hoon…”

Vinata ne dukh se kaha:

“Beta, ek durebhagya ke kaaran
main apni sautan Kadru ki daasi ban gayi hoon.
Saampon ne dhokha dekar mujhe shart harvaayi thi.
Isi liye mujhe aur tumhe
unka kehna maana pad raha hai…”

Garuda yeh sunkar bahut udaas ho gaya.
Phir saampon se bola:

“Batao, main kya karoon
jisse main aur meri maa
tumhari gulami se azaad ho sakein?”

⭐ Saampon ki sakht shart

Saampon ne turant kaha:

“Amrit humein laa do—
chahe bal se hi kyon na laana pade…
tab hum tumhe azaad kar denge.”

Garuda ne yeh shart sun li—
aur yahi se shuru hoti hai
uski sabse vishal, sabse kathin yatra."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.16
        with st.expander("Section 1.5.16"):
            text1 = """ 
⭐ Section XXVIII – Garuda ka Pehla Kaarya: Bhojan aur Bachav ki Sikhsha

(Hinglish Story Rewrite)

Garuda ko saampon ne kaha tha:
“Humein amrit laa do, tab tum azaad hoge.”

Garuda apni maa Vinata ke paas gaya aur bola:

“Maa, main amrit laane jaa raha hoon.
Par mujhe raste mein kuch khana hoga.
Bataaiye main kya kha sakta hoon?”"""
            create_image_text_layout("attached_assets/chapter1/1.5.16.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Vinata ka updesh: “Brahman ka jeevan kabhi mat lena”

Vinata ne pyaar se kaha:

“Beta, samundar ke beech ek door jagah par
Nishad logon ka ghar hai.
Wahan hazaaron log rehte hain—
unhe khaa sakte ho, phir amrit lekar aa jaana.

Lekin ek baat yaad rakhna:
Kabhi bhi kisi Brahman ko mat maarna.
Brahman ka gussa aag jaisa hota hai—
jo sab kuch jala sakta hai.
Brahman ko chot pahunchana
saare jeevon ko dukh dena jaisa hai.”

Garuda ne poocha:

“Maa, main kaise pehchanu ki kaun Brahman hai?”

Vinata ne kaha:

“Beta, jo aadmi tumhare gale mein jaa kar
tumhe andar se chubhaye…
ya angaar ki tarah jale…
ya tumhare pet mein hazam hi na ho—
samajh lena, woh Brahman hai.
Aise kisi ko kabhi mat maarna.”

Vinata ne apne bete ko aashirvaad diya:

“Tumhare pankhon ko Marut dev raksha kare,
tumhari reedh ki haddi ko Surya aur Chandra,
tumhare sir ko Agni,
aur tumhare sharir ko Vasus.
O mere laal, surakshit raho…”

⭐ Garuda ka prabhas: Nishadon ka ant

Garuda ne apne vishal pankh failaaye
aur aakaash mein tezi se udda.

Woh samundar paar karke
Nishadon ke sheher ke upar pahunch gaya—
bhookh se Yamraj ki tarah bhayankar.

Usne:

apne pankhon se dhoondh ka bada tufaan khada kar diya,

samundar ka paani upar kheench liya,

parvaton ke ped tak hila diye,

aur sheher ke sab raste
apne vishal khule muh se band kar diye.

Nishad log darr ke maare bhaag kar
seedhe Garuda ke muh ki taraf bhagne lage—
jaise pedon se hattakar pakshi
toofan se bachaav ke liye aasman ka rasta pakad lete hain.

Dhundh se andhe ho chuke Nishad
samajh hi nahi paaye ki woh
Garuda ke muh mein ghus rahe hain.

Garuda ne jab apna muh band kiya,
to anek Nishad turant maar daale gaye.

Garuda ki bhookh ab shaant ho gayi thi—
aur ab woh amrit ki talash mein
aur aage badhne ke liye tayyar tha."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.17
        with st.expander("Section 1.5.17"):
            text1 = """ 
⭐ Section XXIX – Brahman ka Udhaar, Garuda ki Bhojan Ki Khoj, aur Do Shraapit Bhaiyon ka Rahasya

(Hinglish Story Rewrite)

Garuda ne hazaaron Nishadon ko nigal liya tha—
par achanak uske gale mein ek tez jalan mehsoos hui.

Woh ek Brahman tha, apni patni ke saath,
jo galti se Garuda ke muh mein ghus gaya tha!

Brahman ki tapta-angaar jaisi tapasya
Garuda ko jalane lagi.

Garuda ne turant kaha:"""
            create_image_text_layout("attached_assets/chapter1/1.5.17.jpg", text1, layout="side", image_position="left")
            text2 = """ 
“Hey Brahman! Jaldi bahar aa jao!
Main kabhi bhi Brahman ko nahi marta—
chahe woh paap hi kyun na kare.”

Brahman ne kaha:

“Main toh aa jaaunga…
par meri patni bhi saath aaye!”

Garuda ne kaha:

“Thik hai! Apni patni ko lekar
turant bahar aa jao.
Tum dono abhi pache gaye nahi ho—
isse pehle niklo!”

Brahman aur uski Nishad patni
Garuda ke muh se nikal gaye
aur usse aashirvaad dekar chale gaye.

⭐ Garuda apne pita Kasyapa se milta hai

Garuda aasman mein udda,
apne pita Rishi Kasyapa ke paas pahucha.
Pitaji ne pyaar se poocha:

“Beta, theek ho?
Kya tumhe poora khana mil jata hai?”

Garuda ne sach bata diya:

“Maa theek hai. Bhai bhi. Main bhi.
Par pitaji… mujhe poora khana nahi milta.
Snakes ne mujhe amrit laane bheja hai—
maa ko azaad karne ke liye.
Nishadon ko maine bahut kha liya,
par bhookh abhi bhi nahi mili!
Aap hi bataiye, main kya khaun
jisse main itna shaktishaali ban jaaun
ki amrit chura kar la sakun?”

⭐ Kasyapa ka raaz: Do shraapit bhai – Haathi aur Kachhua

Kasyapa muskuraaye aur bole:

“Beta, yeh jheel pavitra hai.
Yahan ek vishaal haathi
aur ek mahaan kachhua
lagataar ladte rehte hain.

Dono bhai the pichhle janm mein.”

✦ Unka purana janm – ek laalachi jhagda

Ek Rishi tha – Vibhavasu,
bahut gusse wala.

Uska chhota bhai Supritika,
hamesha bolta rehta:
“Hamein dhan baat lena chahiye!”

Bada bhai samjhata:

“Dhan baatne se bhrashtachar hota hai.
Baatne ke baad bhai-bhai ladte hain.
Dushman aur fasaad paida karte hain.
Alag hone se tabahi aati hai.”

Par Supritika nahi maana.

Gusse mein Vibhavasu ne kaha:

“Tum haathi ban jaoge!”

Aur Supritika ne jawab diya:

“Aur tum kachhua banoge!”

Dono ka shraap sach ho gaya.

Isliye aaj woh:

Haathi – 6 yojan uncha

Kachhua – 3 yojan uncha

lagataar ladte rehte hain.

⭐ Garuda ka agla bhojan: Haathi aur Kachhua

Kasyapa ne kaha:

“Beta, dono ko khaa jao.
Phir tum itne shaktishaali ho jaoge
ki amrit bhi laa sakte ho.”

Aur pitaji ne aashirvaad diya:

“Devtas se yuddh ho,
ved, mantr, ghrit, upanishad—
sab tumhari shakti banenge.”

Garuda pitaji ke charanon mein jhuk gaya
aur jheel ki taraf udda.

Wahaan usne dono dushman bhai dekhe
aur apne do bade panjon se
ek mein haathi,
aur doosre mein kachhua pakad liya—
jaise halke patthar ho!

⭐ Alamva ka divya jungle aur bolne wala vishaal bargad

Garuda aasman mein un dono ko le udda
aur Alamva naam ke divya van par pahucha.

Jab uske pankhon ki hawa lagi,
toh sona-chandi ke ped,
ratnon se sajhe vriksh
kaampne lage—
dar ke maare toot na jaayen!

Tab ek vishaal bargad ka ped,
jiska ek shakh 100 yojan lambi thi,
Garuda se bola:

“O Garuda!
Baithe yahan iss shakh par
aur araam se apna bhojan karo.”

Garuda us shakh par utar gaya—
magar uska sharir itna bhaari tha
ki poori shakh hi toot kar gir gayi!

Aasman ka sabse bada panchi
bhojan karne ko taiyaar tha…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.18
        with st.expander("Section 1.5.18"):
            text1 = """ 
⭐ Section XXX – Garuda ka Bhaari Bojh, Rishiyon ki Raksha aur Devlok Mein Darr

(Hinglish Story Rewrite)

Garuda ne jaise hi apne pair se ped ki badai shaakh ko chuha,
vah patak se toot gayi.

Par Garuda hairan reh gaya—
kyunki us shaakh par Valakhilya Rishis ulte latke tapasya kar rahe the!

Agar shaakh girti…
toh saare Rishis kuchal jaate.

Garuda ne turant apne daaye panje mein haathi,
aur baaye panje mein kachhua
aur beak se poori shaakh pakad li.

Woh teenon cheezein sambhalte hue
aasman mein udda—
sirf Rishiyon ko bachane ke liye.

Ye kaam itna kathin tha
ki Devta bhi aisa na kar paate!"""
            create_image_text_layout("attached_assets/chapter1/1.5.18.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Rishiyon ne hairan hoke kaha:

“Yeh pakshi itna bhaar lekar bhi aasman mein udd raha hai!
Iska naam hona chahiye Garuda—
matlab ‘bhaari bojh uthane wala’!”

⭐ Garuda apne pita Kasyapa ke paas

Garuda udte-udte Gandhamadana Parvat pahucha,
jahan uske pita Rishi Kasyapa tapasya kar rahe the.

Kasyapa ne apne vishaal, tejomay putra ko dekha—
jo haathi, kachhua aur ek baari-shaakh le ja raha tha—
toh woh chauk gaye.

Kasyapa ne kaha:

“Beta, sambhal kar!
Valakhilya Rishi surya ki kirno ka paan karte hain—
agar woh gusse ho gaye, toh tumhein jalakar raakh kar denge!”

Phir unhone Valakhilya Rishiyon ko manaya aur bola:

“Garuda sabke hit ke liye yeh kaarya kar raha hai.
Kripya ise anumati dijiye.”

Rishiyon ne shaakh chhod di
aur Himalaya ki taraf chale gaye tapasya karne.

⭐ Ab shaakh ko kahan phenka jaaye?

Garuda ne beak mein shaakh dabaye-dabaye
apne pita se puchha:

“Pitaji, is bhaari shaakh ko main kahan fekun?
Aisi jagah bataiye jahan koi insaan na ho.”

Kasyapa ne ek door aur barfili si pahadi ka zikr kiya
jahan jeevit prani tak jane ka soch bhi nahi sakte.

Garuda ne turant
haathi, kachhua aur vishaal shaakh lekar
hazaaron yojan door uddan bhari.

Ek pal mein wah pahad par pahunch gaya
aur shaakh ko neeche gira diya.

Dhaddd!
Itni zor ki awaz hui ki poora pahaad kaanp utha.
Sona-jade se sajhe hue patthar
aur phoolon se lade ped girne lage.

⭐ Garuda ka bhojan aur devlok mein daraawa sanket

Garuda ne pahaad ki choti par baith kar
haathi aur kachhua dono ko kha liya.
Phir woh tezi se aasman mein udda—
amrit lene ke liye.

Par jaise hi Garuda udda…
devlok mein ajeeb-ajeeb ashubh sanket dikhne lage:

Indra ka vajra chamak utha, jaise darr gaya ho.

Meteor din ke samay girne lage.

Hawayein garajne lagi.

Rakt ki baarish hone lagi!

Devtaon ki haar-maala murjha gayi.

Aasmaan bina badal ke bhi ghoom utha.

Indra ghabraakar Vrihaspati se poochha:

“Yeh sab kyon ho raha hai?
Kaun hamara dushman aa raha hai?”

Vrihaspati ne kaha:

“Garuda aa raha hai, hey Devraj.
Uski shakti apar hai.
Vah amrit lene ka sankalp kar chuka hai—
aur use rokna lagbhag asambhav hai.”

⭐ Amrit ki raksha ke liye devta taiyaar

Indra ne turant devtaon ko chetavani di:

“Garuda amrit churaane aa raha hai.
Taiyaar ho jao!”

Devtaon ne:

sona-jadit kavach pehne,

chakra, trishool, gadayein, talwaron jaise shastr uthaye,

amrit ke chaaron taraf ek loha-jaise majboot chakra bana liya.

Poora devlok ek tejasvi sena ke roop mein chamak utha—
sab Garuda ka intezar kar rahe the.

Aasmaan ek dusra surya mandal lag raha tha,
sabhi astron se prakash phoot raha tha."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.19
        with st.expander("Section 1.5.19"):
            text1 = """ 
⭐ Section XXXI – Indra ka Apmaan, Rishiyon ka Shraap, aur Garuda ka Janm

(Hinglish Story Rewrite)

Saunaka ne Sauti se poochha:

“Indra ki kya galti thi?
Garuda ka janm Valakhilya Rishiyon ki tapasya se kaise juda?
Kasyapa—jo ek Brahman the—unke ghar itna maha-shaktishaali pakshi kaise paida hua?
Garuda itna ajey, apar shakti wala aur ichchha se har jagah pahunchne wala kyun tha?”

Sauti bola:

“Tumne bahut uchit prashna kiya, Saunaka!
Ye sab ek Purana ki kathaa mein aata hai.
Dhyan se suno…”"""
            create_image_text_layout("attached_assets/chapter1/1.5.19.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Indra ka apmaan aur Rishiyon ka gussa

Ek baar Prajapati Kasyapa santan prapt karne ke liye ek bada yagya kar rahe the.
Saare devta, Rishi, aur Gandharva unki madad kar rahe the.

Indra ko yagya ke liye lakdi lana diya gaya.
Indra apni shakti ke anusar pahaad jaisa bojh utha kar bina thake chal pada.

Raaste mein usne dekha—
Valakhilya Rishis, jo sirf anguthay jitne bade the,
ek palāsha patte ka daanta saath milkar utha rahe the.

Woh Rishis bhojan ki kami se kamzor the,
aur raaste mein gaay ke khur ke gaddhe ke paani mein gir kar pareshaan ho gaye.

Indra ne unhe dekha…
aur hans pada.

Phir unke sir ke upar se uchhal kar nikal gaya—
jaise unka mazaak uda raha ho.

Rishiyon ko yeh beizzati bardaasht na hui.
Unhone yagya ki tayyari ki aur kaha:

“Ham ek aisa Indra paida karenge—
jo vartamaan Indra se bhi adhik shaktishaali ho,
jo man ki gati se chale,
jo ichchha se shakti paida kare,
aur jo devon ke raja ko bhi daraye!”

Indra ye sunkar gabra gaya
aur turant Kasyapa ke paas bhaaga.

⭐ Kasyapa ka madhyasthata

Kasyapa ne Rishiyon se puchha:

“Kya tumhara yagya safal ho gaya?”

Rishiyon ne kaha:

“Haan, jo hoga, tumhare kahe anusaar hi hoga.”

Tab Kasyapa ne unse kaha:

**“Brahma ne vartamaan Indra ko teenon lokon ka swami banaya hai.
Tum phir se ek doosra Indra laane ki ichchha rakhte ho—
yeh Brahma ke vachan ke viruddh ho jayega.

Par tumhara yagya vyarth bhi na ho.
Isliye tumhaari tapasya se
pakshiyon ka Indra paida ho—
jo atishay shaktishaali ho!”**

Valakhilya Rishiyon ne kaha:

“Acha, Prajapati, hum apni ichchha tumhe saup dete hain.
Tum hi faisla karo.”

⭐ Vinata ka var aur Garuda ka garbh

Tabhi Daksha ki beti Vinata, Kasyapa ki patni,
tapasya karke pati ke paas aayi.

Kasyapa ne kaha:

“Tumhe do putra milenge—bahut shaktishaali aur teenon lokon mein poojit.
Ye tumhari ichchha aur Valakhilya Rishiyon ki tapasya ka phal hai.”

Phir unhone kaha:

“Yeh do putra sab pakshiyon ke swami honge.
Ve ichchha se koi bhi roop dharan kar sakenge.”

Indra ko bhi santvana di gayi:

“Ye do bhai—Aruna aur Garuda—tumhari madad karenge, tumhara nuksaan nahi.”

Vinata prasanna ho gayi
aur kuch samay baad
Aruna aur Garuda ka janm hua.

Aruna kaal-purush Surya ka sarathi bana.

Garuda ban gaya sab pakshiyon ka raja,
teenon lokon mein adbhut,
ajey, apar shakti se sampann,
aur apni ichchha se har jagah pahunchne wala.

Sauti ne kaha:

“Ab suno Garuda ke mahaan kaaryo ki kathaa…”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.20
        with st.expander("Section 1.5.20"):
            text1 = """ 
⭐ Section XXXII – Garuda ka Devtas se Maha-Yudh aur Amrit ki Khoj

(Hinglish Story Rewrite)

Sauti bola:

“He Brahmanon ke sheersh, jab devta yudh ki poori taiyari kar chuke the, tabhi Garuda—pakshiyon ka raja—vahaan bijli ki tarah aa pahuncha!”

Garuda ka shaktishaali, tejomayi roop dekh kar
saare devta kaanp uthhe.
Dar ke maare ve apne hi hathiyaar galat disha mein chalane lage."""
            create_image_text_layout("attached_assets/chapter1/1.5.20.jpg", text1, layout="side", image_position="left")
            text2 = """ 
⭐ Garuda vs. Vishvakarma (yuddh ek pal ka)

Amrit ki raksha karne walon mein Vishvakarma, devtaon ke maha-vastru-nirmata, bhi the—
bahut tej, bahut shaktishaali.

Lekin Garuda ne sirf ek pal ke yuddh mein
apne panjon, chonch aur pankhon se use dhool chata di—
aur Vishvakarma zameen par bejaan jaise gir peya.

⭐ Andhi, aandhi, aur andhera!

Garuda ne apne bade-bade pankhon se
itni tez hawa aur itni dhool uthayi
ki poora aasman andhera ho gaya.

Devtaon ki aankhen bandh ho gayi.
Ve kuch dekh na sake, behosh hone lage.

Garuda ne poore swarg lok ko hila diya.
Devta use dhoond hi nahi pa rahe the!

⭐ Indra ka aadesh: “Vayu, is dhool ko hatao!”

Indra—sahasra-netra—bulaaya:

“Vayu! Jaldi aa.
Is dhool ko hatao, hum kuch dekh hi nahi pa rahe!”

Vayu dev ne turant aandhi saaf ki.
Jab dhool gayi…

Devtaon ne phir se Garuda par humla bol diya!

⭐ Garuda ki dahaar – Yuga-ant ki tarah

Garuda ne ek dahaar maari—

“GROOOAAHHH!”

Aisi dahaar jaise Yuga ke ant par badal garajte hon.
Saare prani dar se kaanp gaye.

Fir Garuda aasman mein tezi se uchla
aur chaaro taraf se devtaon par vaar karne laga.

⭐ Devtaon ka har disha mein bhaagna

Garuda ke pankh, chonch aur panje
devtaon ko bhari ghav dene lage.
Khoon behta ja raha tha.

Garuda ki shakti se har group bhaag gaya:

Sadhya aur Gandharva – Poorv ki disha

Vasu aur Rudra – Dakshin

Aditya – Paschim

Ashvini Kumar – Uttar

Sab bhaagte hue peeche mud mud kar dekhte ja rahe the—
Garuda unke peeche aayega kya?

⭐ Garuda vs. Yakshas – Khooni toofan

Garuda ne phir Yakshon se mukabala kiya—
Asvakranda, Rainuka, Krathanaka, Tapana, Uluka, Nimesha, bhot saare.

Garuda ne sabko
pankh, panje aur chonch se chithda-chithda kar diya,
bilkul us tarah jaise Mahadev pralay ke samay shatruon ko maarte hain.

Yaksha lag rahe the jaise kaale badal
jisme se laal khoon ki baarish ho rahi ho.

⭐ Amrit tak pahunch – Aag ki deewaar

Saare rakshak hara kar
Garuda seedha Amrit ki taraf gaya.

Lekin wahaan…

Amrit ko chaaro taraf se aag ne gher rakha tha—
aag itni tej ki jaise sooraj ko bhi jala de.

⭐ Garuda ka adbhut roop – 90×90 mooh!

Garuda ne turant ek adbhut roop dharan kiya—

Nabbe guna nabbe mooh! (8100 mouths!)

Un moohon se
bahut saari nadiyon ka paani ek saath peeya
aur bijli se bhi tez wapas aa kar
wo saara paani aag par daal diya.

🔥 Aag turant bujh gayi!

Amrit tak ka raasta saaf ho gaya.

⭐ Amrit ki raksha tod kar andar pravesh

Aag bujhte hi
Garuda ne apna roop bahut chhota kar liya—

jaise ek chhota sa chidiya—

taaki woh Amrit-ke-kund ke andar chori-chupe pravesh kar sake.

“Ab Amrit pakadne ka waqt aa gaya…”
—Garuda ne man mein socha."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.21
        with st.expander("Section 1.5.21"):
            text1 = """ 
Garuda ek din sun ki tarah chamakta hua golden shareer banakar Soma-ke-ghar ke paas jaa pahucha.
Wahan usne ek bhaari, steel ka chakr dekha—itna tez ki kisi ko bhi kaat de. Woh chakr bina rukhe ghoom raha tha.

Garuda ek pal rukkar socha,
“Iske beech se jaa sakta hoon.”
Aur phir apne aap ko chhota karke aankh jhapakte chakr ke andar ghus gaya.

Andar do bhayankari saanp Soma ki raksha kar rahe the—unki aankhen aag ki tarah jal rahi thi, zubaan bijli ki chamak jaisi, aur gussa toh jaise kabhi khatam hi na ho. Unko dekhte hi koi bhi raakh ban jaata.

Par Garuda bahut chaalak tha.
Usne apne pankh se dhool udaakar unki aankhen dhak di.
Saanp kuch dekh hi nahi paaye—aur Garuda ne tez hamla karke unhe hara diya.

Phir bina waqt gavaaye Garuda ne Amrit ka ghada utha liya.
Chakr ko todkar woh aasman ki taraf ud gaya—Amrit lekar par khud uska ek boond bhi nahi piya. Aasman tak andhera ho gaya, kyunki Garuda ki tej roshni suraj ko bhi dhak rahi thi!"""
            create_image_text_layout("attached_assets/chapter1/1.5.21.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🕉️ Garuda meets Vishnu

Raste mein Garuda ki mulaqat Bhagwan Vishnu se hui.
Vishnu ne muskurakar kaha:

“Garuda, tumne Amrit liya par piya nahi. Main tumhe ek vardaan deta hoon.”

Garuda bola:

“Mera pehla vardaan yeh ho ki main hamesha aapke upar rahun.”
“Aur doosra—main bina Amrit piye hi ammar aur rogon se door rahun.”

Vishnu ne kaha, “Tathastu.”

Garuda ne bhi kaha,
“Prabhu, aap bhi mujhse ek vardaan maang lijiye.”

Vishnu ne haskar kaha:

“Garuda, tum mere vaahan ban jao.”

Garuda ne turant haan kar di.

⚡ Indra attacks!

Garuda Amrit lekar jaa raha tha ki Indra ne Vajra un par phenka.
Vajra Garuda se takraya, par Garuda muskura kar bola:

“Main Rishi Dadhichi ka samman karta hoon, jinke asthi se tumhara Vajra bana hai.
Main Vajra ka bhi samman karta hoon, aur tumhara bhi, Indra.
Par tumhari bijli ne mujhe chot tak nahi pahunchayi.”

Yeh kehkar usne ek sundar pankh gira diya. Sab log us pankh ko dekhkar prasan ho gaye aur bole:

“Yeh pakshi Suparna kehlaayega—jiske pankh sundar hain.”

Indra hairaan ho gaya aur bola:

“Garuda, tumhari shakti ka koi ant hai?
Main tumse hamesha ki dosti chahta hoon.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.22
        with st.expander("Section 1.5.22"):
            text1 = """ 
Garuda ne Indra se kaha,
“Purandara, agar tum chaho to hum dono dost ban sakte hain. Par meri shakti bahut bhaari hai.”

Garuda ne dheere se bataya,
“Achhe log apni taareef nahi karte, par tum mere dost ban gaye ho, isliye bata raha hoon.
Main apne ek pankh par poori dharti, samundar, pahaad… aur tumko bhi utha sakta hoon.
Main sab ko, saare lokon ko, bina thake sambhal sakta hoon.”

Indra yeh sunkar hairaan bhi hua aur khush bhi.
Usne kaha,
“Garuda, tumhari baat sahi lagti hai. Ab hum sachche dost hain. Agar tumhe Amrit nahi chahiye, to use wapas de do. Jise tum doge, woh hamare dushman ban jayenge.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.22.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Garuda shant se bola,
“Main Amrit kisi ko peene nahi doonga.
Bas ek kaam ke liye le jaa raha hoon.
Jab main ise zameen par rakh doonga, tum turant aa kar ise le jaana.”

Indra khush ho kar bola,
“Garuda, tumhari imandari par mujhe garv hai.
Mujhse koi bhi vardaan maang lo.”

Garuda ko yaad aaya ki uski maa Vinata saanpon ki gulami mein thi.
Aur saanp—Kadru ke bete—usey tab chhodenge jab woh unke liye Amrit laayega.

Garuda ne kaha,
“Sakra, meri maa ka dukh tum jaante ho.
Bas mujhe vardaan do ki saanp mere khaadya ban jayen.”

Indra ne turant kaha,
“Tathastu. Aisa hi hoga.”

Phir Indra wapas Hari (Vishnu) ke paas gaya. Vishnu ne bhi Garuda ke faisle ko maan liya.

🐍 Amrit aur Saanpon ka Vichitra Pal

Garuda tez gati se apni maa ke paas pahucha aur saanpon se bola:

“Yeh raha Amrit! Main ise kusa ghaas par rakh raha hoon.
Tum sab snaan aur pooja karke aa kar peena.
Aur aaj se meri maa azaad hai.”

Saanp khushi se bole,
“Thik hai Garuda, hum abhi snaan kar ke aate hain!”

Par jaise hi saanp chale gaye, Indra neeche aaya aur Amrit utha kar aasman mein laut gaya.

Jab saanp wapas aaye, unhone dekha—
kusa ghaas khaali! Amrit gayab!

Ghabraakar unhone ghaas ko apni zubaan se chaat diya.
Isse unki zubaan do hisson mein waant gayi—tab se saanp do-farqi zubaan wale hote hain.
Aur kusa ghaas bhi pavitra ho gayi.

🦅 Garuda — Azaadi Aur Parakram

Garuda ab bahut khush tha.
Uske kaaran maa Vinata azaad ho gayi thi.
Aur ab woh saanpon ko kha bhi sakta tha.

Garuda apni maa ke saath jungle mein aaraam se rehne laga.
Saare pakshi uska samman karte the."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.23
        with st.expander("Section 1.5.23"):
            text1 = """ 
Saunaka Rishi ne Sauti se pucha:
“Tumne humein bataya ki saanpon ko apni maa Kadru ne kyun shraap diya, aur Vinata ko bhi apne bete ne kyun shraap diya.
Tumne ye bhi bataya ki Kasyapa ne dono patniyon ko kaise vardaan diye.
Vinata ke do bete—Arun aur Garuda—ke baare mein bhi humne sun liya.
Lekin ab humein ye batao—saanpon ke mukhya naam kaun-kaun se the?”

Sauti muskuraya aur bola:
“Rishiwar, saare saanpon ke naam ginana bahut lamba ho jayega.
Isliye main sirf sabse important, mukhya saanpon ke naam bataunga.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.23.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Phir Sauti ek-ek karke un bade saanpon ke naam ginta gaya:

Sesha — sabse pehle janme, sabse shaktishaali.

Vasuki — jo samudra manthan mein rassi bane the.

Airavata

Takshaka

Karkotaka

Dhananjaya

Kalakeya

Mani, Purana, Pinjaraka, Elapatra

Vamana, Nila, Anila

Kalmasha, Savala, Aryaka

Ugra, Kalasapotaka, Suramukha

Dadhimukha, Vimalapindaka, Apta, Karotaka

Samkha, Valisikha, Nisthanaka, Hemaguha

Nahusha, Pingala, Vahyakarna, Hastipada

Mudgarapindaka, Kamvala, Asvatara, Kaliyaka

Vritta, Samvartaka, Padma, Mahapadma

Sankhamukha, Kushmandaka, Kshemaka, Pindaraka

Karavira, Pushpadanshtraka, Vilvaka, Vilvapandara

Mushikada, Sankhasiras, Purnabhadra, Haridraka

Aparajita, Jyotika, Srivaha, Kauravya

Dhritarashtra, Sankhapinda, Virajas, Suvahu

Salipinda, Prabhakara, Hastipinda, Pitharaka

Sumuksha, Kaunapashana, Kuthara, Kunjara

Kumuda, Kumudaksha, Tittri, Halika

Kardama, Vahumulaka, Karkara, Akarkara

Kundodara, Mahodara

Sauti ne phir kaha:
“Ye sirf mukhya saanp hain.
Inke bete-pote, aur unki aage ki peedhiyan itni zyada hain ki ginana mushkil hai. Duniya mein saanp lakhon-crore ki sankhya mein hain.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.24
        with st.expander("Section 1.5.24"):
            text1 = """ 
Saunaka Rishi ne poocha:
“Tumne bahut saare shaktishaali saanpon ke naam bataye. Par shraap sunne ke baad unhone kya kiya?”

Sauti ne jawab diya:
“In sab mein, sabse mahaan tha Sesha.
Shraap sunte hi woh chup-chaap apni maa se door chala gaya aur kathin tapasya karne laga.”

Sesha hawa par jeeta tha, sirf dhyaan aur sankalp.
Woh Gandhamadan, Badri, Gokarna, Pushkara, aur Himavat ke charnon tak ghoomta raha—
hamesha tapasya, hamesha shanti, hamesha ek hi iccha ke saath:
“Main bure saanpon se door rehna chahta hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.24.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Aakhir Brahma ji ne usko dekha.
Sesha bilkul sukha, kapde faate huye, baal bandhe, par mann bilkul shant.

Brahma ji bole:
“Sesha, tumhari tapasya bahut kathor hai.
Tum saari praja ko dara rahe ho.
Batao, kya chahte ho?”

Sesha ne dheere se kaha:
“Mere bhai—saare saanp—dushman jaise hain.
Irsha, jhagda, dusmani… sab unmein bhara hai.
Unhe Vinata aur Garuda se bhi jalan hai.
Main unke saath ek janam bhi nahi rehna chahta.
Isliye main tapasya kar raha hoon, takki main unse door ho jaun—iss janam mein bhi aur aane waale janmon mein bhi.”

Brahma ji muskuraye.
“Tumhare bhaiyon ki badi galti hai, par maine pehle hi iska upaay rakh diya hai.
Tum unke liye mat chinta karo.
Tumhara mann dharm mein laga rahe—that is the best.
Ab mujhse ek vardaan maango.”

Sesha ne haath jod kar kaha:
“Mera mann hamesha dharm, tapasya aur shanti mein laga rahe.”

Brahma ji bahut khush hue.
Phir unhone ek bada kaam diya:

“Sesha, dharti bahut hilti rehti hai—pahaad, samundar, jangale sab uspar hai.
Tum usse apne sir par sambhalo.
Isse saari praja ka bhala hoga.”

Sesha ne bina sankoch kaha:
“Aapka aadesh hi mera kartavya hai.”

Phir woh ek gehri surang se dharti ke neeche gaya.
Wahan usne apne bade, anant shareer se poori dharti ko sambhal liya—
jaise ek bada sa takiya jise koi kabhi hila nahi sakta.

Brahma ji bole:
“Sesha, tum khud Dharma ho.
Jis tarah main ya Indra vishwa ko sambhalte hain,
waise hi tumne bhi dharti ko sambhala hai.”

Aur ant mein Brahma ji ne Sesha ko ek saathi diya—
Garuda, Vinata ka beta, jiske pankh chamakdar aur hriday pavitra tha.

Is tarah Sesha—Ananta Naag—hamesha ke liye dharti ka aadhar ban gaya."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.25
        with st.expander("Section 1.5.25"):
            text1 = """ 
Kadru ke shraap ke baad, Vasuki, saanpon ka neta, bahut ghabra gaya.
Usne sab bhaiyon—Airavata aur dusre saanpon—ko bula kar bola:

“Maa ka shraap hum par girne wala hai.
Agar humne kuchh na kiya toh hum sab ka anth pakka hai.
Chalo milkar sochte hain ki is shraap ko kaise roka jaaye.”

Sab saanp ek jagah baith kar baat karne lage."""
            create_image_text_layout("attached_assets/chapter1/1.5.25.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🐍 Kuch saanpon ki chalak salaah

Ek group bola:
“Hum Brahmanon ka roop dhar kar Raja Janamejaya ke paas jayenge aur kahenge—
‘Maharaj, yeh saap-yagya mat karo.’”

Doosra group bola:
“Hum uske sabse kareebi mantri ban jaayenge.
Fir woh humse salaah maangega, aur hum usse kahenge ke yagya na kare.”

Kuch aur saanp bole:
“Jo Brahman us yagya ka mukhya purohit banega,
usko kaat kar maar do.
Purohit hi nahi hoga toh yagya ruk jayega!”

🐍 Achhe dil wale saanpon ki baat

Par kuch saanp bade dayaalu the.
Unhone turant mana kiya:

“Brahmano ko maarna paap hai.
Galat raasta hamesha vinash laata hai.”

🐍 Aur bhi ajeeb-o-gareeb ideas aaye

Koi bola:
“Hum badal ban kar bijli-chamak ke saath baarish gira kar yagya ki agni bujha denge.”

Koi bola:
“Raat ko chori se Soma-ras chura lenge.”

Kuch saanp gusse mein bole:
“Hum hazaaron ki sankhya mein logon ko kaat kar bhaga denge.”

Doosre bole:
“Hum khaana bigaad denge taaki yagya ho hi na sake.”

Kuchne to yeh tak kaha:
“Raja ko hi pani mein khelte waqt chura kar le chalte hain!”

Aur sabse kathor salah ye thi:
“Raja Janamejaya ko hi kaat kar maar do.
Raja hi nahi hoga toh yagya kaise hoga?”

🐍 Sab Vasuki ki taraf dekhne lage

Sabne apni-apni baatein keh kar Vasuki ki taraf dekha.

Vasuki ne bahut der socha, phir shant awaaz mein bola:

**“Aap sab ki salaah suni,
par sach kahun toh koi bhi sahi nahi lagti.

Na hume paap karna chahiye,
na hume teesra raasta dikh raha hai.

Mere hisaab se hume apne pita—
Mahaan Rishi Kasyapa—
ki sharan me jaana chahiye.
Unki kripa hi hume bacha sakti hai.”**

Aur usne aakhir mein kaha:

“Jo bhi faisla hoga,
uski zimmedari meri hogi.
Isliye mujhe bahut soch-samajh kar kadam uthana hoga.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.26
        with st.expander("Section 1.5.26"):
            text1 = """ 
Section XXXIX — Hinglish Kahani (Summary Style)

Elapatra ki baat sunte hi saare saanp bahut khush ho gaye.
Woh sab zor se bole: “Waah, bahut sahi kaha!”

Iske baad Vasuki, saapon ka raja, ne apni behen Jaratkaru ko bohot pyaar se paalna shuru kiya.
Woh jaanta tha ki ek din woh hi saapon ko bachayegi."""
            create_image_text_layout("attached_assets/chapter1/1.5.26.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🌊 Samudra Manthan aur Vasuki ka Dar

Thodi hi der mein devta aur asur milkar samudra ka manthan karne lage.
Aur rassi kis ko banaya? Vasuki ko!

Manthan ke baad, Vasuki devtaon ke saath Brahma ji ke paas gaya.
Devtaon ne vinamrata se kaha:

“Prabhu, Vasuki apni maa ke shraap se bahut pareshan hai.
Woh hamesha hamara mitra raha hai.
Kripya uska dukh door kijiye.”

🌟 Brahma Ji ka Upay

Brahma ji ne shaant hoke kaha:

**“Jo Elapatra ne kaha tha, woh bilkul sahi hai.
Sirf bure saanp hi marenge, achchhe bache rahenge.

Rishi Jaratkaru janam le chuke hain aur tapasya kar rahe hain.
Jab sahi samay aaye, Vasuki apni behen Jaratkaru ka vivaah us Rishi se kar de.
Yahi saapon ko vinash se bachayega.”**

🐍 Saanpon ko Diya Gaya Kaam

Brahma ji ki baat sun kar Vasuki ko umeed mili.
Usne sab saanpon ko bula kar kaha:

**“Dhyaan se suno!
Jab bhi Rishi Jaratkaru kahen ki unhe patni chahiye,
turant mujhe khabar dena.

Hamari saari jaati ki suraksha isi par depend karti hai.”**

Saanp taiyaar ho gaye—ab sab us pal ka intezaar karne lage jab Rishi patni maangenge."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.27
        with st.expander("Section 1.5.27"):
            text1 = """ 
Section XL — Hinglish Kahani (Summary Style)

Saunaka ne Sauti se pucha:
“Jaratkaru naam kyon pada? Iski kahani kya hai?”

🌿 Jaratkaru Naam ka Matlab

Sauti ne shanti se bataya:
“Jara ka matlab hota hai ‘ghatna’ ya ‘waste’,
aur Karu ka matlab hota hai ‘bahut bada’.

Rishi Jaratkaru ka sharir pehle bahut bada tha,
phir kathin tapasya karte-karte woh dheere-dheere patla ho gaya.
Isi liye unka naam Jaratkaru pada.
Aur Vasuki ki behen ka naam bhi isi wajah se Jaratkaru tha."""
            create_image_text_layout("attached_assets/chapter1/1.5.27.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Saunaka muskura kar bola, “Theek hai, samajh gaya.”
Phir usne pucha, “Ab hume batao Astika ka janm kaise hua.”

🌱 Rishi Jaratkaru aur Vivah ki Talash

Sauti ne kahani aage badhai:

Vasuki chah raha tha ki woh apni behen ka vivaah Rishi Jaratkaru se kara de.
Lekin Rishi ji din-raat tapasya mein lage rehte,
unhe shaadi ki bilkul ichchha nahi thi.
Woh poori dharti par ghoomte, brahmacharya aur tapasya mein doobe rehte.

🏹 King Parikshit ki Galti

Isi dauraan, ek raja the—Parikshit, bahadur aur shikar ke shaukeen.
Ek din unhone ek hiran ko baan mara aur uska peecha karte-karte gehre jungle mein pahunch gaye.

Pyaas aur thakan se pareshaan, unhe ek Muni dikhe,
jo go-shala mein chup-chaap baitha tha,
aur bachdon ke muh se girti dudh ki jhaag peete hue tapasya kar raha tha.

Parikshit ne pucha:
“Hey Brahman, kya tumne ek ghayal hiran ko idhar bhagte dekha?”

Lekin Muni maun-vrat me the—unhone ek shabd bhi nahi bola.

Raja ko gussa aa gaya,
aur unhone apne dhanush ki nok se ek mara hua saanp uthaya,
aur Muni ke kandhe par rakh diya.

Muni ne tab bhi kuch nahi kaha—
woh chup-chaap baitha raha.

Thodi der baad raja ko apni galti ka ehsaas hua,
woh sharminda hokar wapas mahal laut gaya.

🐍 Rishi ka Beta – Sringin

Muni ke bete ka naam tha Sringin—
bahut tapasvi, bahut gusse wala, aur maafi dene mein bilkul kathor.

Ek din jab Sringin apne guru ke paas se ghar laut raha tha,
toh uska dost Krisa hans padha aur bola:

**“Sringin, itna ghamand mat karo!
Tumhare pitaji ke kandhe par ek mara hua saanp pada hai.
Aur tum yahan apne gyaan ka dikhava kar rahe ho?

Unhone kuch galat nahi kiya,
phir bhi unhe yeh apmaan jhelna pada.
Mujhe to aisa lag raha hai jaise yeh saza mujhe mili ho.”**

Sringin yeh sun kar aag ki tarah bhadak utha—
aur yahi se aage ki kahani Astika ke janm ki taraf badhti hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.28
        with st.expander("Section 1.5.28"):
            text1 = """ 
🌩️ Sringin Ka Gussa

Sauti ne bataya:

Jab Krisa ne Sringin ko bola ki “Tumhare pitaji ke kandhe par ek mara hua saanp rakha hai,”
to Sringin ka chehra laal-hot anger se bhar gaya.

Sringin ne dhire se pucha:
“Mere father ke saath aisa kisne kiya? Kis baat ka badla tha?”

Krisa ne jawab diya:
“Raja Parikshit shikar karte-karte thak gaye the.
Unhone tumhare pitaji se hiran ke baare mein pucha,
par woh maun-vrat me the, isliye nahi bole.
Gusse me Raja ne bow se uthakar ek dead snake unke kandhe par rakh diya.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.28.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Shraap Dene Ki Galti

Yeh sunte hi Sringin ka gussa phat padta hai.
Woh paani chho kar shraap deta hai:

“Raja Parikshit ne Brahman ko apmaan kiya hai.
Saat din ke andar Takshak naam ka zehreela naga use maar dalega!”

Shraap dekar Sringin apne father ke paas pahunchta hai.
Woh unhe dead snake ke saath baitha hua dekhta hai
aur phir se rosh me bhar jaata hai.

Woh rota hua bolta hai:
“Pitaji, maine Raja ko shraap de diya hai!
Usne aapka apmaan kiya, isliye woh marne layak hai.”

👳‍♂️ Father ki Samajh Bhari Daant

Rishi-father ne shant swar me kaha:

**“Beta, yeh tumne bahut galat kiya.
Ascetic ka kaam badla lena nahi hota.

Raja hume raksha deta hai.
Hume shanti aur dharam se jeene deta hai.
Agar raja na ho to log anushasan me nahi rahte.”**

Unhone samjhaya:

Raja galti se gussa kar gaya, jaane-bina ki main maun-vrat me hoon.

Hum jaise tapasvi logon ko bhi Raja ki raksha chahiye hoti hai.

Dharam yahi kehta hai ki Raja ko maaf kar dena chahiye.

Aakhir me Rishi ne dukh se kaha:
“O mere bachche, Raja Parikshit hamara shraap ka patra nahi tha.
Tumne bachpana dikhaya hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.29
        with st.expander("Section 1.5.29"):
            text1 = """ 
🌩️ Sringin Ka Zidd

Sauti ne bataya:

Jab Samika ne apne beta Sringin ko shant karna chaha,
to Sringin ne zidd se jawab diya:

“Pitaji, chahe aapko pasand aaye ya na aaye…
mera diya hua shraap kabhi vyarth nahi jayega.
Main kabhi jhooth nahi bolta.”

Samika ne pyaar aur dukh ke saath kaha:

“Beta, tum satya-vadi ho, tapasvi ho,
isliye tumhare shabd jarur sach honge.
Par bachcha hone ke bawajood tumne gusse me galti ki hai.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.29.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🕊️ Father Ki Seekh

Samika ne dheere se samjhaya:

“Ascetic ka kaam shanti lana hai, badla lena nahi.”

“Krodh tapasya ka phal jala deta hai.”

“Jo maaf kar sakta hai, wahi bade lokon me jagah paata hai.”

Phir unhone kaha:

“Main raja ko sandesha bhejunga.
Woh jan le ki shraap ek bachche ke gusse ki wajah se hua hai.”

Samika ne apne shishya Gaurmukha ko bulaya
aur use Raja Parikshit ke paas bheja.

🏰 Sandesha Raja Tak Pohonchta Hai

Gaurmukha ne rajmahal jaakar respect se message diya:

“Raja Parikshit,
Aapne anjaan me ek maun-vrati Rishi ke kandhe par dead snake rakha.
Rishi ne toh maaf kar diya,
par unke bete Sringin ne aapko shraap de diya hai—
Saat din ke andar Takshak naga aapko kaatega.”

Yeh sunte hi Raja Parikshit ka dil toot gaya.
Woh apni maut se kam,
apne durvyavhaar par zyada pachtaya.

🛡️ Raja Ki Tayari

Raja ne turant mantriyon se salah ki
aur ek uunchi, ek-pillared mansion banwayi.
Uske aas-paas:

vaidya

mantrik Brahman

suraksha ke pehredaar

sab ko tainaat kiya gaya.

Koi hawa tak andar na ja sake—
itni sakht security thi.

🐍 Takshak aur Kasyapa Ki Mulaqat

Jab sathvan din aaya,
mahan Rishi Kasyapa raja ko bachane ja rahe the.
Unka sochna tha:

“King ko bachakar, main punya aur dhan pa sakta hoon.”

Raaste me unki mulaqat ek buzurg Brahman se hui—
jo asal me Takshak tha.

Takshak ne poocha:

“Itni jaldi kahan ja rahe ho?”

Kasyapa bole:

“Takshak aaj raja ko dasega.
Main jaakar uska ilaaj karunga.”

Takshak muskura kar bola:

“Main hi Takshak hoon.
Aur meri zeher se bite hue ko
tum kabhi nahi bacha sakte.”

Kasyapa ne vishwas se jawab diya:

“Mere gyaan aur tapasya ke saamne,
tumhara zeher kuch nahi.
Main raja ko zaroor bachaa sakta hoon.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.30
        with st.expander("Section 1.5.30"):
            text1 = """ 
Section XLIII
🐍🔥 Takshak Ka Challenge

Ek din Takshaka ne Rishi Kasyapa se kaha:

“Agar tum waaqai kisi ko bhi bachaa sakte ho,
to pehle is bargad ke ped ko bachakar dikhao.
Main ise abhi zeher se jala deta hoon.”

Kasyapa shant se bole:

“Theek hai, tum ped ko dasto.
Main use phir se zinda kar dunga.”

Takshaka ne ped ko dant diya.
Ped turant zeher se jalne laga.
Aag ki tarah woh poora ped bhasm ho gaya."""
            create_image_text_layout("attached_assets/chapter1/1.5.30.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Phir Takshak ne hans kar kaha:

“Ab dikhao apni vidya!”

🌱 Kasyapa Ka Chamatkar

Kasyapa ne bhasm uthaya aur muskurakar bola:

“Dekho, gyaan ki shakti kya kar sakti hai.”

Unhone mantra ki shakti se:

ek chhota sa ankur banaya,

phir do patte,

phir tana,

phir shaakhen…

Aur dheere-dheere,
poora bargad ka ped dobara khada ho gaya!

Takshaka hairaan reh gaya.
Usne kaha:

“Tumhari vidya bahut badhi hai.
Par raja Parikshit ko bachane mat jao.
Woh Brahman ke shraap se marrne wala hai.
Agar tum nahi bachaa paaye,
to tumhari khyaati ko nuksaan ho jayega.
Main tumhe utna hi dhan de deta hoon.”

💰 Samjhauta

Kasyapa ne imaandaari se kaha:

“Main dhan ke liye hi ja raha hoon.
Agar tum de doge, to main laut jaunga.”

Takshaka ne kaha:

“Main raja se zyada tumhe de sakta hoon.
Mat jao.”

Tab Kasyapa ne yog-shakti se jaanch ki—
raja ki umr sach much poori ho chuki thi.

Isliye unhone Takshaka ka diya hua dhan liya
aur wapas chale gaye.

🏰 Takshak Ki Chalaki

Ab Takshaka raja ko marne ke liye
Hastinapur ki taraf utra.

Woh sun chuka tha ki raja
mantron, vaidyon aur suraksha ke beech
bahut sambhalkar reh raha hai.

Takshaka ne socha:

“Seedha attack karna mushkil hai…
humesha ki tarah chal chhedni hogi.”

Usne kuch saap ko fake ascetic bana kar
fruits, kusa grass aur paani ke saath raja ke paas bheja.

🍎 Vishwala Phal

Raja ne woh phal-kusha sab prem se accept kiya
aur apne mantriyon se kaha:

“Aao, sab milkar in dravyon ko khaate hain.”

Sab ne haan kar di,
kyunki kismet unhe isi taraf dhakel rahi thi.

Ek khaas phal jisme Takshaka insect ke roop me chhupa tha
raja ke haath lag gaya.

Jab raja us phal ko kha rahe the,
andar se ek chhota sa, ajeeb sa,
kaala-tamba rang ka keeda nikla.

Raja ne muskura kar kaha:

“Aaj suraj bhi doob raha hai.
Ab mujhe dar nahi.
Iskeeda ko hi Takshaka banne do.
Woh mujhe dase—
taaki shraap poora ho
aur mera paap dhul jaaye.”

Mantri, jo kismet ke haath ka khilona ban chuke the,
is baat se sehmat ho gaye.

🐍⚡ Takshaka Ka Antim Dasta

Raja ne keede ko apne gale par rakha.

Aur ek pal me—
Takshaka ne asli roop dhar liya!

Woh raja ke gale par lapet gaya,
zor se dahada,
aur ek hi vaar me
Parikshit ko dant diya.

Is tarah shraap poora hua
aur raja apni antim yatra par chale gaye."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.31
        with st.expander("Section 1.5.31"):
            text1 = """ 
🌩️ Section XLIV — Raja Parikshit ka Ant aur Janamejaya ka Rajya

Takshaka ne jab Raja Parikshit ko kaata,
to sab mantri dar se peele pad gaye.
Takshaka ka zor daar garajna sun kar
sabhi taraf afra–tafri mach gayi.

🐍 Takshaka Aasmaan Mein Uda

Mantriyon ne dekha ki Takshaka
aasmaan mein ek laal roshni ki dhaar ki tarah ud raha tha—
bilkul us maang ke sindoor jaisa
jo ek aurat ke baal ke beech mein chamakta hai."""
            create_image_text_layout("attached_assets/chapter1/1.5.31.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Mahal Jal Utha

Jahan Raja Parikshit rukte the,
woh mahal Takshaka ke zehreeli aag se jalne laga.
Mantri bhagne lage.
Aur raja… bijli ki tarah gira aur wahin shaant ho gaya.

⚰️ Antim Sanskaar Aur Naya Raja

Mantriyon aur raj purohit ne
poori shraddha se raja ka antim sanskaar kiya.
Phir nagar ke log ikattha hue aur bole:

“Hamara naya raja hoga… Janamejaya!”

Woh Parikshit ka chhota beta tha,
par bada buddhimaan aur shaant swabhav ka.

👑 Raja Janamejaya Ka Vivah

Jab Janamejaya thoda bada aur samajhdaar hua,
mantriyon ne socha:

“Ab yeh raja apne dushmano ka samna kar sakta hai.”

Isliye ve Kashi ke raja Suvarnavarman ke paas gaye
aur unki beti Vapushtama ka haath maanga.

Raja ne pooch–taach kar,
sab rivaazon se
apni beti Janamejaya ko de di.

Janamejaya bahut khush tha.
Vapushtama sundar thi, komal thi,
aur apne pati se bahut prem karti thi.

💕 Prem Aur Shanti Ka Samay

Raja Janamejaya ne
jangal, nadion, bagichon aur kheton mein
apni rani ke saath khushiyon bhare din bitaye—
bilkul purane yug ke Pururava jaise
jab usne apsara Urvashi ko paaya tha.

Raja ne apne dil mein
kisi aur ke liye kabhi jagah nahi banne di.
Rani Vapushtama bhi
apne prem aur seva se raja ka dil jeet leti thi."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.32
        with st.expander("Section 1.5.32"):
            text1 = """ 
🌿 Section XLV — Jaratkaru aur Uske Pitron ka Dukh

Ek din mahan tapasvi Jaratkaru poori dharti par ghoom rahe the.
Jahan shaam hoti, wahi unka aaj ka ghar.
Woh hawaa ko hi bhojan bana kar kathin tapasya karte,
aur roz aur patle hote ja rahe the.

🕳️ Ek Darawani Gufa aur Ulte Latakte Purvaj

Ek shaam unhone ek ajeeb drishya dekha—
ek gehri gufa ke andar, kuch purvaj ulte latak rahe the,
ek patli si virana jaddi ki rassi se."""
            create_image_text_layout("attached_assets/chapter1/1.5.32.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Woh rassi lagbhag kaat-chuki thi,
aur ek bada sa chooha (Time ka prateek)
use dheere–dheere chaba raha tha.

Purvaj bahut kamzor, bhooke, bechaare the.
Girne mein bas kuch hi pal baaki the.

Is drishya ko dekh kar Jaratkaru ka dil pighal gaya.

🙏 “Main Kya Madad Kar Sakta Hoon?”

Jaratkaru ne pyaar se poocha—

“Aap kaun ho?
Aap ulte kyun latak rahe ho?
Agar meri tapasya ka aadha, chautha… ya poora hissa de kar bhi
main aapko bacha sakoon, to main taiyaar hoon!”

Woh sach mein unki madad karna chahte the.

👴 Pitron ki Dard Bhari Kahani

Pitron ne dheere se jawab diya—

“Beta, hum Yayavara rishi vansh ke purvaj hain.
Humne kathin tapasya ki, dharm se jee kar uchche lokon tak pahunch gaye.
Lekin ek baat ki wajah se hum gir rahe hain…
humari vansh belaasi ho gayi hai.

Humari poori kulvansh ki rassi toot chuki hai—
sirf ek dhaga bacha hai… tum!

Tumhara naam bhi Jaratkaru hai.
Tum tapasya kar rahe ho, par tumhara koi beta nahi hai.
Isliye hum sab, aur tum bhi,
Time ke choohe ke kaato se
isko sankat mein pad gaye ho.

Beta, tapasya se zyada mahatvapurn hai
santaan ka hona,
kyunki santaan hi apne purvajon ko upar uthata hai.

🐀 Rassi, Choohha aur Arth

Phir unhone symbols samjhaaye:

Rassi = hamara vansh.

Khaali jagah = vansh ka tootna.

Ek bacha hua dhaga = tum, Jaratkaru.

Choohha = kaal (Time), jo sabko kamzor karta hai.

💬 “Beta, Jao aur Vivah Kar Lo!”

Pitron ne pyaar se kaha—

“Beta, agar tum humein bachana chahte ho,
to humein ek hi raasta dikhta hai—
vivah karo aur santaan paida karo.

Hamari taraf se yehi prarthana hai.
Agar tum Jaratkaru se milo,
to use sab kuch batana.”

Yah sun kar Jaratkaru andar se hil gaye—
kyunki unhe tab pata chala
ki yeh pitra unke apne hi purvaj hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.33
        with st.expander("Section 1.5.33"):
            text1 = """ 
🌿 Section XLVI — Jaratkaru Ka Dukh aur Unki Shart

Jaratkaru ne jab apne purvajon ki dard bhari baat suni,
to unka dil toot gaya.
Aankhon mein aansu bhar aaye.

😢 “Main Hi Aapka Paapi Vanshaj Hoon!”

Rote hue unhone kaha—

“Aap hi mere pitra ho… mere dada-par dada ho.
Main woh paapi beta Jaratkaru hoon.
Batao, main kya karoon?
Mujhe dand do, main is layak hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.33.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🧓 Pitron ka Sawal

Purvaj pyaar se bole—

“Beta, tum ab tak vivaah kyun nahi kiya?
Ek beta hi humara udhaar utaar sakta hai.”

🌱 Jaratkaru ki Saalon Purani Qasam

Jaratkaru ne shant awaaz mein kaha—

“Main to hamesha sochta tha ki
apne sharir ko tapasya se khatam karke
sidhe upar lok mein chala jaaun.
Maine vivaah ka sankalp nahi liya tha.

Par aaj aapko is haal mein dekhkar
mere mann ki drishti badal gayi.”

Phir unhone ek shart rakhi—

📜 “Agar Vivaah Karna Hai, To Sirf Iss Tarah…”

“Main tabhi shaadi karunga agar—

Kanya ka naam bhi Jaratkaru ho, bilkul mera jaisa.

Woh mujhe daan mein mil jaye, main usey paalunga nahi.

Woh khud apne mann se vivaah kare.

Agar aisi kanya mili, to main shaadi karunga—
aur mera beta hi aapka uddhaar karega.
Aap fir sada ke liye shanti mein reh sakenge.”

Purvajon ne unhe aashirvaad diya,
aur Jaratkaru phir se dharti par nikal pade.

🌳 Jaratkaru Ka Dukh Bhara Safar

Woh bohot bohot buddhe ho gaye the,
par unhe apni shart wali kanya nahi mili.
Woh pareshaan ho gaye—
apne purvajon ka dukh, unka bojh, unki zimmedaari
unka dil tod rahi thi.

Gehre jungle mein jaakar woh zor-zor se rote—

“Mujhe ek patni chahiye!
Jo daan mein mile!
Jiska naam bhi Jaratkaru ho!
Koi sun lo meri baat!”

Woh ye prarthna teen baar chillaye,
taaki saari srishti unki pukaar sun le.

🐍 Saanp Sun Lete Hain Prarthna

Vasuki ke saanp, jo pehle se hi Jaratkaru par nazar rakhe hue the,
turant bhaagkar apne raja ke paas gaye—

“Maharaj! Woh shaadi ke liye taiyaar hain!
Bas unhe ek aisi kanya chahiye jiska naam bhi Jaratkaru ho!”

Ye sunte hi Vasuki,
apni behen Jaratkaru ko lekar
us rishi ke paas pahunch gaye.

👰 Vasuki ki Behen — Jaratkaru

Woh sundar, shant, aur sajji hui thi.
Vasuki ne pyaar se kaha—

“Rishi ji, main apni behen aapko daan mein deta hoon.
Yeh aapke naam wali, Jaratkaru hai.”

Lekin Rishi ne turant haan nahi kahi.
Unhone doubt se poocha—

“Pehle iska naam batao.
Aur sun lo—
main usey paalunga nahi, yeh meri shart hai.”

Rishi sach mein apni sharton par dridh the.
Unke purvajon ki kismet ab
Vasuki ke jawab par tikki hui thi…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.34
        with st.expander("Section 1.5.34"):
            text1 = """ 
🌟 Section XLVII — Jaratkaru ka Vivaah aur Judai

Vasuki Rishi Jaratkaru ke saamne haath jod kar bola—

“O Mahaan Brahman,
ye meri behen hai — iska naam bhi Jaratkaru hai.
Yeh pavitra hai, tapasya karti hai.
Aap ise apnaaiye.
Iska poora dhyaan main rakhunga.”

Rishi ne shaant par sakht swar mein kaha—"""
            create_image_text_layout("attached_assets/chapter1/1.5.34.jpg", text1, layout="side", image_position="left")
            text2 = """ 
“Theek hai.
Par ek baat yaad rakhna—
main ise kabhi paalunga nahi.
Aur yeh kuch bhi aisa nahi karegi jo mujhe pasand na ho.
Agar kiya… to main usey turant chhod doonga.”

Vasuki ne vachan diya—
“Main apni behen ki zimmedaari leta hoon.”

💐 Shaadi Aur Naya Ghar

Rishi ne kanya ka haath pakda
aur shastron ke anusaar vivaah ho gaya.

Vasuki ne unke liye ek sundar kaksh banwayi—
soft bed, sukoon waali jagah, sab kuch tayyar.

Jaratkaru ne apni patni ko ek aur shart batayi—

“Kabhi kuch mat karna jo mujhe na pasand ho.
Agar hua— main yahan nahi rukunga.”

Bechari Vasuki ki behen,
dil mein darr lekar, dheere se boli—

“Jo aap keh rahe ho… wohi hoga.”

🕯️ Patni ki Seva aur Tapasya

Woh rishi ki har baat par nazar rakhti,
bilkul:

kutte jaise hamesha jaag rahi,

hiran jaise sharmeeli,

kagaz jaise har sanket pe dhyaan.

Ek din pavitra snaan ke baad,
woh apne pati ke paas aayi
aur woh garbhvati ho gayi.

Garbha ek jalti lau jaise tej tha —
din-pratidin badhta hua.

😴 Doopahar ki Neend Aur Syaahani Shaam

Ek din Rishi Jaratkaru
patni ki god mein sir rakh kar so gaye.

Shaam ka samay ho chuka tha,
suraj pashchim pahadon ke peeche jaa raha tha.

Patni ghabraa gayi—

“Agar Rishi ne sandhya-vandana nahi ki,
to inka punya kam ho jayega!
Par inhe uthaya… to ye naraaz ho jayenge.
Kya karoon?”

Soch-kar
dheere se unke kaan mein bola—

“Swami, jaag jaiye…
Suraj doob raha hai…
Aapko sandhya-prarthna karni hogi.”

⚡ Rishi ka Krodh

Rishi ne aankhen kholi,
unka hoth gusse se kaamp raha tha—

“Tumne mujhe be-ijzat kiya!
Main yahan nahi reh sakta.
Aise ghar mein nahi jahan meri neend tod di jaye!
Main ja raha hoon—
hamesha ke liye.”

Bechari patni ka dil toot gaya.

😭 Patni ki Vinanti

Aankhon mein aansu lekar boli—

“Swami, maine aapka apmaan nahi kiya.
Main to sirf aapke dharm ko bachana chahti thi.
Agar aap chale gaye,
to mera kya hoga?
Mere parivaar ka kya hoga?
Aapke bete se hi hamara vansh bachega.
Aap hume bina wajah mat chhodiye…”

✨ Rishi ka Antim Vachan

Rishi ne thoda shaant hokar kaha—

“Tumhare garbh mein jo bachcha hai,
woh agni jaise tej,
mahaan tapasvi,
aur Vedon ka gyani hoga.”

Ye kehkar
Rishi Jaratkaru
phir se apni tapasya ke liye
jungle ki aur chal diye.

Patni aansuon ke saath
unhe door jaate dekhti reh gayi…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.35
        with st.expander("Section 1.5.35"):
            text1 = """ 
✨ Section XLVIII — Astika ka Janm

Jaratkaru Rishi jaise hi chale gaye,
unki patni Jaratkaru (Vasuki ki behen) roti hui
apne bhai ke paas pahunchi.

Usne sab kuch bata diya—
kaise Rishi naraaz hokar chale gaye.

🐍 Vasuki ka Dard

Apni behen ki baat sunte hi
Vasuki aur bhi dukhi ho gaya.

Woh bola—"""
            create_image_text_layout("attached_assets/chapter1/1.5.35.jpg", text1, layout="side", image_position="left")
            text2 = """ 
“Behen… tum jaanti ho na,
tumhari shaadi ka ek hi uddeshya tha—
agar tumhare ghar ek beta paida ho jaye,
to woh hum saapon ko aane wale sarp-yagya se bachayega.
Brahmaaji ne bhi kaha tha ki woh bachcha humara rakshak hoga.
Kya tumhari kokh mein bachcha hai?
Batao behen… meri chinta door karo.”

🌸 Patni ka Uttar

Jaratkaru ne shant swar mein kaha—

“Bhaiya, maine Rishi se bacche ke baare mein poocha tha.
Unhone kaha: ‘Haan, hoga.’
Unhone kabhi jhooth nahi bola…
aur aise samay par to bilkul nahi.
Unhone mujhe aashwasan diya:
“Chinta mat karo, tumhare yahan ek beta hoga —
Suraj ki tarah tej.”
Isliye, bhaiya, dukhi mat ho.”

Yeh sun kar Vasuki ki saanson ka bojh halka ho gaya.
Woh khushi se bol utha—

“Achha hua! Be it so!”
Aur usne apni behen ko vardaan, dhan, aur pyaar se nawaza.

🌙 Astika Ka Janm

Samay ke saath
uske garbh ka tej badhta hi gaya—
jaise shukla paksh ka chand.

Aur ek din
usne ek sundar, divya roshni se chamakta beta janma.
Yeh bachcha
apne pita ke pitron aur saap-kul dono ke liye
umeed ka deepak ban kar aaya.

📚 Astika ka Balpan

Astika bachpan se hi asadharan tha:

Vedas aur shaastron ka gyaan liya

Rishi Cyavana se adhyayan kiya

Mann se pavitra

Buddhimaan aur vachan ka pakka

Sansaar ke moh se pare

Tapasvi aur vinamra

Astika naam bhi ajeeb tarike se pada—
kyunki jab uski maa garbhvati thi,
usne apne pati se poocha,
aur Rishi ne sirf ek shabd bola:
“Asthi — Haan, hai.”
Bas tab se sab usko Astika bulane lage.

🐍 Saapon ki Aasha

Astika dheere-dheere bada hua—
saap rajya ka laadla,
unki umeed,
unke bhavishya ka rakhwala.

Sabhi saapon ko lagta tha—

“Yahi hum sabko bachaayega.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.36
        with st.expander("Section 1.5.36"):
            text1 = """ 
🌿 Section XLIX — Janamejaya Apne Pitaji Ki Mrityu Ka Raaz Sunta Hai

Ek din Saunaka Rishi ne Sauti se poocha:

“Humein batao, Janamejaya ne apne mantriyon se kya-kya poochha tha apne pita Parikshit ki maut ke baare mein?”

📜 Sauti ne kaha

“Suno Brahmanon, main sab kuch bataata hoon jo raja ne poochha aur jo mantriyon ne jawab diya.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.36.jpg", text1, layout="side", image_position="left")
            text2 = """ 
👑 Janamejaya ka Prashna

Naujawan raja Janamejaya ne apne mantriyon se kaha:

“Kya aap jaante ho mere pita ke saath kya hua?
Unka anth kaise hua?
Main sab kuch sahi-sahi sunna chahta hoon.
Agar sun kar mujhe lage ki kisi ka bhala ho sakta hai, tab main kuch karunga.”

🕊️ Mantri ka Uttaar: Parikshit Kaun The?

Mantri ne shant swar me kaha:

**“Rajan, aapke pita Parikshit bahut dharmic aur dayalu the.
Unhone chaaron varnon—Brahmana, Kshatriya, Vaishya, Shudra—sabko nyay aur raksha di.

Koi unse nafrat nahi karta tha, aur woh bhi kisi se nafrat nahi rakhte the.
Vidhwavan, garibon, anathon—sabki dekhbhaal karte the.

Tej aur shaurya mein woh Somdev jaise lagte the.
Ve dhanurvidya Saradvat Rishi se seekh chuke the.

Govind (Shri Krishna) ke bhi priya the.
Aur Kuru vansh ke lagbhag samaapt hone par, Uttara ke garbh se paida hue the—
isliye unka naam Parikshit pada.”**

Mantri ne aage bataya:

**“Unhone 60 saal tak rajya ki raksha ki.
Sab unse pyaar karte the.
Aur jab unka deh-ant hua, pura raj shok mein doob gaya.

Uske baad, bachpan mein hi aapko raj-tilak diya gaya.
Aur tab se aap Kuru vansh ko sambhaal rahe hain.”**

🤔 Janamejaya aur Jankari Maangta Hai

Raja ne fir kaha:

“Hamare vansh mein koi raja aisa nahi hua jo praja ka bura chahe.
Par mujhe batayo—
mere pita jaise dharmic purush ka anth kaise hua?
Mujhe poori kahani sunao.”

🐍 Mantri Sachchai Batate Hain: Shraap Ki Kahani

Mantriyon ne sachchai bataai:

**“Rajan, aapke pita shikar ke bohot shaukeen the.
Ek din ve jungle gaye aur ek hiran ko baan se chot pahunchayi.
Hiran bhaag gaya aur unhe nahi mila.

Ve thak gaye, bhookhe ho gaye, aur bhaatak-te hue ek tapasvi ke paas pahunche.

Par woh Rishi maun-vrat par the.
Aapke pita baar-baar poochhte rahe, par Rishi chup rahe.

Thakaan, bhookh aur gusse se andhe ho kar
raja ne zameen par pada hua mara hua saanp
apne dhanush ki nok se uthaya
aur Rishi ke kandhe par rakh diya.”**

Mantri ne gahri saans lekar kaha:

“Rishi ne gussa nahi kiya, na kuch bola.
Ve bas maun-vrat mein baithe rahe.
Par baad mein unke bete Shringin ne—apne pita ka apmaan sun kar—
aapke pita ko shraap de diya
ki saat din baad Takshaka saap unhe marega.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.37
        with st.expander("Section 1.5.37"):
            text1 = """ 
🌿 Section L — Sringin Ka Shraap Aur Janamejaya Ka Pratigya

Sauti ne aage bataya:

Mantriyon ne Janamejaya se kaha:

🐍 Parikshit Wapas Rajdhani Laut Aaye

“Rajan, jab aapke pita Parikshit thak gaye the—bhookh, pyas aur gusse se bhar kar—
unhone us maun-dhari Rishi ke kandhe par mara hua saanp rakha
aur phir rajdhani laut aaye.”

Us Rishi ka ek beta tha—Sringin—
jo gaay ke garbh se paida hua tha,
bahut shaktishaali, tejasvi aur bohot hi gusse waala.

Har roz woh apne guru ko pranam karne jaata tha."""
            create_image_text_layout("attached_assets/chapter1/1.5.37.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Sringin Gusse Se Jal Uthta Hai

Ek din raat ko, Sringin ko uske saathi ne bataya:

“Tumhare pita Rishi ko bina kisi galti ke, raja Parikshit ne apmaanit kiya hai.
Unke kandhe par ek mara hua saanp rakh diya!”

Sringin ka chehra gusse se laal ho gaya.

Mantriyon ne Janamejaya se kaha:

“Rajan, tumhare pita ne jiska apmaan kiya tha,
woh Rishi bohot dharmic, shant, tapasvi, aur nirdosh the.
Unme na lalach tha, na irsha.
Woh sab praaniyon ke liye sharan tha.”

Aise Rishi ka apmaan sun kar
Sringin, jo toofan jaise gussail tha,
ne paani chhoo kar shraap diya:

“Suno sab! Mere shabdon ki shakti dekh lo!
Saat din ke andar–
saap-raja Takshaka
raja Parikshit ko apne zehre se jala kar maar dalega!”

Aur phir woh apne pita ke paas chala gaya.

🕊️ Rishi Samika Raja Ko Bachane Ki Koshish Karte Hain

Rishi Samika ne turant apna shishya Gaurmukha Janamejaya ke pita ke paas bheja.

Gaurmukha ne kaha:

“Rajan, meri baat suniyega.
Aapko mere guru ke bete ne shraap diya hai.
Saat din baad Takshaka aapko marega.
Savdhaan rahiye!”

Parikshit ne bahut savdhaani barati—
mantron wale Brahmanon ko bulaya,
vish-hara dawaaiyaan rakhi,
aur ek surakshit mahal mein chhup kar rehte rahe.

🐍🔥 Takshaka aur Kasyapa Ki Mulakaat

Saathve din, ek mahan Brahman Rishi Kasyapa unhe bachane aa rahe the.

Par raaste mein Takshaka unhe mil gaya
ek sadhu ke roop mein.

Takshaka ne poochha:

“Kahan jaa rahe ho, Rishi?”

Kasyapa bole:

“Raja Parikshit ko tum zehr dene wale ho.
Main unhe bachaane ja raha hoon.”

Takshaka hansa:

“Main Takshaka hoon!
Tum mujhe rok nahi sakte.
Mera zehr dekhna chahte ho?”

Usne ek bargad ka ped kaata—
aur ped turant bhasm ban gaya.

Kasyapa ne shant ho kar
apne vidya se
us ped ko fir se jeevit kar diya—
jaise kuch hua hi na ho.

Takshaka ghabra gaya,
par fir chalak ban kar bola:

“Aao, main tumhe raja se bhi zyada dhan deta hoon.
Tum wapas chale jao.”

Kasyapa ne dhan le liya
aur laut gaye.

🔥 Takshaka Parikshit Ko Maar Deta Hai

Uske baad Takshaka
apna roop badal kar
Raja Parikshit ke surakshit mahal mein ghus gaya
aur unhe zehr se jala kar maar dala.

Is tarah Janamejaya raaja ban gaye.

😡 Janamejaya Ka Krodh

Ye sab sun kar Janamejaya ro pade.

Unhone haath jod liye, saans tez ho gayi,
aankhon se aansu bahaakar bole:

**“Ab mujhe sab samajh aa gaya hai.
Takshaka ne mere pita ko maarne ke liye
Kasyapa ko rishwat di.

Galti Sringin ki nahi—
seedha dosh Takshaka par hai.

Main ab apne pita ka badla loonga.
Main Takshaka aur saap-vansh ko dandayunga!”**

Mantriyon ne kaha:

“Rajan, humne aapko saari baat bata di.
Aap jo uchit samjhein, wahi kariye.”

Janamejaya ne kathor swar me kaha:

“Ab der nahi hogi.
Takshaka ne yeh anyaay kiya hai—
aur main usey saja doonga.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.38
        with st.expander("Section 1.5.38"):
            text1 = """ 
🌿 Section LI — Janamejaya Ka Maha Sarp-Yagya

Sauti ne kaha:

King Janamejaya ne jab apna kathor sankalp sunaaya,
to unke mantriyon ne turant prashansa ki—
sabne kaha “Yeh theek hai, Maharaj!”"""
            create_image_text_layout("attached_assets/chapter1/1.5.38.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Janamejaya Ka Badle Ka Pratigya

Janamejaya—Parikshit ka veer putra—
ne apne purohit aur Ritwikon ko bula kar kaha:

“Main apne pita ka badla loonga.
Takshaka ne unhe zehr se jala dala.
Mujhe koi aisa yagya batao
jisme main Takshaka aur uske saathi saap
aag mein gira kar bhasma kar doon—
jaise usne mere pita ko jala diya tha.”

📜 Purohit Ka Uttar: Sarp-Satra Yagya

Mukhya purohit bole:

**“Rajan, ek mahaan yagya hota hai—
Sarp-Satra, yaani Saanpon ka Mahayagya.

Iska ullekh Puranon mein bhi hai.
Yeh devtaon dwara banaya gaya yagya hai.

Aur isse sirf aap jaisa raja hi kar sakta hai.”**

Yeh sun kar Janamejaya ko laga
ki jaise Takshaka abhi se aag mein jal raha ho.

🕯️ Yagya Ki Taiyariyaan

Raja ne kaha:

“Theek hai, taiyaari shuru karo.
Mujhe batao, kya kya chahiye.”

Ritwik—jo mantron aur Vedo mein nipun the—
ne shastron ke anusaar
ek vishaal yagya-vedi ki jagah mapni shuru ki.

Phir:

vedi ko keemti vastuon se sajaaya gaya,

dhan-dhaan rakha gaya,

aur adhik sankhya mein Brahmanon ko bulaya gaya.

Raja ko vidhi-purvak
yagya ke liye sthapit kiya gaya.

Sab kuch shubh-shubh chal raha tha…
lekin tabhi ek ashubh ghatna hui.

⚠️ Ek Rahasya Bhari Chitaavni

Vedi banate waqt
ek Suta—jo kala-mehar aur puranon ka gyani tha—
waha aaya.

Usne mitti ko dekha,
samay ko dekha,
aur bada gahla sanket diya:

“Rajan, jahan aur jis samay par
ye vedi ban rahi hai,
uske soochak batate hain
ki yagya poora nahi hoga.
Iska kaaran ek Brahmana banega.”

Janamejaya yeh sunkar ghabra gaye,
par sankalp mazboot tha.

Isliye unhone turant hukm diya:

“Aaj se bina meri ijazat
koi bhi vyakti mahal mein pravesh nahi karega.
Chaahe woh kaun ho.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.39
        with st.expander("Section 1.5.39"):
            text1 = """ 
🌿 Section LII — Sarp-Yagya Shuru Hota Hai

Sauti ne kaha:

Raja Janamejaya ka Sarp-Yagya
ab shastron ke anusaar shuru ho gaya.

🔥 Agni Mein Ghee, Aur Saapon Ke Naam

Yagya ke purohit—
jo apne-apne kaam mein bahut nipun the—
kale vastra pehne,
dhueṅ se unki aankhen laal ho chuki thi.

Woh Agni dev ke muh mein
shuddh ghee chadhaa rahe the,
mantron ke saath saanpon ke naam bolte jaa rahe the.

Unke mantra ka daman itna teekha tha
ki saare saanp dar se kaamp uthe."""
            create_image_text_layout("attached_assets/chapter1/1.5.39.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🐍🔥 Saanpon Ki Dukhad Haalat

Mantra ki shakti se
saare saanp apne aap kheech kar
aag ki aur girne lage.

Koi chillaa raha tha,
koi apne saathi ko bula raha tha—
lekin koi bach nahi pa raha tha.

Safed saanp,

kaale saanp,

neele saanp,

chhote, bade,

jawaan aur boodhe—

sab ek jaise
lapakte huye aag mein girte ja rahe the.

Kuch ek-do nahi,
laakhon saanp—
apne haath-pair jaise kho baithe—
ek ke baad ek
Agni dev ki laal-aag mein samate gaye.

⚔️ Vibhinn Aakar, Vibhinn Rang

Kuch saanp ghodon jitne lambe,
kuch haathiyon ke dandon jaise mote,
kuch pehadiyon ki jaise bade badan wale.

Koi iron-spike jaisi kothi-darakkh sharir banae,
koi zeher se bhara hua,
koi rang-biranga,
sab aag ki garaj se bhaay bhare.

Ma ke shraap se pareshaan,
sab ka ant ek hi tha—
Agni dev ki bhayanak laptoṅ mein girna."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.40
        with st.expander("Section 1.5.40"):
            text1 = """ 
🌿 Section LIII — Sarp-Yagya Ke Rishiyon Ki Suchi aur Vasuki ka Dard

Saunaka ne pucha:

“Sauti ji, Janamejaya ke Sarp-Yagya mein kaun-kaun se mahan Rishi Ritwik bane?
Kaun Sadasya bane?
Humein sab ka naam batao.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.40.jpg", text1, layout="side", image_position="left")
            text2 = """ 
📜 Yagya ke Ritwik aur Sadasya

Sauti ne kaha:

“Achha, suno. Main un sab ka naam bataata hoon—
jo is bade Sarp-Yagya mein shamil hue.”

Chandabhargava — woh Hotri bane; Cyavana vansh ke, bahut vidvaan.

Kautsa — Udgatri, jo Vedic geet gaate the.

Jaimini — Brahma-Ritwik.

Sarngarva aur Pingala — Adhvaryu.

Baaki bahut bade Rishi bhi wahan maujood the:

Vyasa apne putra aur shishyon ke saath,

Uddalaka,

Svetaketu,

Devala,

Narada,

Parvata,

Asita,

Vatsya,

Srutasravas,

Kohala, Devasarman, Maudgalya, Samasaurava…

Ye sab Sadasya bane—
yaani jo yagya ko dekh-rekh karte hain.

🔥🐍 Saanp Barf Ki Tarah Aag Mein Girne Lage

Jab Ritwik ghee daal kar mantra padhne lage,
to mantron ki shakti se
saare saanp hawa se gir-gir kar aag mein jaane lage.

Unka charbi aur majja pighal kar
aag mein behne laga—
jaise chhote-chhote nadiyaan.

Hawa meṅ ajeeb si badboo fail gayi,
aur saanpon ke rote-chilate awaaz
aasmaan tak pahunchne lage.

Koi bach nahi raha tha.

🐍➡️👑 Takshaka Bhaag Kar Indra Ke Paas

Jab Takshaka ko pata chala
ki Janamejaya usse jalane ke liye
ye maha-yagya kar raha hai,

to woh dar ke maare Indra ke mahal chala gaya.

Wahan jaakar bola:

“Indra dev, mujhe bachaiye!
Maine jo galti ki thi, uska parinaam aa gaya hai.”

Indra ne use shant karte hue kaha:

“Chinta mat kar, Takshaka.
Brahma ji tumhare liye shaant ho chuke hain.
Isliye tumhe yahaan koi khatra nahi.”

Takshaka phir Indra ke mahal mein
aaraam aur sukh se rehne laga.

😢🐍 Vasuki ka Dard — Samay aa gaya hai

Par Vasuki—
jo saare saanpon ka raja tha—
yagya ki dasha dekh kar
behad dukh se bhar gaya.

Usne dekha:

uski jaati khatam ho rahi hai,

har pal saanp gir kar jal rahe hain,

parivaar bikhar raha hai.

Dard se uska sharir kaanpne laga.

Usne apni behen ko bula kar kaha:

“Behen, mera mann tut raha hai.
Mujhe lagta hai aaj main bhi jal jaunga.
Yeh yagya hamaari vansh-nashaai ke liye hi hua hai.”

Phir usne yaad dilaya:

“Isi din ke liye maine tumhaari shaadi
Rishi Jaratkaru se karayi thi—
taaki ek aisa putra paida ho
jo humein bachaye.”

Aur Vasuki ne vinati ki:

“Jao, Astika ko bulao.
Wahi is yagya ko rok sakta hai.
Wahi hamara rakshak hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.41
        with st.expander("Section 1.5.41"):
            text1 = """ 
🌿 Section LIV — Astika Ka Vachan

Sauti ne kaha:

Jaratkaru nag-kanya ne apne bete Astika ko bula kar pyaar se kaha:

“Beta, ab woh waqt aa gaya hai.
Jis kaaran maine tumhaare pita se vivaah kiya tha—
woh kaam tumhe poora karna hoga.”

🤔 Astika Ka Sawal

Astika ne poocha:

“Maa, mama Vasuki ne aapko mere pita ko kyon diya tha?
Yeh sab mujhe sach-sach bataaiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.41.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🐍 Kadru ka Shraap — Saanpon ki Museebat

Jaratkaru ne shaant swar mein kaha:

“Beta, tumhara janam ek bade kaam ke liye hua hai.
Saanpon ki maa Kadru ne gusse mein apne hi bachchon ko shraap diya tha.”

Phir usne bataya:

Kadru ne saanpon se kaha tha:

“Uchchaihshravas ghode ko tum kaala keh do,
taaki Vinata humse haar jaaye.”

Par saanpon ne jhooth bolne se mana kar diya.
Kadru gusse se bhadak uthi:

“Tum sab Janamejaya ke Sarp-Yagya mein jal kar maroge!
Aur tum un paapi aatmaon ke lok mein jaaoge!”

Brahma ji ne, Kadru ke shabd sunkar,
“Be it so” kehkar shraap ko manzoor kar liya.

🐍🙏 Vasuki Ka Dar aur Brahma Ji Ka Vachan

Jab Vasuki ko shraap ka pata chala,
to woh devtaon ke paas bhaaga.

Jab amrit-manthan ho raha tha,
to Vasuki devtaon ke saath
Brahma ji ke paas gaya aur bola:

“Prabhu, humari jaati to khatam ho jaayegi!
Is shraap ko kaise roka jaaye?”

Brahma ji ne kaha:

“Ek Brahmana, Jaratkaru naam ki kanya se hi janm lega.
Wahi jaakar saanpon ko bachaayega.”

Vasuki ne tab apni behen (Jaratkaru) ka vivaah
tumhaare pita (Jaratkaru Rishi) se karaya.

Aur tum janme—Astika.

🔥🐍 Jaratkaru Maa Ki Vinati

Jaratkaru ne beta Astika se kaha:

**“Beta, ab hum sab jal rahe hain.
Takshaka to Indra ke paas chhupa hua hai,
baaki saare saanp aag mein gir rahe hain.
Yeh Sarp-Yagya hamaari vansh ko samaapt kar dega.

Tumhara janam humein bachane ke liye hua tha.
Ab humein tumhari zaroorat hai.”**

💬 Astika Ka Vachan

Astika ne maa aur mama Vasuki se kaha:

“Aap dono chinta mat karo.
Main aap sabko bachaaunga.
Mere shabd kabhi jhoothe nahi hote.”

Vasuki ro raha tha, darr se kaanp raha tha.
Usne kaha:

“Astika, mera mann bhaari hai.
Mujhe kuch dikhai nahi deta.
Hum sab khatam ho jayenge…”

Astika ne usse santvana di:

“Mama, main yeh aag thandi kar dunga.
Aapka dar main door karunga.
Aap bilkul mat ghabraaiye.”

🛕 Astika Chalta Hai Yagya Ki Or

Sauti ne kaha:

Astika apni poori taakat lekar
Janamejaya ke Sarp-Yagya ki taraf chal pada.

Wahan usne dekha:

Ek bade se yagya ka maidan,

Rishiyon ki anek pangatiyaan,

Aag ki tej laal lau,

Aur aas-paas chamakdhami se bhara sabha-sthal.

Par darwaanon par rakshak ne usse rok diya.

Astika ne vinamr bhasha mein
unhe prasann kiya,
aur phir yagya-mandap mein pravesh kiya.

Andar pahunchkar usne:

Raja Janamejaya ko,

Ritwikon ko,

Sadasyon ko,

Aur pavitra agni ko

maan-samman diya aur pranam kiya.

Uske aane se sab jagah ek shubh shanti si phail gayi."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.42
        with st.expander("Section 1.5.42"):
            text1 = """ 
🌿 Section LV — Astika Ki Prashansa

Astika ne yagya-mandap mein khade hokar
Raja Janamejaya aur sab Rishiyon ko
meethi aur samman-bhari awaaz mein kaha:

🌟 Astika ki Shubh-kaamnaayein

“Rajan, Prayag mein pehle Soma, Varuna aur Prajapati ne maha-yagya kiya tha.
Lekin aaj ka tumhara yagya bhi unse kam nahi hai.
Bhagwan tum sab par kripa banaye rakhein.”

Astika ne sabke liye fir shubh-aashirvaad diya:

“Indra ne sau yagya kiye the,
par tumhara ek yagya un dus hazaar yagyon ke barabar hai.
Tum sach-much mahaan raja ho.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.42.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Purane Mahaan Yagyon Se Tula

Astika ne kaha:

**“Yamraj ka yagya, Raja Rantidev ka yagya,
Raja Maya aur Vaishravana ke yagya—
ye sab duniya bhar mein prasiddh the.

Lekin Raja Parikshit ke putra,
tumhara yah yagya un sab jaisa hi tejasvi hai.”**

Woh aage bola:

“Jaise Yudhishthir ka dharm-yagya
swarg tak suna gaya tha,
waise hi tumhara yagya bhi yugon-tak yaad rahega.”

🕯️ Ritwik aur Rishiyon Ki Prashansa

Astika ne sabhi hotriyon, udgatriyon, aur brahmanon ko dekh kar kaha:

**“Yahan jo Rishiyan aur Ritwik baithe hain,
unka tej suraj jaisa hai.

Aur Ved-vyas ji jaisa Ritwik
teenon lokon mein aur koi nahi.
Unke shishya bhi,
jahan jaate hain, dharm phailate hain.”**

Usne agni ko pranam kiya:

“Agni dev tumhare havan ko khushi-khushi devtaon tak le ja rahe hain.
Yeh yagya sach-much pavitra hai.”

👑 Raja Janamejaya Ki Prashansa

Astika ne raja ki taraf dekhkar kaha:

**“Rajan, tum logon ki raksha karne mein
Varuna aur Yama jaisa nyay karte ho.
Indra jaisi shakti tumhari aankhon mein dikhti hai.

Tum Khatvanga, Dilipa, Yayati, Mandhatri jaise veer rajaon ki tarah ho.

Gyaan mein tum Valmiki aur Vasishtha jaise ho.
Tej mein Surya jaise.
Maryada mein Bhishma jaise.

Tumhari aisi prashansa teenon lokon mein ki ja sakti hai.”**

🙏 Ant mein Astika ka samman-pradaan

Astika ne sabko—

Raja ko,

Sadasyon ko,

Ritwik Rishiyon ko,

aur yajna-agni ko—

pranam kiya aur apni vinamr bhasha se sabko prasann kar diya.

🤔 Raja Ka Badalta Mann

Sauti batata hai:

Astika ki baaton se sab yagya-mandap mein
shubh sanket dikhne lage.

Tab Raja Janamejaya ne Rishiyon ki tarah,
gambhir aur soch-bhari awaaz mein kaha:

“Mujhe kuch vishesh dikh raha hai…
Yeh sab ka kya arth hai?”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.43
        with st.expander("Section 1.5.43"):
            text1 = """ 
🌿 Section LVI — Astika Ka Asli Mannorath

Yagya ke beech, Raja Janamejaya ne Astika ko dekhkar socha:

“Yeh ladka toh bilkul buddhe jaise samajhdaar baat karta hai.
Isse main koi vardaan dena chahta hoon.”

Raja ne Brahmanon se poocha:

“Kya main ise vardaan de sakta hoon?”

Brahmanon ne kaha:

“Rajan, Brahmana chaahe baccha ho ya bada, samman ke layak hota hai.
Par vartmaan mein ek kaam baaki hai—Takshak ko bulana.
Uske aane se pehle vardaan mat dena.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.43.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🔥 Takshaka Ko Kheenchte Hue

Raja ne fir bhi Astika se bola:

“Bolo, kya chahiye?”

Par Hotri ne yaad dilaya:

“Takshak abhi aaya nahi hai.”

Raja gusse mein bola:

“Toh mantra aur zor se padho!
Jab tak mera dushman Takshak aag mein na aa jaye,
yagya ka koi arth nahi.”

Ritwik ne kaha:

“Rajan, lagta hai Takshak abhi Indra ke paas chhupa baitha hai.
Dar ke maare woh wahan par hi hai.”

Ek purana Suta, Lohitaksha, ne bhi kaha:

“Indra ne Takshak ko bachane ka vaada kiya tha.
Woh keh raha hai—‘Mere saath raho, Agni tumhe nahi jala payega.’”

Yeh sunkar raja aur gussa ho gaya.

⚡ Indra Ka Prakat Hona

Mantron ki teevr ghoonjte hi,
Indra apni divya rath par aasmaan mein dikhayi diya,
devtaon, apsaraon aur badalon ke saath.

Takshak darr ke maare Indra ke uparna mein chip gaya.

Raja cheekha:

“Agar Takshak Indra ke saath chhupa hai,
toh Indra ko bhi aag mein kheench lo!”

Brahmanon ne mantron ka zor badhaya.
Agni ke bal se Indra ko Takshak dikhayi dene laga,
aur Indra ghabra kar
Takshak ko chhodkar wapas bhaag gaya.

Takshak ab akela, be-hosh sa,
aasmaan se seedha jalte yagya ki aag ki taraf ghirta ja raha tha.

🌟 Astika Ka Sahi Samay

Sab ne dekh liya ki Takshak girne hi wala hai.
Ritwik bole:

“Rajan, ab Astika ko vardaan dena chahiye.”

Janamejaya ne pyar se kaha:

“Bolo putra, kya chaho?
Chahe mushkil ho, main poora karoonga.”

Ritwik bole:

“Rajan, dekho! Takshak behosh ho kar neeche aa raha hai.
Mantra apna kaam kar rahe hain.”

Yahi woh pal tha jisme Astika ne shant awaaz mein kaha:

“Rajan, agar aap mujhe sach-much vardaan dena chahte ho,
toh iss nag-yagya ko yahin rok dijiye.
Aur koi saap aag mein na gire.”

⚖️ Raja Ka Sankat

Raja dukhi hokar bola:

“Nahi, nahi! Main sona, chandi, gau—jo chaho de doonga,
par yagya band mat karvao!”

Astika ne phir kaha:

“Mujhe kuch nahi chahiye.
Bas mere mama Vasuki aur mere saap-parivaar ko bachaa lijiye.”

Raja fir bola:

“Koi aur vardaan maango!”

Par Astika to adig tha:

“Mujhe sirf ek hi cheez chahiye—
yagya ruk jaye.”

Is par sab Sadasya ek saath bole:

“Rajan, Brahmana ko uska vardaan dijiye.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.44
        with st.expander("Section 1.5.44"):
            text1 = """ 
🌿 Section LVII — Kaun-Kaun Saap Aag Mein Gir Gaye

Saunaka ne Sauti se poocha:
“Suta-putra, batao kaun-kaun se naag is maha-nag-yagya mein aag mein gir gaye?”

Sauti bola:

“Rishi, itne saap gire ki ginana mushkil hai!
Hazaaron, lakhon, crore tak nag aag mein tapak pade.
Phir bhi, jitna mujhe yaad hai, main kuch bade naagon ke naam bata deta hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.5.44.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🐍 Vasuki vansh ke saap — bade, bhayankar, tezz zeher wale

Ye sab apni maa Kadru ke shraap se majboor ho kar seedhe aag mein gir pade:

Kotisa

Manasa

Purna

Cala

Pala

Halmaka

Picchala

Kaunapa

Cakra

Kalavega

Prakalana

Hiranyavahu

Carana

Kakshaka

Kaladantaka

Sauti kehta hai:
“Ye sab shaktishaali saap the, kuch neele, kuch laal, kuch safed.
Dhar-dhar kar aag mein gir rahe the.”

🐍 Takshaka vansh ke saap

Puccandaka

Mandalaka

Pindasektri

Ravenaka

Uchochikha

Charava

Bhangas

Vilvatejas

Virohana

Sili

Salakara

Muka

Sukumara

Pravepana

Mudgara

Sisuroman

Suroman

Mahahanu

🐍 Airavata vansh ke saap

Paravata

Parijata

Pandara

Harina

Krisa

Vihanga

Sarabha

Meda

Pramoda

Sauhatapana

🐍 Kauravya vansh ke saap

Eraka

Kundala

Veni

Veniskandha

Kumaraka

Vahuka

Sringavera

Dhurtaka

Pratara

Astaka

🐍 Dhritarashtra vansh ke saap — bada veer aur zehreela vansh

Sankukarna

Pitharaka

Kuthara

Sukhana

Shecaka

Purnangada

Purnamukha

Prahasa

Sakuni

Dari

Amahatha

Kumathaka

Sushena

Vyaya

Bhairava

Mundavedanga

Pisanga

Udraparaka

Rishabha

Vegavat

Pindaraka

Raktanga

Sarvasaranga

Samriddha

Patha

Vasaka

Varahaka

Viranaka

Sucitra

Citravegika

Parasara

Tarunaka

Maniskandha

Aruni

🐍 Anant sankhya saap aag mein gire

Sauti bolta hai:

“Ye toh sirf kuch mukhya naagon ke naam hain.
Baaki toh itne the ki unka hisaab hi nahi.
Kuch ke teen sir, kuch ke saat, kuch ke dus!
Kuch ek yojan lamba, kuch do yojan!
Bhoot-jasay, pahaad-jasay, aur agni-jasay zeher wale—
Sab shraap ke chalte girte gaye.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.5.45
        with st.expander("Section 1.5.45"):
            text1 = """ 
🌿 Section LVIII — Astika Ka Adbhut Kaam

Sauti bola:

“Ab Astika se judi ek aur ajeeb ghatna suno.”

Jab Raja Janamejaya Astika ko var dene hi wale the, tab Takshaka, jise Indra ne apne haath se chhod diya tha,
asman mein hi latka hua tha — na upar ja raha tha, na neeche gir raha tha!

Raja hairaan ho gaya.
Aag mein uska naam lekar mantra chadha rahe the, phir bhi Takshaka gir hi nahi raha tha."""
            create_image_text_layout("attached_assets/chapter1/1.5.45.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🕉 Saunaka ka prashna

Saunaka ne poocha:

“Suta, kya un Brahmano ke mantra kamzor ho gaye the?
Kyun Takshaka nahi gira?”

🐍 Sauti ka jawab — Astika ki teen baatein

Sauti bola:

“Takshaka behosh tha.
Indra se chhutkar neeche gir raha tha.
Tab Astika ne teen baar kaha:
‘Ruko… ruko… ruko.’
Aur bas — Takshaka hawa mein hi ruk gaya.”

Vo aise thama raha jaise koi aadmi aasman aur zameen ke beech latka diya gaya ho.

👑 Raja ka faisla

Sadasya baar-baar Raja se bole:

“Astika ka var de dijiye.”

Tab Raja ne kaha:

“Theek hai.
Jo Astika chahta hai wahi hoga.
Yagya band karo.
Saapon ki raksha ho.
Aur Astika ka var satya ho.”

Jaisi hi Raja ne maan liya,
aasman mein shubh awaaz gungunayee — sab khush ho gaye.

Is tarah Parikshit ke putra Janamejaya ka maha-sarp-yagya samapt hua.

💰 Raja ka daan aur khushi

Raja Janamejaya bahut khush hua.
Usne:

Ritwikon ko

Sadasyon ko

Saare upasthit logon ko

Hazaaron-dason ki dhan-rashi daan di.

Jo suta Lohitaksha ne pehle hi bata diya tha ki “yagya ek Brahman ki wajah se rukega,”
Raja ne use bhi bahut dhan diya.

Phir, poori maryada se,
Raja ne Astika ko vidha purvak vidha di aur kaha:

“Mere ashvamedh yagya mein zaroor Sadasya ban kar aana.”

Astika ne kaha “Avashya”
aur khushi-khushi ghar laut gaya.

Wahan jaakar apni maa aur mama ko sab bataya.

🐍 Saapon ki khushi aur Astika ka anokha var

Saap jo wahan the, sun kar bahut khush hue.
Unhone Astika se kaha:

“Batao beta, tumhare liye hum kya karein?
Tumne hum sabko bachaya hai.”

Astika bola:

“Jo bhi Brahman ya koi bhi aadmi
subah ya shaam
dhyaan se is katha ko padhe ya sune —
use kisi saap se kabhi dar na lage.”

Saap bole:

“Aisa hi hoga.
Jo Astika, Artiman aur Sunitha ke naam ko yaad kare — use hum kabhi nahi dasenge.”

Aur koi vyakti bole:

‘Main Jaratkaru-putra Astika ko yaad karta hoon,
jinhone saapon ko bachaaya.
Hey saap, mujhe mat dasko,
jao apne raste.’

Toh saap use nahi dasenge.

Sauti kehta hai:

“Jo saap aise bolne ke baad bhi kisi ko das lega —
uska phan 100 tukde ho jayega
jaise sinsha phal.”

🌟 Astika ka ant

Astika sabse santusht ho kar
apna kaam poora karke
isi apne punya se
samay aane par swarg chala gaya,
apne parivaar ko chhod kar.

🌿 Sauti ka samapan

“Jo bhi Astika ki yeh pavitra katha padhta-sunta hai—
use saapon ka dar nahi rehta.”

Sauti ne Saunaka se kaha:

“Jis tarah mere purvaj Pramati ne yeh katha Ruru ko sunayi thi,
maine bhi tumhe poori tarah waise hi suna di.
Ab tumhara jigyaasa shant ho jaye.”"""
            create_image_text_layout(text_content=text2, layout="full")


    # ============================
    # Chapter 1.6
    # ============================

    with st.expander("Chapter 1.6 – Adivansavatarana Parva (Origin of the Dynasties)"):

        with st.expander("Section 1.6.1"):
            text1 = """ 
Hinglish Kahani Version — Section LIX

Ek din Saunaka Rishi ne pyaar se kaha,
“Beta, tumne Bhrigu ji ke vansh se shuru hoti itni badi kahani sunayi.
Main tumse bahut khush hoon.
Par ab mera mann aur bhi sunna chahta hai.

O Suta-putra, mujhe woh purani kahani sunao jo Rishi Vyasa ne rachhi thi.
Woh sab sundar aur adbhut kisse jo bade yajna ke time,
jab Sadasya log apne kaam se free hote,
tab beech-beech mein sunaate the.
Main un sab ko poori tarah sunna chahta hoon.
Isliye mujhe woh kahani batao.”"""
            create_image_text_layout("attached_assets/chapter1/1.6.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Sauti ne vinamrta se jawab diya,
“Brahman log jab yajna ke kaam se free hote,
toh woh Vedas se judi bahut si baatein karte the.
Par Vyasa ji…
Vyasa ji ne ek bohot hi adbhut aur mahaan itihas sunaya—
Mahabharata.”

Saunaka ne fir prem se kaha,
“Wahi pavitra Mahabharata…
jo Pandavo ki kirti ko door-door tak failata hai,
aur jise Vyasa ji ne Janamejaya ki ichchha par
yajna ke baad poori tarah sunaya tha…
Main usse poori shraddha se sunna chahta hoon.

Yeh kahani ek gehre samundar jaise man se nikli hai,
Vyasa jaise mahaan yogi ke hriday se.
O Suta-putra, meri pyaas abhi nahi bujhi.
Mujhe sab kuch poora sunao.”

Is par Sauti muskuraya aur bola,
“Achha, Brahman!
Main ab tumhe Mahabharata ki kahani
bilkul shuruaat se sunaoonga.
Dhyan se suno.
Mujhe bhi yeh kahani sunate hue bahut anand hota hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.2"):
            text1 = """ 
Hinglish Kahani Version — Section LX

Sauti ne kahani aage badhate hue bataya:

Jab Janamejaya ka bada sa sarp-yagna chal raha tha,
tab yeh baat Rishi Krishna-Dvaipayana Vyasa ko pata chali.
Woh turant wahan aa gaye.

Vyasa ji, jo Pandavo ke dada the,
Yamuna ke beech ek chhoti si island par paida hue the—
Kali naam ki ek kanya se,
aur unke pitaji the Parasara Rishi.

Vyasa ji to janam se hi adbhut the.
Paida hote hi, unhone apni ichchha se apna sharir badha liya,
aur Vedas, unke saare ang, aur purani kathayein sab seekh liye."""
            create_image_text_layout("attached_assets/chapter1/1.6.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Unhone woh gyaan pa liya
jo tapasya, Veda-adhyayan, vrat, upvas ya yajna se bhi mushkil hota hai.
Aur wahi Vyasa ji, sabse pehle Vedas ko chaar hisson mein baante wale the.

Woh pavitra the, sachche the,
aur unhe puro-past ka gyaan apne antar-gyan se hota tha.
Unhi udaat karyaon ke saath unhone
Pandu, Dhritarashtra aur Vidura ka janm karvaya
taaki Shantanu vansh aage badh sake.

Vyasa ji apne shishyon ke saath,
jo sab Vedas mein nipun the,
yajna ke bade mandap mein pravesh kar gaye.

Wahan unhone dekha ki raja Janamejaya,
Indra ki tarah shaan se baitha hai—
uske aas-paas Sadasya log,
bahut se raja maharaja,
aur ritwik jo Brahma ji jaise gyaani the.

Raja Janamejaya ne Vyasa ji ko aate hi dekha
aur turant, bade prem se,
apne parivaar aur saathiyon ke saath unke paas daud padta gaya.

Sab Sadasyaon ki ijazat se
usne Vyasa ji ko suneheri asan diya—
jaise Indra ne kabhi Brihaspati ko diya tha.

Fir raja ne shastron ke anusaar
unki pooja ki.
Vyasa ji ko paani diya, Arghya diya,
aur gau-daan kiya.

Vyasa ji ne in sab ko swikar kiya
aur gaayon ko maarne se mana bhi kar diya.
Raja ne apne pardada ko pranam kiya
aur muskurate hue unki khairiyat puchhi.

Vyasa ji ne bhi pyaar se jawaab diya
aur sab Sadasyaon ko ashirwaad diya.

Thodi der baad,
Janamejaya ne haath jod kar Vyasa ji se poocha:

**“O Brahman! Aapne apni aankhon se
Kaurav aur Pandavo ke kaam dekhe hain.
Main unki puri kahani sunna chahta hoon.

Unmein itna bada jhagda kyon hua?
Kyon yeh mahan yudh hua jisme
aneka jeev mar gaye
aur mere dada-pardada sab ek-dusre ke saamne aa khade hue?

Please, mujhe sab kuch bilkul poora batayein.”**

Janamejaya ki baat sun kar
Vyasa ji ne apne shishya Vaisampayana ki taraf dekha
aur kaha:

“Jaisa maine tumhe sikhaya hai,
waise hi puri kahani raja ko suna do—
Kaurav aur Pandavo ke beech jo kuch hua, sab batao.”

Aur phir Vaisampayana Rishi
apne gurudev ki aagya par
puri kahani sunane lage—

Dushmani ka aarambh,
puri vansh ki katha,
aur kaise Kaurav aur Pandavo ka
ant ho gaya—
sab kuch.

Yahin se kahani ka narrator badal jaata hai—
ab sunayenge Vaisampayana,
aur sunenge Raja Janamejaya."""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.3"):
            text1 = """ 
🌿 Hinglish Kahani Version — Section LXI

Vaisampayana folded his hands,
aur sabse pehle apne gurudev Vyasa ji ko pranam kiya.
Sar dharti tak jhuk gaya,
aur mann mein poori shraddha thi.

Phir unhone sab Brahmano aur gyaani logon ko respect diya
aur bole:

“Rajan, main ab woh sab sunaoonga
jo maine Vyasa ji se khud suna hai.
Aap is Bharata katha ko sunne ke liye bilkul yogya hain.”

Unhone raja ko pyar se kaha:

“Suno rajan…
Kaurav aur Pandavon mein jhagda kyon hua?
Kyon unhe vanvaas bheja gaya?
Main sab bataunga.”"""
            create_image_text_layout("attached_assets/chapter1/1.6.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🌱 Pandavon ka bachpan aur Duryodhan ki jalan

Pita ke guzarne ke baad
Pandav apne ghar wapas aaye.
Thode hi dino mein
woh dhanurvidya aur yudh-kala mein bahut tez ho gaye.

Log unhe pasand karte the —
woh sundar, shaktishaali, aur buddhimaan the.

Ye dekh kar Kaurav,
khaskar Duryodhana,
andar-andar jalne lage.

Duryodhan, Karna, aur Mama Shakuni
milkar Pandavon ko tang karne lage
aur sochne lage ki unhe kaise desh-nikala diya jaaye.

🧪 Bhima ko zeher… par Bhima nahi mara

Ek din Duryodhana ne
Bhima ko khaane mein zeher de diya.

Par Bhima ka pet “bhediye jaisa” mazboot tha —
woh zeher hi pacha gaya!

Fir Duryodhan ne sote hue Bhima ko
Ganga kinare baandh kar
paani mein dhakka de diya.

Par jab Bhima jaaga,
usne rassi tod di
aur asaani se upar aa gaya.

Paani ke andar zehreele saanp bhi kaat gaye,
phir bhi Bhima ko kuch nahi hua.

🤝 Vidura — Pandavon ka chupchaap rakshak

Jab bhi Kaurav koi bura plan banate,
Vidura unhe rokne ki poori koshish karte.

Jaise devendra —
jo swargon ki raksha karte hain —
waise hi Vidura
Pandavon ko hamesha bachate rahe.

🔥 Lakshagriha ka khel

Jab Duryodhan har tareh se thak gaya,
toh usne mama Shakuni ke saath
ek khatarnak plan banaya:

Ek lakdi aur lak (jaisi wax) ka mahal banwao,
aur Pandavon ko wahan bhej do.
Woh dheere-dheere jal kar mar jayenge.

Dhritarashtra ne bhi anjaan ban kar
Pandavon ko Varanavat bhej diya.

Vidura ne chori-chhipe unhe
is khatre ki warning di
aur bachne ka tareeqa bataya.

Pandav wahan ek saal rahe.
Fir raat ko, chhipi hui surang se nikal gaye
aur poore mahal ko aag laga di,
jisme Purocana jal kar mar gaya.

🌲 Jungle ka safar, Rakshas, aur Hidimba

Jungle se guzarte hue
unki mulakaat ek rakshas se hui.

Bhima ne us rakshas ko hara diya,
aur uski behen Hidimba
Bhima se pyaar kar baithi.

Bhima aur Hidimba ka beta
Ghatotkacha wahi paida hua.

🌾 Ekachakra aur Rakshas Vaka

Pandav fir Ekachakra nagar gaye
aur Brahmachari ban kar ek Brahman ke ghar rahe.

Wahin Bhima ne
dusht Rakshas Vaka ko maara
aur saare nagar ko bachaya.

🌸 Draupadi swayamvar

Phir unhe pata chala
ki Panchal ki rajkumari Krishnaa (Draupadi)
swayamvar rakh rahi hain.

Pandav wahan gaye
aur Draupadi ko jeet kar
ghar le aaye.

Draupadi sabhi Pandavon ki
sanyukt patni bani.
Woh unke saath ek saal rahi.

🏞️ Khandavaprastha — Pandavon ka naya ghar

Jab sabko pata chala ki Pandav zinda hain,
woh Hastinapura wapas gaye.

Dhritarashtra aur Bhishma ne kaha:

“Jhagda mat badhao.
Tum log Khandavaprastha jao aur wahan raho.”

Pandav wahan chale gaye
aur apni shakti aur nyaay se
poori duniya mein apni prabhuta sthapit ki.

Bhima ne Poorv jeeta,
Arjun ne Uttar,
Nakula ne Paschim,
aur Sahadeva ne Dakshin.

🌟 Arjun ka vanvaas aur Subhadra vivah

Kisi baat par Yudhishthir ne
Arjun ko vanvaas bheja.

Arjun gyarah saal tak van mein raha.
Is dauran woh Dwaraka gaya
aur wahan uski shaadi hui
Vasudev ki behen Subhadra se.

🔥 Khandava-dahan aur Maya ka mahal

Arjun aur Krishna ne milkar
Agni ko Khandav van jalane mein madad ki.

Khush hokar Agni ne
Arjun ko diya:

Gandiva dhanush

Akshay baan तरकस

Garuda-dhwaj wala rath

Is aag mein Arjun ne
Asura Maya ko bachaya.

Maya ne shukriye mein
Pandavon ke liye
ek adbhut, chamakdar mahal banaya.

Duryodhan ne jab woh mahal dekha,
toh lalach se bhar gaya.
Usi lalach se
Shakuni ke saath dice-game racha.

Yudhishthir har gaye,
aur Pandavon ko
12 saal vanvaas + 1 saal agyatvas mila.

⚔️ Vapasi, jhagda, aur Mahayudh

14 saal baad jab Pandav wapas aaye
aur apna raj maanga,
toh Kauravon ne na keh diya.

Fir yudh hua —
bahut bada, vinashkari yudh.

Is yudh mein
Kaurav vansh ka ant ho gaya
aur Pandavon ko
apna raj phir mil gaya.

⭐ Vaisampayana ka ant

Vaisampayana ne kaha:

“Rajan, yeh hai Pandavon ki kahani.
Unhone kabhi buri bhaavna se kaam nahi kiya.
Unki satyata aur dharma ne hi
unhe jeet dilayi
aur Kauravon ki haar hui.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.4"):
            text1 = """ 
🌼 Hinglish Kahani Version — Section LXII

Raja Janamejaya ne pyaar se Vaisampayana se kaha:

“Hey acharya,
Aapne ab tak mujhe Mahabharata ki kahani bahut chhote roop mein sunayi hai.
Par mera mann abhi bhi utsuk hai.
Main usse poori tarah sunna chahta hoon.

Yeh itni chhoti baat nahi ho sakti
jis wajah se dharmic logon ne
apne hi logon ko maarna pada.

Pandav jaise shant, veer aur nyaay-premee log
Kauravo ki itni sataayi ko
shantipurn tareh se kyon saha?"""
            create_image_text_layout("attached_assets/chapter1/1.6.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Bhima jiske paas das hazaar haathiyon ki shakti thi—
woh apna gussa kyon rok gaya?

Draupadi, jo tapas se dushmano ko jala sakti thi,
usne Dhritarashtra ke putron ko
gusse ki drishti se kyon nahi jalaya?

Aur Bhima, Arjun, Nakul, Sahadev—
sab ko nuksaan pahuncha tha…
phir bhi woh Yudhishthir ke saath
us khatarnak juye ki aadat ko
kyon bardasht karte rahe?

Yudhishthir, jo dharma ka putra kaha jata tha,
woh itni kashton ko kyon seh raha tha?

Aur Arjun—
jiske rath ki dor Krishna pakadte the,
jiske teer ne dushmanon ki fauj ko dhool chata di—
woh itne saare dukh kyon saha raha tha?

Hey Brahman!
Kripya mujhe sab kuch bataiye.
Main poori kahani sunna chahta hoon.”

📚 Vaisampayana ka jawab

Vaisampayana ne dheere se muskurakar kaha:

“Rajan,
Yeh kahani bahut badi hai.
Aap sahi samay taiyyar kijiye,
main sab kuch shuruaat se sunaoonga.

Yeh kahani Vyasa ji ki rachna hai—
jiske mann ki shakti anant hai.
Unhone 1 lakh shlokon ka
pavitra Mahabharata rach diya.

Jo ise sunta hai,
ya sunata hai,
woh devataon jaisa punya paata hai.

Mahabharata Vedo ke samaan pavitra hai.
Isme dharma, artha, kama,
aur moksha—
sab ka gyaan hai.

Is kahani ko sunne se
manushya ke paap jal jaate hain,
jaise surya grahan ke baad
Rahu suraj ko chhod deta hai.”

🌟 Mahabharata sunne ke phal — bachchon ki kahani ki tarah mitha sa varnan

Vaisampayana ne kaha:

“Jo is kahani ko shraddha se sunta hai—

uska mann pavitra ho jaata hai,

uske paap door ho jaate hain,

ghar mein sukh aata hai,

bacche achhe aur vinamra bante hain,

aur har kaam mein safalta milti hai.

Ek raja agar yeh kahani sun le,
toh woh poori duniya par shasan kar sakta hai.

Ek grahastha sun le,
toh uske parivaar mein prem badhta hai.

Ek brahmachari sun le,
toh uski buddhi tej ho jaati hai.

Ek tapasvi sun le,
toh uska tap aur shuddh ho jaata hai.”

✨ Mahabharata — saari kahaniyon ki maan

“Vyasa ji ne teen saal tak
roz snan karke, tap karke,
yeh granth likha.

Isme devataon ki kathayein hain,
rishiyon ki kathayein hain,
Shiva-Parvati ka varnan hai,
Kartikeya ka janm hai,
aur gaayon aur Brahmanon ki mahima bhi.

Jo Mahabharata ka ek bhi shloka
Shraddha se sunata hai
ya sunta hai,
woh punya ka bada bhandar kama leta hai.

Jo pura Mahabharata sun le,
woh Vedo ka gyaata samjha jaata hai.”

🌈 Sabse bada rahasya

Ant mein Vaisampayana bole:

“Rajan,
Is Mahabharata mein jo kuch hai,
woh kisi aur granth mein nahi milta.

Aur jo isme nahi hai—
woh duniya mein kahin nahi mil sakta.

Ab main poori kahani
aapke saamne recite karne jaa raha hoon.
Dhyan se suniye,
yeh kathaa punya-dene wali hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.5"):
            text1 = """ 
🌳 Hinglish Kahani — Section LXIII

Vaisampayana ne shuru kiya, dheere aur pyar se:

Ek raja tha — Uparicara, jise doosre log Vasu bhi bulate the.
Woh bahut dharmik tha. Par shikar ka bhi shauk tha.
Ek din usne Chedi rajya jeet liya. Phir thoda samay baad usne shastra chhod diye.
Woh ekant mein jaakar kathor tapasya karne laga.

Devatayein sochne lagi ki shayad usne devtaon ka sthan paane ki ichcha kar li.
Tab Indra aur devta uske paas aaye. Unhone pyar se samjhaya:
“Hey raja, dharma ki raksha karo. Dharti par dharma jab safe rahega, tabhi sansaar accha chalega.”"""
            create_image_text_layout("attached_assets/chapter1/1.6.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
Indra ne use kuch vardaan diye.
Usne raja ko ek kristal ki vahan (car) di, jo hawaa mein udti thi.
Ek amartulya haar di jo yudh mein use nukhsaan se bachata.
Aur ek bamboo pole di, jise log Indra ki puja ke liye khada karte.

Vasu ne woh sab sweekar kiya.
Usne Indra ki puja ki aur desh ko nyay se chalaya.
Uske paanch bahadur putr hue. Har ek ne apna raajya basaya.
Ek ka naam Vrihadratha, ek Pratyagraha, ek Kusamva (Manivahana), aur do aur — Mavella aur Yadu.

Raja Vasu jab apni crystal vahan par aasman mein chala,
tab usne ek pahaad Kolahala ko usay nadi Suktimati se pareshan karte dekha.
Usne pahaad ko thokar maari. Nadi azad ho gayi.
Kolahala se janme do bachche mile—ek ladka aur ek ladki.
Vasu ne ladke ko apnaya. Uska naam Matsya pada.

Ladki ko Satyavati kaha gaya.
Woh machhli jaise smell karti thi kyunki woh ek Apsara Adrika ki jaati mein paida hui thi.
Satyavati ko machhli se paida hone ka kissa bada alaukik tha.

Phir ek mahaan rishi Parasara ne Satyavati ko dekha.
Woh uski saundarya se prabhavit hua. Parasara ne usse kahaa, aur ek jadu ki megh bana di,
jisne sabko andhera dikhaya. Satyavati ne Parasara se ek var maa ngi: uska badan sugandhit ho.
Parasara ne vardaan diya. Satyavati phir Gandhavati / Yojanagandha ke naam se mashhoor hui.

Aur ussi din, Yamuna ke ek island par, Satyavati ne ek beta paida kiya.
Us bachche ka naam tha Dvaipayana (island-born).
Wahi Vyasa bana — jo baad mein Vedas ko vyavasthit karega.
Vyasa ne Vedas ko chaar bhaagon mein baanta aur Mahabharata likha.

Vyasa ne apne guno se kuch shishyon ko Sikhaya — Sumanta, Jaimini, Paila, Suka aur Vaisampayana.
Inhi se Mahabharata alag-alag roop mein duniya tak pahucha.

Phir bahut saare mahan janam hue:

Bhishma — Ganga aur Santanu se; bahut balwaan.

Ek rishi Animandavya ko zaldi saja mili. Usne Dharma pe shikayat ki. Isliye Dharma ne janm liya Vidura ke roop mein (Sudra jaati mein) — par Vidura bilkul nirdosh aur dharmik tha.

Kunti (Suta jaati ka janm) se ek putra Surya ke dwara paida hua — us par natural mail (armor) tha.

Vishnu ka avataar bhi hua — jise log Krishna jaante hain (Devaki aur Vasudeva ke dwara).

Aur aage kayi veer hue:

Drona (pot-born) — Rishi Bharadvaja ki seed se.

Kripi aur Kripa — jo tej aur yoddha the.

Dhrishtadyumna — agni se janma hua, Drona ke vinash ke liye paida.

Draupadi (Krishnaa) — agnikund se nikli, sundar aur sashakt.

Sakuni (Suvala ka putra) aur Gandhari — jisse Duryodhana hua.

Dhritarashtra aur Pandu — Vicitravirya ke vanaspati se janme.

Vyasa se hi Vidura bhi janma hua (Sudra roop mein, par atyant guni).
Pandu ke do patniyon se paanch putr — Yudhishthira, Bhima, Arjuna, Nakula, Sahadeva — yeh paanch Pandav hue.
Unke janm alag-alag devtaon ke vardaan se hue: Dharma, Vayu, Indra, aur Ashvin yugal.

Dhritarashtra ko sau putr hue — jisme Duryodhana aage aaya.
Arjun aur Subhadra ka beta Abhimanyu bana.
Pandavon ke bachche bhi hue — jaise Pritivindhya, Sutasoma, Srutakirti, Satanika, Srutasena aur Ghatotkacha (Bhima ka beta, Hidimba se).
Sikhandin bhi paida hua — jo pehle ladki (Sikhandini) tha aur baad mein male bana.

Ant mein Vaisampayana ne kaha:
“In us bade yudh me hazaaron aur hazaaron raja lade.
Sabka naam bataana mushkil hai. Maine khaas mahanon ke naam bataaye hain jo is kahani me aage aaye.”"""
            create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.6.6"):
            text1 = """ 
🌱 Hinglish Kahani — Section LXIV

Raja Janamejaya ne puchha,
“Hey Brahmana, tumne jo kuch bataya, bahut accha hai.
Par mujhe aur sunaao.
Un hazaaron rajaon ki kahani poori batao.
Aur yeh bhi batao ki woh maha-rathas (bahut balwaan yoddha) kyon paida hue?”

Vaisampayana ne haath jodkar bola:
“Rajan, jo tum puch rahe ho, woh bahut gehra raaz hai.
Main phir bhi batata hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.6.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
🕊️ Jab dharma phir se strong hua

Ek rishi Parasurama ne jab 21 baar kshatriyon ka vinash kar diya,
duniya mein kshatriya kam reh gaye.
Tab kshatriya mahilayein bachchon ki tamanna lekar
Brahmano ke paas aane lagi.
Brahmanas bhi sirf samay par, maryada se, unke saath milte.

Is tarah se naye kshatriya janme.
Nayi peedhi shakti-shali aur dharmik bani.
Dharma wapas jagmagaya.
Khet hal chalne lage.
Gau palan theek hua.
Sab log apna kartavya nibhaane lage.
Dharma phir mazboot ho gaya.

😨 Jab Asur aaye — dharti dukhi hui

Par phir kuch bura hua.
Asur (bure shaktis) zyada paida hone lage.
Kuch asur rajaon ki lineon mein aaye.
Woh garvile, takatwar aur anyaay karne wale the.
Woh brahmanon aur kshatriyon ko dabane lage.
Zameen dukhi hui.
Ped paudhe bhi pareshan ho gaye.
Pranion aur manushyon par dabav badhne laga.

Dharti ne sahara maanga.
Woh Brahman, sabka karta, ke paas gayi.
Brahman ne suna aur samjha.
Phir usne sab devtaon ko kaha:
“Tum sab dharti par janm lo. Asuron se ladho. Dharati ko bachao.”

🌟 Devta aate hain — yudh ki taiyari

Sab devtaon ne manaa.
Indra ne Narayana (Hari) se kaha,
“Bhagwan, kripya janm lo aur asuron se sangharsh karo.”
Narayana ne maan liya.
Is tareh devta aur pavitra jaatiyan dharti par aayi.
Yahi wajah thi ki maha-rathas aur mahapurush zameen par utare.
Takht, yudh aur dharma ka khel shuru hua.

Vaisampayana ne ant mein kaha:
“Yeh sab ghatnayein bahut purani aur gahri hain.
Isi karan se duniya mein bade bade yoddha paida hue.
Main aage aur bhi kisse sunaunga, raja.”"""
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

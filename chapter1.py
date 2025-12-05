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
        with st.expander("Section 1.2.12"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.12.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.13"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.13.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.14"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.14.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.15"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.15.jpg", text1, layout="side", image_position="left")

            text2 = """ """
            create_image_text_layout(text_content=text2, layout="full")
                # Section 1.2.1
        with st.expander("Section 1.2.16"):
            text1 = """ """
            create_image_text_layout("attached_assets/chapter1/1.2.16.jpg", text1, layout="side", image_position="left")

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

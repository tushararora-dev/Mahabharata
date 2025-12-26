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
            text1 = """ 
            Vaisampayana bole:

“Us samay Indra ne Narayana se salah ki.
Baat yeh thi ki devta apne-apne ansh ke saath
swarg se dharti par avtar lein.

Sab devlok ke vaasiyon ko aadesh dekar
Indra wapas Narayana ke dham se laut aaye.
Aur dheere-dheere
sab devta dharti par janam lene lage—
Asuron ka naash karne ke liye
aur teenon lokon ke bhale ke liye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌟 Devta dharti par janam lete hain

“Hey raja Janamejaya,
devta apni marzi se
Brahmarshiyon aur Rajarshiyon ke vanshon mein
janam lene lage.

Unhone Danav, Rakshas, Gandharva, Naag
aur anya dusht jeevon ka sanhaar kiya.

Itni shakti unmein thi
ki bachpan mein bhi
koi Asur unhe maar nahi paaya.”

👑 Janamejaya ka sawaal

Janamejaya bole:

“Main shuruaat se sunna chahta hoon.
Devta, Danav, Gandharva, Apsara,
Manav, Yaksha aur Rakshas—
sabke janm ki kahani.
Kripya sab kuch batao.”

📜 Srishti ka aarambh

Vaisampayana ne kaha:

“Main Brahma ko pranam karke
sab kuch bataata hoon.

Brahma ke chhe maanas putra the—
Marichi, Atri, Angiras, Pulastya, Pulaha, Kratu.

Marichi ke putra the Kashyapa.
Aur Kashyapa se hi
bahut si prajaon ka janm hua.”

👩‍👧 Daksha ki putriyan

“Daksha Prajapati ki
13 putriyan thi:

Aditi, Diti, Danu, Kala, Danayu, Sinhika,
Krodha, Pradha, Visva, Vinata, Kapila, Muni, Kadru.

Inke vansh se
anaginat prani paida hue.”

☀️ Aditi ke putra — Adityas

“Aditi se 12 Aditya paida hue—
yeh hi vishv ke palak hain:

Dhatri, Mitra, Aryaman, Indra (Sakra), Varuna,
Ansha, Bhaga, Vivasvat (Surya), Usha, Savitri,
Tvashtri aur Vishnu.

In sab mein
Vishnu sabse shreshth the.”

👹 Diti aur Danav vansh

“Diti ka putra tha Hiranyakashipu.
Uske paanch putra hue—
sabse bada Prahlada tha.

Prahlada ke putron mein
Virochana hua.
Virochana ka putra tha Bali.
Aur Bali ka putra Bana (Vana)—
jo Rudra ka bhakt tha.”

🌑 Danu ke putra

“Danu ke 40 putra hue—
jaise Viprachitti, Namuchi, Kesi, Vrishaparva,
Svarbhanu aur bahut se aur.

Inke vansh mein
anaginat Danav hue.
Unki ginti karna mushkil hai.”

🌘 Rahu aur anya

“Sinhika se paida hua
Rahu—
jo Surya aur Chandra ko grahan lagata hai.

Kala ke putra
Yamraj jaise bhayankar the.

Shukra Asuron ke guru the.
Unke bhi putra hue
jo Asuron ke purohit bane.”

🐦 Garuda aur Naag

“Vinata ke putra the—
Garuda aur Aruna.

Kadru ke putra hue—
Shesha (Ananta), Vasuki, Takshaka
aur anya Naag.”

🎶 Gandharva aur Apsara

“Pradha se
bahut se Gandharva paida hue.

Aur usi se
sundar Apsaraen bhi paida hui—
Tilottama, Rambha, Menaka,
Alambusha jaise naam prasiddh hue.”

🌍 Srishti ka saar

Vaisampayana bole:

“Is prakaar
devta, asur, gandharva, apsara,
naag, pakshi, gaay, brahman—
sabka janm hua.

Yeh kahani
pavitra hai,
jeevan badhaati hai,
aur mann ko shuddh karti hai.

Jo is srishti-katha ko
shraddha se sunta ya padhata hai,
use santaan, yash aur sukh milta hai.
Aur ant mein
uttam lokon ko prapt karta hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.2
        with st.expander("Section 1.7.2"):
            text1 = """ 
            Vaisampayana bole:

“Raja Janamejaya,
tumne srishti ka raaz poocha hai.
Main tumhe dheere-dheere
sab bataata hoon.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔱 Rudra aur Rishiyon ki utpatti

“Brahma ji ke
chhe maanas putra the—
Marichi, Atri, Angiras, Pulastya, Pulaha, Kratu.

Ek aur mahaan tha—
Sthanu.
Uske 11 putra hue—
yeh hi 11 Rudra kehlaye.
Ye sab shaktishaali the.
Aur shatruon ko nasht karne wale the.”

📿 Rishiyon ke vansh

“Angiras ke teen putra hue—
Brihaspati, Utathya, Samvarta.

Atri ke putra bahut zyada the.
Sab Vedo ke gyaani the.
Aur mann se shaant.”

“Pulastya ke vansh se
Rakshas, Vanar, Yaksha, Kinnar paida hue.”

“Pulaha ke vansh se
sher, baagh, bhalu, bhediye aur
kuch adbhut prani aaye.”

“Kratu ke putra the
Valikhilya Rishi—
jo Surya dev ke saathi bane.”

👩‍👧 Daksha aur uski putriyan

“Daksha Prajapati
Brahma ji ke anguthe se paida hue.
Unki patni bhi Brahma ji se hi utpann hui.

Daksha ki 50 sundar putriyan thi.
Putra na hone ke kaaran
unhone putriyon ko
putrika bana diya.”

Unhone putriyon ka vivaah kiya:

10 Dharma ko

27 Chandra (Moon) ko

13 Kashyapa ko

⚖️ Dharma aur uski patniyan

“Dharma ki 10 patniyan thi:
Kirti, Lakshmi, Dhriti, Medha,
Pushti, Shraddha, Kriya,
Buddhi, Lajja, Mali.

Inse hi
dharm, gyaan aur maryada
duniya mein faili.”

🌙 Chandra aur Nakshatra

“Chandra ki 27 patniyan thi.
Ye hi Nakshatra bani.
Samay aur gati
inke kaaran chalti hai.”

🌟 Vasus ka janm

“Brahma ji ke putra Manu hue.
Manu ke vansh se
8 Vasu paida hue:

Dhara, Dhruva, Soma, Aha,
Anila, Anala, Pratyusha, Prabhasa.

Inse hi
kaal, agni, hawa, prakash
jaise tattva bane.”

🔥 Kartikeya aur Vishwakarma

“Agni ke putra hue Kartikeya.
Unhe Krittikaon ne pala,
isliye naam pada Kartikeya.

Prabhasa Vasu ki patni se
paida hue Vishwakarma—
jo devtaon ke engineer bane.
Sab shilp, rath aur nagar
unhone banaye.”

🌸 Dharma ke putra

“Dharma ke teen putra hue—
Sama (Shanti)
Kama (Ichchha)
Harsha (Anand)

Inhi par duniya tiki hui hai.”

☀️ Aditi aur Adityas

“Aditi ke 12 putra hue—
sab Aditya kehlaye.
In sab mein
Vishnu sabse shreshth the.

Inhi ko milkar
33 Devta kaha jaata hai.”

🐦 Garuda, Naag aur anya prani

“Vinata ke putra hue—
Garuda aur Aruna.

Kadru se paida hue—
Shesha, Vasuki, Takshaka
jaise Naag.”

🌺 Apsara, Gandharva aur pashu

“Pradha se paida hui
sundar Apsaraen—
Rambha, Tilottama, Menaka.

Aur Gandharva bhi.”

“Krodha ki putriyon se
janwar paida hue—
hiran, baagh, sher, haathi,
bandar, ghode.”

“Syeni se paida hue—
Sampati aur Jatayu.”

⚫ Adharma ka janm

“Jab bhookh badhi
aur prani ek-doosre ko khaane lage,
tab Adharma (Paap) paida hua.

Uski patni Nirriti se
Rakshas hue.

Uske putra hue—
Bhay, Mahabhay aur Mrityu.”

🌍 Srishti ka saar

Vaisampayana bole:

“Raja Janamejaya,
maine tumhe
devta, asur, manav, pashu, pakshi
sabki utpatti bata di.

Jo is katha ko
shraddha se sunta hai,
uske paap dhul jaate hain.
Use gyaan milta hai.
Aur ant mein
uttam gati milti hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.3
        with st.expander("Section 1.7.3"):
            text1 = """ 
            Raja Janamejaya bole:
“Gurudev,
mujhe poori kahani sunni hai.
Devta kaise insaan bane?
Asur, Gandharva, Rakshas kaise janme?
Aur phir unhone kya-kya kaam kiya?”"""
            create_image_text_layout("attached_assets/chapter1/1.7.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            📜 Vaisampayana ki kahani shuru hoti hai

Vaisampayana bole:
“Raja, dhyaan se suno.
Yeh kahani bahut gehri hai.
Par main ise seedhi aur sachchi bhaasha mein bataunga.”

👑 Asur jo Raja bane

“Sabse pehle ek mahaan Danava Viprachitti tha.
Wahi dharti par Jarasandha bana.
Bahut shaktishaali raja.”

“Hiranyakashipu
dharti par Shishupala bana.
Gusse aur ghamand se bhara.”

“Prahlad ka bhai Samhlada
dharti par Shalya bana.”

“Anuhlada bana Dhrishtaketu.
Sivi bana Druma.
Vashkala bana Bhagadatta.”

“Bahut saare Asur
alag-alag rajyon ke raja bane.
Koi Kekaya ka raja bana,
koi Magadh ka,
koi Kalinga ka.”

💡 Seekh:
Shakti hone ka matlab
dharm hona zaroori nahi.
Shakti bina dharm ke
vinash laati hai.

⚔️ Kansa aur anya mahaan yoddha

“Ek bhayanak Asur tha Kalanemi.
Wahi dharti par Kansa bana.
Krishna ka shatru.”

“Drona koi normal manushya nahi tha.
Woh Devguru Brihaspati ka ansh tha.
Isliye mahaan dhanurdhar bana.”

“Uska beta Ashwatthama
Mahadev, Yama, Krodh aur Kaam ka ansh tha.
Isliye uska gussa bahut bhayanak tha.”

🌊 Ganga ke putra – Vasus

“Ganga aur Shantanu se
8 Vasu paida hue.”

“Sabse chhota tha Bhishma.
Gyaan mein mahaan.
Shastra aur shastra dono mein expert.”

💡 Seekh:
Bal se zyada
niyam aur pratigya
insaan ko mahaan banati hai.

🧠 Vidura, Pandu aur Dhritarashtra

“Vidura dharm ka ansh tha.
Isliye sabse buddhimaan aur nyay-priya.”

“Dhritarashtra andha hua
maa ki galti aur rishi ke shraap se.”

“Pandu pavitrata aur sachchai ka roop tha.”

🌑 Kali ka ansh – Duryodhana

“Duryodhana
Kali yug ke ansh se paida hua.
Isliye uske mann mein
jalan aur ahankaar bhara tha.”

“Uske 100 bhai the.
Sab Rakshasi pravritti ke.
Bas ek alag tha—Yuyutsu.”

🌞 Pandav kaun the?

“Raja, yaad rakho:

Yudhishthira = Dharma ka ansh

Bhima = Vayu ka ansh

Arjuna = Indra ka ansh

Nakula & Sahadeva = Ashwini Kumar ke ansh”

“Abhimanyu
Chandra dev ke putra Varchas ka ansh tha.
Isliye itna veer tha.”

💡 Seekh:
Achha janm nahi,
achha kartavya
insaan ko mahaan banata hai.

🌀 Chakravyuh aur Abhimanyu

“Chandra dev ne kaha:
‘Mera putra sirf 16 saal dharti par rahega.’

Usne Chakravyuh tod diya.
Par bahar nikalna nahi jaanta tha.
Phir bhi bina dare
veer gati ko praapt hua.”

💡 Seekh:
Veerta ka matlab jeetna nahi,
kartavya nibhaana hota hai.

🔥 Draupadi aur anya deviyaan

“Draupadi
Indrani (Sachi) ka ansh thi.
Sundar, tejasvi aur pavitra.”

“Kunti aur Madri
Siddhi aur Dhriti ka roop thi.”

🌞 Karna ki kahani

“Kunti ne mantra se
Surya dev ko bulaya.
Usse Karna paida hua.”

“Dar ke kaaran
usne Karna ko nadi mein chhod diya.”

“Radha aur uske pati ne
use paala.”

“Karna ke paas
janm se kavach aur kundal the.”

“Indra ne brahman ban kar
woh daan maang liya.
Karna ne bina soche
daan kar diya.”

💡 Seekh:
Sachcha daan
jaan kar bhi diya jaata hai.

🌸 Krishna, Balram aur Rukmini

“Krishna = Narayan ka poora roop
Balram = Sheshnaag ka ansh”

“Rukmini
Mahalakshmi ka roop thi.”

“16,000 raniyan
Apsaraon ke ansh thi.”

🌍 Ant mein sandesh

Vaisampayana bole:
“Raja Janamejaya,
maine tumhe bataya
kaun devta tha,
kaun asur,
aur kaun dharm ke paksh mein tha.”

“Jo is katha ko
shaant mann se sunta hai,
woh dukh mein bhi
kabhi toot-ta nahi.”

✨ Yahin Section LXVII samaapt hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.4
        with st.expander("Section 1.7.4"):
            text1 = """ 
            Raja Janamejaya bole:
“Gurudev,
maine devtaon, asuron aur unke avatar ki kahani sun li.
Ab main Kuru vansh ki kahani
bilkul shuru se sunna chahta hoon.
Sab rishiyon ke saamne
aap ise bataiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            📜 Vaisampayana bolte hain

Vaisampayana bole:
“Rajkumaar Janamejaya,
dhyaan se suno.
Main tumhe Kuru vansh ki jad batata hoon.”

👑 Raja Dushyanta – Kuru vansh ke aadi purush

“Kuru vansh ki shuruaat hui
Raja Dushyanta se.
Woh bahut shaktishaali raja the.”

“Unka raaj
chaaron samudron tak phaila hua tha.
Chaaron dishaayein
unke adheen thi.”

“Samudron ke beech ke desh bhi
unke niyantran mein the.
Yahaan tak ki
Mlechha desh bhi
unke adhikaar mein aate the.”

🌾 Sone ka yug jaisa raaj

“Dushyanta ke raaj mein
koi paap nahi karta tha.
Koi jaati-bhed nahi tha.”

“Kheti karni nahi padti thi,
zameen khud hi fasal deti thi.”

“Khadaan khodne ki zarurat nahi thi,
dharti upar hi upar
dhan ugal deti thi.”

“Koi chor ka darr nahi.
Koi bhookh ka darr nahi.
Koi bimari ka darr nahi.”

💡 Seekh:
Jab raja dharm se raaj karta hai,
toh praja bina darr ke jeeti hai.

🕊️ Dharm aur sukh ka raaj

“Chaaron varna
apna-apna kartavya
khushi se karte the.”

“Koi bhi dharm ka kaam
lalach se nahi karta tha.”

“Sab log
apne raja par bharosa karte the.
Isliye mann mein koi bhay nahi tha.”

“Indra dev
samay par baarish karte the.
Fasal rasbhari hoti thi.”

“Dharti par
dhan, pashu aur sampatti
bharpoor thi.”

“Brahman
hamesha sach bolte the
aur apna dharm nibhate the.”

💪 Raja Dushyanta ka bal aur gun

“Raja Dushyanta
jawaan aur veer the.”

“Unka sharir
vajra jaisa majboot tha.”

“Woh chaahen toh
Mandar parvat ko bhi
baahon par utha sakte the.”

“Gada yuddh ke
chaaron tareeke
unhe aate the.”

“Talwar, dhanush, bhala—
har shastra mein nipun the.”

“Haathi aur ghode
bahut achhe se chalate the.”

🌞 Raja ke gun

“Shakti mein
woh Vishnu jaise the.”

“Tej mein
Surya jaise chamakte the.”

“Gambhirata mein
samudra jaise the.”

“Dhairya mein
dharti jaise shaant the.”

“Isliye
praja unse prem karti thi.”

“Woh apni praja par
dharm ke saath
raaj karte the.”

✨ Yahin Section LXVIII samaapt hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.5
        with st.expander("Section 1.7.5"):
            text1 = """ 
            👑 Janamejaya ki prarthana

Raja Janamejaya bole:
“Gurudev,
ab main Maharaj Bharata ke janm aur jeevan ke baare mein sunna chahta hoon.
Saath hi mujhe Shakuntala ka janm aur
yeh bhi batayiye ki
veer Raja Dushyanta ne unhe kaise paaya.”

“Hey satya ke gyaata,
mujhe sab kuch poori tarah bataiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            📜 Vaisampayana kahani shuru karte hain

Vaisampayana bole:
“Rajkumaar, dhyaan se suno.
Yeh kahani hai
veer Raja Dushyanta ki.”

🏹 Raja Dushyanta ka van-gaman

“Ek samay,
bahut shaktishaali Raja Dushyanta
shikaar ke liye
van ki ore nikle.”

“Unke saath
bahut badi sena thi—
haathi, ghode, rath aur paidal sainik.”

“Talwaron, bhallon, gada aur dand ke saath
veer yoddha
raja ke chaaron taraf the.”

🔊 Sena ka ghosh

“Jaise-jaise raja aage badhte gaye,
sankh-naad, nagade, rath ke pahiye,
haathiyon ki cheekh,
ghodon ki hin-hinahat—
sab milkar
bhayanak shor paida kar rahe the.”

“Puri dharti
us shabd se goonj uthi.”

🌸 Nagar ki striyon ka drishya

“Shahar ki sundar striyan
mahalon ki chhat se
raja ko dekh rahi thi.”

“Unhe dekhkar woh boli:
‘Yeh toh Indra jaise lagte hain!
Yeh toh shatruon ke haathiyon ko bhi
peeche dhakel dete hain!’”

“Prem aur shraddha se
unhone raja par
phool barsaaye.”

🙏 Aashirvaad ke saath prasthaan

“Brahman rishiyon ne
raja ko aashirvaad diya.”

“Khushi ke saath
Raja Dushyanta
van ki ore badhe,
hiranon ke shikaar ke liye utsuk.”

“Kuch door tak
nagrik unke saath chale,
phir raja ke aadesh par
waapas laut gaye.”

🌲 Van ka varnan

“Raja apne tej rath par baithe
aur van mein pravesh kiya.”

“Woh van
Nandan van jaisa sundar tha.”

“Wahan
bilva, khair, kapittha, dhava jaise vriksh the.”

“Zameen
patharon se bhari thi,
na paani tha,
na manushya.”

“Door-door tak
sirf jangli pashu—
hiran, sher, aur bhayanak jaanwar.”

🗡️ Raja ka shikaar

“Raja Dushyanta ne
apne sainikon ke saath
van ko hila diya.”

“Unhone
baan se sher aur baagh gira diye.”

“Jo door the,
unhe baan laga.”

“Jo paas aaye,
unhe talwar se maara.”

“Gada aur dand se bhi
kai jaanwar gir pade.”

🐅 Van mein bhay

“Raja ke shaurya se
sher bhaagne lage.”

“Pashu apne jhund se bichhad gaye.”

“Pyaas aur thakaan se
kai jaanwar gir pade,
kyonki nadiyon mein paani nahi tha.”

“Kuch jaanwar
sainikon ka bhojan ban gaye.”

“Kai ko bhun kar khaaya gaya.”

🐘 Haathiyon ka aatank

“Kai jangli haathi
ghayal aur bhaybhit ho gaye.”

“Khoon vomit karte hue,
apni soondh uthaaye bhaagte hue
kai sainikon ko kuchal diya.”

“Poora van
halchal se bhar gaya.”

🌑 Van ka badalna

“Jo van kabhi
jeevan se bhara tha,
woh dheere-dheere
sher, baagh aur anya pramukh pashuon se
khaali ho gaya.”

“Raja Dushyanta ke shikaar ne
van ka roop hi badal diya.”

✨ Yahin Section LXIX samaapt hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.6
        with st.expander("Section 1.7.6"):
            text1 = """ 
            🏹 Raja Dushyanta aage badhte hain

Vaisampayana bole:
“Rajkumaar,
uske baad Raja Dushyanta
apne sainikon ke saath
hazaaron jaanwaron ka shikaar karke
ek aur van mein pravesh karte hain.”

“Shikaar karte-karte
ab raja thak chuke the.
Bhookh aur pyaas lag chuki thi.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌵 Banjar bhoomi ka drishya

“Raja ke saath
ab sirf ek sevak tha.”

“Van ke kinare
unhone ek bada registan jaisa maidan dekha—
jahan
na ghaas thi,
na ped,
na paani.”

“Us nirjeev bhoomi ko paar karke
raja
achanak ek bilkul alag duniya mein aa gaye.”

🌸 Tapovan ka pravesh

“Saamne tha
ek divya van—
tapovan!”

“Wahan
thandi, madhur hawa chal rahi thi.”

“Har taraf
phoolon se lade ped,
mulayam hari ghaas,
aur pakshiyon ka sangeet.”

“Kokila ki meethi boli,
jhinguron ki tez dhun,
aur madhumakkhiyon ka gunjan
poore van ko jeevit bana raha tha.”

🌳 Swarg jaisa van

“Yeh van
kai yojan tak phaila hua tha.”

“Har ped phalon se bhara,
kisi mein kaante nahi,
har jagah madhumakkhiyaan mandra rahi thi.”

“Phoolon ki chadar
zameen par bichhi thi.”

“Lataon ke mandap the,
aur rang-birange phool
indradhanush jaise lag rahe the.”

✨ Divya jeevon ka nivaas

“Is van mein
Siddha, Charana, Gandharva, Apsara,
vanar aur Kinnar
sab anand mein rehte the.”

“Sab taraf
sugandhit hawa
phoolon ki khushboo la rahi thi.”

“Raja Dushyanta
sab dekhkar
man hi man bahut prasann hue.”

🌊 Malini nadi ka darshan

“Isi van ke beech
behti thi
pavitra Malini nadi—
bilkul saaf, shant aur sundar.”

“Usmein
jal pakshi khel rahe the.”

“Rishi us nadi mein
snan karke
anand paate the.”

“Nadi ke kinaare
hiran shaant bhaav se char rahe the.”

🛕 Rishiyon ka aashram

“Raja ne dekha
ek atyant pavitra aashram—
jaise devlok ho.”

“Wahan
sacred agni jal rahi thi.”

“Bahut se
Rishi, Yati, Valakhilya Muni
wahan dhyaan aur tap mein lage the.”

“Har taraf
yagya-agni ke mandap,
aur shanti ka vaataavaran.”

📿 Vedon ka nad

“Raja ne suna—
kahin Rigveda ka ucharan,
kahin Yajurveda,
kahin Samveda ka madhur gaan,
aur kahin Atharvaveda ke mantra.”

“Jaise poora aashram
Brahmalok ban gaya ho.”

“Vyakarana, tark, jyotish,
moksha-dharma,
sabhi vidyaon ke gyaata
yahaan maujood the.”

👑 Raja ka vinamr roop

“Raja Dushyanta ne
apni rajsi pehchaan chhod di.”

“Sirf apne
mantri aur purohit ke saath
aage badhe.”

“Sena ko
van ke bahar hi rok diya.”

“Raja bole:
‘Main Rishi Kanva ke darshan karke
turant laut aaunga.’”

🌺 Kanva Rishi ka tapovan

“Yeh wahi tapovan tha
jo Kashyapa vansh ke
mahaan Rishi Kanva ka tha—
jinki tejasvi aabha
aankhon se dekhi bhi mushkil thi.”

“Raja jaise-jaise aage badhe,
unhe bhookh-pyaas ka
ehsaas hi nahi raha.”

“Unka man
shanti aur anand se bhar gaya.”

✨ Ant mein…

“Is prakaar,
veer Raja Dushyanta
us pavitra aur divya tapovan mein
pravesh karte hain—
jahan
unki zindagi ka
sabse mahatvapurn adhyay
ab shuru hone wala tha…”

🌸 (Yahin Section LXX samaapt hota hai)"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.7
        with st.expander("Section 1.7.7"):
            text1 = """ 
            “Dushyanta aur Shakuntala ki pehli mulaqat”

👑 Raja Dushyanta akela ashram mein pravesh karta hai

Raja Dushyanta
apni baaki saari sena aur sevakon ko ashram ke bahar chhod deta hai
aur akela hi andar jaata hai.

Lekin…
👀 Rishi Kanva kahin dikhai nahi dete.

Raja zor se bolta hai:
🗣️ “Koi hai yahan?”

Uski awaaz
🌳 jungle mein ghoonj kar wapas aa jaati hai."""
            create_image_text_layout("attached_assets/chapter1/1.7.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌸 Shakuntala ka pravesh

Tab achanak
✨ ek sundar kanya bahar aati hai —
🪷 Sri (Lakshmi) jaisi sundar
👁️ kaali, badi aankhen
🧘‍♀️ tapasvi kanya ka ves

Woh raja ka
🙏 vinamr swagat karti hai —
🪑 baithne ka aasan
💧 pair dhone ka jal
🌼 arghya

Aur pyar se poochti hai:
🗣️ “Rajan, aapki seva ke liye main upasthit hoon. Aap kya aagya dena chahte hain?”

💖 Raja ka man mohit ho jaata hai

Raja Dushyanta
Shakuntala ko dekh kar chakit reh jaata hai 😮

Uski sundarta sirf sharir ki nahi thi —
✨ vinamrata
✨ tapasya ka tej
✨ yuvavastha ki komalta

Raja poochta hai:
🗣️
“Tum kaun ho? Kis ki putri ho?
Itni sundar aur gunwaan ho kar jungle mein kyun rehti ho?
Pehli nazar mein hi tumne mera hriday chura liya hai.”

🌼 Shakuntala ka parichay

Muskurate hue Shakuntala bolti hai 😊:
🗣️
“Hey Raja Dushyanta,
main Maharshi Kanva ki putri hoon.”

🤔 Raja ka sandeh

Raja hairaan ho jaata hai:
🗣️
“Kanva jaise maha-tapasvi rishi,
jinmein kaam-vasna ka lesh bhi nahi,
unke yahan putri ka janm kaise hua?
Yeh baat meri samajh mein nahi aa rahi.”

📜 Shakuntala apni janm-katha sunati hai

Shakuntala bolti hai:
🗣️
“Rajan, jo kahani mujhe mere pita ne batayi,
wahi main aapko sunaati hoon.”

🔥 Vishwamitra aur Indra ka bhay

🧘‍♂️ Maharshi Vishwamitra
bahut kathor tapasya kar rahe the.

☁️ Unki tapasya se
Indra ka singhasan kaanpne laga 😨

Indra sochta hai:
🗣️ “Agar Vishwamitra tapasya mein safal ho gaye
toh mera rajya chhin sakte hain!”

💃 Menaka ko bulaya jaata hai

Indra
🌺 Apsara Menaka ko bulata hai aur kehta hai:

🗣️
“Tum apni sundarta, muskaan, kala aur yauvan se
Vishwamitra ki tapasya bhang karo.”

😨 Menaka ka bhay

Menaka dar jaati hai 😰:
🗣️
“Indra dev!
Vishwamitra toh agni ke samaan hain!
Unke krodh se devta bhi kaampte hain.”

Woh yaad dilati hai:

🔥 Vishwamitra ne dusra brahmand bana diya

🌊 Kaushiki nadi ka srijan kiya

⭐ naye taare bana diye

⚡ Meru parvat tak hila sakte hain

🗣️
“Main ek stri ho kar unke paas kaise jaaun?”

🛡️ Indra ki yojna

Menaka kehti hai:
🗣️
“Agar mujhe jaana hi pade,
toh aap meri raksha ke liye yeh karo:”

✔️ Marut (Pavan dev) meri vastra uda dein
✔️ Kaamdev meri madad kare
✔️ hawa mein phoolon ki sugandh bhar di jaaye

Indra sahmat ho jaata hai 👍

🌸 Menaka tapasya-bhumi ki or prasthan karti hai

Aur is tarah
✨ Menaka Maharshi Vishwamitra ke ashram ki or jaati hai…

👉 Aage kya hota hai?

Vishwamitra ki tapasya bhang hoti hai

Menaka se Shakuntala ka janm hota hai

Kanva rishi use apni putri ke roop mein paalte hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.8
        with st.expander("Section 1.7.8"):
            text1 = """ 
            “Shakuntala ka janm aur uska naam”

🧙‍♂️ Rishi Kanva apni kahani aage badhate hain

Kanva Rishi bolte hain:

🌬️ Indra ka aadesh aur Pavan Dev

Indra ne
🌪️ Pavan Dev (Marut) ko kaha:
🗣️ “Jab Menaka Rishi Vishwamitra ke saamne jaaye,
tum bhi wahan maujood rehna.”   """
            create_image_text_layout("attached_assets/chapter1/1.7.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            💃 Menaka aur Vishwamitra

Dar se bhari
par sundar Menaka
🌿 Rishi Vishwamitra ke ashram mein jaati hai.

Wahan woh dekhti hai:
🔥 Vishwamitra tapasya mein leen hain
✨ unke paap tapasya se jal chuke hain

Menaka
🙏 rishi ko pranam karti hai
aur phir unke saamne nritya aur khel shuru karti hai.

🌬️ Pavan Dev ki leela

Tabhi achanak 😲
🌪️ Pavan Dev Menaka ke vastra uda dete hain,
jo 🌕 chandrama jaise shwet the.

Menaka
😳 sharm se daud kar vastra pakadne lagti hai,
jaise Pavan Dev se naraz ho.

Yeh sab
👀 Vishwamitra apni aankhon se dekhte hain.

💔 Tapasya ka bhang

Vishwamitra
Menaka ki nir-dosh sundarta dekh kar
💓 apna sanyam kho dete hain.

Unka mann kaam-bhav se bhar jaata hai.

Woh
🫱 Menaka ko apne paas rehne ka sanket dete hain
aur Menaka bhi sahmati de deti hai.

⏳ Samay ka beet jaana

Dono
🌸 saath rehte hain
🎶 khelte–muskurate hain

Unhe lagta hai jaise
🕰️ sirf ek din beeta ho,
lekin asal mein bahut samay guzar jaata hai.

👶 Shakuntala ka janm

Isi samay ke beech
Menaka ke garbh se
👶 ek kanya ka janm hota hai —
uska naam Shakuntala.

🌊 Malini nadi ke kinaare

Menaka
🏞️ Himalaya ke sundar ghaati mein
🌊 Malini nadi ke kinaare jaati hai
aur wahin bachchi ko janm deti hai.

Par phir… 😢
woh us nanhi si bachchi ko wahin chhod kar chali jaati hai.

🦅 Pakshiyon ki raksha

Woh jungle
🦁 sher–baagh se bhara tha
lekin 😲
👶 bachchi ko koi nuksaan nahi pahunchta.

🦅 Gidh (vultures)
uske charon taraf baith kar
🛡️ uski raksha karte hain.

Na Rakshas aaye
na koi hinsa hui.

🧘‍♂️ Kanva Rishi ko bachchi milti hai

Rishi Kanva
🚿 snan ke liye nadi par aate hain
aur dekhte hain:

👶 ek nanhi bachchi
🦅 pakshiyon se ghirii hui hai.

Unka mann pighal jaata hai 💖

Woh bachchi ko
🫶 utha kar ashram le aate hain
aur use apni putri bana lete hain.

📜 Pita ka arth

Kanva Rishi kehte hain:

📖 “Shastra ke anusaar:

jo sharir deta hai,

jo jeevan bachata hai,

jo bhojan deta hai —
teeno pita ke samaan hote hain.”*

🐦 Naam: Shakuntala

Kanva Rishi bolte hain:

🗣️
“Jungle mein yeh bachchi
Shakunta (pakshi) se ghir kar rakshit thi,
isi liye maine iska naam
Shakuntala rakha.”

Aur Shakuntala bhi
❤️ Kanva Rishi ko hi apna pita maanti hai.

🌸 Shakuntala Raja se kehti hai

Shakuntala Raja Dushyanta se bolti hai:

🗣️
“Maharaj,
yeh sab mujhe mere pita Kanva ne bataya tha.
Main apne janm ke baare mein itna hi jaanti hoon.
Isliye main Kanva Rishi ko hi apna pita maanti hoon.”

✨ Yahin Section LXXII samaapt hota hai ✨"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.9
        with st.expander("Section 1.7.9"):
            text1 = """ 
            Section LXXIII : “Dushyant aur Shakuntala ka Vivaah”**

👑 Raja Dushyant bolte hain

Shakuntala ki baat sun kar
Raja Dushyant muskura kar bole:

🗣️
“Bahut sundar baat kahi tumne, O rajkumari.
Tum meri patni bano.”

✨
“Main tumhe
💛 sone ke haar,
👗 sundar vastra,
💍 sone ke kaan ke kundal,
⚪ safed moti,
🪙 sone ke sikke
aur 🧶 keemti carpet dunga.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🏰
“Aaj se mera poora rajya tumhara hai.”

💖
“Chalo, mujhe swikar karo.
Hum Gandharva vivaah karein.
Yeh Kshatriyon ke liye shreshth vivaah maana jaata hai.”

🌼 Shakuntala ka uttar

Shakuntala shant swar mein boli:

🗣️
“Maharaj,
mere pita Rishi Kanva fal laane gaye hain.
Kripya thoda ruk jaiye.
Wahi mujhe aapko denge.”

👑 Dushyant samjhate hain

Raja bole:

🗣️
“Tum hi apni malik ho.
Shastra ke anusaar,
tum swayam apna nirnay le sakti ho.”

📜
“Shaadi ke 8 prakaar hote hain.
Unmein se Gandharva vivaah
Kshatriyon ke liye uchit hai.”

💞
“Mujhe tum chahiye,
aur mera dil tum mein basa hai.”

🌸 Shakuntala ki shart

Shakuntala ne dhyaan se sab suna
phir boli:

🗣️
“Yadi dharm yeh maanta hai,
toh meri ek shart hai.”

👶
“Jo putra mujhe hoga,
wahi aapka uttaradhikari banega.”

“Yadi aap isse sweekar karein,
tabhi main vivaah karungi.”

👑 Raja ka vachan

Raja Dushyant bina soche bole:

🗣️
“Main vachan deta hoon.
Aisa hi hoga.”

💍
Aur wahin
🌿 Gandharva vivaah ho gaya.

Raja ne kaha:

🗣️
“Main jald hi
tumhe apni rajdhani le jaane ke liye
apni sena bhejunga.”

🚶‍♂️ Raja ka prasthan

Vivaah ke baad
Raja apni rajdhani laut gaye.

Raaste mein unke mann mein aaya:

🤔
“Rishi Kanva kya kahenge?”

Sochte hue
woh nagar pahunch gaye.

🧘‍♂️ Rishi Kanva ka aagman

Jaise hi Raja gaye,
✨ Rishi Kanva ashram laut aaye.

Shakuntala
😔 sharam ke kaaran
bahar nahi aayi.

Par Kanva Rishi
👁️ divya drishti se sab jaan gaye.

🌿 Kanva Rishi ka aashirvaad

Rishi Kanva bole:

🗣️
“Putri,
tumne jo kiya
woh adharm nahi hai.”

📜
“Gandharva vivaah
Kshatriyon ke liye
uchit maana jaata hai.”

👑
“Raja Dushyant dharmik aur mahaan hain.”

✨
“Tumhara putra
bahut pratapshali hoga,
samudron tak raj karega,
aur uski sena
kabhi haaregi nahi.”

🌸 Shakuntala ka pranam

Shakuntala aage aayi,
🙏 pita ke charan dhoye,
aur boli:

🗣️
“Pitaji,
kripya Raja Dushyant ko
apna aashirvaad dein.”

🌼 Boons ka var

Kanva Rishi bole:

🗣️
“Putri,
jo vardaan maangna chaho,
maango.”

💖 Shakuntala ka vardaan

Shakuntala boli:

🗣️
“Pitaji,
Paurava vansh ke raja
hamesha dharmik rahein,
aur kabhi apna rajya na khoen.”

✨
Rishi Kanva ne
yeh vardaan de diya.

🌟 Yahin Section LXXIII samaapt hota hai 🌟"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.10
        with st.expander("Section 1.7.10"):
            text1 = """ 
            Section LXXIV : Shakuntala ka Apmaan, Sach ki Jeet aur Bharat ka Janm

📖 Vaisampayana bolte hain

Raja Dushyant ke jaane ke baad,
🌸 Shakuntala ne ek balwaan putra ko janm diya.

👶
Bachcha itna tej aur shaktishaali tha
ki jaise agni ki jwala ho.

🔥
3 saal ka hote-hi,
uska tej sabko chamka deta.

✨
6 saal ki umar mein,
woh sher, baagh, haathi tak ko
pakad kar pedon se baandh deta."""
            create_image_text_layout("attached_assets/chapter1/1.7.10.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😲
Sab ashram ke log hairaan reh gaye.

🧘‍♂️
Rishi Kanva ne kaha:
“Yeh bachcha Sarvadamana kehlayega
— jo sabko vash mein karta hai.”

🏛️ Shakuntala Hastinapur jaati hai

Rishi Kanva ne apne shishyon se kaha:

🗣️
“Ab Shakuntala ko
uske pati ke ghar le jaane ka samay aa gaya hai.”

🚶‍♀️
Shakuntala apne putra ke saath
Hastinapur pahunchi.

🌞
Bachcha suraj ki tarah chamak raha tha.

🙏
Shakuntala ne Raja Dushyant se kaha:

🗣️
“Yeh aapka putra hai.
Kripya ise apna uttaradhikari banaiye.
Aapne jo vachan diya tha,
use yaad kijiye.”

💔 Raja Dushyant ka inkaar

Raja Dushyant ne thandi awaaz mein kaha:

🗣️
“Mujhe kuch yaad nahi.
Main tumhe nahi jaanta.
Tum kaun ho?”

😞
Yeh sun kar
Shakuntala ka dil toot gaya.

🔥
Uski aankhon mein aansu aur gussa dono the,
par usne apna krodh sambhaal liya.

🌸 Shakuntala ka dharm-yukt jawab

Shakuntala ne kaha:

🗣️
“Raja,
aap sach jaante hue bhi
jhoot bol rahe ho.”

🕉️
“Bhagwan Narayana
har dil mein baste hain.
Woh sab jaante hain.”

⚖️
“Surya, Chandra, Agni, Vayu,
Dharti aur Dharma
sab aapke karm ke sakshi hain.”

👩‍❤️‍👨
“Patni purush ka aadha hissa hoti hai.
Patni hi dharm, sukh aur moksha ka mool hai.”

👶
“Putra pita ka hi roop hota hai.
Isi liye patni ko Jaya kaha jaata hai.”

🌱
“Putra purkhon ko narak se bachata hai.
Isi liye use Putra kaha gaya.”

💔
“Aap apne hi bete ko kaise thukra sakte ho?”

🔥 Raja ka kathor uttar

Raja Dushyant ne kaha:

🗣️
“Tumhari baatein jhooth hain.
Tumhari maa Menaka ek apsara thi.
Tumhara janm bhi shuddh nahi.”

😡
“Main tumhe nahi maanta.
Jaahan chaaho jao.”

🌺 Shakuntala ka gaurav

Shakuntala ne shant par garv bhare swar mein kaha:

🗣️
“Aap dusron ki chhoti galti dekhte ho,
par apni badi galti nahi.”

✨
“Main apsara ki beti hoon.
Mera janm aap se bhi uchch hai.”

🦢
“Jo buddhimaan hote hain,
woh doodh aur paani mein se
sirf doodh chunte hain.”

⚖️
“Satya sabse bada dharm hai.
Satya se bada kuch nahi.”

🗣️
“Agar aap mujhe nahi maante,
toh main chali jaungi.”

🌍
“Par yaad rakhiye —
mera putra ek din
poori prithvi par raj karega.”

🌩️ Aakashvani (Divine Voice)

Jaise hi Shakuntala jaane lagi,
☁️ aakash se awaaz aayi:

🗣️
“Raja Dushyant,
yeh tumhara hi putra hai.”

👶
“Putra pita ka hi doosra roop hota hai.”

🌸
“Shakuntala sach bol rahi hai.”

📜
“Isliye is putra ka naam hoga —
Bharata,
kyunki ise tum apnaoge.”

😊 Sach ki jeet

Raja Dushyant anand se bhar gaye.

🫂
Unhone apne bete ko gale lagaya,
uska sir soonga.

🙏
Shakuntala ko samman ke saath apnaya.

👑
Putra ko rajgaddi ka uttaradhikari banaya.

🌟 Maharaj Bharata

👑
Bharata ne
sab rajaon ko jeet liya.

⚔️
Woh Chakravarti Samrat bane.

🔥
Unhone kai yajna kiye.
Rishi Kanva unke purohit bane.

🌍
Isi Bharata ke naam par
Bharat-vansh aur
Bharatvarsh ka naam pada."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.11
        with st.expander("Section 1.7.11"):
            text1 = """ 
            Section LXXV : Vansh, Ahankar, Ichchha aur Sachchi Samajh

📖 Vaisampayana bole

Ab main tumhe
🌼 rajaon ki pavitra vanshavali sunata hoon.
Iska shravan
➡️ dharm,
➡️ arth,
➡️ kaam
teenon ko badhata hai.

✨
Is vansh-katha se
📿 punya milta hai,
💰 dhan milta hai,
🌱 aur lambi aayu milti hai."""
            create_image_text_layout("attached_assets/chapter1/1.7.11.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌍 Srishti se Manav tak

🧘‍♂️
Pehle hue Pracetas.
Unke 10 putra tapasvi the.

🔥
Unke baad hue Daksha Prajapati —
jinse sampoorna srishti ka vikas hua.
Isi liye unhe
👴 “Pitamaha” kaha gaya.

👩‍👧‍👧
Daksha ki 50 betiyan thi.
Unhone unka vivaah
➡️ Dharma,
➡️ Kashyapa,
➡️ Chandra
se karwaya.

☀️
Kashyapa aur Aditi se
Aditya hue.
Unmein se ek the Vivasvan (Surya).

👑 Manu aur Manav

🌞
Surya ke putra hue Manu.

📜
Manu se hi
sab Manav jaati ka janm hua.
Isliye hum sab
👥 Manav kehlaye.

👨‍👩‍👦
Manu ke kai putra hue.
Unmein se ek the Ila.

✨
Ila se hue Pururava.

⚡ Pururava ka patan

👑
Pururava bahut shaktishaali raja the.
Unke saath devta jaise saathi rehte the.

❌
Par shakti ke ghamand mein
unhone Brahmanon ka apmaan kiya.

⚡
Rishiyon ke shraap se
Pururava ka vinaash ho gaya.

📌 Seekh:
Shakti bina vinamrata ke vinash laati hai.

🌸 Yayati aur Ichchha ka Rahasya

👑
Pururava ke vansh mein hue Raja Yayati.
Woh dharmic, daani aur veer the.

⏳
Par ek din
un par budhaapa aa gaya.

😔
Yayati ne apne putron se kaha:

🗣️
“Mujhe apni jawani wapas chahiye.
Tum mein se koi
mera budhaapa le lo.”

❌
Sab putron ne mana kar diya.

🌱
Tab sabse chhote putra Puru ne kaha:

🗣️
“Pitaji,
aap apni ichchha poori kijiye.
Main aapka budhaapa sweekar karta hoon.”

💖
Yayati ne Puru ki jawani le li
aur khud jawan ban gaye.

🔥 Bhog se Tripti nahi

⏰
Hazaar saal tak
Yayati ne
sukh aur bhog ka anand liya.

😶
Par phir bhi
unke mann ko shanti nahi mili.

🧠
Tab unhone socha:

🗣️
“Bhog se ichchha kabhi poori nahi hoti.
Jaise agni mein ghee dalne se
aag aur bhadakti hai.”

🌿
“Sachchi shanti tab milti hai jab
man kisi ko dukh na de,
kisi se dare nahi,
aur kisi ko daraye nahi.”

👑 Puru ka Mahaan Ban-na

🙏
Yayati ne
Puru ko uski jawani wapas de di.

👑
Usse rajgaddi par bithaya
aur kaha:

🗣️
“Tu hi mera sachcha uttaradhikari hai.
Mera vansh
tere naam se jaana jayega.”

🧘‍♂️
Yayati khud van mein chale gaye
aur tapasya mein jeevan samarpit kiya.

✨
Ant mein
swarg ko prapt hue.

🌟 Is Kahani ki Seekh

🌼

Ghamand ka ant nishchit hai

Bhog se kabhi poorn tripti nahi milti

Sacrifice sabse bada gun hai

Sachcha putra wahi hai
jo dharm aur tyag samjhe

Shanti bahar nahi,
andar hoti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.12
        with st.expander("Section 1.7.12"):
            text1 = """ 
            📖 Janamejaya ne poocha
“Guruji, mujhe bataiye —
Raja Yayati ko Shukracharya ki beti Devayani kaise mili?
Aur ye sab kaise shuru hua?”

🧘‍♂️ Vaisampayana bole

Yayati Indra jaise tejashvi raja the.
Par is kahani ki jad
⚔️ Devtas aur Asuron ke yudh mein chhupi hai."""
            create_image_text_layout("attached_assets/chapter1/1.7.12.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            ⚔️ Devtas vs Asur

🌩️
Teen lokon ke raaj ke liye
Devtas aur Asur
baar-baar ladte the.

👑

Devtas ke guru the Brihaspati

Asuron ke guru the Shukracharya (Sukra / Kavya)

✨
Par Shukra ke paas ek khaas gyaan tha —
🧬 Sanjeevani Vidya
➡️ jisse mare hue Asur
dubara zinda ho jaate the.

😟
Devtas pareshaan ho gaye.
Unke mare hue sainik
wapis nahi aa pate the.

🌱 Kacha ka Yagya

🙏
Devtas ne Brihaspati ke putra Kacha se kaha:

🗣️
“Tum Shukra ke paas jao.
Unke shishya bano.
Aur Sanjeevani Vidya seekh lo.”

💪
Kacha maan gaye.
Wo Vrishaparva ke rajya mein
Shukra ke paas gaye.

🧘‍♂️
Kacha ne kaha:
“Main aapka shishya banna chahta hoon.
1000 saal tak brahmacharya ka vrat rakhunga.”

✨
Shukra ne sweekar kar liya.

🌸 Devayani aur Kacha

💐
Kacha apne seva-bhav,
vinamrata aur kala se
Devayani ko bhi khush rakhte the.

🎶
Gaana, seva, phool-phal —
sab kuch dil se.

❤️
Devayani bhi
Kacha se lagav mehsoos karne lagi.

☠️ Asuron ka Krodh

😡
500 saal baad
Asuron ko sach samajh aa gaya.

⚠️
Unhone socha:
“Agar Kacha zinda raha
to Sanjeevani Vidya
Devtas ke paas chali jaayegi.”

💀
Asuron ne Kacha ko
3 baar maara:

1️⃣ Pehli baar —
maar kar jaanwaron ko khila diya
➡️ Shukra ne zinda kiya

2️⃣ Doosri baar —
peese hue sharir ko samundar mein mila diya
➡️ Phir zinda hua

3️⃣ Teesri baar —
jala kar raakh bana di
aur Shukra ke sharab mein mila di

😢
Devayani toot gayi.

🗣️
“Pitaji, agar Kacha nahi raha
to main bhi nahi rahungi.”

🔥 Guru aur Shishya ka Dharam

😞
Shukra samajh gaye —
Kacha unke sharir ke andar hai.

⚖️
Dharam ke mutabik
Brahman ko maarna paap tha.

🧠
Isliye Shukra ne ek bada nirnay liya:

🗣️
“Kacha,
main tumhe Sanjeevani Vidya sikha deta hoon.
Tum mere sharir se bahar aao
aur mujhe zinda kar do.”

✨
Kacha ne vidya seekhi.
Shukra ke sharir ko cheera,
bahar aaye
aur apne guru ko phir se jeevit kiya.

🙏
Kacha bole:

🗣️
“Guru hi maa-baap hote hain.
Jo gyaan deta hai,
use nuksaan pahunchana
sabse bada paap hai.”

🚫 Shukra ka Niyam

⚠️
Shukra ne dekha
sharab ki wajah se
ye sab hua.

📜
Unhone ghoshna ki:

🗣️
“Aaj ke baad
jo Brahman sharab piyega
wo apna dharm kho dega.”

Ye niyam
teenon lokon mein fail gaya.

🌈 Ant aur Naya Mod

✨
Shukra ne kaha:

🗣️
“Kacha apna kaam poora kar chuka hai.
Wo Sanjeevani Vidya seekh chuka hai.”

🏹
1000 saal baad
Kacha ne guru se aashirvaad liya
aur devlok laut gaye.

🌟 Is Kahani ki Seekh

🌼

Guru-shishya sambandh pavitra hota hai

Gyaan ka durupyog vinash laata hai

Prem mein bhi dharm zaroori hai

Balidaan aur buddhi
sabse badi shakti hoti hai

✨ Section LXXVI yahin samaapt hota hai ✨"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.13
        with st.expander("Section 1.7.13"):
            text1 = """ 
            Section LXXVII : Kacha aur Devayani ka Antim Mod

🕉️ Vaisampayana bole —

Jab Kacha ka brahmacharya vrat poora ho gaya,
aur unhone Shukracharya se aagya le li,
toh wo Devlok lautne wale the.

Tab Devayani ne unhe roka."""
            create_image_text_layout("attached_assets/chapter1/1.7.13.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            💔 Devayani ka Prem

Devayani ne kaha:

🗣️
“Kacha,
tum janm, gyaan, tapasya aur vinamrata mein mahaan ho.
Jaise mere pita Shukra tumhare pita Brihaspati ka samman karte hain,
waise hi main bhi karti hoon.

Tumhe yaad hai na,
jab tumhara vrat chal raha tha,
mainne tumhara kitna dhyaan rakha?

Ab tumhara vrat poora ho chuka hai.
👉 Mujhe apni patni bana lo.
👉 Mantron ke saath mera haath thaam lo.”

Devayani ke shabdon mein
prem tha, aastha thi, aur vishwas bhi ❤️

🧘‍♂️ Kacha ka Dharam

Kacha shaant rahe.
Unhone vinamrata se kaha:

🗣️
“Devayani,
tum mere liye maa ke samaan ho.

Jaise tumhare pita
mere guru hain,
waise hi tum bhi
mere liye poojniya ho.

Guru ki beti
patni nahi ban sakti.
Ye mera dharm hai.”

😢 Devayani ka Dukh

Devayani ne dukhi hokar kaha:

🗣️
“Jab Asuron ne tumhe baar-baar maara,
tab main tumhare liye royi,
tumhare bina jeene se inkaar kiya.

Meri itni bhakti, itna prem —
kya sab bekaar tha?

Main tumse sach mein prem karti hoon,
phir bhi tum mujhe chhod rahe ho?”

⚖️ Kacha ka Antim Nirnay

Kacha bole:

🗣️
“Devayani,
tum nirdosh ho, pavitra ho.
Par tum meri behen ho.

Humne saath samay achha bitaya,
par maryada kabhi todi nahi.

Mujhe aashirvaad do
taaki meri yatra surakshit rahe.

Aur mere baare mein
hamesha ye yaad rakhna
ki mainne kabhi dharm ka ullanghan nahi kiya.”

🔥 Devayani ka Shraap

Dukh aur gusse mein
Devayani ne keh diya:

🗣️
“Agar tum mujhe apnate nahi,
toh tumhara gyaan
kabhi safal nahi hoga!”

🌟 Kacha ka Shaant Uttar

Kacha ne shaant swar mein kaha:

🗣️
“Tum mujhe shraap de sakti ho.
Par yaad rakho,
mainne tumhe isliye thukraya
kyunki tum guru-putri ho,
na ki kisi dosh ki wajah se.

Tumhara shraap mujhe sweekar hai.

👉 Mera gyaan mere liye nahi,
👉 balki uske liye safal hoga
jise main ye gyaan dunga.

Aur ek baat —
koi bhi Rishi ka putra
tumse vivaah nahi karega.”

(Ye bhi ek shraap hi tha.)

✨ Devlok mein Samman

Kacha turant Devlok chale gaye.

Wahan Indra aur sab Devtaon ne unka swagat kiya 🙏

🗣️
“Tumne hum sab ke liye
bahut bada kaam kiya hai.

Tumhara naam amar rahega.
Tum bhi yagyon ke phal mein
hamare saath bhaag paoge.”

🌈 Is Kahani ki Seekh

🌸

Prem se bada kabhi-kabhi dharam hota hai

Guru aur unke parivaar ka samman sabse upar

Gyaan ka mool uddeshya seva hota hai, swarth nahi

Gusse mein diya shraap bhi jeevan ka rukh badal deta hai

✨ Section LXXVII yahin samaapt hota hai ✨"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.14
        with st.expander("Section 1.7.14"):
            text1 = """ 
            Section LXXVIII : Devayani, Sharmishtha aur Raja Yayati

🕉️ Vaisampayana bole —

Swarg mein sab Devta bahut khush the.
Kacha ne jo adbhut gyaan seekha tha,
wo sab ne use seekh liya.
Ab Devtaon ka kaam poora ho chuka tha ✨

Devta bole:

🗣️
“Ab shakti dikhane ka samay aa gaya hai.
Hey Indra (Purandara), shatruon ka naash karo!”"""
            create_image_text_layout("attached_assets/chapter1/1.7.14.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌸 Talab ke paas khel

Indra Devtaon ke saath nikal pade.
Raste mein unhone dekha —

🌊 Gandharva Citraratha ke udyan mein
kuch yuvtiyan talab mein khel rahi thi.

Indra ne mazaak mein
🌬️ hawaa ka roop le liya
aur un ladkiyon ke kapde
jo kinaare rakhe the
unhe aapas mein mila diya 😄

⚡ Devayani aur Sharmishtha ka Jhagda

Jab sab ladkiyan paani se bahar aayi,
toh galti se —

👗 Sharmishtha
(ne Asur Raja Vrishaparvan ki beti)
👗 Devayani ke kapde pehen liye.

Devayani gusse mein boli:

🗣️
“Tum meri kapde kaise pehen sakti ho?
Tum toh meri shishya ho!”

Sharmishtha aur bhi zyada gussa ho gayi 😡

🗣️
“Tumhare pita
mere pita ke darbaar mein
sir jhuka kar khade rehte hain!

Tum toh bhiksha lene wale ki beti ho,
aur main daan dene wale raja ki beti hoon!
Tum meri barabari nahi kar sakti!”

🕳️ Kuan aur Anyay

Devayani ro padi.
Usne apne kapde kheenchne ki koshish ki.

Sharmishtha ne
😠 gusse mein
Devayani ko ek kuan mein dhakel diya
aur socha —
“Ye toh mar hi gayi hogi.”

Phir wo wahan se chali gayi.

👑 Raja Yayati ka Aana

Thodi der baad
👑 Raja Yayati
(shikar se laut rahe the)
usi jagah aaye.

Unhe pyaas lagi thi.
Kuan ke paas gaye
aur neeche dekha 👀

✨ Unhone kuan mein
ek tej se chamakti hui ladki dekhi.

Raja ne pyaar se poocha:

🗣️
“Tum kaun ho, sundari?
Yahan kaise gir gayi?
Tumhari aankhon mein dukh kyun hai?”

🌼 Devayani ka Parichay

Devayani boli:

🗣️
“Main Shukracharya ki beti hoon.
Mujhe dhokhe se yahan phenk diya gaya hai.

Hey Raja,
aap dharmi aur mahaan ho.
👉 Mera haath pakad kar
mujhe bahar nikaliye.”

✋ Haath Pakadna – Bhagya ka Mod

Raja Yayati ne
jaise hi suna ki
ye Brahman ki beti hai,
unhone turant
👉 Devayani ka daahina haath pakda
aur use kuan se bahar nikaal liya 🌟

Phir Raja apni rajdhani laut gaye.

😢 Devayani ka Dukh

Devayani ne socha:

🗣️
“Main ab Vrishaparvan ke nagar
wapas nahi jaungi.”

Usne apni daasi Ghurnika ko bheja
aur bola:

👉 “Pita ji ko sab sach bata dena.”

🔥 Shukracharya ka Krodh

Jab Shukracharya ne suna
ki unki beti ko apmaanit kiya gaya,
toh unka dil bhar aaya 💔

Wo turant jungle gaye
aur Devayani ko gale lagaya 🤍

Pyaar se bole:

🗣️
“Beti,
kabhi-kabhi dukh
hamare hi karmon ka phal hota hai.”

⚖️ Devayani ka Sach

Devayani boli:

🗣️
“Pitaji,
Sharmishtha ne mujhe kaha
ki aap sirf
dusron ki tarif karne wale ho,
daan lene wale ho!

Agar ye sach hai,
toh mujhe sharmishtha se maafi maangni chahiye!”

🌟 Shukracharya ka Garv

Shukracharya muskuraye 😊
aur garv se bole:

🗣️
“Tum kisi bhikshuk ki beti nahi ho!

Main woh hoon
jise sab poojte hain,
jo kisi se bhiksha nahi leta!

Indra, Vrishaparvan aur Raja Yayati
sab ye jaante hain.

Brahma khud meri shakti hain.
Varsha aur ann
mere tap se hi hota hai!”

🌈 Is Kahani ki Seekh

🌸

Ghamand se hamesha anyay hota hai

Sachcha samman karm se milta hai, pad se nahi

Dukh mein bhi dhairya rakho

Dharam aur vinamrata sabse badi shakti hai

✨ Section LXXVIII yahin samaapt hota hai ✨"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.15
        with st.expander("Section 1.7.15"):
            text1 = """ 
            Section LXXIX : Krodh aur Kshama ki Seekh

🕉️ Shukracharya bole —

“Sun meri beti Devayani,”
“Jo dusron ki buri baaton par dhyaan nahi deta,
wo sab kuch jeet leta hai.”

🚗
Jaise ek achha saarathi
ghodon ki lagam majbooti se pakadta hai
aur unhe bhatakne nahi deta,
waise hi sachha insaan
apne gusse ko kaboo mein rakhta hai."""
            create_image_text_layout("attached_assets/chapter1/1.7.15.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔥
Jo apne uthal-puthal wale krodh ko
rok leta hai,
wo sab par vijay pa leta hai.

🐍
Jo vyakti maaf kar deta hai,
wo apna gussa
aise chhod deta hai
jaise saap apni purani khaal chhod deta hai.

🌿 Kshama ki Mahima

Jo insaan —

gussa nahi karta

dusron ki kadvi baatein ignore karta hai

wajah hone par bhi shant rehta hai

✨
wo jeevan ke chaar lakshya pa leta hai:
👉 Dharma, Arth, Kaam aur Moksha

🕯️
Socho —
100 saal tak har mahine yagya karne wala
aur
jo kabhi gussa hi nahi karta,
dono mein kaun bada hai?

➡️ Jo gussa nahi karta, wahi mahaan hai.

👦👧
Bachche sahi-galat samajh nahi paate
aur jhagadte rehte hain.
🧠 Buddhimaan log kabhi unki nakal nahi karte.

🌸 Devayani ka Dard

Devayani ne pitaji ki baat suni,
phir boli 😔 —

🗣️
“Pitaji,
main jaanti hoon ki
krodh aur kshama mein
kaunsa zyada shaktishaali hai.

Lekin jab
ek shishya apne guru ka apmaan kare,
toh agar guru usse maaf kar de,
toh wo shishya kabhi sudharta nahi.”

🏞️ Sahi Jagah ka Chunav

Devayani boli:

🗣️
“Main us desh mein nahi rehna chahti
jahan bura vyavhaar sahi maana jaye.

Jo buddhi aur bhalaai chahte hain,
unhe un logon ke beech nahi rehna chahiye
jo —

achhe logon ki burai karte hain

achhe kul aur sanskaar ka mazaak udate hain

📍
Sabse achhi jagah wahi hoti hai
jahan acharan aur pavitrata
ki kadar hoti ho.”

🔥 Ant ka Dukh

Devayani ne kaha:

🗣️
“Sharmishtha ke kroor shabd
mere dil ko aise jala rahe hain
jaise sookhe lakdi ko aag jalati hai.

Teenon lokon mein
is se bada dukh aur kya ho sakta hai
ki insaan apne shatruon ki pooja kare
jabki khud ke paas kuch na ho?

📜
Buddhimaan kehte hain —
aisi zindagi se toh
mrityu bhi behtar hoti hai.”

🌈 Is Section ki Moral (Seekh)

✨

Gussa jeet nahi deta, kshama jeet dilati hai

Apmaan ko har baar maaf karna bhi galat ho sakta hai

Sahi sangati aur sahi jagah bohot zaroori hoti hai

Apna swaabhimaan kabhi nahi chhodna chahiye

🌼 Section LXXIX yahin samaapt hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.16
        with st.expander("Section 1.7.16"):
            text1 = """ 
            Section LXXX : Shukracharya ka Krodh aur Devayani ka Nyay

🕉️ Vaisampayana bole —

Us samay Kavya (Shukracharya), jo Bhrigu-vansh ke shreshth the,
bahut krodhit ho gaye.
Wo seedhe Asura-raj Vrishaparvan ke paas gaye aur bina soch-vichaar ke bole 👇"""
            create_image_text_layout("attached_assets/chapter1/1.7.16.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔥 Shukracharya ka Updesh aur Shaap-jaisa Vachan

🗣️
“Hey Raja!
Paap turant phal nahi deta,
lekin dheere-dheere, chupchaap
apna asar dikhata hai.

🍽️
Jaise bhari bhojan kabhi pachta nahi,
waise hi paap bhi kabhi nasht nahi hota.

Uska phal ya toh
👉 khud par,
👉 putra par,
👉 ya potra par
avashya padta hai.”

⚔️
“Tumhare logon ne
Brahmana Kacha ka vadh kiya —
jo dharm gyani aur kartavya-nishth tha,
aur wo mere ghar mein reh raha tha!

😡
Aur meri beti Devayani ka apmaan bhi hua.

Isliye, hey Vrishaparvan,
👉 main tumhe aur tumhare kul ko chhod raha hoon!
Ab main yahan nahi reh sakta.”

😨 Vrishaparvan ka Bhay aur Vinay

Vrishaparvan ghabra gaya aur bola 🙏 —

🗣️
“O Bhargava!
Aap satya aur dharma ke moort swaroop hain.
Kripya hum par daya kijiye!

Agar aap hume chhod denge,
toh hum Asura log
samudra ke tal mein jaakar chhupne ke siwa kuch nahi kar sakte.”

💔 Shukracharya ka Spasht Faisla

Shukracharya bole —

🗣️
“Mujhe tumhari parwah nahi —
chahe tum samudra mein jao
ya dishaon mein bhag jao.

😔
Main apni beti ka dukh nahi dekh sakta.
Devayani meri jaan hai.
Uske bina mera jeevan vyarth hai.

🕯️
Jaise Brihaspati Indra ka hit chahte hain,
waise hi main bhi tumhara hit chahte aaya hoon.

👉 Isliye, Devayani ko prasann karo.”

👑 Vrishaparvan ka Atmasamarpan

Vrishaparvan ne kaha —

🗣️
“O Shukracharya,
Asuron ke paas jo kuch bhi hai —
hathi, ghode, dhan, sampatti —
sab aapka hai…
yahan tak ki main khud bhi!”

Shukracharya bole —

🗣️
“Agar sach mein aisa hai,
toh jao —
👉 Devayani ko santusht karo.”

🌸 Devayani ki Shart

Shukracharya ne sab Devayani ko bataya.
Devayani ne turant kaha —

🗣️
“Agar pitaji sach mein sabke swami hain,
toh Raja Vrishaparvan khud aakar mujhe yeh baat kahe.”

Vrishaparvan aaye aur bole —

🗣️
“O Devayani,
jo bhi tum chaho —
chahe kitna hi kathin kyun na ho —
main dene ko tayaar hoon.”

Devayani boli —

🗣️
“👉 Sarmishtha,
aur uske saath 1000 daasiyaan,
meri seva karein.

Aur jab mere pita mujhe vivaah ke liye den,
tab Sarmishtha mere saath chale.”

😔 Sarmishtha ka Balidan

Vrishaparvan ne Sarmishtha ko bulaya.
Daasi ne sandesh diya —

🗣️
“Devayani ke kehne par
Shukracharya Asuron ko chhodne wale hain.
Tumhe unki iccha poori karni hogi.”

Sarmishtha ne bina virodh kaha —

🗣️
“Main khushi se Devayani ki seva karungi.
Mere kaaran
Shukracharya aur Devayani Asuron ko na chhodein,
bas yahi meri chah hai.”

👑
Sarmishtha 1000 daasiyon ke saath palanquin mein aayi aur boli —

🗣️
“Main aur meri daasiyaan
aapki seva mein samarpit hain.”

Devayani ne taana maara —

🗣️
“Main toh bhikh maangne wale ki beti hoon,
aur tum pooje jaane wale ki —
tum meri daasi kaise?”

Sarmishtha ne shaant bhaav se kaha —

🗣️
“Apne parivaar ke kalyan ke liye
yeh mera kartavya hai.
Main aapke saath chalungi.”

🌈 Ant: Devayani Santusht

Devayani ne apne pita se kaha 😊 —

🗣️
“Pitaji,
ab main santusht hoon.
Ab mujhe pata chal gaya
ki aapka gyaan aur tapasya vyarth nahi hai.”

✨
Is prakar Shukracharya khushi se Asura nagari mein pravesh karte hain,
aur Danav unka bhakti-bhaav se poojan karte hain.

🪔 Section LXXX ki Seekh (Moral)

Paap ka phal avashya milta hai, chahe der se hi kyun na ho

Guru aur beti ka apmaan sabse bada dosh hai

Shakti se zyada nyay aur dhairya prabhavi hota hai

Kabhi-kabhi balidan hi kul ko bachata hai

🌼 Section LXXX yahin samapt hota hai 🌼"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.17
        with st.expander("Section 1.7.17"):
            text1 = """ 
            Vaisampayana bole—
Kuch samay baad,
Devayani, jo bahut sundar thi,
maze ke liye phir usi jungle mein aayi.

Uske saath thi Sarmishtha
aur unki hazaar saheliyan.
Sab milkar jungle mein ghoomne lagi.
Phoolon ka madhu piya,
phal khaye,
aur hasi–mazaak kiya.
Sab bahut khush the 😊"""
            create_image_text_layout("attached_assets/chapter1/1.7.17.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Usi waqt,
Raja Yayati, jo Nahusha ke putra the,
shikaar karte hue wahan aa gaye.
Woh thake hue the
aur pyaas se pareshaan the.

Raja ne dekha—
Devayani, Sarmishtha
aur kai sundar kanyaayein
divya gehno se saji hui hain.

Devayani sabse alag chamak rahi thi ✨
Woh aaraam se leti hui thi,
aur Sarmishtha pyaar se uske pair daba rahi thi.

Raja Yayati bole—

“O sundar kanyaao,
tum dono kaun ho?
Tumhare maa–baap kaun hain?

Lagta hai yeh sab tumhari seva mein hain.”

Devayani ne shaant swar mein kaha—

“O Maharaj, dhyaan se suniye.

Main Shukracharya ki beti hoon,
jo Asuron ke guru hain.

Yeh meri saheli Sarmishtha hai.

Woh Vrishaparvan ki beti hai,
jo Asuron ke raja hain.

Woh mere saath har jagah rehti hai.”

Raja ne poochha—

“Par itni sundar aur rajkumari hote hue bhi,
yeh tumhari seva kyun karti hai?”

Devayani boli—

“Maharaj,
sab kuch bhagya se hota hai.

Aap raja lagte ho,
aapki boli bhi vedon jaisi pavitra hai.

Ab aap apna parichay dijiye.”

Raja Yayati bole—

“Main Yayati hoon.

Brahmacharya ke samay
maine vedon ka gyaan praapt kiya.

Main raja ka putra hoon
aur khud bhi raja hoon.”

Devayani ne poochha—

“Maharaj,
aap yahan kyun aaye ho?
Phool lene, machhli pakadne,
ya shikaar ke liye?”

Yayati bole—

“Main shikaar ke peechhe tha.

Bahut thak gaya hoon
aur mujhe paani chahiye.

Agar aap kahe,
toh main chala jaaun.”

Devayani ne muskurakar kaha 😊

“Hum sab aapke aadesh mein hain.

Aap mere mitra aur swami banein.

Aapka kalyan ho.”

Yayati bole (vinamrata se)—

“Sundari,
main aapke yogya nahi hoon.

Aap Shukracharya ki beti ho.

Aapke pita toh
kisi bade raja ko bhi
aap nahi denge.”

Devayani boli—

“Pehle bhi Brahman aur Kshatriya
ek–dusre se vivaah karte rahe hain.

Aap Rishi ke putra ho
aur khud bhi Rishi ho.

Isliye,
mujhse vivaah kijiye.”

Yayati bole—

“Sab varna ek hi sharir se bane hain,
par unke kartavya alag hain.

Brahman sabse shreshth hote hain.”

Devayani ne dridh swar mein kaha—

“Mera haath
aaj tak kisi ne nahi chhua.

Aaj aapne chhua hai,
isliye main aapko apna pati maanti hoon.

Ab koi aur is haath ko nahi chhoo sakta.”

Yayati bole—

“Buddhiman log kehte hain—

krodhit Brahman
zehrele saanp
aur bhadakti aag se bhi
zyada khatarnaak hota hai.”

Devayani ne poochha—

“Aisa kyun, Maharaj?”

Yayati bole—

“Saanp ek ko maarta hai.
Talwaar bhi ek ko.

Par krodhit Brahman
poore rajya ka vinaash kar sakta hai.

Isliye,
bina aapke pita ki anumati ke
main vivaah nahi kar sakta.”

Devayani boli—

“Agar pita ji anumati de den,
toh aap vivaah sweekaar karenge.

Phir chinta kis baat ki?”

Devayani ne turant
ek daasi ko
Shukracharya ke paas bheja.

Sab baat batayi gayi.

Thodi der mein,
Shukracharya swayam aaye.

Raja Yayati ne
haath jodkar
unka samman kiya 🙏

Devayani ne kaha—

“Pita ji,
yahi Raja Yayati hain.

Mushkil samay mein
inhone mera haath thaama.

Kripya mujhe inhe de dijiye.

Main kisi aur se vivaah nahi karungi.”

Shukracharya bole—

“Beti,
tumne inhe apna pati maan liya hai.

Main tumhe Yayati ko deta hoon.

O Nahusha-putra,
ise apni patni ke roop mein sweekaar karo.”

Yayati ne kaha—

“Maharaj,
mujhe vardaan dijiye
ki is vivaah se
mujhe koi paap na lage.”

Shukracharya bole—

“Chinta mat karo.
Main tumhe paap se mukt karta hoon.

Devayani ka dharm se palan karo
aur sukh pao.

Par ek baat yaad rakhna—

Sarmishtha ka sammaan karna,
par use patni ka adhikaar nahi dena.”

Raja Yayati ne
Shukracharya ke chaaron or
pradakshina ki.

Vidhi–vidhaan se
vivaah sampann hua 🎉

Devayani, Sarmishtha
aur sab saheliyon ke saath
Raja Yayati
khushi–khushi
apni rajdhani laut gaye।

🌸 Moral (Seekh)

✨ Vinamrata aur maryada sabse badi shakti hoti hai

✨ Har nirnay guru aur bado ki anumati se lena chahiye

✨ Bhagya aur dharm milkar jeevan ka raasta banate hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.18
        with st.expander("Section 1.7.18"):
            text1 = """ 
            Vaisampayana bole—

Yayati apni rajdhani wapas aaye.
Shehar Indra ke nagar jaisa sundar tha.
Unhone apni patni Devayani ko mahal mein sthapit kiya.
Devayani ke kehne par, Sarmishtha ko garden ke paas, Ashoka trees ke nikat ek alag mahal diya gaya.

Sarmishtha ke saath 1000 maidens rakhi gayi.
Uske khane–peene aur kapdon ka poora dhyan rakha gaya.
Lekin Yayati zyada samay Devayani ke saath hi rahe.
Un dono ke jeevan mein kaafi saalon tak sukh aur anand raha 🌼"""
            create_image_text_layout("attached_assets/chapter1/1.7.18.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Samay beetne par Devayani maa bani.
Usne ek sundar putra ko janm diya.

Kaafi saal baad, Sarmishtha bhi jawan ho gayi.
Uske mann mein chinta aa gayi.

Usne socha,
“Devayani maa ban chuki hai.
Mera samay bhi aa gaya hai.
Agar aisa hi chalta raha,
to meri zindagi bekaar chali jayegi.”

Uske mann mein ek nischay bana—
“Yayati mujhe bhi ek putra dein.”

Ek din Yayati garden mein ghoomte hue
usi Ashoka van mein aa gaye.
Wahan Sarmishtha khadi thi.
Koi aur wahan nahi tha.

Sarmishtha ne vinamrata se kaha,
“Rajaji, aap jaante hain main achhe kul mein janmi hoon.
Mera samay aa chuka hai.
Kripya mujhe nirash na karein.”

Yayati ne kaha,
“Tum sundar ho, susheel ho.
Lekin Shukraacharya ne mujhe mana kiya hai
ki main tumhe patni jaisa samman na doon.”

Sarmishtha boli,
“Rajaji, main Devayani ki daasi hoon.
Aap Devayani ke pati hain.
Isliye aap mere bhi swami hue.
Mujhe sirf apna dharm poora karna hai.”

Yayati dharm aur kartavya mein ulajh gaye.
Unhone socha aur phir Sarmishtha ki baat maan li.

Kuch samay baad, dono alag ho gaye
aur apni-apni jagah laut gaye.

Samay beetne par, Sarmishtha bhi maa bani.
Usne ek sundar putra ko janm diya.
Bachcha devta jaisa tejashvi tha ✨

Moral:
👉 Zindagi mein galat faisle bhi aage chal kar bade parinaam laate hain.
👉 Dharm aur self-control hi insaan ko sahi raah par rakhte hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.19
        with st.expander("Section 1.7.19"):
            text1 = """ 
            Vaisampayana bole—

Jab Devayani ne suna ki Sarmishtha ke yahan bhi bachcha paida hua hai,
toh uske mann mein jalan (jealousy) aa gayi 😔
Uske dil mein Sarmishtha ke liye kadvi soch bhar gayi.

Devayani seedha Sarmishtha ke paas gayi aur boli,
“Tumne ye kaunsa paap kiya?
Tum apni ichha ke vash mein kaise aa gayi?”

Sarmishtha shaant rahi aur boli,
“Ek mahaan Rishi mere paas aaye the.
Wo Vedo ke gyata the, pavitra aur dharmik.
Maine unse dharm ke anusaar vardaan manga.
Mera beta unhi ka hai.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.19.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Devayani boli,
“Agar aisa hai toh mujhe gussa nahi.
Par agar tum un Rishi ka naam aur kul jaanti ho,
toh mujhe batao.”

Sarmishtha boli,
“Wo tapasya aur tej mein Surya ke saman the.
Unhe dekh kar mujhe aur kuch puchne ki zarurat hi nahi lagi.”

Devayani hans padi 😊
Aur boli,
“Agar sach mein aisa hai,
toh mujhe koi shikayat nahi.”

Dono baat karke alag ho gaye.
Devayani mahal laut gayi.

Samay beetne par—
Devayani ke do putra hue:
👉 Yadu aur Turvasu

Aur Sarmishtha ke teen putra hue:
👉 Drahyu, Anu aur Puru

Ek din Devayani aur Yayati jungle ke ek shaant hissa mein ghoomne gaye.
Wahan unhone teen sundar bachchon ko khelte dekha ✨

Devayani hairaan ho gayi.
Usne pucha,
“Ye bachche kaun hain?
Ye toh bilkul aap jaise lagte hain, rajaji!”

Bina ruke Devayani ne bachchon se puch liya,
“Tumhare pita kaun hain?
Sach batao.”

Bachchon ne ungli se Yayati ki taraf ishara kiya
aur bole,
“Hamaari maa Sarmishtha hai.”

Bachche Yayati ke paas bhaag kar gaye
aur unke ghutno se lipatna chaha.
Par Devayani ke saamne
Yayati unhe gale nahi laga sake.

Bachche dukhi ho kar rote hue
apni maa ke paas laut gaye 😢

Ab Devayani sab samajh gayi.
Usne gusse mein Sarmishtha se kaha,
“Tum meri seva mein rehte hue
mujhe dhokha dene ki himmat kaise kar sakti ho?”

Sarmishtha boli,
“Maine aapse jhooth nahi bola.
Maine dharm ke anusaar hi kiya.
Jab aapne Yayati ko pati chuna,
maine bhi unhe apna pati maana.”

Ye sun kar Devayani aur bhi dukhi ho gayi.
Wo boli,
“Rajaji, aapne mujhe dhokha diya!
Main yahan aur nahi rahungi!”

Aankhon mein aansu lekar
Devayani apne pita Shukracharya ke paas chali gayi.
Yayati bhi pichhe-pichhe gaye,
par Devayani nahi ruki.

Devayani ne apne pita se kaha,
“Pitaji, yahan dharm haar gaya hai.
Sarmishtha ke teen putra hain,
aur mere sirf do.
Yayati dharm jaante hue bhi galat raah par chale gaye.”

Shukraacharya gusse mein bole 😠
“Yayati!
Tum dharm jaante hue bhi paap kar rahe ho.
Isliye tumhari jawani abhi ke abhi chali jayegi!”

Yayati ghabra gaye.
Unhone kaha,
“Pitaji, maine ye kaam dharm ke liye kiya tha.
Agar main Sarmishtha ko mana karta,
toh mujhe bhi paap lagta.”

Shukraacharya bole,
“Tum mere adheen ho.
Tumhe meri aagya ka intezaar karna chahiye tha.
Tum doshi ho.”

Usi pal Yayati ki jawani chali gayi
aur wo buddhe ho gaye 😔

Yayati ne vinamrata se kaha,
“Pitaji, mujhe abhi jeevan ka sukh nahi mila.
Kripya kuch upaay batayein.”

Shukraacharya bole,
“Main apni baat wapas nahi leta.
Par ek rasta hai—
tum apni budhapa apne kisi putra ko de sakte ho.”

Yayati bole,
“Jo putra mujhe apni jawani dega,
wo mera rajya sambhale
aur yash aur dharm paaye.”

Shukraacharya bole,
“Tum jis putra ko chaho,
us par apna budhapa daal sakte ho.
Jo putra tumhari madad karega,
wahi tumhara uttaradhikari hoga.”

Moral:
👉 Jab hum jaante hue bhi galat kaam karte hain,
toh uska phal hamesha milta hai.
👉 Dharm, sach aur self-control hi jeevan ko sahi disha dete hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.20
        with st.expander("Section 1.7.20"):
            text1 = """ 
            Vaisampayana bole—

Yayati, jo ab budhape se peedit ho chuke the,
apni rajdhani laut aaye.
Unhone apne sabse bade putra Yadu ko bulaya.

Yayati bole,
“Beta Yadu,
Shukracharya ke shraap se mujhe budhapa aa gaya hai.
Safed baal, kamzori aur thakaan.
Par mera mann abhi youth ke sukh se bhara nahi hai."""
            create_image_text_layout("attached_assets/chapter1/1.7.20.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Tum meri ye budhapa aur kamzori le lo,
aur mujhe apni jawani de do.
Hazaar saal baad,
main tumhe tumhari jawani wapas kar dunga.”

Yadu ne shaant par spasht shabdon mein kaha,
“Pitaji, budhapa bahut kasht deta hai.
Na dhang se khana, na peena,
na taakat, na utsaah.
Shareer dheere ho jaata hai,
kaam karne ki shakti chali jaati hai.

Isliye pitaji,
main aapka budhapa nahi le sakta.
Aapke aur bhi putra hain.
Kripya unse puchiye.”

Yayati dukhi hue 😔
aur bole,
“Tum mere hriday se janme ho,
phir bhi meri madad nahi ki.
Isliye, Yadu,
tumhare vansh se koi raja nahi banega.”

Phir Yayati ne Turvasu ko bulaya.
Aur wahi baat dohrayi.

Turvasu bola,
“Pitaji, budhapa toh
sukh, sundarta, buddhi
sab kuch chheen leta hai.
Main ise sweekar nahi kar sakta.”

Yayati gusse mein bole 😠
“Tum bhi mere hriday se janme ho,
par meri madad nahi ki.
Isliye tumhara vansh
ashuddh riti-rivaaj wale logon mein rahega,
jahaan dharm ka maan nahi hoga.”

Phir Yayati ne Drahyu se kaha,
“Beta, tum mera budhapa le lo.
Main tumhari jawani se jeevan ka sukh bhogna chahta hoon.”

Drahyu ne kaha,
“Pitaji, budhe log
na ghode, na rath,
na raj-sukh bhog sakte hain.
Unki awaaz bhi kamzor ho jaati hai.
Main ye nahi le sakta.”

Yayati bole,
“Tum bhi mana karte ho.
Isliye tum aise desh ke raja hoge
jahaan na sadkein hongi,
na rath, na ghode.
Log sirf kashti aur beedo se yatra karenge.”

Phir Yayati ne Anu ko bulaya.
Aur wahi prarthana ki.

Anu bola,
“Pitaji, budhapa
shuddhi aur kartavya mein badha daalta hai.
Aise mein yajna aur dharm ka paalan mushkil ho jaata hai.
Main ise sweekar nahi kar sakta.”

Yayati bole,
“Tum bhi mana karte ho.
Isliye tumhare vansh mein
jawani milte hi mrityu aa jaayegi.
Tum yajna bhi nahi kar paoge.”

Ant mein Yayati ne apne sabse chhote putra Puru ko bulaya.
Aur bole,
“Puru, tum mere sabse chhote ho,
par aaj sabse bade sabit hoge.

Mujhe budhapa aa gaya hai.
Par mera mann abhi trupt nahi.
Tum mera budhapa le lo,
aur mujhe apni jawani de do.
Hazaar saal baad
main sab kuch wapas kar dunga.”

Puru ne vinamrata se sir jhukaya 🙏
aur bola,
“Pitaji,
aapka aadesh mere liye sab kuch hai.
Main aapka budhapa sweekar karta hoon.
Aap meri jawani le lijiye
aur jeevan ka sukh bhogiye.”

Yayati ka mann bhar aaya ❤️
aur bole,
“Puru, tumne mujhe prasann kar diya.
Tumhare rajya ke logon ki
saari ichchhaayein poori hongi.”

Itna kehkar,
Yayati ne Shukracharya ka smaran kiya
aur apna budhapa Puru ko de diya,
aur Puru ki jawani swayam le li.

Moral:
👉 Jo santaan niswaarth bhav se
apne mata-pita ka kartavya nibhati hai,
wahi sach mein sabse mahan hoti hai.
👉 Tyag aur vinamrata
jeevan mein sabse bada bal hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.21
        with st.expander("Section 1.7.21"):
            text1 = """ 
            Vaisampayana bole—

Yayati, Nahusha ke putra,
jab Puru ki jawani paakar phir se yuva ho gaye,
toh unka mann bahut prasann ho gaya 😊

Unhone phir se jeevan ke sukh bhogne shuru kiye.
Ritu ke hisaab se,
shakti ke hisaab se,
aur dharm ke daayre mein rehkar.

Yayati ne kabhi adharm ka rasta nahi liya.
Unhone—"""
            create_image_text_layout("attached_assets/chapter1/1.7.21.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Devtaon ko yagya se prasann kiya

Pitron ko shraddh se santusht kiya

Gareebon ko daan diya

Brahmanon ki ichchha poori ki

Atithiyon ko bhojan aur jal diya

Vaishyon ko suraksha di

Shudron se daya se vyavhaar kiya

Aur apraadhi logon ko nyay ke saath dand diya

Is tarah,
Yayati ne apni praja ko
bilkul Indra jaise raja ki tarah paala 👑

Hazaar saal tak,
jawani ke saath,
saare sukh unke vash mein the.
Phir bhi,
unka mann kabhi poori tarah bhara nahi.

Unhe sirf ek baat ka dukh tha—
“Ye hazaar saal kab khatam ho jayenge?”

Hazaar saal beet gaye.
Tab Yayati ne apne putra Puru ko bulaya.

Yayati bole,
“Beta Puru,
tumhari jawani se maine jeevan ke sab sukh bhog liye.
Par ek sach samajh aaya hai.

Iccha kabhi poori nahi hoti.
Jitna bhogo,
utni aur badh jaati hai.
Jaise ghee daalne se aag aur bhadakti hai 🔥

Agar kisi ke paas
poori prithvi ka dhan, sona, ratn,
pashu aur sukh bhi ho,
tab bhi mann santusht nahi hota.

Sachchi khushi unko milti hai
jo laalach chhod dete hain.
Meri icchha hazaar saal tak zinda rahi,
par kam nahi hui.

Ab main sab tyag karunga.
Jungle mein jaakar,
hiranon ke saath,
shant jeevan jeeyunga 🌿

Puru,
tumne mera sabse bada upkaar kiya hai.
Ye lo, tumhari jawani wapas.
Aur ye lo, mera rajya bhi tumhara.
Tum hi mere sachche putra ho.”

Yeh kehkar,
Yayati ne apna budhapa wapas le liya,
aur Puru ne apni jawani phir paayi.

Yayati chahte the ki
Puru ko hi raja bana dein.
Par sab vargon ke log bole—

“Rajan,
Yadu sabse bada beta hai.
Devayani ka putra hai.
Use chhodkar Puru ko rajgaddi kaise mile?”

Yayati shaant swar mein bole,
“Jo beta pita ki baat maane,
jo unka hit chahe,
wahi sabse uttam hota hai.

Yadu, Turvasu, Drahyu aur Anu—
sab ne meri baat nahi maani.
Sirf Puru ne
mera kasht apnaya.

Shukracharya ne bhi kaha tha—
jo beta pita ka aadesh maane,
wahi raja banega.

Isliye,
Puru hi mera uttaradhikari hoga.”

Logon ne bhi kaha,
“Yeh sahi hai.
Achha beta,
chahe chhota ho,
rajya ka adhikari hota hai.”

Is tarah,
Puru raja bane 👑
Aur Yayati ne rajya chhodkar
vanprastha le liya.

Aage chal kar—

Yadu ke vansh se Yadava

Turvasu ke vansh se Yavana

Drahyu ke vansh se Bhoja

Anu ke vansh se Mleccha

Aur Puru ke vansh se Paurava hue

Aur usi Paurava vansh mein,
hey raja,
tumhara janm hua ✨

Moral (Seekh):

👉 Icchha kabhi poori nahi hoti,
par tyag se shanti milti hai.
👉 Jo santaan mata-pita ka aadesh maane,
wahi sachchi uttaraadhikari hoti hai.
👉 Asli rajya bahar nahi,
mann ke niyantran mein hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.22
        with st.expander("Section 1.7.22"):
            text1 = """ 
            Vaisampayana bole—

Jab Raja Yayati, Nahusha ke putra,
apne pyaare putra Puru ko rajgaddi par bithakar,
bahut santusht ho gaye,
toh unhone rajya chhod diya 👑➡️🌿

Woh jungle chale gaye.
Ab unka jeevan tha ek sanyasi ka jeevan."""
            create_image_text_layout("attached_assets/chapter1/1.7.22.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Jungle mein rehkar,
Brahmanon ke saath,
Yayati ne kathor vrat kiye.
Woh phal aur mool khaate the.
Garmi, thand, bhookh—
sab kuch shant mann se sehte the.

Unhone sanyam seekha.
Aur santosh apnaya.

Aakhirkaar,
is pavitra jeevan ke phal ke roop mein,
Raja Yayati swarg pahunch gaye ✨

Swarg mein unhone sukh bhoga.
Par kuch samay baad,
Indra ne unhe swarg se neeche gira diya.

Yeh bhi suna gaya hai,
hey raja,
ki girne ke baad bhi
Yayati dharti tak nahi gire.
Woh kuch samay akash ke madhya mein rahe.

Phir kuch kaal baad,
Vasuman, Ashtaka, Pratardana aur Sivi ke saath,
Yayati ne phir se devlok mein pravesh kiya 🌟

Tab Raja Janamejaya bole—

“Hey Brahman,
main yeh sab vistaar se sunna chahta hoon.

Yayati ko pehle swarg mila,
phir kyun gira diya gaya?
Aur phir dobara swarg kaise mila?

Woh toh dharti ke raja hote hue bhi
Indra jaise mahaan the.
Surya ke samaan tej tha unka.

Kripya,
unke jeevan ki poori kahani sunaiye—
dharti ki bhi,
aur swarg ki bhi.”

Vaisampayana bole—

“Main aapko
Yayati ki pavitra aur adbhut kahani sunata hoon.
Is kahani ko sunne se
paap bhi nasht ho jaate hain 🙏

Puru ko raja banakar,
aur baaki putron ko unke karm ke anusaar sthaan dekar,
Yayati jungle chale gaye.

Wahan woh phal aur mool par jeevan bitate the.
Unka mann aur indriyaan
poori tarah niyantran mein the.

Unhone—

Devtaon aur Pitron ko yagya se prasann kiya

Vanprastha ke niyam anusaar agni mein aahuti di

Mehmaan aur yatriyon ka satkar kiya

Khud zameen par gire daano se jeevan chalaya

Hazaar saal tak
unhone aisa hi pavitra jeevan jiya.

Ek saal tak
maun vrat rakha 🤫
Sirf hawa par jeevit rahe,
bina soye.

Agla saal,
charon taraf aag jalakar
aur sir par surya ke saath,
kathor tapasya ki 🔥☀️

Phir chhe mahine tak,
sirf ek pair par khade hokar,
sirf praan-vayu par jeevit rahe.

Aisi ghor tapasya ke baad,
Raja Yayati ne
swarg ko praapt kiya 🌈

Unki kirti ne
dharti aur swarg—
dono ko prakashit kar diya.”

Moral (Seekh):

👉 Rajya chhodna kathin hota hai,
par tyag se hi sachcha sukh milta hai.
👉 Jo mann aur indriyon par niyantran rakhta hai,
wahi uchch gati ko praapt karta hai.
👉 Tapasya aur sanyam
insaan ko dharti se swarg tak pahucha dete hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.23
        with st.expander("Section 1.7.23"):
            text1 = """ 
            Vaisampayana bole—

Jab Raja Yayati swarg mein reh rahe the,
toh devta, Sadhya, Marut aur Vasu
sab unka samman karte the 🙏

Unka mann poori tarah niyantran mein tha.
Kabhi-kabhi woh devlok se
Brahma-lok bhi jaate the.
Bahut lambe samay tak
woh swarg mein sukh se rahe."""
            create_image_text_layout("attached_assets/chapter1/1.7.23.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Ek din,
Yayati Indra ke paas gaye.
Baaton-baaton mein Indra ne poocha—

“Hey raja,
jab dharti par
tumhare putra Puru ne tumhari budhaapa le li
aur tumne use rajya diya,
tab tumne usse kya shiksha di thi?”

Yayati bole—

“Mainne usse kaha—

👉 Ganga aur Yamuna ke beech ka poora desh tumhara hai.
Yeh dharti ka madhya bhaag hai.
Baaki seema ke rajya
tumhare bhaiyon ke liye hain.

Phir mainne use kuch jeevan ke niyam sikhaye—

👉 Gusse se door rehna.
👉 Maaf karne wala
hamesha gusse wale se bada hota hai.
👉 Agar koi tumhe dukh de,
toh tum bhi use dukh mat dena.

Gussa agar dabaya na jaaye,
toh woh pehle
apne hi mann ko jala deta hai 🔥
Aur jo gusse ko ignore karta hai,
woh dusre ke gunn chheen leta hai.

Kabhi bhi
kadve aur kathor shabd mat bolna.
Aise shabd
teer ki tarah dil ko chubhte hain 🏹
Aur insaan din-raat rota rehta hai.

Jo log
bolon se chot dete hain,
samjho unke muh mein
Rakshas baste hain.
Unse bhagya aur samriddhi door bhaag jaati hai.

Isliye—

👉 Achhe logon ko apna model banao
👉 Buddhiwaan logon ke acharan ko dekho
👉 Bure logon ke shabdon ko ignore karo

Teenon lokon mein
devtaon ko prasann karne ka
sabse achha tareeka hai—

🌸 Dayaa
🌸 Mitrata
🌸 Daan
🌸 Meethe shabd

Isliye hamesha
aise shabd bolo jo mann ko shant karein,
jalane wale shabd kabhi mat bolo.

Jo yogya ho,
uska samman karo.
Aur yaad rakho—

👉 Hamesha do,
👉 Kabhi maango mat.”

Moral (Seekh):

✨ Meethi boli sabse badi shakti hoti hai.
✨ Gussa pehle apne hi mann ko nuksaan pahunchata hai.
✨ Daya, shanti aur achhe shabd
insaan ko swarg tak pahucha dete hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.24
        with st.expander("Section 1.7.24"):
            text1 = """ 
            Vaisampayana bole—

Ek baar phir Indra ne Raja Yayati se poochha—

“O rajan,
tumne apne sab kartavya poore karke van mein tapasya ki.
Batao, ascetic tapasya (tapas) mein
tum apne aap ko kis ke barabar maante ho?”"""
            create_image_text_layout("attached_assets/chapter1/1.7.24.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yayati ne kaha—

“Hey Vasava (Indra),
tapasya ke maamle mein
mujhe manushyon, devtaon, Gandharvon
ya bade Rishiyon mein
apne barabar koi nazar nahi aata.”

Yeh sunkar Indra bole—

“O raja,
tum apne se bade,
apne barabar
aur apne se chhote logon ko bhi
unke gun jaane bina hi
nazarandaz kar rahe ho.

Isi ahankaar (ghamand) ki wajah se
tumhare punya kam ho gaye hain,
aur ab tumhe swarg se girna padega.”

Yayati ne vinamrta se kaha—

“O Sakra,
agar mere punyon mein kami aa hi gayi hai
aur mujhe swarg chhodna hi pade,
toh kam se kam
mujhe sajjan aur dharmic logon ke beech girne ka vardaan do.”

Indra ne kaha—

“Aisa hi hoga, O rajan.
Tum buddhimaan aur dharmic logon ke beech giroge,
aur wahan tumhe maan aur yash bhi milega.

Lekin yaad rakhna—
is anubhav ke baad
kabhi bhi
apne se bade ya barabar logon ka
apmaan mat karna.”

Yayati ka patan (fall)

Itna kehkar,
Raja Yayati swarg se neeche girne lage.

Girते hue unhe dekha
ek mahaan rajarshi ne—
Ashtaka,
jo dharm ke rakshak the.

Ashtaka ne poochha—

“Tum kaun ho, O yuvak?
Tumhari sundarta Indra jaisi hai,
tej agni aur surya ke saman hai!

Aisa lagta hai jaise
surya badalon se nikal raha ho ☀️

Tumhe swarg ke marg se girte dekh
sab log hairaan aur behosh ho rahe hain.

Tumhari shakti Indra, Surya
ya Vishnu ke saman lagti hai.
Isliye hum sach jaanne aaye hain.

Agar pehle tum humse poochhte
toh hum kabhi tumse pehle prashn na karte.
Par ab hum poochhte hain—
tum kaun ho aur yahan kyun aa rahe ho?

Darne ki koi baat nahi.
Tum buddhimaan aur sajjan logon ke beech ho.
Yahan par khud Indra bhi
tumhe koi haani nahi pahuncha sakta.

Sajjan log
dukh mein pade hue logon ka sahara hote hain.
Yahan sirf
gunwaan aur dharmic log hi hain.

Isliye nishchint raho,
shanti se yahan raho.”

Phir Ashtaka ne ek gehri seekh di—

🔥 Agni hi garmi de sakti hai
🌍 Prithvi hi beej ko jeevan deti hai
☀️ Surya hi sabko prakash deta hai

Usi tarah—
Atithi (mehmaan) ko
sajjan logon par
adhikar hota hai
aur woh samman ke yogya hota hai.

Moral (Seekh):

✨ Ahankaar punya ko nasht karta hai
✨ Apne se bade aur barabar logon ka samman zaroori hai
✨ Sajjan log girte hue ko bhi sahara dete hain
✨ Vinamrata swarg ka raasta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.25
        with st.expander("Section 1.7.25"):
            text1 = """ 
            Yayati bole—

“Main Yayati,
Nahusha ka putra aur Puru ka pita hoon.

Maine sab praniyon ko tuchchh samjha,
isi liye
devlok, siddhon aur rishiyon ke lok se gira diya gaya hoon.
Mere punya kam ho gaye hain
aur isliye main neeche gir raha hoon.

Tum sab mujhse umr mein chhote ho,
isliye maine pehle pranam nahi kiya.
Kyunki shastra kehte hain—
jo umr, gyaan ya tapasya mein bada ho,
wahi samman ke yogya hota hai.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.25.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Ashtaka ka uttar

Ashtaka bole—

“O rajan,
sirf umr se koi poojya nahi hota.
Wahi sach mein poojya hota hai
jo gyaan aur tapasya mein shreshth ho.”

Yayati ka gyaan (Wisdom)

Yayati ne kaha—

“Paap, chaar prakaar ke punyon ko nasht kar deta hai.
Ahankaar (ghamand)
narak ka beej hota hai.

Sajjan log kabhi dushton ka anusaran nahi karte.
Ve aisa jeevan jeete hain
jisse unka punya badhta hi rahe.

Mere paas bhi bahut bada dharm-punya tha,
lekin ab sab nasht ho chuka hai.
Shayad main use phir kabhi
apni poori shakti se bhi
prapt na kar paoon.

Meri dasha dekh kar,
jo apna bhala chahte hain
unhe chahiye ki
ahankaar ko turant tyag dein.

Jo vyakti—
• bahut dhan paakar bhi ghamand nahi karta
• saari vidya paakar bhi vinamr rehta hai
• poore Vedo ka adhyayan karke bhi
bhog se door tapasya mein jeeta hai

wahi swarg ko prapt karta hai.

Kisi ko dhan par garv nahi karna chahiye.
Kisi ko vidya par bhi ghamand nahi hona chahiye.

Destiny (Bhagya) ka Siddhant

“Sansaar mein sab log ek jaise nahi hote.
Bhagya sabse shaktishaali hai.

Kabhi kabhi
shakti aur purusharth dono vyarth ho jaate hain.

Jo yeh samajh leta hai
ki sukh aur dukh
bhagya ke adheen hain,
na ki sirf apne prayas ke,

woh na atyadhik khush hota hai
na atyadhik dukhi.

Jab bhagya hi sarvashaktimaan ho,
toh na shok uchit hai
na hi ghamand.

O Ashtaka,
mujhe na bhay vyapt karta hai
na hi main shok karta hoon.
Kyunki mujhe pata hai—
jo vidhaata ne likha hai,
wahi hoga.”

Aatma aur Moksha ka Gyaan

“Keede, patange, ped-paudhe,
sarisrip jeev, machhli, patthar, ghaas, lakdi—

sab prani
jab apne karmon ke bandhan se mukta hote hain,
Parmatma mein vilin ho jaate hain.

Sukh aur dukh
dono asthaayi (temporary) hain.

Isliye, O Ashtaka,
main shok kyun karoon?

Humein kabhi poori tarah pata nahi hota
ki kaunsa karm dukh se bachayega.

Isliye—
dukh aane par shok nahi karna chahiye.”

Ashtaka ka Prashn

Yayati, jo har gun se yukt the
aur Ashtaka ke nana (maternal grandfather) bhi the,
ab bhi aakash mein sthit the.

Ashtaka ne phir poochha—

“O rajaon ke raja,
kripya mujhe bataiye—
tum kaun-kaun se lokon mein rahe,
kitne samay tak unka anand liya?

Tum dharm ki baatein
bilkul mahaan rishiyon ki tarah bolte ho.”

Yayati ka Swarg Lok ka Varnan

Yayati bole—

“Main prithvi par
poori dharti ka samraat tha.

Use chhod kar
maine apne punyon se
kai unche lok prapt kiye.

Pehle maine
ek hazaar varsh tak
uncha lok bhoga.

Phir maine prapt kiya
Indra ka lok—
jo sau yojan tak phaila hua tha
aur jisme hazaar dwar the.

Wahan bhi
maine hazaar varsh bitaye.

Uske baad
main Brahma ke lok mein gaya—
jahan budhapa aur kshay nahi hota,
jise paana bahut kathin hai.

Wahan bhi
maine hazaar varsh vyateet kiye.

Phir main
Vishnu ke lok mein gaya
aur wahan bhi anand liya.

Main Nandana van mein
das lakh varsh tak raha,
apsaraon ke saath khela,
sundar vrikshon aur sugandh ka anand liya.

Punya ka Ant

“Lekin ek din
ek bhayankar dev-doot ne
teen baar zor se pukara—

‘Nashṭ! Nashṭ! Nashṭ!’

Us pal mere saare punya samapt ho gaye.

Devta aakash mein ro rahe the—

‘Haay! Yayati gir raha hai,
uske saare punya nasht ho gaye!’

Girte hue maine poochha—
‘Mujhe kin sajjan logon ke beech girna hai?’

Unhone tumhara
yeh yagya-sthal dikhaya.

Havankund se uthti dhuaan,
ghee ki sugandh se marg pehchaan kar
main yahan aaya hoon—
prasann hoon ki
mujhe tum jaise dharmic log mile.”

🌼 Moral (Seekh):

🔹 Ahankaar sabse bada patan hai

🔹 Dhan, vidya aur swarg bhi asthaayi hain

🔹 Bhagya ko samajhne wala na dukhi hota hai, na ghamandi

🔹 Vinamrta aur gyaan hi sacha swarg hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.26
        with st.expander("Section 1.7.26"):
            text1 = """ 
            Section XC: Ashtaka ne poochha—

“O Maharaj Yayati,
tum apni ichchha se koi bhi roop le sakte the.
Tum Nandana van mein das lakh saal rahe.
Phir tumhe wahan se kyun jaana pada?
Tum yahan kaise aa gaye?”

Yayati ka uttar (Truth of Heaven)

Yayati bole—

“Jaise dharti par
jab kisi ka dhan khatam ho jaata hai,
toh rishtedaar aur dost use chhod dete hain,

waise hi swarg mein bhi hota hai.

Jiska dharm (punya) khatam ho jaata hai,
use devta bhi chhod dete hain.
Indra ke saath sab devta
mujhe chhod kar aage badh gaye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.26.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Ashtaka ka sawaal

Ashtaka bole—

“Par Maharaj,
insaan swarg mein rehkar bhi
apna dharm kaise kho deta hai?

Aur kaunse karm se
kaunse lok milte hain?
Aap toh mahaan purushon ke gyaan ko jaante ho.”

Ghamand ka sabse bada paap

Yayati ne kaha—

“O Rajan,
jo apni hi badaai karta hai,
use Bhauma naam ke narak ka bhog karna padta hai.

Aise log marne ke baad
dharti par apni santaan ke roop mein dikhte hain,
lekin sirf isliye
taaki pakshi aur jaanvar
unke sharir ko kha sakein.

Isliye,
apni tareef karna
sabse ganda aur khatarnaak dosh hai.
Isse hamesha door rehna chahiye.”

Ashtaka ka aur prashn

Ashtaka ne poochha—

“Jab sharir mar jaata hai
aur jal kar raakh ho jaata hai,
toh insaan kahan jaata hai?

Bhauma narak toh dharti par dikhta hi nahi!”

Janm–Mrityu ka rahasya

Yayati bole—

“Sharir ke nasht hone ke baad,
jeev apne karmon ke anusar
maa ke garbh mein phir pravesh karta hai,
ek bahut sookshma roop mein.

Yeh hi Bhauma narak hai—
kyunki yahan jeev
baar-baar janm leta hai
aur moksha ki disha mein
kadam hi nahi badhata.

Kuchh log
60 hazaar saal,
kuchh 80 hazaar saal swarg mein rehte hain,
phir wapas gir jaate hain.

Girte waqt,
unke apne hi rishtedaar
(putra, potra)
Rakshas jaise ban jaate hain,
aur unhe
moksha ke marg se bhatka dete hain.”

Jeev ka sharir mein aana

Yayati aage bole—

“Swarg se girkar
jeev pehle paani mein rehta hai.
Wahi paani
beej ban jaata hai.

Maa ke garbh mein jaakar
wahi beej
dheere-dheere
bhroon, phir bachcha banta hai—
jaise phool se phal banta hai.

Kabhi ped,
kabhi jaanvar,
kabhi insaan—
yeh sab karm ke hisaab se hota hai.”

Indriyon ka vikas

Yayati ne samjhaya—

“Janm ke baad—
kaan se shabd,
aankh se roop,
naak se sugandh,
jeebh se swaad,
sharir se sparsh,
aur mann se vichaar mehsoos hote hain.

Is tarah
sookshma aatma
sthool sharir paati hai.”

Mrityu ke baad kya hota hai?

Yayati bole—

“Mrityu ke baad
jeev sookshma roop mein
sapne ki tarah sab kuchh yaad rakhta hai.

Punya wale
uchchh yoni paate hain,
paapi log
keede-makode ban jaate hain.”

Swarg ke saat dwar (Seven Gates of Heaven)

Ashtaka ne poochha—

“Phir kaise
wapas janm se chhutkaara milta hai?”

Yayati bole—

“Swarg ke saat dwar hain—
1️⃣ Tapasya
2️⃣ Daya
3️⃣ Shant mann
4️⃣ Indriyon par niyantran
5️⃣ Lajja (vinamrta)
6️⃣ Saralta
7️⃣ Sab jeevon par karuna

Lekin ghamand
in sab ko nasht kar deta hai.

Jo vyakti
gyaan paakar khud ko mahaan samajhta hai
aur doosron ko neecha dikhata hai,

woh Brahma lok bhi prapt nahi kar paata.

Padhai, maun, yagya aur pooja—
yeh bhay door karte hain.
Par jab inmein ghamand aa jaaye,
toh yahi bhay ka kaaran ban jaate hain.”

Antim seekh (Final Moral)

Yayati ne kaha—

“Mainne itna daan kiya,
itne yagya kiye,
itna padha—
yeh soch hi patan ka mool hai.

Jo log
nirakaar, avinaashi Brahma ko
apna sahara bana lete hain,

wahi is jeevan mein bhi
aur agle jeevan mein bhi
shanti aur sukh paate hain.”

🌼 Moral (Bachchon ke liye seekh):

🌱 Ghamand sabse bada dushman hai

🌱 Gyaan ho, par vinamrta zaroor ho

🌱 Daya aur karuna hi swarg ka raasta hai

🌱 Janm-mrityu se mukti tab milti hai jab ahankaar chhod diya jaaye"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.27
        with st.expander("Section 1.7.27"):
            text1 = """
            Is section mein Ashtaka aur Maharaj Yayati ke beech
jeevan ke chaar ashramon aur Muni (silent sage) ke dharm par
gehra samvaad hota hai.

Main ise asaan bhaasha mein samjha raha hoon 👇"""
            create_image_text_layout("attached_assets/chapter1/1.7.27.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔱 Chaar Ashram (Modes of Life)
1️⃣ Brahmacharya (Student Life)

Yayati kehta hai:

Guru ke ghar rahe

Guru bulaye tabhi padhai kare

Bina kahe guru ki seva kare

Guru se pehle uthe, baad mein soye

Vinamra ho, indriyon par niyantran rakhe

Satark, dhairyavaan aur adhyayan mein laga rahe

👉 Tabhi gyaan safal hota hai

2️⃣ Grihastha (Householder Life)

Upanishadon ke anusaar:

Imaandari se dhan kamaye

Yagya kare

Daan de

Atithi ka satkar kare

Bina baant ke kuchh bhi na bhoge

👉 Khud khaye, par doosron ko bhool jaaye — yeh paap hai

3️⃣ Bhikshu / Sanyasi (Renunciate)

Sacha Bhikshu wahi hai jo:

Mehnat ya kala se paisa na kamaye

Indriyon ko vash mein rakhe

Sansaar se asang rahe

Ghar mein na rahe

Patni na ho

Roz thoda-thoda chal kar desh bhraman kare

👉 Uska jeevan hi sadhna hota hai

4️⃣ Vanaprastha (Forest Dweller)

Jab bhog ki ichha shaant ho jaaye

Sampatti ka lobh chhoot jaaye

Tab jungle mein tapasya kare

🕊️ Agar Vanaprastha jeevan mein mrityu ho jaaye,
toh 10 peedhiyan tak uddhar hota hai

🌿 Muni ka Sachcha Arth

Ashtaka poochta hai:
Muni ka matlab kya hai?

Yayati ka uttar bahut gehra hai 👇

🔸 Muni ka matlab sirf jungle mein rehna nahi

Jo sansaar se mann hata leta hai

Chahe gaon mein rahe ya jungle mein

Jo ahankaar, jaati, gyaan ka ghamand na kare

Kam vastra mein bhi santusht rahe

Thoda khaye, bas jeevan chalane layak

Kisi ko peeda na de

👉 Wahi sachcha Muni hai

🔸 Maun (Silence) ka Mahatva

Jo indriyon ko vash mein rakhe

Ichha aur karma se virakt ho

Maun vrat apnaaye

👉 Wahi safal hota hai

🔸 Uchch Tam Avastha (Yoga)

Sukh–dukh, maan–apmaan se pare

Dhyaan mein sthit

Jab yog mein baithta hai

✨ Tab Brahma se ek ho jaata hai

🔸 Bhojan ka Antim Rahasya 🍃

Jab Muni:

Khana pehle se plan na kare

Na swaad ke liye khaye

Bas jeevan chalane ke liye grahan kare

Jaise shishu maa ki god mein bina ichha doodh peeta hai

👉 Tab vah sampoorn brahmand se ek ho jaata hai
aur moksha paata hai

🌟 Saar (Core Teaching)

🔹 Ashram badalne se nahi, soch badalne se moksha milta hai

🔹 Jungle mein reh kar bhi sansaar chhoot sakta hai

🔹 Gaon mein reh kar bhi jungle jaise nirmoh ho sakte hain

🔹 Ahankaar hi sabse bada bandhan hai

🔹 Ichha ka tyag hi mukti ka dwar hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.28
        with st.expander("Section 1.7.28"):
            text1 = """ 
            Ashtaka ne pucha,
“Hey Maharaj Yayati,
jo tapasya karta hai aur jo gyaan rakhta hai,
in dono mein se kaun pehle Brahma ko paata hai?”"""
            create_image_text_layout("attached_assets/chapter1/1.7.28.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yayati muskuraye aur bole:

“Suno, Ashtaka.
Jo gyani hota hai,
wo Vedo aur gyaan ke sahare
samajh jaata hai ki
yeh poora duniya ek maya hai.

Uske liye sirf Brahma hi sach hota hai.
Isliye gyani turant mukti paa leta hai.”

“Jo log yog aur tapasya karte hain,
unhe thoda samay lagta hai.
Practice se hi unka mann shaant hota hai.

Agar ek janam mein safalta na mile,
toh agle janam mein
pehle ki mehnat ka fayda milta hai.”

“Lekin jo sachcha gyaan rakhta hai,
wo duniya ke sukh bhogte hue bhi
andar se asang rehta hai.

Isliye uski mukti mein
koi rukawat nahi hoti.”

Yayati ne aage kaha:

“Jo gyaan nahi paa sake,
use nishkaam dharm karna chahiye.
Lekin agar koi
sirf moksha ke laalach mein
yagya aur karm kare,
toh wo safal nahi hota.”

“Lalach se kiya gaya dharm
phal nahi deta.
Bina phal ki ichha ke kiya gaya karm
hi sachcha yoga hai.”

Ashtaka ne phir Yayati ko dekha aur kaha:
“Aap toh yuva jaise lagte ho.
Aap itne tejashvi kyun ho?
Aap kahaan ja rahe ho?”

Yayati ne gambhir swar mein kaha:

“Main swarg se gir chuka hoon.
Mera punya khatam ho gaya.
Ab mujhe Prithvi ke narak mein jaana hai.”

“Lekin Indra ne mujhe vardaan diya hai
ki main girunga toh
sirf gyani aur dharmi logon ke beech hi girunga.
Tum sab waise hi ho.”

Ashtaka bola:
“Agar mere swarg ke lok hain,
toh main sab aapko de deta hoon.
Aap girkar bhi na giro.”

Yayati ne mana kar diya:

“Sirf Brahma-gyani Brahman
daan le sakta hai.
Main raja hoon.
Mujhe daan lena shobha nahi deta.”

Pratardana aage aaye aur bole:
“Mere paas bhi anek swarg-lok hain.
Main sab aapko deta hoon.”

Yayati ne phir mana kar diya:

“Ek raja
doosre raja ka punya daan mein nahi leta.
Vipatti mein bhi
adharm ka raasta nahi chhodna chahiye.”

🌟 Moral (Seekh)

🔹 Gyaan tapasya se tez hai

🔹 Lalach se kiya dharm vyarth hota hai

🔹 Nishkaam karm hi yoga hai

🔹 Sankat mein bhi maryada nahi chhodni chahiye

🔹 Sachcha gyani duniya mein rehkar bhi bandhan se mukt hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.29
        with st.expander("Section 1.7.29"):
            text1 = """ 
            Vasumat ne vinamrata se kaha,
“Main Vasumat hoon.
Maharaj Yayati,
kya mere liye bhi swarg ke lok bane hue hain?
Aap sab jaante ho.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.29.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yayati bole,
“Haan Vasumat.
Tumhare liye itne swarg-lok hain
jitne aakash, dharti
aur dishaon mein chamakti roshni hai.”

Vasumat ne turant kaha,
“Main sab lok aapko deta hoon.
Aap girkar bhi na giro.
Agar daan lena uchit na ho,
toh ek tinke ke badle kharid lo.”

Yayati ne shaant swar mein kaha,
“Main kabhi bhi
adharm se khareed-farokht nahi karta.
Na maine, na kisi mahaan raja ne
aisa kabhi kiya hai.”

Vasumat phir bole,
“Toh phir main zidd karta hoon.
Main khud un lokon mein nahi jaaunga.
Aap hi le lijiye.”

Tab Maha-dani Raja Sivi bole,
“Main Sivi hoon,
Usinara ka putra.
Maharaj, kya mere liye bhi swarg-lok hain?”

Yayati ne kaha,
“Sivi,
tumne kabhi bhi
sachche aur dharmik logon ka apmaan nahi kiya.
Tumhare liye anant swarg-lok bane hain,
bijli jaise chamakne wale.”

Sivi bole,
“Agar lena galat hai,
toh main sab lok aapko deta hoon.
Main unka bhog nahi karunga.”

Yayati ne fir mana kar diya,
“Sivi,
tumhare punya anmol hain.
Main doosron ke diye hue lok
kabhi nahi loonga.”

Ashtaka ne kaha,
“Hum sab aapko
apne-apne lok dena chahte hain.
Agar aap nahi lenge,
toh hum dharti ke narak mein gir jaayenge.”

Yayati bole,
“Tum sab sachche aur gyani ho.
Mujhe wahi do
jo main deserve karta hoon.
Jo kaam maine kabhi nahi kiya,
wo main aaj bhi nahi kar sakta.”

Ashtaka ne aakash ki taraf dekhkar pucha,
“Ye paanch sunehre rath kiske hain?”

Yayati ne kaha,
“Ye rath
tum sabko swarg le jaane ke liye hain.”

Ashtaka bola,
“Toh aap pehle chaliye,
hum baad mein aa jaayenge.”

Yayati muskuraye,
“Hum sab saath-saath chalenge.
Dekho, swarg ka raasta
ab chamak raha hai.”

Tab sab raja
un sunehre rathon par baith gaye.
Unke punya ki roshni se
poora aakash jagmaga utha.

Raaste mein Ashtaka ne pucha,
“Mujhe lagta tha Indra mera mitra hai.
Phir Sivi humse pehle
kaise swarg pahunch gaye?”

Yayati bole,
“Sivi ne
sab kuch daan kar diya tha.
Unki daan, satya, kshama, vinamrata
itni mahaan hai
ki koi uska naap nahi kar sakta.”

Phir Ashtaka ne pucha,
“Aap kaun ho, Maharaj?
Kya kisi aur ne
dharti par aap jaisa kaam kiya hai?”

Yayati bole,
“Main Yayati hoon.
Nahusha ka putra
aur Puru ka pita.
Main kabhi jhooth nahi bola.

Sachchai se hi
dharti aur aakash tikte hain.
Agni jalti hai.
Dev aur rishi pooje jaate hain.”

“Jo koi bhi
meri aur tumhari
is swarg-yatra ki katha
nishkapat mann se
padhe ya sunaye,
wo bhi wahi lok paayega.”

🌟 Moral (Seekh)

🔹 Sachchai sabse bada bal hai

🔹 Punya kharida ya liya nahi jaata

🔹 Tyag aur vinamrata swarg ka raasta hain

🔹 Jo khud ke liye nahi, doosron ke liye jeeta hai, wahi sabse aage badhta hai

🔹 Sacche karm kabhi vyarth nahi jaate"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.30
        with st.expander("Section 1.7.30"):
            text1 = """ 
            Janamejaya ne vinamrata se kaha,
“O gurudev,
main Puru ke vansh ke rajaon ki kahani sunna chahta hoon.
Maine suna hai ki
is vansh mein
koi bhi raja
na toh kamzor tha
na hi bina santaan ke.
Sab gyaan aur shaurya se bhare the.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.30.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Vaisampayana bole,
“Rajan,
main tumhe
Puru ke vansh ki
sundar aur prerna dene wali kahani batata hoon.
Ye sab raja
Indra jaise veer
aur dharm ke rakshak the.”

🌿 Puru se Bharata tak

Puru ke teen putra hue.

Unmein se Pravira ne vansh ko aage badhaya.

Pravira → Manasyu → Sakta, Sahana, Vagmi

Aage chal kar
Richeyu hue
jinhone poori dharti par raaj kiya.
Unka naam pada Anadhrishti.

👑 Mahaan Raja aur Yagya

Anadhrishti → Matinara
jinhone Rajasuya aur Ashwamedha yagya kiye.

Matinara ke putron mein
Tansu ne vansh sambhala.

Tansu → Ilina → Dushmanta

Aur yahin se
ek bahut hi prasiddh kahani shuru hoti hai.

🌸 Dushmanta aur Shakuntala

Dushmanta ne Shakuntala se vivah kiya.

Unke putra hue Bharata.

👉 Bharata itne mahaan hue
ki poora vansh
unke naam se
Bharata Vansh kehlaya.

🔥 Tyag aur Dharm

Bharata ke pehle putra
raja jaise gunon wale nahi the.

Ant mein
ek yagya ke baad
unhe Bhumanyu naam ka putra mila.

Bhumanyu se
aage Suhotra, Ajamidha, Riksha,
aur phir Samvarana hue.

🌧️ Sankat aur Dhairya

Samvarana ke samay
akaal, bimari aur yudh aaye.

Bharata vansh ko
rajya chhodna pada.

Ve jungle mein rahe,
par haar nahi maani.

Tab aaye
Rishi Vashishtha.
Unhone mantra shakti se
Samvarana ko
phir se raja banaya.

👉 Seekh:
Sachcha guru aur dhairya
gire hue ko bhi utha deta hai.

🌞 Kuru aur Kurukshetra

Samvarana ke putra hue Kuru,
jo Surya putri Tapati ke beta the.

Kuru ne tapasya se
dharti ko pavitra kiya.

Isi se
Kurukshetra ka naam pada.

🏹 Santanu tak ka Safar

Kuru → Avikshit → Parikshit

Parikshit → Janamejaya

Aage chal kar aaye
Pratipa,
aur phir unke putra—

👉 Devapi (sanyasi bane)
👉 Santanu (raja bane)

Yahin se
aage jaakar
Ganga-putra Bhishma,
Hastinapur,
aur Mahabharata ki katha shuru hoti hai.

🌟 Moral (Seekh)

👑 Achha vansh sirf khoon se nahi, karm se banta hai

🔥 Dharm aur tyag se hi rajya tikta hai

🌱 Mushkil waqt mein dhairya hi sabse bada bal hai

📿 Guru aur tapasya giray hue ko bhi utha sakti hai

🌍 Isi liye ise Bharata Vansh kaha jaata hai — dharm ka vansh"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.31
        with st.expander("Section 1.7.31"):
            text1 = """ 
            Is section mein Janamejaya apni poori vanshavali (genealogy) sunna chahta hai — chhoti nahi, poori detail mein, kyunki ye katha amrit jaise madhur aur dharma se bhari hui hai.

🌍 Srishti se Rajaon tak (Cosmic Lineage)

Vansh ki shuruaat hoti hai srishti ke mool se:

Daksha → Aditi → Vivasvat (Surya) → Manu (Manav jaati ke pita)

Manu se shuru hoti hai rajaon ki parampara:

Manu → Ha

Ha → Pururavas

Pururavas → Ayus

Ayus → Nahusha

Nahusha → Yayati"""
            create_image_text_layout("attached_assets/chapter1/1.7.31.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            👑 Yayati aur uske Putra

Yayati ki do patniyaan thi:

Devayani → Yadu, Turvasu

Sarmishtha → Druhyu, Anu, Puru

👉 Yadu se Yadava vansh
👉 Puru se Paurava / Bharata vansh

Is katha ka kendr Puru ka vansh hai.

🌸 Puru se Bharata tak

Puru → Janamejaya (older)

Janamejaya → Prachinvat

Prachinvat → Sanyati

Sanyati → Ahayanti

Ahayanti → Sarvabhauma

Aage kai raja aaye, jinhone:

yagya kiye

rajya jeete

dharma ka palan kiya

🌊 Saraswati aur Tansu

Matinara ne Saraswati nadi ke kinare tapasya ki

Saraswati ne prasann hokar unse putra Tansu ko janm diya

👉 Yahin se aage aate hain:

Ilina

Dushmanta

Shakuntala

Bharata

⭐ Bharata — jiske naam par Bharat

Dushmanta ne pehle Bharata ko sweekar nahi kiya

Dev-vani (akashvani) hui:

“Pita hi putra hota hai”

Tab Bharata ko sweekar kiya gaya
Isi liye uska naam pada Bharata (jo sambhala gaya)

👉 Isi Bharata ke naam par Bharatvarsh

🏹 Hastinapur ka Udbhav

Bharata → Bhumanyu

Bhumanyu → Suhotra

Suhotra → Hasti

👉 Hasti ne basayi Hastinapur

🌞 Kuru aur Kurukshetra

Samvarana → Kuru (Surya putri Tapati ka beta)

Kuru ne tapasya se Kurukshetra ko pavitra banaya

👉 Isiliye ye dharti dharma-yuddha ki bhoomi bani

🌊 Santanu aur Bhishma

Pratipa → Santanu

Santanu + Ganga → Devavrata (Bhishma)

Bhishma ne:

pita ke liye pratigya li

apni ichha ka tyag kiya

vansh ko bachaya

🌺 Satyavati, Vyasa aur Rajya ka Rakshan

Santanu + Satyavati → Chitrangada, Vichitravirya

Vichitravirya ke putra nahi hue

Tab:

Vyasa (Dvaipayana) aaye

Janm hue:

Dhritarashtra

Pandu

Vidura

🏹 Pandavas ka Janm

Pandu shraap ke kaaran santaan nahi pa sake

Kunti ke mantra se:

Dharma → Yudhishthira

Vayu → Bhima

Indra → Arjuna

Madri se:

Ashwini Kumar → Nakula, Sahadeva

👉 Pandu ki mrityu, Madri ka sati hona
👉 Panch Pandav Kunti ke saath pale

🔥 Duryodhana ka Irshya aur Sangharsh

Duryodhana ne kai baar Pandavon ko marne ki koshish ki

Lakshagriha, vanvaas, rakshason ka vadh

Draupadi se vivah

Ant mein rajya ka adhikar

🌟 Pandav Putra aur Vansh Raksha

Pandavon ke 11 putra hue
Sabse mahatvapurn:

👉 Abhimanyu

Arjuna ka putra

Uttara se vivah

Putra Parikshit (jo jal kar mar gaya tha)

👉 Shri Krishna ne Parikshit ko punar-jeevit kiya

👑 Janamejaya (Aap)

Parikshit → Janamejaya

Janamejaya → Satanika, Sankukarna

Is tarah:
Bharata Vansh zinda raha

🕉️ Antim Mahavakya (Vyasa ka Sandesh)

Mahabharata = Pancham Veda

Jo ise shraddha se sunta ya padhta hai:

Punya paata hai

Swarg prapt karta hai

Gyaan aur vivek badhta hai

🌺 Moral (Seekh)

🔱 Vansh khoon se nahi, dharma se chalta hai

🔥 Tyag aur satya hi rajya ko amar banate hain

📿 Stri, guru aur dharma ka apmaan vinaash ka kaaran banta hai

🌍 Isiliye ye katha sirf itihaas nahi, jeevan-darshan hai
"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.32
        with st.expander("Section 1.7.32"):
            text1 = """ 
            Yeh kahani ahankar, maryada aur bhagya ki gehri seekh deti hai. Tone simple hai, jaise children’s moral story.

Ek samay ki baat hai.
Ikshvaku vansh mein ek mahaan raja tha — Mahabhisha.
Wo poori dharti ka swami tha.
Sach bolta tha.
Dharma par chalta tha.

Usne:

1000 Ashvamedha yagya

100 Rajasuya yagya

kiye the.
Isliye wo swarg pahunch gaya."""
            create_image_text_layout("attached_assets/chapter1/1.7.32.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Swarg mein ek galti

Ek din swarg mein sab devta aur rajarshi Brahma ji ki pooja kar rahe the.
Wahan Ganga mata, nadiyon ki rani, bhi aayi.

Tez hawa chali.
Ganga mata ke safed vastra hil gaye.

Sab devtaon ne:

nazar jhuka li

maryada rakhi

Par Raja Mahabhisha ne:

dekhte rehna chuna

apna sanyam kho diya

⚡ Brahma ji ka shraap

Brahma ji ne turant kaha:

“Tum apni maryada bhool gaye ho.
Isliye tumhe dharti par dobara janm lena hoga.”

Aur phir kaha:

Tum baar-baar swarg jaa paoge

Lekin Ganga bhi dharti par janm legi

Wo tumhe dukh degi

Jab tumhara krodh jag uthega, tab tum shraap se mukt hoge

Mahabhisha chup ho gaya.
Use apni galti samajh aa gayi.

👑 Pratipa ka putra banne ki ichha

Mahabhisha ne socha:
“Main dharti par Raja Pratipa ka putra banna chahta hoon.”

Udhar Ganga mata bhi usse yaad kar rahi thi.
Isi dauran unki mulaqat Aath Vasuo se hui.

🌟 Vasuo ka dukh

Vasu bole:

“Hum par Rishi Vashishtha ka shraap lag gaya hai.
Galti se hum unke saamne se guzar gaye jab wo sandhya kar rahe the.
Isliye hume bhi manushya ban kar janm lena hoga.”

Unhone Ganga se vinati ki:

“Mata, aap hi hume janm dijiye.
Hum kisi aur stri ke garbh mein nahi jaana chahte.”

🤍 Ganga ka vachan

Ganga ne poocha:
“Dharti par kaun hoga tumhara pita?”

Vasu bole:

“Raja Pratipa ka putra Santanu.”

Ganga boli:

“Yeh bhi meri ichha hai.”

🌊 Ek kathin shart

Vasu bole:

“Janm ke baad hume jal mein pravahit kar dena,
taaki hum jaldi mukti paa sakein.”

Ganga ne kaha:

“Main yeh karungi.
Par ek putra zinda rehna chahiye.”

Vasu bole:

Sab apni shakti ka 1/8 hissa denge

Usse ek putra hoga — mahaan aur tejashvi

Par wo santaan nahi paayega

Ganga maan gayi.

Aur is tarah:

Santanu ka janm

Ganga ka dharti par avatar

aur Bhishma ke aane ka marg

tay ho gaya.

🌼 Moral (Seekh)

👁️ Nazar ka sanyam bhi dharma hai

⚖️ Maryada bhoolne par mahaan bhi gir sakta hai

🌊 Bhagya aur karm milkar jeevan likhte hain

🤍 Tyag kabhi vyarth nahi jaata

Yahi kahani aage chal kar Bhishma, Santanu aur Mahabharata ka aadhaar banti hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.33
        with st.expander("Section 1.7.33"):
            text1 = """ 
            Bahut pehle ki baat hai.
Kuru vansh mein ek dharmic raja the — Raja Pratipa.
Wo sab jeevon par daya karte the.
Lambi tapasya karte the.

Unhone Ganga nadi ke udgam par kai saal tapasya ki."""
            create_image_text_layout("attached_assets/chapter1/1.7.33.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Ganga ka prakat hona

Ek din, Ganga mata
ek sundar stri ka roop lekar
jal se bahar aayi.

Wo bahut hi sundar thi.
Uski beauty dekh kar koi bhi ruk jaaye.

Ganga ne Raja Pratipa ke paas aakar
unki daahini jangha (right thigh) par baith gayi.

🤍 Raja ka sanyam

Raja ne shant swar mein kaha:
“Tum kaun ho?
Aur tum kya chahti ho?”

Ganga boli:
“Main aapko apna pati banana chahti hoon.
Jo stri swayam aaye, use mana karna uchit nahi.”

Par Raja Pratipa ne kaha:
“Main apne vrat se bandha hoon.
Main kisi anya stri ko nahi apnata.
Yeh mera dharm hai.”

🌸 Maryada ka gyaan

Ganga ne phir kaha:
“Main apsara hoon.
Main sundar hoon.
Mujhe mana mat kijiye.”

Raja Pratipa bole:
“Tum meri daahini jangha par baithi ho.
Yeh beti ya bahu ka sthaan hota hai.
Patni ke liye baayi jangha hoti hai.

Isliye main tumhe patni nahi bana sakta.
Par main tumhe apne putra ki patni maanta hoon.”

🌟 Ganga ka vachan

Ganga ne shradha se kaha:
“Jaise aap chahte hain, waisa hi hoga.
Main aapke putra se vivaah karungi.

Par yaad rakhna:
Aapka putra mere karmon par prashn nahi karega.
Main uska bhala hi karungi.
Usse sukh milega.
Aur ant mein wo swarg ko praapt karega.”

Itna keh kar
Ganga antarhit ho gayi.

👑 Santanu ka janm

Samay beeta.
Raja Pratipa aur unki patni tapasya karte rahe.

Budhape mein
unhe ek putra praapt hua.

Uska naam rakha gaya — Santanu.
Kyunki wo sanyam aur tapasya ke baad janma tha.

Santanu bada hua.
Dharmik bana.
Gunon se bhara hua.

🕊️ Pitaji ka updesh

Raja Pratipa ne Santanu se kaha:

“Ek din tumhe ek divya stri milegi.
Agar wo tumse vivaah maange,
toh use mana mat karna.

Uske karmon par prashn mat uthana.
Na uska naam poochna.
Na uska rahasya.”

🌲 Ganga ke kinare mulaqat

Pratipa van chalay gaye.
Santanu raja ban gaya.

Ek din shikar ke dauran
wo Ganga ke tat par pahuncha.

Wahan usne
ek atyant sundar stri dekhi.
Uski beauty Lakshmi ji jaisi thi.

Santanu use dekh kar
apne aap ko sambhaal na saka.
Uska hriday pighal gaya.

Stri ne bhi
Santanu ko dekha.
Uske mann mein bhi
prem jag utha.

💫 Santanu ka prastav

Santanu ne komal swar mein kaha:

“Tum devi ho ya apsara,
yakshini ho ya manav stri —
mujhe nahi pata.

Par tumhari sundarta alaukik hai.
Kripya meri patni bano.”

(Yahin se aage chal kar Ganga–Santanu vivah aur Bhishma ki kahani shuru hoti hai.)

🌼 Moral (Seekh)

🧘 Sanyam hi sabse bada bal hai

🌸 Maryada se hi rishton ka janm hota hai

🌊 Bhagya dheere-dheere apna raasta banata hai

🤍 Sachcha dharm kabhi akela nahi hota"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.34
        with st.expander("Section 1.7.34"):
            text1 = """ 
            Raja Santanu ke madhur shabdon ko sun kar
wo sundar stri muskuraayi.
Use Vasus ko diya hua vachan yaad aa gaya.

Shant aur meethi awaaz mein usne kaha:

“O Raja,
main aapki patni banungi.
Main aapki seva karungi.

Par meri ek shart hai.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.34.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Ganga ki shart

Usne dheere se kaha:

“Aap mere kaamon mein hastakshep nahi karenge.
Chahe wo kaam achha lage ya bura.

Aur aap kabhi bhi
mujhse kathor shabd nahi bolenge.

Jab tak aap daya se pesh aayenge,
main aapke saath rahungi.

Par jis din aapne mujhe roka
ya kadve shabd bole,
main turant chali jaungi.”

🤍 Santanu ka vachan

Raja Santanu ne bina soche kaha:
“Theek hai.
Main aapka vachan maanta hoon.”

Aur is tarah
wo stri Santanu ki patni ban gayi.

🌸 Sukh ke din

Ganga manav roop mein
Santanu ke saath rehne lagi.

Wo sundar thi.
Prem se bhari thi.
Sangeet aur nritya jaanti thi.

Raja Santanu
uske prem mein itne doob gaye
ki samay ka pata hi nahi chala.

Mahine beet gaye.
Ritu badal gayi.
Saale guzar gaye.

👶 Aath bachchon ka janm

Samay ke saath
Ganga ne aath putron ko janm diya.

Sab ke sab
devtaon jaise sundar the.

Par har baar,
janm ke turant baad,
Ganga unhe Ganga nadi mein baha deti.

Wo kehti:
“Yeh tumhare hi bhale ke liye hai.”

💔 Santanu ka dukh

Raja Santanu ka hriday toot jata.
Par wo chup rahe.

Kyunki unhone vachan diya tha.
Wo darrte the
kahin Ganga unhe chhod kar na chali jaaye.

😢 Aathva bachcha

Jab aathva bachcha paida hua,
aur Ganga use bhi nadi mein daalne lagi,
toh Santanu ka dhairya toot gaya.

Aankhon mein aansu the.
Awaaz kaanp rahi thi.

Unhone kaha:

“Ruko!
Is bacche ko mat maaro.

Tum kaun ho?
Apne hi bachchon ko kyun maar rahi ho?

Yeh paap bahut bada hai!”

🌊 Ganga ka sach

Tab Ganga boli,
bilkul shant aur gambhir swar mein:

“O Raja,
aap apna vachan tod chuke hain.
Isliye ab mera yahan rehna samaapt hota hai.

Par chinta na kijiye.
Main is bachche ko nahi maarungi.”

✨ Ganga apni pehchaan batati hai

Usne kaha:

“Main Ganga hoon,
Jahnu ki putri.
Rishiyon dwara poojit.

Main yahan
devtaon ke kaam se aayi thi.

Ye jo aath bachche the,
ye aath Vasu the.
Vasishtha ke shraap se
unhe manav janm lena pada.

Sirf aap hi
itne yogya the
ki unke pita ban sake.

Aur sirf main hi
unki mata ban sakti thi.”

🌟 Shraap se mukti

Ganga ne aage kaha:

“Humara vachan tha
ki janm ke turant baad
main unhe mukti dungi.

Isliye maine unhe nadi mein le jaakar
shraap se mukt kar diya.

Isse aapne bhi
punya aur swarg lok praapt kiya.”

👑 Bhishma ka janm

Ganga ne ant mein kaha:

“Ab is bachche ko paaliye.
Yeh bahut kathor vraton wala hoga.

Iska naam hoga — Gangadatta.”

(Itna keh kar
Ganga antardhan ho gayi.)

🌼 Seekh (Moral)

🤍 Vachan ka palan sabse bada dharm hai

🌊 Kabhi-kabhi jo dukh lagta hai, wo bhale ke liye hota hai

🧘 Sabr aur sanyam raja ka bhi gehna hota hai

✨ Bhagya apne raaz dheere-dheere kholta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.35
        with st.expander("Section 1.7.35"):
            text1 = """ 
            Raja Santanu ne Ganga se poocha:

“Vasus ka dosh kya tha?
Apava kaun tha?
Aur mera putra Gangadatta kyun manav lok mein rahega?
Sab kuch batao, O Jahnu-putri.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.35.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🧘 Apava (Vasishtha) ka parichay

Ganga boli:

“Varuna ke putra Vasishtha,
jinhone baad mein Apava naam paya,
Meru parvat ke nikat tapasya karte the.

Unka ashram pavitra tha,
phoolon, pakshiyon aur mrigniyon se bhara hua.”

🐄 Nandini — Kaamna poori karne wali gai

Daksha ki putri Surabhi se
Nandini naam ki divya gai paida hui.

Yeh kaamna-purti gai thi —
jo bhi uska doodh peeta,
wo lambi aayu aur yuvaavastha paata.

Nandini Apava ke ashram mein
nishchint ghoomti rehti thi.

🌸 Vasus aur unki patniyon ka aana

Ek din aath Vasus,
apni patniyon ke saath wahan aaye.

Unmein se ek Vasu Dyu ki patni
Nandini ko dekh kar mohit ho gayi.

Usne kaha:

“Mere mitra Jitavati ke liye
is gai ka doodh chahiye,
taaki wo vriddh na ho.”

❌ Galti jo shraap ban gayi

Apni patni ko prasann karne ke liye,
Dyu ne apne bhaiyon ke saath
Nandini ko chura liya.

Unhe yaad nahi raha
ki ye Rishi ki gai hai.

🔥 Rishi Apava ka shraap

Jab Apava ne apni gai ko gaayab paaya,
toh apni divya drishti se sab jaan liya.

Krodh mein bole:

“Tum sab Vasus
manav lok mein janm loge!”

Baad mein daya karke kaha:

“Tum sab janm ke ek saal ke andar mukt ho jaoge,
lekin Dyu ko lamba manav jeevan jeena hoga.

Wo putra paida nahi karega,
nari-sang se door rahega,
par dharm aur shastra ka gyani hoga.”

🌊 Ganga ka vachan

Vasus ne Ganga se prarthana ki:

“Janm ke baad humein jal mein le jaana,
taaki hum shraap se mukt ho jaayen.”

Ganga ne vachan nibhaaya
aur pehle saat bachchon ko
janm ke baad jal mein le gayi.

👑 Dyu ka manav janm — Bhishma

Aathva bachcha Dyu tha.
Use jeevit rehna tha.

Isliye Ganga ne kaha:

“Yeh bachcha Gangeya
aur Devavrata ke naam se jaana jaayega.”

Yehi bachcha aage chal kar
Bhishma bana —
maha-tyaagi, brahmachari aur dharm ka stambh.

🌼 Ant aur Mahabharata ki shuruaat

Ganga apne lok chali gayi.
Santanu dukhi man se rajdhani laute.

Aur isi se
Bhishma ki mahaan gatha shuru hoti hai.

📖 Yahi se Mahabharata ka vishal itihaas prarambh hota hai.
✨ Seekh (Moral)

🐄 Dharm ke vastu ko chhuna bhi paap ban sakta hai

🔥 Krodh ka shabd bhi bhagya badal deta hai

🤍 Vachan aur tyag se hi mahaanata janm leti hai

👑 Bhishma ka jeevan — kartavya, sanyam aur balidaan ka pratik"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.36
        with st.expander("Section 1.7.36"):
            text1 = """ 
            Raja Santanu ek mahaan raja the.
Wo satya, daya aur dharm ke liye mashhoor the.

Unke rajya mein koi bhay nahi tha.
Log shaanti se sote aur khushi se uthte the.
Janwar bhi surakshit the.
Kisi ko bina wajah kasht nahi diya jaata tha.

Santanu sab ke pita jaise the.
Insaan, pashu, pakshi — sab unke liye barabar the.

36 saal rajya chalane ke baad,
unhone apna putra Devavrata ko yuvaraj banaya.

Devavrata, jo baad mein Bhishma kehlaya,
apne pita jaisa hi dharmatma tha.
Wo shastra-vidya, dhanurvidya aur gyaan mein mahaan tha."""
            create_image_text_layout("attached_assets/chapter1/1.7.36.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Ganga ka putra — Devavrata

Ek din Santanu ne dekha
ki Ganga ka pravah ruk gaya hai.

Wahan ek yuva veer khada tha
jo apne divya shastr se nadi ko rok raha tha.

Wo koi aur nahi,
Santanu ka apna putra Devavrata tha.

Ganga prakat hui aur boli:
“Yeh tumhara putra hai.
Maine ise sab vidya sikha di hai.
Ab ise apne saath le jao.”

Santanu anand se bhar gaye.

🌸 Machhuaarin ki beti — Satyavati

Kuch saal baad,
Santanu Yamuna ke kinare gaye.

Wahan unhone ek sundar kanya dekhi.
Uske sharir se divya sugandh aa rahi thi.

Wo thi Satyavati,
machhuaare ki beti.

Santanu usse vivah karna chahte the.
Par uske pita ne ek shart rakhi:

👉 “Satyavati ka beta hi raja banega.”

Santanu chinta mein pad gaye.
Wo apne putra Devavrata ka adhikar nahi cheenna chahte the.

😔 Pita ka dukh, putra ka tyag

Devavrata ne pita ka dukh dekha.
Usne sach jaan liya.

Wo seedha machhuaare ke paas gaya aur bola:

“Satyavati ka putra hi raja banega.
Main apna adhikar tyag karta hoon.”

Machhuaara phir bhi nishchint nahi hua.
Usne kaha:

“Tumhare bete kya karenge?”

🔥 Bhishma Pratigya

Tab Devavrata ne sabse kathor pratigya li:

“Aaj se main brahmachari rahunga.
Na shaadi, na santaan.
Main jeevan bhar nishtha aur tyag ka palan karunga.”

Yeh sunkar
devta, rishi aur apsara aakash se pushp barsane lage.

Sab ne kaha:
“Yeh Bhishma hai — bhayankar pratigya wala!”

👑 Pita ka vardaan

Santanu ne jab sab suna,
unka hriday bhar aaya.

Unhone Bhishma ko vardaan diya:

“Tumhe ichha-mrityu ka vardaan deta hoon.
Jab tak tum chahoge, mrityu tumhe nahi chhooegi.”

🌼 Seekh (Moral)

🤍 Sachha putra wo hota hai jo pita ke sukh ke liye apna sukh tyaag de

🔥 Tyag aur pratigya insaan ko mahaan banati hai

👑 Bhishma ka jeevan = kartavya + sanyam + balidaan"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.37
        with st.expander("Section 1.7.37"):
            text1 = """ 
            Shaadi ke baad,
Raja Santanu ne
apni sundar patni Satyavati ko
raaj ghar mein sthaan diya.

Kuch samay baad,
Satyavati se
Santanu ke
ek buddhimaan aur veer putra hue.
Uska naam tha Citrangada."""
            create_image_text_layout("attached_assets/chapter1/1.7.37.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Citrangada
bahut shaktishaali tha.
Veer tha.
Aur dheere-dheere
ek prasiddh yoddha ban gaya.

Santanu ke
Satyavati se
ek aur putra bhi hua.
Uska naam tha Vicitravirya.

Vicitravirya
bhi mahaan dhanurdhar bana.
Aur baad mein
raja bhi bana.

Lekin
Vicitravirya ke
poori tarah yuva hone se pehle hi
Samay ne apna kaam dikhaya.

Raja Santanu
svarg ko chal base.

Santanu ke jaane ke baad,
Bhishma,
jo sach aur kartavya ka
jeevit roop tha,
Satyavati ke aadesh mein raha.

Bhishma ne
Citrangada ko
Kuru rajya ke
singhasan par bithaya.

Citrangada ne
apni shakti se
kai rajaon ko hara diya.

Use laga
ki duniya mein
uske barabar
koi nahi hai.

Par ahankaar ke saath
pariksha bhi aati hai.

Ek din,
Gandharvon ka raja,
jiska naam bhi
Citrangada hi tha,
us se yudh karne aa gaya.

Kurukshetra ke maidan mein,
Sarasvati nadi ke kinaare,
bhayankar yudh hua.

Yeh yudh
teen saal tak chala.

Shastra takraate rahe.
Zameen kaanpti rahi.
Dono yoddha
poori shakti se lade.

Ant mein,
Gandharva raja
adhik chalaak aur balwaan nikla.

Usne
Kuru rajkumar Citrangada ko
yudh mein maar diya.

Jeet ke baad,
Gandharva raja
svarg chala gaya.

Citrangada ke veer mrityu ke baad,
Bhishma ne
uske sab
antim sanskaar kiye.

Phir Bhishma ne
chhote aur abhi yuva na bane
Vicitravirya ko
singhasan par bithaya.

Vicitravirya
Bhishma ke margdarshan mein
rajya chalane laga.

Woh Bhishma ka
bahut aadar karta tha.

Aur Bhishma bhi
use
pita jaise
suraksha dete rahe.

Is tarah,
kartavya, tyaag aur maryada
Kuru vansh ko
sambhalte rahe.

🌼 Seekh (Moral)

⚖️ Ahankaar veer ko bhi gira deta hai

🤝 Sahi margdarshak zindagi bachata hai

🌱 Kartavya aur vinamrata se hi rajya tikta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.38
        with st.expander("Section 1.7.38"):
            text1 = """ 
            Citrangada ke veer ghatna ke baad,
jab Vicitravirya abhi chhota tha,
tab Bhishma ne rajya ka bojh sambhala.

Bhishma ne
sab kuch Maa Satyavati ke aadesh se kiya.
Unka ek hi lakshya tha —
Kuru vansh ka bhavishya surakshit rahe.

Jab Vicitravirya bada hua,
samajhdaar aur yogya bana,
tab Bhishma ne socha:

👉 “Ab mere bhai ka vivaah hona chahiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.38.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Usi samay,
yeh samachar aaya
ki Kashi ke raja ki teen sundar putriyaan
ek Swayamvar mein
apna pati chune wali hain.

Teeno kanyaein
apsaraon jaisi sundar thi.

Bhishma,
jo sabse mahaan rath-yoddha the,
sirf ek rath par
Varanasi nagar pahunch gaye.

Wahan unhone dekha —
har disha se
raja aur yoddha aaye hue the.

Swayamvar shuru hua.
Rajaon ke naam liye ja rahe the.

Tab Bhishma ne
sabke saamne
ek garajti awaaz mein kaha:

“Kshatriya dharm ke anusaar,
yudh ke bal par kanya haran bhi vivah ka ek roop hai!”

Aur kehkar,
Bhishma ne
teeno kanyaon ko rath par bithaya
aur kaha:

👉 “Jo mujhe rok sakta hai, rok ke dikhaye!”

Yeh kehna tha,
aur sab raja
krodh se bhar gaye.

Shastra uthe.
Rath daude.
Aasmaan mein
baanon ki barsaat ho gayi.

Ek taraf —
sauon raja
Dusri taraf —
akela Bhishma.

Par Bhishma
parvat ki tarah atoot the.

Unke baan
bijli jaise chalte.
Shatruon ke
dhanush toot gaye.
Rath dhwaj gir gaye.

Yudh itna bhayankar tha
ki dekhne wale bhi kaanp uthe.

Ant mein,
sab raja
haar maan gaye.

Sirf Raja Shalya
peeche se aakar
Bhishma ko yudh ke liye lalkarne lage.

Bhishma ruke.
Kshatriya dharm nibhaya.

Dono veeron ka
bhayankar sangharsh hua.

Ant mein,
Bhishma ne
Shalya ko hara diya,
par jeevan daan diya.

Yeh dekhkar,
sab raja
apne-apne rajya laut gaye.

Bhishma
teeno kanyaon ko lekar
Hastinapur pahunche.

Unka vyavhaar
aisa tha
jaise woh
unki rakshak pita ho.

Phir Bhishma ne
sab kuch Maa Satyavati se salah karke
shaadi ki taiyaari shuru ki.

Tab sabse badi kanya Amba boli:

👉 “Mera mann pehle se hi
Saubha ke raja ke saath jud chuka tha.”

Bhishma ne
dharma ka paalan kiya.

Brahmanon se salah li.
Aur Amba ko
apni ichchha se jaane diya.

Baaki do behnein —
Ambika aur Ambalika
Vicitravirya se vivaahit hui.

Vicitravirya ne
kuch varsh
apni patniyon ke saath
sukh se jeevan bitaya.

Par bhagya ne
phir kadi pariksha li.

Jawani mein hi
Vicitravirya
gambhir rog se grasit ho gaye.

Bahut upchaar hue.
Par Samay ko koi hara nahi sakta.

Jaise doobta sooraj,
waise hi
Vicitravirya ka jeevan
shant ho gaya.

Bhishma
gehre dukh mein doob gaye.

Unhone phir bhi
kartavya nahi chhoda.

Satyavati ke saath milkar,
sab antim sanskaar
vidhi se karwaye.

Aur Kuru vansh ka
bojh phir se
apne kandhon par le liya.

🌼 Seekh (Moral)

⚔️ Shakti se zyada mahatvapurn dharma hota hai

🤍 Sachcha veer daya bhi jaanta hai

⏳ Samay sabse shaktishaali hai

👑 Kartavya kabhi chhodna nahi chahiye"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.39
        with st.expander("Section 1.7.39"):
            text1 = """ 
            Vicitravirya ke nidhan ke baad,
Mata Satyavati ka hriday
gehre shok mein doob gaya.

Unhone
apni dono bahuon (Ambika–Ambalika) ke saath
antim sanskaar poore vidhi–vidhaan se kiye.

Phir,
apne aansuon ko sambhalte hue,
unhone Bhishma ko dekha —
jo shastra mein mahaan,
par hriday se bhi mahaan the."""
            create_image_text_layout("attached_assets/chapter1/1.7.39.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Satyavati ne
dharma aur vansh ki or drishti karke kaha:

“O Bhishma,
pind-daan, vansh ki kirti
aur Santanu ke vansh ka bhavishya
sab kuch ab tum par nirbhar hai.

Jaise swarg punya ke bina nahi milta,
jaise satya ke bina dirgh aayu nahi hoti,
waise hi dharma tumhare bina adhoora hai.”

Satyavati aage boli:

“Tum Vedo, Shrutiyon
aur kul-dharma ke gyaata ho.
Gyaan mein tum Shukra aur Angiras ke samaan ho.

Isliye,
main tumse ek kaarya ke liye vinati karti hoon.
Suno aur mera aadesh poora karo.”

Unhone bhari awaaz mein kaha:

“Tumhara bhai
nishsantan swarg ko chala gaya.
Uski patniyaan ab putra ki ichchhuk hain.

Isliye,
tum unse santaan utpann karo
taaki Kuru vansh toot na jaaye.”

Aur phir Satyavati ne
sabse kathor baat kahi:

“Rajya sambhalo.
Vivah karo.
Vansh ko bachao.
Apne purkhon ko narak mein mat girao!”

Yeh sunte hi,
Bhishma ne
shant par dridh swar mein uttar diya:

“Maa,
aap jo keh rahi hain
dharma ke anuroop hi lagta hai.

Lekin
aap mere pratigya ko jaanti hain.”

Bhishma ne kaha:

“Main teenon lok chhod sakta hoon,
swarg ka raj bhi chhod sakta hoon,
par satya ko kabhi nahi chhod sakta.”

Aur phir
unhone ek–ek kar
prakriti ke udaharan diye:

“Prithvi apni sugandh chhod de,
jal apni shitalta,
agni apni garmi,
surya apni roshni,
Indra apni shakti,
Yama apna nyay chhod de…

par Bhishma satya nahi chhod sakta.”

Satyavati ne
phir karun swar mein kaha:

“Main jaanti hoon tumhari pratigya
meri wajah se thi.

Par beta,
yeh aapatkaal hai.
Vansh toot gaya
toh sab kuch nasht ho jayega.”

Par Bhishma ne
vinamrta se kaha:

“Maa,
Kshatriya ke liye
satya-bhang sabse bada paap hai.

Main pratigya todkar
vansh nahi bacha sakta.”

Phir Bhishma ne
ek buddhimani ka marg bataya:

“Main aapko
ek anya dharmik upaay batata hoon
jo aapatkaal mein sweekrit hai.

Pehle us par
brahmanon aur gyaaniyon se
vichaar-vimarsh kariye.”

Yeh kehkar,
Bhishma chup ho gaye —
jaise dharma khud bolkar
maun ho gaya ho.

🌼 Moral (Seekh)

🕊️ Satya ka bal sabse bada hota hai

👑 Pratigya todkar jeeta hua rajya, rajya nahi hota

⚖️ Dharma mein bhi buddhi aur maryada chahiye

🔥 Aapatkaal mein bhi satya ka tyag nahi"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.40
        with st.expander("Section 1.7.40"):
            text1 = """ 
            Bhishma bole:

“Maata, main aapko
praachin itihaas sunata hoon,
jisse aapatkaal ka dharmic marg samjha ja sake.”

🔱 Parashurama aur Kshatriyon ka Vinash

Praachin kaal mein
Rama Jamadagni-putra (Parashurama)
ne apne pita ke vadh se krodhit hokar
Haihaya raja Arjuna ko apni parashu se maar diya
aur uske hazaar bhuja kaat di."""
            create_image_text_layout("attached_assets/chapter1/1.7.40.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Uske baad bhi unka krodh shaant na hua.
Unhone 21 baar Kshatriya vansh ka nash kiya.

Jab dharti Kshatriyon se rikt ho gayi,
tab Kshatriya striyon ne
Brahmanon se santaan utpann karayi,
kaamna se nahi, dharma se.

📜 Vedo ka niyam kehta hai:

“Jo putra aise janme,
vah maa ke pati ka hi maana jaata hai.”

Is prakar Kshatriya vansh punah jeevit hua.

🌱 Rishi Dirghatamas ki Katha

Bhishma ne kaha:

“Ab ek aur katha suno.”

Ek mahaan rishi the — Utathya
unki patni ka naam tha Mamata.

Utathya ke chhote bhai
Vrihaspati (Devguru)
ne kaamna-vash Mamata se sambandh chaha.

Mamata ne rokte hue kaha:

“Main garbhavati hoon.
Jo shishu mere garbh mein hai,
usne garbh mein hi Ved aur Anga padh liye hain.
Ek hi garbh mein do shishuon ka sthaan nahi.”

Garbh se hi shishu ne kaha:

“He pita, ruk jaaiye.
Main pehle se yahan hoon.”

Par Vrihaspati ne na maana.
Garbh-shishu ne beej ko pravesh se roka
aur veerya dharti par gir gaya.

Krodhit hokar Vrihaspati ne shraap diya:

“Tum sada andhakaar mein rahoge!”

Is shraap se
Dirghatamas ka janm hua —
jo janm se andhe the
par Ved-gyaani bhi the.

🕯️ Dirghatamas ka Parivaar aur Tyag

Dirghatamas ne
Pradveshi naamak kanya se vivah kiya
aur kai putra utpann hue,
par ve lobhi aur moorkh nikle.

Ashram ke rishiyon ne
un par galat aarop lagaye
aur patni bhi unse vimukh ho gayi.

Patni boli:

“Pati use kehte hain jo poshan aur raksha kare.
Aap to swayam asahay hain,
main hi sab sambhaal rahi hoon.”

Dirghatamas ne kaha:

“Mujhe Kshatriyon ke paas le chalo,
tum dhani ho jaogi.”

Patni ne inkaar kiya
aur putron ko aadesh diya:

“Is vriddh ko Ganga mein baha do!”

Putron ne unhe
bedi se baandh kar Ganga mein baha diya.

🌊 Raja Bali aur Vansh ka Uddhaar

Ganga mein bahte hue
Dirghatamas ko
Raja Bali ne dekha aur bachaya.

Raja ne vinati ki:

“Mere vansh ke liye
dharmic putra utpann kijiye.”

Raja ki patni Sudeshna
rishi ke paas na jaakar
apni dhaai (nurse) bhej deti hai.

Us dhaai se
11 mahaan putra hue —
jinmein Kakshivat pramukh tha.

Raja Bali ne poocha:

“Kya ye mere putra hain?”

Rishi bole:

“Nahi.
Ye mere hain.
Tumhari patni ne mera apmaan kiya.”

Phir Sudeshna swayam aayi.
Rishi ne keval sparsh se kaha:

“Tumhare paanch putra honge —
Anga, Vanga, Kalinga, Pundra, Suhma.”

Aur unke naam par
desh prasiddh hue.

⚖️ Bhishma ka Sandesh Satyavati ko

Bhishma ne katha samapt karte hue kaha:

“Maata,
is prakar aapatkaal mein
Brahman se Kshatriya vansh ki raksha hui.

Yeh dharma ke viruddh nahi,
balki dharma ki raksha hai.

Ab aap gyaaniyon se vichaar karke
jo uchit ho, wahi nirnay lein.”

🌼 Moral / Seekh

🔥 Aapatkaal ka dharma alag hota hai

🧬 Vansh-raksha ke liye Niyoga dharmic tha

⚖️ Niyat shuddh ho to kriya paap nahi

🕊️ Dharma sthir hai, par uska marg paristhiti ke anusaar hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.41
        with st.expander("Section 1.7.41"):
            text1 = """ 
            Bhishma bole:

“Maata, Bharata vansh ko bachane ka upaay suno.
Ek mahaan, siddh Brahmana ko bulaya jaaye
aur Vicitravirya ki patniyon par santaan utpann karai jaaye.
Yeh aapatkaal ka dharm hai.”

🌊 Satyavati ka Rahasya (Vyasa ka Janm)

Satyavati, halki si laaj ke saath, Bhishma se boli:

“Tum dharm aur satya ho, isliye meri baat suno.”

“Yuvavastha mein, main apne pita ki naav chalati thi.”

Ek din Maharshi Parashara Yamuna paar karne aaye.

Unki tapasya ke bhay aur shraap ke darr se
Satyavati ne niyog-sambandh sweekar kiya.

✨ Parashara ka varadaan:

Machhli ki gandh divya sugandh mein badal gayi

Kumari avastha barkarar rahi

Dweep par janma putra hua — Dvaipayana (Vyasa)"""
            create_image_text_layout("attached_assets/chapter1/1.7.41.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            📜 Vyasa ka Mahatva

Vedo ko chaar bhaagon mein vibhaajit kiya → isliye Vyasa

Shyaam varna → Krishna

Maha-tapasvi, nishkaam, satyavaadi

Janm ke turant baad tapasya ke liye chale gaye

Jaate samay kaha:

“Maata, jab bhi sankat ho, mujhe smaran karna.”

🔔 Vyasa ka Aahvaan

Bhishma ne poorn samarthan diya:

“Jo dharm, arth aur kaam ko santulit kare, wahi buddhi hai.”

Satyavati ne man hi man Vyasa ka smaran kiya
Aur Vyasa turant prakat ho gaye — bina kisi ko pata chale.

🤍 Maa–Putra Milan

Satyavati ne Vyasa ko gale lagaya, aansu bahaaye

Vyasa ne unhe shaant kiya aur kaha:

“Aapka aadesh poora karne aaya hoon.”

Ritual ke baad Satyavati ne kaha:

“Tum mere bade putra ho, Vicitravirya chhota.
Bhishma satya ke kaaran raj aur santaan tyag chuke hain.
Isliye vansh-raksha tumhara kartavya hai.”

⚖️ Niyoga ka Niyam (Vyasa ki Shartein)

Vyasa bole:

“Main dharm ke liye taiyaar hoon”

“Par ek saal ka vrat patniyon ko rakhna hoga”

“Bina shuddhi ke koi mere paas nahi aa sakti”

Satyavati boli:

“Rajya bina raja ke nasht ho jaata hai
Isliye der nahi ho sakti.”

🔥 Vyasa ki Kathor Shart

Vyasa ne spasht kaha:

“Agar abhi santaan chahiye,
to patniyon ko meri kathor roop, gandh aur bhayanak ves sahna hoga.
Yahi unki tapasya hogi.
Jo sah legi, wahi uttam putra ko janm degi.”

👑 Ambika ko Bulawa

Vyasa ne kaha:

“Kosala ki rajkumari (Ambika)
shuddh vastra aur aabhooshan pehen kar
apne kaksh mein meri pratiksha kare.”

Vyasa adrishya ho gaye.

🕊️ Satyavati ka Ambika se Anurodh

Satyavati ne Ambika se kaha:

“Yeh dharma ke viruddh nahi”

“Bharata vansh tum par nirbhar hai”

“Tumhara putra Indra saman tejashvi raja hoga”

Bahut mushkil se Ambika ne sammati di.

🎉 Daan–Punya aur Yagya

Brahmanon ko bhojan

Rishiyon ka satkaar

Rajya mein dharmic taiyaari

🌼 Is Section ki Seekh

🔱 Niyoga aapatkaal ka dharm tha, kaamna ka nahi

⚖️ Vansh-raksha raj-dharma ka mool hai

🧘 Tapasya sirf van mein nahi, kartavya mein bhi hoti hai

👁️ Bahar ka roop nahi, man ki sthirata santaan ka bhavishya tay karti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.42
        with st.expander("Section 1.7.42"):
            text1 = """ 
            🔱 Paristhiti (Background)

Vicitravirya ki mrityu ke baad Kuru vansh ko aage badhane ki zimmedari aayi.
Bhishma ne apni pratigya ke kaaran santaan utpann karne se inkaar kar diya.
Isliye Satyavati ne apne putra Vedavyasa ko niyog ke liye bulaya.

👶 1) Ambika se Dhritarashtra ka janm

Ambika (badi rani) ko shuddhi ke baad shayan-kaksh mein bithaya gaya

Vyasa jab aaye,

unka ugra roop, jataaye, daadhi, teekhi aankhen dekhkar

Ambika dar ke maare aankhen band kar leti hai"""
            create_image_text_layout("attached_assets/chapter1/1.7.42.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🧿 Parinaam

Vyasa ne kaha:

Putra:

10,000 haathiyon jitni shakti

mahaan raja-rishi

100 putron ka pita

Par maa ke dosh ke kaaran andha hoga

➡️ Is prakar Dhritarashtra ka janm hua —
shaktishaali, gyaani, par drishtihin.

👑 2) Ambalika se Pandu ka janm

Ambalika (chhoti rani) Vyasa ko dekhkar

bhay se peeli (pale) pad jaati hai

Vyasa bole:

“Tumhara putra Pand u kehlayega (arth: peela / feeka)”

✨ Parinaam

Pandu ka janm hua

Roop-gun se yukt, shubh lakshan

Aage chal kar Pandavon ka pita bana

🌿 3) Dasī se Vidura ka janm (sabse mahatvapurn)

Ambika dobara niyog ke liye mana kar deti hai

Apni jagah:

ek sundar, vinamra, sanskari dasi ko bhej deti hai

🙏 Vyasa prasann hote hain

Vyasa ne kaha:

“Tu ab dasi nahi rahegi”

“Tera putra:

mahaan buddhimaan

dharm aur rajneeti ka gyata

sabse gyaani hoga”

➡️ Is prakar Vidura ka janm hua

⚖️ Vidura ka vishesh mahattva

Dhritarashtra aur Pandu ka bhai

kaam-krodh se mukt

Rajneeti, nyay, dharm ka mahaan gyaata

Dharamraj Yama ka avtar,
jo Rishi Mandavya ke shaap se dharti par aaye

👉 Isi liye Vidura:

hamesha satya aur dharm bolta hai

Duryodhan jaise logon ko bhi nidar updesh deta hai

🧬 Vansh-Saral Rekha

Vyasa + Ambika → Dhritarashtra (andha)

Vyasa + Ambalika → Pandu (peela, par veer)

Vyasa + Dasi → Vidura (maha-gyani)

📜 Gahra Arth (Hidden Dharma Message)

Mann ki sthiti santaan par prabhav daalti hai

Bhay → andhapan

Kampan → durbalta

Vinamrata → mahagyaan

Janm se nahi, gun se mahanata hoti hai

Raja ke ghar janme Dhritarashtra–Pandu se

Dasi ka putra Vidura adhik mahan nikla

Dharma ka vansh sharir se nahi, charitra se chalta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.43
        with st.expander("Section 1.7.43"):
            text1 = """ 
            🌿 Ek Mahaan Rishi

Bahut pehle ki baat hai.
Ek Brahmana rishi the — Mandavya Rishi.
Woh satya, dharma aur tapasya mein poori tarah leen the.

Rishi Mandavya:

Apne ashram ke bahar ped ke neeche baithte the

Haath upar uthaye,

maun vrat (bilkul chup rehna) ka palan karte the

Saalon tak bina bole tapasya karte rahe

Unka mann bilkul shant tha.
Unka hriday pavitra tha. 🌸"""
            create_image_text_layout("attached_assets/chapter1/1.7.43.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🗡️ Chor aur Galatfehmi

Ek din achanak:

Kuch chor loot ka samaan lekar bhagte hue aaye

Raja ke sipahi unka peecha kar rahe the

Dar ke maare:

Choron ne ashram ke paas hi loot chhupa di

Aur idhar-udhar chup gaye

Tabhi sipahi aa gaye.

❓ Sipahiyon ka Sawaal

Sipahiyon ne Mandavya Rishi ko dekha.
Woh bole:

“Hey Brahman!
Chor kis taraf gaye?
Bata do taaki hum unhe pakad saken.”

Par Rishi Mandavya:

Maun vrat mein the

Na sach bole

Na jhooth bole

Bilkul chup rahe

⚖️ Anyay (Injustice)

Sipahiyon ne ashram ki talashi li.
Unhe:

Chor bhi mil gaye

Loot ka samaan bhi mil gaya

Par galat soch ke kaaran:

Sipahiyon ne socha

“Yeh Rishi bhi inka saathi hoga”

👉 Bina sach jaane,
👉 Bina poori jaanch,

Unhone:

Rishi ko bhi pakad liya

Choron ke saath raja ke saamne le gaye

😢 Bhayanak Saza

Raja ne bhi bina dhyaan diye:

Rishi ko choron ke saath saja suna di

Sipahiyon ne:

Mandavya Rishi ko suli par chadha diya (impale kar diya)

Par ek chamatkaar hua ✨

🔥 Tapasya ki Shakti

Rishi mara nahi

Na khaya, na piya

Fir bhi zinda rahe

Unki tapasya itni shaktishaali thi ki:

Unhone apni pran-shakti se jeevan bachaya

Raat ke samay:

Anya mahan rishi

pakshiyon ka roop lekar aaye

Unhone Mandavya Rishi ko dekha:

Suli par bhi dhyaan mein leen

Chehre par shanti

Mann mein krodh nahi

🕊️ Rishiyon ka Prashn

Dusre rishi dukhi ho gaye.
Unhone poocha:

“Hey Mahatma,
Aapka kaunsa paap tha
jiske kaaran aapko itni kathor saja mili?”

Mandavya Rishi:

Ab bhi shaant the

Par is anyay ne dharma ka ek bada prashn khada kar diya

👉 Yahin se Dharmaraj ka shaap shuru hota hai,
jo aage chal kar Vidura ke janm ka kaaran banta hai…

🌼 Moral (Seekh)

Chup rehna hamesha galat nahi hota,
par bina samjhe faisla lena galat hota hai

Satya aur dharma ko pehchaan zaroori hai,
sirf vesh ya sthiti se nyay nahi hota

Anyay chahe raja se ho ya praja se,
uska phal milta hi milta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.44
        with st.expander("Section 1.7.44"):
            text1 = """ 
            🌿 Rishi ka Shant Uttar

Jab dusre rishiyon ne poocha,
“Yeh sab kis galti ka phal hai?”

Tab Mandavya Rishi bole:

“Isme main kisi aur ko dosh nahi deta.
Shayad yeh mere hi karm ka phal hai.”

Unke shabd shant the.
Unke mann mein krodh nahi, sirf samyak soch thi."""
            create_image_text_layout("attached_assets/chapter1/1.7.44.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            👑 Raja ka Pachhtawa

Udhar:

Raja ke sipahiyon ne dekha

Rishi abhi bhi zinda hain

Yeh sunkar:

Raja ghabra gaya

Apne mantriyon ke saath Rishi ke paas aaya

Raja ne vinamr hokar kaha:

“Hey Mahaan Rishi,
Maine agyaan mein aapko dand diya.
Mujhe maaf kar dijiye.”

Mandavya Rishi:

Krodhit nahi hue

Raja ko kshama kar diya

🪵 Suli ka Tukda

Raja ne:

Rishi ko suli se nikaalne ki koshish ki

Par poori tarah nikal nahi paaya

Isliye:

Suli ka ek hissa kaat diya

Thoda sa hissa Rishi ke sharir ke andar reh gaya

Is haal mein bhi:

Rishi tapasya karte rahe

Bade-bade lok jeet liye

Isliye unka naam pada:
👉 Ani-Mandavya
(jinke sharir mein suli ka hissa tha)

⚖️ Dharmaraj se Sawal

Ek din Ani-Mandavya:

Dharmaraj (Yama) ke paas gaye

Aur poocha:

“Maine kaunsa paap kiya
jiske liye mujhe itna bada dand mila?”

Dharmaraj bole:

“Ek baar tumne
ek chhote keede ko ghaas mein chhed diya tha.
Yeh usi ka phal hai.”

❗ Rishi ka Virodh

Mandavya Rishi ne poocha:

“Yeh maine kab kiya?”

Dharmaraj bole:

“Tum bachpan mein the.”

Tab Rishi bole:

“Bachcha jab 12–14 saal se chhota ho,
uske karm ko paap nahi maana ja sakta.

Itne chhote karm ke liye
itna bada dand anyay hai.”

🔥 Shaap aur Naya Niyam

Mandavya Rishi ne kaha:

“Is anyay ke kaaran,
tumhe manushya lok mein
Shudra yoni mein janm lena hoga.

Aur aaj se yeh niyam rahega:

14 saal se neeche ka karm → paap nahi

14 saal ke baad → karm ka phal milega”

🌟 Vidura ka Janm

Is shaap ke kaaran:

Dharmaraj ne Vidura ke roop mein janm liya

Vidura:

Bahut buddhiman the

Neeti, dharma aur rajneeti jaante the

Lobha aur krodh se door

Hamesha Kuru vansh ke hit ke baare mein sochte the

🌼 Moral (Seekh)

Nyay bina samjhe dena paap hai

Bachpan ke karm aur samajh mein farq hota hai

Dharma bhi galti kare to uska phal milta hai

Vidura jaise log janm se nahi, karm se mahan bante hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.45
        with st.expander("Section 1.7.45"):
            text1 = """ 
            🌸 Teen Rajkumaron ke Janm se Badlav

Jaise hi Dhritarashtra, Pandu aur Vidura ka janm hua,
Kurujangala, Kurukshetra aur poora Kuru desh khushiyon se bhar gaya।

Zameen ne acchi fasal deni shuru ki

Phal meethe ho gaye

Phool mehkaane lage

Baadal time par baarish karne lage

Gaay-bail khush the 🐄
Panchhi aur jaanwar bhi anand mein the 🕊️"""
            create_image_text_layout("attached_assets/chapter1/1.7.45.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🏙️ Khushhaal Sheher aur Log

Sheher aur gaon:

Vyapari, kalakar, shilpi se bhar gaye

Bazaar zinda aur rangeen ho gaye

Log:

Sahasik the

Imaandaar the

Padhe-likhe the

Aur sabse badi baat — khush the

Na chor the ❌
Na paapi log ❌

Lagta tha jaise
✨ Satya Yug wapas aa gaya ho ✨

❤️ Prem, Satya aur Dharma

Log:

Ek-doosre se prem karte the

Yagya, daan aur satya mein vishwas rakhte the

Na:

Ghamand ❌

Gussa ❌

Laalach ❌

Sirf:

Saaf mann

Nirdosh khel

Sachi khushi 😊

🏰 Hastinapur ka Vaibhav

Kuru rajdhani Hastinapur:

Samundar ki tarah bhari hui

Bade-bade mahal

Unche dwar aur toran

Bilkul lagta tha jaise
✨ Doosri Amaravati ✨

Log:

Nadiyon, talab aur bageechon mein ghoomte

Utsav aur utsah se jeete

🌾 Poore Desh Mein Samriddhi

Poore rajya mein:

Na koi kanjoos tha

Na koi vidhwa stree

Kuan aur talab hamesha bhare rehte

Rishi aur Brahman ke ghar bhi dhan se poore the

Har taraf:
🎉 Utsav hi utsav 🎉

👑 Bhishma ka Shasan

Bhishma:

Rajya ko dharma se chalate the

Har jagah yagya-stambh khade the

Dharma ka chakra aisa chala ki:

Dusre rajyon ke log bhi
apna ghar chhod kar
Kuru desh mein basne lage

👦 Teen Rajkumaron ki Shiksha

Dhritarashtra, Pandu aur Vidura:

Bhishma ne unhe
apne hi putron jaise pala

Unhone seekha:

Vedas

Vrat aur niyam

Dhanurvidya 🏹

Ghudsawari 🐎

Gada, talwar aur dhal

Hathi yudh 🐘

Neeti aur rajdharma

🌟 Teenon ki Visheshata

Pandu → Dhanurvidya mein sabse aage

Dhritarashtra → Shareerik shakti mein sabse balwaan

Vidura → Dharma, neeti aur gyaan mein sabse mahaan

Teenon lokon mein:
👉 Vidura jaisa dharmgyani koi nahi tha

🏆 Lokpriya Kahawat

Har jagah yeh baat chal padi:

Maaon mein → Kashi ki rajkumariyaan shreshth

Deshon mein → Kurujangala shreshth

Dharmiyon mein → Vidura shreshth

Shehron mein → Hastinapur shreshth

👑 Raja Kaun Bana?

Pandu raja bane

Dhritarashtra andhe hone ke kaaran raja nahi bane

Vidura Shudra janm ke kaaran raja nahi bane

🌿 Aage Kya?

Ek din:

Mahaan Bhishma

Neeti aur satya ke gyani Vidura se

Rajdharma par baat karte hain…

👉 Wahin se aage ki kahani shuru hoti hai…

🌼 Moral (Seekh)

Achha shasan poore desh ko swarg bana deta hai

Shakti, kala aur gyaan — teenon zaroori hain

Janm se nahi, gun se mahan banaya jaata hai

Dharma se rajya chale, to sab khush rehte hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.46
        with st.expander("Section 1.7.46"):
            text1 = """ 
            Section CX — Kuru Vansh ke Vivah aur Gandhari ka Vrat
            👑 Bhishma ka Soch-vichaar

Bhishma ne Vidura se kaha:

“Hamare Kuru vansh ne hamesha dharma aur gunon ke saath raj kiya hai.
Is vansh ko Vyasa, Satyavati aur maine milkar zinda rakha hai, taaki yeh khatam na ho.

Ab zaroori hai ki yeh vansh
🌊 samundar ki tarah phir se phail jaaye.”

Bhishma bole:
“Teen rajkumariyan hain jo is vansh ke layak hain:

Yadava vansh ki rajkumari

Gandhara raja Suvala ki beti

Madra desh ki rajkumari

Teeno sundar hain, shuddh vansh ki hain, aur hamare liye uchit hain.
Tum kya kehte ho?”"""
            create_image_text_layout("attached_assets/chapter1/1.7.46.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🧠 Vidura ka Vinamr Uttar

Vidura ne shant swar mein kaha:

“Pitashree,
Aap hi hamare pita, mata aur guru ho.
Jo aapko sahi lage, wahi hamare liye sahi hai.”

👉 Yeh tha Vidura ka vinay aur samarpan.

🌸 Gandhari ka Vardaan

Thode samay baad, Bhishma ne Brahmanon se suna:

👉 Gandhari, jo Gandhara raja Suvala ki beti thi,
ne Bhagwan Shiv ki bhakti karke vardaan paaya tha:

✨ “Tumhe sau putron ka var milega.” ✨

Yeh sunkar Bhishma ne turant
Gandhara desh mein sandesh bheja.

🤝 Vivah ka Nirnay

Raja Suvala pehle hichkichaaye,
kyunki Dhritarashtra andhe the.

Lekin phir unhone socha:

Kuru vansh ka maan

Unki maryada

Unka achar-vyavhaar

Aur apni sundar aur pavitra beti Gandhari
Dhritarashtra ko dene ka nirnay liya.

🕊️ Gandhari ka Mahaan Tyag

Jab Gandhari ko pata chala:

Unke pati andhe hain

Mata-pita ne vivah sweekar kar liya hai

Toh unhone ek adbhut nirnay liya:

👉 Unhone apni aankhon par patti baandh li
Aur kaha:
“Main bhi wahi dekhoongi
jo mere pati dekh paate hain.”

🌼 Yeh tha prem, samman aur samarpan ka shikhar.

🎉 Shaadi ka Utsav

Shakuni, Gandhari ka bhai:

Apni behen ko Kuru rajya laya

Vidhi-vidhan se uska daan kiya

Bhishma ke nirdeshan mein:

Shaadi dhoom-dhaam se hui

Kuru vansh ne Gandhari ka
bade samman se swagat kiya

Shaadi ke baad:

Shakuni uphaar dekar

Bhishma ko pranam karke

Apne desh laut gaye

🌺 Gandhari ka Acharan

Gandhari:

Sab Kuruvanshiyon ko
apne shishtachar se prasann karti thi

Hamesha pati-vrata rahi

Bade logon ka samman karti rahi

👉 Itni pavitra thi ki
apne pati ke alawa
kisi purush ka naam bhi nahi leti thi

🌼 Moral (Seekh)

Tyag aur prem se rishton ko pavitra banaya jaata hai

Sacha saath sukh-dukh dono mein hota hai

Vansh ki shakti gun aur sanskaar se hoti hai

Vinay aur shraddha se bade faisle sahi hote hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.47
        with st.expander("Section 1.7.47"):
            text1 = """ 
            Is section mein Karna ke janm ka rahasya bataya gaya hai.

Pritha (Kunti) ka parichay

Yadava kul mein Sura naam ka raja tha, jo Vasudeva (Shri Krishna ke pita) ka pita tha

Sura ki beti thi Pritha, jo baad mein Kunti ke naam se prasiddh hui

Sura ne apni beti Pritha ko apne nishsantaan mitra Kuntibhoja ko godh de diya

Kunti apne adoptive pita ke ghar Brahmanon aur atithiyon ki seva karti thi."""
            create_image_text_layout("attached_assets/chapter1/1.7.47.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Durvasa ka vardaan

Ek din Rishi Durvasa Kunti ki seva se prasann ho gaye

Unhone Kunti ko ek mantra diya:

“Is mantra se tum kisi bhi devta ko bula sakti ho,
aur woh devta tumhe santaan dega.”

Durvasa ko bhavishya dikh raha tha—
ki Pandu ke shraap ke baad yeh mantra kaam aayega.

Kunti ki jijnasa aur Surya ka aagman

Kunti ne sirf mantra ki shakti jaanchne ke liye
Surya dev (Arka / Vivasvat) ko bula liya

Surya dev prakat ho gaye

Kunti darr gayi aur boli:

“Maine sirf mantra pariksha ke liye bulaya tha,
mujhe maaf kijiye.”

Surya ne kaha:

“Devta ko bulaana vyarth nahi jaata.
Tumhari pukar ka phal milna hi chahiye.”

Karna ka janm

Surya dev ke yog se Karna ka janm hua

Karna:

janm se hi kavach (armor) aur kundal ke saath paida hua

adbhut tej aur saundarya se yukt tha

Surya dev ne Kunti ko phir se kanya bana diya
aur swarg chale gaye.

Kunti ka kathin nirnay

Kunti:

samaj aur parivaar ke darr se

is bachche ko apna nahi paayi

Bahut dukh ke saath:

Kunti ne Karna ko tokri mein rakhkar nadi mein chhod diya

Radha aur Adhiratha

Radha aur uske pati Adhiratha (Sut jati) ne
nadi se bachche ko uthaya

Use apna beta maana

Naam diya: Vasusena

Baad mein woh Karna ke naam se prasiddh hua

Karna ka daan aur Indra

Karna:

Surya ki roz pooja karta tha

daan mein kabhi “na” nahi kehta tha

Indra ne:

Brahman ka roop dharan karke

Karna se uska janm-jaat kavach aur kundal maang liya

Karna ne bina soche:

apna kavach kaat kar daan de diya

Prasann hokar Indra ne diya:

Vasavi Shakti

“Is shastra se tum jis shatru ko chahoge,
woh avashya marega (sirf ek baar).”

Isi kaaran Vasusena ka naam pada:
👉 Karna (jo apna kavach kaat de)

Moral (Seekh) 🌱

Karna janm se mahaan tha, par uska jeevan tyag aur sangharsh se bhara raha

Daan aur kartavya uske liye janm se bada tha

Kunti ka nirnay galat nahi, par majboori bhara tha

Mahabharata sikhata hai:

“Dharm hamesha seedha nahi hota,
par satya aur tyag hamesha mahaan hote hain.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.48
        with st.expander("Section 1.7.48"):
            text1 = """ 
            Kunti, jiska asli naam Pritha tha,
Kuntibhoja ki beti thi.
Uski aankhen badi aur sundar thi.
Woh khoobsurat thi, gunon se bhari thi,
aur dharm ke raaste par chalne wali thi.

Par ek ajeeb baat hui.
Itni qualities hone ke baad bhi,
kisi raja ne uska haath nahi manga.

Yeh dekhkar Kuntibhoja ko chinta hui.
Unhone faisla liya:

“Main swayamvar rakhunga.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.48.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Swayamvar ka din

Bahut se raja aur rajkumar aaye.
Sab apne shaan-shaukat ke saath baithe the.

Jab Kunti sabha mein aayi,
toh uski nazar ek raja par jaakar ruk gayi.

Woh the Raja Pandu —
Bharat vansh ke shresth yoddha.
Sher jaise garv se khade.
Chaudhi chhaati, tez aankhen,
aur sabse alag chamak.

Kunti ka mann hil gaya.
Dil tez dhadakne laga.
Par chehre par sharam aur maryada thi.

Dheere-dheere chal kar,
usne varmala Pandu ke gale mein daal di.

Pandu ka chayan

Sab raja samajh gaye.
Kunti ne Pandu ko chuna tha.

Baaki raja bina gussa kiye,
shaanti se apne rajya laut gaye.

Vivah aur naya jeevan

Kuntibhoja ne dharm ke saath
Kunti aur Pandu ka vivaah karwaya.

Dono saath aise lag rahe the
jaise Indra aur Paulomi swarg mein.

Vivah ke baad:

Kuntibhoja ne Pandu ko bahut dhan diya

Aashirvaad ke saath unhe vida kiya

Pandu apni sena, jhande,
aur Brahmanon ke vedic mantraon ke saath
apni rajdhani pahunche.

Aur wahan:

Pandu ne Kunti ko rani ke roop mein sthapit kiya

Moral (Seekh) 🌼

Sahi vyakti ka chayan shor mein nahi,
dil ki shanti mein hota hai

Kunti ne roop nahi,
veerata aur dharm dekha

Swayamvar sikhata hai:

“Apni zindagi ka faisla
khud soch samajh kar lena chahiye.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.49
        with st.expander("Section 1.7.49"):
            text1 = """ 
            Kuch samay baad,
Bhishma, jo Santanu ke buddhimaan putra the,
ne socha ki Pandu ki doosri shaadi honi chahiye.

Woh bade rishiyon, Brahmanon
aur chaar tarah ki sena ke saath
Madra desh gaye.

Madra ke Raja se milan

Madra ke raja ne Bhishma ka
bahut aadar se swagat kiya.
Unhe baithne ko safed aasan diya,
pair dhone ka jal diya,
aur poora samman diya."""
            create_image_text_layout("attached_assets/chapter1/1.7.49.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Phir Bhishma ne shaant swar mein kaha:

“Aapki behen Madri
sundar, gunwaan aur pavitra hai.
Main use Pandu ke liye maangne aaya hoon.”

Madra ke raja bole:

“Kurus ke saath rishta mere liye garv ki baat hai.
Par hamare ghar ki ek parampara hai.
Usse todna mere liye possible nahi.”

Bhishma muskuraye.
Unhone kaha:

“Parampara ka sammaan hi sabse bada dharm hai.”

Madri ka vivah

Bhishma ne Madra ke raja ko
bahut saare ratna, sona, kapde, haathi aur ghode diye.

Khushi se Madra ke raja ne
apni behen Madri ko Pandu ko arpit kar diya.

Shubh din aur shubh muhurat mein,
Pandu aur Madri ka vivaah hua.

Pandu ne Madri ko
apne mahal mein rani ke roop mein sthapit kiya.

Pandu ka Vijay Abhiyan

Kuch din baad,
Pandu ne faisla kiya:

“Ab rajya ko majboot banana hai.”

Bhishma aur badon ko pranam karke,
aashirvaad lekar,
woh vishaal sena ke saath yuddh yatra par nikle.

Pandu ne:

Dakait rajyon ko haraya

Magadha ke shaktishaali raja ko jeeta

Mithila, Kasi, Sumbha, Pundra jaise deshon ko vash mein kiya

Jahan-jahan Pandu gaye,
wahan Kuru vansh ka yash failta gaya.

Sab raja Pandu ke saamne
haath jod kar khade hue
aur bhent mein:

sona–chandi

haathi–ghode

ratna, kapde aur anaj laaye

Vijayi Raja ka Swagat

Jab Pandu jeet kar
Hastinapur laute,
toh poora shehar khushi se bhar gaya.

Bhishma sabke aage khade the.
Pandu ne unke charan chhuye.

Bhishma ne Pandu ko gale lagaya.
Unki aankhon mein khushi ke aansu the.

Nagade baje,
shankh goonje,
aur Pandu vijayi raja ke roop mein
rajdhani mein pravesh kiya.

Conclusion / Moral (Seekh) 🌼

Parampara aur sammaan rishton ko mazboot banate hain

Shakti ka sahi upyog rajya ko samriddh karta hai

Vijay ke baad vinamrata hi asli mahaanta hai

Pandu ne dikhaya:

“Achha raja wahi hota hai
jo jeet ke baad bhi jhukna jaane.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.50
        with st.expander("Section 1.7.50"):
            text1 = """ 
            Jab Pandu yuddh se vijay lekar laute,
toh Dhritarashtra ke kehne par,
unhone apni kamayi hui sampatti
Bhishma, Dadi Satyavati,
aur apni maayon ko arpit ki.

Unhone Vidura ko bhi
uska hissa bheja.
Aur apne baaki rishtedaaron ko bhi
prem se daan diya."""
            create_image_text_layout("attached_assets/chapter1/1.7.50.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Parivaar ki Khushi

Bhishma, Satyavati
aur Kosala ki raniyan
sab Pandu ke daan se khush hue.

Ambalika,
apne veer putra Pandu ko gale lagakar
utni hi prasann hui
jaise Indra ki rani apne putra Jayanta ko dekh kar hoti hai.

Usi dhan se
Dhritarashtra ne paanch maha-yagya karaye.
In yagyon mein
hazaaron Brahmanon ko daan diya gaya.

Poora rajya
punya aur samriddhi se bhar gaya.

Pandu ka Van ki Ore Jaana

Kuch samay baad,
Pandu ne ek bada nirnay liya.

Rajmahal ke sukh,
narangi shaiyya aur aishwarya chhod kar,
woh Kunti aur Madri ke saath van chale gaye.

Himalaya ke dakshini dhalan par,
sala ke ghane vrikshon ke beech,
ek sundar aur shaant jagah par
unhone apna nivaas banaya.

Wahan Pandu:

mrigaya karte

prakriti ke beech jeete

aur van ke jeevan ko apnate

Pandu apni dono patniyon ke saath
aise lagte the
jaise Airavata haathi
do sundar haathiniyon ke saath ghoom raha ho.

Van ke log
unhe devta samaan maante the.

Rajya ki Chinta

Dhritarashtra ne aadesh diya
ki Pandu ko van mein bhi
kisi cheez ki kami na ho.

Isliye rajya se
unke liye
sabhi sukh-suvidhaon ka prabandh hota raha.

Vidura ka Grihastha Jeevan

Isi beech,
Bhishma ko pata chala
ki Raja Devaka ki ek beti hai,
jo gunwaan aur sundar hai.

Bhishma use le aaye
aur Vidura se vivaah karaya.

Vidura ne uske saath
grihastha dharm nibhaya
aur unke kai santaan hui
jo Vidura jaise gyaani aur vinamr bane.

Conclusion / Moral (Seekh) 🌿

Sampatti ka sahi upyog parivaar aur samaj ko jodta hai

Rajya hone ke baad bhi tyaag mahaan logon ki pehchaan hota hai

Van jeevan manushya ko vinamr aur prakriti ke kareeb karta hai

Vidura ka jeevan sikhaata hai:

“Janm se nahi,
gun aur buddhi se mahaanta milti hai.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.51
        with st.expander("Section 1.7.51"):
            text1 = """ 
            Yeh kahani Kuru vansh ke do gharon ki hai.
Ek taraf Dhritarashtra aur Gandhari,
dusri taraf Pandu, Kunti aur Madri.

Gandhari ka Vardaan

Ek din Maharshi Vyasa
thake aur bhookhe Gandhari ke mahal aaye.

Gandhari ne unka
bahut prem aur shraddha se seva ki.

Vyasa khush hue.
Unhone vardaan diya:

👉 “Tumhe 100 putra honge,
sab apne pita jaise shaktishaali.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.51.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Lambi Pratiksha aur Dukh

Samay beetta gaya.
Do saal ho gaye,
par Gandhari ka prasav nahi hua.

Isi beech use pata chala
ki Kunti ne ek tejasvi putra ko janam diya.

Dukh aur vyatha mein,
Gandhari ne gusse mein
apne garbh par zor se prahar kar diya.

Uske garbh se
loha jaise kathor maans ka gola nikla.

Gandhari toot gayi.
Usne kaha:
“Yeh mere 100 putra kaise ho sakte hain?”

Vyasa ka Chamatkar

Vyasa turant aaye.
Unhone kaha:

👉 “Mera vardaan kabhi vyarth nahi hota.”

Unhone kaha:

100 matke lao

sab mein ghrit (ghee) bharo

is maans ke gole ko
thande paani se secho

Kuch samay baad,
woh gola 101 tukdon mein bat gaya.

Har tukda
ek matke mein rakha gaya.

Vyasa bole:
👉 “Do saal baad matke kholna.”

Duryodhana ka Janm

Sabse pehle Duryodhana paida hua.

Usi din
Bhima ka bhi janm hua.

Par Duryodhana ke janm par
kuch ashubh sanket hue:

ghadhe jaisi awaaz

siyaron aur kauon ka chillana

tez aandhi

aag lagna

Vidura ki Salah

Bhishma aur Vidura ko bulaya gaya.

Vidura ne spasht kaha:

👉 “Yeh balak vansh ka vinaash karega.”
👉 “Isse tyagna hi dharm hai.”

Par Dhritarashtra ka pita-hṛiday
maan nahi saka.

Usne apne putra ko nahi chhoda.

100 Putra aur 1 Putri

Ek mahine ke andar:

100 putra

aur 1 putri (Duhshala) paida hui

Saath hi,
Dhritarashtra ka
Vaisya daasi se ek putra bhi hua
jiska naam tha Yuyutsu.

Pandu ke 5 Putra

Dusri taraf,
Pandu par rishi ka shraap tha
isliye unke putra
devtaon ke vardaan se hue:

Yudhishthira – Dharma se

Bhima – Vayu se

Arjuna – Indra se

Nakula – Ashwini Kumar se

Sahadeva – Ashwini Kumar se

Yeh paanchon
mahaan rathi aur dharmic the."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.52
        with st.expander("Section 1.7.52"):
            text1 = """ 
            Section CXVI – Duhsala ka janm (Gandhari ki putri)

(Sambhava Parva – spashtikaran aur saar)

Is prashn mein Janamejaya ne bilkul sahi jigyāsa rakhi:
jab Vyasa ne Gandhari ko 100 putron ka var diya aur maans-pind 100 bhaagon mein baanta gaya, to ek putri Duhsala ka janm kaise hua?

Vaisampayana ka uttar (mool ghatna)

Jab Vyasa us maans-pind ko jal chhidak kar tukdon mein baant rahe the aur 100 bhaag ghee ke ghadon mein rakhe ja rahe the,

tab Gandhari ke man mein putri-bhāv udaya hua.

Gandhari ne man hi man prarthana ki:

“Mujhe 100 putra milenge—yeh nishchit hai.

Par agar ek putri bhi mil jaaye, to mere pati ko daamād aur pautron ke saath woh punya-lok prapt hon.

Yadi maine tapasya, daan, hom, aur gurujanon ki seva ki hai, to uska phal mujhe ek putri ke roop mein mile.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.52.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Vyasa ka karuna-may nirnay

Jab 100 tukde gin kar rakh diye gaye,
to Vyasa ne kaha:

“Yeh tumhare 100 putra hain—mera vachan asatya nahi hua.
Par yeh ek atirikt bhaag tumhari ichchha ke anuroop putri ke liye hai.”

Us 101ve tukde ko alag ghee ke ghade mein rakha gaya.

Parinaam

Isi atirikt bhaag se Duhsala ka janm hua—
Gandhari ki ekmatra putri, jo 100 putron se chhoti thi.

Is prasang ka saar (Key Takeaways)

Vyasa ka var satya raha—100 putra hue.

Gandhari ke man ki ichchha aur punya se ek putri ka bhi janm sambhav hua.

Yeh ghatna putri-mahatva ko darshati hai—daamād aur pautron ke saath grihastha-punya ki parampara."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.53
        with st.expander("Section 1.7.53"):
            text1 = """ 
            Section CXVII – Dhritarashtra ke putron ke naam (janm-kram ke anusar)

(Sambhava Parva – vyavasthit samjhaav)

Is prasang mein Janamejaya ne Vaisampayana se seedha prashn kiya ki
Dhritarashtra ke putron ke janm-kram ke anusar naam bataye jaayen.

Mool soochi ka saar (samajhne layak tareeke se)

Dhritarashtra ke kul 100 putra hue, jo sab Atirathi,
shastr-vidya mein nipun, aur Vedo ke gyata the.

Inke naam janm ke kram mein ginaaye gaye hain—
jismein sabse pehle Duryodhana aur baad mein anya putra aate hain.

Inke beech Yuyutsu ka naam bhi aata hai (jo Vaishya maata se janme the).

Naam-soochi mein kuchh naam dohraye hue dikhte hain
(jaise Karna, Bhima), jo Mahabharata ke vibhinna paath-antar ka parinaam hai
— ise vidvaan bhi sweekar karte hain.

Mahattvapurn baat:
Yeh poori soochi paramparaagat paathon mein aati hai,
aur iska uddeshya kul-parampara aur vansh-vistaar dikhana hai,
na ki har naam ko aaj ke arth mein alag-alag pehchaan dena."""
            create_image_text_layout("attached_assets/chapter1/1.7.53.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Duhsala – ekmaatra putri

In 100 putron ke atirikt, ek putri bhi thi:

👉 Duhsala

Dhritarashtra ne samay aane par, vidhi-vidhaan se,
Duhsala ka vivaah Jayadratha
(Sindhu desh ke raja) se kiya.

Is adhyaay ka tattvik sandesh

Kaurav vansh sankhya aur shakti mein bahut bada tha.

Fir bhi, keval sankhya ya shastra-bal hi dharm aur vijay ka maap-dand nahi hota—
aage jaakar Mahabharata ka yahi mool sandesh prakat hota hai.

Duhsala ka vivaah Jayadratha se aage chal kar
Mahabharata ke gahan aur dukhad ghatna-kramon se juda hota hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.54
        with st.expander("Section 1.7.54"):
            text1 = """ 
            Section CXVIII – Pandu par laga shraap (Hinglish Moral Story Version)

Janamejaya ne vinamrta se kaha:
“Hey Brahmana, aapne Dhritarashtra ke putron ke baare mein sab bata diya.
Ab mujhe Pandavon ke janm aur unke jeevan ke baare mein bhi sunna hai.
Batayiye, unki kahani kaise shuru hui?”

Vaisampayana ne kaha:
Pandu aur jungle ka ghatna-kram

Ek din Pandu Himalaya ke dakshini pahaadon mein jungle ghoom rahe the.
Wahan hiran, jangli jaanwar aur shaant van-jeevan tha.

Achaanak Pandu ne dekha—
ek hiran aur hiranni saath mein the.
Bina zyada soche, Pandu ne apne teer chala diye.

Dono gir pade.

Par tab kuchh ajeeb hua…"""
            create_image_text_layout("attached_assets/chapter1/1.7.54.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Hiran bol utha!

Girte hi woh hiran insaan ki awaaz mein rone laga.
Usne Pandu se kaha:

“Hey Raja, tumne bahut badi galti kar di.
Main koi saadharan hiran nahi hoon.
Main ek Rishi hoon—
Kindama,
jo apni patni ke saath hiran ke roop mein yahan reh raha tha.”

Pandu sann reh gaye.

Rishi Kindama ka updesh

Rishi ne dukh bhare shabdon mein kaha:

“Raja, shikar karna tumhara adhikar ho sakta hai,
lekin sambhog ke samay kisi jeev ko maarna
adharm hai.

Tum khud jaante ho ki
yeh samay har jeev ke liye pavitra hota hai.

Tum Paurav vansh ke ho—
jahan dharm aur maryada ka maan hota hai.
Phir tumne aisa kaam kaise kiya?”

Pandu ne tark diya,
“Raja to hamesha shikar karte hain.”

Par Rishi ne shaant par dridh awaaz mein kaha:

“Main is baat par krodhit nahi hoon
ki tumne hiran maara.
Main is baat se dukhi hoon
ki tumne samay aur maryada ka dhyaan nahi rakha.”

Shraap (Curse)

Fir Rishi Kindama ne kaha:

“Jaise tumne mujhe
sukh ke pal mein maara,
waise hi tum bhi
sukh ke pal mein hi maroge.

Jab tum apni patni ke saath
kaamna ke vash mein aaoge,
usi pal tumhari mrityu ho jaayegi.

Aur jis patni ke saath
tum us samay hoge,
wahi tumhare saath
mrityu ke baad bhi jaayegi.”

Yeh kehkar Rishi ne
pran tyag diye.

Pandu ka pashchataap

Rishi ke shabd sun kar
Pandu ka hriday toot gaya.

Unhe apni galti ka ehsaas hua

Unhone apne aap ko dosh diya

Aur tab se unka jeevan
dukh aur sanyam se bhar gaya

Yahin se Pandu ke jeevan ka
sabse bada mod shuru hota hai—
jo aage chal kar Pandavon ke janm ka kaaran banta hai.

Is kahani ka moral (Bachchon ke liye)

Shakti ke saath zimmedari aani chahiye

Har kaam ka sahi samay aur maryada hoti hai

Gusse ya jaldi mein kiya gaya kaam
jeevan bhar ka dukh de sakta hai

Dharm sirf niyam nahi, samvedna bhi hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.55
        with st.expander("Section 1.7.55"):
            text1 = """ 
            Section CXIX – Pandu ka Tyag aur Vanvaas

(Hinglish | Simple | Moral Story Tone)

Vaisampayana ne kaha:

Rishi Kindama ki mrityu ke baad,
Pandu bahut dukhi ho gaye.
Unki aankhon se aansu ruk hi nahi rahe the.
Unhone apne mann se baat ki aur bole:

Pandu ka atma-manthan

“Insaan agar achhe kul mein janm le,
phir bhi agar kaamna aur vasna ke vash mein aa jaaye,
toh wahi uske dukh ka kaaran ban jaati hai.

Mere pita Vichitravirya bhi kaamna ke kaaran
jaldi chal base the.
Aur main, Rishi Vyasa ka putra hote hue bhi,
aaj jungle mein shikar karte hue
itni badi galti kar baitha.

Lagta hai devta bhi mujhse mooh mod chuke hain.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.55.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Brahmacharya ka sankalp

Phir Pandu ne dridh nishchay kiya:

“Ab main moksha ka marg apnaunga.
Santaan ki ichha aur sansaar ke bandhano se
khud ko door kar dunga.

Main Brahmacharya ka palan karunga.
Apni indriyon ko niyantran mein rakhunga.
Sir mundwa kar, akela bhiksha maangta hua
dharti par vicharan karunga.

Na sukh se khush hounga,
na dukh se tootunga.
Gaali aur tareef dono ko ek samaan maanunga.

Jo mujhe nuksaan pahunchaye
aur jo mujhe samman de,
dono ke prati mera mann ek jaisa rahega.

Main kisi jeev ko nuksaan nahi pahunchaaunga—
chahe woh chalne wala ho,
udne wala ho,
ya ped–paudha hi kyun na ho.

Din mein sirf ek baar
5 ya 7 gharon se bhiksha maangunga.
Agar na mile, toh bhooka reh lunga,
lekin lalach nahi karunga.”

Kunti aur Madri ka vachan

Yeh sab kehkar Pandu ne
apni patniyon Kunti
aur Madri ko dekha.

Dono ne bhare mann se kaha:

“He Maharaj,
agar aap vanvaas lenge,
toh hum bhi aapke saath chalenge.

Aapke bina jeevan ka
koi arth nahi.
Agar aapne humein chhod diya,
toh hum jeevit nahi rahenge.”

Saath-saath vanvaas

Pandu ne unki baat maan li.
Unhone kaha:

“Achha, toh hum teenon saath chalenge.
Shehron ka sukh tyag kar,
pedon ki chhaal pehnenge.
Phal–mool khayenge.
Tapasya aur dhyaan mein jeevan bitayenge.”

Rajya aur dhan ka tyag

Pandu ne apna mukut, gehne, vastra,
sab kuchh Brahmanon ko daan kar diya.
Apne sevakon se kaha:

“Hastinapur jaakar sabko bata do—
Pandu apni patniyon ke saath
sab kuchh tyag kar
vanvaas ke liye nikal chuka hai.”

Sevak rone lage.
Par Pandu shaant rahe.

Vanvaas ki yatra

Pandu, Kunti aur Madri—

Nagasata parvat

Chaitraratha van

Kalakuta

Himavat

Gandhamadan parvat

jaise pavitra sthalon se guzar kar
tap aur sanyam ka jeevan jeene lage.

Wahan Rishi, Siddh aur devtaon ki raksha mein
Pandu ne kathor tapasya shuru ki.
Is kahani ka moral (Seekh)

Galti ka ehsaas ho jaaye,
toh pashchataap aur sudhaar hi sachcha raasta hai

Sanyam aur tyag se
jeevan ko nayi disha milti hai

Saath dene wale log
mushkil samay mein hi pehchaane jaate hain

Kabhi-kabhi,
vanvaas hi bhavishya ka maarg bana deta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.56
        with st.expander("Section 1.7.56"):
            text1 = """ 
            Section CXX – Pandu ki Chinta aur Vansh aage badhane ka vichaar

(Hinglish | Simple | Moral Story Tone)

Vaisampayana ne kaha:

Pandu ne kathor tapasya shuru kar di.
Unki shakti aur sanyam dekh kar
Siddha aur Charan unka bahut samman karne lage.

Pandu bilkul ghamand-rahit the.
Unka mann poori tarah niyantran mein tha.
Dheere-dheere, tapasya se
woh Brahmarshi jaise pavitra ho gaye,
chahe janm se woh Kshatriya hi the.

Kuch Rishi unhe bhai kehne lage,
kuch mitra,
aur kuch putra jaise pyaar karne lage."""
            create_image_text_layout("attached_assets/chapter1/1.7.56.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Swarg yatra ka vichaar

Ek Amavasya ke din,
kai mahaan Rishi ekatrit hue.
Woh Brahma-lok jaane ki tayyari kar rahe the.

Pandu ne poocha:
“Bhagavan Rishiyon, aap log kahan ja rahe hain?”

Rishiyon ne kaha:
“Aaj Brahma-lok mein devta, pitra aur Rishi
sab ekatrit ho rahe hain.
Hum bhi wahi ja rahe hain.”

Yeh sun kar Pandu khush ho gaye.
Woh apni dono patniyon ke saath
unke saath chalna chahte the.

Rishiyon ki chetavani

Rishiyon ne Pandu ko rokte hue kaha:

“Uttar disha mein aage jaakar
bahut kathin sthal aate hain.

Kahin hamesha barf hoti hai

Kahin itni tez baarish hoti hai

Kahin na ped-paudhe hote hain

Na jeev-jantu

Wahan sirf hawa, Siddha aur Rishi hi ja sakte hain.

Tumhari patniyan sukhi jeevan ki aadat wali hain.
Unke liye yeh yatra bahut kashtdayak hogi.
Isliye tum yahin ruk jao, Pandu.”

Pandu ka dard

Pandu dukhi ho gaye.
Unhone kaha:

“Main putrahīn hoon.
Aur bina putra ke
swarg mein pravesh nahi milta.

Mujh par mere pitr̥-rin (ancestors ka rin) baaki hai.
Agar main putra ke bina mar gaya,
toh mere pitra bhi kasht paayenge.

Insaan par chaar rin hote hain:

Devta ka – yagya se

Rishi ka – adhyayan aur tapasya se

Manushyon ka – daya aur satkarm se

Pitra ka – santaan se

Maine pehle teen rin chuka diye.
Par pitra-rin abhi baaki hai.”

Santaan ke vibhinn prakaar

Pandu ne kaha:

“Dharm-shastra mein
12 prakaar ke putra bataye gaye hain.

Agar pehla prakaar sambhav na ho,
toh agla apnaya ja sakta hai.

Mere upar shraap hai,
isliye main santaan utpann nahi kar sakta.”

Kunti se gupt baat

Phir Pandu ne apni patni
Kunti ko alag se bulaya
aur bole:

“Kunti,
putra hona bahut bada dharm hai.
Putra ke bina
daan, yagya, tapasya –
sab adhoora reh jaata hai.

Main shraap ke kaaran asamarth hoon.
Isliye main tumhe aadesh deta hoon
ki kisi mahaan aur tapasvi purush ke dwara
santaan utpann karo.

Yeh dharm ke viruddh nahi hai.
Shastra aur purane udaharan
isi baat ko sahi maante hain.”

Pandu ne ek purani kahani sunayi
jisme ek veer stree ne
apne pati ke aadesh se
Brahman ke dwara putra paaye the.

Ant mein Pandu ka vachan

Pandu bole:

“Kunti,
tum bhi wahi karo jo dharm ke anukul ho.
Isse mera pitra-rin chukega
aur vansh aage badhega.”

Is bhaag ki seekh (Moral)

Tapasya se insaan atmaik uchchai pa sakta hai

Dharm sirf niyam nahi,
samay aur paristhiti ke hisaab se vivek bhi hai

Vansh aur pitra ka rin
Bharatiya parampara mein bahut mahatvapurn hai

Kabhi-kabhi,
balidaan aur kathin faisle hi
bhavishya ka raasta kholte hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.57
        with st.expander("Section 1.7.57"):
            text1 = """ 
            Section CXXI – Kunti speaks to Pandu (Hinglish Story Rewrite)

Vaisampayana ne kaha,
Pandu ki baat sun kar
Kunti ne shaant aur vinamr swar mein jawaab diya.

Kunti boli,
“Swami, aap mujhse aisa na kahiye.
Main aapki patni hoon.
Main aapse hi judi hoon.”

Unki aankhon mein shraddha thi.
“Main sirf aapki hoon.
Mera mann, mera jeevan
sab aapko samarpit hai.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.57.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Kunti ne kaha,
“Aap dharm ke maarg par
mujhse santaan paida kar sakte hain.
Uske baad main bhi
aapke saath swarg jaungi.”

“Main kabhi sapne mein bhi
kisi aur purush ke baare mein
soch nahi sakti.
Aap se shreshth
is sansaar mein kaun ho sakta hai?”

Phir Kunti ne dheere se kaha,
“Swami, ek purani Pauranik kahani hai.
Main woh aapko sunana chahti hoon.”

Unhone kahani shuru ki.

“Bahut purane samay mein
Puru vansh mein
Vyushitasva naam ka ek raja tha.
Woh satya aur dharm ka palan karta tha.”

“Uska tej sooraj jaisa tha.
Uske baahubal das haathiyon jaise the.
Usne kai bade yagya kiye.”

“Usne chaaron dishaon ke rajao ko jeeta
aur sabki raksha ek pita jaise ki.”

“Kai yagya karke
usne brahmanon ko daan diya.
Uske jeevan mein
samriddhi aur dharm dono the.”

“Uski patni Bhadra
bahut sundar aur pavitra thi.
Dono ek-doosre se
bahut prem karte the.”

“Par atyadhik bhog ke kaaran
raja bimaar pad gaye.
Aur kuch hi dinon mein
unka dehant ho gaya.”

“Bhadra toot gayi.
Woh santaan-heen thi.
Uska dukh gehra tha.”

Bhadra roti hui boli,
“Swami ke bina
stri ka jeevan vyarth hai.
Aapke bina
ek pal bhi jeena mushkil hai.”

“Main aapke peeche aana chahti hoon.
Mujhe apne saath le chaliye.”

“Main aapki chhaaya ban kar
aapke saath chalungi.”

“Shayad kisi pichhle janm mein
maine kisi prem ko alag kiya hoga.
Isi paap ka fal
aaj mujhe mil raha hai.”

“Ab main
sukh chhod dungi.
Sirf aapko dekhne ki aasha mein
jeeti rahungi.”

Kunti ne aage kaha,
“Bhadra roti hui
apne pati ke sharir se lipat gayi.”

Tab ek adrushya awaaz aayi,
“Utho, Bhadra.
Main tumhe vardaan deta hoon.”

“Shuddhi ke baad
niyamit raat mein
tumhe santaan prapt hogi.”

Bhadra ne
vidhi ka palan kiya.
Aur usse
saat santaan prapt hui.

Kunti ne Pandu ki taraf dekha.
Unki awaaz komal thi.

“Swami,
jaise us raja ne
apni tapasya se
santaan paida ki,
waise hi aap bhi kar sakte hain.”

“Main aapki patni hoon.
Mera jeevan
aapke saath hi poora hoga.”

Kunti chup ho gayi.
Unke shabd sachche the.
Unke mann mein
shraddha aur dharm tha.

Yeh kahani
prem, vishwas aur kartavya ki
seekh deti hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.58
        with st.expander("Section 1.7.58"):
            text1 = """ 
            Section CXXII – Pandu aur Kunti ka Samvaad (Hinglish Story Rewrite)

Vaisampayana ne kaha,
Kunti ki baat sun kar
Raja Pandu ne shaant aur dharmik shabdon mein kaha.

Pandu bole,
“Kunti, tum jo keh rahi ho,
woh satya hai.
Purane samay mein
Vyushitasva ne aisa hi kiya tha.”

“Par main tumhe
purane rishiyon ke niyam batana chahta hoon.
Woh niyam
dharm par aadharit the.”

Pandu ne dheere se kaha,
“Bahut purane yug mein
striyan ghar mein band nahi hoti thi.
Woh swatantra thi.
Jahan chahein ja sakti thi.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.58.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Us samay
ek hi pati se bandhe rehna
zaroori nahi tha.
Aur ise paap nahi maana jaata tha.”

“Pashu aur pakshi
aaj bhi aise hi jeete hain.
Us yug ke rishi
is vyavahaar ko maante the.”

Pandu bole,
“Par baad mein
yeh niyam badla.
Aur yeh badla
Rishi Uddalaka ke putra
Shvetaketu ke kaaran.”

Unhone kahani sunayi.
“Ek din
Shvetaketu ne dekha
ki ek Brahman
uski maa ka haath pakad kar
use le ja raha hai.”

“Shvetaketu ko gussa aa gaya.
Par uske pita ne kaha,
‘Yeh purana niyam hai.’”

“Par Shvetaketu ne ise galat maana.
Aur usne naya niyam sthapit kiya.
Us din se
patni ka ek hi pati hona
dharm maana gaya.”

Pandu bole,
“Tab se
agar stri apne pati se hat kar chale,
toh paap maana jaata hai.”

“Isi tarah,
jo pati
pavitra patni ka apmaan kare,
woh bhi paapi hota hai.”

Pandu ne Kunti ki taraf dekha.
“Isliye, Kunti,
ab patni ka kartavya hai
ki woh pati ke aadesh ka palan kare.”

Phir Pandu bole,
“Madayanti ne bhi
apne pati ke liye
Rishi Vasishtha se
santaan prapt ki thi.”

“Aur tum jaanti ho,
hum khud bhi
Kuru vansh ko badhane ke liye
Vedvyas ke kaaran janme the.”

Unki awaaz komal ho gayi.
“Kunti,
main santaan dekhna chahta hoon.
Par main asamarth hoon.”

“Isliye main tumse
vinati karta hoon.
Mera aadesh
dharm ke viruddh nahi hai.”

“Tum kisi maha tapasvi Brahman ke dwara
santaan prapt karo.
Isse mujhe bhi
putravaan hone ka sukh milega.”

Pandu ne haath jod liye.
“Main tumse prarthana karta hoon.”

Yeh sun kar
Kunti ne vinamrata se kaha,
“Swami,
jab main kanya thi,
main apne pita ke ghar
atithiyon ki seva karti thi.”

“Ek din
Maharshi Durvasa
mere seva se prasann hue.”

“Unhone mujhe
ek mantra diya.
Us mantra se
main kisi bhi devta ko
bula sakti hoon.”

“Woh devta
mujhe santaan bhi de sakta hai.”

Kunti ne kaha,
“Swami,
aap aadesh dein.
Main kisi bhi devta ko bula sakti hoon.”

Pandu ne turant kaha,
“Kunti,
Dharm Devta ko bulao.”

“Woh sabse pavitra hain.
Unse janma putra
dharm aur satya ka paalan karega.”

“Log bhi
is karm ko paap nahi maanenge.”

Kunti ne sir jhuka diya.
“Jaise aap kahein, Swami.”

Unhone Pandu ke charanon mein
namaskar kiya.
Aur unka aadesh
maan lene ka sankalp liya.

Yahin se
Kuru vansh ke bhavishya ki
neev padti hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.59
        with st.expander("Section 1.7.59"):
            text1 = """ 
            Section CXXIII – Kunti aur Pandu ke Putron ka Janm (Hinglish Story Rewrite)

Vaisampayana ne kaha,
Janamejaya,
jab Gandhari ko garbh dharan kiye
ek saal ho chuka tha,
tab Kunti ne
Dharm Devta ka aahvan kiya.

Kunti ne yagya kiya.
Durvasa ka diya mantra japne lagi.
Mantra ke prabhav se
Dharm Devta prakat hue.
Unka rath sooraj jaisa chamak raha tha."""
            create_image_text_layout("attached_assets/chapter1/1.7.59.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Devta muskuraye aur bole,
“Kunti, kya chahiye tumhe?”

Kunti bhi muskurayi.
Boli,
“Mujhe santaan chahiye.”

Tab Dharm Devta ne
divya roop mein
Kunti ko putra diya.

Shubh samay par
ek putra ka janm hua.
Aakash se awaaz aayi,
“Yeh balak
sabse dharmik hoga.
Satya bolne wala hoga.
Prithvi par raaj karega.”

“Iska naam
Yudhishthira hoga.”

Pandu bahut prasann hue.
Par phir bole,
“Kshatriya ko
sirf dharm hi nahi,
sharirik bal bhi chahiye.”

Unhone Kunti se kaha,
“Ab balwaan putra ke liye
Vayu Devta ka aahvan karo.”

Kunti ne Vayu Devta ko bulaya.
Vayu Devta hiran par baith kar aaye.

Bole,
“Kya vardaan chahiye, Kunti?”

Kunti ne vinamrata se kaha,
“Mujhe aisa putra dijiye
jo sabse shaktishaali ho.”

Vayu Devta ne vardaan diya.
Aur janma hua
Bhima ka.

Aakash se awaaz aayi,
“Yeh bal mein
sabse shreshth hoga.”

Bhima ke janm par
ek adbhut ghatna hui.
Bachcha maa ki godi se
pahaad par gir gaya.
Pahaad toot gaya,
par Bhima ko
kuch bhi nahi hua.

Pandu hairaan reh gaye.

Usi din
Duryodhana ka bhi janm hua.

Phir Pandu ne socha,
“Mujhe ab
sabse mahaan putra chahiye.
Jo poori duniya mein
prasiddh ho.”

Unhone kathor tapasya ki.
Rishiyon se salah li.
Kunti ne ek saal ka vrat rakha.

Aakhir
Indra Dev prasann hue.
Unhone Pandu se kaha,
“Main tumhe
ek aisa putra dunga
jo sab par vijayi hoga.”

Pandu ne Kunti se kaha,
“Indra Dev ko bulao.”

Kunti ne Indra ka aahvan kiya.
Indra aaye
aur janma hua
Arjuna ka.

Aakash garaj utha.
Devtaon ki awaaz aayi,
“Yeh balak
veeron mein shreshth hoga.
Mahadev se
Paashupat astra paayega.
Devtaon ke shatru
iska bhay maanenge.”

Phool barse.
Dev, Gandharva, Apsara
sab prasann hue.
Nritya aur sangeet hua.
Poori dishaen
anand se bhar gayi.

Sab rishiyon ne
Pandu ke putron ko aashirvaad diya.

Pandu fir se
aur santaan chahne lage.
Par Kunti ne kaha,
“Shastra ke anusaar
chaar se adhik putra
is vidhi se paap maane jaate hain.”

“Isliye ab
aur aahvan uchit nahi.”

Pandu chup ho gaye.
Unhone Kunti ki baat maan li.

Yahin se
Pandavon ke yug ki
neev poori hoti hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.60
        with st.expander("Section 1.7.60"):
            text1 = """ 
            Section CXXIV – Madri ko Santaan ka Vardaan (Hinglish Story Rewrite)

Vaisampayana ne kaha,
jab Kunti ke putra
aur Gandhari ke sau putra
janm le chuke the,
tab Madri ne
chupchaap Pandu se baat ki.

Madri boli,
“Swami,
agar aap mujhse thode door bhi ho,
toh mujhe koi shikayat nahi.”

“Main yeh bhi nahi maanta
ki main Kunti se kam hoon.
Aur mujhe is baat ka bhi dukh nahi
ki Gandhari ke sau putra hue.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.60.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Uski awaaz bhaari ho gayi.
“Par ek baat
mera mann tod deti hai.”

“Kunti aur main
barabar hain.
Par main
abhi tak maa nahi bani.”

“Yeh dukh hai
ki aapko santaan
sirf Kunti se mili.”

Madri ne sir jhuka liya.
“Kunti se maangna
mujhe theek nahi lagta.
Woh meri saut hai.”

“Par agar aap chaahein,
toh aap hi
unse baat kijiye.”

Pandu ne Madri ki baat suni.
Aur bole,
“Madri,
main yeh baat
bahut samay se soch raha tha.”

“Bas yeh nahi jaanta tha
ki tum kya chahogi.”

“Ab mujhe sab samajh aa gaya.
Main Kunti se baat karunga.
Woh mana nahi karegi.”

Phir Pandu ne
Kunti se akele mein kaha,
“Kunti,
mere vansh ko badhane ke liye
aur duniya ke bhale ke liye
mujhe aur santaan chahiye.”

“Madri ko bhi
maa banne ka adhikar hai.
Yeh kaam mushkil hai,
par mahaan bhi.”

“Isse tumhe
amar yash milega.”

Kunti ne bina sankoch kaha,
“Swami,
jaise aap kahein.”

Phir Kunti ne
Madri se kaha,
“Tum kisi devta ka smaran karo.
Woh tumhe
putra denge.”

Madri ne kuch pal socha.
Phir unhone
Ashwini Kumaron ka smaran kiya.

Ashwini Kumar turant aaye.
Aur Madri ko
do putra mile.

Jab dono balak janme,
aakash se awaaz aayi,
“Yeh dono
saundarya aur shakti mein
sabse shreshth honge.”

Unke naam pade—
Nakula aur Sahadeva.

Rishiyon ne
sab bachchon ke naam rakhe.

Kunti ke putra—
Yudhishthira,
Bhima,
aur Arjuna.

Madri ke putra—
Nakula
aur Sahadeva.

Paanch putra
paanch varshon ke yug jaise lag rahe the.
Sab mein tej tha.
Bal tha.
Sundarta thi.

Pandu apne putron ko dekh kar
bahut prasann hue.

Rishi aur unki patniyan bhi
in bachchon se prem karti thi.

Kuch samay baad
Pandu ne phir
Kunti se Madri ke liye kaha.

Tab Kunti ne dukhi ho kar bola,
“Swami,
maine Madri ko
mantra sirf ek baar diya.”

“Par usne
do putra paida kar liye.”

“Main bhool gayi thi
ki yugm devta
yugm santaan dete hain.”

“Ab mujhe aur aadesh na dijiye.
Yahi meri prarthana hai.”

Pandu ne
Kunti ki baat maan li.

Is prakaar
Pandu ke paanch putra hue.
Sab devputra the.
Sab mahaan bane.

Pandav
aur Dhritarashtra ke sau putra
ek saath bade hone lage.

Jaise talab mein
kamal ek saath khilte hain.

Aur rishi
unke bhavishya ko dekh kar
ascharya se bhar gaye.

Yahin se
Mahabharat ke yug ka
sachcha aarambh hota hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.61
        with st.expander("Section 1.7.61"):
            text1 = """ 
            Section CXXV – Pandu ka Ant aur Madri ka Tyag (Hinglish Story Rewrite)

Vaisampayana ne kaha,
jab Pandu ne
apne paanch sundar putron ko
us van aur pahadi pradesh mein
badte hue dekha,
toh unke mann mein
purani shakti jaag uthi.

Basant ka ritu tha.
Har taraf phool khile the.
Hawa madhur thi.
Mann ko behkane wali.

Ek din Pandu
Madri ke saath
van mein ghoomne nikle."""
            create_image_text_layout("attached_assets/chapter1/1.7.61.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Pedon par
palash, aam, champa,
ashok aur kesar ke phool the.
Bhanwre gun gun kar rahe the.
Koyal madhur ga rahi thi.

Jheelon mein
kamal khile hue the.
Sab kuch bahut sundar lag raha tha.

Is prakriti ko dekh kar
Pandu ka mann
vichlit ho gaya.
Unke hriday mein
ichha jaag uthi.

Madri paas hi thi.
Yuva aur sundar.
Us drishya ne
Pandu ki samajh par
parda daal diya.

Rishi ke shraap ko
woh bhool gaye.
Aur apne mann par
niyantran kho baithe.

Madri ghabra gayi.
Usne rokne ki koshish ki.
Par bhagya ke bal se
Pandu apne aap ko
rok na sake.

Aur usi kshan
Rishi ka shraap
sach ho gaya.

Pandu ka shareer
nishchet ho gaya.
Pran chhoot gaye.

Madri cheekh padi.
Woh Pandu ke sharir ko
pakad kar roti rahi.

Kunti aur sab bachche
unke rone ki awaaz sun kar
daudte hue aaye.

Madri ne Kunti se kaha,
“Sirf tum aao.
Bachchon ko wahin roko.”

Kunti daudi aayi.
Aur dono ko zameen par
is haal mein dekh kar
toot gayi.

Kunti boli,
“Madri,
yeh kaise ho gaya?
Pandu toh hamesha
shraap se darte the.”

“Tumhe unka
dhyaan rakhna chahiye tha.”

Madri roti hui boli,
“Didi,
maine unhe rokna chaha.
Par bhagya se
kuch bhi nahi bach saka.”

Tab Kunti boli,
“Main badi patni hoon.
Mujhe unke saath
antim yatra par jaana chahiye.”

Par Madri ne kaha,
“Didi,
yeh mera kartavya hai.”

“Pandu mere paas aaye the.
Unka mann adhoora reh gaya.”

“Agar main jeeti rahi,
toh main tumhare bachchon ko
apne jaise nahi paal paungi.”

“Par tum
mere putron ko
apne jaise paal sakti ho.”

“Isliye
mujhe unke saath jaane do.”

Kunti chup ho gayi.
Unki aankhon se aansu behte rahe.

Ant mein
Madri ne Pandu ke sharir ke saath
chita par chadh kar
apna jeevan tyag diya.

Vaisampayana ne kaha,
“Is prakaar
Pandu ka ant hua.
Aur Madri ne
atyant tyag ka path chuna.”

Yeh ghatna
bhagya, niyam aur kartavya ki
gehri seekh deti hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.62
        with st.expander("Section 1.7.62"):
            text1 = """ 
            Section CXXVI – Pandu ka Antim Sanskar aur Hastinapur Lautna (Hinglish Story Rewrite)

Vaisampayana ne kaha,
jab devtulya Rishiyon ne
Raja Pandu ki mrityu dekhi,
toh sab ek saath baith kar
vichaar karne lage.

Unhone kaha,
“Pandu ek dharmic aur prasiddh raja the.
Rajya aur sukh chhod kar
woh yahan tapasya ke liye aaye the.”

“Ab woh swarg ko prapt ho chuke hain.
Unki patni aur chhote bachche
ab humari zimmedari hain.”

“Ab humein
in bachchon aur Kunti ke saath
Hastinapur jana chahiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.62.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Phir sab Rishi
ek saath taiyaar hue.
Unhone faisla kiya
ki Pandu ke putron ko
Bhishma aur Dhritarashtra ke
haathon saunp denge.

Usi kshan
yatra shuru ho gayi.
Bachche aage the.
Kunti saath thi.
Aur Pandu aur Madri ke
nirjeev sharir bhi saath le jaaye gaye.

Kunti ne apni poori zindagi
sukh mein bitayi thi.
Par is kathin yatra ko bhi
usne chhota samjha.
Uska mann sirf
kartavya par tika tha.

Jald hi
woh Kurujangala pahunchi.
Aur Hastinapur ke
mukhya dwar par aa gayi.

Rishiyon ne
darbanon ko sandesh dene ko kaha.
Sandesh turant raj sabha tak pahunch gaya.

Jaise hi shehar ko pata chala
ki hazaaron Rishi aur Muni aaye hain,
log ashcharya se bhar gaye.

Subah hote hi
shehar ke log
apni patniyon aur bachchon ke saath
bahar nikal aaye.

Rath, palakhi, aur gaadiyon mein
Kshatriya, Brahman,
Vaishya aur Shudra
sab ek saath aaye.

Sabka mann shaant tha.
Sabke hriday mein
bhakti aur shraddha thi.

Bhishma aaye.
Dhritarashtra aaye.
Vidura aaye.
Maa Satyavati aayi.
Gandhari aur raj gharane ki
sab striyan aayi.

Dhritarashtra ke
sau putra bhi
saj-dhaj kar aaye.

Sabne milkar
Rishiyon ko pranam kiya.
Shehar ke logon ne bhi
sir jhuka diya.

Bhishma ne sabko shaant kiya.
Rishiyon ke charan dhoye.
Unhe arghya diya.

Phir ek vriddh Rishi khade hue.
Jataon wale,
mrigchhaal dharan kiye hue.

Unhone kaha,
“Tum sab Pandu ko jaante ho.
Unhone rajya chhod kar
vanvaas liya tha.”

“Unke bade putra
Yudhishthira ka janm
Dharm Devta se hua.”

“Bhima
Vayu Devta ke putra hain.”

“Arjuna
Indra ke putra hain.”

“Aur Madri ke do putra—
Nakula aur Sahadeva—
Ashwini Kumaron se janme.”

“Is tarah
Pandu ne tapasya ke dwara
Kuru vansh ko fir se jeevit kiya.”

“Pandu satrah din pehle
is lok se chale gaye.
Madri bhi unke saath
chita par chadh gayi.”

“Yeh unke avshesh hain.
Aur yeh unke putra.”

“Ab aapka kartavya hai
unke antim sanskar poore karein
aur unka Shraddh karein.”

Itna keh kar
Rishi aur Siddh
logon ke saamne hi
antardhyaan ho gaye.

Jaise baadal
aakash mein ghoom kar
gaayab ho jaate hain.

Shehar ke log
yeh adbhut drishya dekh kar
chakit reh gaye.

Phir dheere-dheere
sab apne ghar laut gaye.

Aur Hastinapur mein
Pandavon ke naye jeevan ka
aarambh hua…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.63
        with st.expander("Section 1.7.63"):
            text1 = """ 
            Section CXXVII – Pandu aur Madri ka Antim Sanskar (Hinglish Story Rewrite)

Vaisampayana ne aage kaha,
tab Dhritarashtra ne Vidura se kaha,

“Vidura,
Raja Pandu aur Madri ka
antim sanskar
poori rajsi maryada ke saath karo.”

“Unki aatma ki shanti ke liye
daan diya jaaye.
Gaay, kapde, ratna, dhan—
jo maange, usey diya jaaye.”

“Kunti ko bhi
Madri ke antim karm
apni ichha ke anusaar
karne diya jaaye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.63.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Pandu ke liye
shok na karo.
Woh mahaan raja the.
Unhone paanch veer putra chhode hain,
jo devon ke samaan hain.”

Vidura ne sir jhukaya.
“Jaise aap kahein.”

Bhishma ke saath milkar
unhone ek pavitra sthal chuna.

Raj purohit
pavitra agni lekar
shehar se baahar nikle.
Agni mein ghrit aur sugandh thi.

Pandu aur Madri ke sharir
safed kapdon mein lapete gaye.
Phoolon aur itron se sajaye gaye.
Arthi ko bhi
sundar malaon se sajaya gaya.

Dono shariron ko
ek hi arthi par rakha gaya.
Logon ke kandhon par
arthi aage badhi.

Safed chhatra tha.
Chamri ke chauri
lehraye ja rahe the.
Shankh aur vadya
dhimi awaaz mein baj rahe the.

Raste mein
log ratna aur vastra
daan kar rahe the.

Brahman,
Kshatriya,
Vaishya,
Shudra—
sab saath chal rahe the.

Sab ro rahe the.
Sabke muh se ek hi baat nikal rahi thi,
“Rajkumaar,
humein chhod kar
aap kahan ja rahe ho?”

Bhishma ro pade.
Vidura ro pade.
Pandav bhi ro rahe the.

Aakhir
Ganga ke kinare
ek sundar van mein
arthi rakhi gayi.

Sone ke kalashon mein
jal laaya gaya.
Sharir ko snan karaya gaya.
Chandan lagaya gaya.

Safed vastra pehnaya gaya.
Us pal aisa laga
jaise Raja Pandu
sirf so rahe hon.

Purohiton ke vidhan ke anusaar
sab karm poore hue.
Phir chita ko agni di gayi.

Jaise hi
agni bhadki,
Kausalya zor se ro padi,
“Putra… mere putra…”

Woh behosh ho kar
zameen par gir padi.

Shehar ke log
aur bhi zor se rone lage.
Pashu aur pakshi bhi
jaise shok mein doob gaye.

Bhishma, Vidura,
Dhritarashtra,
Pandav aur sab striyan
aansuon mein doob gaye.

Ant mein
jal kriya ki gayi.
Sab ne milkar
paani arpit kiya.

Log Pandavon ko
dilasa dene lage.
Par Pandav
zameen par hi so gaye.

Unka dukh dekh kar
Brahman aur nagrikon ne bhi
apne bistar chhod diye.

Barah din tak
poora shehar shok mein raha.
Bade, chhote,
sab Pandavon ke saath
rote rahe.

Is prakaar
Pandu ka yug samaapt hua,
aur Pandavon ka
jeevan kathin pariksha se
shuru hua…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.64
        with st.expander("Section 1.7.64"):
            text1 = """ 
            Section CXXVIII – Bhima par Visha, aur Uska Chamatkaar (Hinglish Story Rewrite)

Vaisampayana ne kaha,
Pandu ke Shraddha ke baad
Bhishma aur Kunti ne
pind daan kiya.
Brahmanon ko bhojan karaya.
Daan diya.
Zameen aur ratna bhi diye.

Uske baad
sab log Pandavon ko lekar
Hastinapur laut aaye.
Pura shehar ro raha tha.
Jaise sabne
apna hi koi kho diya ho."""
            create_image_text_layout("attached_assets/chapter1/1.7.64.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Shraddha ke baad
ek din Maharshi Vyasa
Mata Satyavati se bole,
“Maata,
achhe din beet chuke hain.”

“Ab paap badhega.
Anyay badhega.
Kuru vansh ka patan hoga.”

“Tum van mein chali jao.
Tapasya karo.
Apni aankhon se
is vansh ka vinash mat dekho.”

Satyavati ne
Vyasa ki baat maan li.
Unhone Ambika se kaha.
Bhishma se anumati li.
Aur van chali gayi.

Kuch samay baad
tapasyā karte hue
unhone sharir tyag diya
aur swarg chali gayi.

Ab Pandav
Hastinapur mein bade hone lage.
Dhritarashtra ke putron ke saath
khelte the.

Par har jagah
Bhima alag hi dikhta tha.

Daud mein sabse aage.
Khel mein sabse taakatwar.
Khaane mein sabse zyada.

Kabhi woh
Kauravon ko pakad kar
ghuma deta.
Kabhi hansi-hansi mein
unhe zameen par gira deta.

Kabhi ped hila deta,
aur saare bachche
neeche gir jaate.

Bhima yeh sab
bura mann se nahi karta tha.
Bas bachpana tha.
Par Kaurav
is baat ko nahi samajh paaye.

Duryodhana ka mann
jalne laga.

Usne socha,
“Bhima ko taqat se
haraya nahi ja sakta.”

“Toh usey
chaal se maarna hoga.”

Usne plan banaya.
“Bhima ko
Ganga mein dooba dunga.”

Phir Yudhishthira aur Arjuna ko
bandi bana kar
main akela raja ban jaunga.”

Ek din
Ganga ke kinare
Pramanakoti naam ki jagah par
ek sundar mahal banaya gaya.
Wahan khel aur bhojan ka
intezaam tha.

Duryodhana ne
Pandavon ko bulaya.
“Chalo,
Ganga ke kinare khelte hain.”

Yudhishthira maan gaye.

Sab rajkumaar
hathi aur rathon par
wahan pahunche.

Khel hua.
Hansi hui.
Bhojan hua.

Par Duryodhana ne
Bhima ke khane mein
tez zeher mila diya.

Woh muskurata raha.
Aur Bhima ko
zyaada khana khilata raha.

Bhima ne khaya.
Phir sab
paani mein khelne lage.

Shaam ko
Bhima thak gaya.
Zeher ka asar ho gaya.
Thandi hawa ne
zeher ko aur faila diya.

Bhima behosh ho gaya.

Duryodhana ne
use belon se baandha.
Aur Ganga mein
phenk diya.

Bhima paani mein doobta gaya.
Seedha
Nagon ke lok tak pahunch gaya.

Hazaaron saanp
usey kaatne lage.

Par ek chamatkaar hua.

Saanpon ka zeher
Bhima ke sharir mein
maujood zeher ko
khatam karne laga.

Bhima hoash mein aa gaya.

Usne bandhan tod diye.
Aur saanpon ko
zameen mein daba diya.

Kuch saanp bhaag gaye.
Aur apne raja
Vasuki ke paas gaye.

Vasuki aaye.
Aur Bhima ko dekha.

Wahan Aryaka bhi tha.
Jo Kunti ke purkhon mein se tha.

Aryaka ne Bhima ko
pehchaan liya.
Aur gale laga liya.

Vasuki bole,
“Hum isse
kya vardaan dein?”

Aryaka ne kaha,
“Isse dhan nahi chahiye.”

“Isse amrit pilao.
Isse aur shakti milegi.”

Bhima ko
amrit diya gaya.

Usne ek ke baad ek
aath kalash pee liye.

Har kalash mein
hazaar haathiyon jitni shakti thi.

Amrit peene ke baad
Bhima aur bhi taakatwar ho gaya.

Saanpon ne
uske liye sundar shayya banayi.
Bhima wahan
shaanti se so gaya.

Aur upar Hastinapur mein
sab samajh rahe the
Bhima mar chuka hai…
jabki neeche
uski taqat aur bhi badh chuki thi."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.65
        with st.expander("Section 1.7.65"):
            text1 = """ 
            Section CXXIX – Bhima ki Wapsi aur Duryodhana ka Asli Chehra (Hinglish Story Rewrite)

Vaisampayana ne kaha,
Ganga ke kinare khel ke baad
Kaurav aur Pandav
Hastinapur ki taraf laut aaye.
Par Bhima saath nahi tha.

Koi ghode par tha.
Koi haathi par.
Koi rath mein.

Raaste mein log bole,
“Shayad Bhima
humse pehle chala gaya hoga.”

Par Duryodhana ke mann mein
alag hi khushi thi.
Bhima ka na dikhna
usey sukoon de raha tha."""
            create_image_text_layout("attached_assets/chapter1/1.7.65.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Hastinapur pahunch kar
Yudhishthira seedhe
maa Kunti ke paas gaye.

Pranam karke bole,
“Maata,
kya Bhima aa gaya?”

“Humne usey har jagah dhoonda.
Van mein, bagiyon mein.
Par woh kahin nahi mila.”

“Hum soch kar aaye
ki shayad woh
humse pehle ghar aa gaya hoga.”

Yudhishthira ki awaaz bhaari ho gayi.
“Par yahan bhi
woh nahi hai.”

“Maata,
kya aapne
usey kahin bheja hai?”

“Woh so raha tha…
aur phir gayab ho gaya.”

“Main darr raha hoon.
Kahin…
woh jeevit na ho…”

Yeh sunte hi
Kunti chilla uthi.

“Putra!
Bhima yahan nahi aaya!”

“Jaldi jao.
Apne bhaiyon ke saath
usey dhoondo.”

Phir Kunti ne
Vidura ko bulaya.

“Vidura,
Bhima gayab hai!”

“Sab laut aaye hain.
Sirf Bhima nahi.”

“Duryodhana
ussey nafrat karta hai.
Woh raaj ka lalchi hai.”

“Mujhe darr hai
kahin usne
mere putra ko maar na diya ho.”

Kunti ka hriday
jal raha tha.

Vidura ne shaant swar mein kaha,
“Maata,
aisa mat sochiye.”

“Apne baaki putron ki
raksha kijiye.”

“Agar Duryodhana par
shak hua,
toh woh aur bada paap kar sakta hai.”

“Rishi ka vachan hai—
aapke sab putra
lambi aayu paayenge.”

“Bhima zaroor lautega.”

Vidura yeh keh kar chale gaye.
Par Kunti ka mann
bechain hi raha.

Udhar…
aath din baad
Bhima ki aankh khuli.

Amrit poori tarah
pach chuka tha.
Uska sharir
pehle se kai guna
zyaada shaktishaali tha.

Naag bole,
“Veer Bhima,
ab tum mein
das hazaar haathiyon ka bal hai.”

“Koi bhi tumhe
hara nahi sakta.”

“Ab snaan karo
aur ghar jao.
Tumhare bhai
tumhare liye ro rahe hain.”

Bhima ne snaan kiya.
Safed vastra pehne.
Safed phoolon ki mala pehni.

Naagon ne
usey madhur bhojan diya.
Aashirvaad diya.

Phir Bhima ko
usi bagiya mein chhod diya
jahan se usey
Ganga mein phenka gaya tha.

Aur sab naag
gayab ho gaye.

Bhima daudta hua
maa Kunti ke paas pahuncha.

Pranam kiya.
Bhaiyon ko gale lagaya.

Kunti ne
usey zor se gale lagaya.
Sabki aankhon mein aansu the.

Sab ek hi baat bol rahe the,
“Aaj kitni badi khushi hai!”

Phir Bhima ne
poori baat batai.
Zeher.
Bandhan.
Ganga.
Naag lok.
Duryodhana ki saazish.

Yudhishthira ne shaant swar mein kaha,
“Bhima,
is baat ko
abhi kisi se mat kehna.”

“Hum sab
ek-doosre ki raksha karenge.”

“Samay aane par
sab sach saamne aayega.”

Us din se
Pandav satark ho gaye.
Aur Vidura
hamesha unhe
samajhdari ki salah dete rahe.

Par Duryodhana
ruka nahi.

Usne phir
Bhima ke khane mein
naya zeher milaya.

Is baar
Yuyutsu ne
Pandavon ko bata diya.

Bhima ne bina dare
woh zeher kha liya.
Aur usey
pacha bhi liya.

Kuch bhi nahi hua.

Duryodhana, Karna aur Shakuni
aur bhi chal chalne lage.
Par Pandav
Vidura ki salah par
shaant rahe.

Aakhir Dhritarashtra ne socha,
“Yeh rajkumaar
zyada hi shararti ho gaye hain.”

Isliye unhone
Guru Kripa (Gautama) ko
unka acharya banaya.

Aur sab rajkumaar
astra-vidya seekhne lage.

Yahin se
shiksha, yuddh aur bhavishya ke
mahaan sangharsh ki
shuruaat hoti hai…  """
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.66
        with st.expander("Section 1.7.66"):
            text1 = """ 
            Section CXXX – Kripa ka Janm aur Guru ka Safar (Hinglish Story Rewrite)

Janamejaya ne poocha,
“Hey Brahman Dev,
mujhe Kripa ke janm ki poori kahani sunaiye.
Woh ghaas ke jhund se kaise paida hue?
Aur unhe shastra ka gyaan kaise mila?”

Vaisampayana bole,
“Rajaa,
Maharshi Gautama ke ek putra the—Saradvat.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.66.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Saradvat janm se hi
teer aur dhanush ke saath paida hue the.
Unka mann
sirf shastra-vidya mein lagta tha.
Baaki vidyaon mein
unka ruchi kam tha.

Tapasya ke bal se
unhone saari astra-vidya seekh li.
Unki shakti dekh kar
Indra bhi chintit ho gaye.

Indra ne ek apsara
Janapadi ko bulaya.
Aur kaha,
“Gautama ke putra ki tapasya bhang karo.”

Janapadi van mein pahunchi.
Saradvat wahan akela tha.
Uske haath mein dhanush tha.
Sharir par mrigchhaal.

Apsara bahut sundar thi.
Ek hi vastra mein thi.
Use dekh kar
Saradvat ka mann hil gaya.

Uske haath se
dhanush aur teer gir gaye.
Sharir kaanp gaya.
Par usne apna dhairya sambhala.

Phir bhi,
mann ke achanak vichlan se
ek anjaani ghatna ho gayi.

Saradvat wahan se
turant chala gaya.
Par uski veerya
ghaans ke jhund par gir gayi.

Us ghaas se
do shishu paida hue.
Ek ladka.
Ek ladki.
Dono judwa the.

Kuch samay baad
Raja Shantanu ke ek sainik ne
shikar ke dauran
un bachchon ko dekha.

Paas hi
dhanush, teer aur mrigchhaal pade the.
Usne socha,
“Yeh kisi mahaan Brahman ke bachche honge.”

Woh dono bachchon ko
Raja Shantanu ke paas le gaya.

Raja ne bachchon ko dekha.
Unka dil bhar aaya.
Unhone kaha,
“Main inhe apna bachcha banaunga.”

Raja ne unka palan kiya.
Naam diya—
Kripa aur Kripi.
Kyuki unhe
daya se apnaya gaya tha.

Udhar Saradvat ko
tapogyaan se pata chal gaya
ki uske bachche
raja ke mahal mein hain.

Woh Raja Shantanu ke paas aaya.
Apni poori kahani batayi.

Phir usne
Kripa ko
astra-vidya ke chaaron bhaag sikhaye.
Saare gupt rahasya bhi.

Kripa bahut jaldi
ek mahaan acharya ban gaya.

Uske paas
Dhritarashtra ke sau putra aaye.
Pandav aaye.
Yadav aur Vrishni vansh ke rajkumaar bhi aaye.

Sabne
Kripa se
shastra-vidya seekhni shuru ki.

Yahin se
Kuru rajkumaaron ki
yuddh shiksha ka
sachcha aarambh hota hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.67
        with st.expander("Section 1.7.67"):
            text1 = """ 
            Section CXXXI – Drona ka Janm, Shiksha aur Guru banna (Hinglish Story Rewrite)

Vaisampayana bole,
Bhishma apne poton ke liye
sabse shreshth shikshak chahte the.

Unka vichaar tha,
“Jo guru ho,
woh bahut buddhimaan ho.
Astra-vidya ka poora gyaan ho.
Aur tejasvi ho.”

Isliye Ganga-putra Bhishma ne
Pandav aur Kaurav dono ko
Drona ke sharan mein diya."""
            create_image_text_layout("attached_assets/chapter1/1.7.67.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Drona,
Bharadvaja ke putra the.
Vedo ke gyaata the.
Aur shastra-vidya mein
atyant nipun the.

Bhishma ke samman se
prasann ho kar
Drona ne
sab rajkumaron ko
apna shishya maan liya.

Unhone
astra-vidya ke
saare bhaag sikhaye.
Aur kuch hi samay mein
Pandav aur Kaurav
sabhi shastraon mein
nipun ho gaye.

Tab Janamejaya ne poocha,
“Hey Brahman Dev,
Drona ka janm kaise hua?
Unhone shastra ka gyaan
kaise paaya?
Aur woh Kuruvansh tak
kaise aaye?”

“Mujhe Asvatthama ke janm ki
kahani bhi sunaiye.”

Vaisampayana bole,

Ganga ke udgam par
ek mahaan rishi rehte the—
Bharadvaja.

Ek din
Agnihotra yagya ke liye
woh Ganga ke tat par aaye.

Wahin
apsara Ghritachi snaan kar rahi thi.
Woh sundar thi.
Yuva thi.

Uske vastra
thode vyavasthit ho gaye the.

Use dekh kar
rishi Bharadvaja ka mann
kshan bhar ke liye
vichlit ho gaya.

Unke sharir se
veerya nikal aaya.
Par rishi ne
usey turant
ek patra mein sambhaal liya.

Us patra ko kehte hain
drona.

Usi drona se
ek balak ka janm hua—
Drona.

Drona ne
sab ved, upved
aur shastra-vidya
seekh li.

Bharadvaja ne pehle
Agneya astra ka gyaan
Agnivesh ko diya tha.
Agnivesh ne
wahi gyaan
Drona ko diya.

Us samay
Raja Prishata the,
jo Bharadvaja ke mitra the.
Unke putra ka naam tha
Drupada.

Drupada aur Drona
saath khelte the.
Saath padhte the.

Par samay badla.
Prishata ki mrityu hui.
Drupada
Panchal ka raja ban gaya.

Kuch samay baad
Rishi Bharadvaja bhi
swarg sidhaar gaye.

Drona
aashram mein hi rahe.
Tapasya aur adhyayan mein
leen ho gaye.

Phir unka vivaah
Kripi se hua,
jo Saradvat ki putri thi.

Kripi ne
ek putra ko janm diya.

Jaise hi woh balak paida hua,
woh ghode ki tarah
hin-hinaya.

Aakash se awaaz aayi,
“Is balak ki awaaz
ghode jaisi hai.
Isliye iska naam
Asvatthama hoga.”

Drona bahut prasann hue.

Isi dauran
Drona ko pata chala
ki Parashurama
(apne shastra daan ke liye prasiddh)
sab kuch Brahmanon ko
daan dena chahte hain.

Drona ne socha,
“Mujhe unse
astra-vidya leni chahiye.”

Woh apne shishyon ke saath
Mahendra parvat gaye.

Wahan Parashurama mile.
Drona ne pranam kiya.
Apni poori kahani batayi.

Drona bole,
“Main Bharadvaja ka putra hoon.
Main drona se janma hoon.
Aur main aapse
aapki sampatti chahata hoon.”

Parashurama bole,
“Maine apni saari dhan-daulat
daan kar di hai.”

“Mere paas sirf
mera sharir
aur mere shastra bache hain.”

“Bolo,
kya chahte ho?”

Drona ne kaha,
“Mujhe
aapke saare shastra chahiye.
Aur unka rahasya bhi.”

Parashurama bole,
“Thik hai.”

Aur unhone
apni poori astra-vidya
Drona ko de di.

Drona ka mann
tripti se bhar gaya.

Shastra paa kar
woh apne mitra
Drupada ke nagar ki taraf
chal pade.

Yahin se
Drona ka guru ke roop mein
uday hota hai,
aur Mahabharat ke
mahaan yoddha taiyaar hone lagte hain…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.68
        with st.expander("Section 1.7.68"):
            text1 = """ 
            Section CXXXII – Drupada ka Ghamand aur Drona ka Apmaan (Hinglish Story Rewrite)

Vaisampayana bole,
phir Bharadvaja ke putra Drona
Panchal nagar pahunche.

Woh seedhe
Raja Drupada ke darbar mein gaye
aur shaant swar mein bole,

“Rajaa,
mujhe apna purana mitra samjho.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.68.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Yeh sunkar
Drupada ka mann badal gaya.
Uska hriday khushi se nahi,
ghamand se bhar gaya.

Daulat aur rajya ke nashe mein
uski aankhen laal ho gayi.
Bhaunhen tedhi ho gayi.

Woh gusse se bola,

“Hey Brahman,
tumhari buddhi kamzor lagti hai.”

“Achaanak aakar
mujhe apna mitra keh rahe ho?”

“Rajaa aur
gareeb Brahman
kab se mitra ho gaye?”

“Pehle hum dost the,
yeh sach hai.
Par tab hum
barabar the.”

“Samay sab kuch badal deta hai.
Mitrata bhi.”

“Is duniya mein
koi dosti hamesha nahi rehti.”

“Samay usey ghisa deta hai.
Aur krodh usey tod deta hai.”

Drupada aur tez bola,

“Is purani dosti ko
ab chhod do.”

“Meri tumse dosti
sirf us samay tak thi
jab iska koi matlab tha.”

“Gareeb aur ameer
kabhi dost nahi ho sakte.”

“Veer aur kaayar
kabhi mitra nahi ho sakte.”

“Jo raja nahi hai,
woh raja ka dost
kaise ho sakta hai?”

“Isliye,
is bekaar ki dosti ko
yaad karke
apna aur mera
samay barbaad mat karo.”

Yeh shabd
Drona ke hriday mein
teer ki tarah chubh gaye.

Uska chehra shaant tha,
par mann mein
agni jal uthi.

Usne kuch pal socha.
Aur phir
nirnay kar liya.

“Is ghamand ka
sahi uttar diya jaayega.”

Bina kuch kahe
Drona ne Panchal nagar chhod diya.

Uske kadam
ab Hastinapur ki taraf the.
Kuruon ki nagri ki taraf.

Yahin se
apmaan badle ki aag ban gaya,
aur bhavishya ka
mahaan sangharsh
chup-chaap janm lene laga…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.69
        with st.expander("Section 1.7.69"):
            text1 = """ 
            Section CXXXIII – Drona ka Parichay aur Bhishma ka Vachan (Hinglish Story Rewrite)

Vaisampayana bole,
Drona Hastinapur aa kar
chup-chaap Kripa ke ghar rehne lage.

Unka putra Asvatthama
kabhi-kabhi Pandavon ko
astra-vidya sikhata tha.
Par abhi tak
kisi ko
uski asli shakti ka pata nahi tha."""
            create_image_text_layout("attached_assets/chapter1/1.7.69.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Ek din
Pandav aur Kaurav
shehar se bahar
khelne nikle.

Khushi-khushi
ball se khel rahe the.
Achaanak
ball ek gehre kuen mein
gir gaya.

Sab rajkumaar
poori koshish karne lage.
Par ball
bahar nahi aayi.

Sab ek-doosre ko
sharm ke saath
dekhne lage.
Sab pareshaan ho gaye.

Tab unhone
paas hi ek Brahman ko dekha.
Woh patla-sa tha.
Saanwla rang.
Roz ka pooja-paath
abhi khatam kiya tha.

Woh Brahman
aur koi nahi,
Drona hi the.

Rajkumaar unke paas aaye.
Drona ne unhe dekha
aur halka sa muskuraye.

Bole,
“Bharat vansh ke rajkumar ho,
phir bhi ek ball
kuen se nahi nikaal pa rahe?”

“Tumhari Kshatriya shakti par
sharam aani chahiye.”

Phir bole,
“Agar aaj mujhe
bhojan ka vachan do,
toh main
sirf ghaas ke tanon se
na keval ball,
balki apni anguthi bhi
nikal kar dikhaunga.”

Yeh keh kar
Drona ne
apni anguthi
kuen mein phenk di.

Yudhishthira bole,
“Hey Brahman Dev,
sirf bhojan nahi.
Aap jo maangein,
hum denge.”

Drona ne
lambe ghaas ke tan liye.
Mantra padhe.

Ek tan se
ball ko cheda.
Phir us tan ko
doosre tan se.
Phir teesre se.

Aakhir
ball upar aa gayi.

Sab rajkumaar
hairaan reh gaye.

Phir unhone kaha,
“Hey Brahman Dev,
ab anguthi bhi nikaaliye.”

Drona ne
dhanush uthaya.
Teer chhoda.
Anguthi ko ched kar
bahar le aaye.

Sab rajkumaar
dandavat ho gaye.

Bole,
“Aap kaun hain?
Itni kala kisi mein nahi.”

Drona bole,
“Bhishma ke paas jao.
Unhe meri kala batao.
Woh mujhe pehchaan lenge.”

Rajkumaar
Bhishma ke paas gaye.
Sab kuch bataya.

Bhishma samajh gaye,
“Yeh toh
Drona hi hain.”

Woh turant
Drona ke paas gaye.
Unka samman kiya.
Aur Hastinapur le aaye.

Bhishma ne poocha,
“Aap yahan kyun aaye?”

Drona ne
poori kahani sunai.
Drupada se dosti.
Vachan.
Aur apmaan.

Apne bete Asvatthama ki
doodh wali kahani bhi batayi.
Kaise pani aur chawal ko
doodh samajh kar
bachcha khush ho gaya tha.

Drona bole,
“Us din
mera hriday toot gaya.”

“Isliye main yahan aaya hoon.
Achhe shishya chahiye.
Aur apna kartavya nibhana hai.”

Bhishma bole,
“Hey Brahman Dev,
aap dhanush uthaiye.”

“Pandav aur Kaurav
sab aapke shishya honge.”

“Hastinapur ki sampatti,
rajya aur samman
sab aapka hai.”

“Jo aap chahte ho,
woh poora hoga.”

Drona ka mann
shaant ho gaya.
Unki aankhon mein
naya sankalp tha.

Yahin se
Mahabharat ke mahaan yoddha
guru Drona ke haathon
ghadne lage…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.70
        with st.expander("Section 1.7.70"):
            text1 = """ 
            Section CXXXIV – Guru Drona, Arjun aur Ekalavya (Hinglish Moral Story)

Vaisampayana bole,
Bhishma ke samman se prasann ho kar
Guru Drona
Kuru rajya mein rehne lage.

Unhe sab aadar dete the.
Bhishma ne
Pandav aur Kaurav rajkumaar
Drona ko shishya roop mein saunp diye.

Saath hi
ghar, dhan, anna
sab kuch diya.

Drona khush hue.
Unhone sab ko
apna shishya maan liya."""
            create_image_text_layout("attached_assets/chapter1/1.7.70.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Ek din
Guru Drona ne sab shishyon ko bulaya.
Sab ne unke charan sparsh kiye.

Drona bole,
“Mere mann mein ek iccha hai.
Agar tum sach mein mere shishya ho,
toh wada karo
jab tum mahaan yoddha banoge,
meri us iccha ko poora karoge.”

Sab chup rahe.
Sirf Arjun aage aaye.

Arjun bole,
“Guruji,
jo aadesh hoga,
main poora karunga.”

Drona ki aankhon mein
aansoo aa gaye.
Unhone Arjun ko
gale laga liya.

Guru Drona ne
sab ko samaan gyaan diya.
Par Arjun ka lagav
sabse zyada tha.

Karna bhi wahan tha.
Woh Duryodhan ke saath
Arjun se irshya karta tha.

Par Arjun
sirf vidya par dhyaan deta tha.
Din-raat
guru seva karta tha.

Drona samajh gaye,
“Yeh ladka
sabse aage niklega.”

Drona sab shishyon ko
paani bharne bhejte the.
Sab ko patle muh ka ghada milta.
Par apne putra Asvatthama ko
chauda muh ka ghada dete.

Arjun ne yeh dekh liya.
Usne Varun Astra se
apna ghada turant bhar liya.
Aur Asvatthama ke saath hi
laut aaya.

Drona muskura diye.
Unhe samajh aa gaya,
“Yeh shishya
peeche rehne wala nahi.”

Ek raat
Arjun khana kha raha tha.
Achanak diya bujh gaya.

Par Arjun
andhere mein bhi
khana khaata raha.

Usne socha,
“Haath toh bina dekhe bhi
nishana pakad leta hai.”

Usi raat se
Arjun ne
andhere mein teer chalane ka
abhyaas shuru kiya.

Raat ko
dhanush ki awaaz sun kar
Drona aaye.

Unhone Arjun ko gale lagaya.
Bole,
“Main tujhe
is duniya ka
sabse mahaan dhanurdhar banaunga.”

Tab ek aur katha hui.
Ek Nishad rajkumar – Ekalavya
Guru Drona ke paas aaya.
Par jaati ke kaaran
use shishya nahi banaya gaya.

Ekalavya chup-chaap
jangal chala gaya.
Wahan mitti se
Guru Drona ki murti banayi.
Aur use hi guru maan kar
abhyaas karne laga.

Uska shraddha
bahut gehra tha.

Ek din
Pandav aur Kaurav
shikaar par gaye.
Unka kutta
jangal mein bhatak gaya.

Ekalavya ne
sirf yaav ke liye
us kutte ke muh mein
saath teer daal diye.

Kutta zinda tha.
Par bhonk nahi pa raha tha.

Sab rajkumaar hairaan reh gaye.
Aisi kala
unhone kabhi nahi dekhi.

Jab Arjun ne yeh suna,
woh Drona ke paas gaya.
Bola,
“Guruji,
aapne kaha tha
mujhse behtar koi nahi hoga.
Phir yeh Ekalavya kaun hai?”

Drona gambhir ho gaye.
Woh Arjun ko saath le kar
Ekalavya ke paas gaye.

Ekalavya ne
guru ke charan sparsh kiye.

Drona bole,
“Agar tu sach mein mera shishya hai,
toh guru-dakshina de.”

Ekalavya khush ho gaya.
Bola,
“Jo aadesh ho.”

Drona bole,
“Apna daahina angutha de do.”

Ekalavya ne
bina soche
apna angutha kaat diya.
Aur guru ko de diya.

Us din
uski kala kam ho gayi.
Arjun ka mann shaant ho gaya.

Ant mein
sab shishyon ka gun bataya gaya.

Bhima aur Duryodhan – gada yuddh

Nakula–Sahadev – talwar

Yudhishthira – rath yuddh

Asvatthama – gupt astras

Arjun – sab mein sarvashreshth

Arjun
Atirathi bana.
Uski keerti
poori prithvi par phail gayi.

Par
Kauravon ke mann mein
irshya badhti chali gayi.

Yahin se
Mahabharat ke beej
aur gehre hote gaye…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.71
        with st.expander("Section 1.7.71"):
            text1 = """ 
            Section CXXXV – Arjun ka Lakshya, Guru Drona ka Vishwas (Hinglish explanation)

Vaisampayana kehte hain—
jab sab shishya nishana lagane mein asafal ho gaye,
Guru Drona muskuraye aur Arjun ko bulaya.

Drona bole,
“Tum hi is lakshya ko bhed sakte ho.
Dhanush uthao aur tayyar raho.”

Arjun ne dhanush taana.
Tab Drona ne poocha—
“Arjun, kya tum ped, pakshi aur mujhe dekh rahe ho?”"""
            create_image_text_layout("attached_assets/chapter1/1.7.71.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Arjun shant swar mein bola,
“Main sirf pakshi ko dekh raha hoon.
Na ped, na aap.”

Drona ne phir poocha,
“Agar pakshi dikh raha hai, to batao—kya poora pakshi?”

Arjun ne kaha,
“Sirf pakshi ka sir. Uska sharir bhi nahi.”

Yeh sunte hi
Drona ke romanch khade ho gaye.
Unhone kaha—
“Chalao.”

Arjun ka teer chala—
aur pakshi ka sir
seedha zameen par aa gira.

Guru Drona ne
Arjun ko seene se laga liya.
Unke mann mein yeh nishchit ho gaya—
Drupad ka ghamand ek din yahin shishya tod dega.

Kuch samay baad
Drona apne sab shishyon ke saath
Ganga ke tat par snaan ke liye gaye.

Jab Drona jal mein utre,
ek ghadiyal ne
unki jaangh pakad li.

Yeh pariksha thi.

Drona bole,
“Is prani ko maaro aur mujhe bachao.”

Sab shishya ghabra gaye.
Sirf Arjun ne
pal bhar bhi der nahi ki.

Usne paanch tez teer
jal ke andar hi chala diye.

Ghadiyal tukdon mein kat gaya
aur Drona mukt ho gaye.

Drona ne mann hi mann maana—
yeh mera shreshth shishya hai.

Tab Drona ne Arjun se kaha,
“Main tumhe
ek ati-shaktishaali astr deta hoon—
Brahmasira Astra.

Par yaad rakhna—
ise manav yuddh mein kabhi na chalana.
Kam shakti wale shatru par chalaya
toh poora vishv jal sakta hai.

Yeh astr
teenon lokon mein nirala hai.
Sirf tab prayog karna
jab koi amanavi shatru saamne ho.”

Arjun ne
haath jod kar
is pratigya ke saath astr grahan kiya.

Tab Guru Drona bole—
“Is sansaar mein
tumse bada dhanurdhar koi nahi hoga.
Tumhara parakram mahaan hoga
aur koi shatru
tumhe kabhi parajit nahi kar paayega.”

Is adhyay ka saar

Sahi lakshya = adha yuddh jeetna

Ekagrata hi mahaan banati hai

Guru–shishya ka vishwas astr se bhi shaktishaali hota hai

Yahin se
Arjun Atirathi banne ki or
ek aur kadam aage badhta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.72
        with st.expander("Section 1.7.72"):
            text1 = """ 
            Section CXXXVI – Shastra-vidya ka Mahotsav (Hinglish Story)

Vaisampayana kehte hain—
jab Pandav aur Kaurav
sabhi shastra-vidya mein nipun ho gaye,
to Guru Drona ne
raja Dhritarashtra se kaha,

“Rajann,
aapke putron ki shiksha poori ho chuki hai.
Ab inka kaushal sabke saamne dikhna chahiye.”

Yeh sunkar raja khush ho gaye.
Unhone kaha,
“Jaise aap theek samjhein,
waise hi pratiyogita karwaiye.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.72.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Vidur ne turant vyavastha sambhali.
Ek bada, khula maidan tayaar hua.
Sundar rangmanch bana.
Raniyon ke liye alag sabha-sthal.
Shehar ke log tents laga kar aa gaye.

Poora Hastinapur
jaise utsav mein doob gaya.

Nirdharit din,
sabha saj chuki thi.
Bhishma, Kripa, mantri, raniyaan—
sab apni jagah baith gaye.

Gandhari aur Kunti
sone ke gehno mein chamak rahi thi.
Logon ka shor
samundar ki lehron jaisa lag raha tha.

Tab Guru Drona pravesh karte hain—
safed vastra,
shant mukh,
jaise chandramā aakash mein aa gaya ho.

Pooja hui.
Shankh aur nagade baje.

Ab rajkumaron ki baari aayi.

Yudhishthira aage the.
Ek ke baad ek
sab shastra-pradarshan karne lage.

Tez ghode,
udte rath,
nishane par lagte teer.

Log hairaan the.
Har taraf se awaaz aayi—
“Shabash! Shabash!”

Talvaar aur dhal chamki.
Sharir ka santulan,
chehre par shanti—
sab kuch adbhut tha.

Phir maidan mein aaye
Bhima aur Duryodhana.

Gada haath mein.
Dono garaj pade
jaise do matwale haathi.

Poora rangmanch
saans rok kar dekh raha tha.

Aur Vidur,
andhe raja Dhritarashtra ko
har drishya shabd mein samjha rahe the.

Conclusion (Saar) 🌸

Yeh sirf khel nahi tha,
yeh bhavishya ka sanket tha.

Yahin se
Bhima aur Duryodhana ke beech
chhupi shatru-ta shuru hui.

Aur yahin duniya ne dekha—
Pandav aur Kaurav
sirf rajkumaar nahi,
balki maha-yoddha ban chuke hain.

Yeh adhyay sikhata hai—
👉 Kala jab pradarshan ban jaaye,
toh kismat ki lakeerein khud likhne lagti hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.73
        with st.expander("Section 1.7.73"):
            text1 = """ 
            Section CXXXVII – Arjuna ka Divya Pradarshan (Hinglish Kahani)

Vaisampayana kehte hain—
jab Duryodhana aur Bhima
arena mein aaye,
toh sabha do hisso mein bat gayi.

Kuch log chillaye,
“Kururon ke raja ko dekho!”

Kuch bole,
“Bhima ko dekho!”

Shor itna badh gaya
jaise samundar mein toofan aa gaya ho."""
            create_image_text_layout("attached_assets/chapter1/1.7.73.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Guru Drona ne dekha.
Unhone turant kaha,
“Asvatthaman,
in dono ko roko.
Yeh yuddh yahin shant hona chahiye.”

Asvatthaman aage badha.
Dono gada-yoddha ruk gaye.
Maahol shaant hua.

Tab Guru Drona bole,
“Ab dekho us shishya ko
jo mujhe apne putra se bhi adhik priya hai.”

Aur tab Arjuna arena mein aaya.

Sone ka kavach.
Haath mein dhanush.
Teeron se bhara tarkash.

Woh aisa chamak raha tha
jaise shaam ka badal
bijli se jagmaga raha ho.

Sabha khushi se bhar gayi.
Shankh baje.
Nagadey goonje.

Awaazein aayi—

“Yeh Kunti ka putra hai!”
“Yeh Pandavon ka madhya bhai hai!”
“Yeh Indra ka ansh hai!”
“Yeh dharma ka rakshak hai!”

Kunti ki aankhon se aansu behne lage.
Maa ka garv
uske chehre par saaf dikh raha tha.

Andhe raja Dhritarashtra ne poocha,
“Vidur,
yeh itna shor kyun?”

Vidur bole,
“Rajann,
Arjuna ne pravesh kiya hai.”

Raja bole,
“Aaj main sach mein dhanya ho gaya.”

Ab Arjuna ne apna kaushal dikhaya.

Aag bani.
Paani bana.
Hawa chali.
Badal garje.

Pahad ubhre.
Zameen phaili.
Aur phir sab gaayab.

Kabhi woh bada dikhta.
Kabhi chhota.
Kabhi rath par.
Kabhi zameen par.

Teer aise chalte
jaise soch se pehle nikal jaate ho.

Sab dekh kar chup the.
Saans bhi dheemi ho gayi.

Jab pradarshan khatam hone wala tha,
achanak gate se zor ka shabd aaya.

Dhamm! Dhamm!

Log dar gaye.
“Kya dharti phat rahi hai?”
“Kya aakash garaj raha hai?”

Sabne gate ki taraf dekha.

Ek taraf Pandav khade the.
Beech mein Guru Drona.
Chand jaise shant.

Doosri taraf Duryodhana khada tha.
Haath mein gada.
Saath mein uske sau bhai.

Woh aisa lag raha tha
jaise koi devta
apni sena ke beech khada ho.

Saar (Moral) 🌿

Yeh sirf pradarshan nahi tha.

Yeh ahankar aur dharma ka pehla saamna tha.

Arjuna ka kaushal
sab par bhari pad gaya.

Aur yahin se
jalan ki aag
aur tez ho gayi.

👉 Kala jab shreshth ho,
toh ahankar hamesha kaamp jaata hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.74
        with st.expander("Section 1.7.74"):
            text1 = """ 
            Section CXXXVIII – Karna ka Pravesh aur Takraav (Hinglish Kahani)

Vaisampayana kehte hain—
jab sab log Arjuna ka adbhut pradarshan dekh kar
abhi bhi hairaan the,
tab bheed ne ek raasta banaya.

Us raaste se Karna arena mein aaya.

Uske sharir par prakritik kavach tha.
Kaanon mein chamakte kundal.
Haath mein dhanush.
Kamar par talwar.

Woh chalta hua
jaise koi pahad chal raha ho."""
            create_image_text_layout("attached_assets/chapter1/1.7.74.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Karna Surya ka putra tha.
Tej mein Surya jaisa.
Sundarta mein Chandra jaisa.
Shakti mein Agni jaisa.

Sab log chup ho gaye.
Sab sochne lage—
“Yeh kaun hai?”

Tab Karna ne garajti hui awaaz mein kaha,
“O Partha,
aaj main woh sab karunga
jo tumne kiya hai—
aur usse bhi aage jaakar.”

Aur sach mein,
usne wahi sab kaushal dikhaya
jo Arjuna ne dikhaya tha.

Bheed phir se goonj uthi.

Duryodhana khushi se uchhal pada.
Usne Karna ko gale lagaya aur bola,
“Tumhara aana mere liye bhaagya hai.
Yeh Kuru rajya bhi tumhara hai!”

Karna ne shaant swar mein kaha,
“Mujhe rajya nahi,
sirf tumhari mitrata chahiye.
Aur Arjuna se yuddh.”

Ab Arjuna ka mann jal utha.
Usne kaha,
“O Karna,
aaj tum mere haathon se bach nahi paoge.”

Karna ne bhi garaj kar uttar diya,
“Yeh arena sabke liye hai.
Yahan baatein nahi,
sirf teer bolte hain!”

Dono yoddha
yuddh ke liye aage badhe.

Aasmaan mein badal chha gaye.
Bijli chamakne lagi.

Indra badalon ke peeche se
Arjuna ko dekh raha tha.
Surya apni kirno se
Karna ko roshan kar raha tha.

Maa Kunti
dono putron ko aamne-saamne dekh kar
behosh ho gayi.

Maa ka hriday
is drishya ko seh nahi paaya.

Tab Kripa bole,
“Yuddh se pehle
apna vansh batao, Karna.
Kshatriya yuddh
barabari mein hota hai.”

Karna ka chehra murjha gaya.
Uske paas jawab nahi tha.

Turant Duryodhana aage aaya.
Usne kaha,
“Yeh yoddha raja hai.
Aaj se Karna
Anga ka raja hai!”

Mantron ke saath
Karna ka rajyabhishek hua.
Rajchhatra uske sir par tha.
Bheed ne taali bajayi.

Karna ne Duryodhana se kaha,
“Tumne mujhe sab kuch diya.
Main tumhara mitra hoon,
jeevan bhar.”

Dono ne gale lagkar
mitrata ka vachan diya.

Saar (Moral) 🌿

Karna ka saahas
uski pehchaan se bada tha.

Duryodhana ne mitrata ko
rajya se bhi upar rakha.

Aur Kunti ke liye,
yeh drishya
maa ke liye sabse bada dukh tha.

👉 Jab ahankar, pehchaan aur mitrata takraate hain,
toh itihaas janm leta hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.75
        with st.expander("Section 1.7.75"):
            text1 = """ 
            Section CXXXIX – Karna, Adhiratha aur Apmaan (Hinglish Kahani)

Vaisampayana kehte hain—
sab kuch shant hone hi wala tha
tab ek buddha vyakti
kaampte hue arena mein aaya.

Woh Adhiratha tha.
Karna ka paalne wala pita.
Kapde dheele the.
Haath mein laathi thi.
Chehra paseene aur thakaan se bhara tha."""
            create_image_text_layout("attached_assets/chapter1/1.7.75.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Adhiratha ko dekhte hi
Karna ne apna dhanush chhod diya.
Rajabhishek ka paani
abhi bhi uske sir par tha.

Usne jhuk kar
apne pita ke charan chhuye.

Adhiratha ne
use gale laga liya.
Aankhon se aansu beh gaye.
Woh bola,
“Tu mera beta hai.”

Yeh dekh kar
Bhima hans pada.
Usne tanz mein kaha,
“O rath haankne wale ka beta!
Tum Arjuna ke yogya nahi ho.
Tum rajya ke bhi layak nahi.”

Uski baat
teer ki tarah lagi.

Karna chup raha.
Uske honth kaanp gaye.
Usne sirf Surya ki taraf dekha.
Kuch nahi bola.

Tab Duryodhana gusse mein khada ho gaya.
Uski awaaz poori sabha mein goonj uthi.

“Shakti hi Kshatriya ka dharm hai!
Vansh nahi, veerta maayne rakhti hai.

Aag paani se nikalti hai.
Vajra haddi se bana.
Devtaon ka vansh bhi anek hai.

Karna Surya jaisa tejwala hai.
Yeh poori prithvi ke yogya hai,
sirf Anga ke rajya ke nahi!”

Sabha mein shor mach gaya.
Kai log Duryodhana ke paksh mein bole.

Tabhi surya ast ho gaya.
Yuddh nahi ho saka.

Duryodhana ne
Karna ka haath pakda
aur deepak se jagmagate arena se
use bahar le gaya.

Pandav bhi
Bhishma, Drona aur Kripa ke saath
wapas laut gaye.

Log jaate hue bol rahe the—
“Koi Arjuna jeeta.”
“Koi Karna.”
“Koi Duryodhana.”

Kunti ne Karna ko dekha.
Uske sharir ke chinh
maa ka hriday pehchaan gaya.

Uska mann khushi aur peeda
dono se bhar gaya.

Aur is tarah,
Duryodhana ne Karna ko paakar
Arjuna se apna darr kam kar liya.

Karna ne bhi
meethi baaton se
Duryodhana ka mann jeet liya.

Aur Yudhishthira ne socha—
“Is dharti par
Karna jaisa yoddha
koi nahi.”

Saar (Moral) 🌱

Janm se bada hota hai karm.

Apmaan chup rehkar bhi saha ja sakta hai.

Sachhi mitrata wahi hai
jo mushkil mein saath khadi rahe.

👉 Karna ki kahani batati hai—
veer hone ke liye
sirf rajkumar hona zaroori nahi."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.76
        with st.expander("Section 1.7.76"):
            text1 = """ 
            Section CXL – Guru Dakshina aur Drupada ki Haar (Hinglish Kahani)

Vaisampayana kehte hain—
jab Pandav aur Kaurav
sabhi shastra-vidya mein nipun ho gaye,
tab Guru Drona ne socha,
“Ab Guru Dakshina ka samay aa gaya hai.”

Ek din unhone sab shishyon ko bulaya
aur shaant swar mein kaha—

“Panchal ke raja Drupada ko
yuddh mein jeet kar
mere saamne le aao.
Yahi meri Guru Dakshina hogi.”

Sab ne ek saath kaha—
“Jaise aap aagya dein, Gurudev.”"""
            create_image_text_layout("attached_assets/chapter1/1.7.76.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Shishya rath par chadhe
aur Panchal ki rajdhani par chadhai ho gayi.
Duryodhana, Karna, Duhshasana—
sab pehle aage badhe.

Lekin jaise hi yuddh shuru hua,
Raja Drupada akela hi
bijli ki tarah ladhne laga.

Uske teeron ki baarish se
Kaurav sena ghabra gayi.
Unhe laga jaise
ek nahi, kai Drupada ladh rahe ho.

Jab sena toot kar bhagi,
tab shor macha—
“Pandavon ko bulao!”

Tab Arjuna ne rath sambhala.
Bhima gadaa le kar
toofan ki tarah aage badha.

Bhima ne haathiyon ko
giraa diya jaise khilone ho.
Khoon aur dhool se
ranbhoomi bhar gayi.

Arjuna ne shant par bhayanak roop mein
Panchal sena ko chhed diya.
Uske teeron mein
rukne ka naam hi nahi tha.

Aakhirkaar Arjuna
seedha Drupada ke rath par chadha.
Usne bina darr ke
Drupada ko pakad liya—
jaise Garud naag ko pakadta hai.

Panchal sena bhaag gayi.

Arjuna ne zor se kaha—
“Yeh raja hamare Guru ka mitra tha.
Kisi ko anavashyak na maaro.
Humein sirf Guru Dakshina deni hai.”

Bhima ruk gaya,
chahe uska mann abhi bhara nahi tha.

Drupada ko
Guru Drona ke saamne laya gaya.
Drupada sharminda tha.
Sir jhuka hua tha.

Drona bole—

“Tumne kabhi kaha tha
ki raja sirf raja ka mitra hota hai.
Aaj main raja hoon.”

Phir muskura kar bole—

“Par hum Brahman kshama karte hain.
Main tumhe aadha rajya wapas deta hoon.
Tum dakshin ke raja raho,
main uttar ka.”

Drupada ne haath jod kar kaha—
“Main aapka mitra hoon.
Aap mahaan ho.”

Par uske mann mein ek baat reh gayi—
“Sirf shastra-bal se
Brahma-bal ko nahi jeeta ja sakta.”

Us din se
Drupada ne ek aise putra ki kaamna ki
jo Drona ko hara sake.

Saar (Moral) 🌱

Guru Dakshina sirf daan nahi, kartavya hoti hai.

Shakti se jeet mil sakti hai,
par kshama se mahaanta.

Ahankar mitrata todta hai,
aur vinamrata naye rishtay jodti hai.

👉 Yeh kahani sikhati hai—
sachhi jeet wahi hoti hai
jisme daya bhi saath ho."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.77
        with st.expander("Section 1.7.77"):
            text1 = """ 
            Section CXLI – Pandavon ki Udaan aur Dhritarashtra ka Darr (Hinglish Kahani)

Vaisampayana bole—

Ek saal beette hi
Dhritarashtra ne
logon ke hit mein
ek bada faisla liya.

Usne Yudhishthira ko
rajya ka yuvaraj bana diya.

Yudhishthira shaant tha.
Dhairyavaan tha.
Dayalu aur sadaa sach bolne wala.

Thode hi samay mein
uska vyavhaar itna uttam ho gaya
ki log
Pandu ke kaamon ko bhi
bhoolne lage."""
            create_image_text_layout("attached_assets/chapter1/1.7.77.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Is dauraan
Bhima ne
Balram se
gada, talwar aur rath yuddh seekha.

Shiksha poori hote hi
Bhima ki shakti
bijli jaisi ho gayi.

Woh apne bhaiyon ke saath
mil-jul kar rehne laga
par shakti mein
kisi se kam nahi tha.

Arjuna ki keerti
har jagah phailne lagi.

Uski pakad majboot thi.
Nishana bilkul sahi.
Hath itna tez
ki aankh follow na kar paaye.

Drona ne khud kaha—

“Arjuna jaisa
is duniya mein
koi dhanurdhar nahi.”

Ek din
Drona ne sabke saamne
Arjuna se kaha—

“Maine apne guru se
Brahmasira astra paaya tha.
Yeh astra
duniya ko bhi jala sakta hai.”

“Ab yeh vidya
shishya se shishya ja sakti hai.”

“Par yaad rakhna—
ise kisi manushya par
kabhi na chalana.”

Phir Drona bole—

“Ab mujhe
apni Guru Dakshina do.”

Arjuna ne bina soche kaha—

“Jo aagya ho, Gurudev.”

Drona bole—

“Jab main tumse yuddh karun,
tum mujhse yuddh karoge.”

Arjuna ne guru ke charan chhoo kar
haan keh di.

Us din
poori dharti par
yeh ghoshna ho gayi—

“Arjuna jaisa
koi dhanurdhar nahi.”

Sahadeva ne
dharma aur neeti ka
poora gyaan paaya.

Nakula
ek uttam yoddha bana.

Aur Arjuna, Bhima ke saath milkar,
kai rajyon ko jeetne laga.

Purab, pashchim,
uttar aur dakshin—
har jagah
Pandavon ka prabhav badhne laga.

Itna dhan aur vijay
Hastinapur pahunchi
ki rajya samriddh ho gaya.

Par…
yeh sab dekh kar
Dhritarashtra ka mann badalne laga.

Pandav majboot ho rahe the.
Log unse pyaar kar rahe the.

Raja ke hriday mein
darr ghus gaya.

Woh raat ko
theek se so bhi
nahi paata tha.

Saar (Moral) 🌱

Gun aur mehnat se
samman milta hai.

Jab sachchai aage badhti hai,
to anyaay dar jaata hai.

Jab shakti badhti hai,
to kamzor mann mein
bhay janm leta hai.

👉 Yahin se
Mahabharat ka
agla andhera
shuru hota hai…"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.7.78
        with st.expander("Section 1.7.78"):
            text1 = """ 
            Section CXLII – Galat Salah ka Beej (Hinglish Moral Kahani)

Vaisampayana bole—

Jab Dhritarashtra ne suna
ki Pandu ke bete
din-ba-din aur zyada shaktishaali ho rahe hain,
toh uska mann
shaant na raha.

Andar hi andar
woh jalne laga.
Usse neend nahi aati thi.
Dil hamesha bhara-bhara rehta tha.

Usne apne sabse tez dimaag wale mantri
Kanika ko bulaya.

Dhritarashtra bola—"""
            create_image_text_layout("attached_assets/chapter1/1.7.78.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Pandav
poori dharti par chha rahe hain.
Mere mann mein jalan hai.
Mujhe nahi pata
unse shanti rakhoon
ya yuddh.”

“Kanika,
sach batao.
Main wahi karunga
jo tum kahoge.”

Kanika muskuraya.
Uski baatein meethi nahi thi.
Par tez thi…
aur khatarnak bhi.

Kanika bola—

“Raja,
raaj chalane ke liye
daya nahi,
chaturai chahiye.”

“Raja ko hamesha
waar ke liye tayaar rehna chahiye.
Apni kamzori chhupaao.
Dushman ki kamzori dhoondo.”

“Dushman ko
chhota mat samajhna.
Chingari bhi
poora jungle jala sakti hai.”

“Jab mauka mile,
toh dushman ko
jad se mita do.
Daya mat dikhao.”

Phir Kanika ne
ek kahani sunayi—

Jungle mein
ek lomdi rehti thi.
Uske dost the—
baagh,
chuha,
bhediya
aur nevala.

Ek din
sabne milkar
ek hiran maara.

Lekin lomdi ne
chal chali.

Usne baagh ko bola—
“Chuha tumhari taakat ka mazaak uda raha hai.”

Baagh chala gaya.

Phir chuhe ko bola—
“Nevala tumhe maarna chahta hai.”

Chuha bhaag gaya.

Phir bhediye ko dara diya.

Aakhir mein
lomdi akeli reh gayi
aur poora shikaar
akeli kha gayi.

Kanika bola—

“Raja,
aise hi
chal se
sabko alag karo
aur khud fayda uthao.”

Kanika aur bhi aage gaya.

Usne kaha—

“Agar apna bhi
dushman ban jaaye,
toh use bhi mat chhodo.”

“Muskurate hue
ghaat karo.”

“Baahar se
dharm ka dikhawa,
andar se
chhura tez.”

“Jab maaro,
toh itna maaro
ki woh dobara
uth na sake.”

Yeh sab sun kar
Dhritarashtra
chup ho gaya.

Uska mann
aur bojhil ho gaya.

Aankhon mein
andhera tha.
Soch mein
bhay aur jalan.

Kanika chala gaya.

Aur Hastinapur ke mahal mein
sirf ek cheez reh gayi—

👉 chinta
👉 bhay
👉 aur galat raah ka beej

Saar (Moral) 🌱

Galat salah
hamesha vinash laati hai.

Chaturai bina dharm
zehar ban jaati hai.

Jalan se liye gaye faisle
poori vansh ko jala dete hain.

👉 Yahin se
Mahabharat ka
anyaay bhara
raasta shuru hota hai…"""
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.8
    with st.expander("Chapter 1.8 – Jatugriha Parva (The House of Lac)"):

        # Section 1.8.1
        with st.expander("Section 1.8.1"):
            text1 = """ 
            Section CXLIII – Lakshagriha ka Saazish aur Pandavon ka Bachav

(Hinglish • short • simple • moral story tone)

Vaisampayana bole:

Duryodhana,
Shakuni ka beta,
Karna aur Duhshasana
sab milkar ek bahut buri saazish banate hain.

Unka plan tha –
Kunti aur paanch Pandavon ko zinda jala dena.

Is saazish ko
raja Dhritarashtra ki bhi manzoori mil jaati hai."""
            create_image_text_layout("attached_assets/chapter1/1.8.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Lekin Vidura bahut buddhimaan the.
Woh chehron ke bhaav dekh kar
logon ka mann padh lete the.

Sirf unke chehre dekh kar hi
Vidura samajh gaye
ki kuch bahut galat hone wala hai.

Unhone turant socha –
Pandavon ko yahan se bhagana hoga.

Vidura chupke se
ek majboot naav (boat) tayaar karwa dete hain,
jo aandhi aur toofan dono seh sake.

Woh Kunti se kehte hain:

“Dhritarashtra
ab dharma se bhatak raha hai.
Maut ka jaal tumhare aas-paas bichha diya gaya hai.

Ganga ke kinaare
ek boat ready hai.
Apne bachchon ke saath
turant nikal jao.”

Yeh sunkar
Kunti ka mann dukhi ho jaata hai.
Lekin apne bachchon ke liye
woh himmat karti hain.

Kunti aur paanch Pandav
raat mein chupchaap
boat mein baith kar
Ganga paar kar jaate hain.

Phir jungle ki taraf nikal jaate hain,
aur Vidura ke kehne par
boat chhod dete hain.

Udhar Lakshagriha
(jo lakdi aur lac se bana ghar tha)
mein aag laga di jaati hai.

Us ghar mein galti se
ek nishad aurat
apne bachchon ke saath jal kar mar jaati hai.

Aur us ghar ka banane wala,
Purochana,
woh bhi usi aag mein jal jaata hai.

Duryodhana aur uske saathi
sochte hain –
“Pandav mar gaye.”

Unki saazish
unhi par ulta pad jaati hai.

Varanavata ke log
jalta hua ghar dekh kar
samajh jaate hain
ki Pandav mar gaye hain.

Sab log bahut dukhi ho jaate hain.
Raja Dhritarashtra ko sandesh bhejte hain:

“Aapka kaam poora ho gaya.
Pandav jal kar mar gaye.”

Dhritarashtra aur uske bete
bahar se dikhawa ka shok karte hain.
Antim sanskaar bhi karwa dete hain.

Lekin sach yeh tha –
Pandav zinda the.
Vidura ki buddhi
unki raksha kar chuki thi.

Janamejaya poochhte hain:

“Yeh lakshagriha wali ghatna
poori batao.
Mujhe sab kuch detail mein sunna hai.”

Vaisampayana aage bole:

Duryodhana ko
Bhima ki taakat
aur Arjuna ki kala
bilkul pasand nahi thi.

Sheher ke log
Yudhishthira ki tareef karne lage:

“Yudhishthira hi
raja banne layak hai.”

Yeh baatein sunkar
Duryodhana ka mann
jalan se bhar gaya.

Woh Dhritarashtra ke paas jaakar bola:

“Pitaji,
log Pandu ke bete ko raja banana chahte hain.

Agar aisa hua,
toh hamara vansh
hamesha ke liye side mein ho jaayega.

Kuch aisa karo
ki hum bhookhe aur par dependent
na ho jaayein.”

✨ Seekh (Moral):
Buddhi aur dharma
saazish se zyada taakatwar hote hain.
Vidura jaise sache log
andhere mein bhi
raasta dikha dete hain."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.2
        with st.expander("Section 1.8.2"):
            text1 = """ 
            Section CXLIV – Pandavon ko Varanavata bhejne ka plan (Hinglish summary)

Vaisampayana kehte hain:

Dhritarashtra ne jab
Duryodhana ki baatein suni
aur Kanika ki purani salah yaad aayi,
toh unka mann duvidha aur shok se bhar gaya.

Tab Duryodhana, Karna, Shakuni
aur Duhshasana
chaaron ne milkar
chupke se salah ki."""
            create_image_text_layout("attached_assets/chapter1/1.8.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔥 Duryodhana ka proposal

Duryodhana ne kaha:

“Pitaji, kisi chaalak tareeke se
Pandavon ko Varanavata bhej dijiye.
Wahaan chale gaye toh
humein unse koi darr nahi rahega.”

⚖️ Dhritarashtra ka dharmic conflict

Dhritarashtra ne jawab diya:

Pandu ne hamesha dharma nibhaya

Rajya bhi mujhe bina lalach de diya

Yudhishthira bhi bilkul waisa hi hai

Log usse pyaar karte hain

Uske saath purane mitra aur sainik hain

“Aise insaan ko zabardasti
kaise nikaala jaa sakta hai?
Kahin log hum sabko
maar hi na daalein?”

🧠 Duryodhana ka chaalak tark

Duryodhana bola:

Pitaji, baat sahi hai

Lekin dhan aur pad se logon ko
apni taraf kiya jaa sakta hai

Treasury aur mantri humare control mein hain

“Bas shanti se, bina jhagda kiye,
Pandavon ko Varanavata bhej do.
Jab main raja ban jaaunga,
tab Kunti aur Pandav wapas aa sakte hain.”

(yeh sirf bolne ki baat thi)

😔 Dhritarashtra ka darr

Dhritarashtra ne kaha:

Yeh vichaar mere mann mein bhi hai

Par yeh bahut paapi hai

Bhishma, Drona, Kripa aur Vidura
kabhi is baat ko nahi maanenge

Unke liye Pandav aur hum barabar hain

“Aisa kiya toh
poori duniya humein doshi samjhegi.”

🐍 Duryodhana ka final manipulation

Duryodhana ne sabka jawab tayaar kar rakha tha:

Bhishma neutral rahenge

Asvatthama mere saath hai
→ Drona bhi mere saath honge

Kripa Drona ka saath chhod nahi sakta

Vidura hum par nirbhar hai
→ akela kuch nahi bigaad sakta

“Isliye bina darr ke
Pandavon ko aaj hi Varanavata bhej do.
Mere mann ki aag bujha do,
jo mujhe sone bhi nahi deti.”

✨ Moral / Arth

Jab irsha (jealousy) buddhi par haavi ho jaaye,
toh dharma bhi kamzor pad jaata hai

Duryodhana ne
har rishte aur maryada ko
raajneeti ke hisaab se tolna shuru kar diya

Yeh hi Lakshagriha ki ghatna
ka pehla official step tha"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.3
        with st.expander("Section 1.8.3"):
            text1 = """ 
            Section CXLV – Pandavon ko Varanavata bhejna (Hinglish kahani)

Vaisampayana bolte hain:

Duryodhana ne dheere-dheere
logon ka mann apni taraf karna shuru kar diya.
Kahin dhan baant kar,
kahin samman dekar.
Log chupchaap uske saath aane lage.

Isi beech,
Dhritarashtra ke kehne par,
kuch chaalak mantri
ek din sabha mein
Varanavata ki tareef karne lage."""
            create_image_text_layout("attached_assets/chapter1/1.8.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🎉 Varanavata ka jhootha rang

Mantri bole:

“Varanavata mein
Pasupati (Shiv ji) ka maha-utsav chal raha hai.
Logon ki bheed dekhi nahi jaati.
Juloos itna sundar hai
ki duniya mein uska koi jawab nahi.

Sheher sajha hua hai,
gehno se chamak raha hai,
jo dekhe bas dekhta hi reh jaaye.”

🌱 Pandavon ke mann mein ichchha

Ye baatein sunte-sunte
Pandavon ke mann mein bhi
Varanavata jaane ki ichchha jaag uthi.

Dhritarashtra ne jab dekha
ki unka mann tayaar ho raha hai,
toh unhone turant kaha:

🎭 Dhritarashtra ka meetha nimantran

“Beta,
mere log Varanavata ki
bahut tareef karte rehte hain.

Agar tum festival dekhna chahte ho,
toh apne mitron aur logon ke saath
wahaan jao.

Brahmanon aur gaayakon ko
motiyon aur ratnon ka daan karo.
Kuch samay wahaan khushi se raho,
devtaon ki tarah anand lo,
phir wapas Hastinapur aa jaana.”

(Baat meethi thi,
par mann mein kuch aur tha)

🧠 Yudhishthira ka samajhdaar jawab

Yudhishthira sab samajh gaye the.
Unhe Dhritarashtra ka asal iraada dikh raha tha.
Par wo jaante the:

hum kamzor hain

humare paas shakti nahi

virodh karna abhi sahi nahi

Isliye shant swar mein bole:

👉 “So be it.”
(“Jaise aap chahein.”)

🙏 Sabse aashirvaad lena

Phir Yudhishthira ne
sab bade-buzurgon ko
namrata se sambodhit kiya:

Bhishma, Vidura, Drona, Kripa,
Ashwatthama, Gandhari,
sab mantri, brahman, rishi
aur sheher ke log.

Unhone kaha:

“Hum Dhritarashtra ke aadesh se
Varanavata jaa rahe hain.
Kripya humein aashirvaad dijiye,
taaki humein samriddhi mile
aur hum paap se bache rahein.”

🌼 Aashirvaad aur vidai

Sab Kaurav bade
khushi-khushi bole:

“Pandavon,
sab devta tumhari raksha karein.
Tumhare raaste mein
koi bhi buraai na aaye.”

🚶‍♂️ Yatra ki shuruaat

Pandavon ne
shubh kriyaein ki,
tayyari poori ki
aur Varanavata ki yatra par nikal pade.

Unhe nahi pata tha
ki aage chal kar
yeh sheher
unke liye agni-pariksha banne wala hai…

✨ Moral / Seekh

Kabhi-kabhi badi muskaan ke peeche
gehra shadayantra chhupa hota hai

Yudhishthira ka shant rehna
kamzori nahi,
samyak buddhi thi

Yeh kahani sikhati hai
ki har yuddh talwar se nahi,
samay aur dhairya se jeeta jaata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.4
        with st.expander("Section 1.8.4"):
            text1 = """ 
            Section CXLVI – Lakshagriha ka shadayantra (Hinglish kahani)

Vaisampayana bolte hain:

Jab Dhritarashtra ne
Pandavon ko Varanavata bhejne ki baat maan li,
toh Duryodhana ka mann khushi se bhar gaya.
Uske chehre par muskaan thi,
par dil mein andhera plan."""
            create_image_text_layout("attached_assets/chapter1/1.8.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😈 Purochana se gupt baat

Duryodhana ne
apne vishwasniya aadmi Purochana ko
chupke se bulaya.
Uska haath pakad kar bola:

“Purochana,
yeh duniya jo dhan se bhari hai,
meri hai… aur utni hi teri bhi.
Isliye iski raksha tumhari zimmedari hai.

Tum mere sabse vishwasniya aadmi ho.
Isliye mera kaam
chalaaki se poora karo.”

🏰 Lakshagriha ka plan

Duryodhana bola:

“Pandav ab
Dhritarashtra ke kehne par
Varanavata jaa rahe hain.
Tum aaj hi
tez khachar-wali gaadi mein
wahaan pahunch jao.

Wahaan tum
ek chaar-kona mahal banwao.
Bahut sundar dikhe,
sabse accha ho,
taaki kisi ko shaq na ho.

Lekin yaad rakhna—
us mahal mein istemal karna:

laakh (lac)

tel

ghee

charbi

san aur rassi

lakdi

Sab jalne wali cheezein.”

🔥 Aag chhupi ho, dikhe na

Duryodhana aage bola:

“Deewaron par
mitti, ghee aur laakh mila kar
aisa lep lagana
ki koi bhi pehchaan na paaye
ki yeh ghar jal sakta hai.

Har taraf
aise chhupa kar samaan rakhna
ki dekhne wala
kuch samajh hi na paaye.”

🎭 Pandavon ka bharosa jeetna

“Jab mahal tayaar ho jaaye,
toh Pandavon ko
bade samman ke saath
wahaan rehne ko bulaana.

Unke liye
acche palang,
gaadiyaan,
baithne ke aasan
sab kuch badhiya rakhna.

Aisa lage
jaise Dhritarashtra ne
khud dhyaan rakha ho.”

🌙 Raat ka andhera, maut ka pal

Duryodhana ne dheere se kaha:

“Jab tumhe pakka ho jaaye
ki Pandav
aur Kunti
nishchint hokar
ghar ke andar so rahe hain…

👉 tab bahar ke darwaaze se aag laga dena.

Pandav jal kar mar jaayenge,
aur log kahenge
yeh sirf ek durghatna thi.”

🏃‍♂️ Purochana ka rawana

Purochana ne sir jhuka kar kaha:

👉 “So be it.”

Aur bina der kiye,
tez khachar-wali gaadi mein
Varanavata ki taraf nikal pada.

Wahaan pahunch kar,
usne bilkul wahi kiya
jo Duryodhana ne kaha tha.

Lakshagriha banne lagi…
aur maut
chupchaap uske saath chal rahi thi.

🌑 Moral / Seekh

Jo bahar se sundar dikhe,
zaroori nahi andar se surakshit ho

Lalach aur jalan
aadmi ko andha bana deti hai

Par dharm aur buddhi
hamesha andhere se raasta dhoondh leti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.5
        with st.expander("Section 1.8.5"):
            text1 = """ 
            Section CXLVII – Vidura ka gupt sandesh (Hinglish kahani)

Vaisampayana bolte hain:

Pandav
apni rathon par chadhne lage.
Ghode hawa jaise tez the.
Par unke mann
bohot bhaari the 💔"""
            create_image_text_layout("attached_assets/chapter1/1.8.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🙏 Antim pranam

Rath par chadhne se pehle,
Pandavon ne
Bhishma, Dhritarashtra, Drona, Kripa, Vidura
aur sabhi bade buzurgon ke
charan chhoo kar pranam kiya.

Unki aankhon mein aansu the.
Dil mein dukh tha.

Phir apne barabari walon ko gale lagaya,
bachchon se vida li,
ghar ki sabhi mahilaon ko
shraddha se pranam kiya.

Shehar ke nagrikon ko
antim baar dekha…
aur Varanavata ki aur nikal pade.

😢 Shehar walon ka dukh

Vidura, Bhishma
aur kai nagrik
Pandavon ke saath
kaafi door tak chale.

Log ro rahe the.
Aur zor zor se keh rahe the:

“Dhritarashtra
ek hi nazar se sabko nahi dekhte.
Unhone dharm ko bhula diya hai!

Yudhishthira paapi nahi.
Bhima anyayi nahi.
Arjuna kabhi vidroh nahi karega.

Phir bhi inhe vanvaas?
Ye anyaay hai!

Agar Pandav ja rahe hain,
toh hum bhi shehar chhod denge!”

🌼 Yudhishthira ka shant uttar

Yudhishthira ne
thoda socha.
Dil dukh se bhara tha,
par awaaz shant thi.

Unhone kaha:

“Raja hamare pita samaan hain.
Guru hain.
Bade hain.

Unka aadesh maanna
hamara kartavya hai.

Aap sab hamare mitra ho.
Aapka pyaar
hamare saath rahega.

Aashirvaad dekar
apne ghar laut jaaiye.
Jab samay aayega,
tab ham aapko yaad karenge.”

Log chup ho gaye.
Pandavon ko ashirvaad diya.
Aur dheere dheere
wapas laut gaye.

🔐 Vidura ka gupt sandesh

Jab sab log peeche reh gaye,
tab Vidura
Yudhishthira ke paas aaye.

Unhone
Mleccha bhasha mein baat ki.
Aisi bhasha
jo sirf Yudhishthira samajh sake.

Vidura bole:

“Jo dushman ki chaal jaanta hai,
wo bach sakta hai.

Kuch hathiyaar
loha ke nahi hote,
phir bhi maar dete hain.

Aisi aag hoti hai
jo bahar se nahi dikhti.

Jo apni indriyon par niyantran rakhe,
use koi hara nahi sakta.

Jo ghar
dushman de,
usme hamesha
nikalne ke raaste hone chahiye.

Yaad rakhna…
samajhdaar aadmi
andhere mein bhi raasta dhoond leta hai.”

🤫 “Main samajh gaya”

Yudhishthira ne
sir jhuka kar
sirf itna kaha:

👉 “Main samajh gaya.”

Bas.
Aur kuch nahi.

Vidura ne unhe pranam kiya,
ek baar mud kar dekha,
aur laut gaye.

👩‍👦 Kunti ka prashn

Thodi der baad,
Kunti Yudhishthira ke paas aayi.

Boli:

“Vidura ne
tumse ajeeb si baat ki.
Aur tumne bhi.

Hum kuch samajh nahi paaye.
Agar galat na ho,
toh hume bhi batao.”

🔥 Sach ka khulasa

Yudhishthira bole:

“Vidura ne kaha
ki jo mahal
hamare liye banaya ja raha hai,
wo jalne wali cheezon se bana hai.

Unhone kaha
nikalne ka raasta
bhi pata hona chahiye.

Aur jo apne mann ko vash mein rakhe,
wo sab kuch paa sakta hai.

Isliye maine kaha—
‘Main samajh gaya.’”

Kunti ne gehri saans li.
Unki aankhon mein chinta thi…
par vishwas bhi.

🌟 Yatra ka aarambh

Phalguna mahine ka
aathva din tha.
Rohini nakshatra chamak raha tha ✨

Pandav
Varanavata pahunche.
Shehar sundar tha.
Log hans rahe the.

Par kahani ka
andhera hissa
ab shuru hone wala tha…

🌱 Seekh (Moral)

Jo shabd seedhe na ho,
unmein bhi sach chhupa hota hai

Buddhi aur shanti
aag se bhi raasta nikaal leti hai

Dharm ka saath ho,
toh sabse bada shadayantra bhi haar jaata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.6
        with st.expander("Section 1.8.6"):
            text1 = """ 
            Section CXLVIII – Lakshagriha ka sach (Hinglish mein samjhaaya hua)
            Vaisampayana kehte hain:

🎉 Varanavata mein Pandavon ka bhavya swagat

Jaise hi Pandav Varanavata pahunche,
shehar ke log khushi se jhoom uthe.

Hazaaron rath, gaadiyan,

shastraon ke anusaar shubh samagri,

“Jaya! Jaya!” ke naare

Sab log Pandavon ko gher kar khade ho gaye.
Yudhishthira unke beech Indra jaise chamak rahe the.

Pandav pehle:

Brahmanon ke ghar gaye

Phir rajkarmiyon, Suton, Vaishyon

Aur Shudron ke ghar bhi
— sabko samman diya, sabse milkar.

Aakhir mein Purocana unhe us mahal tak le gaya
jo usne banwaya tha."""
            create_image_text_layout("attached_assets/chapter1/1.8.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🏠 “Blessed Home” – naam shubh, sach shraapit

Pandav wahan 10 raat rahe.
Sab kuch shandar tha—
khana, bistar, kapde, seva.

Phir Purocana ne kaha:

“Is ghar ka naam hai Shubh Grih (Blessed Home).”

Pandav us ghar mein gaye…
lekin Yudhishthira ne jaise hi ghar ko dekha aur sugandh mehsoos ki—
unhe sach samajh aa gaya.

🔥 Yudhishthira ka khulaasa

Yudhishthira ne Bhima se kaha:

“Is ghar mein
ghee, charbi, lac, resins, baans, ghaas
sab bhare hue hain.
Ye ghar aag pakadne ke liye hi bana hai.”

Unhone spasht kaha:

Ye Duryodhana ki yojana hai

Purocana yahan isliye hai
taaki mauka milte hi
humein jala de

Aur phir Vidura ki baat yaad dilayi:

“Vidura pehle hi humein chetavani de chuke the.”

💪 Bhima ka seedha prashn

Bhima bole:

“Agar ghar hi aisa hai
toh hum pehle wale ghar mein kyun na laut jaayein?”

🧠 Yudhishthira ki buddhi bhari rananiti

Yudhishthira ne shant par gehri baat kahi:

Agar hum ghabra gaye,
toh Purocana turant aag laga dega

Agar hum bhaag gaye,
toh Duryodhana
jasooson se humein marwa dega

Hamare paas:

na sena

na rajya

na dhan
Par Duryodhana ke paas sab kuch hai

Isliye unka faisla:

“Hum yahin rahenge,
bilkul nirdosh aur anjaan ban kar
par poori satarkta ke saath.”

🕳️ Sabse bada rahasya – surang (tunnel)

Yudhishthira ne kaha:

Isi raat
apne kamre se
ek gupt underground raasta khudwayenge

Kisi ko pata nahi chalega

Na Purocana

Na shehar ke log

Aur saath hi:

Shikaar ke bahane jungle jaayenge

Raaston se parichit ho jaayenge

Zarurat padi toh turant nikal sakenge

“Agar hum aisa karein,
toh aag bhi humein nahi jala paayegi.”

🌱 Is section ki gehri seekh

Sirf shakti nahi, buddhi jeet dilati hai

Jo dikh raha hai,
sach hamesha wahi nahi hota

Shant rehkar, dhoop mein bhi
chhaaya ka raasta banaya ja sakta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.7
        with st.expander("Section 1.8.7"):
            text1 = """ 
            Section CXLIX – Gupt Surang aur Vidura ka Vishwas
            Vaisampayana bole:

Ek raat, Vidura ka ek vishwasniya mitra chupke se Pandavon ke paas aaya.
Woh khadan (mining) ka expert tha.

Usne dheere se kaha:

“Mujhe Vidura ne bheja hai.
Main surang banane mein nipun hoon.
Bataiye, main aapki kya seva karun?”

Phir usne apni pehchaan di:

Vidura ne use sab kuch bataya tha

Purocana ka plan

Andheri paksh ki 14vi raat

Darwaze se aag lagane ka irada

Usne kaha:"""
            create_image_text_layout("attached_assets/chapter1/1.8.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            “Pandavon ko aur unki mata Kunti ko
zinda jala dena
Duryodhana ka sabse bada sapna hai.”

Aur usne woh gupt baat bhi batayi
jo Vidura aur Yudhishthira
sirf Mleccha bhasha mein samajhte the.

Yeh sunte hi
Yudhishthira samajh gaye
ki yeh vyakti sach mein Vidura ka hi bheja hua hai.

🤝 Yudhishthira ka bharosa

Yudhishthira ne shaant swar mein kaha:

“Ab mujhe koi sandeh nahi.
Tum Vidura jaise hi ho,
hamare apne.”

Phir unhone sach khol diya:

Yeh ghar jalne ke liye bana hai

Purocana sirf mauka dhoondh raha hai

Duryodhana ke paas

dhan hai

mitra hai

shakti hai

Yudhishthira bole:

“Agar hum yahan jal gaye,
toh Duryodhana jeet jaayega.
Isliye humein chupchaap bachna hoga.”

Unhone miner se prarthna ki:

“Bina Purocana ko pata chale,
humein is aag se bacha lo.”

🕳️ Surang ka kaam shuru

Miner ne sir jhuka kar kaha:

“Aisa hi hoga.”

Usne raat ke andhere mein
ghar ke beech se
ek badi underground surang khodni shuru ki.

Surang ka muh:

farsh ke barabar

lakdi ke takhton se dhaka hua

Bahar se kisi ko shak na ho

Purocana roz darwaze par nazar rakhta tha

🏹 Pandavon ki dincharya

Raat ko:

Pandav sote

par hathiyaar paas rakhte

Din mein:

shikaar ke bahane

jungle-jungle ghoomte

raaston ko yaad karte

Bahari duniya ke liye:

Pandav khush lagte the

Nirdosh lagte the

Bharose mein lagte the

Par andar se:

Woh satark the

tayyar the

samay ka intezaar kar rahe the

🌑 Gupt yojana ka raaz

Is poori yojana ke baare mein:

Na shehar ko pata tha

Na Purocana ko

Na kisi aur ko

Sirf 6 log jaante the:

Kunti

5 Pandav

aur Vidura ka mitra

🌟 Is kahani ki seekh

Kabhi-kabhi chup rehna bhi shakti hoti hai

Asli mitra
andhere mein raasta banata hai

Jo dhairya rakhta hai,
wahi aag se bhi bach jaata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.8
        with st.expander("Section 1.8.8"):
            text1 = """ 
            Section CL – Aag, Andhera aur Pandavon ka Palayan
            Vaisampayana bole:

Ek poora saal beet gaya.
Pandav us ghar mein khush aur nishchint dikhte rahe.
Yeh dekh kar Purocana bahut khush ho gaya.
Usse laga,
“Sab kuch bilkul mere control mein hai.”

Par asli khel toh aur hi tha.

🔥 Yudhishthira ka sanket

Ek din Yudhishthira ne Bhima, Arjuna aur Nakula–Sahadeva se dheere se kaha:

“Woh paapi poori tarah dhokha kha chuka hai.
Ab nikalne ka samay aa gaya hai.
Is ghar ko jala do.
Purocana ko yahin chhod do.
Aur hum chhupkar nikal jaayenge.”

Sab bhai shaant the.
Par taiyaar."""
            create_image_text_layout("attached_assets/chapter1/1.8.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🍚 Us raat ka bhoj

Us raat Kunti mata ne daan-bhoj rakha.
Bahut se Brahman,
aur shehar ki auratein aayi.

Sabne khaya, piya
aur apne ghar laut gaye.

Tab bhagya se
ek Nishad aurat bhi wahan aa gayi.
Uske paanch bachche bhi saath the.

Sabne zyada peene ki wajah se
hosh kho diya

Woh aur uske bachche
ghar ke andar hi so gaye

Kisi ko kuch pata nahi tha.

🌪️ Aandhi aur aag

Raat gehri ho chuki thi.
Tez hawa chalne lagi.

Tab Bhima utha.

Pehle Purocana ke kamre mein aag lagayi

Phir darwaze par

Phir ghar ke chaaron taraf

Aag bhadak uthi.
Lak ka ghar jalne laga.

🕳️ Surang ka raasta

Jab pakka ho gaya
ki aag poore ghar mein phail chuki hai,
tab:

Kunti mata

paanch Pandav

turant underground surang mein ghus gaye.

Bina shor.
Bina rukke.

😢 Shehar ka dard

Aag ki garmi aur awaaz se
poora shehar jaag gaya.

Log rote hue bole:

“Yeh sab Duryodhana ka paap hai!”
“Nirdosh Pandav jal gaye!”
“Purocana ne jo khud gaddha khoda tha,
usmein khud hi jal gaya!”

Poora shehar
raat bhar ghar ke aas-paas khada raha.

Par Pandav…
kahin aur nikal chuke the.

💪 Bhima ka adbhut bal

Andhera tha.
Darr bhi tha.
Mata ke saath tez chalna mushkil tha.

Tab Bhima aage aaya.

Mata ko kandhe par uthaya

Nakula–Sahadeva ko side mein

Yudhishthira aur Arjuna ko baahon mein

Aur woh andhere jungle mein daud pada.

Ped toot-te gaye

Zameen dhans-ti gayi

Bhima hawa ki tarah aage badhta gaya

🌄 Is kahani ki seekh

Dhokha hamesha jeet nahi paata

Chupchaap ki gayi sahi planning
sabse badi shakti hoti hai

Aur jab bhai saath ho,
toh andhera bhi raasta de deta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.9
        with st.expander("Section 1.8.9"):
            text1 = """ 
            Section CLI – Vidura ka Vishwas, Ganga aur Pandavon ki Raksha
            Vaisampayana bole:

Isi samay, Vidura, jo sab kuch door se bhi samajhne wale the,
ne jungle ki taraf ek vishwasniya purush ko bheja—
ek aisa vyakti jiska charitra shuddh tha
aur jo Vidura ka poora bharosa jeetta tha.

🌲 Jungle mein mulaqat

Woh vyakti us jagah pahuncha
jahaan Pandav apni mata Kunti ke saath
ek nadi ki gehraai naap rahe the—
yeh jaanch rahe the ki kaunsa raasta surakshit hai.

Vidura ko pehle hi
Duryodhana ke gupt yojna ka pata chal chuka tha
apne jaasuson ke zariye.
Isliye yeh madad bilkul samay par pahunchi."""
            create_image_text_layout("attached_assets/chapter1/1.8.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🚣 Ganga ke kinaare taiyaar nauka

Us vyakti ne Pandavon ko
Ganga ke pavitra tat par
ek mazboot nauka dikhayi:

tez hawa aur lehron ko jhelne wali

jisme yantra aur jhande lage the

jo toofan ya vichaar ki gati se chal sakti thi

Yeh sab Vidura ke bharosemand shilpiyon ne banaya tha.

🔑 Vidura ka gupt sandesh (pehchaan ka pramaan)

Us purush ne kaha:

“Yudhishthira,
yeh shabd Vidura ne kahe the—
‘Na lakdi jalane wali aag,
na os sukhaane wali hawa,
jungle ke bil mein rehne walon ko jala sakti hai.’

In shabdon se pehchaan lo
ki main sach mein Vidura ka hi bheja hua hoon.”

Pandav samajh gaye.
Yeh wahi gupt bhaasha thi.

Phir usne aur kaha:

“Vidura ne kaha hai—
tum avashya Karna, Duryodhana,
uske bhaiyon aur Shakuni ko yudh mein haraoge.
Yeh nauka tum sabko surakshit
in pradeshon se paar le jaayegi.”

🌊 Ganga paar

Pandav aur Kunti mata
mann mein dukh liye
par himmat banaye hue
nauka mein chadh gaye.

Vidura ka dūt
khud unke saath gaya.

Usne kaha:

“Vidura ne mann hi mann
tum sabko gale lagaya hai
aur kaha hai—
‘Aage ke safar mein kabhi asavdhaan mat hona.’”

Nauka shaant lehron par chali…
aur Pandav surakshit roop se Ganga ke us paar pahunch gaye.

✨ Vidai aur Vijay

Us vyakti ne:

Pandavon ko ‘Jaya!’ kaha

Unki safalta ki kaamna ki

Aur chupchaap wapas laut gaya

Pandav bhi
Vidura ke liye sandesh bhej kar
ab aur gehre jungle ki taraf
bilkul gupt roop se aage badhne lage.

🌟 Is khand ki seekh

Vidura jaise log door rehkar bhi raksha karte hain

Sahi samay par sahi madad
poori kismat badal deti hai

Ganga ke paar jaana sirf yatra nahi,
balki purani zindagi ka ant
aur nayi yatra ki shuruaat thi"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.10
        with st.expander("Section 1.8.10"):
            text1 = """ 
            Section CLII – Aag ke Baad ka Sach aur Jungle ki Andheri Yatra
            Vaisampayana bole:

Subah hui.
Raat guzar chuki thi.
Shehar ke log tez-tez bhaagte hue
Pandavon ko dekhne aaye.

🔥 Jali hui lakshagriha

Aag bujha di gayi thi.
Logon ne dekha—

Ghar poora lac aur jalne wale saman se bana tha

Purochana usi aag mein jal chuka tha

Tab log zor-zor se rone lage.

“Yeh sab Duryodhana ki yojna thi!”
“Dhritarashtra ko pata hoga, tabhi toh yeh hua!”
“Pandavon ko jalne se kyun nahi bachaya gaya?”

Log gusse aur dukh se bhar gaye."""
            create_image_text_layout("attached_assets/chapter1/1.8.10.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😢 Galat samajh aur jhootha sandesh

Raakh hatate hue
logon ko ek Nishada aurat aur uske paanch bachche mile—
sab jal chuke the.

Vidura ke bheje hue khani-kaam jaanne wale vyakti ne
chupchaap
gaddhe ke muh ko raakh se dhak diya,
taaki koi sach na jaan paaye.

Phir sandesh bheja gaya Hastinapur:

“Pandav aur Purochana
sab jal kar mar gaye.”

🕯️ Hastinapur ka dikhawa

Yeh sun kar Dhritarashtra roya.
Usne kaha:

“Lagta hai aaj hi
mere bhai Pandu bhi mar gaye.”

Antim kriya ka aadesh diya gaya.
Paani chadhaya gaya.
Sab log rote rahe:

“O Yudhishthira!”
“O Bhima!”
“O Arjuna!”
“O Nakula-Sahadeva!”
“O Kunti!”

Sirf Vidura kam roya,
kyunki woh sach jaanta tha.

🌌 Udhar… Pandav zinda the

Isi beech,
Pandav aur Kunti mata
Varanavata chhod chuke the.

Woh Ganga ke kinaare pahunche.
Nauka se us paar gaye.
Phir andheri raat mein
taaron ki roshni dekh kar
south ki taraf chal pade.

🌲 Gehra jungle aur thakaan

Bahut chalne ke baad
woh ghane jungle mein pahunch gaye.

Sab thak chuke the.
Pyaas lagi thi.
Neend aankhon ko bandh kar rahi thi.

Tab Yudhishthira ne Bhima se kaha:

“Isse zyada kasht kya hoga?
Humein rasta bhi nahi pata.
Pata nahi Purochana mara ya nahi.

Bhima…
tum hi sabse taqatwar ho.
Humein uthakar
aage le chalo.”

💪 Bhima ka bal

Yudhishthira ki baat sun kar
Bhima bina kuch bole—

Maa Kunti ko kandhe par uthaya

Bhaiyon ko apni baahon mein liya

Aur hawa ki tarah tez
andheri jungle mein chal pada.

🌟 Is hissa ki seekh

Jo dikhta hai, hamesha sach nahi hota

Samajh aur sabr
jaan bacha sakte hain

Bhima ka bal sirf shakti nahi,
parivaar ke liye pyaar bhi tha"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.8.11
        with st.expander("Section 1.8.11"):
            text1 = """ 
            Section CLIII – Jungle ki Andheri Raat aur Bhima ka Dard
            Vaisampayana bole:

Bhima aage badhta gaya.
Uske kadmon se jungle kaanp raha tha.
Ped aur belen
uske seene se takra kar
toot rahi thi.

Uski janghon ki gati se
garmi wali hawa chalne lagi,
jaise garmiyon ke mahine mein hota hai.

Bhima raasta banata hua chala.
Bade-bade ped
phool, phal ke saath
zameen par girte gaye.

Woh pagal haathi jaisa lag raha tha—
taqat se bhara,
gusse se bhara,
aur rukne wala nahi."""
            create_image_text_layout("attached_assets/chapter1/1.8.11.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Nadi, bhesh aur maa ka bojh

Raaste mein kai nadiyan aayi.
Bhima ne tair kar paar kiya.
Pandav apna bhesh badalte gaye,
taaki Kauravon ke jaasoos
pehchaan na paaye.

Bhima ne
Kunti maa ko kandhe par uthaya,
aur pathrile kinaaron se
sambhal-sambhal kar chalaya.

🌌 Shaam ka andhera

Shaam hote-hote
woh ek bhayanak jungle mein pahunch gaye.

Phal kam the

Paani mushkil se milta

Pakshiyon aur jaanwaron ki
darawani awaazein aa rahi thi

Andhera gehra ho gaya.
Tez hawa chali.
Ped tootne lage.

Pandav thak chuke the.
Pyaas se behaal the.
Neend aankhon par bhaari thi.

Sab bhookhe aur pyaase
wahin baith gaye.

💧 Maa ki pyaas

Tab Kunti maa ne kaha:

“Main paanch Pandavon ki maa hoon…
par mujhe bahut pyaas lag rahi hai.”

Unhone yeh baat
baar-baar kahi.

Yeh sun kar
Bhima ka dil bhar aaya.
Maa ke liye uska mann
karuna se bhar gaya.

🌳 Bargad ka ped

Bhima aage chala
aur ek bada bargad ka ped dekha.

Usne maa aur bhaiyon ko
wahin sula diya.

Phir bola:

“Tum yahin aaram karo.
Mujhe paani ki awaaz aa rahi hai.
Yahin kahin talab hoga.”

Yudhishthira ne kaha:
“Jao.”

Bhima chala gaya
pakshiyon ki awaaz ki taraf.

🏞️ Paani mila

Thodi door jaakar
Bhima ne ek talab dekha.

Usne paani piya.
Nahaya.
Aur phir
apne kapdon mein paani bhigo kar
wapas le aaya.

Tez kadmon se
char kos chal kar
maa ke paas pahuncha.

😢 Bhima ka aansuon bhara mann

Maa aur bhai
nangi zameen par so rahe the.

Yeh dekh kar
Bhima ro pada.

“Arey bhagya!
Mere bhai
jo kabhi naram bistar par sote the,
aaj zameen par so rahe hain!

Meri maa Kunti—
jo rajmahal mein rahi,
aaj thaki hui
zameen par so rahi hai!

Yudhishthira,
jo teen lok ka raja ban sakta hai,
aaj aam insaan ki tarah so raha hai!

Arjuna,
jo badalon jaisa sundar hai,
zameen par pada hai!

Nakula aur Sahadeva—
jo Ashwini Kumaron jaise sundar hain—
bhi zameen par so rahe hain!”

🔥 Krodh aur sanyam

Bhima ka gussa phoot pada.

“Duryodhana!
Tum abhi zinda ho
sirf isliye
kyunki Yudhishthira mujhe rok raha hai!

Agar unhone kaha hota,
toh aaj hi
main tum sabko Yama ke paas bhej deta!”

Par phir
Bhima ne apne gusse ko
rok liya.

🌙 Raat ka pehra

Bhima ne socha:

“Yahin kahin koi basti hogi.
Sab so rahe hain.
Main jaag kar pehra dunga.”

Aur woh
poori raat jaagta raha,
maa aur bhaiyon ki raksha karta raha.

Conclusion – Is Kahani ki Seekh 🌟

Sachcha bal sirf taqat nahi, zimmedari hota hai

Bhima ka gussa bhi tha,
par sanyam usse bada tha

Maa ke liye pyaar
aur bhaiyon ke liye raksha
hi uski asli shakti thi"""
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.9
    with st.expander("Chapter 1.9 – Hidimva-vadha Parva (Slaying of Hidimva)"):

        # Section 1.9.1
        with st.expander("Section 1.9.1"):
            text1 = """ 
            Section CLIV – Bhima aur Hidimba
            Pandav gehri jungle mein so rahe the.
Raat shaant thi.
Par paas hi ek Rakshas Hidimva rehta tha.

Hidimva bahut bhayanak tha.
Lambe daant.
Laal aankhen.
Insaan ka maans khane wala.

Usse bhook lagi thi.
Hawa mein insaan ki khushboo mehki.
Usne Pandavon ko dekh liya.

Woh khush ho gaya.
Aur apni behen Hidimba ko bola:

“Behna,
jao aur dekho kaun hai.
Unhe maar kar le aao.
Aaj hum daawat karenge.”"""
            create_image_text_layout("attached_assets/chapter1/1.9.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌙 Hidimba ka mann badalna

Hidimba wahan pahunchi.
Usne dekha —
Pandav so rahe hain.
Kunti maa bhi so rahi hain.

Par ek yodha jaag raha tha.
Bhima.

Hidimba ne Bhima ko dekha.
Mazboot.
Tez.
Sone jaisa chamakta shareer.

Uska dil pighal gaya.
Woh sochne lagi:

“Yeh purush mere yogya hai.
Main apne bhai ka hukm nahi maanungi.
Ek patni ka prem
bhai ke darr se bada hota hai.”

Usne Rakshasi roop chhod diya.
Insaan ka sundar roop dhar liya.
Aur dheere dheere Bhima ke paas aayi.

💬 Hidimba ka sach

Hidimba ne Bhima se kaha:

“Veer,
yeh jungle Rakshason ka hai.
Mera bhai Hidimva
tum sabko maarna chahta hai.

Par tumhe dekh kar
mera dil tumhara ho gaya.
Main tumse vivaah karna chahti hoon.

Main tum sabko bacha sakti hoon.
Mujhe apni patni bana lo.
Hum pahadon par khushi se rahenge.”

🛡️ Bhima ka dharm

Bhima ne shant awaaz mein jawab diya:

“Main kaise
apni maa aur bhaiyon ko
sote hue chhod sakta hoon?

Koi bhi purush
apni zimmedari chhod kar
apna sukh nahi chunta.

Main kisi Rakshas se nahi darta.
Chahe tumhara bhai aaye,
main taiyaar hoon.”

Hidimba boli:
“Main sabko bacha loongi.”

Bhima ne kaha:

“Dar ke kaaran
main kisi ko jagaunga nahi.
Mera bal kaafi hai.

Tum chaho toh jao.
Chaho toh apne bhai ko bhejo.
Main yahin khada hoon.”

🌱 Is kahani ki seekh

Prem tab pavitra hota hai jab woh dharm ke saath ho

Parivaar aur kartavya, apni ichha se bade hote hain

Sacha veer pehle raksha karta hai, phir apna sukh dekhta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.2
        with st.expander("Section 1.9.2"):
            text1 = """ 
            Section CLV – Bhima vs Hidimva
            Pandav gehri neend mein so rahe the.
Bhima jaag kar pehra de raha tha.

Tab Rakshas Hidimva, jo insaan ka maans khata tha,
ped se neeche utra.
Laal aankhen, bhayanak daant,
baadal jaise shareer ke saath
woh gusse mein aage badha.

⚠️ Hidimba ka darr

Hidimba ne apne bhai ko aate dekha.
Woh ghabra gayi aur Bhima se boli:

“Veer Bhima,
yeh rakshas bahut balwaan hai.
Main tum sabko utha kar
aasmaan ke raaste le ja sakti hoon.
Maa Kunti aur bhaiyon ko jaga do.”"""
            create_image_text_layout("attached_assets/chapter1/1.9.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🛡️ Bhima ka atoot vishwas

Bhima shaant raha aur bola:

“Dar mat,
jab tak main yahan hoon,
koi rakshas inhe haani nahi pahuncha sakta.

Main ise tumhare saamne maar dunga.
Yeh meri takkar ka nahi hai.”

Usne apni bhujaen,
apna seena,
apni taangein dikhayi
— jaise lohe ke gade.

😡 Hidimva ka krodh

Hidimva ne dekha
uski behen sundar manav roop mein hai.
Usey samajh aa gaya
ki woh Bhima se prem kar baithi hai.

Gusse se chillaya:

“Dushta aurat!
Tum Rakshason ki maryada tod rahi ho!
Main pehle tujhe maarunga,
phir in sabko kha jaunga!”

Aur woh apni behen par jhapta.

🗡️ Bhima ka dharmic krodh

Bhima ne turant garaj kar kaha:

“Ruk jaa!
Kisi stree ko maarna
veer ka kaam nahi hota!

Agar ladna hai
toh mujhse lad!”

Bhima ne saaf kaha:

“Yeh ladki doshi nahi.
Kaam-dev ke vash mein aakar
uska mann bhatka hai.

Aaj tumhara ant nishchit hai.”

💥 Mahabali yuddh

Hidimva garajta hua Bhima par toota.
Bhima ne uske dono haath pakad liye
— jaise sher kisi jaanwar ko pakadta hai.

Usse zameen par ghaseeta
taaki uski cheekh
bhaiyon ko na jaga de.

Dono rakshas aur manushya
do madha hathi jaise ladne lage.
Ped toot gaye.
Belain ukhad gayin.

Par shor itna badha
ki Pandav aur Maa Kunti jaag gaye
aur dekha —
Bhima aur Hidimva aamne-saamne yuddh kar rahe hain.

🌱 Is adhyay ki seekh

Stree par hinsa adharm hai

Veer pehle raksha karta hai, phir yuddh

Sachcha bal sirf sharir ka nahi, dharm ka hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.3
        with st.expander("Section 1.9.3"):
            text1 = """ 
            Section CLVI – Hidimva ka Ant
            Pandav aur Maa Kunti achanak neend se jaag gaye.
Unhone dekha ek bahut sundar stree khadi hai.
Uski beauty dekh kar sab hairaan reh gaye.

Maa Kunti ne pyaar se poocha:

“Devi si sundar kanya,
tum kaun ho?
Kya tum is jungle ki devi ho
ya koi apsara?”"""
            create_image_text_layout("attached_assets/chapter1/1.9.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌸 Hidimba ka sach

Hidimba ne shant swar mein kaha:

“Yeh jungle mere bhai Hidimva ka hai.
Woh ek bhayanak rakshas hai.

Mujhe usne bheja tha
tum sabko maarne ke liye.
Par jab maine Bhima ko dekha,
mera mann badal gaya.

Prem ne mujhe rok liya.
Bhima hi maine apna pati maana.”

Usne aage kaha:

“Ab dekhiye,
mera bhai aur Bhima
aapas mein bhayanak yuddh kar rahe hain.”

⚔️ Yuddh ka drishya

Tab Yudhishthira, Arjuna, Nakula aur Sahadeva
sab uth khade hue.

Unhone dekha —
Bhima aur Hidimva
do sher jaise lad rahe the.

Dhool itni udi
jaise jungle mein aag lag gayi ho.
Dono ke shareer
dhundh se dhake pahadon jaise lag rahe the.

🏹 Arjuna ki chinta

Arjuna muskurate hue bola:

“Bhima bhai, daro mat.
Agar thak gaye ho
toh main madad kar doon?”

Bhima garaj kar bola:

“Bas dekhte raho.
Yeh mere haathon se
zinda nahi bachega.”

Arjuna ne yaad dilaya:

“Subah hone wali hai.
Rakshas subah zyada shaktishaali ho jaate hain.
Ab der mat karo.”

🔥 Bhima ka prachand roop

Yeh sunte hi Bhima ka krodh jag utha.
Usne apne pita Vayu ki shakti ko yaad kiya.

Bhima ne Hidimva ko
aasmaan mein utha kar
kai baar ghumaya.

Aur garaj kar bola:

“Tu adharmi hai.
Tu manushya ka khoon peeta hai.
Aaj tera ant nishchit hai.”

💥 Rakshas ka vadh

Bhima ne poori shakti se
Hidimva ko zameen par patka.
Ek bhayanak cheekh ghoonji.

Phir Bhima ne
rakshas ke shareer ko
do tukdon mein tod diya.

Hidimva ka ant ho gaya.

😊 Khushi aur samman

Sab bhai khush ho gaye.
Unhone Bhima ko gale lagaya.
Arjuna ne kaha:

“Yahan se jaldi chalo.
Kahin Duryodhana ko pata na chal jaye.”

Sab ne “haan” kaha
aur Maa Kunti ke saath
aage badh gaye.

Hidimba bhi unke saath chali
— shant aur vinamra.

🌼 Is kahani ki seekh

Adharma ka ant nishchit hota hai

Prem hinsa se bada hota hai

Sachcha veer apno ki raksha karta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.4
        with st.expander("Section 1.9.4"):
            text1 = """ 
            Section CLVII – Bhima, Hidimba aur Ghatotkacha ka Janm
            Bhima ne dekha ki Hidimba unke peeche aa rahi hai.
Bhima thoda sakht swar mein bola:

“Rakshasi log badla lene ke liye
chaal aur dhokha use karte hain.
Isliye tum bhi apne bhai ke raaste chali jao.”"""
            create_image_text_layout("attached_assets/chapter1/1.9.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌿 Yudhishthira ka dharma

Yeh sun kar Yudhishthira aage aaye.
Unhone shant par majboot awaaz mein kaha:

“Bhima,
chahe gussa kitna bhi ho,
ek aurat ko marna dharma nahi.

Rakshas jo humein marna chahta tha,
uska ant ho chuka hai.
Yeh stree ab humara koi nuksaan nahi karegi.”

Bhima shaant ho gaya.

💗 Hidimba ka vinti bhara sach

Hidimba ne Maa Kunti aur Yudhishthira ko
haath jod kar pranam kiya aur boli:

“Maata ji,
auraton ke mann mein jo prem jagta hai,
uska dard bahut gehra hota hai.

Bhima ke liye jo prem mere dil mein hai,
use main aur nahi jhel sakti.
Maine apna kul, apne log,
sab chhod diya hai.

Agar mujhe thukra diya gaya,
toh main jee nahi paungi.

Kripya mujhe Bhima ki patni bana dijiye.
Main unhe surakshit rakhungi,
aur jab bhi aap yaad karengi,
main turant aa jaungi.”

🌸 Yudhishthira ka faisla

Yudhishthira ne dhyaan se suna aur bole:

“Tum jo keh rahi ho,
woh dharma ke viruddh nahi hai.

Bhima din bhar tumhare saath rahega.
Par surya ast hone se pehle,
use har din wapas aana hoga.”

Bhima ne bhi sir hila kar haan keh di.

🌈 Bhima aur Hidimba ka samay

Hidimba Bhima ko le kar
pahadon, jangalon aur sundar sthalon par gayi.

Kabhi phoolon se bhare van,
kabhi nadiyon ke kinaare,
kabhi shant jheelon ke paas.

Woh Bhima ko khush rakhna chahti thi.
Aur Bhima bhi apna vachan nibha raha tha.

👶 Ghatotkacha ka janm

Samay ke saath Hidimba ne
ek bahut shaktishaali putra ko janm diya.

Bachcha paida hote hi
yuvak jaisa balwaan lag raha tha.

Uski aankhen bhayanak,
haath majboot,
aur awaaz garajne wali thi.

Uska sir ghade (ghat) jaisa tha.
Isliye maa-pita ne uska naam rakha:

👉 Ghatotkacha

Woh bachpan se hi
sab rakshason se zyada shaktishaali tha.

🤝 Vachan aur vidaai

Ghatotkacha ne
apne pita Bhima ke charan chhuye.
Aur bola:

“Jab bhi aap ya Pandav mujhe bulayenge,
main zaroor aaunga.”

Hidimba ne bhi sab Pandavon ko pranam kiya
aur apne lok chali gayi.

🌟 Is kahani ki seekh

Dharma gusse se bada hota hai

Prem bal se bhi zyada shaktishaali hota hai

Sahi samay par liya gaya faisla bhavishya banata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.9.5
        with st.expander("Section 1.9.5"):
            text1 = """ 
            Section CLVIII – Pandavon ka Vanvaas aur Vyasa Rishi ka Aashirvaad
            Pandav ab
ek jungle se doosre jungle ja rahe the.
Kabhi hiran shikar karte,
kabhi chhote jaanwar,
taaki bhookh mita sakein.

Woh Matsya, Trigarta, Panchala aur Kikata deshon se guzre.
Raste mein sundar jheel, gehre van aur shaant jagahen dekhi."""
            create_image_text_layout("attached_assets/chapter1/1.9.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌿 Tapasvi jaisa jeevan

Sab Pandav
jangli kapdon,
ped ki chhaal aur jaanwaron ki khal pehne hue the.

Unke baal jataa bane hue the.
Maa Kunti bhi unke saath thi.
Dekhne mein woh sab rishi-muni jaise lagte the.

Kabhi Bhima
maa ko kandhon par utha leta.
Kabhi sab log
guise mein chupke se chalte.
Kabhi bahut tez,
kabhi bahut sambhal kar.

Raat ko woh
Veda, neeti aur dharma ka adhyan karte.
Unka mann majboot tha,
chahe jeevan kathin ho.

🌸 Vyasa Rishi se milan

Ek din jungle mein
Pandavon ko Maharshi Vyasa mile.

Pandav aur Maa Kunti
haath jod kar unke saamne khade ho gaye.

Vyasa Rishi ne pyaar se kaha:

“Main jaanta hoon
tumhare saath jo anyaay hua hai.

Yeh vanvaas
tumhari bhalaai ke liye hai.
Isse ghabrao mat.

Jo dukh mein hota hai,
us par bhagwan aur rishiyon ki
kripa zyada hoti hai.”

🔮 Bhavishya ki bhavishyavaani

Vyasa Rishi ne Maa Kunti se kaha:

“Tumhara beta Yudhishthira
ek din poori dharti par raj karega.

Bhima aur Arjuna ke bal se
sab shatru jeete jaayenge.

Yeh tumhare bete
Rajasuya aur Ashwamedha yagna bhi karenge.

Tumhara dukh
ek din mahima aur samman mein badlega.”

Maa Kunti ki aankhon mein aansu the,
par mann ko shanti mil gayi.

🏡 Ekachakra ka surakshit thikana

Vyasa Rishi
Pandavon ko Ekachakra naam ke shahar le gaye.

Wahan ek Brahman ke ghar unhe rehne ko mila.

Vyasa ne kaha:

“Yahin raho.
Desh aur samay ke hisaab se jiyo.
Main wapas aaunga.”

Pandavon ne haath jod kar kaha:
“Jaisa aap kahein.”

Aur Vyasa Rishi
shaant muskaan ke saath
wahaan se chale gaye.

🌟 Is kahani ki seekh

Kathin samay hamesha sthayi nahi hota

Dharma aur gyaan sabse bada sahara hota hai

Jo shant rehkar sahi raasta chunta hai, wahi aage raj karta hai"""
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.10
    with st.expander("Chapter 1.10 – Vaka-vadha Parva (Slaying of the Demon Vaka)"):

        # Section 1.10.1
        with st.expander("Section 1.10.1"):
            text1 = """ 
            Section CLIX – Ekachakra mein Dukh ki Awaaz
            Janamejaya ne poocha:
“Gurudev,
Pandav Ekachakra pahunch kar
kya kar rahe the?”

🏡 Ekachakra ka jeevan

Vaisampayana bole:

Pandav
Ekachakra mein
ek Brahman ke ghar rahe.

Woh bhiksha maang kar jeete the.
Din bhar
gaav aur jungle dekhte.
Log unse pyaar karne lage.
Unki vinamrata aur gyaan sabko achha lagta tha.

Shaam ko
jo kuch bhi bhiksha milti,
woh sab Maa Kunti ke paas rakh dete."""
            create_image_text_layout("attached_assets/chapter1/1.10.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Maa Kunti
sab kuch barabar baant deti.
Aadha sab bhaiyon ke liye,
aur aadha Bhima ke liye.

Is tarah
Pandav shanti se jee rahe the.

😢 Dukh ki awaaz

Ek din
baaki Pandav bhiksha par gaye.
Sirf Bhima aur Maa Kunti ghar par the.

Tab achanak
ghar ke andar se
rone ki tez awaaz aayi.

Maa Kunti ka mann
hil gaya.
Unka dil
daya se bhar gaya.

Unhone Bhima se kaha:

“Beta,
yeh Brahman humein
sharan de raha hai.
Humein bhi
uska bhala sochna chahiye.

Jo madad kare,
uska rin chukana
dharma hota hai.

Lagta hai
koi bada dukh
us par aa pada hai.”

Bhima bola:
“Maa,
aap poori baat jaan lo.
Agar madad mumkin hui,
main zaroor karunga.”

🕯️ Brahman ka dard

Maa Kunti
andar gayi.

Wahan unhone dekha:
Brahman,
uski patni,
beta aur beti
sab dukh mein baithe the.

Brahman keh raha tha:

“Yeh jeevan
khokhla hai.
Har jagah
dukh hi dukh hai.

Dhan paane mein dukh,
dhan bachane mein dukh,
aur kho jaaye to aur dukh.

Mujhe samajh nahi aa raha
kisey bachaoon.

Patni ko chhod doon?
Beta ko de doon?
Beti ko tyag doon?

Main kaise
apne bachchon ko
marne ke liye de doon?

Aur agar
main khud mar jaun,
toh yeh sab
kaise jeeyenge?

Koi raasta nahi dikh raha.
Shayad
sab ka saath hi marna
behtar hai…”

🌱 Is hissa ki seekh

Jo sharan deta hai, uska dukh apna hota hai

Sachcha dharma sirf apna nahi, doosron ka bhala sochta hai

Sabse gehra dukh wahi hota hai, jahan faisla insaan ko tod deta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.2
        with st.expander("Section 1.10.2"):
            text1 = """ 
            Section CLX – Maa ka Balidaan
            Vaisampayana bole:

Brahman ke dukh bhare shabd sunkar
uski patni aage aayi.
Uski aankhon mein aansu the,
par awaaz mein dheeraj aur bal tha."""
            create_image_text_layout("attached_assets/chapter1/1.10.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌸 Patni ka kathor faisla

Usne kaha:

“Swami,
aap aise mat roiye
jaise aam insaan rota hai.

Aap gyaani ho.
Aap jaante ho
ki mrityu sabko aani hai.
Jo nahi badal sakta,
uske liye shok nahi karna chahiye.

Patni, beta, beti –
yeh sab bhi
jeevan ke liye hi chune jaate hain.

Mujhe jaane dijiye.
Main khud jaungi.
Yehi stree ka
sabse bada dharma hai –
apne pati ke liye apna jeevan dena.

Isse aap bach jaoge.
Mujhe is sansaar mein
maan milega,
aur aage sukh.”

👩‍👧‍👦 Maa ka dard

Woh aage boli:

“Main aapko
beta aur beti de chuki hoon.
Mera kartavya poora ho chuka hai.

Aap in bachchon ko
paal sakte ho.
Par main,
aapke bina,
unhe kaise sambhaal paungi?

Agar aap nahi rahe,
toh
yeh duniya
ek akeli aurat ke liye
bahut kathor hoti hai.

Buri nazar wale log
meri beti par nazar daalenge.
Main use kaise bacha paungi?

Aur agar
main bachon ke saath reh bhi jaun,
toh bina aapke
hum teenon
zinda nahi reh paayenge.”

🔥 Antim satya

Usne dheere se kaha:

“Isliye,
aap mujhe chhod do.

Shastra kehte hain,
maa ban chuki stree ke liye
pati se pehle marna
sabse bada punya hai.

Rakshas bhi
nari-vadh se darte hain.
Ho sakta hai
woh mujhe na maare.

Agar koi bhi bach sakta hai,
toh aap hi bachoge.

Aap phir shaadi kar sakte ho.
Ye paap nahi.
Par stree ke liye
doosra pati
adharm hota hai.

Isliye,
mujhe jaane do.
Mere balidaan se
aap,
aapka vansh,
aur yeh bachche
bach jaayenge.”

😢 Nishabd dukh

Yeh kehkar
Brahman patni ke paas gaya.
Usse gale laga liya.

Dono chup the.
Par aankhon se
aansu beh rahe the.

Shabd khatam ho gaye the,
sirf tyaag aur prem baaki tha.

🌱 Is kahani ki seekh

Sachcha prem apna sukh nahi, doosron ka jeevan dekhta hai

Balidaan jab majboori se ho, tab sabse adhik dukh deta hai

Maa ka dil sabse pehle apne parivaar ko bachata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.3
        with st.expander("Section 1.10.3"):
            text1 = """ 
            Section CLXI – Beti aur Chhote Bhai ka Prem
            Vaisampayana bole:

Maa-baap ke dukh bhare shabd sunkar
Brahman ki beti ka dil bhar aaya.
Uski aankhon mein aansu the,
par soch bahut gehri thi."""
            create_image_text_layout("attached_assets/chapter1/1.10.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌼 Beti ka bada faisla

Usne kaha:

“Pitaji,
aap aise kyun ro rahe ho
jaise koi sahara hi na ho?

Main hoon na.
Mujhe suno.

Ek din toh
aap mujhe chhodoge hi.
Toh aaj hi chhod do.

Sabko bachane ke liye
sirf mujhe de do.

Bachche isliye hote hain
taaki maa-baap ko bachayein.
Isi liye bachcha
Putra kehlata hai.

Main aaj
apni jaan dekar
aap sabko bacha lungi.
Mujhe kisi aur ka intezaar nahi.”

👧💔 Beti ka dard

Woh aage boli:

“Mera bhai abhi bahut chhota hai.
Agar aap mar gaye,
toh woh bhi zinda nahi reh paayega.

Agar aap aur bhai dono chale gaye,
toh pitron ka pind bhi ruk jaayega.
Sab kuch toot jaayega.

Par agar aap bach gaye,
maa bach gayi,
bhai bach gaya,
toh vansh bhi bachega.

Pitaji,
beta apna hi roop hota hai.
Patni dost hoti hai.
Par beti…
aksar bojh samjhi jaati hai.

Aaj us bojh ko
hata dijiye.
Aur mujhe
dharma ke raaste par bhej dijiye.”

🌸 Chhoti si muskaan

Itna kehkar
beti chup ho gayi.

Maa-baap aur beti
teenon ro pade.

Tab achanak
chhota bhai,
jo abhi bachcha tha,
muskurate hue bola:

“Pitaji, mat royo.
Maa, aap bhi mat royo.
Didi, aap bhi nahi.”

Woh hansi-hansi aaya
aur ghaas ka tinka uthakar bola:

“Isse main
Rakshas ko maar dunga!”

🌈 Andhere mein ek roshni

Us bachche ke maasoom shabd sunkar
sabke chehron par
ek pal ke liye muskaan aa gayi.

Dukh wahi tha,
par dil ko
thoda sahara mil gaya.

Usi pal
Kunti aage badhi.
Usne mehsoos kiya
yeh sahi samay hai bolne ka.

Beti ke shabd
jaise amrit the—
jo mare hue dilon ko
phir se zinda kar gaye.

🌱 Is kahani ki seekh

Bachche kabhi bojh nahi hote, woh rakshak hote hain

Beti ka tyaag bhi putra ke samaan mahaan hota hai

Masoomiyat kabhi-kabhi sabse bade dukh ko bhi halka kar deti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.4
        with st.expander("Section 1.10.4"):
            text1 = """ 
            Section CLXII – Brahman ka Dukh aur Rakshas Vaka
            Kunti ne shaant aur daya bhare swar mein kaha:
“Main jaanna chahti hoon
aapke dukh ka kaaran.
Agar mumkin hua,
main ise zaroor door karungi.”"""
            create_image_text_layout("attached_assets/chapter1/1.10.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😔 Brahman ka sach

Brahman ne gehri saans li
aur bola:

“Devi,
aapke shabd bilkul aap jaise pavitra hain.
Par yeh dukh
kisi insaan ke bas ka nahi lagta.

Is shehar ke paas
Vaka naam ka ek Rakshas rehta hai.
Woh insaan ka maans khata hai
aur poore shehar par raj karta hai.

Uski taqat ke kaaran
humein kisi aur shatru ka darr nahi.
Par wahi Rakshas
hamari sabse badi museebat hai.”

🚚 Bhayanak niyam

Brahman aage bola:

“Vaka ka niyam hai—
har parivaar ko baari-baari
uske liye khana bhejna padta hai.

Us khane mein hota hai:

ek gaadi bhar chawal

do bhains

aur ek insaan,
jo yeh sab us tak le jaaye.

Agar koi mana kare,
toh woh Rakshas
poore parivaar ko
maar kar kha jaata hai.”

⏳ Aaj meri baari

Uski awaaz bharra gayi:

“Bahut saalon baad
aaj meri baari aayi hai.

Mere paas itna dhan nahi
ki kisi aur ko bhej sakoon.
Aur main
apne parivaar ke kisi bhi sadasya
ko nahi de sakta.

Na mujhe raasta dikhta hai,
na umeed.”

👑 Kamzor raja

Brahman ne dard se kaha:

“Is desh ka raja bhi kamzor hai.
Use raj karna nahi aata.
Woh humein
is Rakshas se bacha nahi paaya.

Shayad
hamari galti yeh hai
ki hum aise raja ke raj mein reh rahe hain.”

🌊 Antim nirnay

Aankhon mein aansu lekar
Brahman bola:

“Ab koi raasta nahi bacha.

Aaj
main apni patni,
apne bachchon ke saath
us Rakshas ke paas jaaunga.

Agar marna hi hai,
toh sab ek saath mar jaayein.
Yeh dukh
ab aur saha nahi jaata.”

🌱 Is kahani ki seekh

Jab shasan kamzor hota hai, toh nirdosh log peedit hote hain

Bhay se jeena bhi ek tarah ki mrityu hoti hai

Par jahan anyaay hota hai, wahan dharma zaroor khada hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.5
        with st.expander("Section 1.10.5"):
            text1 = """ 
            Section CLXIII – Kunti ka Sahas aur Bhima ka Vachan
            Kunti ne shaant aur vishwas bhari awaaz mein kaha:
“Hey Brahman,
bilkul bhi shok mat karo.
Mujhe ek raasta dikh raha hai
jisse tum is Rakshas se bach sakte ho.”

Woh aage boli:
“Tumhara ek hi beta hai,
bahut chhota.
Ek beti hai,
bilkul nirbal.
Main yeh bilkul nahi chahti
ki tum, tumhari patni,
ya tumhare bachche
Rakshas ke paas jaayein.

Mere paas paanch bete hain.
Unmein se ek mera beta
tumhari taraf se
Rakshas ke liye bhojan le jaayega.”"""
            create_image_text_layout("attached_assets/chapter1/1.10.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😟 Brahman ka inkaar

Yeh sunkar Brahman ghabra gaya.
Usne turant kaha:

“Devi,
main apni jaan bachane ke liye
kabhi bhi
kisi Brahman ya atithi ko
balidaan nahi hone dunga.

Chahe mujhe khud marna pade,
par main
tumhare bete ko nahi bhej sakta.
Brahman ki hatya
sabse bada paap hai.
Iska koi prayashchit nahi hota.”

Woh bhari mann se bola:
“Apni jaan dena
kam paap hai
par kisi nirdosh ko dena
sabse bada adharm.”

🌸 Kunti ka dradh vishwas

Kunti ne dheere se muskura kar kaha:
“Tumhari baat sahi hai,
Brahman ka rakshan
sabse bada dharm hai.

Par suno,
mera beta koi saadharan nahi hai.
Woh bahut shaktishaali hai.
Mantron aur bal mein nipun hai.

Rakshas
use maar nahi sakta.
Woh bhojan dega,
aur khud surakshit laut aayega.”

Phir Kunti ne vinamrata se kaha:
“Par ek baat yaad rakhna.
Yeh baat
kisi aur ko mat batana.
Varna log
mere beton ko
pareshaan karenge.”

🌼 Aasha ki roshni

Yeh sunkar
Brahman aur uski patni
khushi se bhar gaye.
Unke chehre par
jaise andhere ke baad
roshni aa gayi.

Kunti phir
Vayu ke putra Bhima ke paas gayi.
Usse sab bataya
aur kaam karne ko kaha.

Bhima ne bina hichkichaye kaha:
“So be it.
Main jaaunga.”

🌱 Is kahani ki seekh

Sachcha dharm bal aur daya ka sangam hota hai

Jab koi anyaay ke khilaaf khada hota hai, tab bhagwan uske saath hota hai

Maa ka vishwas aur putra ka sahas, asambhav ko bhi sambhav bana deta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.6
        with st.expander("Section 1.10.6"):
            text1 = """ 
            Section CLXIV – Maa ka Vishwas aur Putra ka Dharm
            Bhima ne jab kaha,
“Main yeh kaam karunga,”
tab Pandav us din
bheek se jo mila tha
woh le kar ghar laut aaye.

Yudhishthira ne
sirf Bhima ke chehre ko dekh kar hi
samajh liya
ki kuch bahut bada aur khatarnaak
hone wala hai."""
            create_image_text_layout("attached_assets/chapter1/1.10.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Woh maa Kunti ke paas baith kar
chupchaap poochta hai:
“Maa,
yeh kaunsa kaam hai
jo Bhima karne jaa raha hai?
Kya yeh aapke kehne par hai
ya uski apni ichchha se?”

🌺 Kunti ka seedha jawab

Kunti ne shant swar mein kaha:
“Bhima,
mere kehne par,
ek mahaan kaam karega.
Yeh kaam
us Brahman ke bhale ke liye hai
aur poore shehar ki mukti ke liye.”

😠 Yudhishthira ka chinta bhara virodh

Yudhishthira ka mann kaanp utha.
Usne kaha:

“Yeh aapne kya kar diya, Maa?
Yeh kaam
lagbhag aatma-balidaan jaisa hai.

Gyani log kabhi bhi
apne bachche ko
is tarah tyagne ki salah nahi dete.

Jis Bhima ke bal par
hum raat ko nishchint sote hain,
jiske sahare
hume apna rajya wapas milega,
jis Bhima ke dar se
Duryodhana aur Shakuni
raat bhar so nahi paate—

usi Bhima ko
aap tyagna chahti ho?

Kya aapka vivek
dukh ke kaaran
dhundhla ho gaya hai, Maa?”

🌸 Maa Kunti ka dradh vishwas

Kunti ne pyaar se kaha:
“Yudhishthira,
Bhima ke liye
chinta mat karo.

Maine yeh faisla
kisi kamzori mein nahi liya.
Is Brahman ne
hume bina pehchaan ke
apne ghar mein sharan di.

Uska upkaar chukana
mera dharm hai.”

Woh aage boli:
“Lakshagriha se bachne ke samay
aur Hidimba ke vadh ke baad
mujhe Bhima ke bal par
poora bharosa ho gaya hai.

Uske haath ka bal
das hazaar haathiyon ke barabar hai.
Usi bal se
woh tum sabko
Varanavata se uthakar le aaya.

Dharti par
Bhima ke jaisa balwaan
koi nahi.”

🔥 Bhima ka bal – janm se hi adbhut

Kunti ne yaad dilaya:
“Jab Bhima chhota tha,
meri god se gir kar
pahaad par ja gira.
Pahaad toot gaya,
par Bhima ko kuch nahi hua.

Tab se mujhe pata hai
ki Bhima saadharan nahi hai.”

🌼 Dharm ka raasta

Kunti boli:
“Is kaam se
do cheezein hongi:
1️⃣ Brahman ka upkaar chukega
2️⃣ Hume mahaan punya milega

Kshatriya ka dharm hai
sabki raksha karna—
Brahman, Vaishya,
yahaan tak ki Shudra ki bhi.

Yeh baat
mujhe pehle hi
Maharshi Vyasa ne samjhai thi.”

Woh shant ho kar boli:
“Isliye,
maine soch-samajh kar
yeh nirnay liya hai.”

🌱 Is kahani ki seekh

Sachcha dharm apno ke dar se upar hota hai

Maa ka vishwas aur dharm ka gyaan, bade se bade sankat ka samna kar sakta hai

Bal sirf shakti nahi, zimmedaari bhi hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.7
        with st.expander("Section 1.10.7"):
            text1 = """ 
            Section CLXV – Bhima aur Vaka Rakshas ka Samna
            Maa Kunti ki baat sun kar
Yudhishthira shant ho gaya.
Usne kaha:

“Maa,
aapne jo faisla liya hai,
woh sach mein uttam hai.
Bhima zaroor jeet kar lautega
aur us rakshas ko maar kar aayega,
kyunki aap hamesha
Brahmanon par daya karti ho."""
            create_image_text_layout("attached_assets/chapter1/1.10.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            Bas ek baat ka dhyaan rakhna—
us Brahman se keh dena
ki yeh baat shehar mein kisi ko pata na chale.
Woh vachan de
ki sab kuch gupt rakhe.”

Maa Kunti ne haan mein sir hila diya.

🌙 Subah ka samay – Bhima ka prasthan

Raat beet gayi.
Subah hui.

Bhima ne
rakshas ke liye taiyaar kiya gaya
bhojan uthaya
aur akela hi
us jungle ki taraf chal pada
jahan Vaka Rakshas rehta tha.

Jungle ke paas pahunch kar
Bhima ne kuch ajeeb kiya.

🍚 Rakshas ka bhojan… Bhima ne hi kha liya

Bhima ne
us rakshas ka bhojan
khud hi khana shuru kar diya
aur zor se awaaz lagayi:

“O Vaka!
Nikal bahar!”

Bhima shanti se kha raha tha.

😡 Vaka Rakshas ka gussa

Bhima ki awaaz sun kar
Vaka Rakshas gusse se aag-baboola ho gaya
aur jungle se bahar nikla.

Woh bahut bhayankar tha—
laal aankhen,
laal baal,
laal daadhi,
aur itna bada sharir
ki dharti kaanp uthi.

Uska muh kaanon tak khula tha.
Har kadam se zameen dhans rahi thi.

Usne Bhima ko dekha
jo uska bhojan kha raha tha.

Rakshas garja:
“Kaun hai yeh moorkh
jo Yama ke ghar jaana chahta hai
aur mere samne mera hi bhojan kha raha hai?”

😏 Bhima ka shant apmaan

Bhima sirf muskuraaya.
Usne rakshas ki taraf
dekha bhi nahi
aur khaana jaari rakha.

Yeh dekh kar
Vaka zor se chillaaya
aur dono baah utha kar
Bhima par toot pada.

Bhima tab bhi shaant raha.
Sirf ek halki si nazar daali
aur khaata raha.

💥 Rakshas ka prahaar, Bhima achal

Gusse mein paagal ho kar
Vaka ne peeche se
Bhima ki peeth par
zor se vaar kiya.

Par Bhima…
hilaa bhi nahi.

Rakshas aur bhadak gaya.
Usne ek bada ped ukhaada
aur Bhima par phenka.

🌳 Pedon ki yuddh-bhoomi

Bhima ne araam se
poora khaana khatam kiya,
haath-muh dhoya
aur khade ho kar bola:

“Ab… lad sakte hain.”

Rakshas ne ped phenka.
Bhima ne ek haath se pakad liya.

Phir dono
ek-doosre par ped phenkte rahe.
Jungle dheere-dheere
khaali hota gaya.

Aakhir Rakshas chillaaya:
“Main Vaka hoon!”

Aur Bhima par toot pada.

🤼 Bal ka maha-yuddh

Vaka ne Bhima ko jakad liya.
Bhima ne bhi Vaka ko pakad liya.

Dono ek-doosre ko
ghaseetne lage.
Dharti kaanp uthi.
Ped toot kar girne lage.

Dheere-dheere
Vaka thakne laga.

🔥 Antim pal

Bhima ne mauka dekha.
Usne Vaka ko
ghutnon se zameen par daba diya.

Ek ghutna peeth par,
ek haath gardan par,
aur doosre se kamar ka kapda pakad kar
Bhima ne rakshas ko
do hisson mein mod diya.

Vaka bhayanak cheekha.
Uske muh se khoon nikalne laga.

🌟 Is hissa ki seekh

Shant rehna bhi shakti hoti hai

Sachcha veer pehle kartavya nibhata hai, phir yuddh karta hai

Ahankaar aur bhookh hamesha vinaash laati hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.10.8
        with st.expander("Section 1.10.8"):
            text1 = """ 
            Section CLXVI – Vaka Rakshas ka Ant aur Ekachakra ki Mukti (Hinglish Summary)

Vaisampayana kehte hain—
Bhima ke ghutne par tod diya gaya Vaka Rakshas, pahad jaisa vishal, bhayankar cheekhein maarta hua mara. Uski aawaazon se darr kar uske rishtedaar aur saathi bahar nikal aaye.

🛑 Bhima ka Daya–Dand

Bhima ne un bhatke hue Rakshason ko shant kiya aur kaha:

“Aaj ke baad manav-hatya mat karna.
Agar phir ki, to Vaka jaisa ant hoga.”

Sab Rakshason ne vachan diya.
Us din ke baad se, us kshetra ke Rakshas manushyon ke prati shaant ho gaye."""
            create_image_text_layout("attached_assets/chapter1/1.10.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🚪 Vaka ka Deh aur Rahasya

Bhima ne Vaka ke nirjeev sharir ko shehar ke ek darwaze par rakh diya
aur chupchaap nikal gaya.
Vaka ke parivaar wale darr ke maare idhar-udhar bhaag gaye.

Subah, jab log bahar nikle,
to lahooluhan Vaka ko pada dekh kar sab stambhit reh gaye.
Shehar mein khabar phail gayi—Ekachakra azaad ho chuka tha!

Hazaaron nagrik, apni patniyon, bachchon, buzurgon ke saath,
us drishya ko dekhne aaye.
Sab devtaon ko dhanyavaad dene lage.

🤫 Pandavon ka Rahasya Surakshit

Logon ne jaanne ki koshish ki—
“Kal kaun Rakshas ko bhojan dene gaya tha?”

Jab pata chala ki us Brahman ka turn tha,
to sab uske ghar pahunch gaye.

Brahman ne, Pandavon ko bachane ke liye, kaha:

“Ek mahaan, mantra-vid Brahman ne meri peeda dekh kar kaha—
‘Aaj main khud bhojan le jaunga, chinta mat karo.’
Usi ne yeh punya karya kiya.”

Sab log vismit ho gaye—
Brahman, Kshatriya, Vaishya, Shudra—sab khush the.

🎉 Utsav aur Smriti

Shehar mein utsav manaya gaya.
Us din se, Ekachakra mein
Brahman-pooja pramukh karm ban gayi—
us anjaan upkaar ke smaran mein,
jisne shehar ko Vaka ke bhay se mukt kar diya.

🌟 Is Adhyay ki Seekh

Shakti ke saath daya ho to sahi parivartan hota hai

Raksha bina ghamand ke ho, to lok-kalyan hota hai

Gupat upkaar sabse shreshth hota hai"""
            create_image_text_layout(text_content=text2, layout="full")

    # Chapter 1.11
    with st.expander("Chapter 1.11 – Caitraratha Parva (The Chaitraratha Episode)"):

        # Section 1.11.1
        with st.expander("Section 1.11.1"):
            text1 = """ 
            Section CLXVII – Ekachakra mein nayi kahani (Hinglish Moral Story)

Rakshasa Vaka ke marne ke baad,
shehar ke log
shanti se apne ghar laut gaye.

Aur
Pandavas
phir se
Ekachakra mein rehne lage,
bilkul pehle jaise."""
            create_image_text_layout("attached_assets/chapter1/1.11.1.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌿 Janamejaya ka sawaal

Janamejaya ne pucha:

“Guruji,
Vaka ke marne ke baad
Pandavas ne kya kiya?”

📖 Vaisampayana bole

Vaisampayana bole:

Pandavas
us Brahman ke ghar hi rahe,
jahan pehle se reh rahe the.

Woh roz
Vedas padhte.
Shaant jeevan jeete.
Maa Kunti
unke saath thi.

🧙‍♂️ Ek naye mehmaan ka aana

Kuch hi dinon mein
ek aur Brahman
wahan aaya.

Woh tapasya wala tha.
Seedha aur shaant.

Ghar ke malik ne
uska poora samman kiya.
Paani diya.
Aasan diya.
Rehne ki jagah di.

Pandavas khush hue.

🔥 Rochak kahaniyaan

Pandavas ne kaha:

“Maharaj,
apni yatra ki kahani sunaiye.”

Brahman muskuraya.

Usne bataya:

alag-alag desh

pavitra nadiyaan

rajaa aur nagar

mandir aur teerth

Sab sun kar
Pandavas dhyaan se sunte rahe.

🌸 Draupadi ki adbhut janm-katha

Phir Brahman ne
ek bahut khaas baat batayi.

Usne kaha:

“Panchal ke raja
Drupada
ne ek maha-yagya kiya.

Us yagya se
aag ke beech se
ek kanya janmi.

Uska naam tha
Draupadi.”

Pandavas hairaan ho gaye.

Brahman ne aage bataya:

Dhrishtadyumna ka janm

Shikhandi ka janm

aur Drona aur Drupada ki purani dosti ka tootna

🤔 Pandavas ki jigyasa

Pandavas ne ek saath pucha:

“Yeh sab kaise hua?
Aag se janm kaise?
Dosti kyun tooti?”

Brahman muskuraya.

Usne kaha:

“Main tumhe
Draupadi ki poori kahani
agle adhyay mein sunaunga.”

🌟 Is Ansh ki Seekh

Shanti ke baad gyaan aata hai

Mehmaan ka samman dharma hota hai

Har badi kahani se pehle jigyasa hoti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.2
        with st.expander("Section 1.11.2"):
            text1 = """ 
            Section CLXVIII – Drona ka Janm, Shiksha aur Drupada se Vair (Hinglish Story Explanation)

Yeh ansh Mahabharata ki ek bahut hi mahatvapurn background story batata hai—
jisse aage chal kar Draupadi, Dhrishtadyumna, aur Kurukshetra yuddh ka beej padta hai."""
            create_image_text_layout("attached_assets/chapter1/1.11.2.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Rishi Bharadvaja aur Drona ka janm

Ganga ke kinare ek maha-rishi rehte the—
Bharadvaja

Ek din Ganga snaan ke samay
apsara Ghritachi hawa ke kaaran vastrahin ho gayi.
Rishi ne brahmacharya ka vrat liya tha,
lekin prakriti ke niyam ke kaaran
unke sharir se veerya nikal gaya.

👉 Rishi ne us veerya ko ek matke (drana) mein sambhaal liya.
Usi se ek balak ka janm hua—
jiska naam pada Drona
(isiliye Dronacharya = pot-born).

📚 Drona aur Drupada ki bachpan ki dosti

Usi samay Panchal ke raja Prishata ke yahan
ek putra hua—
Drupada

Drona aur Drupada
ek hi ashram mein
saath padhte–khelte bade hue

Bachpan mein dono gehre mitra the

Lekin…
samay badla.

Prishata ke baad
Drupada raja ban gaya
aur Drona ek garib Brahman hi raha.

⚔️ Parashurama se shastra-prapti

Drona ne suna ki
Parashurama
apni saari sampatti daan kar rahe hain.

Drona unke paas gaya.

Parashurama bole:

“Mere paas sirf
mera sharir aur mere shastra bache hain.”

Drona ne maanga:

“Aapke sab shastra aur unka gyaan.”

👉 Parashurama ne
sabhi divya astra–shastra
Drona ko de diye,
yahan tak ki Brahmastra bhi.

Isse Drona
sabse shreshth dhanurdharon mein ginne jaane lage.

💔 Drupada ka apmaan

Ab Drona
apni purani dosti yaad karke
Drupada ke darbar gaye aur bole:

“Mujhe apna mitra mano.”

Drupada ne ghamand mein kaha:

“Raja aur garib Brahman ki dosti nahi hoti.”

⚡ Yeh shabd
Drona ke hriday mein
gehra ghaav ban gaye.

🏹 Guru Drona aur pratishodh

Drona ne Hastinapur jaakar
Bhishma ke sahyog se
Pandavas–Kauravas ko shiksha deni shuru ki.

Shiksha ke baad
unhone guru-dakshina maangi:

“Drupada ko harao
aur uska rajya mujhe do.”

Pandavas ne
Drupada ko yuddh mein hara diya
aur bandi bana kar
Drona ke samne laaya.

🏰 Rajya ka vibhaajan

Drona ne kaha:

“Ab hum barabar ke raja hain,
isliye dosti sambhav hai.”

Ganga ke dakshin ka rajya → Drupada

Ganga ke uttar ka rajya → Drona

Drupada ne upar se haan keh di…
lekin andar hi andar
uska apmaan jalta raha.

👉 Yahin se Drupada ke yagya,
Dhrishtadyumna aur Draupadi ke janm,
aur Drona ke vinash ki kahani shuru hoti hai.

🌟 Is Ansh ki Gehari Seekh

Ahankar dosti tod deta hai

Apmaan badla ban jaata hai

Shabd talwar se zyada ghaav dete hain

Guru–shishya sambandh yuddh ki disha badal dete hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.3
        with st.expander("Section 1.11.3"):
            text1 = """ 
            Section CLXIX – Drupada ka Yagya aur Agni se Janm (Hinglish Moral Story)

Bahut samay tak
Raja Drupada ka mann shaant nahi tha.
Uske dil mein sirf ek dard tha.
Aur ek hi iccha.

👉 “Mujhe aisa beta chahiye
jo Drona ko hara sake.”"""
            create_image_text_layout("attached_assets/chapter1/1.11.3.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            😔 Drupada ka dukh

Drupada ghoomta raha.
Ek ashram se doosre ashram.
Brahmanon se milta raha.

Woh aksar kehta tha:
“Jo bachche mere paas hain,
woh kaabil nahi.”

Uska dukh
badle ki aag ban chuka tha.

🔥 Yaja aur Upayaja Rishi

Ek din
Drupada ko do maha-rishi mile—
Yaja aur Upayaja.

Upayaja pavitra the

Yaja thode worldly the

Drupada ne pehle Upayaja se kaha:
👉 “Mere liye yagya karo
aur mujhe aisa beta do
jo Drona ko maar sake.”

Upayaja ne shaant swar mein mana kar diya.

🤝 Yaja ka maan jana

Phir Drupada
Yaja ke paas gaya.
Usne kaha:

👉 “Main hazaaron gaaye dunga.
Bas ek beta chahiye—
jo Drona ka ant kare.”

Yaja ne socha.
Aur phir bola:
“Theek hai.”

Upayaja ne bhi
bina kisi lalach ke
is yagya mein madad ki.

🪔 Mahaan Yagya

Sab taiyaari ho gayi.
Agni jalaayi gayi.
Mantra bole gaye.

Yaja ne rani ko bulaya.
Rani boli:
👉 “Main abhi taiyaar nahi hoon.”

Yaja muskuraye aur bole:
👉 “Yagya rukta nahi.”

⚔️ Agni se Putra ka janm

Agni se
ek tejshwi yoddha nikla.

haath mein talwar

sharir par kavach

aankhon mein veerta

Aakash se awaaz aayi:
👉 “Yeh balak
Drona ke vinash ke liye janma hai.”

Uska naam rakha gaya—
Dhrishtadyumna.

🌸 Agni se Putri ka janm

Usi yagya se
ek sundar kanya bhi nikli.

gehri kaali aankhen

neeli ghungraali zulfein

kamal jaisi sundarta

Aakashvani hui:
👉 “Yeh kanya
bahut se Kshatriyon ke vinash ka kaaran banegi.
Aur Kauravon ke liye kaal hogi.”

Uska naam rakha gaya—
Krishna,
jo baad mein Draupadi ke naam se vikhyat hui.

📚 Vidhambna ki seekh

Kismat ka khel dekho—

👉 Drona,
jise maarne ke liye
Dhrishtadyumna janma tha,
usi Drona ne usey shastra-shiksha di.

Destiny apna raasta
khud banati hai.

🌟 Is Kahani ki Seekh

Badla aag hai,
jo poora vansh jala sakta hai

Bhagya ko koi rok nahi sakta

Jo janma agni se hota hai,
woh itihaas badal deta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.4
        with st.expander("Section 1.11.4"):
            text1 = """ 
            Section CLXX – Ek Naya Safar Shuru Hone Wala Hai (Hinglish Moral Story)

Brahmana ki baat sunte hi
Kunti ke saare bete
jaise andar se hila diye gaye.

Unke chehre shaant the,
par mann ashant ho chuka tha."""
            create_image_text_layout("attached_assets/chapter1/1.11.4.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌸 Maa Kunti ki soch

Tab sachchi aur samajhdaar Maa Kunti
ne sabko dekha.
Unke bete chup the,
soch mein doobe hue.

Maa ne Yudhishthira se kaha:

👉 “Beta,
humne is Brahmana ke ghar
bahut din bita liye hain.

Humne yahaan
izzat se bhiksha payi,
aur shaanti se jeevan jiya.”

🌿 Badlav ki zarurat

Phir Maa boli:

👉 “Jo jungle aur baag
humne yahaan dekhe,
ab unhe dobara dekhkar
mann khush nahi hota.

Har cheez ek jagah
zyada din rehne se
purani ho jaati hai.”

🥖 Practical sach

Maa ne aage kaha:

👉 “Ab yahaan bhiksha bhi
pehle jaisi aasaan nahi milti.

Maine suna hai
Panchala desh mein
Brahmanon ka bahut samman hota hai.

Wahaan ke raja
daan aur dharm mein aage hain.”

🛤️ Safar ka prastaav

Maa ne pyar se kaha:

👉 “Hum Panchala chalein?
Woh desh humne nahi dekha.
Naya sthal,
naya anubhav.”

👉 “Zyada samay
ek hi jagah rehna
achha nahi hota.”

👑 Yudhishthira ka uttar

Yeh sun kar
Yudhishthira ne namrata se kaha:

👉 “Maa,
aapka aadesh
hamare liye dharm hai.

Aap jo kehti hain,
woh hamare bhale ke liye hota hai.”

Phir usne shaant swar mein kaha:

👉 “Bas ek baat hai, Maa…
mujhe nahi pata
mere chhote bhai
is safar ke liye
taiyaar hain ya nahi.”

🌟 Is Kahani ki Seekh

Jeevan mein badlav zaroori hota hai

Maa ka anubhav
bachchon ka rakshak hota hai

Kabhi-kabhi
aage badhne ke liye
peeche chhodna padta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.5
        with st.expander("Section 1.11.5"):
            text1 = """ 
            Section CLXXI – Vyasa ka Bhavishyavani aur Panchala ki Yatra (Hinglish Moral Story)
🚶‍♂️ Pandavon ka Faisla

Maa Kunti ne jab
Bhimasena, Arjuna, Nakula aur Sahadeva se
Panchala jaane ki baat kahi,
toh sabne ek swar mein kaha:

👉 “So be it.”

Phir Maa Kunti aur Pandavon ne
us Brahmana ko vinamr pranam kiya
jinke ghar ve chhupkar rahe the,
aur sab milkar
Maharaj Drupada ke nagar Panchala
ki aur chal pade."""
            create_image_text_layout("attached_assets/chapter1/1.11.5.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌿 Rishi Vyasa ka Aagaman

Isi dauran,
Vyasa,
Satyavati ke putra,
Pandavon se milne aaye.

Pandav unhe dekhkar
khade ho gaye,
aage badhkar pranam kiya
aur haath jodkar chupchaap khade rahe.

Vyasa prasann hue aur bole:

👉 “Kya tum sab
dharm ke marg par chal rahe ho?
Kya tum Brahmanon ka samman karte ho?”

Unhone dharm, maryada aur jeevan
par updesh diya
aur phir ek rahasyamayi kahani sunayi.

🔮 Pichhle Janm ki Kahani

Vyasa ne bataya:

Ek tapasvi Rishi ki
ek sundar, gunwaan beti thi.
Pichhle janm ke karmon ke kaaran
use pati nahi mila.

Usne kathor tapasya ki
aur Mahadev (Shiva) ko prasann kiya.

Mahadev bole:
👉 “Var maango.”

Us kanya ne paanch baar kaha:
👉 “Mujhe pati do,
jo sab gunon se yukt ho.”

Shiv ji bole:

👉 “Tumne paanch baar pati maanga hai,
isliye agle janm mein
tumhare paanch pati honge.”

🌸 Bhavishyavani ka Sach

Vyasa ne kaha:

👉 “Wahi kanya
is janm mein
Draupadi,
yaani Krishna Panchali,
Drupada
ke ghar janmi hai.”

👉 “Wahi tum sab
Pandavon ki patni banegi.”

👉 “Panchala jao,
wahaan raho,
tum sab usse vivaah karke
bahut sukhi rahoge.”

🙏 Vidai

Itna kehkar
Rishi Vyasa ne
Pandavon ko aashirvaad diya
aur apne ashram ki aur chale gaye.

🌟 Is Adhyay ki Seekh

Kismat aur karm apna kaam karte hain

Jo cheez samajhna mushkil lagti hai,
uske peeche bhi gehra dharm aur niyati hoti hai

Jeevan ke bade mod
pehle se likhe hote hain,
bas samay aane par khulte hain"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.6
        with st.expander("Section 1.11.6"):
            text1 = """ 
            Section CLXXII – Pandav, Gandharva aur Ganga ka Gyaan (Hinglish Moral Story)
🌄 Panchala ki Yatra

Vyasa ji ke jaane ke baad,
Pandav bhai, apni Maa Kunti ke saath,
us Brahmana ko pranam karke
khushi-khushi Panchala ki taraf chal pade।

Din–raat chal kar
ve Bhagwan Shiv ke pavitra sthaan pahúnche,
phir Ganga ji ke kinaare aaye.

Sabse aage Arjuna chal rahe the,
haath mein mashaal (torch) thi,
taaki raasta dikhe aur
jangli jaanwaron se raksha ho."""
            create_image_text_layout("attached_assets/chapter1/1.11.6.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌊 Ganga ke Tat par Takraav

Usi samay,
Gandharvon ke raja Angaraparna
apni patniyon ke saath
Ganga mein khel rahe the.

Pandavon ke kadmon ki aahat sun kar
Angaraparna gusse mein aa gaya.

Usne dhanush uthaya aur bola:

👉 “Yeh twilight ka samay hai.
Yeh samay Gandharva, Yaksha aur Rakshas ka hota hai.
Insaan yahan nahi aane chahiye.
Door raho!
Yeh meri van-bhoomi hai!”

🔥 Arjuna ka Nirbhay Uttar

Arjuna shaant par dridh awaaz mein bole:

👉 “Ganga kisi ki private jagah nahi hai.
Din ho ya raat,
har koi yahan aa sakta hai.
Yeh pavitra nadi sabki hai.”

👉 “Jo kamzor hote hain,
woh dhamki dete hain.
Hum darr ke liye nahi bane.”

⚔️ Yuddh aur Vijay

Gusse mein aakar
Angaraparna ne baan chalaye.

Arjuna ne
apni mashaal aur dhal se
sab baan rok liye.

Phir Arjuna ne
agni-astra chhoda.

🔥 Gandharva ka rath jal gaya.
Angaraparna behosh ho gaya.

Arjuna ne use pakad kar
apne bhaiyon ke paas laaya.

🙏 Karuna aur Daya

Gandharva ki patni Kumbhinasi
Yudhishthira ke paas bhaagi
aur boli:

👉 “Maharaj,
mere pati ko bacha lijiye.”

Yudhishthira ne Arjuna se kaha:

👉 “Jo har chuka ho,
aur sharan mein aaya ho,
use maarna dharm nahi.”

Arjuna ne turant kaha:

👉 “Tum ja sakte ho.
Tumhe jeevan daan diya jaata hai.”

🎁 Gyaan aur Upahaar

Angaraparna ne sharm aur shraddha se kaha:

👉 “Aaj mera ghamand toot gaya.
Isliye main tumhe
Cakshushi Vidya deta hoon.”

👉 “Is vidya se
tum jo chaho,
jaise chaho,
dekh sakte ho.”

Usne Pandavon ko
divya ghode bhi dene ka vachan diya.

Arjuna ne kaha:

👉 “Mujhe badle mein
apna agni-astra le lo.
Hamaari mitrata bani rahe.”

🌙 Raat ka Rahasya

Angaraparna ne sach bataya:

👉 “Raat ke samay
hum Gandharvon ki shakti badh jaati hai.”

👉 “Lekin tum Brahmacharya mein ho,
isliye tum mujhse jeet gaye.”

👉 “Jo raja
Brahmana ke bina hota hai,
uska raj tikta nahi.”

🌟 Is Kahani ki Seekh

Daya aur karuna
jeet ke baad sabse badi shakti hoti hai

Gyaan ka daan
hamesha yuddh se upar hota hai

Dharma, sanyam aur Brahmacharya
insaan ko mahaan banate hain

Ghamand girta hai,
vinamrata jeet jaati hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.7
        with st.expander("Section 1.11.7"):
            text1 = """ 
            Section CLXXIII – Tapati aur Raja Samvarana ki Kahani (Hinglish Moral Story)
❓ Arjuna ka Sawaal

Arjuna ne Gandharva se poocha:

👉 “Aap mujhe baar-baar Tapatya kehte ho.
Hum to Kunti ke putra hain,
phir yeh Tapati kaun hai?
Aur hum uske vanshaj kaise hue?”

Gandharva muskuraya aur bola:

👉 “Arjuna,
main tumhe ek sundar aur pavitra kahani sunata hoon.
Dhyaan se sunna.”"""
            create_image_text_layout("attached_assets/chapter1/1.11.7.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            ☀️ Surya Dev ki Putri – Tapati

Swarg mein Surya Dev (Vivasvat) ki ek beti thi,
jiska naam tha Tapati.

✨ Woh apni behen Savitri se bhi chhoti thi,
par sundarta aur gunon mein
teenon lokon mein mashhoor thi.

Aankhen badi aur kaali

Swabhav shant aur pavitra

Tapasya mein leen

Har roop mein sundar

Surya Dev sochte the:

👉 “Is duniya mein
kaun hai jo meri beti Tapati ke layak ho?”

👑 Raja Samvarana

Us samay dharti par
ek mahaan raja the — Samvarana.

Dharm ke maarg par chalne wale

Surya Dev ke bhakt

Sundar, veer aur gyaani

Dushmanon ke liye Surya jaise tezz

Mitron ke liye Chandra jaise shant

Surya Dev ne nirnay liya:

👉 “Meri beti Tapati ke liye
Samvarana se achha pati
koi nahi ho sakta.”

🌲 Van Mein Achanak Mulakaat

Ek din Raja Samvarana
shikaar ke liye
pahadon ke jungle mein gaye.

Safar lamba ho gaya.
Unka ghoda thak kar gir gaya.

Raja akela jungle mein
chal rahe the…

Tab unhone dekha —

🌟 Ek apsara si sundar kanya
akeli khadi thi.

Raja ruk gaye.
Unki aankhen bhar aayi.

👉 “Yeh to Lakshmi jaisi lagti hai…”
👉 “Ya Surya ki roshni ka roop?”

Uski chamak aag jaisi thi,
par chehra chaand sa shant.

Pahad bhi
uske saamne sone jaise lag rahe the.

💘 Prem aur Vishmay

Raja ka mann
bilkul bandhan mein bandh gaya.

Unhone kaha:

👉 “Tum kaun ho?
Kiski ho?
Yahan akeli kyun ho?”

👉 “Tum kisi dev, yaksha,
ya insaan jaisi nahi lagti.”

👉 “Tumhe dekh kar
Kaamdev mujhe jalane lage hain.”

Par…

⚡ Tapati ne kuch nahi kaha.
Aur bijli ki tarah
uski aankhon ke saamne se
gaayab ho gayi.

😢 Virah aur Peeda

Raja Samvarana
poore jungle mein
use dhoondhte rahe.

Par Tapati nahi mili.

Raja thak kar ruk gaye,
mann dukhi ho gaya.

👉 “Shayad maine
sapna dekha tha…”

Aur woh
dukh mein doob gaye.

🌼 Is Kahani ki Seekh

Sundarta ke saath sanyam zaroori hai

Bhagya apna samay leta hai

Saccha prem shant hota hai, zabardasti nahi

Dev yojna hamesha dharm ke saath hoti hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.8
        with st.expander("Section 1.11.8"):
            text1 = """ 
            Section CLXXIV – Tapati aur Raja Samvarana (Hinglish Moral Story)

Gandharva ne kahani aage badhaayi:

🌲 Tapati ka wapas aana

Jab woh sundar kanya achanak gaayab hui,
toh Raja Samvarana
prem ke dukh mein apna hosh kho baithe.

💔 Kaamdev ke baan unke mann ko jala rahe the.
Aur wahi raja
zameen par gir pade.

Tab achanak—

✨ Tapati phir se saamne aayi.
Chehre par halki si muskaan thi.

Woh boli:

👉 “Utho, O veer raja.
Aap jaise mahaan purush ko
apna hosh khona shobha nahi deta.”

Raja ne aankhen kholi.
Saamne wahi sundar kanya khadi thi."""
            create_image_text_layout("attached_assets/chapter1/1.11.8.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            💘 Raja ka prem-bhara nivedan

Raja ka hriday pighal gaya.
Awaaz kaanp rahi thi.

👉 “O sundar nayan wali kanya,
main prem ki aag mein jal raha hoon.”

👉 “Tumhari ek jhalak ne
mera sab kuch chheen liya.”

👉 “Tumhari aankhen kamal jaisi hain,
tumhari awaaz madhur hai.”

👉 “Tum bin main jee nahi sakta.”

👉 “Kripya mujh par daya karo.”

👉 “Mera mann bhatak raha hai.”
👉 “Tumhe dekh kar
kisi aur ko dekhna hi nahi chahta.”

👉 “Main tumhara daas hoon.”
👉 “Mujhe apna lo.”

👉 “Is prem ki aag ko
apne pyaar se shant kar do.”

👉 “Gandharva vivaah sabse uttam mana gaya hai.
Mujhse vivaah kar lo.”

🌸 Tapati ka dharm aur maryada

Tapati shant thi.
Uski awaaz komal par dridh thi.

👉 “O raja,
main apni swatantra nahi hoon.”

👉 “Main apne pita ke adheen hoon.”

👉 “Agar aapka prem sachcha hai,
toh mere pita se meri maang karo.”

Phir Tapati ne sach kaha:

👉 “Aapne pehli nazar mein
mera bhi mann jeet liya hai.”

👉 “Par na main apne sharir ki maalik hoon,
na apne faislon ki.”

👉 “Nari kabhi swatantra nahi hoti.”

👉 “Kaun si stri hogi
jo aap jaise dharmic aur dayalu raja ko
apna pati na chahe?”

👉 “Tapasya, pooja aur niyam ke saath
mere pita se meri maang karo.”

👉 “Agar pita ne anumati di,
toh main sada aapki patni banungi.”

Phir usne apna parichay diya:

👉 “Mera naam Tapati hai.”
👉 “Main Savitri ki chhoti behen hoon.”
👉 “Main Surya Dev ki putri hoon.”

🌼 Is Kahani ki Seekh

Saccha prem dhairya maangta hai

Maryada prem se upar hoti hai

Nari ki ijjat aur dharm ka samman zaroori hai

Jo sahi tareeke se maanga jaaye, wahi tikta hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.9
        with st.expander("Section 1.11.9"):
            text1 = """ 
            Section CLXXV – Tapati ka Vivaah aur Vasishtha ki Mahima (Hinglish Moral Story)

Gandharva ne kahani aage badhaayi 🌿

🌤️ Tapati ka aakash mein lautna

Yeh kehkar Tapati
aasmaan ki taraf udd gayi.

Raja Samvarana
phir se dharti par gir pade.
Prem ne unka hosh chheen liya tha.

Unke mantri aur sainik
poore jungle mein dhoondhte hue aaye.
Aakhir unhe raja
ek akela pahad par pada mila.

👑 Raja ko aise dekhkar
mukhyamantri ka hriday jal utha.

Woh daud kar aaye.
Pyaar aur samman se
raja ko uthaya."""
            create_image_text_layout("attached_assets/chapter1/1.11.9.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            💧 Raja ka hosh mein aana

Mantri ne thande,
kamal-pankhudiyon se sugandhit jal se
raja ka sir bhigoya.

Dheere-dheere raja ko hosh aaya.

Raja ne sabko jaane ko kaha.
Sirf mukhyamantri ko paas rakha.

Phir raja ne
shuddhi ki.
Aur pahad par baith kar
haath jod kar Surya Dev ki pooja ki.

Unhone apne guru
Rishi Vasishtha ka smaran kiya.

📿 Raja bina ruke
baarah din aur raat
tap mein baithe rahe.

🌞 Vasishtha aur Surya Dev ka milan

Barahve din
Rishi Vasishtha wahan aaye.

Unhone apni tap-shakti se
jaan liya
ki raja prem-vedna mein doobe hain.

Rishi ne raja ko aashvasan diya.

Phir wahi Rishi
aasmaan mein gaye
aur Surya Dev ke paas pahunche.

🙏 Vasishtha ne kaha:
“Main Vasishtha hoon.”

Surya Dev ne muskurakar kaha:
“Jo maango, milega.”

Rishi bole:

👉 “Aapki putri Tapati,
raja Samvarana ke liye maangta hoon.”

👉 “Woh dharmic hai.
Mahaan hai.
Aapki putri ke yogya hai.”

Surya Dev prasann hue.

🌼 “Samvarana shreshth raja hai.
Tapati shreshth nari hai.
Aur aap shreshth Rishi ho.”

Isliye Surya Dev ne
Tapati ko Vasishtha ko saunp diya.

⚡ Vivaah ka mangal pal

Vasishtha Tapati ko lekar
wapas aaye.

Tapati bijli ki tarah
aasmaan se utri.
Das dishaayein chamak uthi.

Raja Samvarana ka
hriday anand se bhar gaya.

💍 Baaraha din ka vrat poora hua.
Rishi Vasishtha ne
Tapati ka vivaah
Samvarana se karwaya.

Is tarah raja ne
pooja aur dhairya se
patni paayi.

🌿 Vasishtha ki Mahima

Arjuna ne poocha:
“Yeh Vasishtha kaun hain?”

Gandharva bola:

✨ Vasishtha
Brahma ji ke putra hain.
Arundhati ke pati hain.

🔥 Kaam aur krodh bhi
unke charan dabate the.

⚖️ Apne putron ke dukh mein bhi
unhone maryada nahi todi.

👑 Jin rajaon ke guru Vasishtha the,
unhone dharti par raj kiya.

🕉️ Isliye,
jo raja vijay chahta hai,
use pehle
ek dharmic Brahmana ko guru banana chahiye.

🌸 Is Kahani ki Seekh

Saccha prem tapasya se milta hai

Guru aur dharm ka sahara sabse bada hota hai

Maryada aur dhairya se hi sukh milta hai

Raja ho ya vyakti, sahi marg guru hi dikhata hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.10
        with st.expander("Section 1.11.10"):
            text1 = """ 
            Section CLXXVI – Visvamitra–Vasishtha Vair aur ‘Tapatya’ ka Arth

Is ansh mein Arjuna (Arjuna) Gandharva se poochte hain ki Visvamitra aur Vasishtha ke beech shatruta ka mool kya tha, aur unhe “Tapatya” kyun kaha jaata hai. Gandharva is prashn ka uttar Tapati–Samvarana–Kuru parampara ke madhyam se deta hai."""
            create_image_text_layout("attached_assets/chapter1/1.11.10.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔱 Tapati ki Katha (Saar)

Tapati, Surya (Vivasvat) ki putri, ka vivah Raja Samvarana se Rishi Vasishtha ke anugrah se hota hai.

Vivah ke baad Samvarana apni patni ke saath parvaton par tapas aur vihār mein lipt rehte hain; rajya ka kaaryabhaar Vasishtha sambhalte hain.

Is avdhi mein 12 varshon ka akaal padta hai—barish band, ann ki kami, praja ka palayan.

Vasishtha Samvarana ko rajya wapas laate hain; raja ke aate hi Indra varsha karte hain, desh phir se jeevant hota hai.

Samvarana–Tapati fir se yajna karte hain; rajya samriddh hota hai.

👑 Kuru Vansh aur ‘Tapatya’

Samvarana aur Tapati se Kuru ka janm hota hai—jo Kuru vansh ke adhar-stambh bane.

Isliye Pandav, jo Kuru vansh ke hain, Tapati ke vanshaj hone ke kaaran “Tapatya” kehlate hain.

Gandharva spasht karta hai: “Tum Kuru ke vansh mein janme ho, isliye Tapatya ho.”

🧠 Mool Sandesh

Rishi Vasishtha ka dharm aur tapas rajya ko bachata hai—raja aur rishi ka sahyog praja-hit ke liye anivarya hai।

Vansh-parampara (Tapati → Kuru → Pandav) se naam aur pehchaan milti hai—“Tapatya” sirf upnaam nahi, itihaas hai।

Aage chal kar isi parampara mein Visvamitra–Vasishtha ka prasiddh sangharsh aata hai—par is ansh mein uska prarambhik sandarbh diya gaya hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.11
        with st.expander("Section 1.11.11"):
            text1 = """ 
            Section CLXXVII – Visvamitra aur Nandini ki Kahani (Hinglish Moral Style)

Arjuna ne Gandharva ki baat suni.
Uske mann mein bhakti aur shraddha aa gayi.
Woh jungle mein rehkar shikar karta aur shaant jeevan jeeta.

🌿 Visvamitra Vasishtha ke Aashram Mein

Ek din shikar karte-karte Visvamitra thak gaye.
Pyaas lagi. Shareer kamzor ho gaya.
Woh Vasishtha ke aashram pahunch gaye.

Vasishtha ne raja ka poora samman kiya.
Paani diya.
Arghya diya.
Phal, makhan aur shuddh bhojan diya.

Yeh sab Nandini naam ki gaay se mila.
Yeh koi sadharan gaay nahi thi.
Jo maanga jaata, wahi de deti."""
            create_image_text_layout("attached_assets/chapter1/1.11.11.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🐄 Nandini – Iccha Poorn Karne Wali Gaay

Nandini ne:

Swadisht bhojan diya

Doodh aur mishri jaisa amrit diya

Sundar vastra aur ratna bhi diye

Raja Visvamitra bahut prabhavit hue.
Unhone Nandini ko dhyaan se dekha.
Unhe laga, “Aisi gaay mere paas honi chahiye.”

👑 Visvamitra Ka Ahankaar

Visvamitra bole:
“Hey Rishi, mujhe Nandini de do.
Main badle mein 10,000 gaayen ya apna rajya de dunga.”

Vasishtha shant rahe.
Unhone kaha:
“Yeh gaay mere yajna, devta aur atithiyon ke liye hai.
Main ise kisi keemat par nahi de sakta.”

Yeh sun kar Visvamitra gussa ho gaye.
Unhone kaha:
“Main Kshatriya hoon.
Bal se le loonga.”

⚔️ Bal vs Kshama

Vasishtha bole:
“Kshatriya ka bal shastra mein hota hai.
Brahmana ka bal kshama aur tap mein hota hai.
Tum jo chaho karo.”

Visvamitra ne zabardasti Nandini ko pakad liya.
Use maarne lage.
Ghasitne lage.

😢 Nandini Ka Dukh

Nandini ro padi.
Woh Vasishtha ke paas aayi.
Boli:
“Guruji, kya main anath ho gayi hoon?
Aap mujhe bachayenge nahi?”

Vasishtha bole:
“Main tumhe nahi chhod raha.
Agar tum mein shakti hai, toh raho.”

🔥 Tapas Ka Asli Bal

Bas itna sunna tha.
Nandini bhayanak roop mein aa gayi.

Uski aankhen aag jaisi ho gayi

Uski poonch se angaar barasne lage

Uske shareer se alag-alag senaayein nikli

Palhavas, Yavanas, Shakas, Kiratas, Hunas…
Har disha se yoddha nikle.

Unhone Visvamitra ki sena ko sirf bhaga diya, maara nahi.
Sena dara-sahma kar door bhaag gayi.

🌸 Gyaan Ka Jaagran

Visvamitra yeh sab dekh kar hil gaye.
Unhone kaha:
“Dhikkar hai Kshatriya bal par.
Asli shakti tapasya mein hai.”

Us din unhone:

Rajya chhod diya

Sukh-suvidha chhod di

Tapasya ka raasta chuna

Lambe samay ke baad,
Visvamitra Brahmarshi bane.
Aur swarg mein Indra ke saath Soma ka paan kiya.

🌟 Moral (Seekh)

Bal se nahi, dharm se jeet hoti hai

Kshama aur tapasya sabse badi shakti hai

Ahankaar jhukta hai, par sachcha tap kabhi nahi"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.12
        with st.expander("Section 1.11.12"):
            text1 = """ 
            Section CLXXVIII – Raja Kalmashapada aur Shraap ki Kahani (Hinglish Moral Story)

Gandharva ne kaha:

Arjun, purane time mein ek raja tha.
Uska naam tha Kalmashapada.
Woh Ikshvaku vansh ka raja tha.
Bahut shaktishaali aur veer tha."""
            create_image_text_layout("attached_assets/chapter1/1.11.12.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌲 Shikaar aur Thakaan

Ek din raja jungle gaya shikaar ke liye.
Usne kai hiran, suar aur gainde maar diye.
Lekin kaafi der shikaar ke baad
woh thak gaya aur pyaasa ho gaya.

Woh aaram karne ke liye jungle mein ruk gaya.

🚶‍♂️ Raja aur Rishi Sakti ka Saamna

Usi samay ek mahan rishi aa rahe the.
Unka naam tha Sakti,
jo Vasishtha ke putra the.

Raja aur Rishi ek hi raaste par aa gaye.
Raja ne gusse mein kaha:
👉 “Raasta chhod do.”

Rishi shaant swar mein bole:
👉 “Yeh mera raasta hai.
Dharma ke anusaar raja ko
Brahmana ko raasta dena chahiye.”

Dono ne ek dusre se kaha:
“Tum hat jao.”

Na raja jhuka.
Na rishi jhuke.

⚔️ Ahankaar Ka Paap

Raja gusse mein aa gaya.
Usne Rishi ko chabuk se maara.

Yeh dekh kar Rishi Sakti ka krodh jaag gaya.
Unhone raja ko shraap de diya:

👉 “Tum Rakshas ban jaoge.
Insaano ka maans khaoge.
Dharti par bhatakte rahoge.”

Shraap lag chuka tha.

🕶️ Visvamitra Ki Chaalaaki

Usi jagah Visvamitra bhi maujood the.
Woh chhupkar sab dekh rahe the.

Unhone ek Rakshas (Kinkara) ko
raja ke sharir mein ghusa diya.

Ab raja Rakshas ke vash mein aa gaya.

🍖 Paap Aur Dusra Shraap

Kuch samay baad ek bhooka Brahmana
raja ke paas aaya aur bhojan maanga.

Raja ne kaha:
👉 “Ruko, main bhejta hoon.”

Raat ko raja ne apne rasoiye ko aadesh diya:
👉 “Brahmana ko bhojan aur maans do.”

Rasoiye ko maans nahi mila.
Rakshas ke prabhav mein raja bola:
👉 “Insaan ka maans de do.”

Brahmana ne apni divya drishti se
sab pehchaan liya.
Gusse mein usne bhi shraap de diya:

👉 “Ab tum hamesha
insaani maans ke bhookhe rahoge.”

Shraap aur zyada gehra ho gaya.

😨 Rakshas Ban Chuka Raja

Ab raja poori tarah se Rakshas ban chuka tha.
Usne Rishi Sakti ko dekha aur bola:

👉 “Main sabse pehle tumhe hi khaunga.”

Aur raja ne Sakti ko maar kar kha liya.

Visvamitra ne Rakshas ko aur bhadkaya.
Raja ne Vasishtha ke baaki putron ko bhi maar diya.

🕊️ Vasishtha Ki Mahaan Kshama

Jab Vasishtha ko pata chala
ki unke sab putra maare ja chuke hain,
toh unka mann toot gaya.

Lekin unhone krodh nahi kiya.
Unhone socha:
👉 “Main dusron ko nasht nahi karunga.”

Dukh mein unhone apna jeevan tyagne ki koshish ki:

Meru parvat se kud gaye – kuch nahi hua

Aag mein gaye – aag thandi lagne lagi

Samudra mein kood gaye – lehron ne bahar pheink diya

Mrityu ne unhe chhua bhi nahi.

Ant mein,
Vasishtha apne aashram laut aaye.
Dukh mein, par dhairya ke saath.

🌟 Moral (Seekh)

Ahankaar se paap hota hai

Shraap aur krodh zindagi barbad kar dete hain

Asli shakti kshama aur sanyam mein hoti hai

Vasishtha jaise log dukh mein bhi dharm nahi chhodte"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.13
        with st.expander("Section 1.11.13"):
            text1 = """ 
            Section CLXXIX – Vasishtha ka Dukh, Dhairya aur Asha (Hinglish Moral Story)

Gandharva ne kaha:

Vasishtha ka aashram bilkul soona ho chuka tha.
Apne sab putron ko kho kar,
Muni ka mann gehre dukh mein doob gaya."""
            create_image_text_layout("attached_assets/chapter1/1.11.13.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌧️ Dukh Mein Aatma-tyaag Ki Koshish

Dukh se bhare hue,
Vasishtha fir se bhatakne lage.

Ek din unhone dekha ek bhari hui nadi.
Barish ka paani tez tha.
Pedh-paudhe beh ja rahe the.

Muni ne socha:
👉 “Agar main isme kood jaun,
toh shayad meri peeda khatam ho jaaye.”

Unhone rassiyon se khud ko baandha
aur nadi mein kood gaye.

Lekin nadi ne:

rassiyan kaat di

aur Muni ko kinare par la diya

Tab se us nadi ka naam pada
👉 Vipasa – jo bandhan tod de.

🌊 Dusri Nadi, Wahi Aanjaam

Dukh kam nahi hua.
Vasishtha aur aage chale.

Unhone dekhi ek aur bhayankar nadi –
Haimavati,
jismein magarmach aur bhayanak jeev the.

Muni ne fir se kood kar
apni jaan deni chahi.

Lekin nadi ne unhe aag ka gola samajh kar
sau dhaaron mein baant diya.

Tab se us nadi ka naam hua
👉 Satadru – sau dhaaron wali nadi.

Muni bole:
👉 “Main apne haath se bhi nahi mar sakta.”

👩‍🦱 Ek Awaaz, Ek Nayi Asha

Wapas aashram jaate hue,
unke peeche koi aa raha tha.

Unhone suna:
👉 Vedon ka madhur paath.

Vasishtha ne pucha:
👉 “Kaun hai jo mere peeche aa raha hai?”

Jawab mila:
👉 “Main Adrisyanti hoon.
Saktri ki patni.”

Vasishtha bole:
👉 “Yeh awaaz toh Saktri jaisi hai.”

Adrisyanti ne kaha:
👉 “Aapke putra ka putra
mere garbh mein hai.
Barah saal se.”

🌱 Umeed Ki Jeet

Yeh sunte hi Vasishtha ka mann bhar aaya.
Unhone kaha:
👉 “Mere vansh ka vanshaj zinda hai!”

Isi pal,
unhone apni jaan dene ka vichaar chhod diya.

Woh Adrisyanti ke saath
wapas aashram laut aaye.

👹 Rakshas Raja Ka Samna

Raste mein unhe mila
Raja Kalmashapada,
jo Rakshas ke vash mein tha.

Rakshas Raja ne
Vasishtha ko dekh kar
unhe khaane ke liye aage badha.

Adrisyanti dar gayi aur boli:
👉 “Yeh Rakshas humein maar dega!”

✨ Mantra Aur Mukti

Vasishtha shaant rahe.
Unhone sirf ek shabd kaha:
👉 “Hum”

Mantron ke paani se
Raja ko chhidka.

Rakshas ka prabhav
turant toot gaya.

Barah saal baad,
Raja phir se insaan ban gaya.

Raja ne vinamrta se kaha:
👉 “Main aapka shishya hoon.
Mujhe batayein main kya karun?”

Vasishtha bole:
👉 “Rajya jao.
Nyay se shasan karo.
Aur kabhi Brahman ka apmaan mat karna.”

👶 Ikshvaku Vansh Ki Raksha

Raja ne ek aur prarthana ki:
👉 “Mujhe ek putra dijiye
jo mere vansh ko aage badhaye.”

Vasishtha ne kaha:
👉 “Tathaastu.”

Ayodhya laut kar,
sab log khushi se jhoom uthe.

Kuch samay baad,
queen ke garbh se
Asmaka ka janm hua.
Wahi aage chal kar
ek mahaan raja bana.

🌟 Moral (Seekh)

Asha kabhi nahi chhodni chahiye

Dukh mein bhi dhairya rakho

Dharm aur kshama sabse badi shakti hai

Zindagi hamesha koi na koi raasta dikhati hai"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.14
        with st.expander("Section 1.11.14"):
            text1 = """ 
            Section CLXXX – Parāśara ka Krodh aur Vasishtha ki Mahān Sikṣā (Hinglish Explanation)

Gandharva ne kaha:

Adrisyanti ne samay aane par ek putra ko janm diya,
jo Saktri ke vansh ka rakshak bana.
Woh balak gun, tej aur tapasya mein
bilkul Saktri jaisa tha.

👶 Janm aur Naam

Vasishtha ne svayam apne potey ke sanskār kiye

Kyunki Vasishtha kabhi aatma-tyaag ka vichaar kar chuke the
aur is balak ke janm se unka jeevan phir se jeevit ho utha,

Isliye balak ka naam pada Parāśara
👉 “jo mare hue ko phir se jeevit kare”

Balak Parāśara bachpan se hi Vasishtha ko
apna pita samajhta tha."""
            create_image_text_layout("attached_assets/chapter1/1.11.14.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            💔 Sach ka Ghaav

Ek din, Parāśara ne sabke saamne Vasishtha ko
“pitaji” keh kar pukara.

Yeh sunkar, maa Adrisyanti ki aankhon mein aansu aa gaye.
Unhone kaha:

“Beta, yeh tumhare pita nahi, tumhare dada hain.
Tumhare pita Saktri ko ek Rakshas ne maar diya tha.”

⚡ Is sach ne Parāśara ke hriday ko jala diya

Pehle dukh

Phir krodh

Aur phir vināsh ka sankalp

Parāśara ne socha:
👉 “Main poori srishti ka naash kar dunga!”

🧘‍♂️ Vasishtha ka Gyaan – Krodh par Vijay

Vasishtha ne apne potey ke mann ka vichaar jaan liya.
Unhone turant use roka aur ek purāni kathā sunai
— taaki uska krodh shaant ho.

📖 Kathā: Kshatriya–Bhrigu Vināsh

Vasishtha ne kaha:

Ek raja tha Kritavirya,
jo Bhrigu Rishiyon ka shishya tha.

Usne yagy aur daan se Brahmano ko prasann kiya.

Par uske baad:

Uske vanshaj gareeb ho gaye

Dhan ke liye Bhrigu Brahmano ke paas bhiksha maangne aaye

Kuch Bhriguon ne:

Dhan chhupa liya

Kuch ne daan de diya

Lekin:

Kuch Kshatriyon ne chhupe hue khazane dekh liye

Unhe laga Brahman dhokha kar rahe hain

⚔️ Phir kya hua?

Kshatriyon ne Bhrigu Brahmano ka nar-sanhār shuru kar diya

Yahan tak ki garbh mein shishu bhi nahi chhode

🌄 Ek Stree, Ek Garbh, Ek Chamatkaar

Bhrigu striyan bhaag kar Himalaya pahunchi

Ek stree ne apne jaangh (thigh) mein
ek tejashvi garbh ko chhupa liya

Ek darpok stree ne yeh baat Kshatriyon ko bata di.

Kshatriya aaye garbh ko nasht karne…

🔥 Par chamatkaar hua!

Garbh jaangh phaad kar bahar nikla

Uski tej se Kshatriya andhe ho gaye
jaise dopahar ka surya aankhon par pad gaya ho

🙏 Kshama ki Shakti

Andhe Kshatriya ghabra gaye.
Unhone us stree se prarthana ki:

“Humein drishti de do,
hum kabhi paap nahi karenge.”

Yahin par Vasishtha ne Parāśara ko roka
aur samjhaya (aage ke section mein):

👉 Kshama vināsh se badi hoti hai
👉 Krodh srishti ko jalata hai, kshama use bachati hai

🌟 Is Section ki Seekh

Janm se hi mahān hona kaafi nahi,
sanyam aur vivek bhi chahiye

Krodh se vināsh hota hai

Brahman ka bal shastra nahi, kshama hai

Sachcha mahaan wahi hai
jo badla lene ki shakti hote hue bhi
kshama chune"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.15
        with st.expander("Section 1.11.15"):
            text1 = """ 
            Section CLXXXI – Aurva Rishi ka Krodh aur Pitron ki Antim Shikṣā (Hinglish Explanation)

Vasishtha ne apne potey Parāśara ko aage samjhaya:

🌿 Bhrigu Stree aur Andhe Kshatriya

Jab andhe Kshatriya us Brahmana stree ke paas aaye,
toh usne shant swar mein kaha:

“Bachcho, maine tumhari drishti nahi chheeni,
aur na hi main tumse krodhit hoon.
Tumhari aankhen mere putra ke krodh se jali hain.”

Woh balak Bhrigu vansh ka tha

Usne apne kul ke sanhār ka smaran karke krodh dharan kiya tha

Isi divya tej se Kshatriyon ki aankhen jal gayi

Stree ne kaha:

“Jab tum Bhrigu vansh ke garbh tak nasht kar rahe the,
tab yeh balak mere jaangh (thigh) mein sau varsh tak raksha mein raha.
Isi avadhi mein poore Veda apni shaakhon ke saath iske hriday mein aa gaye.”

👉 Isliye us balak ka krodh saadharan nahi,
balki vaidik aur divya tha."""
            create_image_text_layout("attached_assets/chapter1/1.11.15.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🙏 Prarthana aur Kshama

Stree ne Kshatriyon se kaha:

“Is balak se prarthana karo.
Agar yeh prasann hua, toh tumhari drishti laut aayegi.”

Kshatriyon ne balak se kaha:
👉 “Prasann ho jaiye!”

Aur:

Balak ne kshama ki

Kshatriyon ki aankhen laut aayi

Is balak ka naam pada Aurva
👉 “jo jaangh se janma ho”

🔥 Aurva ka Pralay Sankalp

Lekin yahin kahani samapt nahi hui.

Aurva Rishi ne socha:

“Main poori srishti ka vināsh kar dunga”

Apne pitraon ko prasann karne ke liye
unhone bhayankar tapasya shuru kar di

⚡ Unki tapasya se:

Devta

Asura

Manushya
sabhi peedit hone lage

Teenon lok jalne lage.

👴 Pitron ka Avtaran

Tab Bhrigu pitra svayam swarg se aaye
aur Aurva se bole:

“Putra, tumhara tej humne dekh liya.
Lekin apna krodh roko.”

Unhone kaha:

🧠 Gehri Rahasya Bhari Baat

Bhrigu Rishi kamzor nahi the

Unhone apna vināsh jaanbujhkar sweekar kiya

“Hum lambe jeevan se thak gaye the,
isliye humne Kshatriyon ke haathon mrityu chuni.”

Dhan chhupaya gaya tha jaanbujhkar

Taaki Kshatriya krodhit ho jaayen

Aur hamara ant ho sake

⚠️ Aatmahatya ka dosh
Pitron ne kaha:

“Jo swayam aatmahatya karta hai,
usey swarg nahi milta.”

Isliye:

Unhone apni mrityu ka saadhan
Kshatriyon ko banaya

👉 Yeh sab sochi-samjhi yojna thi

🛑 Antim Updesh

Pitron ne Aurva se kaha:

“Isliye, putra,
poori srishti ka vināsh hamen sweekar nahi.
Tumhara krodh tumhari tapasya ko kalankit kar raha hai.”

Kshatriyon ka vināsh mat karo

Saaton lokon ka naash mat karo

Is krodh ko hi nasht karo

🌸 Is Section ki Mool Shikṣā

Vasishtha ne Parāśara ko yeh kahani sunakar samjhaya:

Krodh tapasya ko bhi jalata hai

Kshama hi sachchi shakti hai

Mahān hone ka arth hai:

Badla lene ki shakti hote hue bhi,
badla na lena

Aur yahin Parāśara ka krodh dheere-dheere shaant hua 🌿"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.16
        with st.expander("Section 1.11.16"):
            text1 = """ 
            Section CLXXXII – Aurva Rishi ka Krodh, Pitron ka Upāy, aur Vadavamukha ka Janm (Clear Explanation)

Is section mein Aurva Rishi aur Pitron ke beech ka sabse gehra darshanik samvaad aata hai—jahaan krodh, nyāy, tapasya aur jagat-rachna sab ek saath jud jaate hain."""
            create_image_text_layout("attached_assets/chapter1/1.11.16.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔥 Aurva Rishi ka Tarka (Justification of Anger)

Aurva Pitron se kehte hain:

Mera krodh vyarth nahi ja sakta

“Jo apne krodh aur sankalp ko vyarth jaane deta hai,
woh dharma–artha–kāma tino ko hi siddh nahi kar sakta.”

Nyāy ke liye krodh avashyak hai

Raja jab krodh dikhata hai, to:

Dushṭ log niyantrit hote hain

Sajjan log surakshit rehte hain

Mera krodh anuchit nahi, anivārya hai
Aurva kehte hain:

Garbh mein hote hue bhi unhone

Bhrigu striyon ke vilāp

Apne kul ke vināsh
ko suna

Jab koi rakshak nahi tha, tab krodh hi raksha bana

Dand na ho to paap badhta hai

“Jahan dand nahi hota, wahan aparādh badhta hai.”

Jo dand de sakta hai aur nahi deta,
woh bhi doshi hota hai

Isliye Aurva kehte hain:

“Main is paap ka dand dene mein saksham hoon.
Agar main chup raha, to aisa atyachaar phir hoga.”

⚖️ Aurva ka Sankat

Aurva Pitron se antim baat kehte hain:

Agar main:

Krodh ko daba doon → woh mujhe hi jala dega

Agar main:

Jagat ka vināsh kar doon → lok naṣṭ ho jaayenge

👉 Isliye woh Pitron se mārgdarshan maangte hain:

“Aisa upaay bataiye jo mujhe bhi bachaye
aur srishti ko bhi.”

🌊 Pitron ka Mahān Samādhān (The Great Solution)

Pitri kehte hain:

Jal hi srishti ka mool tattva hai

Ras, sharir, jeevan—sab jal par aadharit hain

Isliye:

“Apne krodh ki agni ko jal mein pravisht kara do”

🔑 Gehra Arth

Tumhara sankalp bhi poora ho jaayega

Jagat ka vināsh bhi nahi hoga

👉 Agni jal ko khayegi,
na ki praniyon ko

🐴 Vadavamukha ka Janm (Horse-Headed Fire)

Aurva ne apne krodh ki agni ko
Varuna ke lok (maha-samudra) mein daal diya

Wah agni:

Ghode ke sir jaisi prakat hui

Jise Vedon mein kaha gaya:

Vadavamukha (Horse-mouth Fire)

Yeh agni:

Samudra ke jal ko peeti rehti hai

Isliye samudra kabhi overflow nahi karta

Aur pralay bhi santulit rehta hai

👉 Aaj bhi Ved kehte hain:

Samudra ke neeche ek agni hai
jo jal ko nirantar grahan karti rehti hai

🧠 Is Kathā ka Darshanik Saar
1️⃣ Krodh galat nahi, anuyamit krodh galat hai
2️⃣ Nyāy ke liye shakti ka upyog avashyak hai
3️⃣ Mahān vyakti wahi hai jo:

Apni shakti ko santulan mein rakhe

Na swayam jale

Na jagat ko jalaye

Aur is prakar Aurva Rishi:

Apna sankalp bhi nibhaate hain

Aur srishti ki raksha bhi karte hain

✨ Vasishtha ka Sandesh Parasara ko

Isliye Vasishtha ant mein kehte hain:

“Hey Parasara,
tum bhi krodh se jagat ka vināsh mat chaho.
Buddhi se usse sahi disha do.”"""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.17
        with st.expander("Section 1.11.17"):
            text1 = """ 
            Section CLXXXIII – Parāśara Rishi ka Krodh aur Shaanti ka Vijay (Hinglish Moral Story Rewrite)

Vasishtha ke shabd sun kar Parāśara Rishi ne apna woh krodh rok liya
jo poore jagat ka vināsh kar sakta tha.
Lekin unka dil abhi bhi dukh se bhara tha."""
            create_image_text_layout("attached_assets/chapter1/1.11.17.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🔥 Rakshasa Yagya ka Aarambh

Parāśara Rishi ko apne pita Saktri ki yaad aa rahi thi.
Unke hriday mein nyāy ki aag jal rahi thi.

Isliye unhone ek vishesh yagya shuru kiya —
jise log Rakshasa Yagya ke naam se jaante hain.

Is yagya mein
Rakshas, chahe chhote ho ya bade,
us agni mein bhent ho rahe the.

Parāśara teen bhadakti agniyon ke beech baithe the,
aur khud chauthe agni jaise tej se chamak rahe the.

Unka tej aisa tha
jaise badalon se nikla hua Suraj.

Sab Rishi dekh kar chakit the.

🌞 Rishiyon ka Aagman

Us samay kuch mahan Rishi wahan aaye:

Atri

Pulastya

Pulaha

Kratu

Unka mann Rakshason ko bachane ke liye vyakul tha.

🕊️ Pulastya ka Updesh

Pulastya ne pyaar aur gyaan se Parāśara se kaha:

“O Parāśara,
kya tumhein sach mein is vināsh se sukh mil raha hai?”

Unhone aage kaha:

Yeh Rakshas tumhare pita ke doshi nahi hain

Bahut se toh nirdosh hain

Ek Brahmana ka dharma shaanti hota hai, vināsh nahi

Pulastya bole:

“Shaanti sabse bada dharma hai.”

Phir unhone ek gehri baat kahi:

Saktri ki mrityu
unke apne shabd (shraap) ka phal thi

Koi Rakshas unhe zabardasti nahi kha gaya

Sab log apne karm ke phal bhogte hain

Unhone kaha:

“Tum bhi is vināsh ke sirf ek madhyam ban rahe ho.”

🌼 Krodh se Shaanti ki Or

Pulastya aur Vasishtha ke shabd
Parāśara ke dil tak pahunch gaye.

Unhone apni aankhen band ki
aur gahri saans li.

Fir dheere se kaha:

“Main apna yagya yahin samaapt karta hoon.”

🔥 Agni ka Antim Gaman

Parāśara ne yagya ki agni ko
Himavat ke uttar ke gehre van mein daal diya.

Kaha jaata hai:

Woh agni aaj bhi wahan jalti hai

Rakshason, pedon aur patharon ko bhasm karti hai

Par bina poori srishti ko nuksaan pahunchaye

🌟 Is Katha ka Moral (Seekh)

❌ Andha badla dharma nahi hota

✅ Shaanti aur samajh hi sabse badi shakti hoti hai

🔥 Krodh ko mitaana nahi, sahi disha dena chahiye

🕊️ Mahaan wahi hai jo
krodh par vijay paaye

Parāśara ne yeh seekh di
ki shaanti hi sabse badi tapasya hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.18
        with st.expander("Section 1.11.18"):
            text1 = """ 
            Section CLXXXIV – Kalmashapada, Vasishtha aur Sachchai ka Rahasya (Hinglish Moral Story Rewrite)

Arjuna ne Gandharva se vinamrta se poocha:
“Yeh batao,
King Kalmashapada ne apni rani ko
Rishi Vasishtha ke paas kyun bheja?
Aur Vasishtha jaise mahaan Rishi ne
aisa kaam kyun kiya?
Kya yeh paap tha?”

Gandharva ne shant swar mein jawab diya."""
            create_image_text_layout("attached_assets/chapter1/1.11.18.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌲 Shraap ke Baad ka Andhera Jeevan

King Kalmashapada
pehle hi Saktri ke shraap ke kaaran
apna santulan kho chuke the.

Woh apni rani ke saath
ghane jungle mein bhatak rahe the

Unka mann bhatak chuka tha

Bhookh aur krodh ne
unki buddhi dhundhli kar di thi

Ek din, bhookh se pareshan hokar,
unhone jungle mein ek Brahmana aur uski patni ko dekha
jo saath the.

😢 Ek Bhayanak Paap

Dar ke maare woh dono bhaag gaye.
Lekin Kalmashapada ne
Brahmana ko pakad liya.

Brahmani ne rote hue kaha:
“Hey Maharaj,
main apne pati ke saath thi.
Meri iccha abhi poori bhi nahi hui.
Kripya unhe chhod do.”

Lekin shraap ke prabhav mein
Kalmashapada ne
us Brahmana ko maar diya aur kha gaya.

🔥 Brahmani ka Shraap

Yeh dekh kar Brahmani ka dukh
aag ban gaya.

Usne shraap diya:

“Jis din tum apni patni ke paas jaoge,
usi din tumhari mrityu ho jaayegi.”

“Tumhari rani ek putra ko janm degi,
lekin Vasishtha Rishi ke dwara.”

“Wahi putra
tumhari vansh ko aage badhaayega.”

Shraap dekar
woh Brahmani
aag mein sama gayi.

🕊️ Vasishtha ka Gyaan aur Maryada

Rishi Vasishtha ne
apni tapasya aur gyaan se
sab jaan liya.

Bahut samay baad,
jab Kalmashapada shraap se mukt hue,
woh apni rani Madayanati ke paas gaye.

Lekin rani ne mana kar diya.
Us shraap ki yaad aa chuki thi.

Tab raja ko apni galti ka
gehra pachtava hua.

🌱 Paap Nahi, Kartavya

Isliye raja ne
Vasishtha se prarthana ki
ki woh rani ko putra pradaan karein.

Yeh kaam vasna se nahi,
balki dharma aur vansh ki raksha ke liye tha

Vasishtha ne
apna kartavya nibhaya

Ismein koi paap nahi tha

🌟 Is Katha ki Seekh (Moral)

❌ Shraap aur krodh
insaan ko galat raaste par le jaate hain

✅ Mahaan log
kartavya ko bhavna se upar rakhte hain

🕊️ Kabhi-kabhi
kathin faisle bhi
dharma ke liye lene padte hain

🌱 Sachchi pavitrata
mann aur uddeshya mein hoti hai

Yeh kahani sikhaati hai:
Har ajeeb ghatna paap nahi hoti,
kabhi-kabhi woh dharma ka gehra roop hoti hai."""
            create_image_text_layout(text_content=text2, layout="full")

        # Section 1.11.19
        with st.expander("Section 1.11.19"):
            text1 = """ 
            Section CLXXXV – Pandavas ko Mila Sahi Guru (Hinglish Moral Story)

Arjuna ne Gandharva se poocha:
“O Gandharva,
aap sab kuch jaante ho.
Humein batao,
kaun sa Veda-jaanne wala Brahmana
hamara Guru (priest) banne ke yogya hai?”"""
            create_image_text_layout("attached_assets/chapter1/1.11.19.jpg", text1, layout="side", image_position="left")
            text2 = """ 
            🌿 Gandharva ka Salah

Gandharva ne shaant swar mein kaha:
“Is jungle mein
Utkocaka naam ka ek pavitra aashram hai.
Wahan Rishi Dhaumya,
jo Devala ke chhote bhai hain,
tapassya kar rahe hain.

Agar tum chaho,
unhe apna Guru bana sakte ho.”

🔥 Arjuna ka Dhanyavaad

Sab sun kar Arjuna bahut prasann hua.
Usne shraddha ke saath
apna agni-astra (fire weapon)
Gandharva ko wapas de diya.

Arjuna ne kaha:
“O Shreshtha Gandharva,
jo divya ghode aapne humein diye the,
abhi aapke paas hi rahne do.
Jab samay aayega,
hum unhe le lenge.”

Dono ne
ek-doosre ko pranam kiya
aur apne-apne raaste chal pade.

🏞️ Rishi Dhaumya ka Aashram

Pandavas apni maa Kunti ke saath
Utkocaka ke aashram pahunche.

Rishi Dhaumya ne
unhe phal aur kand-mool dekar
prem se swagat kiya.

Pandavas ne vinamrata se
unse apna Guru banne ki prarthana ki.

Rishi Dhaumya ne
prasann hokar sweekar kar liya.

🌸 Nayi Shuruaat ka Vishwas

Guru milte hi
Pandavas ka mann mazboot ho gaya.

Unhe laga:

Jaise unka raajya wapas mil hi gaya ho

Jaise Panchal rajkumari ka swayamvar
unka intezaar kar raha ho

Rishi Dhaumya
Vedo aur dharma ke gyaata the.
Unhone Pandavas ko
apna yajmaan (shishya) banaya.

Guru ko dekh kar
unhe poora bharosa tha
ki yeh veer bhai
apne karm aur gun se
sab kuch phir se paa lenge.

🌟 Is Kahani ki Seekh (Moral)

🙏 Sahi Guru jeevan ka sabse bada sahara hota hai

🌱 Jahan dharma aur gyaan hota hai,
wahan bhavishya surakshit hota hai

💫 Vinamrata aur shraddha
hamesha sahi raasta dikhati hai

🕊️ Guru mil jaaye to
mushkil safar bhi aasaan lagta hai

Is tarah,
Pandavas apne Guru ke saath
Panchal ki disha mein
ek nayi umeed aur vishwas ke saath
aage badhne ka nirnay lete hain 🌼"""
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

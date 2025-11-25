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


    # Chapter1
    with st.expander("Chapter 1.1 – Anukramanika Parva"):
        with st.expander("Section 1.1.1"):
                text1 = """
⭐ Part 1: Sauti aur Naimisha ke Rishiyon ka Milan

Om! Kahaani ki shuruaat ek pavitra pranam se hoti hai.
Sabse pehle Narayana aur Nara ko pranam.
Aur devi Sarasvati ko bhi vandan.
Phir shabd “Jaya” bola jata hai — jiska matlab hota hai victory.

🌿 Sauti ka Aagman

Ek din Ugrasrava Sauti, jo Lomaharshana ka beta tha,
aur jo Puranas ka bahut bada gyaani tha,
Naimisha ke gahan van (forest) me gaya.

Wahan 12 saal ka ek maha-yajna (great sacrifice) chal raha tha
jise Saunaka Kulapati naam ke bade rishi kar rahe the.

Rishigan wahan shant, sukh se baithe the.
Jab Sauti unke paas pohoncha, sab uski taraf dayaluta se dekhnay lage
kyunki woh unke liye purani, adbhut kahaaniyan sunane wala tha.

        """
                create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                text2 = """
🙏 Sauti ka Namaskar

Rishiyon ne Sauti ka bahut samman kiya.
Sauti ne sab Muniyon (sages) ko pranam kiya
aur unse poocha:
“Aap sab ki tapasya (penance) theek chal rahi hai na?”

Sab rishi shaant hokar baith gaye,
aur Sauti ko ek aasana diya.
Woh wahin vinamrata se baith gaya.

❓ Rishiyon ka Sawal

Ek rishi puchne lage:

“Hey Sauti, tum kahan se aaye ho?
Kahan ghoom kar aa rahe ho?
Humein sab kuch detail me batao.”

📖 Sauti Ka Jawab

Sauti ne halka sa muskurate hue kaha:

“Main bahut saari pavitra kahaniyan sun kar aa raha hoon—
jo Bhagwan Vyasa (Krishna-Dvaipayana) ne Mahabharata me likhi hain,
jise Rishi Vaisampayana ne Raja Janamejaya ke sarp-yajna me sunaaya tha.

Main pavitra tirthon me gaya,
bharat ke sacred waters aur holy places dekhe.
Phir main Samantapanchaka naam ke kshetra (region) gaya—
yahi woh jagah hai jahan purane samay me
Kaurav-Pandav ka maha-yudh hua tha.”

🌞 Sauti ne kaha:

“Rishiyon, aap sab mere liye Brahma ke samaan ho.
Aap log yajna kar chuke ho,
dhyaan kar chuke ho,
aur ab shaant hokar baithe ho.

Batayein—
kya main Purano ki kathayein sunaun?
Ya dharm aur jeevan ke niyam batane wali kahaniyan?
Ya rajaon aur mahan rishiyon ke karmik (deeds) prabandh sunaun?”

📜 Rishi Ka Uttar

Rishiyon ne kaha:

“Humein woh pavitra Purana sunna hai
jo Vyasa ne banaya—
jo sab granthon me sabse uttam maana jata hai,
jise sun kar paap door hote hain.

Humein Mahabharata sunao—
jaise Vaisampayana ne Janamejaya ke yajna me sunaya tha.”

🌺 Sauti ne Ishwar ko Namaskar kiya

Sauti ne prarthana ki:

“Main Ishana, Vishnu aur Hari ko pranam karta hoon—
jo sabke upar hain, jo srishti ke karta bhi hain aur palanhar bhi.”

Phir Sauti ne kaha:

“Ab main Vyasa ji ke pavitra vichaar aap sab ko sunaunga.”


        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.1.2"):
                    text1 = """
 🌌 Part 2: Srishti ka Mahadivya Andaa

Bahut purane samay me, duniya me na roshni thi, na rang.
Sab kuch andhera (darkness) tha.
Isi gehre andhere me ek maha-aadbut cheez bani —
ek bohot bada cosmic egg, jise Mahadivya kaha gaya.

Yahi andaa sab jeevon ka beej (seed) bana.
Isi se Brahma ji—jo eternal (amar) aur invisible (adrishya) the—
prakat hue.

🌟 Brahma se Srishti ki Shuruaat

Mahadivya ande se nikle:

Pitamaha Brahma

Suraguru (guru of devas)

Sthanu (dusra naam Shiva ka)

Phir prakat hue 21 Prajapati jisme shamil the:
Manu, Vasishtha, Parameshthi, Daksha, aur Daksha ke 7 putra.

Uske baad aaye
Visvedevas, Adityas, Vasus, Ashvins, Yakshas, Sadhyas, Pisachas (spirits),
Guhyakas (mystic beings), aur Pitris (ancestors).

Phir aaye Brahmarshis aur Rajarshis—
bade mahan aur pavitra rishi.

            """
                    create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
 🌍 Puray Jahan ka Nirman

Iske baad bani:

Pani

Aakash

Dharti

Hawa

Dishaayen

Samay (years, seasons, months)

Din-raat

Yani saara jagat.

🔄 Yugon ka Chakra

Mahabharata ke hisaab se:

Jab Yug khatam hota hai, sab kuch vinash ho jata hai.
Phir naye yug me sab phir se janm lete hain.

Yeh chakra (cycle) kabhi rukta nahi.
Iska na koi shuruaat hai, na koi ant.

👼 Devo ki Vanshavali (Lineage)

Devas ki ek sankshipt sankhya batayi gayi:
33,000 + 3,300 + 333.

Div ke putra the — Brihadbhanu, Arka, Bhanu, Ravi, Savita, etc.
Phir unke vanshaj the—
Dasa-jyoti, Sata-jyoti, Sahasra-jyoti—
jinme se har ek ke hazaaron putra huye.

Inke vanshaj se hi paida huye:

Kuru vansh

Yadu vansh

Bharata vansh

Yayati aur Ikshvaku ki parampara

Yeh wahi vansh hain jinme se aage chal kar
Pandav, Kaurav, aur Krishna jaise mahan log aaye.

📚 Gyan ka Sagar — Vyasa ji ka Kaam

Vyasa ji ne:

Vedas ke rahasye (mysteries)

Yoga

Vijnana (knowledge)

Dharma, Artha, Kama ke niyam

Puranon ki kathayen

Grahon, sitaron, yugon, rashtron ke gyaan

Kalpas (cosmic cycles)

Yudh ka kala

Sanskriti, sabhyata, aur logon ke charitra

sab kuch likh dala.

Ek bahut bada granth tayaar hua—
jeevo ke jeevan ka poora saar.

Unhone Mahabharata ko
detailed aur short dono roop me likha.

👁️‍🗨️ Ganesh ji ko Lekhak Banana

Vyasa ji ko chinta thi—
itna bada granth kaun likhega?

Tab Brahma ji unke samne aaye aur bole:
“Ganesh ji ko bulao, woh tumhara likhne wala hoga.”

Ganesh ji aaye aur shart rakhi:
“Main tabhi likhunga jab tum bina rukke sunate jaoge.”

Vyasa ji bole:
“Jab bhi tumhe samajh na aaye, likhna rok dena.”

Aur phir Mahabharata likhna shuru hua.

            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.1.3"):
                    text1 = """
🌼 Vyasa aur Brahma ka Samvaad

Brahma ji ne Vyasa ji se kaha:

"Hey Muni, tumhari divine mysteries (adhyatmik raaz) ki samajh bohot gehri hai.
Tumne jo granth banaya hai, woh ek maha-kavya hoga.
Aur duniya me koi bhi kavi tumhari kavita ka samaan nahi likh payega.

Isliye, Bharata ko likhne ke liye Ganesa— hurdles hatane wale devta—ko yaad karo."

🐘 Ganesh ji Lekhak Bante Hain

Brahma ji ke jaane ke baad, Vyasa ji ne Ganesh ji ko smaran kiya.
Aur Ganesh ji turant prakat ho gaye.

Vyasa ji bole:

“Hey Ganesh ji, aap mere granth Bharata ke lekhak baniye.”

Ganesh ji bole:

“Maan lo. Par ek shart hai —
meri kalam ek pal ke liye bhi nahi rukni chahiye.”

Vyasa ji bole:

“Aur jab bhi aapko koi baat samajh na aaye, tab likhna rok dena.”

Is tarah dono ka samjhauta ho gaya.
Ganesh ji ‘Om’ bolkar likhna shuru kar diye,
aur Vyasa ji kathin, gahan slokas (complex verses) sunaane lage.

Kehete hain ki inme se kuch slok aaj bhi log poori tarah samajh nahi paate.
            """
                    create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🌳 Bharata – Ek Vriksh ki Tarah

Sauti kehte hain:

“Bharata ek bada gyan-vriksh (tree of knowledge) jaisa hai.”

Contents chapter — is vriksh ka beej (seed)

Pauloma aur Astika — jad (roots)

Sambhava Parva — tana (trunk)

Sabha aur Aranya Parva — shaakha jahan pakshi baithte hain (roosting branches)

Arani Parva — guthiyan / knots

Virata aur Udyoga Parva — gudda (pith)

Bhishma Parva — mukhya shaakha (main branch)

Drona Parva — patte (leaves)

Karna Parva — phool (flowers)

Shalya Parva — unki mehak (fragrance)

Stri aur Aishika Parva — chhaya (shade)

Shanti Parva — phal (fruit)

Ashvamedha Parva — amrit-saar (immortal sap)

Ashramavasika Parva — zameen jahan vriksh ugta hai

Mausala Parva — Vedas ka saar (essence of Vedas)

Yeh vriksh kabhi khatam nahi hota,
aur sabhi kavi aur vidvans isse sada laabh le sakte hain.

👶 Vyasa ji aur Kuru Vansh

Sauti aage batate hain:

Vyasa ji ne apni tapasya (penance) se teen putron ko janm diya—
Dhritarashtra, Pandu aur Vidura.
Inke bade hote hi Vyasa ji ne Mahabharata ko duniya ko diya.

Janamejaya aur anek Brahmano ne Vyasa ji se prarthna ki,
to unhone apne shishya Vaisampayana se pura Mahabharata sunaaya.

Vyasa ji ne:

Gandhari ki pavitrata

Vidura ki gyaan ki gehraayi

Kunti ki nishtha

Pandavon ka charitra

Vasudeva Krishna ki divyata

Kauravon ki dushta pravritti

sab ka sundar varnan kiya.

🐅 Pandavon ka Balpan

Pandav:

Rishi-ashram me bade hue

Vedas aur shastras padhe

Sabke priya bane

Yudhishthira ki satyata sabko pasand aayi.
Arjuna ka sahas sabko aashcharya karta.
Bhima balwan tha.
Nakula–Sahadeva vinamra (humble) the.

Arjuna ne swayamvara me kathin dhanurvidya dikhakar Krishna (Draupadi) ko jeeta.
Fir usne rajyon ko jeeta,
aur Yudhishthira ko Rajasuya Yagya karne layak banaya.

💎 Duryodhana ki Jalan

Rajasuya me Pandavon ka dhan–vaibhav dekh kar
Duryodhana ke dil me jalan (envy) bhar gayi.

Sabha me Maya danav ki banayi hui imaarat
uske liye jadugar-jaise bhram (illusion) se bhari hui thi.

Ek jagah par woh phisal gaya aur behad sharminda hua.
Bhima ne uska mazaak udaaya.
Aur tabhi se uske mann me dvesh (hatred) badhta gaya.
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.1.4"):
                    text1 = """
🌑 Duryodhana ki Jalan aur Dice Game ka Aarambh

Duryodhana ki haalat dhire–dhire kamzor hone lagi.
Woh ameer cheezein paakar bhi meagre (kamzor) aur pale (peela–sa) dikhne laga.

Yeh dekhkar Dhritarashtra apne bete ke pyaar me pighal gaya.
Aur usne Pandavon ke saath dice game (jua) khelne ki ijazat de di.

Krishna (Vasudeva) ko jab yeh pata chala, to woh wroth (bahut gusse me) ho gaye.
Par unhone beech me padkar kuch roka nahi.
Is tarah jua, dhokha, aur anya anya anyay (injustice) ke kaaran
dheere–dheere woh maha-yuddh tayyar ho gaya
jisme sab Kshatriya ek dusre ko maarne lage.

👑 Dhritarashtra ka Paashchatap

Baad me, jab Dhritarashtra ko pata chala
ki Pandav ek ek kadam par jeet rahe hain,
aur uske bete Duryodhana, Karna aur Shakuni ka chaal galat pad gaya,
to woh dukhi hokar Sanjaya se kehne laga:
            """
                    create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🗣 Dhritarashtra ka Lamba Dukh-bhara Prasang

“Hey Sanjaya, meri baat dhyaan se suno.

Main kabhi yuddh nahi chahata tha.
Main kabhi apni vansh ka naash nahi chaah sakta tha.
Maine Pandav ya Kaurav me koi bhed-bhav nahi kiya.

Par mere apne bete ziddi the…
aur meri andhapan aur budhappe ka mazaak banate the.
Main bekaar hi unka dhyan rakhta raha.

Duryodhana ki sabse badi bewakoofi thi uska envy (jalan).
Pandavon ki sabha me jab woh phisla aur log hase,
to uska gussa aur badh gaya.
Aur usne Shakuni ke saath milkar अनुचित dice game ki saazish rachi.”

💔 Dhritarashtra – “Mujhe tab se haar dikhne lagi”

Fir Dhritarashtra Sanjaya ko sab wahi pal bataata hai
jab usne socha ki:

➡️ “Ab hamari taraf se jeet ki koi umeed nahi bachi.”

Woh har ek ghatna ko yaad karta hai:

⭐ 1. Arjuna ne Draupadi swayamvara jeeta — tab se mujhe umeed nahi rahi.

(Uski dhanurvidya dekh kar sab hairaan the.)

⭐ 2. Arjuna ne Subhadra ko vivaah ke liye le gaya — aur Krishna–Balarama bhi khush the.

(Maine socha – agar Krishna Pandavon ke saath ho, hum jeet nahi sakte.)

⭐ 3. Arjuna ne Indra ki baarish rok kar Khandava jungle Agni ko diya.

(Yeh asambhav kaam tha.)

⭐ 4. Pandav lac wale ghar se bach gaye — Vidura ki madad se.
⭐ 5. Arjuna ne draupadi ko jeet kar Panchalon ko saath mila liya.
⭐ 6. Bhima ne Jarasandha ko haath se hi maar diya.
⭐ 7. Pandavon ne Rajasuya Yagya kiya aur sab raja unke adheen ho gaye.
⭐ 8. Draupadi ko sabha me dora gaya — aur Dushasana usey vastraharan me asafal raha.

(Yeh dev-kripa ka saboot tha.)

⭐ 9. Yudhishthira sab kuch haar kar bhi bhaiyon ke saath ekjut raha.
⭐ 10. Arjuna ko Pasupata astra (divine weapon) mila.

(Shiva ne khud diya.)

⭐ 11. Arjuna swarg gaya, Indra se astra laaye.
⭐ 12. Bhima aur Pandav Kubera ke lok tak pahunch gaye.

(Yeh aam manusya ka kaam nahi.)

⭐ 13. Mere bete Gandharvon dwara bandi banaye gaye — Arjuna ne aakar chhudaaya.

(Isse unki shakti aur badhi.)

⭐ 14. Yudhishthira ne Yaksha ke prashna sahi diye — aur sabko jeevit kiya.
⭐ 15. Pandav Virat ke raj me gopniya roop me rahe — koi pehchaan nahi saka.
⭐ 16. Arjuna ne ek hi rath se pura Kaurav sena ko Virat me hara diya.
⭐ 17. Krishna ne Pandavon ka saath pakad liya — yeh hamari sabse badi haar thi.
⭐ 18. Uttara ka vivaah Arjuna ke bete Abhimanyu se hua — Pandav-Rajvansh aur mazboot ho gaya.
⭐ 19. Pandavon ne vanvas ke baad bhi saat Akshauhini sena jod li.
⭐ 20. Narada ne kaha ki Krishna aur Arjuna — Nara aur Narayana hain.

(Devta jaisa saath mila tha unhe.)

⭐ 21. Krishna shaanti ke liye gaye, par Duryodhana ne maan karak diya.
⭐ 22. Krishna ko kaid karna chaha — par Krishna ne apne sharir me poora brahmand dikha diya.
⭐ 23. Bhishma, Drona, Vidura — sab Pandavon ko aashirvaad dete rahe.
⭐ 24. Karna ne kaha: “Main Bhishma ke saath nahi ladunga.”
⭐ 25. Kurukshetra me Krishna aur Arjuna ek saath aaye — yeh vinash ka sanket tha.
⭐ 26. Arjuna jad ho gaya — Krishna ne usko apna Vishwaroop dikhaya.
⭐ 27. Bhishma Pandavon ko kabhi nahi maar paaye — par roj 10,000 warriors maarte rahe.
⭐ 28. Bhishma ne apna mrityu-ka-rahasya bataya — Pandavon ne turant use lagu kiya.
⭐ 29. Arjuna ne Shikhandi ko aage rakhkar Bhishma ko gira diya.
⭐ 30. Bhishma shar-sayya par the — aur Arjuna ne unko paani diya.
⭐ 31. Devta Pandavon ke saath ho gaye — hamari haar nischit lagne lagi.
⭐ 32. Drona ne bhi Pandavon ko nahi mara.
⭐ 33. Sansaptakon ko Arjuna ne akela hi maar diya.
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.1.5"):
                    text1 = """
🔱 Dhritarashtra’s Final List of Despair

Dhritarashtra Sanjaya se bolta raha:

⭐ Arjuna’s Vow

“Jab maine suna ki Arjuna ne Saindhava ko maarne ki kasam khaayi
aur us kasam ko dushmano ke saamne poora kiya,
tab, hey Sanjaya, mujhe phir jeet ki bilkul umeed nahi rahi.”

⭐ Krishna Saving the Horses

“Jab maine suna ki Arjuna ke ghode thak gaye the,
to Krishna (Vasudeva) ne unko khud khola,
unko paani pilaya, wapas bandh kar unhe rath me joda
aur phir chalate rahe—
tab bhi mujhe umeed nahi rahi.”

⭐ Arjuna Fighting Alone

“Jab maine suna ki ghode thakne ke baad bhi
Arjuna akela rath par khada hokar
sab dushmano ko rok raha tha,
tab toh main poori tarah toot gaya.”
            """
                    create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
⭐ Yuyudhana’s Retreat

“Jab suna ki Yuyudhana (Satyaki),
jo Drona ki sena ko elephants ki wajah se rok nahi paaya,
Krishna aur Arjuna ke paas bhaag kar wapas aaya,
tab bhi mujhe umeed nahi rahi.”

⭐ Karna Letting Bhima Go

“Karna ne jab Bhima ko pakad kar chhod diya,
sirf kuch buri baatein bolkar—
tab mujhe laga hamari buri haalat pakki hai.”

⭐ Saindhava’s Death Allowed by All Great Warriors

“Jab suna ki Drona, Kripa, Karna, Ashwatthama aur Shalya
milkar bhi Saindhava ko bachaa nahi paaye,
tab samajh gaya hum jeet nahi sakenge.”

⭐ Indra’s Shakti Used on Ghatotkacha

“Indra ka diya hua Sakti astra (divya hathiyaar)
jo Karna ko Arjuna ko maarne ke liye diya gaya tha—
woh Krishna ki chaal se Ghatotkacha par chal gaya.
Tab mujhe samajh aaya hamari haar nischit hai.”

⭐ Ghatotkacha’s Death

“Yehi Shakti jo Arjuna ko maar sakti thi,
Karna ne Ghatotkacha par chal di—
Arjuna bach gaya.
Is pal se main haar gaya tha.”

⭐ Drona’s Death

“Jab suna ki Dhrishtadyumna ne
battle ke niyam todkar (transgressing the laws),
akelye Drona ko maar diya,
tab bhi umeed khatam ho gayi.”

⭐ Nakula vs Ashwatthama

“Jab Nakul ne Ashwatthama se akela ladkar
puray sena ke saamne use ghuma diya,
tab main aur ghabra gaya.”

⭐ Narayana Astra Fail

“Drona ke marne ke baad
Ashwatthama ne Narayan Astra galat tarike se chalaya—
par Pandav bach gaye.
Mujhe pata chal gaya—devta unke saath hain.”

⭐ Bhima’s Terrible Act

“Jab suna ki Bhima ne dushman Dushasana ka khoon pi liya
aur koi use rok nahi saka—
tab main samajh gaya ki yeh yuddh hamari barbadi hai.”

⭐ Karna’s Death

“Karna jaise aparajit (invincible) warrior ko
Arjuna ne maar diya—
jo devtaon ke liye bhi adbhut tha—
tab mujhe bilkul umeed nahi rahi.”

⭐ Yudhishthira Wins Battles

“Yudhishthira ne Ashwatthama ka bhai, Dushasana, aur Kritavarman tak ko hara diya—
tab mujhe pata chal gaya hamari har likhi hai.”

⭐ Shalya’s Death

“Shalya—jo hamesha Krishna ko lalkarta tha—
Yudhishthira ne use maar diya.
Meri umeed bilkul khatm.”

⭐ Shakuni’s Death

“Shakuni—jiski chaalbaazi se sab shuru hua—
Sahadeva ne use maar diya.
Tab mujhe laga—yeh sab hamari apni galtiyon ka phal hai.”

⭐ Duryodhana Hiding in the Lake

“Jab maine suna ki Duryodhana thak kar
jheel me chup gaya aur akela pada tha—
tab mujhe pata chal gaya yeh ant hai.”

⭐ Final Mace Duel

“Fir Pandav aur Krishna ne use bula-bula kar
uska mazaak banaya.
Aur gada-yudh me
Krishna ki salaah par
uski jangha (thigh) par vaar kiya gaya—
jo niyam ke khilaaf tha.
Duryodhana gir gaya…
Aur meri umeed bhi.”

⭐ Night Massacre by Ashwatthama

“Ashwatthama ne raat me
soye hue Panchalon aur Draupadi ke putron ko maar diya—
yeh bhayanak paap tha.”

⭐ Uttara’s Child Attacked

“Fir Ashwatthama ne Aishika astra chala kar
Uttara ke garbh me bache ko bhi hani pahunchayi.”

⭐ Brahmashira Astra Stopped

“Arjuna ne uske Brahmashira astra ko
apne mantra ‘Sasti’ se rok diya.
Aur Ashwatthama ko
apna mani (head-jewel) dena pada.”

⭐ Curses on Ashwatthama

“Uttara ke garbh ko chot lagne par
Vyasa aur Krishna ne Ashwatthama ko shraap diya.”

💔 Dhritarashtra’s Collapse

Dhritarashtra ro kar bolta hai:

“Sirf 10 log bache…
3 hamare…
7 unke…
18 akshauhini sena khatm ho gayi.

Main andhere me hoon, Sanjaya.
Mere jeene ka koi matlab nahi.”

Woh behosh ho jata hai.
Sauti kehta hai—Sanjaya ne use hosh me laakar
dhairya diya.
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.1.6"):
                    text1 = """
🌟 Purane 24 Maha-Rajaon ka Udaharan

“Hey Raja, pehle bhi bohot mahaan raja aaye aur chale gaye.
Unki shakti, daan, veerta aur punya ka zikr dev-rishi Narada (divine sage) ne Saivya ko kiya tha.

Unke alawa aur bhi bahut shaktishaali raja the—
jo mahaan rath-yoddha (chariot warriors) aur uttam charitra wale the.”

Sanjaya ne unke naam ginaaye:

Puru, Kuru, Yadu, Sura, Vishvasrawa

Anuha, Yuvanasvu, Kakutstha, Vikrami, Raghu

Vijava, Virihorta, Anga, Bhava, Sveta, Vripadguru

Usinara, Sata-ratha, Kanka, Duliduha, Druma

Dambhodbhava, Para, Vena, Sagara, Sankriti, Nimi

Ajeya, Parasu, Pundra, Sambhu, Deva-Vriddha

Devahuya, Supratika, Vrihad-ratha

Mahatsaha, Vinitatma, Sukratu, Nala

Satyavrata, Santabhaya, Sumitra, Subala

Janujangha, Anaranya, Arka, Priyabhritya, Chuchi-vrata

Balabandhu, Nirmardda, Ketusringa, Brhidbala

Dhrishtaketu, Brihatketu, Driptaketu, Niramaya

Abikshit, Chapala, Dhurta, Kritbandhu, Dridhe-shudhi

Mahapurana-sambhavya, Pratyanga, Paraha, Sruti

Sanjaya bola:

“In sabke paas bohot daulat, shakti aur naam tha.
Phir bhi yeh sab mrityu ko nahi rok paye.
Inke punya-kaam, sachchai, daya aur veerta ka zikr aaj bhi granthon me milta hai.”
            """
                    create_image_text_layout("attached_assets/chapter1/1.1.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🌟 Tumhare bete kyun gire?

Sanjaya ne spasht kaha:

“Hey Bharata, tumhare bete iska ulta the.
Woh krodhi, lalchi aur dusht pravritti (evil nature) ke the.
Unhone apne hi kalyan ka nash kiya.”

🌟 Karma aur Samay ki Seekh

Sanjaya bola:

“Tum shastra-gyani ho.
Tum jaante ho ki fate (vidhi) ko koi nahi rok sakta.

Astitva aur na-astitva,

sukha aur dukh,

sabka mool Samay (Time) hai.

Samay sab ko banata hai.
Samay sab ko mita deta hai.
Samay hi jagta rehta hai jab sab sote hain.
Samay ko koi hara nahi sakta.”

Sanjaya ne Dhritarashtra ko samjhaya:

“Jab tum jante ho ki sab kuch samay ka phal hai,
to tumhe apni buddhi kyun khona chahiye?”

Is tarah Sanjaya ne Raja ke mann ko shaant kiya.

🌟 Vyasa ka Upanishad aur Mahabharata ki Mahima

Sauti kehta hai:

“In sab ghatnaon ko dekh kar
Vyasa ne ek pavitra Upanishad (sacred spiritual text) banayi.
Ye jnan sab purano me gungaya jata hai.”

Phir woh batata hai:

Mahabharata ka adhyayan punya ka kaam hai.

Ek shlok ka shraddha se paath bhi paap ko mitata hai.

Isme devta, rishi, nag, yaksha sabka gyaan hai.

Vasudeva (Krishna), jo shuddh aur sarvavyapi brahma ke swaroop hain,
unka mahima bhi diya hai.

Jo is granth ko shraddha se padhta hai
woh paap se mukt hota hai,
lambi aayu aur yash paata hai.

Purano ke hisaab se:

Jab 4 Veda ek taraf rakhe gaye

aur Mahabharata ek taraf,
to Mahabharata zyaada bhaari nikla.

Isliye ise Mahā-bhārata kaha gaya—
Bada Bharata, sabse gahra aur sabse pavitra.
            """
                    create_image_text_layout(text_content=text2, layout="full")

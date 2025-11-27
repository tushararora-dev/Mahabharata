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
                    create_image_text_layout("attached_assets/chapter1/1.1.2.jpg", text1,   layout="side", image_position="left")

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
                    create_image_text_layout("attached_assets/chapter1/1.1.3.jpg", text1,   layout="side", image_position="left")

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
                    create_image_text_layout("attached_assets/chapter1/1.1.4.jpg", text1,   layout="side", image_position="left")

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
                    create_image_text_layout("attached_assets/chapter1/1.1.5.jpg", text1,   layout="side", image_position="left")

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

    # Chapter2
    with st.expander("Chapter 1.2 – Sangraha Parva"):
        with st.expander("Section 1.2.1"):
                text1 = """
Rishiyon ne Sauti se poocha:
“O Suta-putra, tumne Samanta-Panchaka ka zikr kiya.
Hum us jagah ki poori kahaani sunna chahte hain.”

🌅 Sauti begins the story

Sauti bola:

“O Brahmano, dhyaan se suno.
Samanta-Panchaka ek bahut hi pavitra (sacred) jagah hai.
Treta aur Dvapara Yug ke beech, Parashurama—Jamadagni ka putra—
jo sabse mahaan yoddha tha,
apne upar hue anyaay (injustice) se gusse me bhar gaya.

Gusse me aakar usne baar-baar Kshatriya vansh ka vinash (destruction) kiya.
Aur jab sab Kshatriya nasht ho gaye,
toh Parashurama ne paanch khoon ke talaab banaye.
Un talaabon ko hi Samanta-Panchaka kaha gaya.”
        """
                create_image_text_layout("attached_assets/chapter1/1.2.1.jpg", text1,   layout="side", image_position="left")

                text2 = """
🩸 Parashurama’s ancestors appear

Sauti aage bolta hai:

“Parashurama itna krodhit tha ki
apne pitron (ancestors) ko khoon ki ahuti (offering) dene laga.
Tab unke purvaj Richika aur anya Pitri prakat hue aur bole:

‘O Rama, hum tumse prasann hain.
Koi bhi var (boon) maango.’

Parashurama ne kaha:
‘Agar aap khush hain, to mera paap (sin) door ho
jo gusse me maine Kshatriya ka vinaash kiya.
Aur yeh paanch talaab duniya me pavitra sthal ke roop me mashhoor ho jayein.’

Pitron ne kaha:
‘Tathastu! Shant ho jao.’
Aur tab se woh sthal Samanta-Panchaka pavitra maana gaya.”

⚔️ The Great War at Samanta-Panchaka

Sauti kehta hai:

“Dvapara aur Kali Yug ke beech,
usi jagah par Kaurav aur Pandav ki maha-yudh hui.
Wahan 18 Akshauhini sena ikatthi hui thi.
Saare yoddha wahaan shaheed ho gaye.
Isliye us jagah ka naam teenon lokon me prasiddh hai.”

⭐ What is an Akshauhini?

Rishiyon ne poocha:

“O Suta-putra, Akshauhini ka matlab kya hai?
Kitne ghode, rath, haathi aur paidal fauj hoti hai?”

📘 Sauti explains the Akshauhini math

Sauti bola:

1 Patti = 1 rath + 1 haathi + 5 padati (foot soldiers) + 3 ghode

3 Patti = 1 Sena-mukha

3 Sena-mukha = 1 Gulma

3 Gulma = 1 Gana

3 Gana = 1 Vahini

3 Vahini = 1 Pritana

3 Pritana = 1 Chamu

3 Chamu = 1 Anikini

10 Anikini = 1 Akshauhini

Phir Sauti ne sankhya batayi:

21,870 rath

21,870 haathi

65,610 ghode

109,350 pathal sena

Yeh sab mil kar 1 Akshauhini banti hai.

18 Akshauhini me hi
Mahabharat ka Yudh lada gaya.

⭐ Duration of the Great War

Sauti bolta hai:

Bhishma ne 10 din lada.

Drona ne 5 din sena ki rakhsha ki.

Karna ne 2 din yudh kiya.

Shalya ne aadha din yudh kiya.

Phir aadhe din me Bhima aur Duryodhana ka gada-yudh hua.

Aur raat ko Ashwatthama aur Kripa ne soyi hui Pandav sena ko maar diya.

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.2"):
                text1 = """
Sauti ne Saunaka se kaha:

“O Saunaka, yeh jo Bharata katha tumhare yagya me sunayi ja rahi hai,
yeh pehle Janamejaya ke yagya me Vyasa ke ek buddhimaan shishya ne sunayi thi.

Is katha ko kai hisson (parva) me baanta gaya hai.
Shuruaat me Paushya, Pauloma, aur Astika parva aate hain,
jismein purane rajaon ki shaurya (valour) aur kirti batayi gayi hai.

Yeh granth bahut hi sundar hai—
iska bhasha, iska arth, aur iski kahaani sab adbhut hai.
Isme aneek riti-rivaj (rites) aur jeevan ke tarike bhi diye gaye hain.
Gyani log ise ussi tarah maante hain
jaise moksha chaahne wale vairagya ko maante hain.

Jaise sab gyaan me Atma sabse uchit hai,
aur sab priya cheezon me pran sabse mahatvapurna hain,
waise hi sab shastron me Mahabharata sabse shreshth maana gaya hai.

Duniya ki koi bhi kahaani aisi nahi jo iss mahaan katha se judi na ho—
jaise sharir chalne ke liye pairon par nirbhar hota hai,
waise hi kahania Mahabharata par.

Yeh granth kavi aur vidvaanon ka priya hai.
Jaise sab vidyaon ke shabdon me swar aur vyanjan hota hai,
waise hi iss granth ke sab parvon me param gyaan basa hua hai.”
        """
                create_image_text_layout("attached_assets/chapter1/1.2.2.jpg", text1,   layout="side", image_position="left")

                text2 = """
⭐ Parvon ki Saral List (Hinglish)

Sauti ne kaha:

“Sun lijiye, O tapasviyon,
Mahabharata ke mukhya parvon ka saral saar:

🔹 Aadi Parva ke Parv

Anukramanika

Sangraha

Paushya

Pauloma

Astika

Adivansavatarana

Sambhava (janmon ki kathayen)

🔹 Baad ke Pramukh Parv

Jatugriha Dahan (laakh ke ghar ko jalana)

Hidimba Vadha

Baka Vadha

Citraratha

Swayamvara (Draupadi swayamvara)

Vaivahika (vivah)

Viduragamana

Rajyalabha

Arjuna Vanavasa

Subhadra Harana

🔹 Khandava aur Sabha Parva

Khandava-daha (van ka dahan)

Maya-darshana

Sabha, Mantra, Jarasandha, Digvijaya

Rajasuuya, Sisupala-vadha

Dyuta (jua), Anudyuta, Aranyaka, Kirmira-Vadha

🔹 Vanvas aur Yudh ke Purv kisse

Arjuna-Vigamana (Arjuna ka yog yatra)

Kairati (Arjuna–Mahadev yudh)

Indraloka yatra

Nalopakhyana (Nala-Damayanti)

Tirthayatra

Jatasura Vadha

Yaksha Yudh

Nivatakavacha Yudh

Ajagara, Markandeya Samasya

Draupadi–Satyabhama Samvad

Jayadratha Kaand

Savitri ki kahani

Rama katha

🔹 Virata aur Udyoga Parva

Virata Parva

Kichaka Vadha

Gau-charan (Virat ki gaiyon ka kand)

Abhimanyu Vivah

Udyoga Parva

Sanjaya-yana

Sanatsujata

Krishna ka durbar me aana

🔹 Yudh (Bhishma–Drona–Karna–Shalya)

Amba

Bhishma ko senapati banana

Jambu–Dvip varnan

Bhagavad Gita

Bhishma-vadha

Drona-vadha

Abhimanyu-vadha

Jayadratha-vadha

Ghatotkacha-vadha

Narayana-astra

Karna Parva

Shalya Parva

Gada-yudh (Bhima vs Duryodhana)

🔹 Yudh ke baad

Sarasvata

Tirtha varnan

Vanshavali

Sauptika (Ashwatthama ka raat ka kand)

Aishika (brahmastra sanhaar)

Jalapradana (shraaddh)

Naripravasa (streeon ka shok)

Shraddha Parva

Charvaka vadha

Yudhishthira rajyabhishek

Shanti, Rajadharma, Apaddharma, Mokshadharma

Anusasanika Parva

Bhishma moksha

Ashwamedha

Anugita

Ashramavasa

Putradarshana

Mausala (Yadavo ka ant)

Mahaprasthanika

Svargarohana

Khilvansa (Vishnu katha, Balyan Lila, Kansa vadha, Bhavishya)

Sauti ne bataya ki in sab milakar 100 parva hote hain,
jinhe Vyasa ne 18 mukhya bhaagon me baanta
aur jinhe Sauti ne Naimisharanya me sunaya.

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.3"):
                text1 = """
Adi Parva ke andar bahut saare upa-parva (sections) hote hain. Unme ye sab kathayen aati hain:

🔶 1. Paushya Parva

Isme Rishi Utanka ki mahanta aur unke anokhe karmon ka varnan hai.

🔶 2. Pauloma Parva

Isme Bhrigu Rishi ke vanshajon ki kahani di gayi hai.

🔶 3. Astika Parva

Isme bahut vishal ghatnayen bataayi gayi hain:

Garuda ka janma

Nagon (serpents) ka janma

Samudra manthan (ocean churning)

Uchhaishrava – devtao ka swargiya ghoda ka janma

Bharata vansh ka itihas, jaisa ki Raja Janamejaya ke sarp-yagya me Vyasa ne bayan kiya tha.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.3.jpg", text1,   layout="side", image_position="left")

                text2 = """
🔶 4. Sambhava Parva

Yeh parva bahut lambe janm-kathanon ka sangrah hai:

Vibhinna rajaon aur mahan veeron ka janma

Krishna Dvaipayana Vyasa ka janma

Devo ke ansh-avatar ka prakat hona

Danavo, Yakshon, Gandharvon, Pakshiyon, aur sabhi praniyon ka utpatti-varnan

Raja Bharata ka pura jeevan – Shakuntala ka putra, jiske naam se Bharata vansh chalta hai

Bhagirathi ka mahatva

Vasuon ka janma aur unka swarg gati

Bhishma ka janma, Vasus ke tej se janma hua, aur unka brahmacharya aur raj-tyag

Citrangada aur baad me Vicitravirya ki raksha

Mandavya muni ke shraap ke karan dharma ka manushya rup me janma

Dhritarashtra aur Pandu ka janma (Vyasa ke tapasya se)

Pandavon ka janma

Isme aage:

Duryodhana aur uske bhaiyon ki chalakiyan — Pandavon ko Varanavat bhejna

Vidura ka gupt-sandesh mleccha bhasha me

Laakh ke ghar me surang banana

Ghar jalna aur Purochhana ka marna

Ek shikari ki patni aur uske 5 putron ka jalna (jisse sabko lage Pandav mar gaye)

Fir:

Jungle me Hidimba aur uska bhai Hidimba rakshas se mulaqat

Bhima dwara Hidimba ka vadha

Ghatotkacha ka janma

Pandavon ka Vyasa se milna

Unka Ekachakra nagar me brahman ke ghar me rehna

Asura Vaka ka vadha

🔶 5. Draupadi khand

Is parv me:

Krishna (Vasudeva ke roop me) aur Dhrishtadyumna ka divya-aavirbhav

Pandavon ka Panchal ke swayamvara ke liye nikalna

Raste me Gandharva Angaraparna se Arjun ka yudh

Tapati, Vashishtha, aur Aurva ki kahani (Gandharva se suni)

Fir:

Panchal pahunchna

Arjun dwara Draupadi ka swayamvara jeetna

Baad me sabhi rajaon ka Arjun aur Bhima se paraajit hona

Balarama aur Krishna ka pehchan lena ki yehi Pandav hain

Pandavon ka kumbhar ke ghar wapas aana

Drupada ka shock ki Draupadi 5 pati se shaadi karegi

5 Indraon ki kahani ka prakat hona (jin par shaadi ka niyati aadhar tha)

Draupadi ka divya-vivah

Vidura ka sandesh Pandavon ko bhejne aana

Khandavaprastha me Pandavon ka rehna aur rajya ka aadha hissa paana

Narada ke aadesh se Draupadi ke saath rehne ka niyam (rotation system)

Fir:

Sunda–Upasunda ki kahani ka varnan

Arjuna ka vanvas — kyunki usne Draupadi ko Yudhishthira ke saath dekhta hua astra lene ke liye kosh me pravesh kiya

Raste me:

Ulupi Naga kanya se milna

Teerthon ka darshan

Vabhruvahana ka janma

Panch dev-kanyaaon ko moksha dilana (jinhe magar bana diya gaya tha)

🔶 6. Krishna–Arjun ki kathayen

Arjuna aur Krishna ka Prabhasa me milna

Subhadra Haran – Krishna ke salah par Arjun dwara

Indraprastha wapas aana, Subhadra ka dower (dahej) lena

Subhadra ke garbh me Abhimanyu ka prakat hona

Draupadi ke bachchon ka janma

Krishna–Arjun ka Yamuna kinare par yatra

Arjun ko Gandiva dhanush aur Krishna ko Sudarshan chakra milna

Khandava van ka dahana (Agni ko santusht karna)

Maya asur ki raksha aur uska assembly hall banana

Mandapala rishi ka Sarngi panchi se putra paana

📘 Adi Parva ka Aakhri Varnan

Adi parva Vyasa ne 227 adhyay me baanta hai.

Total shlokas: 8,884

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.4"):
                text1 = """
Sabha Parva Mahabharata ka dusra aur bahut hi vistrit parva hai. Isme Pandavon ki rajya-vistar ki yatra, Jarasandha ka vadha, Rajasuya yagya, Shishupala ka nash, aur aakhir me dice-game ki poori tragedy shamil hai.

Yeh poora Parva matra-vishay (rich with content) mana gaya hai.

🔶 Sabha Parva ke Mukhya Vishay
1. Maya-dwara banayi gayi Pandavon ki Maha Sabha

Pandav apne rajya Indraprastha me ek bhavya sabha (assembly hall) banwate hain.

Maya Danava is adbhut sabha ka nirmaan karta hai.

Is hall me illusion, architecture aur divya shilp kala ka pradarshan hota hai.

2. Retainers aur citizens ki review

Pandav apne praja, sevakon, sainikon aur adhikaarion ka samiksha (review) karte hain.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.4.jpg", text1,   layout="side", image_position="left")

                text2 = """
3. Narada ka aagaman

Narada Muni aate hain.

Wo lokapalon (Guardians of the world: Indra, Varuna, Yama, Kubera) ka varnan karte hain.

Swarglok aur dev-lok ki sabhaon ka bhi vivaran dete hain.

4. Rajasuya Yagya ki taiyyari

Yudhishthira ko Raja-bhoj banne ki iccha hoti hai.

Rajasuya Yagya ke liye sabse pehle:

Dusht rajaon ko jeetna hota hai.

Apne prabhav ka pradarshan karna hota hai.

5. Jarasandha ka vadha

Jarasandha Rajasuya yagya ka sabse bada badhak tha.

Arjuna, Bhima aur Krishna use malla-yuddh me harate hain.

Bhima usko beech se faad kar maar daalta hai.

6. Bandikrit rajaon ki mukti

Jarasandha ne jo rajaon ko pahadon me kaid kiya tha,

Krishna un sab ka rajmukuti (crown) vaapas karta hai

Aur unki mukti karata hai.

7. Pandavon ka digvijaya (world conquest)

Pandav alag-alag dishaon me jaakar:

Poorv, paschim, dakshin, uttar sab jagah rath yatra chalate hain

Aur rajao ko apna adhikar sweekar karne par majboor karte hain.

Iska uddeshya Rajasuya ke liye tributaries banana tha.

8. Rajasuya Yagya me rajaon ka aagaman

Sabhi jeete hue raja aur desh apne uphaar, kar/tribute lekar Indraprastha pahuchte hain.

Yagya badhi shaan se aayojit hota hai.

9. Shishupala ka nash

Arghya ka sammaan Krishna ko diya jata hai.

Shishupala isse gussa ho kar Krishna ki ninda karta hai.

Krishna uske 100 galtiyon ki seema poori hone par usse Sudarshan Chakra se maar daalta hai.

10. Bhima dwara Duryodhana ka upahasan

Yagya pura hone ke baad sab sabha me milte hain.

Bhima Duryodhana ka mazaak udata hai (specially Maya Sabha ke illusions ke karan).

Duryodhana gir padta hai, log haste hain.

11. Duryodhana ka irsha aur dukh

Duryodhana Pandavon ki shaan aur unki sabha dekhkar jalta hai.

Wo sochta hai ki Pandav hamesha usse badhkar hi rahenge.

12. Dice-game ki taiyyari

Duryodhana aur Shakuni milkar juye ki yojna banate hain.

Dhritarashtra kuch nahi rokta.

13. Yudhishthira ka Shakuni se paraajay

Shakuni apni chaal se Yudhishthira ko ek ek daav me haraata hai.

Yudhishthira haar kar:

Apna rajya

Apne bhai

Khud ko

Aur aakhir me Draupadi ko bhi haara deta hai.

14. Draupadi ka apmaan aur uski raksha

Sabha me Draupadi ka anachaar sab hone wala hota hai.

Draupadi sabko dharm ki yaad dilati hai.

Dhritarashtra draupadi ko bachata hai, aur use boons dekar wapas bhej deta hai.

15. Duryodhana phir se dice-game ke liye uksata hai

Duryodhana phir se Yudhishthira ko bulwata hai.

Dusra dice-game hota hai.

Fir Yudhishthira haar jaata hai.

16. Pandavon ka vanvas

Yudhishthira aur sab Pandav 12 saal ka vanvas aur

13va saal ajnatvas (incognito exile) me jaane ke liye majboor ho jaate hain.

📘 Sabha Parva ki Sankhya

Kul sections (adhyay): 78

Kul shlokas: 2,507

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.5"):
                text1 = """
(Mahabharata ka 3rd Parva, 269 sections, 11,664 shlokas)

Aranyaka Parva Pandavon ke 12 saal ke vanvaas ka poora itihas batata hai — unke dukh, tapasya, divine meetings, battles, legends, aur pilgrimages ka vishal sangrah.

Yeh Parva Mahabharata me sabse bada, sabse kahani-sampann aur sabse divya maana jata hai.

🔶 1. Pandavon ka vanvas ki taraf prasthaan

Yudhishthira van ki aur badte hain.

Praja unke peeche-peeche aati hai.

Dhaumya ke updesh ke anusaar Yudhishthira Surya dev ki stuti karte hain.

Surya unhe Akshaya Patra deta hai → jisse Brahmanon ko anant bhojan mil sake.

🔶 2. Vidura ka nikaala & wapas bulaana

Dhritarashtra Vidura ko nikal deta hai (kyunki Vidura sach bolta hai).

Vidura Pandavon ke paas aata hai.

Phir Dhritarashtra usse fir se bula leta hai, Vidura laut jaata hai.

🔶 3. Duryodhana ki saazishen

Duryodhana aur Karna milkar Pandavon ko jungle me maarne ki yojna banate hain.

Tab Vyasa prakatt hote hain, aur Duryodhana ko rok dete hain.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.5.jpg", text1,   layout="side", image_position="left")

                text2 = """
🔶 4. Surabhi ka prasang & Maitreya ki shraap

Surabhi ki purani katha.

Rishi Maitreya aate hain, Dhritarashtra ko samjhate hain.

Duryodhana ko shraap dete hain: “Teri jangha bhima se pitegi.”

🔶 5. Bhima vs Kirmira

Bhima rakshas Kirmira ko mar deta hai — ye rakshas Vaka ka bhai tha.

🔶 6. Krishna, Vrishni aur Panchal rajkumar

Pandavon ki haar ki khabar sunkar Krishna, Panchal and Vrishni log aate hain.

Draupadi Krishna ko apna dukh batati hai.

Krishna use sambhalta hai.

🔶 7. Sauva ka vadha

Krishna dwara Shalva (Sauva) ka nash ka varnan.

🔶 8. Subhadra & Draupadi ke putron ka sambandh

Krishna Subhadra aur Abhimanyu ko Dwaraka le jaata hai.

Dhrishtadyumna Draupadi ke putron ko Panchal lai jaata hai.

🔶 9. Pandav Dvaita van me

Yudhishthira, Bhima aur Draupadi ki beech gahari baatein.

Vyasa unhe Pratismriti (divya smaran shakti) ka vardaan dete hain.

Pandav Kamyaka van ki taraf badh jaate hain.

🔶 10. Arjuna ka divya-shastron ki khoj me tapasya

Arjuna weapons lane nikal padta hai.

Arjuna vs Mahadeva (hunter disguise) — Pashupata Astra prapt hota hai.

Lokpals se divya astra milte hain.

Arjuna Indra lok jata hai shastron ke liye.

Dhritarashtra ise sun kar chintit hota hai.

🔶 11. Yudhishthira ka dukh & Nala-Damayanti ki katha

Yudhishthira Brihadasva rishi se milte hain.

Rishi unhe Nala-Damayanti ki kahani suna kar dhairya dete hain.

Yudhishthira dice ka rahasya seekhta hai.

🔶 12. Rishi Lomasha ka aagaman

Pandavon ko Arjuna ki khabar deta hai.

Lomasha unhe teerth-yatra par le jate hain.

🔶 13. Pandavon ki Teerth-yatra

Bahut saare pavitra sthal: Gaya, Putasta, Pushkara, tatha anek teerth.

Indra dwara Karna ke kundal aur kavach ka le lena.

Agastya aur Vatapi ki katha

Rishyasringa ki kahani

Parashurama ka itihas (Kartavirya ka vadha)

🔶 14. Pandav–Vrishni milan at Prabhasa

Pandav Vrishni clan se milte hain.

🔶 15. Sukanya–Cyavana ki katha

Cyavana rishi ne Ashvin devtaon ko Soma pilaaya.

Cyavana ko youth (jawani) ka vardaan.

🔶 16. Mandhata, Jantu, Somaka ki katha

King Somaka apne eklaute putra Jantu ka balidaan karta hai → 100 putra milte hain.

Hawks & pigeon ki katha

King Sivi ki pariksha

Ashtavakra vs Vandi debate

🔶 17. Yavakrita & Raivya ki kahani

Gyaan ke liye tapasya aur shraap ki kathayein.

🔶 18. Gandhamadana ki yatra

Pandav Narayana ashram jate hain.

Draupadi ke liye Bhima gandhamadana pahad se saugandhika phool lene nikalta hai.

🔶 19. Bhima vs Hanuman

Bhima Hanuman se milta hai.

Hanuman apne bhai ko strength aur humility ka path sikhaata hai.

🔶 20. Yakshas, Rakshasas, Jata rakshas ka vadha

Bhima Yaksha aur Rakshas se ladta hai.

Jata rakshas ko maar deta hai.

🔶 21. Pandavon ka Kubera se milna

Pandav Kuvera se milte hain.

Phir Arjuna se punar milan hota hai.

🔶 22. Arjuna vs Nivatakavachas & Paulomas & Kalakeyas

Arjuna un sab asura senaon ka nash karta hai.

Celestial weapons ka pradarshan — Narada rok dete hain.

🔶 23. Bhima aur bada Sarpa

Bhima ek maha-nag ke jaal me phans jata hai.

Yudhishthira prashnon ka sahi uttar dekar usse chhudaate hain.

🔶 24. Pandav Kamyaka van wapas

Krishna unse milne aate hain.

Markandeya aate hain aur anek purani kathayein sunate hain:

Prithu

Saraswati

Matsya

Dhundhumara

Chaste wife story

🔶 25. Pandav Dvaita van me punah

Calf-seeing procession

Duryodhana pakda jaata hai, Arjuna use chhudaata hai.

🔶 26. Yudhishthira ka Mriga-swapna

Deer, omens aur warnings ka swapna.

🔶 27. Jayadratha dwara Draupadi ka apaharan

Jayadratha Draupadi ko chura leta hai.

Bhima uska peecha karta hai → use harata hai → sirf shaving punishment deta hai.

🔶 28. Rama–Ravana Yudh ki kahani

Parashurama nahi — Maryada Purushottam Ram (Sri Ram) ka Ravan vadh yahan bataya jaata hai.

🔶 29. Savitri–Satyavan ki story

Savitri ka adbhut pativrata-bala ka katha.

🔶 30. Karna ka kundal-kavach

Indra Karna ka kundal & kavach maang kar le leta hai.

Uske badle ek Shakti astra deta hai—jo ek baar me ek hi vyakti ko maar sakta hai.

🔶 31. Dharma ka Updesh

Yudhishthira ko Dharamraj ka gyaan.

Pandav paschim disha ki taraf badhte hain.

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.6"):
                text1 = """
(Mahabharata ka 4th Parva – 67 sections, 2050 shlokas)

Virata Parva me Pandavon ke agyatvaas ke ek saal ka poora varnan diya gaya hai—unke roop badal kar Virata nagari me rahna, unke parichay chhupaana, aur unke lihaz se hue bade sangram.

🔶 1. Pandavon ka Virata nagari me pravesh

Pandav Virata desh pahunchte hain.

Nagar ke bahar smashaan ke paas unhe ek bada Shami vriksha milta hai.

Usi ke upar wo apne sab divya astr-shastra chhupa dete hain.

Yahi se unka Agyat Vas ka yeh antim saal shuru hota hai.

Pandavon ke disguise:

Yudhishthira → Kanka (raj-purohit & dice expert)

Bhima → Ballava (bawarchi & pahalwan)

Arjuna → Brihannala (eunuch dance/music teacher)

Nakula → Granthika (ashva-paalak)

Sahadeva → Tantipala (gau-paalak)

Draupadi → Sairandhri (queen Sudeshna ki dasi)
        """
                create_image_text_layout("attached_assets/chapter1/1.2.6.jpg", text1,   layout="side", image_position="left")

                text2 = """
🔶 2. Kichaka ki durachar aur Bhima dwara vadha

Kichaka, Virata ka senapati, Draupadi par kaamuk drishti rakhta hai.

Draupadi ka apmaan karta hai.

Draupadi Bhima se madad mangti hai.

Bhima raat me ek bhayanak yuddh me usse maar daalta hai.

Kichaka ka vadha Virata parva ka ek most dramatic event hai.

🔶 3. Duryodhana ke jasus (spies)

Duryodhana ko shak hota hai ki Pandav kisi rajya me chhupe hain.

Woh har disha me jasus bhejta hai.

Bahut khoj ke baad bhi koi Pandav ko pehchan nahi paata.

🔶 4. Trigarta dwara Virata ki gaayon ka pehla apaharan

Trigarta (Susharma) raj Virata ki gaayein chura leta hai.

Bhima unka bhayankar yudh me vinaash karta hai.

Virata raja ko bhi bandi banaya jata hai, Bhima use bachata hai.

Virata ki gaayein wapas laayi jaati hain.

🔶 5. Kauravas dwara Virata ki gaayon ka doosra apaharan

Pandavon ke agyatvas ke antim dinon me
Duryodhana + Bhishma + Drona + Karna + sabhi Maharathee
saath milkar Virata ke gau-dhan ko loot lete hain.

Arjuna ko Brihannala roop se bahar aana padta hai.

🔶 6. Arjuna ka eklauta vijay—Kuruvon ki paraajay

Arjuna Shami vriksha se astra nikalta hai.

Brihannala roop chhodkar asli roop dharan karta hai.

Eklauta Arjuna sabhi Kaurav senapatiyon ko yuddh me dhool chataata hai:

Bhishma

Drona

Karna

Kripa

Duryodhana

Ashwatthama

Dusasana

Susharma

Aur poori Kaurav sena

Gayein wapas Virata ko mil jaati hain.

Yudh hote-hote Agyat Vas ka antim din complete ho jaata hai.

🔶 7. Uttara–Uttaraa & Abhimanyu ka sambandh

Virata ki putri Uttara Arjuna ki shishya hoti hai (dance/music).

Par Arjuna kehte hain:
“Main to uska guru hoon, ise uske yogya pati ko do.”

Arjuna → Uttara ki shaadi Abhimanyu (Arjuna–Subhadra ke bete) se karwa deta hai.

Virata aur Drupada milkar Pandavon ko welcome karte hain.

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.7"):
                text1 = """
(Mahabharata ka 5th Parva — 186 sections, 6698 shlokas)

Theme: Peace vs. War negotiations

🔶 1. Pandavas in Upaplavya

Pandava log Upaplavya naam ki jagah reh rahe the aur yudh ki tayari kar rahe the.

Isi samay Duryodhana aur Arjuna, dono ek hi waqt Shri Krishna ke paas jaate hain aur kehte hain:

“Krishna, humein yudh me madad chahiye.”

🔶 2. Krishna ka prashn

Krishna muskurate hue kehte hain:

“Main do cheezein de sakta hoon:

Ek poori Akshauhini sena

Main khud – par bina ladhe (non-fighting counsellor)

Batao kisey kya chahiye?”

Duryodhana ka galat faisla

Duryodhana ko lagta hai zyada sena = jeet,
to woh sena maang leta hai.

Arjuna ka gyaan

Arjuna kehta hai:
“Humein aap chahiye, Krishna – bina ladhe bhi aap hi hamari shakti hain.”

Yahaan se dono pakshon ka bhavishya tay ho jaata hai.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.7.jpg", text1,   layout="side", image_position="left")

                text2 = """
🔶 3. Shalya ka vishesh kissa

Shalya, Madra ka raja, Pandavon ka supporter tha.
Par Duryodhana ne bahut mehmaan-nawaazi aur uphaaron se usse phusla liya.

Shalya ne anjaane me Duryodhana ko var (boon) de diya.
Var maangte hi Duryodhana ne kaha:

“Yudh me tum mere paksh me ladoge.”

Shalya majboori me maan jaata hai,
par Pandavon ko milkar Indra–Vritra ki kahani sunaakar unhe sambhalta hai.

🔶 4. Pandavon ka Purohit – Shaanti sandesh

Pandav apna purohit Kauravon ke paas bhejte hain.
Wahaan Dhritarashtra shaanti ki baat karta dikhta hai.

🔶 5. Dhritarashtra ki chinta aur anidra

Raat bhar Dhritarashtra ko neend nahi aati.
Useh darr hai:

Pandav shaktishaali ho chuke hain

Krishna unke saath hai

Bhishma–Drona bhi yudh ko lekar pareshan hain

Vidura ka Upadesh

Vidura unhe gyaan aur dharma ki baatein samjhate hain.

Sanatsujata ka Darshan

Phir Sanat-sujata Rishi aate hain aur
Atma–tattva (spiritual truth) ka gyaan dete hain.

🔶 6. Krishna ka Hastinapura ke liye Shaanti Doot-bana

Agli subah Sanjaya sabko batata hai:
“Arjuna aur Krishna ek hi tattva ke do roop hain.”

Krishna swayam Shaanti ke liye Hastinapura jaane ka nirnay lete hain.

🔶 7. Duryodhana ka Krishna-dutv ka apmaan

Hastinapura pahunch kar Krishna kehte hain:

“Pandav sirf apna adhikar maang rahe hain. Shaanti karo.”

Duryodhana ka ghamand

Duryodhana kehta hai:

“Main ek suichi ki nok jitni zameen bhi nahi doonga.”

Woh to Krishna ko bandi banane ka bhi prayas karta hai!

Krishna ka divya roop

Tab Krishna sabke saamne apna Vishvaroop dikha dete hain.
Sab raja dar jaate hain – Duryodhana ko chhodkar.

🔶 8. Krishna aur Karna ki gupt baat

Krishna Karna ko rath par bitha kar kehte hain:

“Tum Kunti-putra ho. Pandavon ke bhai ho. Unki taraf aa jao.”

Par Karna kehti hai:

“Main Duryodhana ka bhojan-kritagya hoon. Main uska paksh nahi chhod sakta.”

Karna garv aur wafadari se Krishna ka upadesh thukra deta hai.

🔶 9. Krishna ka wapas Pandavon ke paas aana

Krishna Upaplavya laut kar Pandavon ko sab kuch batate hain:

Duryodhana ki zidd

Shaanti ka asvikaar

Vishvaroop ka darshan

Karna ka sach (Kunti-putra)

Pandav samajh jaate hain — ab yudh anivaarya hai.

🔶 10. Senayon ki taiyaari

Hastinapura se:

Rathi, atirathi, gajak, rath, ghode, paida-sena
sab yudh ke liye chal padte hain.

Dono paksh apne-apne anubhavi yoddha list karte hain.

🔶 11. Uluka – Duryodhana ka dut

Yudh se ek din pehle Duryodhana Uluka ko Pandavon ke paas bhejta hai,
jo uttajit-shabdon me unhe lalkar kar aata hai.

🔶 12. Amba ki kahani

Yudh se pehle ek mahatvapurn kahani batayi jaati hai:

Amba ki dukhbhari katha

Bhishma ke viruddh uska tapasya

Bhishma-vadha ka beej

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.8"):
                text1 = """
“Bhishma ke adheen 10 din ka yudh”
⭐ Major Highlights:
1. Jambu-dweep ki rachna ka varnan

Sanjaya Dhritarashtra ko Jambu region (Jambu-dweep) ki utpatti batata hai.
Ye ek cosmic geography explanation hota hai.

2. Pandava sena ka manobal girna

Yudh ke pehle kuch din Yudhishthira ki sena bahut nuksaan uthati hai.
Bhishma devastate kar rahe hote hain.

3. Arjuna ka moral dilemma (Gita moment)

Arjuna apne rishtedaron ko maarne ka soch kar dukh aur daya se bhar jaata hai.

Krishna unhe Moksha-dharma, Atma-gyan, karma-yoga, sankhya,
yaani Bhagavad Gita ke tattva samjhate hain
aur Arjuna ko fir se yudh ke liye taiyar karte hain.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.8.jpg", text1,   layout="side", image_position="left")

                text2 = """
4. Krishna ka rath se kudkar Bhishma par toot padna

Bhishma se hone wale bhayankar nuksaan ko dekh kar
Krishna apni maryada todne hi wale hote hain.

Woh rath se kud kar, haath me koish (whip) lekar
Bhishma ko maarne ke liye bhagte hain.

Arjuna Krishna ko rok leta hai.
Ye yudh ke sabse dramatic palon me se ek.

5. Arjuna dwara Bhishma-vadha (Shikhandi ke saamne rakhkar)

Arjuna Shikhandi ko shield banata hai,
kyunki Bhishma ne uspar astra na chalaane ka vow liya tha.

Arjuna teer pe teer barsata hai
aur Bhishma rath se gir kar shar-shayya (bed of arrows) par lete hain.

Bhisma Parva ends

Bhishma bed of arrows par soye rehte hain, aur parva yahan samaapt hota hai.

⚔️ 7th Parva – Drona Parva (170 sections, 8909 shlokas)
“Dronacharya as Commander – Abhimanyu’s death – Jayadratha-vadha – Ghatotkacha-vadha”
⭐ Major Events:
1. Dronacharya ka Commander-in-Chief banna

Bhishma ke girne ke baad, Kaurav sena ka senapati Drona banta hai.

2. Drona ka pratigya – Yudhishthira ko pakadne ka sankalp

Duryodhana ke kehne par Drona vow leta hai:
“I will capture Yudhishthira alive.”

3. Arjuna ko Sansaptakon se door rakhna

Kaurav yeh ensure karte hain ki Arjuna ko Sansaptakas (suicide squad) door le jaaye,
taaki woh Yudhishthira ki raksha na kar sake.

Arjuna kuch samay yudh-bhoomi se door bhaagta hua dikhta hai
(yeh retreat strategy ka part tha).

4. Bhagadatta aur uska hathi Supratika ka death

Arjuna Bhagadatta aur uske powerful hathi Supratika ko maarkar gira deta hai.

5. 🎯 Abhimanyu-vadha (tragic highlight)

Arjuna ke bina, Kaurav log Chakravyuha banate hain.

16-year-old Abhimanyu andar ghus to jaata hai, lekin
uske saath adharma hota hai—
kaafi Maharathis milkar usse ghair kar maar dete hain.

Isme Jayadratha ka special role tha—
wah kisi ko vee vyuha me ghusne hi nahi deta.

6. Arjuna ka pratigya – “Jayadratha ko suryast se pehle maarunga”

Abhimanyu ke mrityu ke baad, Arjuna 7 Akshauhini sena ko tod deta hai
aur Jayadratha ko bhi maar daalta hai.

7. Bhima + Satyaki का Kaurava-camp me ghusna

Yudhishthira ke aadesh par
Bhima aur Satyaki Kaurav camp me ghus kar
Sansaptakon ke bache-khuchon ko mita dete hain.

8. Bahut saare Maharathis ki maut

Alambusha

Srutayus

Jalasandha

Somadatta

Virata

Drupada

Ghatotkacha

etc.

9. Asvatthaman ka Narayana-astra

Drona ke marne ke baad
Asvatthaman Narayana-astra chodta hai—
jo saab ko jala kar maar sakta tha.
Pandav apne astra neeche rakhkar bachte hain.

10. Rudra ka mahima – Tripura-dahana ki kahani

Yahan Shiva/Rudra ka bhi mahima-vrittant aata hai.

⚔️ 8th Parva – Karna Parva (69 sections, 4964 shlokas)
“Karna as Commander – Bhima’s vow – Karna-vadha”
⭐ Major Highlights:
1. Karna as Commander + Shalya as charioteer

Shalya ko Karna ka saarathi banaya jaata hai
(lekin woh mann se Karna ko demoralise karta rehta hai).

2. Tripura-asura ki kahani ka punarvartan

Isme Shiva dwara Tripura-nagari ki vinash-leela batayi jati hai.

3. Karna & Shalya ke beech kadve vaaky

Dono ek-doosre ko stork-crow (hans-kauwa) waali kahani suna-suna kar
beizzat karte rehte hain.

4. Asvatthaman kills Pandya

Pandya raja ko Asvatthaman maar deta hai.
Dandasena aur Darda jaise warriors bhi girte hain.

5. Yudhishthira–Karna duel

Yudhishthira Karna se bahut khatarnak situaton me bachkar nikalta hai.

6. Arjuna–Yudhishthira ka jhagda

Arjuna gussa ho jaata hai ke Yudhishthira ne use pathoos bola,
par Krishna Arjuna ko shant karte hain.

7. 🩸 Bhima drinks Dussasana’s blood (his vow fulfilled)

Bhima apni pratigya poori karta hai:

Dussasana ko yudh me maar kar

uska rakt peeta hai (symbolic, krodh-pratik).

8. ⚔️ Arjuna kills Karna (Karna-vadha)

Aakhri ekal yudh hota hai:

Karna ka rath ka pahiya kichad me fas jata hai

Karna astra nahi chala pata

Krishna Arjuna ko opportunity batate hain

Arjuna Anjalika-astra se Karna ko maar deta hai

Karna Parva yahin samapt hota hai.

        """
                create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.2.9"):
                text1 = """
Parva 9 – Shalya Parva

Yudhishthira aur Duryodhana ki sena ke beech yudh almost khatam ho chuka tha.
Zyada tar mahan yoddha mar chuke the.

Is stage par Shalya, jo Madra ka raja tha, Kaurava sena ka naya senapati bana.

Phir kai rath-yoddha ek-ke-baad-ek takraate rahe.
Ant mein Yudhishthira ne Shalya ko maar diya.

Saath hi Sahadeva ne Shakuni ko bhi yudh mein maara.
Ab Kaurav sena bahut kam bach gayi thi.

Duryodhana, sharminda aur thaka hua, ek talab (lake) mein chhup gaya.
Fowlers (jungle ke shikari log) ne yeh baat Bhima ko bata di.

Phir, Yudhishthira ke kathor shabdon se chidh kar,
Duryodhana paani se bahar aa gaya.

Tab hua sabse bhayank yudh –
mace fight (gada yudh) Bhima aur Duryodhana ke beech.

Balarama bhi wahan pahuncha aur dono ko dekhta raha.
Lambe yudh ke baad Bhima ne Duryodhana ki jango (thighs) tod di.

Iss tarah Parva 9 samapt hota hai.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.9.jpg", text1,   layout="side", image_position="left")

                text2 = """
Parva 10 – Sauptika Parva (Night Massacre)

Raat ka samay tha. Yudhishthira aur Pandav apni camp mein aaram kar rahe the.

Tab Ashwatthama, Kripa aur Kritavarma battlefield par aaye aur
Duryodhana ko zameen par pada dekha – khoon se latpat aur jangon se viklang.

Apne pita Drona ki mrityu yaad kar ke,
Ashwatthama gusse se bhar gaya.
Usne sankalp liya:
“Main Panchalon aur Pandavon ko raat ko sote-sote maar daalunga.”

Raat ko woh camp ki taraf chala.
Dwaar par ek Rudra ke roop wala rakshas (demon) khada tha.
Ashwatthama ne Rudra (Shiva) ki puja ki aur uske baad andar ghus gaya.

Phir usne Dhrishtadyumna,
Draupadi ke paanch putron,
aur Panchalon ko
neend mein hi maar diya.

Sirf 5 Pandav aur Satyaki bache — kyunki Krishna ne pehle hi unhe surakshit jagah bhej diya tha.

Subah, jab yeh khabar mili,
Draupadi dukh se toot gayi.
Usne upvas karke marne ka sankalp liya.

Bhima, Draupadi ke aansu dekh kar,
Ashwatthama ka peechha karne nikal pada.

Ashwatthama ne ek celestial weapon (divya astra) chhod diya,
jo sab Pandavon ko maar sakta tha.
Par Krishna ne rok diya: “Yeh nahi hoga.”

Arjun ne apne astra se us astra ko neutralize kiya.

Gussa ho kar, Krishna aur Vyasa ne Ashwatthama ko shraap (curse) diya.
Pandavon ne uske sir par ka chamakta hua mani (jewel) bhi cheen liya
aur Draupadi ko diya.

Iss tarah raat ka yeh bhootal (terrifying) parva khatam hota hai.

Parva 11 – Stri Parva (Women’s Lament)

Yudh ke baad, Dhritarashtra apne putron ki mrityu se toot gaya tha.
Uska dukh aur gussa itna zyada tha ki
jab usne socha ki Bhima uske saamne khada hai,
toh usne gusse mein ek loh ke putle (iron statue) ko tod diya.
Krishna ne hi Bhima ke jagah woh putla rakh diya tha.

Vidura ne Dhritarashtra ko vairagya (detachment) aur dharma ka gyaan diya
aur uska dukh shant kiya.

Phir Dhritarashtra, Gandhari aur raj gharane ki stree log
battlefield par gaye.
Wahan unhone apne pati, putron aur bhaiyon ki laashen dekhi
aur unke roop mein dard bhari vilap shuru hui.

Gandhari ka gussa bhi utra nahi tha,
par Krishna ne use shant kiya.

Uske baad Yudhishthira ne saare rajaon ki antimsanskaar (funeral rites) kiye.

Yehi Parva batata hai kaise Kunti ne sabke saamne sach bataya
ki Karna uska pehla beta tha.

Yeh parva bahut dukhad aur hriday-vidaarak (heart-breaking) mana gaya hai.

Parva 12 – Shanti Parva

Is parva mein Yudhishthira dukh se toot chuka tha.
Use lagta tha ki sab uski wajah se hua —
his own relatives, uncles, brothers, bete, sab mar gaye.

Tab Bhishma, jo abhi bhi bano ke shaiya (bed of arrows) par lete the,
ne Yudhishthira ko raajdharma, apaddharma (emergency duty),
aur moksha-marg ka gyaan diya.

Is parva mein Bhishma ne bahut gehra aur buddhi-bhara updesh diya,
jo rajao ke liye ek shastra (scripture/manual) jaisa mana jata hai.

Yeh parva gyaan aur shanti ka pratik hai —
isliye iska naam Shanti Parva hai.
        """
                create_image_text_layout(text_content=text2, layout="full")
 
        with st.expander("Section 1.2.10"):
                text1 = """
⭐ Parva 13 – Anushasana Parva

(Duties, Charity, Truth)

Yudhishthira abhi bhi yudh ke baad dukh aur paap-bodh me tha.
Tab Bhishma, jo abhi bhi apne banon ke shaiya (bed of arrows) par lete the,
ne use dharma ka gyaan diya.

Is parva me bataya gaya hai:

Dharma (righteous duty) aur Artha (right livelihood) ke niyam

Daan (charity) ke rules aur uska phal

Kaun patra (worthy) hota hai daan lene ke liye

Satya (truth) ki shresthta

Brahmano aur gau-mata ke mahatva

Kis samay kaunsa duty uchit hota hai — time-place ke hisaab se dharma

Ant me, Bhishma swarg lok ko chale jate hain.
Yeh parva batata hai ki ek manushya ko jeevan me kaise rehna chahiye.
        """
                create_image_text_layout("attached_assets/chapter1/1.2.10.jpg", text1,   layout="side", image_position="left")

                text2 = """
🐎 Parva 14 – Ashwamedhika Parva

(Horse Sacrifice & Arjuna’s Journeys)

Is parva ka main kendra hai Ashwamedha yajna (horse sacrifice)
jo Yudhishthira karta hai shanti ke liye.

Isme bataya gaya hai:

Samvarta aur Marutta ki purani katha

Pandavon ko sone ke khazane milna

Parikshit ka janm, jise Krishna ne bachaya tha
jab Ashwatthama ke astra ne use garbh me jala diya tha

Arjuna ka alag-alag rajao se yudh,
jab woh yajna ka ghoda le kar bhraman karta hai

Arjuna ka apne hi bete Vabhruvahana ke saath mushkil yudh

Ek mongoose (nevla) ki katha jo sikhati hai ki
“dharma ka asli maap dhan se nahi, bhavna se hota hai”

Yeh parva adhbhut aur gyaan se bharpur maana jata hai.

🌿 Parva 15 – Ashramavasika Parva

(Dhritarashtra’s Final Departure)

Dhritarashtra, Gandhari aur Vidura raja-mahal chhodkar
van (forest) me vanaprastha jeevan ke liye chale jate hain.
Kunti bhi unke saath chal deti hai.

Vyasa apni shakti se Dhritarashtra ko
uske mare hue putron aur parivaar se milwata hai.
Yeh milan bahut hi adbhut (miraculous) hai.

Is parva me:

Dhritarashtra aur Gandhari dukh se mukta hote hain

Vidura apni saari tapasya (penance) ke baad moksha pa leta hai

Sanjaya bhi shanti ko prapt hota hai

Narada batata hai ki Vrishni vansh (Krishna ka kul) samapt ho chuka hai

Yeh parva shanti aur tyag ka pratik hai.

⚡ Parva 16 – Mausala Parva

(The End of the Yadava Clan)

Yeh parva bahut dardnaak hai.

Ek brahmana ke shraap (curse) ke kaaran
Yadava vansh ke log ek din nasha me bigad jaate hain
aur Eraka grass (jo unke haath me vajra jaise ban gaya) se
ek-dusre ko maar daalte hain.

Krishna aur Balarama bhi apne anta (final time) ko prapt hote hain—
samay aur prakriti ke niyam sab par lagu hote hain.

Arjuna Dwaraka pahuch kar
suna-shahar aur mare hue Vrishni yoddhaon ko dekh kar
gehra dukh mehsoos karta hai.

Woh Krishna, Balarama aur sab Vrishnio ka antimsanskar karta hai.

Fir jab Arjuna Yadava striyon aur bachchon ko lekar aa raha tha,
uska Gandiva uska saath nahi deta—
divya astron ka samay samaapt ho chuka tha.

Vyasa ke salah par Arjuna
sannyasa (renounced life) lene ka sochta hai.

🏔 Parva 17 – Mahaprasthanika Parva

(The Last Journey)

Pandav apna rajya chhod dete hain
aur Mahaprasthana (great journey) par nikal padte hain
Himalaya ki taraf, swarg ke dwar tak.

Raste me:

Pehle Draupadi girti hai

Phir Sahadeva, Nakula, Arjuna, Bhima

Sab apne-apne ahankar (ego) ya truti (fault) karan girte hain

Sirf Yudhishthira aage badhta hai—
wo kabhi peeche mudkar nahi dekhta.

Agni ko Arjuna apna Gandiva wapas de deta hai.
Yeh unke yudh-kale ke samapan ka pratik hai.

🌈 Parva 18 – Swarga Parva

(Heaven & Truth)

Yudhishthira ke liye devdoot ki vimaan aati hai.
Par uska ek kutta saath chal raha tha.

Devdoot kehte hain: “Kutte ko chhodo.”
Par Yudhishthira mana kar deta hai:
“Maine ise nahi chhoda, main ise ab bhi nahi chhodunga.”

Tab woh kutta apna asli roop dikhata hai—
woh Dharma devata tha, Yudhishthira ka pita.

Swarg me Yudhishthira ko pehle narak (hell) dikhaya jata hai
taaki woh apne bhaiyon ka dukh mehsoos kare.

Baad me sab kuch sapasht hota hai—
Indra aur Dharma usse uska asli swarg dikhate hain
jahan woh devtaon ke saath anand se rehta hai.

🌺 Parva-Sangraha Ki Samapti

Sauti kahte hain:

Mahabharat teen lokon ka gyaan samete hai

Jo isse nahi jaanta, wo adhura vidwaan hai

Is kathaa ko sunne se paap dho jaate hain

Bharata sab granthon ka saar hai

Jis tarah samudra jahazon se paar hota hai,
waise hi Mahabharat ko samajhna Parva-Sangraha se aasaan hota hai

        """
                create_image_text_layout(text_content=text2, layout="full")
 
    # Chapter1
    with st.expander("Chapter 1.3 – Paushya Parva"):        
        with st.expander("Section 1.3.1"):
                    text1 = """
🐕 Sarama ka Shraap

Kurukshetra me Raja Janamejaya apne teen bhaiyon—Srutasena, Ugrasena, Bhimasena—ke saath lambe yagna (long sacrifice) me baithe the.

Tab ek Sarama (swargiya dog) ka bachcha wahan aa gaya.
Janamejaya ke bhaiyon ne bina wajah usse maar diya.
Woh rota-rotā apni maa ke paas bhaaga.

Sarama ne pucha:

“Kisne maara? Galti kya ki?”

Bachcha bola:

“Maine kuch nahi kiya!
Na maine ghee chhua, na ghee ko dekha.”

Yeh sun kar Sarama gusse me Janamejaya ke paas gayi aur boli:

“Mere bete ne koi galti nahi ki.
Phir kyun mara?
Iska phal tum bhugatoge—jab bilkul ummeed nahi hogi.”

Janamejaya darr gaya.
Yagna ke baad woh Hastinapura laut gaya aur shraap se chutkaara dhoondne laga.
            """
                    create_image_text_layout("attached_assets/chapter1/1.3.1.jpg", text1,   layout="side", image_position="left")

                    text2 = """
👨‍🦳 Raja ka Purohit ki Talaash

Ek din shikar par, Janamejaya ne ek rishi-ashram dekha.
Us rishi ka naam tha Srutasrava.
Uska beta tha Somasrava, ek kathor tapasvi (ascetic).

Raja ne kaha:

“Rishi ji, mujhe aapka beta Purohit banane dijiye.”

Rishi bole:

“Mera beta Somasrava ek naag-maata (she-snake) se janma hai.
Bahut shaktishali hai.
Sab paap mita sakta hai—bas Mahadeva ke viruddh jo paap kiya ho, woh nahi.”

Phir rishi ne ek baat aur batayi:

“Uski ek aadat buri hai—
Woh kisi bhi Brahmana ko, jo maange, de deta hai.
Agar tum ye bardasht kar sakte ho, tab hi usse le jao.”

Janamejaya ne haan kar di.
Use Purohit banakar wapas rajya gaya aur bhaiyon se kaha:

“Jo Somasrava kahe—tum bina sawaal maane.”

🧘‍♂️ Rishi Dhaumya aur Aruni ki Guru-bhakti

Iske baad kahani me doosra Rishi aate hain—
Ayoda-Dhaumya.

Unke teen shishya:
➡ Aruni
➡ Upamanyu
➡ Veda

Ek din Dhaumya ne Aruni se kaha:

“Khet ki pani ki naali tut gayi hai.
Jao aur usse bandh do.”

Aruni gaya, par koi bhi tarika kaam nahi kar raha tha.
Ant me usne socha:

“Ek hi raste bacha… main hi naali me let jaata hoon.”

Woh naali me let gaya,
aur uske sharir se pani ruka.

Rishi ne jab dekha ki Aruni wapas nahi aaya,
to unhone shishyon se poocha.
Sab milkar naali ke paas gaye aur pukara:

“Aruni! Kahan ho, beta?”

Aruni awaaz sunte hi khada ho gaya.
Pani fir behne laga.

Woh bola:

“Guruji, main naali me letkar pani rok raha tha.
Aapki awaaz sun kar uth gaya.”

Dhaumya bahut prasan hua aur bola:

“Aaj se tumhara naam hoga Uddalaka,
aur tum gyaan se chamko ge.
Sab Veda aur Dharmashastra tumme jagmagayenge.”

Yeh kehkar Rishi ne Aruni ko ashirvaad diya.
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.3.2"):
                    text1 = """
🐄 Guru ka Adesh

Rishi Ayoda-Dhaumya ne ek din kaha:

“Upamanyu, beta, jao aur gaayon (kine) ki dekhbhal karo.”

Upamanyu din bhar gaay charata,
shaam ko guru ke paas aakar namaskar karta.

Guru ne dekha ki Upamanyu mazboot aur healthy lag raha hai.
Unhone pucha:

“Beta, kya khate ho tum? Itne mote-mote lag rahe ho.”

Upamanyu bola:

“Guruji, main bhiksha (alms) se pet bhar leta hoon.”

Guru bole:

“Jo bhiksha mile, pehle guru ko deni hoti hai.”

Upamanyu ne haan kiya.
Agli baar usne saari bhiksha guru ko de di.
Guru ne sab le liya—Upamanyu ke paas kuch nahi bacha.
            """
                    create_image_text_layout("attached_assets/chapter1/1.3.2.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🔄 Doosra Raasta

Phir bhi Upamanyu healthy dikha.
Guru ne pucha:

“Ab kya kha rahe ho?”

Upamanyu bola:

“Guruji, main doosri baar bhiksha maang leta hoon.”

Guru ne kaha:

“Nahi beta, ye galat hai.
Tum dusre bhikshukon ka hissa kam kar rahe ho.
Ye lobh (covetousness) dikhaata hai.”

Upamanyu ne ye bhi chhod diya.

🥛 Teesra Raasta

Agli baar bhi Upamanyu filled-out dikh raha tha.
Guru ne pucha:

“Ab kya kha rahe ho?”

Upamanyu bola:

“Guruji, main gaayon ka doodh pi leta hoon.”

Guru ne mana kiya:

“Beta, doodh bina pooche lena uchit nahi (not lawful).”

Upamanyu ne doodh bhi chhod diya.

🫧 Chautha Raasta

Phir bhi woh healthy tha!
Guru ne dubara pucha.

Upamanyu bola sharmate hue:

“Guruji, main bas bachdon (calves) ke muh se girti hui jhag (froth) chakh leta hoon.”

Guru ne gusse se kaha:

“Nahi!
Bachde tum par daya karke jhag gira rahe honge.
Tum unka hissa le rahe ho.
Yeh bhi galat hai.”

Upamanyu ne ye bhi chhod diya.

🌿 Bhukha aur Andha

Ab Upamanyu ke paas khane ko kuch nahi thā.
Ek din bhookh se pareshaan hokar usne Arka (a poisonous plant) ke patte kha liye.

Patte teekhe, kadve, zehreele the.
Uski aankhen jalne lagi, aur woh andha ho gaya.

Andha hokar woh chal nahi paaya,
aur ek kuen (well) me gir gaya.

😨 Guru ki Talaash

Shaam tak Upamanyu na aaya to guru ne kaha:

“Chalo, hum use dhoondte hain.”

Woh sab milkar jungle me gaye,
aur pukarne lage:

“Upamanyooo!”

Neeche se awaaz aayi:

“Guruji, main kuen me hoon!”

Guru ne pucha:

“Kaise gira?”

Upamanyu bola:

“Bhuke-pan me Arka ke patte khaye. Andha ho gaya. Gir gaya.”

🙏 Asvins ki Stuti (praise of the twin gods)

Guru bole:

“Beta, Asvins (dev-doctors, twin gods) ki stuti karo.
Woh tumhari aankhen theek kar denge.”

Upamanyu ne Rigveda ke sundar mantron se
Asvins ki prarthana ki—
unhe “prakriti ke rakhwale”,
“samay ke chalak”,
aur “jeevan ke pakshi (birds)” bataya.

Prarthana sunkar Asvins prakat hue.

🍪 Pariksha ka Aakhri Mod

Asvins bole:

“Beta, yeh prasad lo. Kha lo. Tumhari nazar wapas aa jayegi.”

Upamanyu bola:

“Main bina guru ko diye kuch nahi kha sakta.”

Asvins bole:

“Tumhare guru ne kabhi prasad paakar hume nahi poocha tha.
Tum bhi waise hi karo.”

Upamanyu bola:

“Nahi devon, main guru-agnya (teacher’s command) nahi tod sakta.”

Asvins bahut khush hue:

“Tumhari bhakti (devotion) sachi hai.
Tumhari aankhen wapas—aur daant sone ke honge!
Tumhara bhavishya shubh hoga.”

Aisa kahi kar unhone vardaan diya.

🌟 Guru ki Prashansa

Drishti paakar Upamanyu guru ke paas gaya
aur sab bataya.

Guru Dhaumya prasan ho gaye:

“Beta, tumhe sab Veda aur Dharmashastra ka gyaan prapt hoga.”

Yeh thi Upamanyu ki kasauti (trial).
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.3.3"):
                    text1 = """
🌱 Veda ka Seva-bhaav

Rishi Ayoda-Dhaumya ne apne teesre shishya ko kaha:

“Veda, beta, kuch samay mere ghar raho aur guru-seva karo. Tumhara hi bhala hoga.”

Veda ne haan ki.
Woh bina shikayat garmi-thand, bhookh-pyaas sab jhelta raha—
bilkul uss bail (ox) ki tarah jo apne malik ka bojh uthaata hai.

Jaldi hi guru usse prasann (pleased) ho gaye.
Isse Veda ko good fortune aur poora gyaan mila.
Yeh thi Veda ki pariksha.

👨‍🏫 Veda ban gaya Guru

Veda ne guru se vidya poori karke grihastha (householder life) apnaaya.
Uske teen shishya bane.

Veda ne kabhi apne shishyon ko kaam karne ko majboor nahi kiya,
kyunki usne khud guru-ke-ghar me bahut kasht jhel rakha tha.
Woh chahta tha ki uske shishyon ko dukh na mile.
            """
                    create_image_text_layout("attached_assets/chapter1/1.3.3.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🐂 Utanka aur Guru ka Ghar

Ek din Raja Janamejaya aur Paushya ne Veda ko apna Upadhyaya (teacher) banaya.
Kuch samay baad Veda ko ek yajna ke kaam se jaana tha.

Usne apne shishya Utanka se kaha:

“Beta, jab tak main nahi hoon, ghar ka saara kaam tum sambhalo.
Koi bhi baat chhuti nahi rehni chahiye.”

Utanka ne guru ka adesh maan liya.

👩‍🦳 Guru-patni ka Ajeeb Aadesh

Guru ke jaane ke baad, ghar ki auratein Utanka se boli:

“Utanka, tumhari guru-patni ab 'garbha-dhaaran yogya' (fertile period) me hain.
Guru ghar me nahi—tum hi unke sthan par 'kartavya' karo.”

Utanka ghabra gaya.
Usne kaha:

“Nahi! Guru ne mujhe kabhi aisa kuch nahi kaha.
Aur main kisi galat kaam me haath nahi daal sakta.”

Yeh sunkar sab chup ho gayi.

🙏 Guru ki Prasannata

Guru wapas aaye to sab sunke khush ho gaye.
Unhone kaha:

“Utanka, beta, tumne maryada (propriety) nibhayi.
Batao, kya vardaan chahiye? Tum ja sakte ho.”

Utanka bola:

“Guruji, chhutti lene se pehle guru-dakshina (honorarium) deni zaroori hai.”

Guru bole:

“Thik hai, apni guru-patni se poocho.”

👑 Guru-patni ka Ichchha

Utanka ne guru-patni se poocha:

“Kya guru-dakshina du?”

Woh boli:

“Raja Paushya ki Rani ke kaan me ek vishesh kundal (ear-rings) hain.
Mujhe wahi chahiye.
Chaar din baad vrata ka din hai—main unhe pehenna chahti hoon.
Laoge, to tumhara kalyan hoga.”

Utanka agree kar gaya.

🐂 Raaste me Ek Rahasya

Raaste me Utanka ne dekha—
Ek asadharan bada sa bail (bull) aur ek ajeeb uncha aadmi uspar baitha hua.

Woh aadmi bola:

“Utanka, is bail ka gobar kha lo.”

Utanka dar gaya.
Usne mana kiya.

Aadmi bola:

“Kha lo. Tumhare guru ne bhi ye hi khaya tha.”

Utanka ne vishwas kar liya
aur gobar khaaya, mutra piya,
phir haath-muh dho kar aage badh gaya.

(Ye sab ek divya pariksha thi—symbolic, impurity removal ka yogic method.)

👑 Raja Paushya ke Darbaar me

Utanka ne Raja Paushya ko pranaam kiya aur bola:

“Mujhe Rani ke ear-rings chahiye. Guru-dakshina hai.”

Paushya ne kaha:

“Andar jaakar Rani se maang lo.”

Utanka gayā, par Rani dikhai nahi di.
Wapas aakar bola:

“Rani toh hai hi nahi. Aap jhooth bol rahe ho?”

Paushya ne kaha:

“Shayad tum ashuddha (impure) ho.
Rani pavitra (pure) ke alawa kisi ko nahi dikhati.”

Utanka ko yaad aaya:

“Haan! Maine chal-te-chalte khade hokar jal paan (ablution) kiya tha.
Woh galat hota hai.”

Paushya ne shuchita (purification) ka sahi tarika bataya.
Utanka ne dhyaan se snan kiya, jal sipa liya, aur phir gaya—
iss baar Rani mil gayi.

Rani ne prasannata se kundal de diye.
Par ek chetavani bhi:

“Dhyaan se rakhna.
Ye kundal Takshaka (Naga king) churaane ki koshish karta hai.”

Utanka bola:

“Takshaka mujhe kya rokega!”

Aur nikal pada.

🍽 Paushya ka Shraap

Wapas jaane se pehle Paushya ne kaha:

“Tum jaise yogya brahman kam milte hain.
Main tumhe shraddha-bhoj khilana chahta hoon.”

Utanka ne haan kiya.

Lekin bhojan me baal tha aur thanda tha—
mata hua bhojan ashuddha maana jata hai.

Utanka ne kaha:

“Aisa bhojan dene par tumhari drishti (sight) chali jaayegi.”

Paushya ne gusse me kaha:

“Aur jo tumne saaf bhojan ko ashuddha kaha—
tum vansh-vihheen (without issue) ho jaoge!”

Utanka bola:

“Bhojan waqehi ganda hai. Dekh lo.”

Paushya ne dekha—
bhojan thanda, baalon se bhara, aur unbraided hair wali naukrani ne banaya tha.
Usne shraap wapas lene ki prarthna ki.
            """
                    create_image_text_layout(text_content=text2, layout="full")

        with st.expander("Section 1.3.4"):
                    text1 = """
🔥 Paushya aur Utanka ka Doosra Vachansangharsh

Utanka ne Raja Paushya ko shraap diya tha:

“Tum andhe ho jaoge!”

Paushya ne bhi shraap diya:

“Tum vansh-vihheen ho jaoge!”

Ab Utanka shant ho kar bola:

“Maine tumhe vastavik roop se dikhaya tha ki bhojan gandaa tha.
Isliye tumhara shraap mujh par kaise lagega?”

Paushya ne kaha:

“Mera dil kathor (hard-hearted) hai, main apna shraap wapas nahi le sakta. Brahman ke shabd kathor lagte hain par unka dil naram hota hai. Kshatriya ke shabd naram dikhte hain, par unka dil teekha hota hai. Isliye, main shraap nahi badal sakta.”

Utanka ne kendrit hokar kaha:

“Koi baat nahi. Tumhara shraap mujhe nahi lagega. Main chalta hoon.”
            """
                    create_image_text_layout("attached_assets/chapter1/1.3.4.jpg", text1,   layout="side", image_position="left")

                    text2 = """
🏃‍♂️ Kundalon ki Chori – Bhikhari jo Takshaka nikla

Utanka ne rani ke vishesh kundal (ear-rings) lekar wapas ja raha tha.
Raaste me ek nagna bhikhari baar–baar nazar aata–gayab hota.

Utanka ne kundal zameen par rakhe aur jal lene gaya.

Jab wapas aaya—
kundal gayab! 😨

Bhikhari bhaag raha tha! Utanka ne peecha kiya.
Pakadne par bhikhari ne apna asli roop dharan kara:

🔥 Woh Takshaka, Nagon ka Raja tha! 🔥

Aur woh zameen me khule ek bade gaddhe (hole) me ghus gaya
—yeh Nagalok ka dwar tha.

⚡ Indra ka Vajra aur Rahasya Dwar

Utanka ne laathi se gaddha khodna shuru kiya, par gaddha nahi khul raha tha.
Indra ne asmaan se dekha:

“Yeh brahman satya ka bhakt hai.”

Usne apna Vajra (thunderbolt) Utanka ki laathi me bhej diya.
Laathi turant Vajra jaise shaktishaali ban gayi
aur Nagalok ka darwaza khul gaya.

Utanka usme ghus gaya.

🐍 Nagalok ka Darshan

Andar Nagalok me Uttanka ne dekha:

✨ Laakhon mahal,
✨ sohne darwaaze,
✨ sone-chandi ke mandir,
✨ snake-palaces with domes,
ek alag hi divya duniya.

Wahan khade hokar Utanka ne Nagas ki stuti ki:

“Hey Airavata ke vanshaj Nagon!
Hey Takshaka! Hey Asvasena!
Main tum sabko pranam karta hoon!”

Par fir bhi Takshaka ne kundal nahi diye.

Utanka pareshaan ho gaya.

🧵 Cosmic Loom – Do Deviyan aur Kaala-Chitta Ka Srijan

Utanka ne aas–paas dekha.
Ek ajeeb drishya:

Do mahilaen ek bada sa loom (taana) chala rahi thi.

Kaale aur safed dhaage—raat aur din—se poora jagat bun rahi thi.

Pas me ek 12 spokes ka chakra, jise 6 ladke ghumaa rahe the—yeh samvatsar (1 saal) tha.

Ek purush, ek tejasvi ghode ke saath khada tha.

Utanka ne unki stuti ki aur kaha:

“Aap hi brahmand ke srijan aur samay ke swami ho.
Mujhe Nag log par niyantran chahiye!”

Woh aadmi bola:

“Iss ghode me phoonk maaro.”

Utanka ne phoonk maari—

🔥 ghoda Agni ban gaya!

Har chhed se aag nikli
aur poora Nagalok jalne laga!

Takshaka ghabra gaya:

“Bas karo! Yeh lo kundal! Le jao!”

Utanka ne kundal wapas le liye.

⚡ Woh Purush Kaun Tha?

Woh bola:

“Chadha jao. Main ek pal me tumhe tumhare guru ke ghar pahunchaa dunga.”

Ghoda turant udkar ashraam pahunch gaya.

🕉️ Guru aur Guru-patni ka Ashirvaad

Guru-patni snan karke soch rahi thi:

“Utanka nahi aaya… galat waqt par aaya to shraap dungi!”

Utanka theek timing par pahunch gaya
aur kundal de diye.

Guru-patni khush ho gayi:

“Tum dharm-nishtha (faithful) ho. Tumhe sab kaam me safalta milegi.”

Utanka ne guru ko sab bataya.
Guru ne arth samjhaya:

Do mahilaen ― Dhata aur Vidhata (Creator aspects)

Kaale-safed dhaage ― Raat aur Din

12-spokes ka chakra ― Varsh ka Chakra

6 ladke ― 6 Ritu (seasons)

Ghoda ― Agni

Aadmi ― Parjanya (rain-god)

Bail ― Airavata

Bail ka dung ― Amrit

Is Amrit ki wajah se Utanka Nagalok me marra nahi.

🐍🔥 Takshaka se Badla — Janamejaya ko Bhadkaana

Guru se vidya poori karke Utanka ab Takshaka se nafrat karta tha.
Isliye woh Hastinapur gaya.

Yahan Raja Janamejaya apne pita Parikshit ki maut ka shok mana raha tha.
Takshaka ne hi unhe kata tha.

Utanka bola:

“Rajan! Aap bacchon ki tarah khel rahe ho?
Takshaka ne aapke pita ka nirdosh hatya ki.
Aap badla kyun nahi le rahe?”

Janamejaya gusse me bhar gaya.

Utanka me aur aag bhadkai:

“Takshaka ne aapke pita ko mara aur
Kashyapa rishi ko bhi rishwat de kar wapas bhej diya.
Ab samay aa gaya hai—
Sarpa-yajna karao.
Takshaka ko jala do!”

Raja gusse me agni ki tarah bhadak uthaa.

Isi gusse se shuru hota hai
Sarpa-Satra – Mahabharat ka prakhyat Sarpa-Yajna.
            """
                    create_image_text_layout(text_content=text2, layout="full")
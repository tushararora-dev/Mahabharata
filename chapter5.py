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
    create_image_text_layout("attached_assets/chapter5/chapter5.jpg", layout="full")


    text0 = """
    <h2>Book 5 - Udyoga Parva</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    # ==================================================
    # Chapter 5.1 - Udyoga Parva
    # ==================================================

    with st.expander("Chapter 5.1  Udyoga Parva"):

        # Section 5.1.1
        with st.expander("Section 5.1.1  Section I"):
            text1 = """ 
            Chapter 1 – Shanti ki Aakhri Koshish

Abhimanyu aur Uttara ka vivaah shaanti se poora ho gaya.

Us raat sab raja aaraam se rahe.

Agli subah sabhi mahaan raja Raja Virat ki sabha mein ikattha hue.

Sabha bahut bhavya thi.

Har taraf sundar heere, moti aur sugandhit phool sajaaye gaye the.

Sabhi raja apni-apni jagah baith gaye.

Raja Virat aur Raja Drupad sabse aage baithe."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Unke paas Shri Krishna, Balram, Yudhishthir, Bhim, Arjun, Nakul, Sahadev, Abhimanyu aur doosre veer yoddha baithe the.

Sabha taaron se bhare aasman ki tarah chamak rahi thi.

Sab kuch shaant tha.

Sabki nazar Shri Krishna par tik gayi.

Tab Shri Krishna dheere se khade hue aur sabse baat karne lage.

Krishna ki Baat

Krishna bole,

“Aap sab jaante hain ki Yudhishthir ko paason ke khel mein dhokhe se haraaya gaya tha.”

“Unse unka rajya cheen liya gaya.”

“Unhe 12 saal vanvaas aur 1 saal agyaatvaas ka vaada nibhaana pada.”

Krishna ne kaha,

“Pandav chaahte toh bal se apna rajya wapas le sakte the.”

“Lekin unhone apna vachan nahi toda.”

“Unhone har mushkil ko shaanti se saha.”

“Agyaatvaas ka aakhri saal sabse kathin tha.”

“Phir bhi kisi ne unhe pehchaana nahi.”

Yudhishthir ka Swabhav

Krishna bole,

“Yudhishthir itne dharmik hain ki woh galat tareeke se Swarg ka rajya bhi nahi lenge.”

“Agar nyaay se sirf ek gaon bhi mile, toh woh usi mein khush rahenge.”

Pandavo ke Saath Anyay

Krishna ne sabko yaad dilaaya,

“Jab Pandav chhote the, tabhi unhe maarne ki kai saazishein rachi gayi.”

“Unka rajya dhokhe se cheena gaya.”

“Phir bhi unhone hamesha dharm ka saath diya.”

Pandav Yudh Nahi Chahte

Krishna bole,

“Pandav sirf wahi rajya maang rahe hain jo unhone apni mehnat aur veerta se jeeta tha.”

“Unki ichchha yudh nahi, nyaay hai.”

Lekin Zarurat Padi Toh...

Krishna ne gambhir swar mein kaha,

“Agar Pandavo ke saath fir anyay hua, toh woh yudh se peeche nahi hatenge.”

“Unke mitra bhi unke saath poori shakti se ladenge.”

Shanti ka Prastaav

Krishna ne sab rajaon ki taraf dekhkar kaha,

“Humein pehle shanti ki koshish karni chahiye.”

“Koi buddhimaan, imaandaar aur samajhdaar doot Hastinapur bhejna chahiye.”

“Woh Duryodhan se vinamrata se kahe ki Yudhishthir ko unka aadha rajya wapas de de.”

“Yahi sabke liye sabse achha raasta hoga.”

Sabha mein baithe sabhi raja Krishna ki baat dhyaan se sunte rahe.

Unhe samajh aa gaya ki Krishna pehle shanti chahte hain.

Lekin agar nyaay na mila, toh yudh ko bhi roka nahi jaa sakega."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.2
        with st.expander("Section 5.1.2  Section II"):
            text1 = """ 
            Chapter 2 – Balram ne Shanti ka Raasta Chuna

Balram ji sabha mein khade hue aur bole,

“Krishna ne bahut samajhdari aur nyaay ki baat kahi hai.”

“Pandav sirf aadha rajya maang rahe hain.”

“Yeh unki taraf se ek bada balidaan hai.”

Aadha Rajya De Dena Chahiye"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Balram ji bole,

“Duryodhan ko bina jhagde aadha rajya de dena chahiye.”

“Isse dono parivaar khushi se reh sakenge.”

“Jab Pandavo ko unka adhikaar mil jaayega, tab sabke liye shanti aur sukh hoga.”

Ek Doot Bhejna Chahiye

Balram ji ne salaah di,

“Humein ek buddhimaan aur vinamra doot Hastinapur bhejna chahiye.”

“Woh pehle Bhishma, Dronacharya, Kripacharya, Vidur aur Dhritarashtra jaise bade logon ko samman se pranam kare.”

“Phir sabke saamne Yudhishthir ki baat shaanti aur vinamrata se rakhe.”

Gusse se Baat Bigad Sakti Hai

Balram ji bole,

“Duryodhan ko gussa dilane wali baat bilkul nahi karni chahiye.”

“Shaanti se baat karne se kaam ban sakta hai.”

Yudhishthir ki Galti

Phir Balram ji ne ek alag baat kahi.

Woh bole,

“Yudhishthir ne bhi ek galti ki thi.”

“Unhe dice ka khel achchhi tarah nahi aata tha.”

“Unke mitron ne bhi unhe mana kiya tha.”

“Phir bhi unhone Shakuni ko hi khelne ke liye chuna.”

Balram ji ne kaha,

“Us samay aur bhi bahut se dice ke khiladi the.”

“Lekin Yudhishthir ne sabko chhodkar sirf Shakuni se hi khela.”

“Jab baar-baar haar rahe the, tab bhi unhone khel nahi roka.”

“Isliye poora dosh sirf Shakuni par nahi daala ja sakta.”

Shanti Hi Sabse Achha Raasta Hai

Balram ji ne apni baat samaapt karte hue kaha,

“Humein yudh se bachna chahiye.”

“Pyaar aur shaanti se baat karne se jo kaam ho sakta hai, woh talwar se hamesha nahi hota.”

“Isliye pehle milkar samjhaane ki poori koshish karni chahiye.”

Balram ji ki baat chal hi rahi thi ki achanak Satyaki khade ho gaye.

Unke chehre par gussa saaf dikh raha tha.

Unhe Balram ji ki baat bilkul pasand nahi aayi.

Ab sabha mein ek nayi behas shuru hone wali thi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.3
        with st.expander("Section 5.1.3  Section III"):
            text1 = """ 
            Chapter 3 – Satyaki ka Krodh aur Yudh ka Elan

Balram ji ki baat khatam hote hi Satyaki turant khade ho gaye.

Unke chehre par gussa saaf dikh raha tha.

Woh bole,

“Insaan ke dil mein jo hota hai, wahi uski baaton mein dikhai deta hai.”

“Duniya mein kuch log bahadur hote hain aur kuch darpok.”

Yudhishthir ko Dosh Mat Do"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Satyaki ne kaha,

“Main Balram ji ka apmaan nahi kar raha.”

“Lekin jo log Yudhishthir jaise dharmik raja ko dosh dete hain, unki baat main kabhi nahi maan sakta.”

Woh bole,

“Yudhishthir ko dice ka khel nahi aata tha.”

“Shakuni dhokhe se khelta tha.”

“Usne chal se Yudhishthir ko haraaya.”

“Ismein Yudhishthir ki kya galti thi?”

Yeh Jeet Nyaay ki Nahi Thi

Satyaki bole,

“Agar saamne se imaandari se jeet hoti, toh baat alag thi.”

“Lekin yeh jeet dhokhe se mili thi.”

“Isliye yeh sachchi jeet nahi thi.”

Pandavo ne Har Vachan Nibhaya

Woh bole,

“Pandavo ne 12 saal vanvaas aur 1 saal agyaatvaas poora kiya.”

“Unhone apna har vaada nibha diya.”

“Ab unka rajya wapas milna hi chahiye.”

Fir Bhi Duryodhan Mana Kar Raha Hai

Satyaki ne kaha,

“Bhishma aur Dronacharya ne bhi Duryodhan ko samjhaya.”

“Lekin woh fir bhi rajya dene ko taiyaar nahi hai.”

“Ab aur kitni baat karni baaki hai?”

Ab Baat Talwar Karegi

Satyaki ki awaaz aur tez ho gayi.

Woh bole,

“Main unse teeron ki bhaasha mein baat karunga.”

“Main Duryodhan aur uske saathiyon ko haraakar Yudhishthir ko fir se singhasan par bithaunga.”

Pandavo ki Shakti

Satyaki bole,

“Arjun ko kaun rok sakta hai?”

“Bhim ka saamna kaun kar sakta hai?”

“Nakul aur Sahadev bhi mahaan yoddha hain.”

“Dhrishtadyumn, Abhimanyu aur Draupadi ke paanch putra bhi kisi se kam nahi.”

“Krishna hamare saath hain.”

“Hum sab milkar Kaurav sena ka saamna karenge.”

Antim Faisla

Satyaki ne dridh swar mein kaha,

“Jo humein maarna chahte hain, unse yudh karna paap nahi hai.”

“Lekin dushman ke saamne haath phailaana bahut badi beizzati hai.”

Phir unhone sabha mein sabki taraf dekhkar kaha,

“Ya toh aaj hi Yudhishthir ko unka rajya wapas milega.”

“Ya phir hamare dushman yudh bhoomi mein girenge.”

Sabha mein sannata chha gaya.

Ab sab samajh gaye the ki shanti ki ummeed dheere-dheere kam hoti ja rahi thi aur yudh ka samay kareeb aa raha tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.4
        with st.expander("Section 5.1.4  Section IV"):
            text1 = """ 
            Chapter 4 – Drupad ka Yudh ki Taiyaari ka Faisla

Raja Drupad sabki baat dhyaan se sunne ke baad bole,

“Satyaki ki baat bilkul sahi hai.”

“Mujhe bhi nahi lagta ki Duryodhan kabhi shaanti se rajya wapas dega.”

Duryodhan Kabhi Nahi Maane Ga

Drupad bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Dhritarashtra hamesha apne bete ka saath denge.”

“Bhishma aur Dronacharya bhi usi paksh mein khade rahenge.”

“Karna aur Shakuni bhi Duryodhan ka hi saath denge.”

Balram ki Salah Achhi Hai

Drupad ne kaha,

“Balram ji ki salah galat nahi hai.”

“Jo vyakti shaanti chahta hai, use pehle baat karni chahiye.”

“Lekin Duryodhan jaise aadmi par sirf meethi baaton ka koi asar nahi hoga.”

Sirf Narmi Kaam Nahi Karegi

Drupad bole,

“Duryodhan bahut ziddi aur ahankaari hai.”

“Agar hum usse sirf pyaar se baat karenge, toh woh ise hamari kamzori samjhega.”

“Use lagega ki woh jeet gaya hai.”

Dono Kaam Saath-Saath Honge

Drupad ne dridh swar mein kaha,

“Isliye humein do kaam ek saath karne chahiye.”

“Ek taraf shaanti ki baat chale.”

“Aur doosri taraf yudh ki poori taiyaari bhi ho.”

Mitra Rajaon ko Bulao

Drupad bole,

“Turant apne sabhi mitra rajaon ko sandesh bhejo.”

“Unse kaho ki apni sena lekar hamara saath dene aayein.”

Unhone kaha,

“Yaad rakho, Duryodhan bhi yahi karega.”

“Jo pehle madad maangta hai, aksar use pehle sahayata mil jaati hai.”

“Isliye humein deri nahi karni chahiye.”

Sabko Sandesh Bheja Jaaye

Drupad ne kai mitra rajaon ke naam liye.

Unhone kaha,

“Shalya, Dhrishtaketu, Kekaya ke raja, Bhagadatta, Kashi ke raja, Kamboj aur doosre sabhi mitra rajaon ko turant bulao.”

“Har mitra ko bata do ki mushkil ka samay aa gaya hai.”

Hastinapur mein bhi Doot Jaayega

Phir Drupad bole,

“Mera vidvaan Brahman purohit Hastinapur jaayega.”

“Woh Dhritarashtra ke saamne hamari baat shaanti aur maryada se rakhega.”

“Woh Bhishma, Dronacharya aur sabhi bade logon ka samman karega.”

“Phir Duryodhan ko nyaay ki baat samjhaayega.”

Antim Faisla

Drupad ne sabha ki taraf dekhkar kaha,

“Hum shaanti ka mauka zaroor denge.”

“Lekin agar nyaay na mila, toh hum yudh ke liye poori tarah taiyaar rahenge.”

Sabhi rajaon ne Drupad ki baat se sahmati dikhayi.

Ab Pandav ek saath do raaston par chal rahe the — pehle shaanti ki koshish, aur saath hi yudh ki poori taiyaari."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.5
        with st.expander("Section 5.1.5  Section V"):
            text1 = """ 
            Chapter 5 – Shanti ki Aakhri Koshish, Phir Yudh ki Taiyaari

Shri Krishna ne Raja Drupad ki baat sunkar kaha,

“Rajan, aapki yojana bilkul sahi hai.”

“Sabse pehle humein shaanti ki poori koshish karni chahiye.”

Pehle Shanti, Phir Yudh

Krishna bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Jo vyakti bina baat kiye seedha yudh chunta hai, woh samajhdaar nahi hota.”

“Isliye pehle Duryodhan ko ek nyaaypoorn sandesh bhejna zaroori hai.”

Krishna ka Drupad par Vishwas

Krishna ne Drupad se kaha,

“Dhritarashtra aapka bahut samman karte hain.”

“Bhishma, Dronacharya aur Kripacharya bhi aapko achchhi tarah jaante hain.”

“Isliye agar aap apna doot bhejenge, toh uski baat ko sab dhyaan se sunenge.”

Agar Duryodhan Maan Gaya

Krishna bole,

“Agar Duryodhan nyaay ki baat maan kar shaanti kar leta hai, toh Kaurav aur Pandav fir se ek parivaar ki tarah reh sakte hain.”

“Yeh sabke liye sabse achha hoga.”

Aur Agar Mana Kar Diya...

Phir Krishna ka swar gambhir ho gaya.

Woh bole,

“Lekin agar Duryodhan ahankaar mein aakar shaanti ka prastaav thukra de...”

“Toh humein bhi bula lena.”

“Us din Arjun ka Gandiv garaj uthega.”

“Aur Duryodhan apne saathiyon ke saath apne karmon ka phal zaroor paayega.”

Krishna Dwarka Laut Gaye

Iske baad Raja Virat ne Krishna ka samman kiya.

Krishna apne parivaar aur saathiyon ke saath Dwarka wapas chale gaye.

Dono Paksh Taiyaar Hone Lage

Krishna ke jaate hi Pandav aur Raja Virat ne yudh ki taiyaari shuru kar di.

Har taraf sandesh bheje gaye.

Mitra rajaon ko apni sena ke saath bulaaya gaya.

Raja Drupad ne bhi apne sabhi saathiyon ko sandesh bheja.

Duryodhan bhi Chup Nahi Baitha

Jab Duryodhan ko pata chala ki Pandav badi sena ikatthi kar rahe hain, toh usne bhi turant apne mitra rajaon ko bula liya.

Dheere-dheere poore Bharat ke raja do pakshon mein bantne lage.

Kuch Pandavo ke saath aaye.

Aur kuch Kauravo ka saath dene lage.

Dharti Hil Uthi

Har taraf haathi, ghode, rath aur sainik hi sainik dikhne lage.

Itni badi senaayein chal rahi thi ki aisa lag raha tha jaise poori dharti unke kadmon se kaanp rahi ho.

Sabko mehsoos ho raha tha ki ek mahaan yudh ab bahut kareeb hai.

Antim Shanti Sandesh

Yudhishthir ki ichchha ke anusaar Raja Drupad ne apne buddhimaan aur vriddh purohit ko Hastinapur bheja.

Unka kaam tha ek baar phir shaanti aur nyaay ki baat rakhna.

Pandav ab bhi yudh nahi chahte the.

Woh bas apna haq aur nyaay maang rahe the.

Lekin ab faisla Duryodhan ke haath mein tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.6
        with st.expander("Section 5.1.6  Section VI"):
            text1 = """ 
            Chapter 6 – Drupad ka Buddhimaan Doot Hastinapur Chala

Raja Drupad ne apne vriddh aur vidvaan Brahman purohit ko bulaaya.

Woh bole,

“Sansar mein sabse mahatvapurn woh log hote hain jo sachcha gyaan aur samajh rakhte hain.”

“Aur un sab mein aap sabse adhik yogya hain.”

Drupad ka Vishwas

Drupad bole,

“Aap buddhi aur gyaan mein Brihaspati aur Shukracharya jaise mahaan guruon ke samaan hain.”

“Aap Dhritarashtra aur Yudhishthir, dono ke swabhav ko achchhi tarah jaante hain.”"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Pandavo ke Saath Anyay Hua

Drupad ne kaha,

“Dhritarashtra sab kuch jaante hue bhi chup rahe.”

“Unhone apne bete Duryodhan ko kabhi nahi roka.”

“Shakuni ne dhokhe se Yudhishthir ko dice ke khel mein haraaya.”

“Yudhishthir imaandaar the, lekin Shakuni chalak tha.”

“Isliye unse rajya cheen liya gaya.”

Nyaay ki Baat Karna

Drupad bole,

“Jab aap Hastinapur jaayein, toh dharm aur nyaay ki baat zaroor kijiye.”

“Vidur jaise buddhimaan log aapki baat ka saath denge.”

“Bhishma, Dronacharya aur Kripacharya bhi sachchai ko samajhenge.”

Samay ka Sahi Upyog

Drupad ne apni yojana samjhaai.

Woh bole,

“Jab tak Kaurav aapki baaton mein lage rahenge, tab tak Pandav aaraam se apni sena aur yudh ki taiyaari poori kar lenge.”

“Isse humein samay bhi mil jaayega.”

Pandavo ke Dukh Batana

Drupad bole,

“Dhritarashtra ko yaad dilaana ki Pandavo ne kitne dukh sahe hain.”

“Unhe unke purvajon ki parampara aur dharm bhi yaad dilaana.”

“Ho sakta hai unka hriday badal jaaye.”

Darne ki Zaroorat Nahi

Drupad ne kaha,

“Aap ek Brahman hain.”

“Aap doot bankar ja rahe hain.”

“Koi bhi aapko nuksaan nahi pahunchayega.”

Shubh Muhurat mein Ravana

Ant mein Drupad bole,

“Pushya nakshatra aur Jaya muhurat mein turant Hastinapur ke liye ravana ho jaiye.”

“Pandavo ke hit ke liye apni poori buddhi aur samajh ka upyog kijiye.”

Vaisampayan ji ne kaha,

“Raja Drupad ka aadesh paakar woh buddhimaan Brahman apne kuch shishyon ke saath Hastinapur ke liye nikal pade.”

Ab Pandavo ki taraf se shaanti ka sandesh Kauravo tak pahunchne wala tha.

Lekin sabke mann mein ek hi sawaal tha—

Kya Duryodhan nyaay maanega, ya Mahabharat ka yudh ab nishchit ho chuka tha?"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.7
        with st.expander("Section 5.1.7  Section VII"):
            text1 = """ 
            Chapter 7 – Krishna ko Chunne ka Faisla

Vaisampayan ji ne kaha,

“Pandavon ne apne doot ko Hastinapur bhej diya.”

Saath hi, alag-alag rajaon ko bhi sandesh bhejne lage ki woh yudh ke liye taiyaar rahein.

Arjun Dwarka Chale

Is beech Arjun ne socha,

“Sabse zaroori baat hai Shri Krishna ka saath.”

Isliye woh khud Dwarka ke liye nikal pade.

Lekin Duryodhan ko bhi yeh khabar mil gayi.

Woh bhi tez ghodon par baithkar Dwarka pahunch gaya."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Dono Ek Saath Pahunche

Jab Arjun aur Duryodhan Dwarka pahunche, tab Shri Krishna aaraam kar rahe the.

Duryodhan jaakar Krishna ke sirhane ke paas baith gaya.

Use laga ki Krishna aankh kholte hi sabse pehle use dekhenge.

Arjun chup-chaap Krishna ke charanon ke paas haath jodkar khade ho gaye.

Krishna Ne Kise Pehle Dekha?

Kuch der baad Krishna ki aankh khuli.

Unhone sabse pehle Arjun ko dekha.

Phir unki nazar Duryodhan par gayi.

Krishna muskuraakar bole,

“Tum dono ek saath yahan kaise aaye?”

Duryodhan ki Maang

Duryodhan bola,

“Prabhu, yudh hone wala hai.”

“Main sabse pehle aaya hoon.”

“Isliye niyam ke anusaar pehle meri madad honi chahiye.”

Krishna ka Faisla

Krishna bole,

“Tum pehle aaye ho, yeh baat sahi hai.”

“Lekin maine sabse pehle Arjun ko dekha.”

“Aur Arjun tumse chhote bhi hain.”

“Isliye pehle chunne ka adhikaar Arjun ka hoga.”

Phir Krishna ne dono ke saamne do vikalp rakhe.

“Ek taraf meri poori Narayani Sena hai.”

“Doosri taraf main khud hoon.”

“Lekin main yudh mein koi hathiyaar nahi uthaoonga.”

“Main sirf saath rahunga.”

Arjun ka Chunav

Krishna ne Arjun se poocha,

“Batao, tum kya chahte ho?”

Arjun ne bina ek pal soche jawab diya,

“Mujhe aap chahiye.”

“Mujhe sena nahi chahiye.”

Duryodhan yeh sunkar andar hi andar bahut khush ho gaya.

Usne turant Narayani Sena ko chun liya.

Usse laga ki asli taakat toh sena mein hi hai.

Balram ka Faisla

Phir Duryodhan Balram ji ke paas gaya.

Usne unse bhi apni taraf se ladne ki prarthana ki.

Balram ji bole,

“Maine pehle hi kaha tha ki main Pandav aur Kaurav, dono ko samaan maanta hoon.”

“Main Krishna ke khilaaf nahi ja sakta.”

“Isliye main is yudh mein kisi bhi paksh se nahi ladoonga.”

Duryodhan ne unka samman kiya aur wahan se chala gaya.

Aur Sena Mil Gayi

Uske baad Duryodhan Kritavarma ke paas gaya.

Kritavarma ne usse ek poori Akshauhini sena de di.

Duryodhan bahut khush ho gaya.

Use poora vishwas tha ki itni badi sena ke saamne Pandav tik nahi paayenge.

Krishna ka Sawaal

Duryodhan ke jaane ke baad Krishna ne Arjun se muskuraakar poocha,

“Arjun, maine toh kaha tha ki main yudh nahi ladoonga.”

“Phir bhi tumne mujhe hi kyun chuna?”

Arjun ka Jawab

Arjun ne vinamrata se kaha,

“Prabhu, mujhe pata hai ki aap chahein toh akele hi sabko hara sakte hain.”

“Lekin mujhe aapki shakti se bhi zyada aapka saath chahiye.”

“Meri bahut purani ichchha thi ki aap mere rath ke saarathi banein.”

“Yahi meri sabse badi ichchha hai.”

Krishna muskura diye.

Woh bole,

“Arjun, tumhari ichchha zaroor poori hogi.”

“Main tumhara saarathi banunga.”

Is tarah Arjun ko duniya ka sabse bada sahara mil gaya.

Woh sena nahi, swayam Shri Krishna ko apne saath lekar khushi-khushi Yudhishthir ke paas laut aaye."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.8
        with st.expander("Section 5.1.8  Section VIII"):
            text1 = """ 
            Chapter 8 – Shalya ka Vachan aur Yudhishthir ki Chatur Yojana

Vaisampayan ji ne kaha,

Raja Shalya apni vishal sena ke saath Pandavo se milne ke liye nikal pade.

Unke paas ek poori Akshauhini sena thi.

Raaste bhar unki sena dheere-dheere aage badh rahi thi.

Itni badi sena thi ki dharti bhi unke kadmon se kaanp rahi thi."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Duryodhan ki Chaal

Duryodhan ko pata chal gaya ki Shalya Pandavo ka saath dene aa rahe hain.

Usne turant ek chaal chali.

Raaste mein har jagah shandaar aaraam ke camp banwa diye.

Wahan swadisht bhojan, peene ka paani, sundar mahal aur har tarah ki suvidha ka intezaam tha.

Lekin kahin bhi Duryodhan ka naam nahi likha tha.

Shalya ko laga,

“Yeh sab Yudhishthir ne mere swagat ke liye karwaya hai.”

Woh bahut khush ho gaye.

Shalya ka Vachan

Khush hokar Shalya bole,

“Jisne mere liye yeh sab kiya hai, main use zaroor koi bada inaam doonga.”

Tabhi Duryodhan saamne aa gaya.

Shalya sab samajh gaye.

Woh muskuraakar bole,

“Bolo Duryodhan, tum kya chahte ho?”

Duryodhan ne turant kaha,

“Bas ek vachan dijiye.”

“Yudh ke samay meri sena ka netritva kijiye.”

Shalya apna diya hua vachan todna nahi chahte the.

Unhone kaha,

“Theek hai.”

“Main tumhari baat maanunga.”

Pehle Pandavo se Milunga

Lekin Shalya ne Duryodhan se kaha,

“Sabse pehle main Yudhishthir se milunga.”

“Uske baad main tumhare paas wapas aa jaaunga.”

Duryodhan ne unhe yaad dilaya,

“Apna vachan mat bhooliyega.”

Shalya bole,

“Main apna vachan zaroor nibhaunga.”

Shalya Pandavo se Mile

Shalya Upaplavya pahunch gaye.

Pandavo ne bade prem aur samman se unka swagat kiya.

Shalya ne Yudhishthir, Bhim, Arjun, Nakul aur Sahadev ko gale lagaya.

Unhone Draupadi ka bhi haal-chaal poocha.

Yudhishthir ki Prashansa

Shalya bole,

“Beta Yudhishthir, tumne bahut bade dukh sahe hain.”

“Vanvaas aur Agyaatvaas poora karna bahut kathin tha.”

“Lekin tumne dharm ka raasta kabhi nahi chhoda.”

“Mujhe poora vishwas hai ki ab tumhe nyaay zaroor milega.”

Sachchai Bata Di

Phir Shalya ne Yudhishthir ko sab sach bata diya.

Unhone kaha,

“Raaste mein Duryodhan ne mujhe dhokhe se apni taraf kar liya.”

“Khushi mein maine use vachan de diya ki main uska saath doonga.”

Yudhishthir ki Chatur Ichchha

Yudhishthir muskuraaye aur bole,

“Mama, aapne jo vachan diya hai, woh theek hai.”

“Main bas aapse ek chhoti si madad chahta hoon.”

Shalya bole,

“Bolo beta.”

Yudhishthir ne kaha,

“Jab Karna aur Arjun ka maha yudh hoga, tab aap hi Karna ke saarathi banenge.”

“Us samay Karna ka hausla badhaane ke bajaay uska ghamand tod dijiye.”

“Uska mann kamzor kar dijiye.”

“Isse Arjun ko jeetne mein madad milegi.”

Shalya ka Vachan

Shalya bole,

“Main tumhari baat zaroor maanunga.”

“Main Karna ka saarathi banunga.”

“Lekin yudh ke dauraan usse aisi baatein kahunga ki uska hausla toot jaaye.”

“Tab Arjun ke liye usse haraana aasaan ho jaayega.”

Dhairya Rakho

Shalya ne pyaar se kaha,

“Beta, jo dukh tumne aur Draupadi ne sahe hain, unka ant ab kareeb hai.”

“Karna ki buri baatein, Dice ka dhokha, Keechak ka apmaan aur tumhare saare kasht ek din samaapt ho jaayenge.”

“Dhairya rakho.”

“Samay badalne wala hai.”

Sabke chehre par umeed ki ek nayi roshni aa gayi.

Ab yudh sirf talwaron ka nahi, buddhi aur yojana ka bhi hone wala tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.9
        with st.expander("Section 5.1.9  Section IX"):
            text1 = """ 
            Chapter 9 – Indra aur Vritrasur ki Kahani

Yudhishthir ne Raja Shalya se poocha,

“Mama, aapne kaha tha ki Devraj Indra ko bhi bahut bade dukh ka saamna karna pada tha.”

“Kripya woh kahani humein bataaiye.”

Twashtri ka Tap

Shalya bole,

“Bahut samay pehle Twashtri naam ke ek mahaan Rishi aur Dev shilpkar kathor tapasya kar rahe the.”

Unhone ek bahut shaktishaali putra ko janm diya."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Uske teen sir the.

Har sir ka alag kaam tha.

Ek sir se woh Ved padhta tha.

Doosre se Somras peeta tha.

Aur teesre se chaaron dishaon ko dekhta rehta tha.

Woh bahut tapasvi aur dharmik tha.

Indra Dar Gaye

Jab Indra ne uski tapasya aur shakti dekhi, toh woh chintit ho gaye.

Unhone socha,

“Agar yeh aur shaktishaali ban gaya, toh mera Indra ka pad chheen lega.”

Apsaraon ki Koshish

Indra ne sundar Apsaraon ko us tapasvi ke paas bheja.

Unhone nritya kiya.

Geet gaaye.

Use mohit karne ki poori koshish ki.

Lekin woh tapasvi apni tapasya se zara bhi nahi hila.

Apsaraayein haar kar wapas aa gayin.

Indra ka Kathin Faisla

Ab Indra ne doosra raasta chuna.

Unhone apna Vajra uthaya.

Aur us tapasvi par vaar kar diya.

Ek hi prahar mein woh tapasvi zameen par gir gaya.

Lekin uska tej ab bhi kam nahi hua tha.

Use dekhkar Indra bhi ghabra gaye.

Lakadhare ki Madad

Tab ek lakadhara wahan se guzar raha tha.

Indra ne usse kaha,

“Iske teenon sir kaat do.”

Lakadhare ne mana kar diya.

Woh bola,

“Yeh toh paap hoga.”

Indra bole,

“Main tumhe vardaan dunga.”

“Tum bas meri baat maan lo.”

Aakhir lakadhare ne uske teenon sir kaat diye.

Teen Pakshiyon ka Janm

Jaise hi sir alag hue,

Unmein se alag-alag pakshi nikal aaye.

Kahin se teetar nikle.

Kahin se bater.

Aur kahin se chidiyaan ud gayin.

Indra ko tab jaakar thodi shanti mili.

Twashtri ka Krodh

Jab Twashtri ko pata chala ki unke nirdosh putra ko maar diya gaya hai,

Toh woh bahut krodhit ho gaye.

Unhone kaha,

“Indra ne bahut bada anyay kiya hai.”

“Ab main uske vinaash ke liye ek mahaan Asur paida karunga.”

Vritrasur ka Janm

Twashtri ne yagya kiya.

Apni tapasya ki shakti se ek bhayankar Asur ko janm diya.

Uska naam tha Vritrasur.

Vritrasur ne poocha,

“Mujhe kya karna hai?”

Twashtri bole,

“Jaao... Indra ka vinaash karo.”

Vritrasur har pal aur bada aur shaktishaali hota gaya.

Maha Yudh

Phir Indra aur Vritrasur ke beech bhayankar yudh shuru hua.

Dono bahut shaktishaali the.

Lambe samay tak yudh chalta raha.

Ek samay aisa aaya jab Vritrasur ne Indra ko pakad liya.

Aur unhe nigal gaya.

Devta Ghabra Gaye

Sabhi Devta bahut dar gaye.

Unhone milkar ek divya shakti paida ki.

Us shakti ki wajah se Vritrasur ko zor ki jamhaai aa gayi.

Jaise hi usne muh khola,

Indra turant uske muh se baahar nikal aaye.

Yudh Phir Shuru Hua

Indra phir se lade.

Lekin is baar bhi Vritrasur bahut shaktishaali saabit hua.

Indra ko peeche hatna pada.

Sabhi Devta chintit ho gaye.

Vishnu ki Sharan

Aakhir sabhi Devta samajh gaye ki sirf apni shakti se Vritrasur ko haraana mumkin nahi hai.

Isliye sab milkar Mandarachal Parvat par gaye.

Wahan unhone Bhagwan Vishnu ka smaran kiya.

Unhe poora vishwas tha ki ab sirf Bhagwan hi unki raksha kar sakte hain."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.10
        with st.expander("Section 5.1.10  Section X"):
            text1 = """ 
            Chapter 10 – Vritrasur ka Ant aur Indra ka Pashchatap

Shalya ne kahani aage badhaate hue kaha,

Devta Vishnu ki Sharan Mein Gaye

Indra bole,

“Vritrasur itna shaktishaali ho chuka hai ki use haraana mere bas ki baat nahi rahi.”

“Ab sirf Bhagwan Vishnu hi hamaari madad kar sakte hain.”

Tab sabhi Devta aur Rishi milkar Bhagwan Vishnu ke paas gaye."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Unhone prarthana ki,

“Prabhu, humein bachaiye.”

“Sirf aap hi Vritrasur ka ant kar sakte hain.”

Vishnu ki Yojana

Bhagwan Vishnu bole,

“Main tumhari madad zaroor karunga.”

“Lekin is baar sirf bal se kaam nahi chalega.”

“Pehle Vritrasur se shaanti ki baat karo.”

“Uska vishwas jeeto.”

“Samay aane par main khud Indra ke Vajra mein apni shakti de dunga.”

Devta Vishnu ki baat maan gaye.

Shaanti ka Prastaav

Sabhi Rishi aur Devta Vritrasur ke paas gaye.

Woh bole,

“Bahut samay se yudh chal raha hai.”

“Isse poori duniya dukhi ho rahi hai.”

“Aao, hum sab milkar shaanti kar lete hain.”

Vritrasur ne poocha,

“Main Indra par bharosa kaise karun?”

Vritrasur ki Shart

Vritrasur bola,

“Main tabhi shaanti karunga jab Indra mujhe...”

Na kisi geeli cheez se maare.
Na kisi sukhi cheez se maare.
Na lakdi se.
Na patthar se.
Na kisi hathiyaar se.
Na din mein.
Na raat mein.

Rishi bole,

“Hum tumhari sab shartein maan lete hain.”

Iske baad dono ke beech kuch samay ke liye shaanti ho gayi.

Indra Mauke ki Talaash Mein

Lekin Indra ke mann mein ek hi baat chal rahi thi.

“Vritrasur ko kaise haraaya jaaye?”

Ek din shaam ke samay woh samundar ke kinaare Vritrasur ko dekhte hain.

Tab unhe achanak ek vichaar aaya.

Chatur Yojana

Indra ne dekha ki samundar ke kinaare bahut saara jhaag tha.

Unhone socha,

“Yeh na poori tarah geela hai, na sukha.”

“Abhi na din hai, na raat.”

“Isi se Vritrasur ko haraaya jaa sakta hai.”

Bhagwan Vishnu bhi us jhaag mein apni divya shakti ke saath pravesh kar gaye.

Indra ne us jhaag ko Vajra ke saath Vritrasur par phenka.

Usi pal Vritrasur ka ant ho gaya.

Sabhi Devta Khush Hue

Vritrasur ke marte hi aasman saaf ho gaya.

Thandi hawa chalne lagi.

Sabhi Devta, Gandharv aur Rishi khushi se bhar gaye.

Sabne milkar Indra ki stuti ki.

Indra ne bhi Bhagwan Vishnu ka dhanyavaad kiya.

Lekin Indra Khush Nahi The

Sab log khush the.

Lekin Indra ke mann mein shanti nahi thi.

Unhe yaad tha ki unhone pehle Twashtri ke nirdosh putra ko maara tha.

Aur Vritrasur ko bhi chaal se haraaya tha.

Isliye unhe apne karmon ka bahut pashchatap hone laga.

Indra Chhip Gaye

Paap aur dukh se pareshaan hokar Indra sabse door chale gaye.

Woh paani ke andar chhipkar rehne lage.

Kisi ko bhi unka pata nahi chala.

Sansar Mein Sankat

Indra ke bina baarish ruk gayi.

Ped-paudhe sukhne lage.

Nadiyon ka paani kam ho gaya.

Dharti par akaal jaisi sthiti ban gayi.

Devta aur Rishi bahut chintit ho gaye.

Sab sochne lage,

“Ab Devtaon ka raja kaun banega?”

Aur isi sawaal ke saath ek nayi kahani shuru hone wali thi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.11
        with st.expander("Section 5.1.11  Section XI"):
            text1 = """ 
            Chapter 11 – Nahush ka Ahankaar

Shalya ne kahani aage sunaai.

Naya Devraj Chuna Gaya

Jab Indra apne paapon ke darr se chhip gaye, tab Devta aur Rishi bahut pareshaan ho gaye.

Unhone milkar kaha,

“Humein swarg ka naya raja chahiye.”"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Sabne milkar Raja Nahush ka naam chuna.

Woh shaktishaali, dharmik aur nyaaypriya raja the.

Nahush ne Mana Kiya

Nahush bole,

“Main itna shaktishaali nahi hoon.”

“Indra hi Devtaon ke raja banne ke yogya hain.”

Lekin sabhi Devta aur Rishi bole,

“Hamari tapasya ki shakti tumhare saath hogi.”

“Tum swarg ka raaj sambhalo.”

Divya Vardaan

Devtaon ne Nahush ko ek vishesh vardaan diya.

Woh bole,

“Jo bhi tumhare saamne aayega, uski shakti tumhare andar aa jaayegi.”

“Isse tum aur bhi shaktishaali ban jaaoge.”

Nahush ne yeh zimmedaari sveekar kar li.

Aur woh naye Devraj ban gaye.

Ahankaar ki Shuruaat

Shuru mein Nahush nyaay aur dharm ke saath raaj karte rahe.

Lekin dheere-dheere unhe apni taakat aur pad ka ghamand hone laga.

Woh swarg ke sundar baagon, pahaadon aur nadiyon mein aish-o-aaraam se rehne lage.

Apsaraayein unke liye nritya karti thi.

Gandharv madhur geet gaate the.

Har taraf sukh hi sukh tha.

Nahush ki Galat Ichchha

Ek din Nahush ki nazar Indra ki patni Shachi par padi.

Unke mann mein galat vichaar aa gaya.

Woh bole,

“Ab main Devtaon ka raja hoon.”

“Toh Shachi ko bhi mere paas aana chahiye.”

Unhone apne sevakon ko aadesh diya,

“Jao, Shachi ko turant mere paas lekar aao.”

Shachi Dar Gayi

Yeh sunkar Devi Shachi bahut ghabra gayin.

Woh seedhe Devguru Brihaspati ke paas pahunchi.

Unhone haath jodkar kaha,

“Gurudev, meri raksha kijiye.”

“Aapne hamesha kaha tha ki main apne pati Indra ke saath hi rahungi.”

“Kripya apni baat ko sach kijiye.”

Brihaspati ka Bharosa

Brihaspati ji ne shaant swar mein kaha,

“Devi, bilkul mat daro.”

“Indra jaldi hi wapas aayenge.”

“Main tumhe unse zaroor milaunga.”

“Nahush tumhara kuch bhi nahi bigaad paayega.”

Shachi ko thodi himmat mili.

Nahush ka Gussa

Jab Nahush ko pata chala ki Shachi ne Brihaspati ki sharan le li hai,

Toh woh bahut krodhit ho gaya.

Uske ahankaar aur gusse ne use aur bhi andha bana diya.

Ab uske galat faislon ki wajah se uska patan shuru hone wala tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.12
        with st.expander("Section 5.1.12  Section XII"):
            text1 = """ 
Chapter 12 – Brihaspati ne Sharan Mein Aayi Shachi ki Raksha Ki

Shalya ne kahani aage sunaai.

Devtaon ne Nahush ko Samjhaya

Jab Nahush gusse aur ahankaar mein doob gaya, tab Devta aur Rishi uske paas aaye.

Woh bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
“Hey Devraj, kripya shaant ho jaiye.”

“Shachi kisi aur ki patni hain.”

“Dusre ki patni par buri nazar rakhna dharm ke viruddh hai.”

“Aap poore swarg ke raja hain.”

“Aapka kartavya sabki raksha karna hai, na ki kisi ka apmaan.”

Nahush ne Baat Nahi Maanee

Lekin Nahush par kaam aur ahankaar ka nasha chadh chuka tha.

Woh bola,

“Jab Indra ne pehle Ahalya ke saath galat kiya tha, tab tum sabne unhe kyun nahi roka?”

“Ab mujhe kyun rok rahe ho?”

“Mujhe Shachi chahiye.”

Devta samajh gaye ki Nahush samajhne ko taiyaar nahi hai.

Devta Brihaspati ke Paas Gaye

Sabhi Devta Brihaspati ji ke paas gaye.

Woh bole,

“Shachi aapki sharan mein hain.”

“Lekin Nahush ab Devraj hain.”

“Kya Shachi unhe apna pati sveekar kar sakti hain?”

Yeh sunkar Shachi ro padi.

Shachi ki Vinati

Shachi ne rote hue kaha,

“Gurudev, main Nahush ko kabhi apna pati nahi maan sakti.”

“Main aapki sharan mein aayi hoon.”

“Kripya meri raksha kijiye.”

Brihaspati ka Dridh Sankalp

Brihaspati ji bole,

“Jo vyakti meri sharan mein aata hai, main uska saath kabhi nahi chhodta.”

“Chahe kuch bhi ho jaaye, main tumhe Nahush ke hawaale nahi karunga.”

Phir unhone ek bada dharm ka niyam bataya.

Sharan Mein Aaye Vyakti ki Raksha

Brihaspati bole,

“Jo kisi dare hue aur sharan maangne wale vyakti ko uske dushman ke hawaale kar deta hai, uska kabhi bhala nahi hota.”

“Uske achchhe kaam safal nahi hote.”

“Uska punya kam ho jaata hai.”

“Isliye main Shachi ko kabhi nahi chhodunga.”

Ek Buddhimaan Yojana

Devta bole,

“Toh ab kya kiya jaaye?”

Brihaspati ne shaant swar mein kaha,

“Shachi Nahush se thoda samay maang le.”

“Samay bahut badi shakti hoti hai.”

“Ho sakta hai isi dauraan koi naya raasta mil jaaye.”

Sabhi Devta ko yeh yojana pasand aa gayi.

Shachi Nahush ke Paas Gayi

Devtaon ne Shachi ko himmat di.

Woh bole,

“Dhairya rakho.”

“Nahush ka ahankaar hi uske patan ka kaaran banega.”

“Jaldi hi Indra apna rajya wapas paayenge.”

Yeh sunkar Shachi himmat jutakar Nahush ke paas gayi.

Nahush ne jaise hi unhe dekha, woh bahut khush ho gaya.

Use laga ki ab uski ichchha poori hone wali hai.

Lekin use bilkul bhi andaaza nahi tha ki yahi mulaqat uske patan ki shuruaat banne wali hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.13
        with st.expander("Section 5.1.13  Section XIII"):
            text1 = """ 
Chapter 13 – Shachi ki Buddhi aur Indra ki Talaash

Shalya ne kahani aage sunaai.

Nahush ka Prastaav

Nahush ne Shachi ko dekhkar kaha,

“Ab main teenon lokon ka Devraj hoon.”

“Tum mujhe apna pati sveekar kar lo.”

Yeh sunkar Shachi bahut dar gayin."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Unka sharir kaampne laga.

Lekin unhone himmat nahi haari.

Shachi ne Samay Maanga

Shachi ne haath jodkar shaant swar mein kaha,

“Hey Devraj, pehle mujhe yeh pata kar lene dijiye ki Indra kahaan hain.”

“Agar mujhe unka koi pata na mila, tab main aapke paas laut aaungi.”

Nahush apne ahankaar mein andha ho chuka tha.

Usne turant haan kar di.

Woh bola,

“Theek hai.”

“Jao, lekin apna vachan yaad rakhna.”

Shachi wahan se turant Brihaspati ke paas laut gayin.

Devta Vishnu ke Paas Gaye

Udhar sabhi Devta fir se Bhagwan Vishnu ke paas gaye.

Woh bole,

“Prabhu, Indra Brahmahatya ke paap se dukhi hain.”

“Kripya unhe is paap se mukt karne ka upaay bataaiye.”

Vishnu ka Upaay

Bhagwan Vishnu bole,

“Indra mere liye Ashwamedh Yagya karein.”

“Is pavitra yagya se unka paap door ho jaayega.”

“Uske baad woh fir se Devraj ban sakenge.”

“Dhairya rakho.”

“Nahush ka ahankaar hi uske vinaash ka kaaran banega.”

Ashwamedh Yagya

Devta aur Rishi Indra ke paas gaye.

Wahan unhone Ashwamedh Yagya karvaaya.

Yagya ke baad Indra ka paap halka hone laga.

Kahte hain ki Indra ne apna paap alag-alag jagahon mein baant diya.

Pedon ko.

Nadiyon ko.

Pahaadon ko.

Dharti ko.

Aur stree jaati ko bhi uska ek hissa mila.

Iske baad Indra ka mann shaant hone laga.

Indra Fir Bhi Chhipe Rahe

Lekin Nahush ab bhi bahut shaktishaali tha.

Uske paas Rishiyon ka diya hua vardaan tha.

Isliye Indra abhi bhi saamne aane ki himmat nahi kar paaye.

Woh chupkar sahi samay ka intezaar karte rahe.

Shachi ki Prarthana

Shachi bahut dukhi thi.

Unhone Bhagwan se prarthana ki,

“Agar maine kabhi sachcha dharm nibhaya hai...”

“Agar main hamesha apne pati ke prati nishthavaan rahi hoon...”

“Toh meri pavitrata ki raksha ho.”

“Kripya mujhe Indra ka pata bataaiye.”

Devi Raatri ki Pooja

Shachi ne pavitra mann se Devi Raatri ki pooja ki.

Phir unhone prarthana ki,

“Hey Devi, mujhe bataaiye ki mere pati Indra kahaan hain.”

“Sachchai ki shakti se mujhe un tak pahunchne ka raasta dikhaiye.”

Ab Shachi ki sachchi bhakti aur dhairya unhe Indra tak pahunchane wale the.

Aur Nahush ka ahankaar dheere-dheere uske ant ki taraf badh raha tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.14
        with st.expander("Section 5.1.14  Section XIV"):
            text1 = """ 
Chapter 14 – Shachi ne Indra ko Dhoondh Nikala

Shalya ne kahani aage sunaai.

Divya Devi ka Prakat Hona

Shachi ki sachchi prarthana se Divination (Daivi Margdarshan ki Devi) unke saamne prakat hui.

Shachi ne vinamrata se poochha,

“Aap kaun hain?”

Devi ka Uttar"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Devi boli,

“Main Divination hoon.”

“Tum satyavaan ho.”

“Tum apne pati ke prati poori tarah nishthavaan ho.”

“Isi pavitrata ke kaaran main tumhare saamne prakat hui hoon.”

“Main tumhe Indra tak le chalungi.”

Indra ki Talaash

Devi ke peeche-peeche Shachi chal padi.

Dono ne—

swarg ke sundar van paar kiye,
bahut se pahaad paar kiye,
Himalaya ke uttar bhaag tak pahunchin,
phir ek vishaal samudra paar kiya.

Samudra ke beech ek sundar dweep tha.

Us dweep par ek bahut bada divya sarovar tha.

Sarovar rang-birange kamalon se bhara hua tha.

Har taraf madhumakkhiyan gunj rahi thi.

Bahut hi adbhut aur shaant drishya tha.

Safed Kamal ka Rahasya

Us bade sarovar ke beech ek vishaal safed kamal tha.

Us kamal ke mote tane (stem) ke andar Devi Shachi ko lekar gayi.

Wahin...

Bahut chhote roop mein...

Indra chhupe hue the.

Brahmahatya ke paap aur Nahush ke vardaan ke darr se woh wahin chhipkar samay ka intezaar kar rahe the.

Shachi aur Devi ne bhi apna roop chhota kar liya aur kamal ke andar pravesh kiya.

Shachi ne Indra ki Stuti Ki

Apne pati ko dekhkar Shachi ne unki purani veerta aur mahima ka smaran karte hue unki stuti ki.

Indra ne aankhen kholi aur poochha,

“Tum yahan kaise pahunchi?”

“Aur tumhe mera pata kaise chala?”

Shachi ne Sab Kuch Bataya

Shachi boli,

“Nahush ab teenon lokon ka raja ban gaya hai.”

“Uska ahankaar bahut badh gaya hai.”

“Usne mujhe apni patni banne ka aadesh diya hai.”

“Maine usse thoda samay maang liya.”

“Lekin woh jaldi mujhe apne paas bulaayega.”

“Agar aap meri raksha nahi karenge, toh woh mujhe zabardasti apne adhikaar mein kar lega.”

Shachi ki Vinati

Shachi ne haath jodkar kaha,

“Hey Vritrasur ke vijeta!”

“Ab aur mat chhipiye.”

“Apni purani shakti fir se dhaaran kijiye.”

“Nahush jaise dusht aur ahankaari vyakti ka vinaash kijiye.”

“Fir se Devtaon ke raja baniye.”

Yahin se kahani ek naye mod par pahunchti hai. Ab Indra ko Nahush ke vardaan ka tod dhoondhna tha, aur Shachi ki buddhi hi Nahush ke patan ka sabse bada kaaran banne wali thi."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.15
        with st.expander("Section 5.1.15  Section XV"):
            text1 = """ 
Chapter 15 – Indra ki Chatur Yojana aur Nahush ka Ahankaar

Shalya ne kahani aage sunaai.

Indra ki Yojana

Shachi ki baat sunkar Indra bole,

“Abhi Nahush mujhse zyada shaktishaali hai.”

“Use Rishiyon ki tapasya aur vardaan ka bal mila hua hai.”

“Is samay seedha yuddh karna theek nahi hoga.”"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
“Isliye humein buddhi se kaam lena hoga.”

Phir Indra ne Shachi ko ek gupt yojana bataai.

Gupt Sandesh

Indra bole,

“Tum Nahush ke paas jao.”

“Usse kehna ki agar woh mujhe paana chahta hai, toh ek anokhi sawaari par mere paas aaye.”

“Uski palki ko ghode ya haathi nahi...”

“Balki swayam Maharishi apne kandhon par utha kar laayein.”

“Yeh baat kisi ko mat batana.”

Shachi ne haan kar di.

Shachi Nahush ke Paas

Shachi fir Nahush ke paas pahunchi.

Nahush unhe dekhkar bahut khush hua.

Woh bola,

“Tum jo kahogi, main wahi karunga.”

“Main tumhare liye kuch bhi karne ko taiyaar hoon.”

Shachi ki Maang

Shachi boli,

“Indra ke paas haathi, ghode aur rath the.”

“Lekin main chahti hoon ki aap un sabse alag aur mahaan dikhai dein.”

“Main chahti hoon ki Maharishi swayam aapki palki uthakar mere paas laayein.”

“Aisa vaahan na Vishnu ke paas tha, na Shiv ke paas aur na kisi Asur ke paas.”

“Tab main aapko apna pati maan loongi.”

Ahankaar Andha Kar Deta Hai

Nahush ko laga ki Shachi uski mahima se prabhavit ho gayi hai.

Uska ahankaar aur badh gaya.

Woh bola,

“Bahut achchhi baat kahi tumne.”

“Sach mein, sirf main hi itna mahaan hoon ki Rishi mujhe uthakar le jaayen.”

“Main teenon kaal ka swaami hoon.”

“Mujhse bada koi nahi.”

“Main tumhari ichchha zaroor poori karunga.”

Maharishiyon se Palki Uthvaana

Apne ghamand mein andha hokar Nahush ne bade-bade Maharishiyon ko hukm diya ki woh uski palki uthayein.

Yahi uski sabse badi galti thi.

Dharm aur tapasya ke prateek Rishiyon ko apna naukar samajhna uske vinaash ki shuruaat ban gaya.

Shachi Fir Brihaspati ke Paas

Udhar Shachi Brihaspati ji ke paas laut aayi.

Unhone kaha,

“Ab samay bahut kam bacha hai.”

“Kripya jaldi Indra ko dhoondhiye.”

Brihaspati ka Vishwas

Brihaspati ji bole,

“Darne ki zarurat nahi.”

“Nahush ka ant ab nishchit hai.”

“Usne Rishiyon ko palki uthwaakar bahut bada adharm kiya hai.”

“Uska ahankaar hi uska vinaash karega.”

Agni ko Indra ki Talaash

Brihaspati ne ek yagya kiya.

Usmein Agni Dev ko aadesh diya,

“Jao, Indra ko dhoondhkar lao.”

Agni Dev ne turant ek adbhut roop dhaaran kiya aur poori srishti mein Indra ko dhoondhne nikal pade.

Unhone—

pahaad,
van,
dharti,
aakaash,

sab jagah khoja.

Lekin Indra kahin nahi mile.

Phir Agni bole,

“Ab sirf jal baaki hai.”

“Lekin paani mein pravesh karna mere liye kathin hai, kyunki paani mujhe bujha deta hai.”

Brihaspati ne unhe phir bhi paani mein pravesh karne ko kaha.

Yahin par kahani agle adhyay ki aur badhti hai, jahan Nahush ka ahankaar apne charam par pahunchta hai aur uske patan ka antim charan shuru hota hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

            # Section 5.1.16
        with st.expander("Section 5.1.16  Section XVI"):
            text1 = """ 
            Chapter 16 – Agni ne Indra ko Dhoondha aur Devtaon ne Yuddh ki Taiyaari Ki

Shalya ne kahani aage sunaai.

Brihaspati ne Agni ko Himmat Di

Agni Dev paani mein jaane se hichkichaa rahe the.

Tab Brihaspati bole,

“Hey Agni, tum sabhi Devtaon ka mukh ho.”

“Sabhi yagyon ki ahuti tumhare dwaara hi Devtaon tak pahunchti hai.”

“Tum teenon lokon ke saakshi ho.”

“Tumhare bina yagya sambhav nahi.”

“Tum hi srishti ka aarambh bhi ho aur ant bhi.”"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
“Isliye bina dare paani mein pravesh karo.”

“Main Vedon ke mantron se tumhari raksha karunga.”

Agni Paani Mein Gaye

Brihaspati ki stuti sunkar Agni prasann ho gaye.

Unhone kaha,

“Main Indra ko zaroor dhoondh nikaalunga.”

Phir Agni samudron, talaabon aur sabhi jalashayon mein pravesh kar gaye.

Aakhirkaar...

Ek bade kamal ke tane ke andar...

Unhone Indra ko chhote roop mein chhipa hua dekh liya.

Turant lautkar Agni ne Brihaspati ko sab bata diya.

Devta Indra ke Paas Pahunche

Brihaspati sabhi Devtaon aur Rishiyon ko lekar Indra ke paas gaye.

Unhone Indra ki purani veerta yaad dilaai.

Woh bole,

“Aapne Namuchi ko maara.”

“Aapne Vala aur Shambara jaise Asuron ko haraaya.”

“Aapne Vritrasur ka vinaash kiya.”

“Aap hi Devtaon ke sachche raja hain.”

“Ab fir se apni shakti dhaaran kijiye.”

Indra ne Shakti Prapt Ki

Devtaon ki prerna se Indra ka hausla badhne laga.

Unka asli roop aur tej dheere-dheere laut aaya.

Phir Indra ne poochha,

“Ab aur kya samasya hai?”

“Vritrasur toh mar chuka hai.”

Brihaspati ne Nahush ki Khabar Di

Brihaspati bole,

“Ab ek nayi samasya hai.”

“Raja Nahush Devtaon ka raja ban gaya hai.”

“Use sabhi Devtaon aur Rishiyon ne apni tapasya ka bal de diya hai.”

“Ab woh bahut shaktishaali ho gaya hai.”

“Uski aankhon mein itna tej hai ki jis par nazar daalta hai, uski shakti kam ho jaati hai.”

“Sabhi Devta usse dar kar chhupe hue hain.”

Lokpal Devta Aaye

Itne mein chaar bade Devta bhi wahan aa gaye—

Kubera (dhan ke devta),
Yama,
Varuna,
aur Soma.

Unhone Indra ko dekhkar khushi vyakt ki.

Phir Indra ne kaha,

“Ab humein milkar Nahush ko haraana hoga.”

Devtaon ki Shart

Devta bole,

“Nahush bahut bhayaanak hai.”

“Hum usse darte hain.”

“Lekin agar aap uska vinaash kar denge, toh hum phir se apne-apne adhikaar sambhaal lenge.”

Indra ne sabko saath aane ko kaha.

Agni ka Vardaan

Agni Dev bole,

“Main bhi aapki madad karunga.”

“Lekin mujhe bhi yagyon mein apna hissa chahiye.”

Indra bole,

“Aaj se bade yagyon mein tumhara bhi hissa hoga.”

“Kai yagyon mein Indra aur Agni ki saanjhi ahuti di jaayegi.”

Devtaon ko Unke Adhikaar Mile

Iske baad Indra ne vibhinna Devtaon ko unke adhikaar fir se diye—

Kubera ko Yakshon aur sampatti ka swaami banaya.
Yama ko Pitrlok ka adhikaar diya.
Varuna ko sabhi jalon ka adhipati banaya.

Ab sabhi Devta ekjut ho chuke the.

Agla kadam tha—Nahush ke ahankaar ka ant karna. Yahi uske patan ka antim charan shuru hone wala tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.17
        with st.expander("Section 5.1.17  Section XVII"):
            text1 = """ 
            Chapter 17 – Nahush ka Ahankaar aur Uska Patan

Shalya ne kahani ka agla bhaag sunaaya.

Agastya Rishi ka Aagaman

Jab Indra aur sabhi Devta milkar soch rahe the ki Nahush ko kaise haraaya jaaye,

Tab mahaan Rishi Agastya wahan aaye.

Unhone Indra ko dekhkar kaha,

“Bahut shubh hai ki Vritra aur anya Asuron ka vinaash ho chuka hai.”

“Aur sabse bada sukh yeh hai ki Nahush swarg ke singhasan se gir chuka hai.”"""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Indra ka Prashn

Indra ne vinamrata se Agastya Rishi ka satkaar kiya aur poochha,

“Hey Maharishi, kripya bataaiye, Nahush swarg se kaise gira?”

Agastya ne Ghatna Sunaai

Agastya bole,

“Jab Nahush apni palki mein baithkar ghoom raha tha, tab uski palki ko hum jaise Maharishi utha rahe the.”

Raaste mein Rishiyon ne usse ek dharmik prashn poochha.

Unhone kaha,

“Vedon mein jo gaayon ke pavitra sanskaar ke samay mantra bole jaate hain, kya tum unhe satya maante ho?”

Nahush ki Sabse Badi Galti

Ahankaar se andha ho chuka Nahush bola,

“Nahi.”

“Woh mantra satya nahi hain.”

Yeh sunkar sabhi Rishi chauk gaye.

Unhone kaha,

“Tum adharm ki aur badh rahe ho.”

“Mahaan Rishiyon ne in mantron ko hamesha satya maana hai.”

Lekin Nahush ne kisi ki baat nahi maani.

Agastya ka Apmaan

Ghamand mein choor Nahush ne jaldi chalne ke liye...

Rishi Agastya ke sir par apne pair se laat maar di.

Yahi uski sabse badi bhool thi.

Ek tapasvi Maharishi ka apmaan karna uske vinaash ka kaaran ban gaya.

Agastya ka Shraap

Agastya Rishi krodhit ho gaye.

Unhone kaha,

“Tumne Vedon ka apmaan kiya.”

“Tumne Maharishiyon ko apna naukar bana diya.”

“Aur tumne mere sir par pair rakha.”

“Isliye tumhara saara tej aur shakti chhin jaayegi.”

“Tum swarg se gir jaaoge.”

“Das hazaar varsh tak tum dharti par ek vishaal saanp ke roop mein bhatakte rahoge.”

“Uske baad hi tumhe fir se swarg lautne ka avsar milega.”

Jaise hi shraap diya gaya...

Nahush ka saara tej samaapt ho gaya.

Woh swarg se seedha dharti par gir pada.

Aur ek vishaal ajgar (python/saanp) ban gaya.

Indra ki Wapasi

Agastya ne Indra se kaha,

“Ab swarg wapas jaaiye.”

“Teenon lokon ki raksha kijiye.”

“Apne man aur indriyon par niyantran rakhiye.”

“Dharm ke saath shaasan kijiye.”

Sabhi Lokon Mein Khushi

Nahush ke patan ki khabar sunkar—

Devta,
Rishi,
Pitra,
Yaksha,
Gandharva,
Naag,
Rakshas,
Apsaraayein,

sabhi bahut prasann hue.

Nadiyan, pahaad, samudra aur prakriti bhi maano khushi manaane lagi.

Sabhi bole,

“Bahut shubh hua!”

“Indra fir se Devraj ban gaye.”

“Aur ahankaari Nahush ko uske karmon ka phal mil gaya.”

Is Kahani ka Sandesh

Is adhyay ka sabse bada sandesh hai:

Ahankaar sabse shaktishaali vyakti ko bhi gira deta hai.
Rishi, Guru aur dharm ka apmaan vinaash ka kaaran banta hai.
Shakti tabhi tikti hai jab uske saath vinamrata aur dharm ho.
Buddhi aur dhairya (jaise Shachi ne dikhaya) kai baar bal se bhi adhik shaktishaali hote hain."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.18
        with st.expander("Section 5.1.18  Section XVIII"):
            text1 = """ 
Chapter 18 – Indra ki Vijay aur Yudhishthira ko Prerna

Shalya ne apni kahani samaapt karte hue kaha.

Indra Fir Devraj Bane

Nahush ke patan ke baad Indra apne divya haathi Airavata par savaar hue.

Unke saath the—

Agni,
Brihaspati,
Yama,
Varuna,
Kubera,

aur anek Devta, Gandharv aur Apsaraayein."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Sabne milkar Indra ka swagat kiya.

Indra fir se Devtaon ke raja ban gaye.

Aur Shachi bhi unse fir mil gayin.

Is tarah Indra aur Shachi ka punarmilan hua.

Indra ka Nyaaypoorn Shaasan

Indra ne fir se dharm ke anusaar teenon lokon ka shaasan shuru kiya.

Sab jagah shaanti aur vyavastha laut aayi.

Atharvangiras ko Vardaan

Iske baad Maharishi Angiras aaye aur Atharva Ved ke mantron se Indra ki stuti ki.

Indra bahut prasann hue.

Unhone vardaan diya,

“Aaj se tum Atharvangiras ke naam se prasiddh hoge.”

“Tumhe yagyon mein bhi hissa milega.”

Shalya ne Yudhishthira ko Samjhaya

Phir Shalya bole,

“Hey Yudhishthira, dekho.”

“Indra jaise mahaan Devta ko bhi dukh aur vanvaas jaisa samay dekhna pada.”

“Unhe bhi kuch samay tak chhipkar rehna pada.”

“Lekin ant mein dharm ki hi jeet hui.”

“Isi tarah tumne bhi Draupadi aur apne bhaiyon ke saath bahut kasht sahe hain.”

“Lekin tum bhi apna rajya wapas paoge.”

Duryodhana aur Karna ka Ant

Shalya ne aage kaha,

“Jaise Nahush apne ahankaar ke kaaran gira...”

“Waise hi Duryodhana, Karna aur unke dusht saathi bhi jaldi vinaash ko praapt honge.”

“Uske baad tum aur tumhare bhai poori dharti par dharm ke saath raaj karoge.”

Is Kahani ka Mahatva

Shalya bole,

“Indra ki vijay ki yeh kahani bahut pavitra hai.”

“Jo raja yuddh se pehle is kahani ko shraddha se sunta ya padhta hai, uske liye yeh shubh maani gayi hai.”

Isse—

paapon ka naash hota hai,
shatruon par vijay milti hai,
dirgh aayu milti hai,
santaan ka sukh milta hai,
aur is lok aur parlok dono mein mangal hota hai.
Yudhishthira ki Vinati

Yeh kahani sunkar Yudhishthira ko nayi himmat mili.

Unhone Shalya se kaha,

“Jab Karna aur Arjuna ka antim yuddh hoga...”

“Tab aap Karna ke saarathi honge.”

“Us samay kripya Arjuna ki veerta ka baar-baar varnan karke Karna ka hausla tod dijiye.”

Shalya ka Vachan

Shalya bole,

“Jaise tum kahoge, main waise hi karunga.”

“Main Karna ka saarathi banunga.”

“Lekin avsar aane par uska utsaah kam karunga aur tumhari vijay mein sahayata karunga.”

Agle Parv ki Taiyaari

Iske baad Shalya ne Pandavon se vida li.

Woh apni sena ke saath Duryodhana ke shivir ki aur chal diye.

Is prakar Indra ki kahani samaapt hoti hai, aur Mahabharat ka kendr phir se Kurukshetra ke aane wale mahaayuddh par aa jaata hai, jahan shaanti ki aakhri koshishon ke baad itihaas ka sabse mahaan yuddh aarambh hone wala hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.19
        with st.expander("Section 5.1.19  Section XIX"):
            text1 = """ 
Chapter 19 – Dono Pakshon ki Sena ka Sangrah

Is adhyay mein Kurukshetra yuddh se pehle dono paksh apni-apni sena ikatthi karte hain.

Pandavon ki Sena

Sabse pehle Satyaki (Yuyudhana), Yadava veer, ek poori 1 Akshauhini sena lekar Yudhishthira ke paas aaye.

Unki sena mein the:

Padati (infantry)
Rath
Ghode
Haathi

Aur har prakar ke shreshth hathiyaar—

Talwar
Gada
Barchha
Bhala
Dhanush-baan
Kulhaadi
Dand
Chakra
Chhure

Sena dekhne mein aisi lag rahi thi jaise bijliyon se ghire hue baadal."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Phir ek-ek karke aur raja bhi Pandavon ke saath judte gaye.

Pandavon ke mukhya sahayak
Satyaki — 1 Akshauhini
Dhrishtaketu — 1 Akshauhini
Jayatsena — 1 Akshauhini
Pandya — Dakshin Bharat se sena
Drupada
Virata
Pahaadi raja aur anya mitra
Pandavon ki Kul Sena

7 Akshauhini

Sabhi yuddh ke liye utsuk the.

Kauravon ki Sena

Udhar Duryodhana ne bhi lagbhag poore Bharat ke rajaon ko apni taraf kar liya.

Kauravon ke mukhya sahayak
Bhagadatta — 1 Akshauhini
Bhurishravas
Shalya — 1 Akshauhini
Kritavarma — 1 Akshauhini
Jayadratha — 1 Akshauhini
Sudakshina — 1 Akshauhini
Nila
Avanti ke do raja
Kekaya ke paanch rajkumar
Aur kai anya deshon ki sena

Inmein—

Chini (China kshetra)
Kirata
Shaka
Yavana
Kamboja

jaise vibhinna janajaatiyon ke yoddha bhi shaamil the.

Kauravon ki Kul Sena

11 Akshauhini

Yeh Pandavon se kaafi badi sena thi.

Sena Itni Badi Thi...

Duryodhana ki sena itni vishaal thi ki Hastinapur mein uske liye jagah hi nahi bachi.

Isliye sena ko kai kshetron mein phaila diya gaya:

Kurujangala
Panchanad (Punjab)
Rohitaka
Ahichatra
Ganga ke kinaare
Yamuna ke aas-paas ke pahaadi ilaake
Aur anya vishaal maidaan

Poora kshetra sainikon, haathiyon, ghodon aur rathon se bhar gaya tha.

Sena ki Tulna
Paksh	Akshauhini
Pandav	7
Kaurav	11
Is Adhyay ka Mukhya Sandesh
Dono pakshon ne Bharat ke lagbhag sabhi bade rajaon ko apni taraf kar liya.
Sankhya ke hisaab se Kauravon ki sena kaafi badi thi (11 vs 7 Akshauhini).
Lekin Pandavon ke paas Arjuna, Bhima, Krishna aur anya mahan yoddha the, jabki Kaurav sankhya-bal par adhik nirbhar the.
Ab dono senaen taiyaar thi, aur Kurukshetra ka mahaayuddh shuru hone ke bilkul kareeb tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.20
        with st.expander("Section 5.1.20  Section XX"):
            text1 = """ 
Chapter 20 – Drupada ke Purohit ka Hastinapur Mein Shaanti Sandesh

Yeh adhyay Mahabharat ke sabse mahatvapurn shaanti-prayas (peace negotiation) mein se ek hai.

Drupada ke Purohit Hastinapur Pahunche

Raja Drupada ke purohit Hastinapur pahunche.

Unka svaagat kiya—

Dhritarashtra
Bhishma
Vidura

Sabse pehle unhone Pandavon ki kushalta bataai aur Kauravon ka haal-chaal poochha.

Uske baad unhone sabha mein apna sandesh rakha."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Unka Pehla Tark – Rajya Dono Bhaiyon Ka Tha

Purohit bole,

“Dhritarashtra aur Pandu dono ek hi pita ke putra the.”

“Toh pita ki sampatti par dono ka barabar adhikaar tha.”

“Toh phir Pandavon ko unka hissa kyun nahi mila?”

Kauravon ke Anyay Yaad Dilaye

Unhone ek-ek karke Kauravon ke anyaay ginaaye.

1. Rajya Cheen Liya

Pandavon ko unke pita ka hissa nahi diya gaya.

2. Unhe Maarne ki Koshish Ki

Kai baar unhe chhal aur saazish se maarne ki koshish hui.

Lekin unki aayu baaki thi, isliye ve bach gaye.

3. Apni Mehnat se Bana Rajya bhi Cheen Liya

Pandavon ne apni veerta se Indraprastha basaya.

Lekin Shakuni ke chhal se unka rajya chheen liya gaya.

Dhritarashtra ne bhi ise rokne ki koshish nahi ki.

4. Vanvaas aur Agyatvaas

Pandavon ne—

12 saal vanvaas
1 saal agyatvaas

poori imaandaari se poora kiya.

5. Draupadi ka Apmaan

Sabha mein Draupadi ka apmaan hua.

Pandav sab kuch sehkar bhi apni pratigya nibhaate rahe.

6. Virat Nagar Mein Kasht

Agyatvaas ke dauraan bhi unhone bahut apmaan aur kasht sahe.

Phir bhi dharm ka maarg nahi chhoda.

Phir Bhi Pandav Yuddh Nahi Chahte

Purohit bole,

“In sab anyaayon ke baad bhi Pandav badla nahi maang rahe.”

“Ve sirf apna haq chahte hain.”

“Ve poori duniya ko yuddh mein jhonkna nahi chahte.”

“Ve shaanti chahte hain.”

Lekin Yuddh Hua To...

Purohit ne chetaavni bhi di.

Unhone kaha,

“Pandav kamzor nahi hain.”

Unke paas—

7 Akshauhini sena taiyaar khadi hai.

Aur unke saath mahaan yoddha hain.

Jaise—

Satyaki
Bhima
Nakula
Sahadeva
Sabse Badi Shakti

Phir unhone kaha,

“Tumhari 11 Akshauhini sena ek taraf hai...”

“Lekin doosri taraf ek hi Arjuna bahut bhaari hai.”

Aur usse bhi bada bal hai—

Krishna ki buddhi aur maargdarshan.

Unhone prashn kiya,

“Aakhir kaun hoga jo Arjuna ki veerta aur Krishna ki neeti ke saamne tik sake?”

Antim Sandesh

Purohit ne sabha se kaha,

“Jo nyaay ke anusaar Pandavon ka hai, woh unhe wapas de dijiye.”

“Abhi bhi samay hai.”

“Shaanti ka avsar haath se mat jaane dijiye.”

Is Adhyay ka Mukhya Sandesh
Pandavon ne apna poora vanvaas aur agyatvaas dharm ke anusaar poora kiya.
Unka rajya unka adhikaar tha.
Ve yuddh nahi, nyaay aur shaanti chahte the.
Lekin agar shaanti na mili, toh Arjuna aur Krishna ke netritva mein ve yuddh ke liye poori tarah taiyaar the.
Yeh Udyoga Parva ki pehli aadhikarik shaanti-varta hai, jahan Pandav apna nyaaypoorn daava vinamrata se rakhte hain."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.21
        with st.expander("Section 5.1.21  Section XXI"):
            text1 = """ 
            Chapter 21 – Bhishma ne Pandavon ke Adhikaar ko Svikar Kiya, Karna ne Yuddh ka Paksh Liya

Yeh adhyay Drupada ke purohit ke shaanti sandesh ke baad Hastinapur ki sabha mein hui pratikriya ko darshata hai.

Bhishma ne Purohit ka Sammaan Kiya

Bhishma ne purohit ka aadar karte hue kaha,

"Yeh bahut shubh hai ki Pandav Krishna ke saath surakshit hain."

"Yeh bhi achha hai ki unhone shaktishaali mitra prapt kiye hain."

"Sabse adhik prasannata ki baat yeh hai ki ve apne hi bandhu Kauravon ke saath shaanti chahte hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Bhishma ne Pandavon ka Haq Svikar Kiya

Bhishma ne spasht roop se kaha,

"Tumne jo kaha hai, vah satya hai."

"Haan, tumhare shabd kathor hain, lekin sachchai par aadharit hain."

Unhone svikaar kiya ki—

Pandavon ne Hastinapur aur van mein bahut kasht sahe.
Unhone apni pratigya poori imaandari se nibhayi.
Dharm aur kanoon ke anusaar unka pita ka rajya unka hi adhikaar hai.
Arjuna ki Apar Shakti

Bhishma ne sabha mein Arjuna ki khulkar prashansa ki.

Unhone kaha,

"Arjuna mahaan dhanurdhar aur ati shreshth maharathi hai."

"Uska saamna yuddh mein kaun kar sakta hai?"

"Devraj Indra bhi uska saamna karne mein kathinai mehsoos karenge."

"Mere vichaar se Arjuna teenon lokon ka saamna karne ki kshamata rakhta hai."

Karna ne Bhishma ki Baat Kaati

Bhishma ki baat chal hi rahi thi ki Karna krodhit hokar beech mein bol pada.

Usne kaha,

"Yeh baatein sabko pehle se pata hain."

"Inhe baar-baar dohraane ka kya laabh?"

Karna ka Tark

Karna ne kaha,

Shakuni ne niyam ke anusaar paason mein jeet haasil ki thi.
Yudhishthira ne swayam vanvaas ki shart sveekar ki thi.
Ab Panchal aur Matsya ki sena dekhkar ve apna rajya wapas maang rahe hain.

Usne kaha,

"Agar unhe rajya chahiye, to pehle poori shart poori karni chahiye."

"Uske baad ve Duryodhana ke adheen shaanti se reh sakte hain."

Aur agar ve yuddh chunte hain,

"Toh ranbhoomi mein Kauravon ka saamna karte samay meri baat yaad rakhenge."

Bhishma ne Karna ko Daant Diya

Bhishma ne turant Karna ko rokte hue kaha,

"Hey Radheya, itna ghamand mat karo."

"Kya tum bhool gaye jab Arjuna ne akela hi chhah mahaan maharathiyon ko parajit kar diya tha?"

Bhishma ne sabha ko chetaavni di,

"Agar hum is Brahman (Drupada ke purohit) ki baat nahi maanenge, to nishchit roop se Arjuna ke haathon yuddh mein vinaash ho jaayega."

Dhritarashtra ne Beech-Bachav Kiya

Tab Dhritarashtra ne—

Bhishma ko shaant kiya,
Karna ko daanta,
aur kaha,

"Bhishma ki baat hum sab ke hit mein hai."

"Lekin antim nirnay lene se pehle main Pandavon ke paas apna doot bhejunga."

Sanjaya ko Doot Banaaya Gaya

Dhritarashtra ne Drupada ke purohit ka samman kiya aur unhe vaapas bhej diya.

Uske baad usne apne vishwas-paatra Sanjaya ko bulaya.

Usne nishchay kiya ki Sanjaya Pandavon ke paas jaakar shaanti ka sandesh pahunchayega.

Yahin se Mahabharat ki prasiddh Sanjaya Shanti-Doot Yatra ka aarambh hota hai.

Is Adhyay ka Mukhya Sandesh
Bhishma ne khule roop se maana ki Pandav apne pita ke rajya ke vaastavik adhikaari hain.
Unhone Arjuna ko lagbhag ajeya yoddha bataya.
Karna ne Duryodhana ka paksh lekar Pandavon ki maang ka virodh kiya aur yuddh ki baat ki.
Bhishma ne Karna ke ghamand ko yaad dilaya ki Arjuna pehle bhi akela kai maharathiyon ko hara chuka hai.
Dhritarashtra ne turant yuddh ka nirnay na lekar Sanjaya ko shaanti-varta ke liye Pandavon ke paas bhejne ka faisla kiya."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.22
        with st.expander("Section 5.1.22  Section XXII"):
            text1 = """ 
Chapter 22 – Dhritarashtra ne Sanjaya ko Shaanti Sandesh ke Saath Pandavon ke Paas Bheja

Yeh adhyay dikhata hai ki Dhritarashtra ko andar hi andar Pandavon ki shakti aur apne putra Duryodhana ki zid ka poora ehsaas tha. Isliye usne apne vishwas-paatra Sanjaya ko Pandavon ke paas sandesh lekar bhejne ka nirnay liya.

Dhritarashtra ne Sanjaya ko Aadesh Diya

Dhritarashtra bola,

"Pandav Upaplavya pahunch chuke hain."

"Jao aur unka haal-chaal poochho."

Yudhishthira se kehna,

"Tum log bahut kasht uthaakar vanvaas se surakshit laut aaye, yeh hamare liye khushi ki baat hai." """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Pandavon ki Prashansa

Dhritarashtra ne svikaar kiya,

"Pandav kabhi jhooth nahi bolte."

"Maine unke vyavahaar mein kabhi koi dosh nahi dekha."

Unhone kaha ki Pandav—

hamesha dharm ka paalan karte hain,
apni mehnat se rajya jeete the,
badon ka samman karte the,
kabhi ahankari nahi bane,
sukh-dukh mein samaan rehte hain,
mitron ka hamesha saath dete hain.
Duryodhana aur Karna par Afsos

Dhritarashtra ne dukh ke saath kaha,

"Kuru vansh mein sirf do log hi Pandavon se dwesh rakhte hain—

Duryodhana
Karna."

Unhone maana ki in dono ki zid hi sab vinash ka kaaran ban rahi hai.

Pandavon ki Sena ka Dar

Dhritarashtra ne kaha,

"Jab tak Pandav jeevit hain, unse rajya chheena nahi ja sakta."

Usne Pandav paksh ke mahaan yoddhaon ka ullekh kiya—

Arjuna
Bhima
Krishna
Satyaki
Nakula
Sahadeva
Dhrishtadyumna
Virata

Aur kaha,

"Yeh sab milkar hamari sena ko tabah kar sakte hain."

Arjuna ki Mahima

Dhritarashtra ne yaad dilaya ki Arjuna—

akela hi uttar disha jeet kar lauta tha.
Khandava van mein devtaon tak ka saamna kar chuka hai.
Gandiva se teeron ki aisi varsha karta hai ki aasmaan dhak jaata hai.

Usne maana,

"Eklauta Arjuna hi poori duniya ka saamna kar sakta hai."

Bhima ka Dar

Dhritarashtra bola,

"Bhima ki gada ka koi samaan nahi."

"Uski shakti das hazaar haathiyon ke barabar hai."

"Krodhit Bhima Kaurav sena ko kuch hi samay mein samaapt kar dega."

Nakula aur Sahadeva

Unhone kaha,

"Madri ke dono putra Arjuna ke shishya hain."

"Ve baaz ki tarah dushmanon ka vinaash kar denge."

Krishna ka Smaran

Dhritarashtra ko sabse zyada chinta Krishna ki thi.

Usne yaad kiya—

Krishna ne Shishupala ko sabha mein hi maar diya tha.
Bade-bade raja Krishna ka saamna nahi kar paaye.
Sab Krishna se dar kar bhaag gaye the.

Dhritarashtra bola,

"Jahan Krishna neta hain, wahan vijay nishchit hai."

Sabse Bada Dar

Phir usne kaha,

"Jab main sochta hoon ki Krishna aur Arjuna ek hi rath par honge, mera hriday bhay se kaamp uthta hai."

Usne kaha,

"Arjuna Indra ke samaan hai."

"Aur Krishna swayam Vishnu hain."

Yudhishthira ka Krodh Sabse Bhayankar

Ek bahut mahatvapurn baat Dhritarashtra ne kahi.

Usne maana,

"Mujhe Arjuna, Bhima ya Krishna se utna dar nahi lagta..."

"...jitna Yudhishthira ke dharmik krodh se lagta hai."

"Kyunki unhone sada dharm ka paalan kiya hai."

"Unpar anyaay hua hai."

"Agar unka dharm-yukt krodh phoot pada, toh Kaurav vansh ka vinaash nishchit hai."

Sanjaya ke Liye Antim Nirdesh

Dhritarashtra ne Sanjaya se kaha,

Yudhishthira ka kushal-mangal poochhna.
Krishna ka bhi samman ke saath haal-chaal poochhna.
Kehna ki Dhritarashtra shaanti chahta hai.
Sabhi Pandavon, Satyaki, Virata aur anya rajaon ko mera pranam kehna.
Aur aise shabd bolna jo yuddh ko roken, na ki bhadkayein.
Is Adhyay ka Mukhya Sandesh
Dhritarashtra ko poori tarah pata tha ki Pandav dharm ke paksh mein hain.
Use Arjuna, Bhima aur Krishna ki apar shakti ka poora gyaan tha.
Usne khud maana ki Duryodhana aur Karna ki zid hi sangharsh ka mool kaaran hai.
Sabse adhik bhay use Yudhishthira ke dharmik krodh se tha.
Phir bhi, putra-moh ke kaaran woh Duryodhana ko rok nahi saka aur keval Sanjaya ke madhyam se ek aur shaanti-prayas karne laga."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.23
        with st.expander("Section 5.1.23  Section XXIII"):
            text1 = """ 
Chapter 23 – Sanjaya Pandavon ke Paas Pahunche, Yudhishthira ne Kauravon ka Haal Poocha

Yeh adhyay batata hai ki Sanjaya Dhritarashtra ka shaanti sandesh lekar Upaplavya mein Pandavon ke paas pahunche.

Sanjaya ne Yudhishthira ko Pranam Kiya

Sanjaya ne sabse pehle Yudhishthira ko pranam kiya aur kaha,

"Hey Rajan, aapko apne mitron ke saath swasth dekhkar mujhe bahut khushi hui."

Unhone bataya ki Dhritarashtra ne unka kushal-mangal poochha hai."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Pandavon ka Haal Poocha

Sanjaya ne poochha,

Bhima kaise hain?
Arjuna kaise hain?
Nakula aur Sahadeva kaise hain?
Aur Draupadi, jo sada satya aur dharm par chalti hain, kya ve bhi apne putron ke saath kushal hain?
Yudhishthira ne Sanjaya ka Swaagat Kiya

Yudhishthira bole,

"Hey Sanjaya, tumhe dekhkar aisa lag raha hai jaise maine swayam Dhritarashtra ko dekh liya ho."

Unhone kaha,

"Hum sab kushal hain."

Sabse Pehle Kauravon ka Haal Poocha

Yeh Yudhishthira ke uchch charitra ko dikhata hai.

Unhone ek-ek karke sabka haal poochha—

Bhishma
Dhritarashtra
Bahlika
Somadatta
Bhurishravas
Drona
Ashwatthama
Kripa
Yuyutsu
Karna

Unhone prarthana ki ki sab swasth hon.

Rajmahal ki Striyon ka Bhi Haal Poocha

Yudhishthira ne poochha,

Mataayein kaisi hain?
Bahuein kaisi hain?
Rajkumariyan kaisi hain?
Bachche kaise hain?
Ghar ke sab log sukhi hain na?

Yeh unki karuna aur vinamrata ko darshata hai.

Brahmanon ka Vishesh Dhyaan

Yudhishthira ne kaha,

"Mujhe aasha hai Dhritarashtra Brahmanon ka samman karte honge."

"Maine jo daan Brahmanon ko diye the, unhe Duryodhana ne cheena toh nahi?"

Unhone kaha,

"Brahmanon ka apmaan kisi bhi rajya ke vinaash ka kaaran ban sakta hai."

Rajya ki Suraksha ka Prashn

Yudhishthira ne poochha,

Kya rajya ke adhikaari santusht hain?
Kya koi dushman mitra bankar andar se saazish toh nahi kar raha?
Kya sab log Dhritarashtra ko apna rakshak maante hain?
Kya Unhe Pandav Yaad Hain?

Yudhishthira ne halka sa vyangya karte hue poochha,

"Kya Kauravon ko Arjuna yaad hai?"

"Wahi Arjuna jiske Gandiva ke teeron ki garaj bijli ki tarah goonjti hai."

"Wahi Arjuna jo ek baar mein anek teer chala sakta hai."

Bhima ko Yaad Hai?

Unhone poochha,

"Kya unhe Bhima yaad hai?"

"Wahi Bhima jise dekhkar shatru sena haathi ke saamne kaanpte hue baans ki tarah hilne lagti hai."

Nakula aur Sahadeva

Yudhishthira ne yaad dilaya,

Sahadeva ne Kalinga ko jeeta tha.
Nakula ne pashchimi deshon ko jeetkar rajya ka vistaar kiya tha.
Dwaitavana ki Ghatna Yaad Hai?

Yudhishthira ne Sanjaya se poochha,

"Kya Kauravon ko Dwaitavana ki ghatna yaad hai?"

Jab—

Gandharvon ne Duryodhana ko hara diya tha.
Use bandi bana liya tha.
Aur ant mein usi Duryodhana ko Bhima aur Arjuna ne chhudaya tha.

Yudhishthira ne yaad dilaya,

"Humne apne dushman ko bhi us samay bachaya tha."

Ant Mein Dukh

Yudhishthira bole,

"Sirf achchai karne se hamesha sukh nahi milta."

"Humne dharm ka paalan kiya."

"Humne Kauravon ki bhi madad ki."

"Lekin phir bhi Duryodhana ka hriday nahi badla."

Is Adhyay ka Mukhya Sandesh
Sanjaya Dhritarashtra ka shaanti sandesh lekar Pandavon ke paas pahunche.
Yudhishthira ne pehle Kauravon aur unke parivaar ka kushal-mangal poochha, jo unke uchch charitra ko darshata hai.
Unhone Brahmanon, rajya-prashasan aur praja ke kalyan ki bhi chinta vyakt ki.
Unhone Kauravon ko unke purane upkaar yaad dilaye—khaaskar Dwaitavana mein Duryodhana ko bachane ki ghatna.
Adhyay ka antim bhaav yeh hai ki dharm aur sadachar ke baad bhi anyaayi vyakti ka hriday badalna bahut kathin hota hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.24
        with st.expander("Section 5.1.24  Section XXIV"):
            text1 = """ 
Chapter 24 – Sanjaya ne Dhritarashtra ka Shaanti Sandesh Sunaya

Is adhyay mein Sanjaya Yudhishthira ko Dhritarashtra ka sandesh sunata hai aur dono vanshon ke beech shaanti ki prarthana karta hai.

Sanjaya ne Yudhishthira ki Baaton ki Pushti Ki

Sanjaya bola,

"Hey Yudhishthira, jo kuchh aapne Kuru vansh ke baare mein poochha aur kaha, vah satya hai."

Usne bataya ki—

Bhishma,
Drona,
Kripa,
aur anya vriddh Kuru

sab swasth hain."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Kauravon Mein Achhe aur Bure Dono Hain

Sanjaya ne imaandari se kaha,

"Kaurav paksh mein dharmic aur buddhimaan log bhi hain..."

"...aur kuchh paapi aur durbuddhi log bhi."

Yeh sanket tha ki sab log Duryodhana jaise nahi the.

Duryodhana ke Baare Mein

Sanjaya ne kaha,

"Duryodhana Brahmanon ko diya hua daan kabhi wapas nahi leta."

Aur kaha,

"Dhritarashtra tumhare saath hue anyaay ko sahi nahi maanta."

"Vah andar hi andar is baat se bahut dukhi hai."

Usne yeh bhi bataya ki Dhritarashtra ne Brahmanon se suna hai ki—

Apne hi kul mein yuddh (grih-yuddh) sabse bada paap hota hai.

Isliye vah shaanti chahta hai.

Pandavon ki Veerta Sabko Yaad Hai

Sanjaya ne kaha,

"Kaurav aaj bhi Pandavon ki veerta ko yaad karte hain."

Sabko yaad hai—

Arjuna ka Gandiva,
Bhima ki gada,
Nakula aur Sahadeva ki asadharan yuddh-kala.

Unhone maana ki yeh chaaron yoddha ranbhoomi mein bhayankar hain.

Bhagya ka Rahasya

Sanjaya ne gahri baat kahi,

"Bhavishya ko koi nahi jaanta."

"Aap jaise dharmatma ko bhi itna kasht sehna pada."

Isliye manushya ko apne karm karte rehna chahiye.

Pandav Kabhi Dharm Nahi Chhodenge

Sanjaya bola,

"Mujhe poora vishvaas hai ki Pandav kabhi sukh ke liye dharm ka tyag nahi karenge."

Yeh Yudhishthira ke charitra ki prashansa thi.

Shaanti ki Aasha

Ant mein Sanjaya ne kaha,

"Hey Yudhishthira, mujhe aasha hai ki apni buddhi aur dhairya se aap aisa maarg nikaalenge..."

"...jisse—

Kaurav,
Pandav,
Srinjaya,
aur sabhi raja

shaanti prapt kar saken."

Dhritarashtra ka Sandesh

Sanjaya ne ant mein kaha,

"Ab dhyaan se suniye."

"Main wahi sandesh sunaunga jo Dhritarashtra ne apne putron aur mantriyon se salaah karke mujhe diya hai."

Yahin se Dhritarashtra ka aadhikarik shaanti-prastaav shuru hota hai.

Is Adhyay ka Mukhya Sandesh
Sanjaya ne bataya ki Kaurav paksh mein sab log anyaayi nahi hain.
Dhritarashtra ko apne hi vansh ke yuddh ka bhay aur pachtava hai.
Kaurav Pandavon ki shakti aur veerta ko achhi tarah jaante hain.
Sanjaya ne Yudhishthira ke dharm aur vivek par bharosa jataya aur unse shaanti ka maarg chunne ki aasha vyakt ki.
Agla adhyay Dhritarashtra ke vistaar se diye gaye sandesh aur shaanti-varta ko aage badhata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.25
        with st.expander("Section 5.1.25  Section XXV"):
            text1 = """ 
Chapter 25 – Sanjaya ne Pandavon se Yuddh Rokne ki Vinati Ki

Is adhyay mein Yudhishthira sabke saamne Sanjaya se kehte hain ki ab vah Dhritarashtra ka poora sandesh sunaaye. Iske baad Sanjaya shaanti ka gehra sandesh deta hai.

Yudhishthira ne Kaha – Sabke Saamne Sandesh Sunao

Yudhishthira bole,

"Yahaan sab upasthit hain—

Pandav,
Srinjaya,
Krishna,
Satyaki,
Virata,

ab Dhritarashtra ka sandesh sabke saamne sunaao." """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Sanjaya ne Sabko Pranam Kiya

Sanjaya ne samman ke saath pranam kiya—

Yudhishthira
Bhima
Arjuna
Nakula
Sahadeva
Krishna
Satyaki
Drupada
Dhrishtadyumna

Phir bola,

"Main yahaan Kuru vansh ke hit ke liye aaya hoon."

Dhritarashtra ki Ichchha – Shaanti

Sanjaya ne kaha,

"Dhritarashtra shaanti chahta hai."

"Isi liye usne bina deri kiye mujhe tumhare paas bheja hai."

Yudhishthira se Vinati

Sanjaya bola,

"Hey Yudhishthira, kripaya shaanti ka maarg apnaaiye."

"Tum sabhi gunon se sampann ho."

"Tum—

dhairyavaan ho,
komal swabhaav ke ho,
satyavaadi ho,
udaar ho,
uchch kul mein janme ho,
aur kabhi apmaanjanak kaam nahi karte."
Yuddh ka Koi Laabh Nahi

Sanjaya ne bahut gahri baat kahi.

Usne poochha,

"Aisa kaun buddhimaan hoga jo jaan-boojhkar aisa kaam kare jisme poori duniya ka vinaash ho?"

Usne kaha,

"Is yuddh mein jeet aur haar dono hi dukhad hongi."

Agar Pandav Jeet Gaye To...

Sanjaya bola,

"Maan lo tum jeet bhi gaye..."

"Lekin agar tumhare hi sabhi rishtedaar mar gaye..."

"Toh aisi jeet ka kya arth?"

"Apne hi kul ka vinaash karke jeena bhi ek prakar ki mrityu ke samaan hoga."

Dono Paksh Bahut Shaktishaali Hain

Sanjaya ne kaha,

Pandavon ke saath hain—

Krishna
Satyaki
Dhrishtadyumna
Chekitana
aur anya mahaan yoddha.

Aur Kauravon ke saath hain—

Bhishma
Drona
Ashwatthama
Kripa
Karna
Shalya

Isliye,

"Kisi bhi paksh ki jeet aasaan nahi hogi."

Main Vijay Ya Haar Mein Koi Bhalaai Nahi Dekhta

Sanjaya ne spasht kaha,

"Na mujhe Pandavon ki jeet mein koi laabh dikhta hai..."

"...na Kauravon ki."

"Kyunki dono sthitiyon mein Bharat vansh ka vinaash hoga."

Krishna se Prarthana

Sanjaya ne vinamrata se haath jodkar kaha,

"Main Krishna aur Maharaj Drupada se prarthana karta hoon."

"Kripaya dono vanshon ka kalyan kijiye."

Krishna aur Arjuna par Vishwas

Sanjaya bola,

"Mujhe vishvaas hai..."

"Krishna aur Arjuna dharm ki baat kabhi nahi taalenge."

"Agar unse shaanti ke liye kaha jaaye, toh ve apni jaan tak dene ko taiyaar ho jaayenge."

Ant Mein Sandesh

Sanjaya ne kaha,

"Yahi Dhritarashtra ki ichchha hai."

"Aur Bhishma bhi isi baat ka samarthan karte hain..."

"...ki Kaurav aur Pandavon ke beech shaanti ho."

Is Adhyay ka Mukhya Sandesh
Sanjaya ne Dhritarashtra ka aadhikarik shaanti sandesh sabke saamne sunaaya.
Usne Yudhishthira ke dharm, vinamrata aur uchch charitra ki prashansa ki.
Usne samjhaya ki is yuddh mein jeetne wala bhi apne hi kul ko kho dega.
Usne maana ki dono paksh apar shaktishaali hain aur yuddh ka parinaam vinashkari hoga.
Ant mein usne Krishna aur Bhishma ki shaanti ki ichchha ka ullekh karte hue yuddh taalne ki vinati ki."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.26
        with st.expander("Section 5.1.26  Section XXVI"):
            text1 = """ 
            Section XXVI – Yudhishthira ka Shaanti Sandesh aur Antim Maang

Is adhyay mein Yudhishthira, Sanjaya ko apna drishtikon batate hain. Ve spasht karte hain ki Pandav yuddh nahi chahte, lekin apna nyayik adhikaar bhi nahi chhodenge.

1. "Humne Kab Yuddh Maanga?"

Yudhishthira ne Sanjaya se puchha,

"Maine aisi kaunsi baat kahi jisse tumhe laga ki main yuddh chahta hoon?"

Unhone kaha,

Shaanti hamesha yuddh se uttam hai.
Agar bina yuddh ke apna adhikaar mil jaaye, to kaun yuddh karega?
Sirf abhishapt vyakti hi yuddh ko pasand karega."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Ichchha Kabhi Samaapt Nahi Hoti

Yudhishthira ne gahra darshanik siddhant diya.

Unhone kaha,

Jaise jalti hui agni mein aur ghee daalne se vah aur bhadakti hai, vaise hi ichchha kabhi poori nahi hoti; use jitna poora karo, vah utni hi badhti hai.

Isliye,

Indriyon ke pichhe bhaagna dukh ka kaaran hai.
Dharma se prapt sukh hi vaastavik sukh hai.
3. Duryodhana ki Lalach hi Sab Vinash ka Kaaran

Yudhishthira ne kaha,

Dhritarashtra aaj dukhi isliye hai kyunki usne shuruaat se hi apne dusht putra ka saath diya.

Usne kabhi Vidura ki baat nahi maani.

4. Vidura ko Nazarandaaz Karna Sabse Badi Galti Thi

Vidura ke baare mein Yudhishthira ne kaha,

Ve sabse buddhimaan the.
Ve sabke sachche hitkari the.
Ve dharma ko jaante the.
Unki har salaah rajya ke hit mein hoti thi.

Lekin,

Dhritarashtra ne putra-moh mein unki baat ko nazarandaaz kar diya.

Yudhishthira ke anusaar,

"Jis din Vidura ki baat thukra di gayi, usi din Kuru vansh ke vinash ki shuruaat ho gayi."

5. Duryodhana ke Teen Mukhya Salahkaar

Yudhishthira ne kaha ki Duryodhana ke aas-paas sirf teen log hain—

Dushasana
Shakuni
Karna

Aur inhi ke prabhav mein vah galat nirnay le raha hai.

6. Karna ki Galatfahmi

Yudhishthira ne kaha,

Karna sochta hai ki vah Arjuna ko rok lega.

Lekin,

Itne saare yuddhon mein Karna kabhi Pandavon ko hara nahi saka.
Bhishma, Drona aur anya maharathi bhi jaante hain ki Arjuna ka koi samaan nahi.
7. Gandiva ki Dhvani Abhi Suni Nahi

Yudhishthira ne kaha,

"Dhritarashtra ke putra isliye zinda hain kyunki unhone abhi tak Gandiva ki asli garjana nahi suni."

Aur,

"Jab Bhima ka krodh phoot padega, tab Duryodhana ki saari aas toot jaayegi."

8. Hum Badla Nahi Chahte

Yudhishthira ne Sanjaya ko yaad dilaya,

Tum hamare saare dukh jaante ho.
Tumne dekha hai ki hamare saath kya hua.
Phir bhi hum shaanti hi chahte hain.

Yeh Yudhishthira ke dhairya aur kshama ka pramaan hai.

9. Antim Maang – Sirf Indraprastha

Ant mein Yudhishthira ne bahut spasht shabdon mein kaha,

"Jaise tum keh rahe ho, main shaanti ke liye taiyaar hoon."

Aur unhone sirf itni maang rakhi—

"Mujhe mera Indraprastha vaapas de diya jaaye."

Unhone na poora Hastinapur maanga, na Kauravon ka rajya.

Sirf apna vaidh aur nyayik rajya.

Is Adhyay ka Mukhya Sandesh
Yudhishthira ne spasht kiya ki Pandav yuddh nahi, shaanti chahte hain.
Ichchha aur lalach ko dukh ka mool bataya.
Dhritarashtra ke putra-moh aur Vidura ki avhelna ko Kuru vansh ke vinash ka kaaran bataya.
Karna ke ahankaar aur Arjuna ki asadharan shakti ka ullekh kiya.
Ant mein Yudhishthira ne sirf apna nyayik rajya, Indraprastha, maanga—yeh dikhata hai ki unka uddeshya badla nahi, dharma aur nyay tha."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.27
        with st.expander("Section 5.1.27  Section XXVII"):
            text1 = """ 
Section XXVII – Sanjaya ka Antim Shaanti Upadesh

Is adhyay mein Sanjaya, Yudhishthira ko yuddh se rokne ke liye gahra darshanik aur naitik upadesh dete hain. Yeh Mahabharata ke sabse shaantivadi sambhashanon mein se ek maana jaata hai.

1. "Yuddh se Rajya Mile, to bhi Achha Nahi"

Sanjaya ne kaha,

"Agar bina yuddh ke tumhe rajya nahi milta, to bhi yuddh karke rajya paane se behtar hai ki tum Andhak aur Vrishni rajya mein bhiksha maang kar jeevan bitao."

Yeh unka sabse kathor shaanti-sandesh tha.

Unke anusaar,

Jeevan chhota hai.
Yash aur dharma rajya se bade hain.
Khoon se jeeta hua rajya sukh nahi deta."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Ichchha Hi Sabse Badi Bedi Hai

Sanjaya ne kaha,

"Manushya ko baandhne wali sabse badi bedi dhan aur ichchha ki trishna hai."

Isliye,

Buddhimaan vyakti pehle apni ichchhaon ko jeetta hai.
Jo sirf dharma ka anusaran karta hai, wahi surya ki tarah prakashit hota hai.
3. Dhan se Bada Dharma

Unhone samjhaya,

Jo vyakti dharma ke bina sampatti paata hai, ant mein vinash ko prapt hota hai.
Chahe poori prithvi mil jaaye, bina dharma ke uska koi moolya nahi.
4. Yudhishthira ka Jeevan Pehle Hi Safal Hai

Sanjaya ne Yudhishthira ki prashansa karte hue kaha,

Tumne—

Vedo ka adhyayan kiya,
Yajna kiye,
Brahmanon ko daan diya,
Vanvaas saha,
Satya aur dharma ka paalan kiya.

Isliye,

Tumne is janm ka kartavya poora kar diya hai.

5. Achhe Karm Kabhi Vyarth Nahi Jaate

Sanjaya ke anusaar,

Maut ke baad dhan nahi jaata.
Sirf karm saath jaate hain.
Achhe karm swarg aur shanti dete hain.

Isliye,

Ek paap ke liye apni poori tapasya ko vyarth mat karo.

6. Vanvaas Kyon Saha Tha?

Sanjaya ne ek kathin prashn poochha,

Agar ant mein yuddh hi karna tha,

to 13 saal vanvaas kyon saha?
us samay hi yuddh karke rajya kyon nahi le liya?

Unhone yaad dilaya ki us samay bhi Pandavon ke paas—

Krishna,
Arjuna,
Satyaki,
Virata,
aur anek mitra the.

Tab bhi ve jeet sakte the.

7. Krodh Sabse Khatarnak Rog Hai

Sanjaya ne kaha,

"Krodh ek kadvi dava hai jo kisi rog ko nahi, balki manushya ko hi nasht kar deti hai."

Uske prabhav—

buddhi ka nash,
yash ka vinash,
paap ki or pravritti.

Isliye,

Krodh ko peena (niyantrit karna) hi sachchi veerta hai.

8. Vijay ke Baad Milega Kya?

Sanjaya ne prashn kiya,

Agar tum jeet bhi gaye aur—

Bhishma,
Drona,
Ashvatthama,
Kripa,
Somadatta ka putra,
Vikarna,
Vivingsati,
Karna,
Duryodhana

sab mar gaye...

To phir tumhe kaunsa sukh milega?

Rajya mil jayega, lekin—

budhapa,
mrityu,
sukh-dukh

to waise hi rahenge.

9. Agar Mitra Yuddh Chahte Hain...

Sanjaya ne bahut asadharan salah di,

"Yadi tumhare mitra hi yuddh chahte hain, to rajya unhe de do aur swayam yuddh se door chale jao."

Unke anusaar,

Swarg ka marg yuddh se nahi, dharma aur tyag se hai.

Is Adhyay ka Mukhya Sandesh
Sanjaya ne rajya se adhik dharma aur yash ko mahatva diya.
Unhone dhan aur ichchha ko bandhan bataya.
Krodh ko sabse bada shatru kaha.
Yuddh ke baad bhi jeevan ke dukh samaapt nahi hote—yeh yaad dilaya.
Ant mein unhone Yudhishthira se vinati ki ki rajya ke liye apne kul ka vinash na hone dein, aur yuddh se bachne ka har sambhav prayas karein."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.28
        with st.expander("Section 5.1.28  Section XXVIII"):
            text1 = """ 
Section XXVIII – Yudhishthira ka Dharma ka Gahra Darshan

Is adhyay mein Yudhishthira, Sanjaya ke shaanti-upadesh ka uttar dete hain. Yah Mahabharata ke sabse gahre dharma-darshanik adhyayon mein se ek hai.

1. Dharma Hamesha Aasaan Nahi Hota

Yudhishthira kehte hain,

"Tumne dharma ki baat sahi kahi. Lekin pehle yeh batao ki jo main kar raha hoon, vah vaastav mein dharma hai ya adharma."

Ve batate hain ki kabhi-kabhi—

Adharma, dharma jaisa dikhai deta hai.
Dharma, adharma jaisa lagta hai.
Isliye sirf bahari roop dekhkar nirnay nahi kiya ja sakta.

Isliye buddhimaan vyakti ko vivek (reason) se faisla karna chahiye."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Sankat ke Samay Dharma Badal Sakta Hai

Yudhishthira ek mahatvapurn siddhant rakhte hain:

"Aapad-dharma" (emergency ethics).

Unke anusaar,

Samanya paristhiti mein har varna aur ashram ka apna kartavya hai.
Lekin sankat ke samay kuch alag niyam lagu hote hain.

Udaharan:

Agar kisi vyakti ki jeevika poori tarah chali jaaye, to vah apne jeevan aur dharma ko bachane ke liye anya uchit saadhan apna sakta hai.

3. Paristhiti ke Anusaar Hi Dharma ka Nirnay

Yudhishthira kehte hain,

Galti do prakaar ki hai:

Jo sankat na hone par bhi sankat ka bahana banaaye.
Jo vaastavik sankat mein bhi zaruri kadam na uthaye.

Dono nindaniya hain.

4. Purvajon ka Marg

Ve kehte hain,

Hamare—

pita,
pitamah,
aur pracheen rishi

sabne isi siddhant ka paalan kiya hai.

Yani,

Dharma ko andhadhund nahi, balki paristhiti aur vivek ke anusaar samajhna chahiye.

5. Adharma se Rajya Nahi Chahiye

Yudhishthira ka dridh sankalp:

"Chahe mujhe poori prithvi mil jaaye...
chahe devlok mil jaaye...
chahe Brahmalok mil jaaye...
main unhe adharma se kabhi prapt nahi karunga."

Yeh unke charitra ka saar hai.

6. Krishna Hi Antim Nyaayadhish Hain

Yudhishthira kehte hain,

"Yahaan Krishna upasthit hain."

Aur Krishna—

buddhimaan hain,
rajneeti jaante hain,
dharma jaante hain,
sabka hit chahte hain.

Isliye Yudhishthira kehte hain,

"Krishna hi bataayein ki yuddh karna mera dharma hai ya shaanti ke liye sab chhod dena."

Yeh dikhata hai ki ve apni ichchha se nahi, dharma ke aadhar par nirnay lena chahte hain.

7. Krishna ki Mahima

Yudhishthira Krishna ki prashansa karte hue kehte hain ki—

Andhak,
Vrishni,
Bhoja,
Kukura,
Srinjaya

sab Krishna ke margdarshan se shaktishaali aur samriddh hue.

Krishna ke baare mein ve kehte hain:

Ve sab kuch jaante hain.
Ve rajneeti ke mahan gyata hain.
Ve dharma ke rakshak hain.
Ve sabke hit ki sochne wale hain.
8. Main Kabhi Krishna ki Salah Nahi Taalta

Adhyay ka sabse mahatvapurn vakya:

"Main kabhi bhi Krishna ki baat ko nazarandaaz nahi karta."

Yudhishthira ke liye Krishna—

mitra bhi hain,
guru bhi,
margdarshak bhi,
aur dharma ke sarvashreshtha vivechak bhi.
Is Adhyay ka Mukhya Sandesh
Dharma ka nirnay hamesha saral nahi hota; kabhi-kabhi dharma aur adharma ek jaise dikhte hain.
Sankat ke samay Aapad-dharma lagu hota hai, jahan paristhiti ke anusaar kartavya badal sakta hai.
Yudhishthira spasht karte hain ki ve adharma se prithvi ya swarg bhi nahi chahte.
Ve apne nirnay ka antim adhikar Krishna ko dete hain, kyunki unke anusaar Krishna hi dharma aur rajneeti ke sarvashreshtha vivechak hain.
Is adhyay se Yudhishthira ka charitra aur bhi spasht hota hai—ve rajya se adhik dharma ko mahatva dete hain, lekin dharma ki raksha ke liye yuddh bhi avashyak ho sakta hai agar Krishna use uchit maanein."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.29
        with st.expander("Section 5.1.29  Section XXIX"):
            text1 = """ 
Section XXIX – Krishna ka Dharma, Karma aur Nyaya par Antim Sandesh

Is adhyay mein Krishna pehli baar is shanti-varta mein apna vistaar se drishtikon rakhte hain. Ve spasht karte hain ki Pandav shanti chahte hain, lekin adharma ke saamne chup rehna bhi paap hai.

1. Krishna Dono Pakshon ki Bhalai Chahte Hain

Krishna kehte hain:

Main chahta hoon ki Pandavon ka vinash na ho.
Main Dhritarashtra aur uske putron ki bhi samriddhi chahta hoon.
Meri pehli ichchha hamesha shanti ki hi rahi hai.

Lekin ve ek mahatvapurn baat jodte hain:

Jab ek paksh atyadhik lalchi ho jaaye, tab shanti tik nahi sakti."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Sirf Gyaan Nahi, Karma Bhi Zaroori Hai

Krishna ek gahra darshanik siddhant dete hain.

Ve kehte hain:

Kuch log kehte hain ki karm hi mukti ka marg hai.
Kuch kehte hain ki keval gyaan hi kaafi hai.

Lekin Krishna udaharan dete hain:

Bhookh ka gyaan hone se bhookh nahi mitti.
Paani ka gyaan hone se pyaas nahi bujhti.

Jab tak vyakti khaata ya peeta nahi, tab tak phal nahi milta.

Isliye karm anivarya hai.

3. Pura Vishva Karma se Chal Raha Hai

Krishna batate hain:

Surya pratidin karm karta hai.
Vayu chalti hai.
Agni jalti hai.
Prithvi sabka bhaar uthati hai.
Nadiyan nirantar bahti hain.
Indra tapasya aur karm se Devraj bana.

Yani,

Prakriti ka har tattva karm kar raha hai.

4. Yudhishthira Apna Kshatriya Dharma Nibha Rahe Hain

Krishna kehte hain:

Yudhishthira—

Vedon ka adhyayan karte hain,
Yajna karna chahte hain,
Astra-shastra chalana jaante hain,
Rajadharma ka paalan karte hain.

Agar bina yuddh ke nyaya mil jaaye, to ve wahi marg chunenge.

Lekin agar yuddh hi kartavya ban jaaye, to usse bhaagna bhi adharma hoga.

5. Chaar Varnon ke Kartavya

Krishna pratyek varna ke kartavya batate hain:

Brahmana: adhyayan, adhyapan, yajna, daan aur tapasya.
Kshatriya: praja ki raksha, daan, yajna aur nyaya.
Vaishya: vyapar, krishi aur goraksha.
Shudra: seva aur parishram.

Aur raja ka kartavya hai ki sabko nyaya ke saath unke kartavya karne de.

6. Jab Raja Lobh Karne Lage...

Krishna kehte hain,

Jab raja—

lalchi ho jaata hai,
doosron ka dhan chheen leta hai,
dharma ko chhod deta hai,

tab yuddh janm leta hai.

Isliye astra aur shastra ka avishkar bhi dushton ko rokne ke liye hua.

7. Dhritarashtra ke Putra Chor ke Samaan Hain

Krishna kathor shabdon mein kehte hain,

Jo vyakti chori-chhipe dhan churaata hai aur jo khule aam bal se kisi ka adhikaar chheen leta hai—

dono chor hain.

Ve poochte hain,

Dhritarashtra ke putron aur choron mein antar hi kya hai?

8. Draupadi ka Apmaan Kabhi Nahi Bhoola Ja Sakta

Krishna sabko yaad dilate hain:

Sabha mein—

Draupadi ko ghaseet kar laya gaya.
Bhishma, Drona aur anya mahan log chup baithe rahe.
Sirf Vidura ne virodh kiya.

Phir Krishna Karna aur Dushasana ke kathor shabdon ko yaad dilate hain.

Yeh sab adharma tha, aur isi ne aaj ki paristhiti paida ki.

9. Krishna Swayam Doot Bankar Jaayenge

Krishna kehte hain,

Main swayam Hastinapura jaunga.

Agar meri baat maan li gayi, to—

Pandav bach jayenge,
Kaurav bhi bach jayenge,
aur maha-vinash tal jayega.

Lekin agar Duryodhana na maana,

to Bhima aur Arjuna uska vinash kar denge.

10. Do Vrikshon ka Prasiddh Roopak

Krishna do prateek dete hain:

Adharma ka Vriksh
Duryodhana – vriksh
Karna – tana (trunk)
Shakuni – shaakhaen
Dushasana – phool aur phal
Dhritarashtra – jad (root)
Dharma ka Vriksh
Yudhishthira – vriksh
Arjuna – tana
Bhima – shaakhaen
Nakula-Sahadeva – phool aur phal
Krishna, Dharma aur dharmanishtha log – jad

Yeh Mahabharata ke sabse prasiddh prateekon mein se ek hai.

11. Van aur Bagh ka Roopak

Krishna ant mein ek aur sundar upama dete hain:

Kaurav van (forest) hain.
Pandav bagh (tigers) hain.

Jaise—

bagh ke bina van surakshit nahi,
aur van ke bina bagh jeevit nahi,

waise hi Kaurav aur Pandav ek hi vansh ke ang hain.

Unka sandesh hai:

Dono ka sah-astitva hi sabke hit mein hai.

Is Adhyay ka Mukhya Sandesh
Krishna spasht karte hain ki shanti sabse pehla vikalp hai, lekin nyaya ke bina shanti sambhav nahi.
Ve karma-yoga ka siddhant rakhte hain—sirf gyaan nahi, uchit karm bhi avashyak hai.
Raja ka kartavya praja ki raksha aur nyaya hai; jab raja hi adhikaar chheen le, tab uska virodh dharma ban jaata hai.
Draupadi ka apmaan aur Pandavon ke adhikaar ka harn Mahabharata ke sangharsh ka mool kaaran bataya gaya.
Ant mein Krishna swayam shanti-doot banne ka sankalp lete hain, lekin saath hi chetavani dete hain ki agar shanti asafal hui, to dharma ki raksha ke liye yuddh anivarya hoga."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.30
        with st.expander("Section 5.1.30  Section XXX"):
            text1 = """ 
Section XXX – Yudhishthira ka Antim Sandesh Hastinapura ke Naam

Is adhyay mein Yudhishthira, Sanjaya ko Hastinapura bhejne se pehle ek bahut hi gahra aur maryadit sandesh dete hain. Yeh Mahabharata ke sabse shreshth diplomatic speeches mein se ek maana jaata hai. Ant mein ve spasht kar dete hain ki ve shanti chahte hain, lekin apna adhikar chhodenge nahi.

1. Sanjaya ki Prashansa

Yudhishthira sabse pehle Sanjaya ki tareef karte hain.

Ve kehte hain:

Tum kabhi jhooth nahi bolte.
Tum kabhi kathor bhasha nahi bolte.
Tum dono pakshon ke priya ho.
Tumhara man nirmal hai.
Tum Vidura ke samaan hamare hitachintak ho.

Isse pata chalta hai ki Sanjaya ko dono paksh poori tarah vishwas ke saath dekhte the."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Sabka Kushal-Mangal Poochna

Yudhishthira Sanjaya se kehte hain ki Hastinapura pahunchkar sirf rajaon hi nahi, balki sabhi logon ka haal poochna.

Ismein shamil hain:

Brahman
Rishi
Guru
Vyapari
Rajya ke adhikari
Senapati
Sipahi
Sevak
Das-dasi
Vriddh
Viklang
Garib
Nirashrit log

Yeh Yudhishthira ki sarvajan-hit ki soch ko darshata hai.

3. Drona, Bhishma aur Kripa ko Pranam

Ve vishesh roop se Sanjaya se kehte hain ki:

Drona ko mera pranam kehna.
Ashvatthama ka haal poochna.
Kripa ke charan sparsh karna.
Bhishma ko mera pranam kehna.
Dhritarashtra ka bhi samman karna.

Yeh sab us samay kaha ja raha hai jab yuddh lagbhag nischit ho chuka hai. Phir bhi maryada bani hui hai.

4. Duryodhana aur Dushasana ka Bhi Haal Poochna

Yeh aur bhi adbhut baat hai.

Yudhishthira kehte hain:

Duryodhana ka bhi kushal poochna.
Dushasana ka bhi.

Yeh dikhata hai ki ve vyaktigat dvesh se prerit nahi hain.

5. Vidura ke Liye Vishesh Sneha

Yudhishthira Vidura ke liye kehte hain:

Vidura hamare guru hain, pita hain, mata hain, mitra hain aur margdarshak hain.

Yeh Mahabharata mein Vidura ke prati Pandavon ki sabse sundar prashansaon mein se ek hai.

6. Mahilaon aur Parivar ke Liye Sandesh

Yudhishthira kehte hain:

Sabhi mataon se kehna:

Asha hai tumhare putra tumhara samman karte hon.

Sabhi bahuon se kehna:

Tumhara samman bana rahe.
Tum apne pati aur sasural ka adar karo.
Tum sukhi raho.

Yeh batata hai ki yuddh ke beech bhi unki chinta samaj aur parivar ke liye hai.

7. Garib aur Viklangon ke Liye Daya

Yudhishthira Sanjaya se kehte hain:

Jo—

andhe hain,
langde hain,
baune hain,
nirbal hain,
garib hain,

unse kehna:

Ghabrana mat. Jab main apna rajya wapas paa lunga, tab main tumhari bhojan aur vastra se seva karunga.

Yeh Yudhishthira ki karuna ka ati uttam udaharan hai.

8. Dharma Hi Meri Shakti Hai

Ve kehte hain:

Duryodhana ke paas bahut bade yoddha hain.

Lekin turant jodte hain:

Meri asli shakti dharma hai.

Yeh Mahabharata ka ek kendriya siddhant hai.

9. Antim Sandesh Duryodhana ke Naam

Sabse antim aur sabse mahatvapurn vaakya:

Yudhishthira Sanjaya se kehte hain ki Duryodhana ko kehna:

Tumhari poore Kuru rajya par akela raj karne ki ichchha anyaay hai.

Aur phir ve apni antim shart rakhte hain:

Ya to mera Indraprastha mujhe wapas de do, ya phir yuddh karo.

Is Adhyay ka Mukhya Sandesh
Yudhishthira Sanjaya ko ek aadarsh rajdoot ke roop mein vidai dete hain aur sabhi—mitra, shatru, guru, sevak, mahilaon aur garibon—ka kushal poochhne ko kehte hain.
Ve dikhate hain ki ek dharmic raja ke liye praja ka har varg samaan mahatva rakhta hai.
Vidura, Bhishma aur Drona ke prati unka samman yuddh ke saamne bhi kam nahi hota.
Ant mein ve ek spasht aur nyayapurn sandesh bhejte hain: Pandav shanti ke ichchhuk hain, lekin apne vaidh adhikar—Indraprastha—se kabhi haath nahi kheench sakte. Agar rajya wapas nahi diya gaya, to yuddh hi antim vikalp hoga."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.31
        with st.expander("Section 5.1.31  Section XXXI"):
            text1 = """ 
Section XXXI – Yudhishthira ka Antim Shanti Prastav (Five Villages Proposal)

Yeh Mahabharata ke sabse prasiddh adhyayon mein se ek hai. Isi adhyay mein Yudhishthira apna antim shanti-prastav rakhte hain—agar poora rajya na mile, to sirf paanch gaon de diye jaayen. Agar itna bhi na diya gaya, to yuddh anivarya hoga.

1. Sab Kuch Ishwar ke Adheen Hai

Yudhishthira Sanjaya se kehte hain:

Dharmic ho ya adharmic, balwan ho ya durbal, buddhiwan ho ya balak—sabhi Bhagavan ke niyantran mein hain.

Isliye kisi ko apne bal ya buddhi ka ahankar nahi karna chahiye."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Dhritarashtra ke Liye Sandesh

Yudhishthira Sanjaya se kehte hain ki Dhritarashtra ko pranam karke kehna:

Hum aaj bhi aapka samman karte hain.
Bachpan mein aapne hi humein rajya diya tha.
Ab humein poori tarah tyag mat dijiye.
Pura rajya kisi ek vyakti ke liye nahi hota.
Hum sab milkar rehna chahte hain.
3. Bhishma ke Naam Sandesh

Bhishma se kehna:

Aapne Kuru vansh ko bachaya tha.

Ab phir wahi kariye—

Aisa upay batayiye jisse sabhi Kuru vanshaj shanti se saath reh saken.

4. Vidura se Vinati

Vidura ke liye sandesh bahut chhota hai lekin gahra:

Kripaya Yudhishthira ke hit ke liye shanti ki salah dete rahiye.

Yudhishthira jaante hain ki Hastinapura mein sach bolne wala sabse bada vyakti Vidura hi hai.

5. Duryodhana ke Liye Yaad Dilayi Gayi Purani Anyay

Yudhishthira Sanjaya se kehte hain ki Duryodhana ko yaad dilana:

Tumne—

Draupadi ka sabha mein apmaan kiya.
Humein vanvaas diya.
Deer-skin pehna kar jungle bheja.
Dushasana se Draupadi ko ghaseetwaya.

Phir bhi—

Humne badla nahi liya.

Humne sab kuch sirf isliye saha kyunki hum Kuru vansh ka vinash nahi chahte.

6. Sirf Apna Adhikar Chahiye

Yudhishthira kehte hain:

Humein doosron ka rajya nahi chahiye.

Sirf apna hissa chahiye.

Yeh unke dharma ka saar hai.

7. Mahabharata ka Sabse Prasiddh Shanti Prastav

Yudhishthira kehte hain:

Agar poora rajya nahi dena chahte—

to humein sirf ye paanch sthaan de do:

Kusasthala
Vrikasthala
Makandi
Varanavata
Aur koi ek paanchva gaon tumhari pasand ka

Bas itna de do—

Aur yuddh nahi hoga.

Yeh wahi prasiddh "Five Villages Proposal" hai. Iska arth tha:

Pandavon ko rajya ki lalach nahi thi; unhe keval nyay aur jeevan-yapan ke liye apna uchit hissa chahiye tha.

8. Antim Appeal

Yudhishthira kehte hain:

Bhai bhai ke saath rahein.
Pita putron ke saath rahein.
Panchala aur Kuru milkar hasen.
Dono vansh surakshit rahen.

Yeh mera sachcha ichchha hai.

9. Antim Vaakya

Adhyay ka sabse prabhavshali vaakya:

Main shanti ke liye bhi taiyar hoon aur yuddh ke liye bhi.

Main dharma bhi jaanta hoon aur shastra bhi.

Komalta bhi mera swabhav hai aur kathorta bhi, jab avashyak ho.

Is Adhyay ka Mukhya Sandesh
Yudhishthira Dhritarashtra, Bhishma aur Vidura se shanti banaye rakhne ki vinati karte hain.
Ve Duryodhana ko yaad dilate hain ki Pandavon ne har apmaan sah liya, sirf Kuru vansh ko bachane ke liye.
Ve poore rajya ki maang chhodkar sirf paanch gaon maangte hain—yeh unki vinamrata aur nyay-priyata ka pramaan hai.
Ant mein ve spasht kar dete hain: "Shanti meri pehli pasand hai. Lekin agar nyay nahi mila, to main yuddh ke liye bhi poori tarah taiyar hoon." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.32
        with st.expander("Section 5.1.32  Section XXXII"):
            text1 = """ 
Section XXXII – Sanjaya ki Wapasi aur Dhritarashtra ko Kadvi Sachchai

Is adhyay mein Sanjaya Pandavon ka sandesh lekar Hastinapura laut te hain. Yudhishthira ka sandesh sunane se pehle hi ve Dhritarashtra ko uski galtiyon ka aaina dikha dete hain. Yeh Mahabharata ke sabse kathor satyavaadi updeshon mein se ek hai.

1. Sanjaya Hastinapura Lautte Hain

Pandavon se vidai lekar Sanjaya Hastinapura pahunchte hain.

Ve pehle dwarpal se kehte hain:

Raja ko batao ki main Pandavon ka sandesh lekar aaya hoon.

Dhritarashtra turant unhe andar bulwa lete hain."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Yudhishthira ka Namaskar

Sanjaya sabse pehle kehte hain:

Yudhishthira ne aapko pranam kaha hai.
Ve aapka, aapke putron, mitron aur mantriyon ka kushal-mangal poochte hain.

Dhritarashtra bhi Yudhishthira aur Pandavon ka haal poochte hain.

Isse dono pakshon ki maryada dikhti hai.

3. Yudhishthira ka Swabhav

Sanjaya Dhritarashtra se kehte hain:

Yudhishthira—

apna adhikar chahte hain,
dharma ke viruddh kuch nahi karna chahte,
ahimsa ko sabse bada gun maante hain,
dhan se adhik dharma ko mahatva dete hain,
sada satya aur nyay ki or jhukte hain.

Yeh Pandavon ki neeti ka saar hai.

4. Sab Kuch Bhagya ke Adheen

Sanjaya kehte hain:

Manushya kathputli ki tarah hai.

Koi adrishya shakti use chalati hai.

Yudhishthira jaise dharmic vyakti ko dukh milna aur Duryodhana jaise adharmi ko rajya milna dekhkar Sanjaya kehte hain ki Bhagya ka bal bahut bada hai.

5. Dhritarashtra ko Seedha Dosh

Iske baad Sanjaya bahut kathor shabdon mein kehte hain:

Aapne anyaay kiya hai.

Aapki kirti kharab ho chuki hai.

Agle janm mein bhi iska phal bhugatna padega.

Ve kehte hain:

Aapne putra-moh mein dharma chhod diya.
Anyay se prapt rajya ko sambhalna chahte hain.
Yeh Kuru vansh ke vinash ka kaaran banega.
6. Dusht Salahkaaron ka Prabhav

Sanjaya kehte hain:

Aapke paas buddhimaan mantri hain.

Phir bhi—

Sab Pandavon ko unka adhikar na dene ka hi nirnay le rahe hain.

Isliye Kuru vansh ka vinash nishchit hai.

7. Yudhishthira Agar Krodhit Hue...

Sanjaya chetavani dete hain:

Yadi Yudhishthira sach mein shraap ya vinash ki ichchha kar dein—

to

Kuru vansh samay se pehle hi samapt ho jayega.

Aur iska paap keval Dhritarashtra par aayega.

8. Arjuna ka Swarg Gaman

Sanjaya yaad dilate hain:

Arjuna jeevit avastha mein hi Swarg gaye the.

Devtaon ne unka satkar kiya tha.

Isse pramaan milta hai ki Pandav asadharan hain aur unhe halka nahi samajhna chahiye.

9. Raja Bali ka Darshan

Sanjaya Raja Bali ka darshanik vichar batate hain:

Janm
Bal
Kirti
Sampatti
Dukh
Sukh

Sab kuch ek gahre kaaran se hota hai.

Ant mein Bali is nishkarsh par pahunchte hain ki sabka mool kaaran Paramatma hi hai.

10. Indriya Niyantran

Sanjaya kehte hain:

Gyan ke paanch dwar hain—

Aankh
Kaan
Naak
Sparsh
Jeevha

Jo apni ichchhaon ko niyantrit kar leta hai, vah swayam shant ho jata hai.

11. Antim Chetavani

Sanjaya kehte hain:

Yadi shanti nahi hui—

to

Arjuna Kuruvansh ko usi tarah jala dega jaise sukhi ghaas ko aag jala deti hai.

Is vinash ke zimmedar keval Dhritarashtra honge.

12. Dhritarashtra ki Sabse Badi Galti

Sanjaya spasht kehte hain:

Aapne—

sache aur wafadar salahkaaron (jaise Vidura) ki baat nahi maani,
aur bure salahkaaron ki baat maan li.

Isi wajah se itna bada samrajya ab haath se nikalne wala hai.

13. Agle Din Sabha Mein Sandesh

Ant mein Sanjaya kehte hain:

Main bahut thak gaya hoon.

Kal subah sabha mein sabhi Kuru rajkumar aur maharathi Yudhishthira ka poora sandesh sunenge.

Yahi se Mahabharata ki antim shanti-varta ka agla charan shuru hota hai.

Is Adhyay ka Mukhya Sandesh
Sanjaya Hastinapura lautkar pehle Dhritarashtra ko Yudhishthira ka kushal sandesh dete hain.
Uske baad ve bina dare Dhritarashtra ko uske putra-moh, anyaay aur durdrishti ke liye doshi thahrate hain.
Ve chetavani dete hain ki agar shanti na hui, to Arjuna aur Pandav Kuru sena ka vinash kar denge.
Ant mein Sanjaya agle din sabha mein Yudhishthira ka poora sandesh sunane ki baat kahkar varta ko agle adhyay ke liye chhod dete hain."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.33
        with st.expander("Section 5.1.33  Section XXXIII"):
            text1 = """ 
Section XXXIII – Vidura Niti ki Shuruaat (Mahabharata ka Maha-Upadesh)

Is adhyay se Vidura Niti shuru hoti hai. Yeh Mahabharata ke sabse prasiddh niti-granthon mein se ek hai. Dhritarashtra ko neend nahi aa rahi, kyunki Sanjaya Pandavon ka sandesh la chuke hain aur kal sabha mein sunaya jayega. Is chinta mein vah Vidura ko bulate hain.

1. Dhritarashtra ki Bechaini

Dhritarashtra Vidura se kehte hain:

Sanjaya Pandavon se laut aaya hai.
Usne mujhe daant diya.
Kal sabha mein Yudhishthira ka sandesh sunayega.
Mujhe nahi pata us sandesh mein kya hai.
Isi chinta se mujhe neend nahi aa rahi.

Woh Vidura se puchte hain:

"Aise vyakti ke liye kya upay hai jo chinta ke karan so nahi pa raha?" """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Vidura ka Pehla Uttar

Vidura kehte hain:

Neend kin logon ko nahi aati?

Chor ko
Kaam-vasna se grast vyakti ko
Jisne dhan kho diya ho
Jo asafal ho gaya ho
Kamzor vyakti jo kisi shaktishaali se dara hua ho
Jo doosron ki sampatti ka lalach karta ho

Phir ve prashn karte hain:

"Maharaj, kya aap doosron ke dhan (Pandavon ke rajya) ka lobh kar rahe hain?"

Yeh ek bahut seedha prahar hai.

3. Dhritarashtra ka Uttar

Dhritarashtra kehte hain:

"Mujhe dharma aur rajneeti ki baatein batao."

Ve maante hain ki Vidura hi sabse buddhimaan hain.

4. Vidura ka Kathor Satya

Vidura kehte hain:

Yudhishthira teenon lokon ka raja banne yogya hai.
Phir bhi tumne use vanvas de diya.
Tum swayam andhe hone ke karan rajya ke adhikari nahi the.
Fir bhi tumne Duryodhana ko rajya de diya.

Ve kehte hain:

Yudhishthira—

satyavaadi hai,
dharmic hai,
dayaalu hai,
tumhara samman karta hai,

isliye sab anyaay seh raha hai.

5. Duryodhana Par Bharosa = Vinash

Vidura kehte hain:

Tumne rajya ka niyantran de diya—

Duryodhana ko
Shakuni ko
Karna ko
Dushasana ko

Phir tum samriddhi ki aasha kaise kar sakte ho?

6. Buddhimaan Vyakti ke Lakshan

Vidura ek lambi suchi dete hain.

Ek buddhimaan vyakti—

achhe kaam karta hai,
bure kaam chhod deta hai,
gussa aur ahankaar par niyantran rakhta hai,
apni yojana gupt rakhta hai,
mushkilon se nahi ghabrata,
ichchha se nahi, vivek se nirnay leta hai,
kaam ko poora karta hai,
samay barbaad nahi karta,
apne indriyon par niyantran rakhta hai.
7. Murkh Vyakti ke Lakshan

Murkh vyakti—

doosron ke kaam mein dakhal deta hai,
shaktishaali se bair leta hai,
dushman ko dost samajhta hai,
apni yojana sabko bata deta hai,
bina bulaye pahunch jata hai,
bahut bolta hai,
galti khud karta hai aur dosh doosron ko deta hai,
apni aukaat jaane bina bade sapne dekhta hai.
8. Kshama ki Mahima

Vidura kehte hain:

Log samajhte hain—

Kshama kamzori hai.

Lekin sach ye hai:

Kshama sabse badi shakti hai.

Aur:

Dharm sabse bada hit hai.
Kshama sabse badi shanti hai.
Gyaan sabse bada santosh hai.
Daya sabse bada sukh hai.
9. Narak ke Teen Dwaar

Vidura kehte hain:

Teen cheezein narak ka dwaar hain—

Kaam (Lust)
Krodh (Anger)
Lobh (Greed)

Inhe hamesha tyagna chahiye.

10. Raja ko Kin Logon se Salah Nahi Leni Chahiye

Kabhi salah na lo:

Murkh se
Aalasi se
Kaam talne wale se
Chaplusi karne wale se

Dhritarashtra ne in chaaron ki baat maani thi.

11. Raja ke Saat Vinashkari Dosh

Ek raja ko tyagna chahiye:

Stri-asakti
Jua
Shikaar ka vyasan
Madira
Kathor vachan
Ati kathor dand
Dhan ka durupyog
12. Safal Raja Kaun?

Safal raja wahi hai jo—

kaam aur krodh par niyantran rakhe,
yogya vyakti ko dhan de,
nyay kare,
doshi ko dand de,
aur samay par daya bhi kare.
13. Antim Upadesh

Vidura ant mein kehte hain:

Pandu ke paanch putra—

tumne hi paale,
tumne hi unhe shiksha di,
ve aaj bhi tumhari aagya maante hain.

Isliye:

Unhe unka uchit rajya wapas de do.

Tab tum bhi sukhi rahoge, tumhare putra bhi, aur devata aur manushya sab tum par vishwas karenge.

Is Adhyay ka Saar
Dhritarashtra ne chinta mein Vidura ko bulaya.
Vidura ne spasht kaha ki unki bechaini ka mool Pandavon ke adhikar par lobh hai.
Is adhyay mein Vidura Niti ka aarambh hota hai—jismein buddhimaan aur murkh vyakti ke lakshan, raja ke kartavya, kshama, dharma, indriya-niyantran aur rajneeti ke siddhant bataye gaye hain.
Ant mein Vidura Dhritarashtra ko ek hi samadhan dete hain: Pandavon ko unka haq de do, tabhi Kuru vansh bach sakta hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.34
        with st.expander("Section 5.1.34  Section XXXIV"):
            text1 = """ 
Section XXXIV – Vidura Niti (Part 2): Self-Control aur Rajdharma

Is adhyay mein Dhritarashtra fir Vidura se poochte hain ki unki chinta ka kya upay hai aur Pandavon ke hit mein kya karna chahiye. Vidura aur bhi gahra niti-upadesh dete hain. Isme sabse bada vishay hai indriya-niyantran (self-control), vivek, aur satya-vachan.

1. Dhritarashtra ka Prashn

Dhritarashtra kehte hain:

Mujhe neend nahi aa rahi.
Mujhe bhavishya ka dar hai.
Mujhe batao Yudhishthira ke mann mein kya hai.
Aur mujhe batao ki Kuruvansh ke hit mein kya karna chahiye."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Kadva Sach Bolna Chahiye

Vidura kehte hain:

Agar kisi ka bhala chahte ho, to bina poochhe bhi satya bolna chahiye—chahe woh kadva ho ya meetha.

Ek buddhimaan vyakti:

anyaay se safalta paane ki ichchha nahi karta,
aur agar nyaay ke baad bhi safalta na mile to shok nahi karta.
3. Kaam Karne se Pehle Teen Cheezen Socho

Har karya se pehle socho:

Kya main iske yogya hoon?
Yeh karya kaisa hai?
Iska parinaam kya hoga?

Jo bina soche kaam karta hai, vah baad mein pachtata hai.

4. Achha Raja Kaun?

Vidura kehte hain ki raja ko hamesha pata hona chahiye:

rajya kitna bada hai,
kitna dhan hai,
kitna nuksan ho sakta hai,
kitni praja hai,
aur dand kab aur kitna dena hai.

Jo raja in sab ka santulan nahi jaanta, uska rajya tikta nahi.

5. Sabse Bada Shatru – Apni Indriyan

Vidura kehte hain:

Insaan ka sabse bada shatru bahar nahi, andar hai.

Pehle:

apne mann ko jeeto,
phir mantriyon ko,
phir dushmanon ko.

Jo ulta karta hai, vah haar jata hai.

6. Sharir Ek Rath Hai

Vidura ek sundar upama dete hain:

Sharir = Rath
Atma = Saarthi
Indriyan = Ghode

Agar ghode niyantrit honge to yatra surakshit hogi.

Agar indriyan aniyantrit hongi to jeevan vinash ki or chala jayega.

Yahi siddhant Bhagavad Gita aur Kathopanishad mein bhi milta hai.

7. Apna Sabse Bada Mitra Aur Shatru

Vidura kehte hain:

Insaan khud hi apna mitra hai.
Aur wahi khud apna shatru bhi hai.

Jo apne mann aur indriyon ko jeet leta hai, usne sab kuch jeet liya.

8. Kaam aur Krodh

Vidura kehte hain:

Kaam (desire) aur Krodh (anger):

buddhi ko tod dete hain,
vivek ko khatm kar dete hain.

Isliye pehle andar ke paanch shatru jeeto, phir bahar ke shatru se lado.

9. Dushton ki Sangat

Vidura kehte hain:

Jaise geeli lakdi sukhi lakdi ke saath jal jaati hai,

waise hi nirdosh vyakti bhi dushton ki sangat se dand paata hai.

Isliye:

Dushton ki mitrata se bacho.

10. Sajjan aur Durjan ka Antar
Sajjan ke gun
Atma-gyan
Dhairya
Satya
Daan
Madhur vaani
Santosh
Saralta
Sanyam
Durjan ke gun
Kapat
Asatya
Ashuddhata
Kathor vaani
Asantosh
Lobh
11. Vaani ka Mahatva

Vidura kehte hain:

Sabse kathin cheez hai—

Apni zubaan ko niyantrit karna.

Achhi vaani:

logon ka hit karti hai,
sambandh banati hai.

Buri vaani:

jeevan bhar ka dukh deti hai.
12. Shabd Talwar se Zyada Chot Pahunchate Hain

Vidura bahut sundar upama dete hain:

Teer sharir se nikala ja sakta hai.
Talwar ka ghaav bhar sakta hai.

Lekin—

Kathor shabdon ka ghaav kabhi poori tarah nahi bharta.

Isliye buddhimaan kabhi aise shabd nahi bolta jo kisi ke hriday ko chhed dein.

13. Vinash Se Pehle Buddhi Chali Jaati Hai

Vidura kehte hain:

Jab kisi ka vinash nikat hota hai,

to uski buddhi ulta kaam karne lagti hai.

Usse galat baat bhi sahi lagne lagti hai.

Phir ve Dhritarashtra se kehte hain:

Aapke putron ke saath bhi yahi ho raha hai.

Unki buddhi Pandavon ke prati dvesh ke karan bhrasht ho chuki hai.

14. Antim Salah

Vidura kehte hain:

Yudhishthira:

sabse yogya vaaris hai,
dharm ko jaanta hai,
buddhimaan hai,
aapka sadaiv aadar karta hai,
aur aapki maryada bachane ke liye bahut dukh sah chuka hai.

Isliye:

Rajya Yudhishthira ko de dijiye. Wahi aapka vaastavik aur uchit uttaradhikari hai.

Is Adhyay ka Saar
Satya kadva ho to bhi hit ke liye bolna chahiye.
Kisi bhi karya se pehle yogyata, karya aur parinaam par vichar karna chahiye.
Sabse pehle apni indriyon aur mann ko jeetna chahiye.
Dushton ki sangat vinash ka kaaran banti hai.
Madhur vaani aur sanyam sabse bade gun hain.
Vinash se pehle buddhi viparit ho jaati hai.
Vidura ka spasht nishkarsh hai: Yudhishthira hi dharm ke anusaar rajya ke adhikari hain; unhe unka rajya wapas de dena hi Kuruvansh ka kalyan hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.35
        with st.expander("Section 5.1.35  Section XXXV"):
            text1 = """ 
Section XXXV – Vidura Niti (Part 3): Satya, Dharma aur Rajdharma

Is adhyay mein Dhritarashtra fir Vidura se aur upadesh maangte hain. Vidura ek prasiddh kahani (Virochana–Sudhanvan–Prahlada) ke madhyam se batate hain ki satya ko kabhi bhi putra, dhan ya rajya ke liye nahi chhodna chahiye.

1. Dhritarashtra aur Sunna Chahte Hain

Dhritarashtra kehte hain:

"Tumhare dharma aur niti ke vachan bahut madhur hain. Meri pyaas abhi nahi bujhi. Mujhe aur batao."

Yeh dikhata hai ki Dhritarashtra sach ko samajhte hain, lekin us par amal karne ki shakti unmein kam hai."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Sabse Bada Teerth – Daya

Vidura kehte hain:

Do cheezein samaan maani jaati hain:

sabhi teerthon mein snaan,
sabhi jeevon par daya.

Lekin Vidura kehte hain:

Sabhi praaniyon par daya karna, teerth-snaan se bhi bada hai.

Aur Dhritarashtra se kehte hain:

Apne sabhi putron (Pandav aur Kaurav dono) par samaan daya rakho.

3. Virochana aur Sudhanvan ki Kahani

Vidura ek purani kahani sunate hain.

Rajkumari Kesini swayamvar karna chahti thi.

Do var aaye:

Virochana (Prahlada ka putra, Asura)
Sudhanvan (Brahmana)

Kesini ne prashn poocha:

"Kaun shreshtha hai – Brahmana ya Asura?"

4. Ahankaar vs Vinamrata

Virochana bola:

"Hum Asura sabse bade hain."

Sudhanvan ne use samaan aasan par baithne se mana kar diya aur kaha ki maryada ka paalan hona chahiye.

5. Jeevan ki Shart

Dono ne apni jaan daav par laga di aur faisla karne ke liye gaye:

Prahlada ke paas (Virochana ke pita).

Kyuki sabko pata tha:

Prahlada kabhi jhooth nahi bolte.

6. Jhooth Bolne ka Parinaam

Prahlada pehle poochte hain:

"Jhooth bolne wale ka kya hota hai?"

Sudhanvan jawab dete hain:

Jhooth bolne wala—

sada dukh paata hai,
shatru paata hai,
kul ka nash karta hai.

Aur phir bahut gahra siddhant dete hain:

Pashu ke liye jhooth → 5 purvajon ka patan.
Gaay ke liye jhooth → 10 purvajon ka patan.
Ghode ke liye jhooth → 100 purvajon ka patan.
Manushya ke liye jhooth → 1000 purvajon ka patan.
Zameen (land/kingdom) ke liye jhooth → poore vansh ka vinash.

Isliye:

Kabhi bhi bhoomi ya rajya ke liye jhooth mat bolo.

Yeh seedha Dhritarashtra ke liye sandesh hai.

7. Prahlada ka Nyaya

Prahlada ne apne putra ke paksh mein jhooth nahi bola.

Unhone kaha:

Sudhanvan tumse shreshtha hai.

Aur is prakar apne hi putra ko hara hua ghoshit kar diya.

8. Vidura ka Sandesh

Vidura kehte hain:

Prahlada ne putra se zyada dharma ko chuna.

Dhritarashtra ko bhi wahi karna chahiye.

Putra-prem mein jhooth bolkar aur anyaay karke apne poore vansh ka vinash mat karo.

9. Devata Kaise Raksha Karte Hain?

Vidura ek bahut sundar baat kehte hain:

Devata hathiyar lekar kisi ki raksha nahi karte.

Ve us vyakti ko sahi buddhi dete hain.

Yahi unki sabse badi kripa hai.

10. Kin Cheezon se Bachna Chahiye

Vidura kuch paapon ki suchi dete hain:

Madira
Nirarthak jhagda
Bahut logon se shatruta
Ghar mein phoot
Raja ke prati vishvasghaat

Aur anya gambhir adharmik karmon ka bhi varnan karte hain.

11. Asli Pariksha Kab Hoti Hai?

Vidura kehte hain:

Sona → Aag mein parikshit hota hai.
Achha kul → Vyavahaar se pehchana jaata hai.
Imaandaar vyakti → Aacharan se.
Veer → Sankat mein.
Sanyami → Garibi mein.
Dost aur dushman → Vipatti mein.
12. Samriddhi Kis Se Aati Hai?

Vidura ke anusaar:

Achhe karm → Samriddhi ka janm.
Parishram → Samriddhi ki vriddhi.
Kaushal → Jad mazboot karta hai.
Atma-sanyam → Samriddhi ko sthir rakhta hai.
13. Aath Mukhya Gun

Vidura aath gun batate hain jo vyakti ko prakashit karte hain:

Buddhi
Uttam kul
Atma-sanyam
Shastra-gyan
Veerta
Kam bolna
Shakti ke anusaar daan
Kritagyata (gratitude)
14. Dharma ke Aath Marg

Vidura dharma ke aath marg batate hain:

Yajna
Daan
Adhyayan
Tapasya
Satya
Kshama
Daya
Santosh

Ve kehte hain ki pehle chaar ka paalan kabhi-kabhi dikhave ke liye bhi ho sakta hai, lekin:

Satya, Kshama, Daya aur Santosh sirf sache sajjanon mein hi hote hain.

15. Jeevan ki Yojana

Vidura kehte hain:

Din mein aisa kaam karo ki raat sukh se bite.
Yuvaavastha mein aisa karo ki budhaapa sukh se bite.
Poore jeevan mein aisa karo ki mrityu ke baad bhi kalyan ho.
16. Antim Salah Dhritarashtra ke Liye

Vidura ant mein bahut kathor satya kehte hain:

Tumne rajya ka bhar diya hai:

Duryodhana,
Shakuni,
Dushasana,
Karna

jaise logon ko.

Isse rajya ka kalyan kaise hoga?

Pandav tumhe pita ke samaan maante hain.

Un par hi apna bharosa rakho; wahi tumhare vaastavik putra ke samaan hain.

Is Adhyay ka Saar
Daya sabse bada teerth hai.
Rajya ya bhoomi ke liye kabhi jhooth nahi bolna chahiye.
Prahlada ne apne putra ke viruddh jaakar bhi satya ka saath diya.
Devata shastra se nahi, sadbuddhi dekar raksha karte hain.
Asli gun sankat mein pehchane jaate hain.
Satya, Kshama, Daya aur Santosh dharma ke sarvottam stambh hain.
Vidura ka antim sandesh spasht hai: Duryodhana aur uske durjan salahkaron par bharosa chhodkar Pandavon ke saath nyay karo; wahi Kuru vansh ko bacha sakta hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.36
        with st.expander("Section 5.1.36  Section XXXVI"):
            text1 = """ 
Section XXXVI – Vidura Niti (Part 4): Krodh, Mitrata, Uchch Kul aur Atma-Sanyam

Is adhyay mein Vidura ek aur gahra niti-upadesh dete hain. Pehle ve Sadhya devata aur Atri-putra Rishi ka samvad sunate hain, phir uchch kul (noble family), sachchi mitrata, indriya-nigrah aur ant mein Dhritarashtra ko Pandavon se shanti karne ki antim salah dete hain.

1. Sadhya Devataon ka Prashn

Vidura kehte hain ki ek samay Sadhya Devataon ne Atri Rishi ke putra se poocha:

"Humein bataiye ki sachcha dharma aur uttam jeevan kya hai."

Rishi ne bahut gahri niti batayi.

2. Gaali ka Uttar Kabhi Gaali se Mat Do

Rishi kehte hain:

Agar koi tumhari ninda kare—

uska jawab ninda se mat do,
use shanti se seh lo.

Kyon?

Jo ninda sah leta hai,
uska paap nindak ko milta hai,
aur nindak ka punya sehne wale ko prapt hota hai.

Yeh Mahabharata ka ek ati-prasiddh siddhant hai."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
3. Kathor Vachan Sabse Bada Astra

Vidura kehte hain:

Harsh words—

hriday ko jalate hain,
haddiyon tak dukh pahunchate hain,
jeevan bhar ghaav chhod dete hain.

Isliye:

Krodh se bole gaye shabd kabhi mat bolo.

4. Vani ka Chaar Star ka Siddhant

Vidura ek bahut prasiddh niti dete hain:

Maun (silence) sabse achha hai.
Agar bolna hi pade → Satya bolo.
Agar satya bolo → Madhur bolo.
Agar madhur bolo → Dharma ke anukul bolo.

Yeh Bharatiya niti-shastra ke sabse mahan vakyon mein se ek mana jata hai.

5. Sangati ka Prabhav

Vidura kehte hain:

Vyakti vaisa hi ban jaata hai—

jiske saath rehta hai,
jise apna adarsh maanta hai,
jaisa banna chahta hai.

Isliye:

Achchhe logon ki sangat sabse bada dhan hai.

6. Uttam, Madhyam aur Nikrisht Vyakti
Uttam Vyakti
sabka bhala chahta hai,
kisi ka ahit nahi chahta,
satyavaadi,
vinamra,
indriya-jit.
Madhyam Vyakti
jhoothi tasalli nahi deta,
vaada nibhata hai,
doosron ki kamzori par nazar rakhta hai.
Nikrisht Vyakti
krodhi,
akritagya,
kisi ka dost nahi,
dusht hriday wala,
hamesha doosron ki unnati se jalan karta hai.
7. Uchch Kul (Noble Family) Kisey Kehte Hain?

Dhritarashtra poochte hain:

"Ucch kul ki pehchan kya hai?"

Vidura jawab dete hain:

Ucch kul wahi hai jahan:

Tapasya
Atma-sanyam
Veda ka gyan
Yajna
Pavitra vivaah
Annadaan
Dharma ka paalan

ho.

8. Kul Ko Kaun Girata Hai?

Vidura kehte hain:

Ucch kul neecha ban jaata hai jab—

dharma chhod diya jaye,
Brahmanon ka apmaan kiya jaye,
amanat mein khayanat ki jaye,
jhooth aur kapat badh jaye.

Aur ve kehte hain:

Dhan se nahi, aacharan se kul mahaan hota hai.

9. Sachcha Mitra Kaun?

Vidura kehte hain:

Sachcha dost woh nahi—

jisse darte ho,
jiske saamne hamesha sambhal kar rehna pade.

Sachcha dost woh hai—

jiske saamne pita jaisa bharosa ho,
jo raksha kare,
jo janm se sambandhi na hote hue bhi tumhara hit chahe.
10. Dukh ka Prabhav

Vidura kehte hain:

Shok—

sundarta ko khatam karta hai,
shakti ko kam karta hai,
buddhi ko nasht karta hai,
rog paida karta hai.

Isliye:

Ati shok mein doobna uchit nahi.

11. Dhritarashtra ka Pashchatap

Dhritarashtra pehli baar spasht roop se sweekar karte hain:

"Maine Yudhishthira ko dhokha diya hai."

Aur kehte hain:

"Ab mera man bhay se bhara hua hai."

Yeh unke antarik pashchatap ka prakat roop hai.

12. Vidura ka Upay

Vidura kehte hain:

Bhay door hota hai:

Atma-gyan se,
Tapasya se,
Indriya-nigrah se,
Lobh tyag se.
13. Rishtedaron Mein Jhagda Sabse Vinashkari

Vidura kehte hain:

Jin logon ka apne rishtedaron se jhagda ho—

unhe neend nahi aati,
dhan ka sukh nahi milta,
stri ka sukh nahi milta,
geet-sangeet bhi anand nahi deta.

Aise log ant mein vinash paate hain.

14. Ekta ki Shakti

Vidura do sundar udaharan dete hain:

Dhaage

Patle dhaage alag-alag kamzor hote hain.

Saath judkar bhaari bojh utha lete hain.

Ped

Ek akela bada ped aandhi mein gir sakta hai.

Jungle ke ped ek doosre ko sambhal kar khade rehte hain.

Isi tarah:

Parivaar ekjut rahe to use koi nahi hara sakta.

15. Krodh – Ek Vish

Vidura kehte hain:

Krodh—

kadva hai,
jalata hai,
rog jaisa hai,
lekin sharirik rog nahi.

Sirf buddhimaan hi ise pacha sakte hain.

Isliye:

Krodh ko nigal jao, shanti pao.

16. Dice Sabha ki Yaad

Vidura Dhritarashtra ko yaad dilate hain:

Jab Draupadi ko dice sabha mein apmaanit kiya gaya tha,

tab maine kaha tha:

"Imandaar log kapat se khel nahi khelte."

Aur maine Duryodhana ko rokne ko kaha tha.

Lekin tumne meri baat nahi maani.

17. Antim Salah

Vidura kehte hain:

Sahi niti hai—

Shakti + Komalta

Sirf bal par tikka hua rajya tikta nahi.

Jo rajya bal aur daya dono par chalta hai,

vah putra-pautron tak sthir rehta hai.

Ant mein ve kehte hain:

Pandav aur Kaurav ek hi mitra aur ek hi shatru rakhkar saath rahen. Pandavon ko apne hi putron ki tarah apnao. Duryodhana ko uske adharmik marg se hatao aur turant shanti karo.

Is Adhyay ka Saar
Gaali ka jawab gaali se nahi dena chahiye.
Sabse uttam vani: Maun → Satya → Madhur Satya → Dharma-anukul Satya.
Sangati vyakti ko gadh deti hai.
Uchch kul ka aadhar dhan nahi, aacharan hai.
Sachcha mitra wahi hai jiske saamne nishchint reh sako.
Krodh aur shok dono vinashak hain.
Parivaar ki ekta hi sabse badi shakti hai.
Vidura ka antim sandesh ek hi hai: Pandavon se shanti karo; wahi Kuru vansh ko bachane ka antim avsar hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.37
        with st.expander("Section 5.1.37  Section XXXVII"):
            text1 = """ 
Section XXXVII – Vidura Niti (Part 5): Murkhata, Ayu, Krodh, Rajniti aur Pandav-Kaurav Ekta

Is adhyay mein Vidura aur bhi kathor aur spasht niti batate hain. Ve murkhata ke lakshan, ayu kam karne wale dosh, sachche salahkar, sevak ke gun, rajniti aur ant mein Pandav-Kaurav ekta ki mahatta samjhate hain.

1. 17 Prakar ke Murkh (Fools)

Vidura kehte hain ki Manu ne 17 prakar ke murkh bataye hain. Aise log asambhav kaam karna chahte hain—jaise hawa ko pakadna ya indradhanush ko modna.

Kuchh pramukh murkh:

Jo apne se adhik shaktishali se bina soche dushmani kare.
Jo dushman ki chaplusi kare.
Jo apni hi patni ki burai kare.
Jo diya hua vaada mukar jaye.
Jo jhooth ko sach sabit karne ki koshish kare.
Jo apne achhe kaam ka dikhava kare.
Jo uchch kul mein janm lekar nich karm kare.

Vidura kehte hain ki aise log narak ke adhikari hote hain."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Dusron ke Saath Waisa Hi Vyavahar Karo

Vidura ka siddhant:

Imaandar ke saath imaandari.
Kapati ke saath satarkata aur uski bhasha mein vyavahar.

Yeh samajik niti ka niyam hai.

3. Chhe Talware Jo Ayu Kam Kar Deti Hain

Dhritarashtra poochte hain:

Agar manushya ki ayu 100 varsh hai, to sab itna nahi jeete kyon?

Vidura jawab dete hain:

Ye 6 dosh ayu ko kaat dete hain:

Ati ahankar
Ati bolna
Ati khana
Krodh
Bhog-vilas ki adhik ichchha
Parivar ke andar jhagda

Ye hi manushya ko maarte hain, mrityu nahi.

4. Kaun Brahmahatya ke Paapi Samaan Hai?

Vidura kuchh aise karm batate hain jo bahut gambhir paap ke saman mane gaye hain, jaise:

Vishwas karne wale ki patni ka apaharan.
Guru-patni ka apmaan.
Brahmanon ki bhoomi chheenna.
Sharan maangne wale ko maar dena.

Aise karmon ke liye prayaschitta avashyak hai.

5. Swarg Kisey Milta Hai?

Vidura kehte hain ki swarg us vyakti ko milta hai jo:

gyani ho,
niti jaanta ho,
daani ho,
pehle devata aur pitron ko arpan karke bhojan kare,
kisi se irsha na kare,
satyavaadi ho,
vinamra ho.
6. Kadvi Lekin Hitkari Baat

Vidura kehte hain:

Madhur bolne wale bahut mil jaate hain.

Lekin:

kadvi par hitkari baat bolne wala,
aur use sunne wala,

bahut durlabh hai.

Yahi sachcha mantri hota hai.

7. Rajniti ka Mahavakya

Vidura ka prasiddh niti-vachan:

Parivar ke liye ek vyakti ka balidan.
Gaon ke liye ek parivar ka balidan.
Rajya ke liye ek gaon ka balidan.
Atma ke liye poori prithvi ka balidan bhi uchit hai.

Yeh Bharatiya rajniti ka ek prasiddh siddhant hai.

8. Jua (Gambling) ka Vinash

Vidura yaad dilate hain:

Maine dice ke samay bhi mana kiya tha.

Jua hamesha:

jhagda,
vair,
vinash

lata hai.

Lekin Dhritarashtra ne meri baat nahi maani.

9. Pandav aur Kaurav ki Tulna

Vidura bahut prabhavshali upma dete hain:

Tum Pandavon jaise moron ko chhodkar apne kauwon jaise putron ko bachane ki koshish kar rahe ho.

Aur:

Sheron ko chhodkar geedaron ko bacha rahe ho.

Yeh Duryodhana aur Pandavon ke charitra ki tulna hai.

10. Achha Raja aur Achha Sevak

Vidura kehte hain:

Achha raja:

wafadar sevakon par bina wajah krodh nahi karta,
unka vetan nahi rokta,
yogya logon se mitrata karta hai.

Achha sevak:

malik ki ichchha samajhta hai,
imaandar hota hai,
apni aur shatru ki shakti jaanta hai,
hamesha hit ki baat karta hai.

Aisa sevak raja ka "doosra swaroop" hota hai.

11. Uttam Sevak ke 8 Gun

Vidura ke anusaar uttam sevak mein hone chahiye:

ahankar ka abhav,
kshamata,
aalas na karna,
daya,
shuddhata,
bhrashtachar se door rehna,
achha kul,
gambhir aur santulit vaani.
12. Kisse Madad Nahi Maangni Chahiye

Vidura kehte hain:

Kabhi bhi sahayata na maango:

kanjoos se,
doosron ki burai karne wale se,
shastra na jaane wale se,
krur vyakti se,
akritagya se,
jhagda karne wale se.
13. Jeevan ka Antim Ashram

Vidura paramparik jeevan vyavastha batate hain:

Santan ko sthapit karo.
Betiyon ka uchit vivaah karo.
Phir vanaprastha ki or badho aur Ishwar ki upasana karo.
14. Pandavon se Yuddh ke Parinaam

Vidura Dhritarashtra ko chetavani dete hain ki yuddh se:

Bhai-bhai ke shatru ban jayenge.
Nirantar chinta rahegi.
Kuru vansh ki kirti nasht hogi.
Shatru khush honge.
15. Jungle aur Sher ki Prasiddh Upma

Vidura kehte hain:

Kaurav van hain. Pandav us van ke sher hain.

Sher bina jungle ke nahi reh sakta.
Jungle bina sher ke surakshit nahi rehta.

Isliye:

Na jungle ko sher se alag karo, na sher ko jungle se.

Yeh Mahabharata ki sabse prasiddh rajnaitik upmaon mein se ek hai.

16. Panch Prakar ki Shakti

Vidura kehte hain ki manushya ki 5 shaktiyan hoti hain:

Bahubal (sabse nichli shakti)
Achhe salahkaron ki shakti
Dhan ki shakti
Uchch janm ki shakti
Buddhi ki shakti (sabse shreshth)

Sabse mahan bal buddhi hai.

17. Antim Chetavani

Vidura ant mein kehte hain:

Pandav agni ki tarah hain.

Abhi ve shant dikh rahe hain, jaise lakdi ke andar chhupi hui aag.

Lekin agar unhe bhadka diya gaya,

to ve poore van ko jala denge.

Aur ant mein phir wahi upma dete hain:

Tumhare putra bel (creeper) jaise hain, Pandav sal-vriksh aur sher jaise hain. Bel bade vriksh ke sahare hi jeeti hai. Isliye Pandavon ko nasht karna tumhare apne vansh ko nasht karna hoga.

Is Adhyay ka Saar
17 prakar ke murkhon se bachna chahiye.
Ahankar, ati-bhojan, krodh aur parivarik jhagde ayu kam kar dete hain.
Kadvi lekin hitkari salah sabse mahan salah hai.
Raja ko yogya sevakon ka samman karna chahiye.
Sabse bada bal buddhi ka bal hai.
Jua aur lobh rajya ka vinash karte hain.
Pandav aur Kaurav ek doosre ke virodhi nahi, ek doosre ke sahayak hone chahiye.
Vidura ka antim sandesh spasht hai: Pandav aur Kaurav saath rahenge to Kuru vansh bachega; yuddh hua to dono ka vinash nishchit hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.38
        with st.expander("Section 5.1.38  Section XXXVIII"):
            text1 = """ 
Section XXXVIII – Vidura Niti (Part 6): Atithi, Grihastha, Rajniti aur Gupt Mantrana

Is adhyay mein Vidura grihastha-dharma, mehmaan-nawazi (atithi satkar), raja ki gupt niti, mantriyon ka chayan aur vyaktitva ke gunon par upadesh dete hain. Ant mein ve phir Dhritarashtra ko Duryodhana ko chunne ki bhool yaad dilate hain.

1. Atithi ka Swagat Kaise Kare?

Vidura kehte hain ki jab koi vriddh aur sammanit vyakti ghar aaye to:

uthkar uska swagat karo,
pranam karo,
baithne ke liye aasan do,
paani do,
pair dhulvao,
kushal-mangal poochho,
phir bhojan karao.

Yahi grihastha ka dharma hai."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Kanjoosi Sabse Badi Kami

Vidura kehte hain:

Jo Brahmana ya yogya atithi:

paani,
madhu,
dahi,
gau-daan

grahan kiye bina laut jaye sirf isliye ki ghar ka malik kanjoos hai ya ichchha se daan nahi de raha, to aisa grihastha vyarth jeevan jeeta hai.

Arth:
Atithi satkar dhan se nahi, bhavna se hota hai.

3. Kaun Sa Vyapar Brahmana Ko Nahi Karna Chahiye?

Vidura batate hain ki Brahmana ko in vastuon ka vyapar nahi karna chahiye:

namak,
paka hua bhojan,
doodh,
dahi,
ghee,
tel,
shahad,
til,
maans,
phal,
jad,
sabzi,
sugandh,
gud,
rangin vastra.

Yeh us samay ke varnashrama-dharma ke sandarbh mein kaha gaya hai.

4. Sachcha Yogi Kaun Hai?

Vidura ke anusaar sachcha yogi vah hai jo:

krodh se pare ho,
shok se pare ho,
mitra aur shatru mein samaan rahe,
prashansa aur ninda dono se prabhavit na ho,
sukh-dukh se upar uth gaya ho.

Yeh Bhagavad Gita ke sthitaprajna ke varnan se milta-julta hai.

5. Buddhimaan Vyakti Se Kabhi Dushmani Mat Karo

Vidura kehte hain:

Agar tumne kisi buddhimaan vyakti ke saath anyay kiya hai, to yeh mat socho ki door rehkar bach jaoge.

Unki "baahen bahut lambi hoti hain" — arthaat unki buddhi aur prabhav bahut door tak pahunchta hai.

6. Vishwas Kis Par Kare?

Vidura ka santulit siddhant:

Jo avishwas ke yogya ho us par kabhi vishwas mat karo.
Jo vishwas ke yogya ho us par bhi andha vishwas mat karo.

Ati-vishwas bhi vinash ka kaaran ban sakta hai.

7. Patni ke Prati Vyavahar

Vidura kehte hain:

Patni se madhur bhasha mein baat karo.
Uska samman karo.
Uski raksha karo.
Lekin uska daas mat ban jao.

Ve patni ko "ghar ki Lakshmi" kehte hain.

8. Ghar Ki Jimmedariyon Ka Vibhajan

Vidura ek rochak vyavastha batate hain:

Antarpur (ghar ke andar) – pita dekhe.
Rasoi – mata dekhe.
Gayein – apna sabse vishwasniya vyakti dekhe.
Kheti – swayam dekhni chahiye.

Yeh prabandhan (management) ka siddhant hai.

9. Rajya Ke Rahasya

Vidura kehte hain:

Apni yojana kabhi pehle mat batao.

Kaam hone ke baad hi logon ko pata chalna chahiye.

Isliye:

Rajnaitik mantrana hamesha gupt jagah par karo.
Rajya ke rahasya har dost ko mat batao.
Mantri ko achhi tarah parakh kar hi chunna chahiye.

Yeh prachin intelligence aur statecraft ka siddhant hai.

10. Uttam Raja Ka Lakshan

Sabse uttam raja vah hai:

jiske mantri uske nirnay tab jaane jab kaam ho chuka ho,
jiske rahasya surakshit rahen,
jo swayam rajkosh par nazar rakhe,
jo khud kaam ki dekhrekh kare.
11. Raja Aur Dhan

Vidura kehte hain:

Raja ko:

sirf apne liye dhan ikattha nahi karna chahiye.
Rajya ka dhan yogya sevakon mein baantna chahiye.

Achha shasak apni praja aur sevakon ko saath lekar chalta hai.

12. Shatru Ko Kab Chhodna Chahiye?

Vidura ka kathor rajnaitik siddhant:

Agar shatru bahut shaktishali hai aur tum kamzor ho, to kuch samay usse sandhi karo.
Lekin jab tum shaktishali ho jao, tab use dobara khatra banne se pehle rok do.

Yeh rajneeti ka vyavaharik drishtikon hai.

13. Kiske Upar Krodh Nahi Karna Chahiye?

Vidura kehte hain:

In par krodh ko niyantrit rakho:

Devata
Raja
Brahmana
Vriddh
Bachche
Asahay log

Yeh maryada ka prateek hai.

14. Samriddhi Ki Saat Lakdiyan (Fuel of Prosperity)

Vidura kehte hain ki samriddhi ki agni ko jalaye rakhne wale saat gun hain:

Buddhi
Shant chitta
Atma-sanyam
Shuddhata
Kathor vaani ka abhav
Mitron ke prati komalta
Imaandari

Jahan ye gun hote hain, wahan samriddhi tikti hai.

15. Kis Vyakti Se Door Rahna Chahiye?

Vidura kehte hain:

Door raho usse jo:

dusron ka adhikar chheen le,
akritagya ho,
besharam ho,
dusht ho,
jhoothe aarop lagata ho.

Aise log kabhi chain ki neend nahi so sakte.

16. Kaun Achha Neta Nahi Ban Sakta?

Vidura kehte hain:

Jo log:

striyon ke moh mein,
kapti logon ke prabhav mein,
bachchon ki soch par,
ya dusht logon ke margdarshan par chalenge,

ve safal nahi honge.

Neta ko vivek se nirnay lena chahiye.

17. Dhritarashtra Ki Sabse Badi Galti

Vidura ant mein phir wahi baat kehte hain:

Tumne Arjuna, Bhima aur Yudhishthira jaise mahan dhanurdharon ko chhodkar poore samrajya ka bhar Duryodhana par rakh diya.

Isliye:

Jaise Raja Bali ka vaibhav gir gaya tha,

waise hi tumhari samriddhi bhi jaldi girne wali hai.

Is Adhyay ka Saar
Atithi ka samman grihastha ka pratham dharma hai.
Patni ka samman karo, par vivek banaye rakho.
Rajya ke rahasya kabhi prakat na karo.
Mantri ko bahut parakh kar chuno.
Raja ko dhan baantna chahiye, sab kuch swayam nahi rakhna chahiye.
Shatru ke saath niti aur samay ka dhyan rakho.
Samriddhi buddhi, sanyam aur satya se tikti hai.
Vidura phir Dhritarashtra ko chetavani dete hain ki Pandavon ko nazarandaaz karke Duryodhana par bharosa karna Kuru vansh ke vinash ka kaaran banega."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.39
        with st.expander("Section 5.1.39  Section XXXIX"):
            text1 = """ 
Section XXXIX – Vidura Niti (Part 7): Duryodhana ko Tyagna, Achhe Mitra, Rajneeti aur Dharma

Is adhyay mein Dhritarashtra apni majboori batata hai ki sab kuch bhagya ke adheen hai. Vidura ise sveekar nahi karte aur phir se Duryodhana ko bachane ke bajaay usse tyagne ki salah dete hain. Yah Vidura Niti ke sabse mahatvapurna adhyayon mein se ek hai.

1. Dhritarashtra ki Soch – "Sab Bhagya Hai"

Dhritarashtra kehte hain:

Insaan apni safalta ya asafalta ka malik nahi hai.
Hum sab Bhagwan ke haath ki kathputli hain.
Isliye mujhe aur upadesh do.

Yeh Dhritarashtra ka favourite excuse hai: zimmedari se bachne ke liye sab kuch destiny par daal dena."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Vidura ki Sabse Badi Yaad-Dihani

Vidura kehte hain:

Jab Duryodhana paida hua tha tabhi maine kaha tha:

"Ek putra ko chhod do, tab tumhare baaki sau putra bach jayenge."

Lekin Dhritarashtra ne mana kar diya.

Vidura fir samjhate hain:

Chhota nuksan agar bada laabh laaye to vah laabh hai.
Aur jo chhota laabh aage chal kar bada vinash laaye, vah asal mein nuksan hai.
3. Gun Dhan Se Bade Hain

Vidura kehte hain:

Do prakaar ke log prasiddh hote hain:

gunon ke kaaran
dhan ke kaaran

Lekin:

Gunheen dhanvaan se door raho.

Character > Wealth.

4. Kis Sangati Se Bachna Chahiye?

Door raho:

jhagadalu log
lalchi
besharam
kapati
paapi
doosron ki burai karne wale

Aise log kabhi achhe mitra nahi hote.

5. Rishtedaaron Ka Dharm

Vidura kehte hain:

Garib, kamzor aur dukhi rishtedaaron ki sahayata karo.

Rishtedaar:

bacha bhi sakte hain,
barbaad bhi kar sakte hain.

Isliye:

Apne kul ko saath lekar chalo.

6. Pandavon Ko Kuchh Gaon De Do

Vidura fir seedha Dhritarashtra se kehte hain:

Pandavon ko:

"Kuch gaon hi de do."

Isse:

tumhara yash badega,
paap dhul jayega,
vansh bach jayega.

Yeh wahi salah hai jo baad mein Yudhishthira "paanch gaon" ke roop mein maangte hain.

7. Baad Mein Pachtana Mat

Vidura chetavani dete hain:

Aaj agar tumne kuch nahi kiya to kal:

ya Pandav marenge,
ya tumhare putra.

Aur tab tum sirf pachtate rah jaoge.

8. Rajya Ke Rahasya Kaise Leak Hote Hain?

Vidura bahut practical rajneeti sikhate hain.

Rahasya 6 kaaranon se bahar nikalte hain:

Nasha
Ati neend
Guptcharon par dhyan na dena
Apne vyavahar se sanket de dena
Dusht mantri par bharosa
Ayogya doot (messenger)

Jo raja in sab ko rok leta hai wahi safal hota hai.

9. Achha Mitra Kaun?

Vidura ke anusaar achha dost vah hai jo:

satyavaadi ho,
kritagy ho,
udaar ho,
indriya-jit ho,
wafadaar ho,
kabhi mitra ko na chhode.

Aise vyakti ko hi mitra banana chahiye.

10. Samriddhi Kis Se Aati Hai?

Prosperity ke mool:

sahi prayas
samay ki samajh
sahi jagah
sahi saadhan
shastra gyaan
imaandari
achhe logon ki sangat

Aur sabse bada:

Perseverance (lagataar prayas).

11. Kshama Ki Mahima

Vidura kehte hain:

Kamzor maaf kare majboori se.
Shaktishaali maaf kare dharma ke liye.
Sabse mahaan wahi hai jo shakti hote hue bhi kshama kare.
12. Samriddhi Kinse Door Bhaagti Hai?

Lakshmi unke paas nahi tikti jo:

sada dukhi rehte hain,
bure kaam karte hain,
mehnat nahi karte,
indriyon ke gulaam hain,
prayatna chhod dete hain.
13. Dharma Ka Saar

Vidura ek bahut prasiddh siddhant dete hain:

Jo tum apne liye pasand nahi karte, vah doosron ke saath kabhi mat karo.

Ve kehte hain:

Yahi sankshipt roop mein Dharma hai.

Baaki sab usi ke vistaar hain.

14. Dushton Ko Kaise Haraye?

Vidura kehte hain:

Krodh → Kshama se jeeto.
Dusht → Imaandari se jeeto.
Kanjoos → Daan se jeeto.
Jhooth → Satya se jeeto.
15. Kis Par Vishwas Nahi Karna Chahiye?

Vishwas na karo:

kapati
chor
darpok
aalsi
ahankari
akritagya
nastik (is sandarbh mein jo naitikta ko hi asweekar kare)

Vidura yahaan rajneetik satarkata ki baat kar rahe hain.

16. Dhan Se Trishna Kabhi Khatm Nahi Hoti

Vidura kehte hain:

Chahe:

sona,
dhan,
anaaj,
pashu,
striyan,

poori prithvi par kyon na mil jaaye,

ek vyakti ki ichchha tab bhi poori nahi hoti.

Isliye:

Lobh chhod do.

17. Antim Sandesh Dhritarashtra Ko

Vidura poore adhyay ka saar ek vaakya mein dete hain:

Pandavon aur apne putron ke saath samaan vyavahar karo.

Yahi tumhare, Kuru vansh aur poore rajya ke hit mein hai.

Is Adhyay ka Saar
Bhagya ka bahana bana kar kartavya se mat bhaago.
Kabhi-kabhi ek dusht vyakti ko rokna poore parivaar ko bachata hai.
Dhan se adhik mahatvapurna gun hain.
Achhi sangat jeevan banati hai, buri sangat vinash karti hai.
Rajya ke rahasya surakshit rakhna shasak ka kartavya hai.
Dharma ka saar: "Jo tum apne liye nahi chahte, vah doosron ke saath mat karo."
Ant mein Vidura phir Dhritarashtra se kehte hain ki Pandavon ko unka adhikar dekar samaan vyavahar karo—isi mein Kuru vansh ki raksha hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.40
        with st.expander("Section 5.1.40  Section XL"):
            text1 = """ 
Section XL – Vidura Niti (Part 8): Dharma Hi Sthayi Hai, Sab Kuchh Anitya Hai

Is adhyay mein Vidura apne upadesh ko aur gahra bana dete hain. Ve batate hain ki dhan, rajya aur sharir sab nashvar hain, lekin dharma aur karm hi vyakti ke saath jaate hain. Ant mein Dhritarashtra sveekar karta hai ki Vidura sahi hain, lekin kehta hai ki Duryodhana ke saamne aate hi uski buddhi badal jaati hai.

1. Achhe Logon Ka Samman Karo

Vidura kehte hain:

Jo vyakti:

sajjanon ka samman karta hai,
ahankaar chhod deta hai,
apni shakti ke anusaar hi kaam karta hai,

vah jaldi hi yash aur safalta prapt karta hai.

Kyon?

Kyunki sajjan log prasann hokar uska bhala karte hain."""
            create_image_text_layout(
                "attached_assets/chapter5/5.1.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
2. Adharma Se Mila Laabh Tyag Do

Vidura kehte hain:

Yadi koi bahut bada laabh bhi:

adharma se mil raha ho,

to use turant chhod dena chahiye.

Aisa vyakti:

saanp ki tarah purani khaal chhodkar naya jeevan pa leta hai.

3. Teen Paap Brahmahatya Ke Barabar

Vidura ke anusaar ye teen karm bahut bhayankar hain:

jhooth bolkar jeet hasil karna,
raja ke saath kapat karna,
guru ke saamne asatya ya kapat rakhna.

Ye Brahmahatya ke samaan paap ke roop mein bataye gaye hain.

4. Vidya Ke Dushman

Vidura kehte hain ki vidya ke teen shatru hain:

guru ki seva mein laparvahi,
jaldbazi,
ahankaar.

Aur vidyarthi ke saat dosh hain:

aalas
dhyan na dena
bhram
chanchalta
samay barbaad karna
ghamand
lobh

Yeh sab seekhne ki shakti ko nasht kar dete hain.

5. Vidya Aur Bhog Ek Saath Mushkil

Vidura ka prasiddh siddhant:

Jo sukh-bhog ka ichchhuk hai uske liye vidya mushkil hai.

Aur:

Jo sachchi vidya chahta hai use sukh-suvaidhayein chhodni padti hain.

Iska arth hai ki gahri shiksha tyag aur anushasan maangti hai.

6. Chaar Cheezein Kabhi Santusht Nahi Hoti

Vidura chaar udaharan dete hain:

Agni → indhan se kabhi nahi bharati.
Samudra → nadiyon se kabhi nahi bharata.
Mrityu → praaniyon se kabhi santusht nahi hoti.
Kaam (ichchha) → kabhi poori nahi hoti.

Sandesh:

Ichchhaon ka ant nahi hota.

7. Kya Kis Ko Nasht Karta Hai?

Vidura bahut sundar sutra dete hain:

Asha (hope) → dhairya ko maar deti hai.
Krodh → samriddhi ko.
Kanjoosi → yash ko.
Gai ki dekhbhal na karna → pashudhan ko.
Krodhit Brahmana → poore rajya ko.

Yeh pratikatmak roop se bataya gaya hai ki har vastu ka ek vinashak hota hai.

8. Dharma Kabhi Mat Chhodo

Vidura ka sabse mahan vakya:

Dharma ko kabhi mat chhodo—

chahe:

lalach ho,
dar ho,
praan bachane ki baat hi kyon na ho.

Kyonki:

Dharma nitya hai.
Sukh-dukh anitya hain.
9. Santosh Sabse Badi Sampatti

Vidura kehte hain:

Santosh hi sabse bada dhan hai.

Jo santusht hai wahi vastav mein samriddh hai.

10. Mrityu Ke Baad Kya Saath Jaata Hai?

Vidura bahut gahra varnan karte hain.

Jab vyakti mar jaata hai:

parivaar rota hai,
shareer ko shamshan le jaata hai,
agni shareer ko jala deti hai,
dhan doosre log baant lete hain.

Lekin:

Sirf do cheezein uske saath jaati hain:

Punya
Paap

Yahi uski asli sampatti hai.

11. Isliye Jeevan Bhar Dharma Kamao

Vidura kehte hain:

Dheere-dheere,

jeevan bhar,

punya ikattha karo.

Kyonki antim yatra mein wahi saath jaayega.

12. Atma Ek Nadi Hai

Vidura ek bahut sundar upama dete hain.

Atma ko ek pavitra nadi batate hain:

Satya uska jal hai.
Sanyam uske kinare hain.
Daya uski lehrein hain.
Dharma uska pavitra snaan hai.

Jo is nadi mein snaan karta hai, vah pavitra ho jaata hai.

13. Jeevan Ki Nadi

Vidura ek aur upama dete hain:

Jeevan ek nadi hai.

Usmein:

paanch indriyan paani hain,
kaam aur krodh magarmachh hain,
punarjanm uski bhavaren hain.

Is nadi ko paar karne ki naav hai:

Atma-sanyam.

14. Indriya Nigrah

Vidura batate hain:

Niyantran ka kram:

Dhairya se kaam aur bhook ko sambhalo.
Aankhon se haath-pair ko niyantrit karo.
Mann se aankh-kaan ko niyantrit karo.
Karmon se mann aur vaani ko shuddh rakho.

Yeh poori self-discipline ki prakriya hai.

15. Chaar Varnon Ka Dharma

Vidura sankshipt roop mein batate hain:

Brahmana
Veda adhyayan
Satya
Shauch
Guru seva
Kshatriya
Praja ki raksha
Dharma yuddha
Gau aur Brahmana ki raksha
Vaisya
Veda ka adhyayan
Daan
Vyapar aur samaj ki seva
Shudra
Teenon varn ki seva
Imaandari se jeevan

Yeh Mahabharata ke samay ki varnashrama vyavastha ke sandarbh mein kaha gaya hai.

16. Vidura Ki Antim Vinanti

Vidura kehte hain:

Yudhishthira Kshatriya hain.

Unka kartavya hai:

Rajya chalana.

Isliye:

Unhe unka rajya wapas de do.

Yahi tumhara dharma hai.

17. Dhritarashtra Ka Dard

Dhritarashtra ant mein ek bahut mahatvapurna sveekar karta hai:

"Mujhe pata hai tum sahi ho."

"Mera mann bhi Pandavon ki taraf jata hai."

"Lekin jaise hi main Duryodhana ke paas jaata hoon, meri buddhi badal jaati hai."

Aur phir wahi kehta hai:

"Shayad sab kuchh bhagya hi hai."

Yahi Dhritarashtra ki sabse badi kamzori thi—sach ko jaanne ke baad bhi us par amal na kar pana.

Is Adhyay ka Saar
Sajjanon ka samman safalta ka mool hai.
Adharma se mila laabh tyag dena chahiye.
Vidya aur bhog dono ka poorn anand ek saath mushkil hai.
Ichchha kabhi poori nahi hoti.
Dharma hi nitya hai; dhan, sharir aur rajya sab anitya hain.
Mrityu ke baad sirf punya aur paap saath jaate hain.
Santosh sabse bada dhan hai.
Jeevan ki nadi ko atma-sanyam ki naav se hi paar kiya ja sakta hai.
Dhritarashtra ko sach ka gyaan tha, lekin putra-moh ne uske vivek ko baar-baar hara diya."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
    # ==================================================
    # Chapter 5.2 - Sanatsujata Parva
    # ==================================================

    with st.expander("Chapter 5.2  Sanatsujata Parva"):

        # Section 5.2.1
        with st.expander("Section 5.2.1  Section XLI"):
            text1 = """ 
            Section XLI – Sanat-Sujata Ka Aagman

Dhritarashtra ne kaha, "Vidura, agar tumhare paas aur bhi koi gyaan hai, to mujhe batao. Main dhyaan se sunne ke liye taiyaar hoon. Tumhari baatein bahut acchi lagti hain."

Vidura ne vinamrata se kaha, "Maharaj, ek amar aur mahaan Rishi hain – Sanat-Sujata. Unhone poori zindagi brahmacharya ka paalan kiya hai. Unka gyaan anant hai. Wahi aapke sabhi sawaalon ka sahi uttar de sakte hain."

Dhritarashtra ne poocha, "Kya tum unki baatein nahi jaante? Agar jaante ho, to tum hi mujhe bata do." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Vidura bole, "Main apni maryada jaanta hoon. Itne gehre adhyatmik rahasya batana mera adhikaar nahi hai. Sirf Sanat-Sujata jaise mahaan Rishi hi in vishayon ko poori tarah samjha sakte hain."

Dhritarashtra ne phir poocha, "Main un mahaan Rishi se kaise mil sakta hoon?"

Vidura ne turant Sanat-Sujata ka dhyaan kiya.

Rishi ne mehsoos kiya ki unhe yaad kiya gaya hai. Ve turant wahan prakat ho gaye.

Vidura ne unka bahut samman ke saath swaagat kiya. Jab Rishi aaraam se baith gaye, tab Vidura ne kaha,

"Maharaj Dhritarashtra ke mann mein bahut gehre sawaal hain. Main unka uttar nahi de sakta. Kripya aap unhe satya ka gyaan dijiye. Aapki shiksha se ye jeevan ke har sukh-dukh, laabh-haani, budhaape, mrityu, bhay, irshya, bhookh, pyaas, ahankaar, kaamna aur krodh ko samajhkar shaanti paa sakenge." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.2
        with st.expander("Section 5.2.2  Section XLII"):
            text1 = """ 
Section XLII – Asli Mrityu Kya Hai?

Vidura ki baat sunne ke baad, Dhritarashtra ne Rishi Sanat-Sujata se ek gehra sawaal poocha.

Unhone kaha, "Maine suna hai ki aap kehte hain ki mrityu hoti hi nahi. Lekin log to mrityu se bachne ke liye tapasya bhi karte hain. In dono baaton mein sach kya hai?"

Sanat-Sujata muskuraye aur bole,

"Dono baatein apni jagah sahi hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Phir unhone samjhaya,

"Asli mrityu sharir ka khatam hona nahi hai. Asli mrityu hai agyaan. Aur sachcha gyaan hi amarta ka raasta hai."

Unhone kaha,

"Jab insaan sach ko nahi samajhta, tab uske andar lalach, gussa aur ahankaar badhne lagte hain. Yehi usse dukh aur barbaadi ki taraf le jaate hain."

"Jo sirf apni ichchhaon ke peeche bhaagta hai, woh baar-baar dukh aur janm-mrityu ke chakra mein phans jaata hai."

Lekin jo apne mann aur ichchhaon par control kar leta hai, woh is chakra se bahar nikal sakta hai.

Dhritarashtra ne phir poocha,

"Agar gyaan sabse bada hai, to Vedo mein bataye gaye yagya aur dharmik karm kyun kiye jaate hain?"

Sanat-Sujata bole,

"Achhe karm bhi zaroori hain. Lekin agar mann mein ichchha aur moh baaki ho, to unka phal sirf kuch samay ke liye milta hai. Sachchi mukti tab milti hai jab insaan apni ichchhaon ko chhodkar sachche gyaan ko apnaata hai."

Dhritarashtra ne aur sawaal pooche. Unhone Brahman, atma aur dharm ka matlab samajhna chaha.

Sanat-Sujata ne dhairya se har baat samjhayi.

Ant mein unhone kaha,

"Sach bolna, seedha rehna, vinamrata rakhna, apne mann par control rakhna, shuddh jeevan jeena aur gyaan paana—yeh chhe gun insaan ko andhkaar se nikaal kar sachchi khushi aur mukti ki taraf le jaate hain."  """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.3
        with st.expander("Section 5.2.3  Section XLIII"):
            text1 = """ Section XLIII – Asli Tapasya Aur Sachcha Gyaan

Dhritarashtra ne poocha,

"Asli maun kya hai? Kya sirf chup rehna hi maun hai, ya kuch aur? Aur kya isse moksha mil sakta hai?"

Sanat-Sujata bole, """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Asli maun sirf chup rehna nahi hai. Jab mann shaant ho jaata hai aur insaan apni atma ko pehchaan leta hai, wahi sachcha maun hai."

Dhritarashtra ne phir poocha,

"Agar koi Vedo ka bahut gyaan rakhta ho, lekin bure kaam kare, to kya Veda usse bacha lenge?"

Sanat-Sujata ne kaha,

"Nahi. Sirf Veda padh lena kaafi nahi hai. Agar insaan apni indriyon par control nahi karta aur dharm par nahi chalta, to Veda bhi uski madad nahi kar sakte."

Unhone aage samjhaya,

"Tapasya tabhi safal hoti hai jab usme ahankaar, lalach aur dikhawa na ho. Agar ye sab ho, to tapasya ka koi fayda nahi."

Phir unhone bataya ki insaan ko kin buri aadaton se bachna chahiye.

Gussa, kaam, lalach, ahankaar, irshya, doosron ki burai aur doosron ko dukh dena insaan ko galat raaste par le jaate hain.

Lekin kuch achhe gun hamesha apnane chahiye.

Sach bolna, daya rakhna, apne mann par control rakhna, vinamrata, dhairya, daan aur gyaan insaan ko mahaan bana dete hain.

Sanat-Sujata ne kaha,

"Asli tyaag sirf cheezen chhodna nahi hai. Asli tyaag apni ichchhaon aur ahankaar ko chhodna hai."

Ant mein unhone sabse bada sach bataya.

"Sirf kitaabein padhne se koi gyani nahi banta. Jo sach ke raaste par chalta hai, apne mann ko jeet leta hai aur apni atma ko pehchaan leta hai, wahi sachcha gyani hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.4
        with st.expander("Section 5.2.4  Section XLIV"):
            text1 = """ 
Section XLIV – Brahman Ko Kaise Paaya Jaaye?

Dhritarashtra ne kaha,

"Hey Rishi, aapki baatein bahut adbhut hain. Kripya mujhe aur gyaan dijiye. Main aisi baatein sunna chahta hoon jo sirf sach aur atma se judi hon."

Sanat-Sujata bole,

"Brahman ko jaldi nahi paaya ja sakta. Jab insaan apni indriyon aur mann par poora control kar leta hai, tab uske andar sachcha gyaan prakat hota hai. Yeh sirf Brahmacharya aur anushasan se milta hai."

Dhritarashtra ne poocha, """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Agar gyaan pehle se hi mann mein hai, to phir amarta kaise milti hai?"

Sanat-Sujata bole,

"Gyaan mann mein zaroor hota hai, lekin chhupa hua hota hai. Shuddh buddhi, anushasan aur Guru ki shiksha se woh saamne aata hai. Jab yeh gyaan mil jaata hai, tab insaan Brahman ko jaan leta hai."

Dhritarashtra ne phir poocha,

"Achha Brahmacharya kaise kiya jaata hai?"

Sanat-Sujata ne kaha,

"Sabse pehle Guru ka samman karo. Unki seva dil se karo. Kabhi gussa ya ahankaar mat rakho."

"Guru ki baat dhyaan se suno. Unke parivaar ka bhi utna hi aadar karo jitna Guru ka karte ho."

"Hamesha yaad rakho ki Guru ne tumhe gyaan diya hai. Unke prati hamesha kritagy raho."

"Aur jab tak Guru ki anumati aur Guru Dakshina poori na ho, tab tak apni padhai ko adhura mat chhodo."

Sanat-Sujata bole,

"Isi anushasan se Devtaon ne apni mahanta paayi. Rishiyon ne Brahman ko jaana. Aur Surya bhi apna kartavya nibhata hai."

Phir unhone kaha,

"Achhe karm sirf kuch samay ka phal dete hain. Lekin sachcha gyaan hamesha ke liye mukti deta hai. Brahman ko paane ka asli raasta gyaan hi hai."

Dhritarashtra ne ant mein poocha,

"Brahman ka rang kaisa hai? Kya woh safed, laal ya neela hai?"

Sanat-Sujata muskuraye aur bole,

"Brahman ka koi ek rang ya roop nahi hai. Use aankhon se nahi dekha ja sakta."

"Wahi har jagah hai. Wahi poori srishti ka aadhaar hai. Sab kuch usi se aata hai aur ant mein usi mein laut jaata hai."

"Jo is sach ko samajh leta hai, wahi janm aur mrityu ke chakra se mukt ho jaata hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.5
        with st.expander("Section 5.2.5  Section XLV"):
            text1 = """ Section XLV – Achha Insaan Kaun Hota Hai?

Sanat-Sujata bole,

"Kuch buri aadatein insaan ki zindagi barbaad kar deti hain."

Unhone bataya,

"Dukh mein doobna, gussa, lalach, kaam, agyaan, aalas, irshya, ahankaar, hamesha aur paane ki ichchha, zyada moh aur buri baatein karna—ye sab insaan ko galat raaste par le jaate hain."

"Jab aise logon ke paas dhan aa jaata hai, to ve aur bhi ghamandi ho jaate hain. Ve doosron ka samman nahi karte aur sirf apni khushi ke baare mein sochte hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Phir Sanat-Sujata ne bataya ki ek achhe insaan ke gun kya hote hain.

"Sach bolna, dharm par chalna, apne mann aur indriyon par control rakhna, santosh, vinamrata, tyaag, daya, daan, gyaan, dhairya aur maaf karna—ye sab mahaan gun hain."

"Jo in gunon ko apna leta hai, wahi sach mein safal insaan banta hai."

Phir unhone sachchi dosti ke lakshan bataye.

"Sachcha dost tumhari khushi mein khush hota hai aur tumhare dukh mein tumhare saath khada rehta hai."

"Zarurat padne par woh apni sabse pyari cheez bhi tumhare liye dene ko taiyaar hota hai."

"Aur kabhi bhi tumhara fayda uthaane ki koshish nahi karta."

Sanat-Sujata ne aage kaha,

"Apni indriyon par control rakhna hi asli tapasya hai. Lekin sirf achhe karm karna hi kaafi nahi hai."

"Bina sachche gyaan ke, bade se bada yagya ya pooja bhi insaan ko mukti nahi de sakti."

Ant mein unhone kaha,

"Jo apne mann ko shaant rakhta hai, tarif se ghamand nahi karta aur ninda se gussa nahi hota, wahi dheere-dheere Brahman ko praapt kar leta hai."

"Yahi sachcha gyaan hai, aur yahi mukti ka raasta hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            
                # Section 5.2.6
        with st.expander("Section 5.2.6  Section XLVI"):
            text1 = """ Section XLVI – Brahman Har Jagah Hai

Sanat-Sujata bole,

"Is poori srishti ka ek hi mool hai. Wahi Brahman hai. Wahi sabse shuddh, prakashmay aur hamesha se maujood hai."

"Surya ka prakash, prakriti ki shakti aur jeevan ki urja sab usi se aati hai."

Unhone kaha,

"Yogi apne mann ki aankhon se us Brahman ko dekhte hain. Use aam aankhon se nahi dekha ja sakta."

Phir unhone ek sundar udaaharan diya. """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Yeh sharir ek rath ki tarah hai. Ek din yeh khatam ho jaayega. Lekin atma amar hai. Agar indriyan aur mann sahi disha mein chalein, to insaan Brahman tak pahunch sakta hai."

Sanat-Sujata bole,

"Yeh duniya ek badi nadi ki tarah hai. Isme moh aur maya ka bahav hai. Bahut log isi mein uljhe rehte hain aur sach ko bhool jaate hain."

"Lekin jo gyaan pa leta hai, woh is maya se bahar nikal aata hai."

Unhone samjhaya,

"Sabhi jeevon ke andar wahi ek Paramatma rehta hai. Farq sirf itna hai ki kuch log use pehchaan lete hain aur kuch nahi."

"Jo apne mann ko shaant kar leta hai, sabka bhala chahta hai aur apne andar ki atma ko pehchaan leta hai, wahi sachcha gyani hai."

Sanat-Sujata ne ek aur chetavni di.

"Kuch log bahar se bahut dharmik dikhte hain, lekin andar se bure hote hain. Aise logon se hamesha saavdhan rehna."

Ant mein unhone sabse gehra satya bataya.

"Brahman har jeev ke hriday mein rehta hai. Wahi sabka mata hai, pita hai aur sabka aadhaar hai."

"Jo ise apne andar pehchaan leta hai, uske liye janm, mrityu aur dukh ka koi dar nahi rehta." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.7
        with st.expander("Section 5.2.7  Section XLVII"):
            text1 = """ Section XLVII – Sanjaya Ki Wapsi

Raat bhar Dhritarashtra, Vidura aur Rishi Sanat-Sujata ke saath gehri baatein karte rahe.

Subah hote hi Hastinapur ki rajsabha saj gayi.

Sabhagaar bahut sundar tha. Sone ki chamak, safed farsh, chandan ki khushboo aur shandaar aasan uski shobha badha rahe the.

Bhishma, Drona, Kripacharya, Shalya, Karna, Ashwatthama, Shakuni, Duryodhana aur doosre sabhi mahan yoddha wahan aa kar baith gaye.

Sabhi ek hi baat ka intezaar kar rahe the. """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Sanjaya Pandavon se milkar laut chuke the.

Thodi der baad dwarpal ne khabar di,

"Maharaj, Sanjaya aa gaye hain. Unka rath Pandavon se laut aaya hai."

Sanjaya turant sabha mein aaye aur sabko pranam kiya.

Phir unhone kaha,

"Main Pandavon se milkar wapas aaya hoon."

"Yudhishthira aur unke sabhi bhaiyon ne Kuru vansh ke har vyakti ko unki umar aur maryada ke anusaar pranam aur shubhkamnayein bheji hain."

Uske baad Sanjaya bole,

"Ab main aap sabko wahi sandesh sunaunga jo Dhritarashtra ke kehne par main Pandavon ke paas lekar gaya tha, aur jo jawab mujhe wahan se mila."

Is tarah sabha mein poori shaanti chha gayi.

Sabhi dhyaan se Pandavon ka sandesh sunne ke liye taiyaar ho gaye. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.8
        with st.expander("Section 5.2.8  Section XLVIII"):
            text1 = """ Section XLVIII – Arjuna Ka Antim Sandesh

Dhritarashtra ne Sanjaya se kaha,

"Sabke saamne batao, Arjuna ne kya sandesh bheja hai."

Sanjaya bole,

"Arjuna ne yeh baat Shri Krishna aur Yudhishthira ki maujoodgi mein kahi thi."

Arjuna ne kaha,

"Agar Duryodhana Yudhishthira ko unka haq ka rajya wapas nahi dega, to yuddh nishchit hai." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Humne bahut anyaay saha hai. Vanvaas bhi poora kiya aur agyaatvaas bhi. Ab hum apna adhikaar lekar hi rahenge."

Phir Arjuna ne Duryodhana ko chetavni di.

"Jab Bhima apni gada lekar yuddh mein utrega, tab tumhe apni galti ka ehsaas hoga."

"Jab Nakula aur Sahadeva apni veerta dikhayenge, tab tum pachtoge."

"Jab Abhimanyu, Draupadi ke putra, Dhrishtadyumna, Shikhandi, Satyaki, Virata aur Drupada yuddh mein aage badhenge, tab tum samajh jaoge ki yeh faisla kitna bhaari tha."

Phir Arjuna ne apni baat kahi.

"Aur jab tum mujhe Gandiva dhanush ke saath dekhoge, mere rath par Shri Krishna saarathi honge, tab tumhe samajh aa jayega ki jeet kiski hogi."

"Mere baan bijli ki tarah girenge. Dushman ki sena har taraf bikhar jaayegi."

Iske baad Arjuna ne Shri Krishna ki mahima batayi.

"Shri Krishna sirf ek mahaan yoddha nahi hain. Unhone bahut bade-bade asuron aur dusht rajaon ka vinaash kiya hai."

"Jinke saath Shri Krishna khade hote hain, unki jeet lagbhag nishchit hoti hai."

Phir Arjuna ne apna vishwas jataya.

"Maine Shri Krishna ko apna saathi chuna hai. Mujhe poora bharosa hai ki dharm ki hi jeet hogi."

Ant mein Arjuna ne Sanjaya se kaha,

"Jaakar Duryodhana ko bata do. Agar woh abhi bhi shanti chahe, to sab bach sakte hain. Lekin agar woh yuddh chunta hai, to Kaurav sena ka vinaash nishchit hai."

Sabha mein yeh sandesh sunkar sab log gehri soch mein doob gaye.

Sabko samajh aa gaya ki ab shanti aur yuddh ke beech sirf Duryodhana ka faisla baaki tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.9
        with st.expander("Section 5.2.9  Section XLIX"):
            text1 = """ Section XLIX – Bhishma Ki Antim Chetavni

Sanjaya ka sandesh sunne ke baad, sabha mein kuch der ke liye shaanti chha gayi.

Tab Pitamah Bhishma uthkar Duryodhana se bole,

"Main tumhe ek purani kahani sunata hoon."

Unhone bataya,

"Bahut pehle Devta Brahma ji ke paas gaye the. Wahan do mahaan Rishi aaye – Nara aur Narayana. Brahma ji ne bataya ki ye dono dharm ki raksha aur adharm ka vinaash karne ke liye janm lete hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhishma ne phir kaha,

"Aaj wahi Nara aur Narayana, Arjuna aur Shri Krishna ke roop mein is dharti par hain."

"Jab bhi adharm badhta hai, ye dono milkar uska ant karte hain."

Phir Bhishma ne Duryodhana ko samjhaya,

"Agar tum yuddh karoge, to Krishna aur Arjuna ko ek hi rath par dekhoge. Us din tumhe meri baat yaad aayegi, lekin tab bahut der ho chuki hogi."

Bhishma ne saaf kaha,

"Tum galat logon ki baat maan rahe ho. Karna, Shakuni aur Dushasana tumhe galat raasta dikha rahe hain."

Yeh sunkar Karna ko gussa aa gaya.

Usne kaha,

"Pitamah, aap hamesha meri ninda karte hain. Maine Duryodhana ka saath nibhaaya hai aur yuddh mein Pandavon ko haraane ki poori koshish karunga."

Bhishma shaant rahe aur bole,

"Sirf badi-badi baatein karne se koi mahaan yoddha nahi ban jaata."

"Pandavon ne apni veerta baar-baar saabit ki hai. Lekin tum kabhi unke saamne tik nahi paaye."

Uske baad Guru Dronacharya bhi bole,

"Maharaj, Pitamah ki baat maan lijiye. Abhi bhi samay hai. Pandavon se shanti kar lijiye."

"Arjuna jo keh raha hai, woh zaroor hoga. Teenon lokon mein uske jaisa dhanurdhar koi nahi hai."

Lekin Duryodhana ne Bhishma aur Drona, dono ki salah ko nazarandaaz kar diya.

Woh phir bhi Sanjaya se Pandavon ke baare mein poochta raha.

Usi samay sab samajh gaye ki ab yuddh ko rokna bahut mushkil ho chuka hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.10
        with st.expander("Section 5.2.10  Section L"):
            text1 = """ Section L – Pandavon Ki Taiyaari

Dhritarashtra ne Sanjaya se poocha,

"Yudhishthira kya kar rahe hain? Itni badi sena dekhkar unhone kya faisla liya? Aur kaun unhe shanti ki salah de raha hai?"

Sanjaya bole,

"Sabhi Pandav, Panchal aur unke saathi Yudhishthira ki taraf dekh rahe hain. Sab unke aadesh ka intezaar kar rahe hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Yudhishthira sabko shaant rakh rahe hain. Ve bina wajah yuddh nahi chahte. Lekin agar nyaay na mila, to ve peeche bhi nahi hatenge."

"Har taraf se raja aur senaayein Pandavon ka saath dene aa rahi hain. Sab unke saath khade hone par khush hain."

Dhritarashtra ne phir poocha,

"Pandavon ke saath kaun-kaun yuddh karega?"

Itna sunte hi Sanjaya kuch pal ke liye chup ho gaye.

Unhone gehri saans li aur achanak behosh hokar zameen par gir pade.

Vidura ne turant kaha,

"Maharaj, Sanjaya behosh ho gaye hain."

Dhritarashtra bole,

"Lagta hai Pandavon ki shakti dekhkar unka mann ghabra gaya hai."

Thodi der baad Sanjaya ko hosh aa gaya.

Phir unhone kaha,

"Maine Pandavon ko dekha. Vanvaas ki wajah se unke sharir patle zaroor ho gaye hain, lekin unka hausla pehle se bhi zyada mazboot hai."

Phir Sanjaya ne ek-ek karke Pandavon ke mahaan yoddhaon ka naam bataya.

"Yudhishthira unke neta hain. Bhima das hazaar haathiyon jaisa bal rakhte hain. Arjuna ka koi muqaabla nahi. Nakula aur Sahadeva bhi mahaan yoddha hain."

"Shikhandi, Dhrishtadyumna, Satyaki, Virata, Drupada, Abhimanyu, Draupadi ke paanch putra aur bahut se shaktishaali raja bhi unke saath hain."

Ant mein Sanjaya bole,

"In sab veer yoddhaon par bharosa karke Yudhishthira yuddh ke liye poori tarah taiyaar hain. Agar shanti nahi hui, to bahut bada yuddh hona nishchit hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.11
        with st.expander("Section 5.2.11  Section LI"):
            text1 = """ 
            Section LI – Dhritarashtra Ka Dar

Dhritarashtra gehri saans lekar bole,

"Mujhe sabse zyada dar Bhima se lagta hai."

"Mujhe lagta hai ki baaki sab yoddha milkar bhi Bhima ke barabar nahi hain."

Unhone dukh se kaha,

"Main raat bhar so nahi paata. Jab bhi Bhima ki yaad aati hai, mera dil kaanp uthta hai."

"Bachpan se hi Bhima mere beton se bahut zyada shaktishaali tha. Khelte waqt bhi woh un sab par bhaari padta tha."

Dhritarashtra bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Ab woh aur bhi balwaan ho chuka hai. Uske haath mein lohe ki gada hai. Mujhe lagta hai ki yuddh mein woh mere kisi bhi bete ko nahi chhodega."

"Jab Bhima gusse mein sena ke beech ghusega, to haathi, ghode aur rath sab toot jaayenge."

Phir unhone Bhima ke purane kaarnamon ko yaad kiya.

"Usne raakshason ko haraaya, Jarasandha jaise mahaan raja ko maara aur hamesha apne bhaiyon ki raksha ki."

"Uska bal das hazaar haathiyon ke barabar maana jaata hai."

Dhritarashtra ne dukhi hokar kaha,

"Mere bete samajh hi nahi rahe ki woh kis se takraane ja rahe hain."

"Ve sirf jeet dekh rahe hain, lekin saamne khadi vinash ki gehri khaai nahi dekh pa rahe."

Phir unhone sweekar kiya,

"Vidura ne pehle hi humein chetavni di thi. Lekin humne unki baat nahi maani."

"Woh paase ka khel hi is sab vinash ki shuruaat tha."

Ant mein Dhritarashtra ne nirash hokar kaha,

"Ab sab kuch Kaal ke haath mein hai. Main dekh raha hoon ki Kuru vansh ka vinaash paas aa chuka hai."

"Mujhe darr hai ki bahut jald mere sau beton ki maut ki khabar sunni padegi. Aur Bhima aur Arjuna milkar meri poori sena ka ant kar denge." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.12
        with st.expander("Section 5.2.12  Section LII"):
            text1 = """ 
Section LII – Arjuna Ka Dar

Dhritarashtra ne udaas hokar kaha,

"Yudhishthira kabhi jhooth nahi bolte. Aur jab Arjuna jaise mahaan yoddha unke saath hain, to unhe teenon lokon ka raajya bhi mil sakta hai."

Phir unhone kaha,

"Main har din sochta hoon, lekin mujhe koi aisa yoddha nazar nahi aata jo Arjuna ka saamna kar sake."

"Jab Arjuna apna Gandiva dhanush uthakar baan chalayega, tab uske saamne tikna bahut mushkil hoga."

Dhritarashtra bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Haan, Dronacharya aur Karna bahut bade yoddha hain. Shayad woh uska saamna kar sakein. Lekin mujhe apni jeet ka bharosa bilkul nahi hai."

"Drona buddhe ho chuke hain aur Arjuna se pyaar bhi karte hain. Karna bahadur hai, lekin Arjuna ka bal aur kaushal alag hi hai."

Unhone aage kaha,

"Mujhe nahi lagta ki koi Arjuna ko hara sakta hai."

"Usne kabhi yuddh mein haar nahi maani. Khandav Van mein usne Devtaon tak ka saamna kiya tha."

Phir Dhritarashtra ne sabse badi baat kahi.

"Arjuna ke rath par Shri Krishna saarathi hain. Gandiva uske haath mein hai. Aur Arjuna khud mahaan yoddha hai."

"Yeh teeno saath hain. Hamare paas inka muqaabla karne wala koi nahi."

Dhritarashtra ne gehri saans lekar kaha,

"Duryodhana aur uske saathi is baat ko samajh hi nahi rahe."

"Mujhe abhi se dikh raha hai ki Arjuna ke baan meri sena ko chaaron taraf se tod denge."

"Mere sainik dar kar bhaagenge aur yuddh ka maidan vinaash se bhar jaayega."

Ant mein Dhritarashtra bole,

"Mujhe bure sanket dikh rahe hain. Har taraf ashubh lakshan nazar aa rahe hain."

"Mera mann keh raha hai ki Kuru vansh ka vinaash ab bahut kareeb aa chuka hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.13
        with st.expander("Section 5.2.13  Section LIII"):
            text1 = """ 
Section LIII – Dhritarashtra Ki Pachtawa Bhari Baat

Dhritarashtra ne udaasi se kaha,

"Pandav sirf veer hi nahi hain. Unke saath ladne wale sabhi raja bhi apni jaan dene ke liye taiyaar hain."

"Krishna unke saath hain. Aur jinke saath Krishna hote hain, unki jeet ki umeed aur badh jaati hai."

Phir unhone Pandavon ke saathiyon ka zikr kiya.

"Satyaki, Dhrishtadyumna, Panchal, Matsya, Kekaya aur bahut se mahaan yoddha unke saath khade hain."

Dhritarashtra bole,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Mujhe Bhima aur Arjuna se dar lagta hi hai. Lekin Yudhishthira ka dhairya aur unka dharm bhi utna hi shaktishaali hai."

"Jab ye sab milkar yuddh karenge, to meri sena unke baanon ke jaal se bahar nahi nikal paayegi."

Phir unhone Yudhishthira ki tareef ki.

"Yudhishthira buddhimaan hain, dayaalu hain, dhairyavaan hain aur hamesha sach aur dharm ka saath dete hain."

"Unke paas veer bhai hain, shaktishaali mitra hain aur achhe salahkaar bhi hain."

Dhritarashtra ne dukh ke saath kaha,

"Maine unke saath anyaay kiya. Aaj usi galti ka parinaam saamne khada hai."

"Agar yuddh hua, to mere bete bach nahi paayenge. Kuru vansh ka vinaash nishchit lag raha hai."

Ant mein Dhritarashtra ne kaha,

"Isliye mujhe lagta hai ki humein yuddh nahi, shanti chuni chahiye."

"Yudhishthira dayaalu hain. Agar hum sachche mann se shanti maangen, to mujhe bharosa hai ki woh humein thukraayenge nahi." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.14
        with st.expander("Section 5.2.14  Section LIV"):
            text1 = """ 
Section LIV – Sanjaya Ne Sach Bata Diya

Sanjaya ne shaant swar mein kaha,

"Maharaj, aap jo keh rahe hain, woh bilkul sach hai."

"Agar yuddh hua, to Arjuna ke Gandiva se bahut bade vinaash ko koi nahi rok sakta."

Phir Sanjaya ne ek kathin baat kahi.

"Lekin mujhe samajh nahi aata. Aap sab kuch jaante hain. Aap Pandavon ki shakti bhi jaante hain. Phir bhi aap apne beton ki galat baat kyun maan rahe hain?"

Unhone yaad dilaya,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Jab Pandav paase ke khel mein haar gaye the, tab aap khush hue the."

"Jab unka apmaan kiya gaya, tab bhi aapne unhe nahi roka."

"Us waqt aapne nahi socha ki ek din is anyaay ka parinaam saamne aayega."

Sanjaya ne phir kaha,

"Yeh poora rajya Pandavon ne apni veerta se jeeta tha. Lekin aapne use apna samajh liya."

"Aur jab Duryodhana Gandharvon ke haath pakda gaya tha, tab bhi Arjuna hi usse bacha kar laaye the."

Phir Sanjaya bole,

"Arjuna ka Gandiva sabse mahaan dhanush hai. Shri Krishna sabse mahaan saarathi hain. Aur unka rath ajey hai."

"Inka saamna karna bahut mushkil hai."

Unhone aage kaha,

"Matsya, Panchal aur bahut se raja ab Pandavon ka saath de rahe hain. Kyunki unhe pata hai ki Yudhishthira dharm ke raaste par hain."

Ant mein Sanjaya ne Dhritarashtra ko seedhi baat kahi.

"Is sab ka asli kaaran Duryodhana hai. Uski irshya aur galat faislon ne hi is yuddh ko janam diya hai."

"Vidura aur maine pehle bhi aapko roka tha. Lekin aapne hamari baat nahi maani."

"Ab sirf pachtane se kuch nahi hoga. Agar kuch badalna hai, to abhi bhi sahi faisla lena hoga." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.15
        with st.expander("Section 5.2.15  Section LV"):
            text1 = """ 
Section LV – Duryodhana Ka Atmavishwas

Dhritarashtra ki baatein sunkar Duryodhana bola,

"Pitashree, chinta mat kijiye. Hum yeh yuddh zaroor jeetenge."

Usne yaad dilaya,

"Jab Pandav vanvaas mein the, tab bhi unke paas Krishna aur bahut se raja aaye the. Sab unhe turant rajya wapas lene ke liye keh rahe the."

"Us samay mujhe bhi dar laga tha. Maine Bhishma, Drona aur Kripacharya se salah maangi."

Duryodhana bola,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Un sabne mujhe himmat di. Unhone kaha ki agar yuddh hua, to hum Pandavon ka saamna kar sakte hain."

Phir usne garv se kaha,

"Aaj hamare paas aur bhi badi sena hai. Bahut se raja mere saath hain. Ve mere liye apni jaan dene ko bhi taiyaar hain."

Usne Bhima ko chunauti di.

"Sab Bhima se darte hain. Lekin main nahi darta."

"Maine Balram ji se gada chalana seekha hai. Unhone khud kaha tha ki gada yuddh mein mera koi muqaabla nahi."

"Ek hi vaar mein main Bhima ko gira sakta hoon."

Phir Duryodhana ne apni sena ke mahaan yoddhaon ka naam liya.

"Bhishma, Drona, Kripacharya, Ashwatthama, Karna, Shalya, Jayadratha aur bahut se mahaan yoddha mere saath hain."

"Ye sab milkar Arjuna ko bhi hara denge."

Usne Karna ki bhi tareef ki.

"Karna ke paas divya astra hai. Mujhe poora vishwas hai ki woh Arjuna ko hara dega."

Ant mein Duryodhana ne apna sabse bada tark diya.

"Hamare paas gyarah Akshauhini sena hai. Pandavon ke paas sirf saat Akshauhini hai."

"Hamari sena zyada badi hai. Isliye haarne ka sawaal hi paida nahi hota."

Yeh kehkar Duryodhana phir Sanjaya ki taraf muda aur bola,

"Ab mujhe Pandavon ki aur taiyaari ke baare mein aur batao." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.16
        with st.expander("Section 5.2.16  Section LVI"):
            text1 = """ 
Section LVI – Pandavon Ka Atmavishwas

Duryodhana ne Sanjaya se poocha,

"Pandavon ke paas sirf saat Akshauhini sena hai. Phir bhi Yudhishthira aur unke saathi itne nishchint kyun hain?"

Sanjaya ne jawab diya,

"Maharaj, Yudhishthira bilkul shaant aur khush hain. Bhima aur Arjuna bhi poore vishwas ke saath yuddh ki taiyaari kar rahe hain. Nakula aur Sahadeva bhi bina kisi dar ke khade hain."

Phir Sanjaya ne Arjuna ke baare mein bataya."""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Arjuna ne apna divya rath taiyaar kiya. Chamakte hue kavach mein woh bijli se ghire baadal ki tarah dikh rahe the."

Arjuna muskurakar bole,

"Sanjaya, in shubh sanketon ko dekho. Humein poora vishwas hai ki jeet hamari hi hogi."

Duryodhana ne phir poocha,

"Achha batao, Arjuna ke rath aur uske ghodon mein aisa kya khaas hai?"

Sanjaya bole,

"Arjuna ka rath divya shilpkar ne Devtaon ki madad se banaya tha."

"Uske dhwaj par Hanuman ji ka chinh hai. Jab rath yuddh mein chalega, to Hanuman ji uski raksha aur utsaah badhaayenge."

"Us rath ke safed ghode bahut tez hain. Unki raftaar mann ki gati jaisi hai. Aur agar ve yuddh mein gir bhi jaayen, to unki sankhya phir se poori ho jaati hai."

Phir Sanjaya ne baaki Pandavon ke rathon ka bhi varnan kiya.

"Yudhishthira ke ghode haathi ke daanton ki tarah safed aur shaant hain."

"Bhima ke ghode hawa ki tarah tez hain."

"Nakula aur Sahadeva ke paas bhi Devtaon ke diye hue bahut shaktishaali ghode hain."

"Abhimanyu aur Draupadi ke putron ke rath bhi divya ghodon se jude hue hain."

Ant mein Sanjaya bole,

"Pandav sirf veer hi nahi hain. Unki taiyaari, unke rath aur unke divya saadhan bhi asadharan hain. Isliye unka atmavishwas itna mazboot hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.17
        with st.expander("Section 5.2.17  Section LVII"):
            text1 = """ 
Section LVII – Yuddh Ki Zimmedaari Baant Di Gayi

Dhritarashtra ne Sanjaya se poocha,

"Pandavon ke saath kaun-kaun raja aa gaye hain? Aur yuddh mein kaun kis se ladega?"

Sanjaya ne kaha,

"Shri Krishna, Satyaki, Chekitana, Drupada, Virata, Dhrishtadyumna, Dhrishtaketu, Kekaya ke paanch bhai aur bahut se mahaan raja Pandavon ke saath aa chuke hain."

"Sabhi apni-apni sena lekar aaye hain aur Yudhishthira ka saath dene ke liye taiyaar hain." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
Phir Sanjaya ne bataya ki Pandavon ne yuddh ki zimmedaari baant di hai.

"Shikhandi ka lakshya Bhishma hain."

"Bhima Duryodhana aur uske bhaiyon se ladenge."

"Arjuna Karna aur Jayadratha ka saamna karenge."

"Abhimanyu Duryodhana ke putron se ladega."

"Draupadi ke putra Dronacharya ke saamne jaayenge."

"Satyaki Kritavarma se, Sahadeva Shakuni se aur Nakula Uluka se yuddh karenge."

Sanjaya ne kaha,

"Har yoddha ko uska saamne wala shatru pehle hi bata diya gaya hai. Pandavon ki poori sena soch-samajh kar taiyaar ki gayi hai."

Yeh sunkar Dhritarashtra bahut dukhi ho gaye.

Unhone kaha,

"Mere bete to pehle hi maut ki taraf badh chuke hain."

"Jo Bhima aur Arjuna ka saamna karna chahte hain, woh aag mein koodne wale patangon jaise hain."

"Pandavon ke saath itne mahaan yoddha hain ki unhe haraana bahut mushkil hai."

Lekin Duryodhana phir bhi ghamand se bola,

"Hum bhi kamzor nahi hain. Hamare paas Bhishma, Drona, Karna, Kripacharya, Ashwatthama aur bahut se mahaan yoddha hain."

"Hum Pandavon ko zaroor hara denge."

Dhritarashtra ne sir hila kar kaha,

"Tum sach ko dekhna hi nahi chahte."

Ant mein Sanjaya ne bataya ki Dhrishtadyumna baar-baar Pandavon ka hausla badha rahe the.

Woh kehte the,

"Daro mat. Hum sab milkar Kaurav sena ka saamna karenge."

Yudhishthira ne un par poora bharosa jataya aur kaha,

"Humein aapki veerta par poora vishwas hai. Is yuddh mein humein sahi raasta dikhaiye."

Jaate waqt Dhrishtadyumna ne Sanjaya se ek antim sandesh bheja.

"Jaakar Kauravon se keh do. Agar woh abhi bhi shanti chahte hain, to Yudhishthira ko unka haq ka rajya wapas de dein."

"Warna Arjuna ko koi nahi rok paayega, aur phir yuddh ka vinaash nishchit hoga." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.18
        with st.expander("Section 5.2.18  Section LVIII"):
            text1 = """ 
Section LVIII – Duryodhana Ka Antim Faisla

Dhritarashtra ne dukh se kaha,

"Yudhishthira bachpan se hi dharm aur anushasan par chale hain. Unse yuddh karna sahi nahi hai."

Phir unhone Duryodhana se kaha,

"Beta, abhi bhi samay hai. Dushmani chhod do. Pandavon ko unka haq ka hissa wapas de do."

"Aadha rajya bhi tumhare liye kaafi hai. Yuddh se kisi ka bhala nahi hoga."

Dhritarashtra ne aage kaha,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Bhishma, Drona, Kripacharya, Shalya, Sanjaya aur hamare bahut se mahaan yoddha bhi yuddh nahi chahte."

"Sirf Karna, Dushasana aur Shakuni tumhe is raaste par le ja rahe hain."

Lekin Duryodhana ne ghamand se jawab diya,

"Mujhe kisi ki madad ki zaroorat nahi hai."

"Main, Karna aur Dushasana hi Pandavon ko hara denge."

Phir usne dridh awaaz mein kaha,

"Chahe mujhe apni jaan hi kyun na deni pade, main Pandavon ke saath rajya baantkar nahi rahunga."

"Main unhe sui ki nok jitni zameen bhi nahi dunga."

Yeh sunkar Dhritarashtra ka dil toot gaya.

Unhone kaha,

"Aaj se main tumhari zid se haar maan leta hoon."

"Mujhe tum par nahi, un sab rajaon par daya aa rahi hai jo tumhare saath yuddh mein jaayenge."

Phir unhone bhavishya ki tasveer batayi.

"Bhima tumhari sena ko aandhi ki tarah tod dega."

"Haathi, ghode aur rath sab zameen par gir jaayenge."

"Satyaki aur doosre Pandav yoddha bhi Kaurav sena ko chaaron taraf se hara denge."

Ant mein Dhritarashtra ne ek baar phir kaha,

"Abhi bhi shanti kar lo. Warna jab Bhima tumhari poori sena ko mita dega, tab tumhe meri aaj ki baat zaroor yaad aayegi." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.19
        with st.expander("Section 5.2.19  Section LIX"):
            text1 = """ 
Section LIX – Krishna Ka Antim Sandesh

Dhritarashtra ne Sanjaya se kaha,

"Mujhe batao, Krishna aur Arjuna ne kya kaha. Main sab kuch sunna chahta hoon."

Sanjaya bole,

"Maharaj, main Krishna aur Arjuna se milne unke shivir gaya."

"Wahan maine dono ko ek saath dekha. Dono bahut shaant, khush aur gehri mitrata se baithe the." """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Unhe dekhkar mujhe aisa laga jaise Narayan aur Indra ek saath baithe hon."

"Usi pal mujhe samajh aa gaya ki Yudhishthira ki jeet ki sambhaavna bahut mazboot hai."

Sanjaya ne Dhritarashtra ka sandesh un tak pahunchaya.

Tab Arjuna ne vinamrata se Krishna ki taraf dekha aur kaha,

"Iska jawab aap dijiye."

Krishna shaant swar mein bole,

"Sanjaya, pehle sabhi buzurgon ko hamara pranam kehna."

Phir unhone kaha,

"Dhritarashtra se kehna ki apne parivaar ke saath samay bitaayein, daan karein aur achhe karm karein."

"Kyunki agar yuddh hua, to bahut bada sankat aane wala hai."

Krishna ki aankhon mein karuna thi.

Unhone kaha,

"Duryodhana ne Arjuna se dushmani karke bahut badi galti ki hai."

"Jiske saath Arjuna aur main dono khade hain, usse koi nahi hara sakta."

"Devta, Asur, Yaksha ya koi bhi mahaan yoddha Arjuna ka saamna nahi kar sakta."

Phir Krishna ne Virat Nagar ka yuddh yaad dilaya.

"Ek baar Arjuna ne akele hi poori Kaurav sena ko hara diya tha. Woh uski shakti ka sabse bada saboot hai."

Krishna ne ant mein kaha,

"Arjuna ki veerta, dhairya aur yuddh kaushal ka koi muqaabla nahi hai."

Yeh sab sunkar Arjuna ne bhi Krishna ki baat se sehmat hote hue apna sandesh dene ki taiyaari ki. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.20
        with st.expander("Section 5.2.20  Section LX"):
            text1 = """ 
Section LX – Dhritarashtra Ne Sach Maan Liya

Sanjaya ki baatein sunkar Dhritarashtra gehri soch mein doob gaye.

Unhone dono senaon ki taakat aur kamzori ko dhyaan se socha.

Ant mein woh bole,

"Ab mujhe saaf dikh raha hai ki Pandav sirf apni taakat se hi nahi, Devtaon ke aashirvaad se bhi mazboot hain."

Phir unhone Duryodhana se kaha,

"Mujhe din-raat ek hi chinta sataati hai. Mujhe lagta hai ki yeh yuddh Kuru vansh ke liye bahut bhaari padega."

Dhritarashtra ne samjhaya,"""
            create_image_text_layout(
                "attached_assets/chapter5/5.2.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
"Jo kisi ka bhala karta hai, use zaroor madad milti hai."

"Arjuna ne Khandav Van mein Agni Dev ki madad ki thi. Isliye Agni Dev bhi uska saath denge."

"Pandav hamesha dharm ke raaste par chale hain. Isliye Devta bhi unki raksha karenge."

Phir unhone Arjuna ki shakti ka varnan kiya.

"Uske paas divya Gandiva dhanush hai."

"Uske baan kabhi khatam nahi hote."

"Uske rath par Hanuman ji ka dhwaj hai. Aur uska rath kisi se kam nahi."

"Arjuna pal bhar mein saikdon baan chala sakta hai. Bahut bade-bade yoddha bhi uska saamna mushkil se kar sakte hain."

Dhritarashtra ne dukh se kaha,

"Main roz sochta hoon ki agar yuddh hua, to Arjuna hamari sena mein bahut bada vinaash karega."

Ant mein unhone ek baar phir apni ichchha batayi.

"Main yuddh nahi chahta."

"Main chahta hoon ki Pandavon se shanti ho jaaye."

"Sach kahoon, to mujhe hamesha se lagta hai ki Pandav Kauravon se zyada shaktishaali hain." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.2.21
        with st.expander("Section 5.2.21  Section LXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.22
        with st.expander("Section 5.2.22  Section LXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.23
        with st.expander("Section 5.2.23  Section LXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.24
        with st.expander("Section 5.2.24  Section LXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.25
        with st.expander("Section 5.2.25  Section LXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.26
        with st.expander("Section 5.2.26  Section LXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.27
        with st.expander("Section 5.2.27  Section LXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.28
        with st.expander("Section 5.2.28  Section LXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.29
        with st.expander("Section 5.2.29  Section LXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.30
        with st.expander("Section 5.2.30  Section LXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            # ==================================================
    # Chapter 5.3 - Bhagavat-Yana Parva
    # ==================================================

    with st.expander("Chapter 5.3  Bhagavat-Yana Parva"):

        # Section 5.3.1
        with st.expander("Section 5.3.1  Section LXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.2
        with st.expander("Section 5.3.2  Section LXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.3
        with st.expander("Section 5.3.3  Section LXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.4
        with st.expander("Section 5.3.4  Section LXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.5
        with st.expander("Section 5.3.5  Section LXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.6
        with st.expander("Section 5.3.6  Section LXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.7
        with st.expander("Section 5.3.7  Section LXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.8
        with st.expander("Section 5.3.8  Section LXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.9
        with st.expander("Section 5.3.9  Section LXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.10
        with st.expander("Section 5.3.10  Section LXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.3.11
        with st.expander("Section 5.3.11  Section LXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.12
        with st.expander("Section 5.3.12  Section LXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.13
        with st.expander("Section 5.3.13  Section LXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.14
        with st.expander("Section 5.3.14  Section LXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.15
        with st.expander("Section 5.3.15  Section LXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.16
        with st.expander("Section 5.3.16  Section LXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.17
        with st.expander("Section 5.3.17  Section LXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.18
        with st.expander("Section 5.3.18  Section LXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.19
        with st.expander("Section 5.3.19  Section XC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.20
        with st.expander("Section 5.3.20  Section XCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.21
        with st.expander("Section 5.3.21  Section XCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.22
        with st.expander("Section 5.3.22  Section XCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.23
        with st.expander("Section 5.3.23  Section XCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.24
        with st.expander("Section 5.3.24  Section XCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.25
        with st.expander("Section 5.3.25  Section XCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.3.26
        with st.expander("Section 5.3.26  Section XCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.27
        with st.expander("Section 5.3.27  Section XCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.28
        with st.expander("Section 5.3.28  Section XCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.29
        with st.expander("Section 5.3.29  Section C"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.30
        with st.expander("Section 5.3.30  Section CI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.31
        with st.expander("Section 5.3.31  Section CII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.32
        with st.expander("Section 5.3.32  Section CIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.33
        with st.expander("Section 5.3.33  Section CIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.34
        with st.expander("Section 5.3.34  Section CV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.35
        with st.expander("Section 5.3.35  Section CVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.36
        with st.expander("Section 5.3.36  Section CVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.37
        with st.expander("Section 5.3.37  Section CVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.38
        with st.expander("Section 5.3.38  Section CIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.39
        with st.expander("Section 5.3.39  Section CX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.40
        with st.expander("Section 5.3.40  Section CXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.3.41
        with st.expander("Section 5.3.41  Section CXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.41.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.42
        with st.expander("Section 5.3.42  Section CXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.42.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.43
        with st.expander("Section 5.3.43  Section CXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.43.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.44
        with st.expander("Section 5.3.44  Section CXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.44.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.45
        with st.expander("Section 5.3.45  Section CXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.45.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.46
        with st.expander("Section 5.3.46  Section CXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.46.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.47
        with st.expander("Section 5.3.47  Section CXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.47.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.48
        with st.expander("Section 5.3.48  Section CXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.48.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.49
        with st.expander("Section 5.3.49  Section CXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.49.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.50
        with st.expander("Section 5.3.50  Section CXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.50.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.51
        with st.expander("Section 5.3.51  Section CXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.51.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.52
        with st.expander("Section 5.3.52  Section CXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.52.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.53
        with st.expander("Section 5.3.53  Section CXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.53.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.54
        with st.expander("Section 5.3.54  Section CXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.54.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.55
        with st.expander("Section 5.3.55  Section CXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.55.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.56
        with st.expander("Section 5.3.56  Section CXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.56.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.3.57
        with st.expander("Section 5.3.57  Section CXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.57.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.58
        with st.expander("Section 5.3.58  Section CXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.58.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.59
        with st.expander("Section 5.3.59  Section CXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.59.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.60
        with st.expander("Section 5.3.60  Section CXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.60.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.61
        with st.expander("Section 5.3.61  Section CXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.61.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.62
        with st.expander("Section 5.3.62  Section CXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.62.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.63
        with st.expander("Section 5.3.63  Section CXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.63.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.64
        with st.expander("Section 5.3.64  Section CXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.64.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.65
        with st.expander("Section 5.3.65  Section CXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.65.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.66
        with st.expander("Section 5.3.66  Section CXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.66.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.67
        with st.expander("Section 5.3.67  Section CXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.67.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.68
        with st.expander("Section 5.3.68  Section CXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.68.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            
                # Section 5.3.69
        with st.expander("Section 5.3.69  Section CXL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.69.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.70
        with st.expander("Section 5.3.70  Section CXLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.70.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.71
        with st.expander("Section 5.3.71  Section CXLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.71.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.72
        with st.expander("Section 5.3.72  Section CXLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.72.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.73
        with st.expander("Section 5.3.73  Section CXLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.73.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.74
        with st.expander("Section 5.3.74  Section CXLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.74.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.75
        with st.expander("Section 5.3.75  Section CXLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.75.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.76
        with st.expander("Section 5.3.76  Section CXLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.76.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.77
        with st.expander("Section 5.3.77  Section CXLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.77.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.78
        with st.expander("Section 5.3.78  Section CXLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.78.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.79
        with st.expander("Section 5.3.79  Section CXLX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.79.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.80
        with st.expander("Section 5.3.80  Section CLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.80.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.3.81
        with st.expander("Section 5.3.81  Section CLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.81.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.82
        with st.expander("Section 5.3.82  Section CLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.82.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.83
        with st.expander("Section 5.3.83  Section CLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.83.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.84
        with st.expander("Section 5.3.84  Section CLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.84.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.85
        with st.expander("Section 5.3.85  Section CLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.85.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.86
        with st.expander("Section 5.3.86  Section CLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.86.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.87
        with st.expander("Section 5.3.87  Section CLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.87.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.88
        with st.expander("Section 5.3.88  Section CLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.88.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.3.89
        with st.expander("Section 5.3.89  Section CLX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.3.89.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )   
            # ==================================================
    # Chapter 5.4 - Uluka Dutagamana Parva
    # ==================================================

    with st.expander("Chapter 5.4  Uluka Dutagamana Parva"):

        # Section 5.4.1
        with st.expander("Section 5.4.1  Section CLXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.2
        with st.expander("Section 5.4.2  Section CLXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.3
        with st.expander("Section 5.4.3  Section CLXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.4
        with st.expander("Section 5.4.4  Section CLXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.5
        with st.expander("Section 5.4.5  Section CLXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.6
        with st.expander("Section 5.4.6  Section CLXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.7
        with st.expander("Section 5.4.7  Section CLXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.8
        with st.expander("Section 5.4.8  Section CLXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.9
        with st.expander("Section 5.4.9  Section CLXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.10
        with st.expander("Section 5.4.10  Section CLXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.4.11
        with st.expander("Section 5.4.11  Section CLXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.12
        with st.expander("Section 5.4.12  Section CLXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.13
        with st.expander("Section 5.4.13  Section CLXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.14
        with st.expander("Section 5.4.14  Section CLXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.15
        with st.expander("Section 5.4.15  Section CLXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.16
        with st.expander("Section 5.4.16  Section CLXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.17
        with st.expander("Section 5.4.17  Section CLXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.18
        with st.expander("Section 5.4.18  Section CLXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.19
        with st.expander("Section 5.4.19  Section CLXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.20
        with st.expander("Section 5.4.20  Section CLXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
                # Section 5.4.21
        with st.expander("Section 5.4.21  Section CLXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.22
        with st.expander("Section 5.4.22  Section CLXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.23
        with st.expander("Section 5.4.23  Section CLXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.24
        with st.expander("Section 5.4.24  Section CLXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.25
        with st.expander("Section 5.4.25  Section CLXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.26
        with st.expander("Section 5.4.26  Section CLXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.27
        with st.expander("Section 5.4.27  Section CLXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.28
        with st.expander("Section 5.4.28  Section CLXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.29
        with st.expander("Section 5.4.29  Section CLXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.30
        with st.expander("Section 5.4.30  Section CXC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.31
        with st.expander("Section 5.4.31  Section CXCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.32
        with st.expander("Section 5.4.32  Section CXCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.33
        with st.expander("Section 5.4.33  Section CXCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.34
        with st.expander("Section 5.4.34  Section CXCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.35
        with st.expander("Section 5.4.35  Section CXCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.36
        with st.expander("Section 5.4.36  Section CXCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.37
        with st.expander("Section 5.4.37  Section CXCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.38
        with st.expander("Section 5.4.38  Section CXCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.4.39
        with st.expander("Section 5.4.39  Section CXCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.4.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
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
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.17
        with st.expander("Section 5.1.17  Section XVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.18
        with st.expander("Section 5.1.18  Section XVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.19
        with st.expander("Section 5.1.19  Section XIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.20
        with st.expander("Section 5.1.20  Section XX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.21
        with st.expander("Section 5.1.21  Section XXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.22
        with st.expander("Section 5.1.22  Section XXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.23
        with st.expander("Section 5.1.23  Section XXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.24
        with st.expander("Section 5.1.24  Section XXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.25
        with st.expander("Section 5.1.25  Section XXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.26
        with st.expander("Section 5.1.26  Section XXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.27
        with st.expander("Section 5.1.27  Section XXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.28
        with st.expander("Section 5.1.28  Section XXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.29
        with st.expander("Section 5.1.29  Section XXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.30
        with st.expander("Section 5.1.30  Section XXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.31
        with st.expander("Section 5.1.31  Section XXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.32
        with st.expander("Section 5.1.32  Section XXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.33
        with st.expander("Section 5.1.33  Section XXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.34
        with st.expander("Section 5.1.34  Section XXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.35
        with st.expander("Section 5.1.35  Section XXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.36
        with st.expander("Section 5.1.36  Section XXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.37
        with st.expander("Section 5.1.37  Section XXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.38
        with st.expander("Section 5.1.38  Section XXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.39
        with st.expander("Section 5.1.39  Section XXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.1.40
        with st.expander("Section 5.1.40  Section XL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.1.40.jpg",
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
    # Chapter 5.2 - Sanatsujata Parva
    # ==================================================

    with st.expander("Chapter 5.2  Sanatsujata Parva"):

        # Section 5.2.1
        with st.expander("Section 5.2.1  Section XLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.2
        with st.expander("Section 5.2.2  Section XLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.3
        with st.expander("Section 5.2.3  Section XLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.4
        with st.expander("Section 5.2.4  Section XLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.5
        with st.expander("Section 5.2.5  Section XLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
            
                # Section 5.2.6
        with st.expander("Section 5.2.6  Section XLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.7
        with st.expander("Section 5.2.7  Section XLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.8
        with st.expander("Section 5.2.8  Section XLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.9
        with st.expander("Section 5.2.9  Section XLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.10
        with st.expander("Section 5.2.10  Section L"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.11
        with st.expander("Section 5.2.11  Section LI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.12
        with st.expander("Section 5.2.12  Section LII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.13
        with st.expander("Section 5.2.13  Section LIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.14
        with st.expander("Section 5.2.14  Section LIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.15
        with st.expander("Section 5.2.15  Section LV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.16
        with st.expander("Section 5.2.16  Section LVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.17
        with st.expander("Section 5.2.17  Section LVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.18
        with st.expander("Section 5.2.18  Section LVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.19
        with st.expander("Section 5.2.19  Section LIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 5.2.20
        with st.expander("Section 5.2.20  Section LX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter5/5.2.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
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
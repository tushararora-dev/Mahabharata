import streamlit as st
from app import create_image_text_layout


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
        background-color: #6969691f;
    }

    .beth1 {
            font-family: 'Beth Ellen', cursive !important;
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
    create_image_text_layout("attached_assets/chapter7/chapter7.jpg", layout="full")

    text0 = """
    <h2>Book 7 - Drona Parva</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    # ==================================================
    # Chapter 7.1 - Dronabhisheka Parva
    # ==================================================

    with st.expander("Chapter 7.1  Dronabhisheka Parva"):
        sections = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
                    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"]
        section_text = {
            1: """Ek baar, Raja Janamejaya ne Rishi Vaisampayana se ek sawal poocha. Unhone poocha ki jab Mahabharat ke yudh mein Bhishma Pitamah gir gaye, tab Raja Dhritarashtra ne kya kiya?

Rishi Vaisampayana ne bataya ki Bhishma ke girne ki khabar sunkar Raja Dhritarashtra bahut udaas ho gaye. Unka mann bilkul shaant nahi tha. Usi raat, unke trusted advisor Sanjaya yudh ke maidan se wapas laute.

Dhritarashtra ne Sanjaya se poocha, "Bhishma ke baad mere bete Duryodhana aur Kaurava sena ne kya kiya? Pandavon ki army toh bahut strong hai. Unse toh sab darte hain. Mujhe sab kuch batao."

Sanjaya ne kaha, "Raja ji, dhyan se suniye. Jab Bhishma maidan mein gire, tab dono teams—Kauravas aur Pandavas—unke paas aaye. Sabne unhe respect diya aur teeron ka ek bed banaya. Unki safety ka dhyan rakha aur unke aage sar jhukaya.

Lekin uske baad, dono armies phir se gusse mein aa gayin. Bhishma ki achhi baaton ko bhoolkar, unhone drums aur trumpets bajaye aur ladai phir se shuru kar di.

Par Bhishma ke bina Kaurava sena bilkul kho gayi thi. Woh aise lag rahe the jaise jungle mein bina charwahe ke bhed-bakriyan, ya samundar ke toofan mein phansi ek chhoti si naav. Har soldier aur raja darr gaya tha.

Tabhi sabko ek hi naam yaad aaya—Karna! Sab chillane lage, 'Karna ko bulao! Wahi hamara sachha dost hai aur hamein bacha sakta hai.'

Actually, Karna pichle dus din se yudh mein nahi lada tha. Bhishma ne sabke saamne Karna ko kamzor warrior kaha tha, jabki woh bahut brave tha. Is baat se Karna gussa ho gaya tha. Usne kasam khayi thi ki jab tak Bhishma ladenge, woh hathiyar nahi uthayega. Lekin agar Bhishma gir gaye, toh woh akele hi Pandavon se ladne aayega.

Ab jab Bhishma nahi rahe, toh sabhi ko Karna par hi bharosa tha. Jaise nadi paar karne ke liye log naav dhoondhte hain, waise hi Kauravas ko ab Karna ki zaroorat thi.

Yeh sab sunkar Dhritarashtra ne ek lambi saans li. Unhone Sanjaya se poocha, "Mujhe pata hai sabko Karna se bahut umeed hai. Par kya Karna sach mein mere beton ki madad kar paya? Kya woh Bhishma ki kami poori kar saka?" """, 2: """ Sanjaya ne aage ki kahani sunayi.

Jab Karna ko pata chala ki Bhishma Pitamah gir gaye hain, toh woh turant yudh ke maidan mein aa gaya. Woh ek bade bhai ki tarah Kaurava sena ko bachana chahta tha, jo ek gahre samundar mein doobti hui naav jaisi lag rahi thi.

Pehle Karna ne sabhi soldiers ke saath Bhishma ko yaad kiya. Usne kaha ki Bhishma bahut brave, honest aur wise the. Unke girne se yeh samajh aata hai ki is duniya mein koi bhi cheez hamesha ke liye nahi rehti. Karna ki yeh baat sunkar Duryodhana ke bhai aur saare soldiers rone lage.

Thodi der baad, yudh ka shor phir se shuru ho gaya. Tab Karna ne sabhi Kaurava warriors ka hausla badhaya. Usne kaha, "Mujhe pata hai ki Pandavas—Yudhishthira, Bhima, Arjuna, Nakula, Sahadeva aur Krishna—bahut powerful hain. Unhe harana aasaan nahi hai. Phir bhi, main bilkul nahi darta! Ab Bhishma ki jagah main is army ko bachaunga."

Karna ne ek pakka vaada kiya. Usne kaha, "Ek saccha dost wahi hota hai jo mushkil waqt mein saath de. Aaj ya toh main Pandavon ko hara kar Duryodhana ko jeet dilaunga, ya phir Bhishma ki tarah bahaduri se ladte hue apni jaan de dunga."

Phir Karna ladai ke liye taiyaar hua. Usne apna chamakta hua golden armour aur crown pehna. Apne best bows, arrows aur haathi ke nishan wala golden flag saath liya. Jeet ke dhol bajne lage, aur Karna apne sundar rath par baith gaya, jisme bahut tez daudne wale ghode jude the.

Saare Kaurava warriors ne Karna ko respect diya. Suraj ki tarah chamakta hua Karna, yudh ke maidan ki taraf aage badh gaya. """, 3: """Sanjaya ne aage bataya ki jab Karna yudh ke maidan mein pahuncha, toh usne Bhishma Pitamah ko teeron ke bed par lete hue dekha.

Bhishma hamesha sabke liye ek safe sahara the. Unhe zameen par gira dekh kar Duryodhana aur uske bhaiyon ki jeetne ki saari umeed khatam ho gayi thi.

Karna ko bhi yeh dekh kar bahut dukh hua. Uski aankhon mein aansu aa gaye. Woh apne rath se neeche utara aur paidal chal kar Bhishma ke paas gaya.

Usne haath jodkar bade respect se kaha, "Pitamah, main Karna hoon. Please apni aankhein kholiye aur mujhse kuch achhi baatein kahiye. Aapne hamesha sach aur achhai ka saath diya, phir bhi aaj aap zameen par lete hain."

Karna ne aage kaha, "Kuru parivar mein aapke jaisa samajhdar aur skilled koi nahi hai. Chahe khazana sambhalna ho, sahi advice deni ho, ya army ko lead karna ho—aap sabse best the. Aapne hamesha hamari raksha ki.

Ab aapke bina Pandavas hamari sena par sheron ki tarah hamla karenge. Koi bhi raja Arjuna ke saamne tik nahi payega. Arjuna ek tez aag ki tarah hai, aur Krishna us hawa ki tarah jo aag ko aur bada kar deti hai. Arjuna ke dhanush ki aawaz sunkar hi sab darr jayenge."

Phir Karna ne himmat dikhate hue Bhishma se permission maangi. Usne kaha, "Aapne toh Parashurama jaise mahan guru ko bhi haraya tha, par Krishna ke saath hone se Arjuna ko rokna mushkil tha. Phir bhi, agar aap mujhe permission aur aashirwad dein, toh main apni poori taqat se Arjuna ka saamna karne ke liye taiyaar hoon." """, 4: """Sanjaya ne aage ki kahani sunayi.

Karna ki baat sunkar, Bhishma Pitamah ke chehre par ek pyaari si muskaan aa gayi. Unhone bade pyaar aur samajhdari se Karna ko aashirwad diya.

Unhone kaha, "Karna, jaise samundar saari nadiyon ko apna leta hai aur baadal sabko baarish dete hain, waise hi tum apne doston aur parivar ka sahara bano. Apne logon ko khushi do aur Kaurava sena ko sambhalo."

Bhishma ne Karna ko uski purani bahaduri bhi yaad dilayi. Unhone kaha, "Pehle bhi tumne Duryodhana ko khush karne ke liye akela jaakar Kamboja, Kalinga, Andhra aur Himalayas ke kai strong rajaon ko haraya tha."

Phir Bhishma ne ek bahut pyari baat kahi, "Beta, mere liye tum bhi Duryodhana ki tarah mere pote ho. Samajhdar log kehte hain ki achhe logon ki dosti ka rishta khoon ke rishte se bhi bada hota hai. Isliye is army ko apna samajh kar iski raksha karo. Mere aashirwad ke saath jao aur sena ko lead karo."

Yeh sunkar Karna ko bahut achha laga. Usne jhuk kar Bhishma ke pair chhooye aur unse vida li.

Phir Karna wapas Kaurava camp mein aaya. Usne wahan khade sabhi brave soldiers ko himmat di aur unka hausla badhaya.

Duryodhana aur poori Kaurava army Karna ko sabse aage khada dekh kar bahut khush ho gayi. Sabne zordaar cheers aur dhanush ki taankar ke saath Karna ka welcome kiya!""", 5: """ Sanjaya ne aage ki kahani sunayi.

Karna ko rath par taiyaar dekh kar Duryodhana bahut khush hua. Usne kaha, "Tumhare aane se hamari army ko ek naya sahara mil gaya hai. Ab hamein aage ka plan banana chahiye."

Karna ne bade pyaar se jawab diya, "Mere raja, aap bahut samajhdar hain. Aap khud batayein ki kya karna sahi rahega. Yahan ke sabhi raja aapki baat sunne ke liye taiyaar hain."

Tab Duryodhana ne kaha, "Bhishma hamare commander the. Dus din tak unhone bahaduri se hamari raksha ki. Lekin ab hamein ek naya leader chahiye. Jaise bina captain ke naav nahi chal sakti aur bina driver ke rath nahi chal sakta, waise hi bina leader ke koi army nahi lad sakti. Karna, tum batao ki hamara naya commander kaun hona chahiye? Tum jise chunoge, hum sab usse maan lenge."

Karna ne thodi der socha aur bahut samajhdari bhara jawab diya. Usne kaha, "Yahan baithe sabhi raja bahut brave, smart aur skilled hain. Har koi leader banne ke layak hai. Par hum sirf ek hi commander chunn sakte hain.

Agar hum kisi ek raja ko leader banayenge, toh baaki raja bura maan sakte hain. Phir woh poore dil se nahi ladenge.

Isliye hamare sabke guru, Dronacharya, sabse best choice hain! Woh hum sabse bade hain aur weapons chalane mein sabse mahir hain. Apne teacher se koi jealous nahi hoga. Sabhi warriors unka respect karte hain aur khushi-khushi unki baat manenge."

Karna ne aage kaha, "Isliye Duryodhana, bina der kiye Guru Drona ko hamari army ka naya commander bana do!" """, 6: """Sanjaya ne aage ki kahani sunayi.

Karna ki baat sunkar Raja Duryodhana turant Guru Drona ke paas gaya, jo soldiers ke beech khade the.

Duryodhana ne bade respect se kaha, "Gurudev, aap bahut wise, brave aur honest hain. Aapki learning aur skills ka koi muqabla nahi hai. Is poori army mein aapse achha leader koi aur nahi ho sakta.

Jaise taaron mein Chand sabse khaas hota hai aur roshni mein Suraj, waise hi saare commanders mein aap sabse best hain. Please hamare naye leader ban jaiye. Hamari poori army aapka har order manegi."

Duryodhana ne aage kaha, "Aap sabse aage chaliye aur hum sab aapke peeche chalenge. Aapko dhanush ke saath sabse aage dekh kar Arjuna bhi attack karne mein hichkichayega. Agar aap hamare commander ban gaye, toh hum Pandavon ko zaroor hara denge!"

Duryodhana ki baat khatam hote hi sabhi raja aur soldiers khushi se jhoom uthe. Sabne zordaar cheers ke saath kaha, "Guru Drona ki jai!" Poori sena mein ek nayi umeed aur khushi bhar gayi.

Phir Guru Drona ne Duryodhana ki taraf dekha aur apna jawab dena shuru kiya.""", 7: """Guru Drona ne Duryodhana ka offer maan liya. Unhone kaha, "Mujhe sabhi Vedas aur special weapons ki knowledge hai. Main Pandavon se poori taqat se ladunga. Par ek baat yaad rakhna—main Dhrishtadyumna ko nahi maar paunga, kyunki woh mere ant ke liye hi paida hua hai."

Iske baad Duryodhana aur sabhi rajaon ne dhol aur shankh baja kar Guru Drona ko apna naya commander bana diya. Poori Kaurava sena khushi se jhoom uthi.

Ab dono armies yudh ke liye taiyaar ho gayin. Drona ne apni sena ko ek gaadi (Sakata) ke shape mein khada kiya. Sabse aage Karna khada tha. Karna ko dekh kar Kaurava soldiers apna dukh bhool gaye aur unhe jeet ka poora bharosa ho gaya.

Doosri taraf, Raja Yudhishthira ne Pandava sena ko ek bagule (Krauncha) ke shape mein khada kiya. Unke sabse aage Arjuna aur Krishna the, aur unka Hanuman wala jhanda aasman mein lehra raha tha. Yudh ke maidan mein Karna aur Arjuna bilkul aamne-saamne khade the.

Jaise hi Guru Drona aage badhe, aasman mein ajeeb signs dikhne lage. Tez dhool udne lagi, zameen hilne lagi aur aasman mein kaale pakshi mandrane lage, jaise kisi bade toofan ka ishara ho.

Phir zabardast ladai shuru hui! Guru Drona ne Pandavon par ek saath saikdon teer chala diye. Unke hamle se Pandava sena tez hawa mein udte pakshiyon ki tarah bikhar gayi.

Tab Dhrishtadyumna aage aaya aur usne apne teeron se Drona ke hamle ko roka. Dono ke beech bahut kadak muqabla hua.

Lekin Guru Drona ne jaldi hi apni army ko phir se sambhala aur sheron ki tarah hamla kar diya. Woh apne rath par aag ke ek gole ki tarah poore maidan mein ghoomne lage. Unki speed aur skill dekh kar dushmanon ke dil mein darr baith gaya!""", 8: """Sanjaya ne aage ki kahani sunayi.

Guru Drona ko itni tezi se hamla karte dekh kar Pandavon ne ek plan banaya. Yudhishthira ne Arjuna aur Dhrishtadyumna se kaha ki sab milkar Drona ko chaaron taraf se gher lein.

Jaldi hi Arjuna, Bhima, Abhimanyu, Ghatotkacha, Satyaki aur baaki sabhi Pandava warriors ne Drona ko gher liya.

Lekin Guru Drona bilkul nahi dare. Bhale hi woh boodhe the, par woh ek jawaan warrior ki tarah tezi se lad rahe the. Unke tez laal ghode hawa ki tarah daud rahe the. Drona ne har taraf itne teer chalaye ki poora maidan unke teeron se bhar gaya. Bas unke rath ka jhanda bijli ki tarah chamakta dikh raha tha.

Unki taqat dekh kar kai Pandava soldiers darr kar peeche hatne lage. Phir bhi, Bhima, Arjuna aur Satyaki jaise brave warriors unke saamne date rahe aur muqabla karte rahe.

Guru Drona ne Duryodhana ke liye bahut bahaduri se ladai ki aur apni skills se sabko hairan kar diya. Lekin aakhir mein, wahi hua jo Drona ne pehle kaha tha—Dhrishtadyumna ke haathon unka ant ho gaya.

Jab mahan guru Drona maidan mein gire, toh har taraf dukh ki aawaz goonj uthi. Doosri taraf, Pandavas ne is badi jeet par khushi ke naare lagaye, jisse poori dharti goonj uthi.""", 9: """Guru Drona ke jaane ki khabar sunkar Raja Dhritarashtra ko bahut bada shock laga. Unhe is baat par yakeen hi nahi ho raha tha.

Unhone Sanjaya se poocha, "Sanjaya, Guru Drona toh weapons chalane mein sabse mahir the. Dhrishtadyumna ne unhe kaise haraya? Kya ladai ke beech unka rath toot gaya tha? Ya unka dhanush toot gaya tha? Ya phir kisi pal unka dhyan bhatak gaya tha?"

Dhritarashtra ko laga ki kismat ke aage kisi ki nahi chalti. Itne samajhdar aur careful guru bhi is yudh mein nahi bach sake. Unhone dukh se kaha ki itni buri khabar sunkar bhi mera dil abhi tak kaise dhadak raha hai.

Phir unhe Guru Drona ka golden rath aur unke tez laal ghode yaad aaye. Woh ghode kabhi thakte nahi the aur na hi dhol-nagaadon ke shor se darte the. Dhritarashtra ne poocha, "Koi un strong ghodon ko kaise rok sakta hai?"

Unhone khud hi andaza lagaya, "Shayad Yudhishthira aur unke bhaiyon ne Drona ko chaaron taraf se gher liya hoga. Aur Arjuna ne Dhrishtadyumna ki madad ki hogi. Ya phir saare dushman rajaon ne unhe aise gher liya hoga jaise cheentiyan kisi saamp ko gher leti hain.

Mujhe yeh bhi batao, kya Drona ki raksha karne wale guards unhe akela chhod kar bhaag gaye the? Kyunki Guru Drona kabhi darr kar peeche nahi hat sakte!"

Itna bolte-bolte Dhritarashtra ka mann bahut bhaari ho gaya aur unhe chakkar aane lage. Unhone kaha, "Sanjaya, abhi thodi der ke liye ruk jao. Jab main thoda sambhal jaunga, tab aage ke sawal poochunga." """, 10: """Rishi Vaisampayana ne aage bataya ki itna kehte hi Raja Dhritarashtra dukh ke maare behosh ho kar zameen par gir gaye.

Unke helpers ne turant un par thanda paani chhidka aur unhe hawa ki. Mahal ki mahilaon ne unhe pyaar se uthaya aur unki seat par baithaya. Thodi der baad, Dhritarashtra ko hosh aaya aur unhone phir se Sanjaya se sawal poochne shuru kiye.

Dhritarashtra ne poocha, "Sanjaya, jab Pandavon ke bade-bade warriors ne Guru Drona par hamla kiya, tab hamari army mein se unhe kisne roka?

Jab Suraj ki tarah chamakne wale Yudhishthira aur dus hazaar haathiyon jitni taqat rakhne wale Bhima aage badhe, toh unke saamne kaun khada hua?

Aur jab Arjuna apne safed ghodon wale rath par aaya—jiske rath par Hanuman wala jhanda tha aur jise khud Krishna chala rahe the—tab tum sabke mann mein kya chal raha tha? Arjuna aur Krishna ki jodi ko toh koi nahi hara sakta! Sach batana, kya hamare soldiers ne Drona ka saath diya, ya woh darr kar bhaag gaye?

Nakula, Sahadeva, Satyaki, Abhimanyu, Dhrishtadyumna, Shikhandi aur giant Ghatotkacha ko kisne roka? Itne saare brave warriors ko dekh kar mere beton ki army kaise tiki?"

Phir Dhritarashtra ko ek gehri baat samajh aayi. Unhone kaha, "Jin logon ke saath itne loyal dost aur khud Bhagwan Krishna hon, unhe bhala kaun hara sakta hai? Krishna is poori duniya ke malik hain. Ab main unhi ko yaad karunga, taaki mere dil ko thoda sukoon aur himmat mil sake." """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """, 19: """  """, 20: """  """,
            21: """  """, 22: """  """, 23: """  """, 24: """  """, 25: """  """, 26: """  """, 27: """  """, 28: """  """, 29: """  """, 30: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.1.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.2 - Abhimanyu-badha Parva
    # ==================================================

    with st.expander("Chapter 7.2  Abhimanyu-badha Parva"):
        sections = ["XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
                    "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
                    "LI", "LII", "LIII", "LVI", "LVII", "LVIII", "LIX", "LX", "LXI", "LXII",
                    "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX", "LXXI", "LXXII",
                    "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", "LXXX", "LXXXI",
                    "LXXXII", "LXXXIII", "LXXXIV"]
        section_text = {
            1: """  """, 2: """  """, 3: """  """, 4: """  """, 5: """  """, 6: """  """, 7: """  """, 8: """  """, 9: """  """, 10: """  """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """, 19: """  """, 20: """  """,
            21: """  """, 22: """  """, 23: """  """, 24: """  """, 25: """  """, 26: """  """, 27: """  """, 28: """  """, 29: """  """, 30: """  """,
            31: """  """, 32: """  """, 33: """  """, 34: """  """, 35: """  """, 36: """  """, 37: """  """, 38: """  """, 39: """  """, 40: """  """,
            41: """  """, 42: """  """, 43: """  """, 44: """  """, 45: """  """, 46: """  """, 47: """  """, 48: """  """, 49: """  """, 50: """  """,
            51: """  """, 52: """  """, 53: """  """, 54: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.2.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.3 - Jayadratha-Vadha Parva
    # ==================================================

    with st.expander("Chapter 7.3  Jayadratha-Vadha Parva"):
        sections = ["LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX", "XC", "XCI", "XCII", "XCIII", "XCIV",
                    "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", "C", "CI", "CII", "CIII", "CIV",
                    "CV", "CVI", "CVII", "CVIII", "CIX", "CX", "CXI", "CXII", "CXIII", "CXIV",
                    "CXV", "CXVI", "CXVII", "CXVIII", "CXIX", "CXX", "CXXI", "CXXII", "CXXII", "CXXIV",
                    "CXXV", "CXXVI", "CXXVII", "CXXVIII", "CXXIX", "CXXX", "CXXXI", "CXXXII", "CXXXIII", "CXXXIV",
                    "CXXXV", "CXXXVI", "CXXXVII", "CXXXVIII", "CXXXIX", "CXL", "CXLI", "CXLII", "CXLIII", "CXLIV",
                    "CXLV", "CXLVI", "CXLVII", "CXLVIII", "CXLIX", "CI", "CLI"]
        section_text = {
            1: """  """, 2: """  """, 3: """  """, 4: """  """, 5: """  """, 6: """  """, 7: """  """, 8: """  """, 9: """  """, 10: """  """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """, 19: """  """, 20: """  """,
            21: """  """, 22: """  """, 23: """  """, 24: """  """, 25: """  """, 26: """  """, 27: """  """, 28: """  """, 29: """  """, 30: """  """,
            31: """  """, 32: """  """, 33: """  """, 34: """  """, 35: """  """, 36: """  """, 37: """  """, 38: """  """, 39: """  """, 40: """  """,
            41: """  """, 42: """  """, 43: """  """, 44: """  """, 45: """  """, 46: """  """, 47: """  """, 48: """  """, 49: """  """, 50: """  """,
            51: """  """, 52: """  """, 53: """  """, 54: """  """, 55: """  """, 56: """  """, 57: """  """, 58: """  """, 59: """  """, 60: """  """,
            61: """  """, 62: """  """, 63: """  """, 64: """  """, 65: """  """, 66: """  """, 67: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.3.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.4 - Ghatotkacha-badha Parva
    # ==================================================

    with st.expander("Chapter 7.4  Ghatotkacha-badha Parva"):
        sections = ["CLII", "CLIII", "CLIV", "CLV", "CLVI", "CLVII", "CLVIII", "CLIX", "CLX", "CLXI",
                    "CLXII", "CLXIII", "CLXIV", "CLXV", "CLXVI", "CLXVII", "CLXVIII", "CLXIX", "CLXX", "CLXXI",
                    "CLXXII", "CLXXIII", "CLXXIV", "CLXXV", "CLXXVI", "CLXXVII", "CLXXVIII", "CLXXIX", "CLXXX",
                    "CLXXXI", "CLXXXII", "CLXXXIII"]
        section_text = {
            1: """  """, 2: """  """, 3: """  """, 4: """  """, 5: """  """, 6: """  """, 7: """  """, 8: """  """, 9: """  """, 10: """  """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """, 19: """  """, 20: """  """,
            21: """  """, 22: """  """, 23: """  """, 24: """  """, 25: """  """, 26: """  """, 27: """  """, 28: """  """, 29: """  """, 30: """  """,
            31: """  """, 32: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.4.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")

    # ==================================================
    # Chapter 7.5 - Drona-vadha Parva
    # ==================================================

    with st.expander("Chapter 7.5  Drona-vadha Parva"):
        sections = ["CLXXXIV", "CLXXXV", "CLXXXVI", "CLXXXVII", "CLXXXVIII", "CXC", "CXCI", "CXCII", "CXCIII",
                    "CXCIV", "CXCV", "CXCVI", "CXCVII", "CXCVIII", "CXCIX", "CC", "CCI", "CCII"]
        section_text = {
            1: """ Raja Dhritarashtra ne Sanjaya se kaha, "Sanjaya, ab Bhagwan Krishna ki mahan baatein suno. Unhone aise kaam kiye hain jo is duniya mein koi aur nahi kar sakta.

Jab Krishna chhote the aur Nanda ji ke ghar bade ho rahe the, tabhi sabne unki taqat dekh li thi. Unhone bina kisi weapon ke, sirf apne haathon se bade-bade demons ko haraya aur cruel Raja Kansa ko bhi khatam kiya.

Bade hokar Krishna ne duniya ke kai strong rajaon ko haraya. Woh samundar ke andar jaakar apna special shankh, Panchajanya, jeet kar laaye. Phir unhe Sudarshana Chakra mila. Itna hi nahi, woh swarg se Parijata ka phool bhi le aaye, aur devtaon ke raja Indra bhi unhe rok nahi paaye.

Mujhe aaj bhi yaad hai jab Krishna mere darbar mein aaye the aur unhone apna Vishwaroop dikhaya tha. Maine khud apni aankhon se unki divya shakti dekhi thi.

Agar aaj Krishna ne Pandavon ke liye hathiyar utha liye, ya apne bade bhai Balarama aur apni army ko bula liya, toh koi unke saamne tik nahi payega. Sach toh yeh hai ki Krishna aur Arjuna ek hi aatma ke do roop hain—Nara aur Narayana. Agar woh chahein, toh sirf apne mann se hi is poori sena ko ek pal mein hara sakte hain. Par apni achhai ki wajah se woh aisa nahi karte.

Mera bewakoof beta Duryodhana yeh sach kabhi nahi samjha. Bhishma aur Drona jaise bade warriors ke girne ke baad ab mujhe sab saaf dikh raha hai. Yudhishthira ke saath sachai aur dharm hai, isliye jeet unhi ki hogi. Yeh sab meri hi galtiyon ka nateeja hai, aur ab kismat ko koi nahi badal sakta.

Ab tum mujhe aage ki poori kahani sunao ki yudh ke maidan mein kya-kya hua." """, 2: """ Sanjaya ne aage ki kahani shuru ki.

Jab Guru Drona Kaurava army ke commander bane, toh unhone Duryodhana se kaha, "Tumne mujhe itna bada honour diya hai. Bolo, tumhe kya wish chahiye?"

Duryodhana ne Karna aur Duhsasana ke saath baat ki. Phir usne Drona se kaha, "Gurudev, agar aap mujhe kuch dena chahte hain, toh bas Yudhishthira ko zinda pakad kar mere paas le aaiye."

Yeh sunkar Guru Drona ko thoda ajeeb laga, par woh khush bhi hue. Unhone kaha, "Wah! Yudhishthira itna achha insaan hai ki uska koi dushman hi nahi hai. Tumne uski jaan nahi maangi. Kya tum usse dosti karke shanti chahte ho?"

Par Duryodhana apne mann ki baat chhupa nahi saka. Usne apna chalak plan bata diya: "Nahi Gurudev! Agar Yudhishthira mara gaya, toh Arjuna gusse mein hum sabko khatam kar dega. Lekin Yudhishthira apni baat ka pakka hai. Agar hum use zinda pakad lein, toh hum use phir se dice game mein hara denge. Phir sabhi Pandavas chupchap jungle wapas chale jayenge, aur jeet hamesha ke liye hamari hogi!"

Samajhdar Drona Duryodhana ki chalaki samajh gaye. Unhone thoda socha aur ek shart rakhi. Unhone kaha, "Main Yudhishthira ko pakad toh lunga, par sirf tab jab Arjuna uske paas na ho. Main Arjuna ka pehla teacher zaroor hoon, par ab woh bahut powerful ho gaya hai. Jab tak Arjuna wahan hai, koi bhi Yudhishthira ko chhoo nahi sakta. Isliye pehle kisi tarah Arjuna ko wahan se door le jao."

Itna sunkar hi Duryodhana bahut khush ho gaya. Use laga ki Yudhishthira ab pakka pakda jayega. Duryodhana ko dar tha ki kahin Drona Pandavon par daya na kar dein, isliye usne poori army ke saamne yeh baat zor se announce kar di, taaki Drona apna vaada poora karein. """, 3: """ Sanjaya ne aage ki kahani sunayi.

Jab Kaurava soldiers ne Drona ka vaada suna, toh woh khushi se shankh bajane lage aur zor-zor se cheers karne lage.

Lekin Raja Yudhishthira ko apne spies se jaldi hi Drona ke is plan ka pata chal gaya. Unhone turant apne bhaiyon aur sabhi allies ko bulaya. Yudhishthira ne Arjuna se kaha, "Arjuna, Drona mujhe pakadne ka plan bana rahe hain. Aaj tum mere paas rehkar hi ladai karna, taaki Duryodhana ka plan poora na ho sake."

Arjuna ne bade bharose se jawab diya, "Bhaiya, main apne Guru ko maar toh nahi sakta, par aapko unke haathon mein bhi nahi jaane dunga. Chahe aasman toot kar gir jaye ya dharti phat jaye, jab tak main zinda hoon, koi aapko pakad nahi sakta. Aap bilkul chinta mat kijiye, main apna vaada hamesha poora karta hoon."

Phir dono taraf se shankh aur dhol bajne lage. Dono armies dhire-dhire aamne-saamne aayin aur ek zabardast ladai shuru ho gayi.

Shuruat mein dono teams barabar lag rahi thin—ek taraf Guru Drona apni sena ko bacha rahe the, aur doosri taraf Arjuna Pandavon ki raksha kar rahe the.

Lekin thodi hi der mein Guru Drona apne golden rath par itni tezi se aage badhe ki aisa laga jaise woh ek saath har jagah maujood hain. Dopahar ke tez suraj ki tarah chamakte hue Drona ne chaaron taraf teeron ki baarish kar di. Pandava sena ke liye unke saamne dekhna bhi mushkil ho gaya, aur Drona ne Dhrishtadyumna ki sena ko peeche dhakelna shuru kar diya! """, 4: """ Sanjaya ne aage ki kahani sunayi.

Yudh ke maidan mein Guru Drona ek tez toofan ki tarah aage badh rahe the. Unke dhanush ki aawaz badalon ki garaj jaisi lag rahi thi. Unhone itne teer chalaye ki Pandava sena mein har taraf halchal mach gayi.

Tab Yudhishthira aur unke saare brave warriors Drona ko rokne ke liye daude. Unhe rokne ke liye Kaurava warriors bhi saamne aa gaye, aur maidan mein kai zabardast one-on-one muqable shuru ho gaye!

Sahadeva aur Shakuni ke rath toot gaye, toh dono ne gada utha kar ladai ki. Bhima, Nakula, Satyaki, Drupada aur Shikhandi bhi apne-apne opponents se poori taqat se bhid gaye. Ek taraf Ghatotkacha aur Alamvusha apni magic powers dikha kar lad rahe the.

Lekin us din sabse zyada chamka Arjuna ka jawaan beta—Abhimanyu!

Pehle Paurava ne Abhimanyu par hamla kiya. Jab Abhimanyu ka dhanush toot gaya, toh usne turant apni talwar aur dhal utha li. Usne badi phurti se Paurava ko haraya aur apne kabze mein kar liya.

Paurava ko mushkil mein dekh kar Raja Jayadratha apne rath se kood pada. Abhimanyu ne Paurava ko chhod diya aur Jayadratha se talwar ki ladai shuru kar di. Dono sher aur cheete ki tarah lad rahe the. Aakhir mein, Jayadratha ki talwar Abhimanyu ki strong dhal se takra kar toot gayi, aur use peeche hat kar apne rath par bhaagna pada.

Iske baad Raja Salya ne Abhimanyu par ek chamakta hua loha ka bhala phenka. Par tez Abhimanyu ne ek baaz ki tarah us bhale ko hawa mein hi pakad liya aur wapas Salya ki taraf phenk diya, jisse Salya ka rath chalane wala gir gaya!

Abhimanyu ki yeh bahaduri dekh kar Yudhishthira, Bhima aur sabhi Pandava heroes khushi se chilla uthe, "Shabash! Shabash!"

Par Duryodhana aur uske bhaiyon ko yeh bilkul pasand nahi aaya. Gusse mein aakar un sabne Abhimanyu ko chaaron taraf se gher liya, aur Salya bhi badla lene ke liye uski taraf dauda! """, 5: """ Raja Dhritarashtra ne kaha, "Sanjaya, tumne bahut achhi ladaiyon ki kahani sunayi. Ab mujhe batao ki Salya aur Abhimanyu ke beech kya hua?"

Sanjaya ne aage ki kahani sunayi.

Apne rath chalane wale ko gira dekh kar Raja Salya bahut gussa ho gaya. Woh ek bhaari loha ki gada lekar rath se neeche kood pada. Abhimanyu bhi ek badi gada lekar taiyaar ho gaya aur bola, "Aao, lado!"

Lekin tabhi Bhima wahan aa gaye. Unhone pyaar se Abhimanyu ko samjha kar peeche hataya aur khud Salya ke saamne khade ho gaye.

Is poori duniya mein sirf Bhima aur Salya hi ek doosre ki taqat ka muqabla kar sakte the. Dono ke beech gada ki ladai shuru hui. Chaaron taraf shankh aur dhol bajne lage, aur saare soldiers "Shabash! Shabash!" chillane lage.

Bhima aur Salya do taqatwar saandon ki tarah ghoom-ghoom kar ladne lage. Jab unki gadayein aapas mein takrati, toh raat ke jugnuon ki tarah chingariyan udti thin! Dono ne ek doosre par bade zordaar vaar kiye, par woh pahad ki tarah apni jagah par date rahe.

Aakhir mein, dono tez daudte hue aaye aur ek hi pal mein ek doosre par aisa vaar kiya ki dono zameen par gir pade!

Turant hi Kritavarman daud kar aaya aur behosh Salya ko apne rath par bitha kar maidan se door le gaya. Lekin himmatwale Bhima palak jhapakte hi phir se khade ho gaye, unke haath mein abhi bhi gada thi!

Salya ko maidan se jaate dekh kar Kaurava sena darr gayi aur idhar-udhar bhaagne lagi. Pandavas ne khushi se shankh aur dhol bajaye aur jeet ka jashn manaya! """, 6: """ Sanjaya ne aage ki kahani sunayi.

Jab Kaurava sena haarne lagi, tab Karna ka brave beta Vrishasena akela hi aage aaya. Usne garmi ke suraj ki tarah tez teer chalaye aur har taraf dushmanon ko rok diya.

Use rokne ke liye Nakula ka beta Satanika aur Draupadi ke baaki bete saath aaye. Unhone Vrishasena par teeron ki baarish kar di. Phir Ashwatthama aur baaki Kaurava warriors bhi wahan aa gaye, aur ek badi ladai shuru ho gayi.

Apni sena ko peeche hat-ta dekh kar Guru Drona ne sabko himmat di aur kaha, "Daro mat, bhaago mat!" Phir Drona apne laal ghodon wale rath par baith kar seedha Raja Yudhishthira ko pakadne ke liye aage badhe.

Kumara, Yugandhara, Vyaghradatta aur Singhasena jaise brave Pandava warriors ne Drona ko rokne ki poori koshish ki. Lekin Drona ne sabko hara diya aur bilkul Yudhishthira ke rath ke saamne pahunch gaye!

Kaurava soldiers khushi se chillane lage, "Dekho! Aaj Drona Yudhishthira ko pakad lenge aur Duryodhana jeet jayega!"

Lekin theek usi pal, Arjuna bijli ki tezi se wahan pahunch gaye! Arjuna ne itni fast arrows chalaye ki poore aasman aur maidan mein teeron ka ek jaal bich gaya. Kisi ko kuch dikhai nahi de raha tha.

Usi waqt suraj bhi doob gaya aur chaaron taraf shaam ka andhera chha gaya. Ab yeh samajh nahi aa raha tha ki kaun dost hai aur kaun dushman. Isliye Drona aur Duryodhana ne apni sena ko wapas bula liya.

Arjuna ne bhi apni army ko safely camp wapas bheja aur khud Krishna ke saath peeche-peeche laute. Saare Pandavas ne khush hokar Arjuna ki tareef ki, kyunki unhone sahi waqt par aakar sabko bacha liya tha! """, 7: """ Sanjaya ne aage ki kahani sunayi.

Us din ka yudh khatam hone par sabhi soldiers apne-apne tents mein wapas chale gaye. Guru Drona ko bahut bura lag raha tha kyunki woh apna vaada poora nahi kar paaye the.

Unhone Duryodhana se kaha, "Maine pehle hi kaha tha ki jab tak Arjuna aur Krishna Yudhishthira ke saath hain, koi unhe pakad nahi sakta. Agar koi Arjuna ko challenge karke maidan ke doosre hisse mein le jaye, tabhi main Yudhishthira ko pakad paunga."

Yeh sunkar Trigarta ke Raja Susarman aur unke bhai aage aaye. Woh pehle se hi Arjuna se gussa the. Unhone aur unke saath aaye hazaaron warriors ne aag jala kar ek pakki kasam khayi—"Aaj ya toh hum Arjuna ko harayenge, ya phir maidan se wapas nahi lautenge!"

Phir woh maidan ke south side mein gaye aur Arjuna ko ladai ke liye challenge karne lage.

Brave Arjuna kabhi kisi challenge se peeche nahi hat-te the. Unhone Yudhishthira se wahan jaane ki permission maangi. Yudhishthira ko thodi chinta hui, toh Arjuna ne unki raksha ke liye ek bahut brave warrior, Satyajit, ko chuna. Arjuna ne kaha, "Jab tak Satyajit aapke paas hai, Drona aapko chhoo bhi nahi sakte. Par agar use kuch ho jaye, toh aap turant surakshit jagah chale jaana."

Yudhishthira ne Arjuna ko gale lagaya aur unhe aashirwad diya. Phir Arjuna ek sher ki tarah Trigartas se ladne nikal pade.

Arjuna ko jaate dekh kar Duryodhana ki sena bahut khush ho gayi. Woh Yudhishthira ko pakadne ke liye tezi se aage badhi, aur dono armies barish ki do badi nadiyon ki tarah aapas mein takra gayin! """, 8: """ Sanjaya ne aage ki kahani sunayi.

Trigarta ke warriors—jinhe Samsaptakas kaha jata tha—ek khule maidan mein aadhe chand ke shape mein khade ho gaye. Arjuna ko aate dekh kar woh khushi se zor-zor se chillane lage.

Arjuna thoda muskuraye aur Krishna se bole, "Dekho Krishna, yeh log kitne khush hain, jabki inhe pata hai ki aage bahut mushkil ladai hai. Par sachhe warriors bina dare ladne mein hi khushi maante hain."

Phir Arjuna ne apna golden shankh, Devadatta, itni zor se bajaya ki uski aawaz chaaron taraf goonj uthi. Us tez aawaz ko sunkar Samsaptakas aur unke ghode ek pal ke liye statue ki tarah jam gaye!

Thodi der mein unhone khud ko sambhala aur ek saath Arjuna par hazaaron teer chala diye, jaise baarish ke baadal baras rahe hon. Par tez Arjuna ne unke teeron ko hawa mein hi kaat diya. Unhone dushmanon ke golden flags gira diye aur Sudhanvan ko hara diya.

Apne ek leader ko girte dekh kar baaki soldiers darr gaye aur Duryodhana ki sena ki taraf bhaagne lage.

Tab Trigarta ke raja ne unhe rok kar kaha, "Ruko! Bhaago mat! Humne sabke saamne kasam khayi thi. Agar hum darr kar bhaag gaye, toh log hamara mazak udayenge. Apni poori himmat se lado!"

Raja ki baat sunkar unmein phir se himmat aa gayi. Unhone shankh bajaye aur ek saath milkar phir se Arjuna ka saamna karne laut aaye! """, 9: """ Sanjaya ne aage ki kahani sunayi.

Samsaptakas ko wapas aate dekh kar Arjuna ne Krishna se kaha, "Krishna, rath ko unki taraf le chalo. Aaj main inhe apni poori taqat dikhaunga." Krishna muskuraye aur safed ghodon ko tezi se maidan mein le gaye.

Jaldi hi dushman ke soldiers ne Arjuna aur Krishna ko chaaron taraf se gher liya aur itne teer chalaye ki dono bilkul chhup gaye.

Tab Arjuna ne apna shankh bajaya aur ek magical weapon—Tvashtra—chalaya. Achanak, poore maidan mein Arjuna aur Krishna ki hazaaron copies dikhne lagin! Dushman ke soldiers confuse ho gaye. Unhe laga har taraf Arjuna hi hai, aur woh galti se aapas mein hi ladne lage!

Phir bhi, bache hue Samsaptakas ne ek saath itne teer chalaye ki Arjuna aur Krishna phir se teeron ke badal mein chhup gaye. Unhe laga ki woh jeet gaye hain, isliye woh khushi se dhol aur shankh bajane lage.

Andhere mein Krishna ne thoda ghabra kar poocha, "Arjuna, tum kahan ho? Sab theek hai na?"

Krishna ki aawaz sunkar Arjuna ne turant Vayavya (hawa) weapon chalaya. Ek tez toofani hawa chali aur usne saare teeron ke jaal ko uda diya. Dushmanon ke rath aur soldiers sookhe patton ki tarah hawa mein ud kar door ja gire! Is tarah Arjuna ne Samsaptakas ko hara diya.

Lekin usi waqt, maidan ke doosre hisse mein, jab Arjuna yahan busy the, Guru Drona apni poori sena lekar Raja Yudhishthira ko pakadne ke liye aage badh gaye! """, 10: """ Sanjaya ne aage ki kahani sunayi.

Agli subah, Guru Drona ne Duryodhana se kaha, "Maine Arjuna ko Samsaptakas ke saath busy kar diya hai. Ab main Yudhishthira ko pakadne ja raha hoon!"

Drona ne apni army ko ek bade baaz (Garuda) ke shape mein khada kiya. Woh khud us baaz ki chonch par khade hue, Duryodhana sir par, aur Karna poonch par khade the. Beech mein Pragjyotisha ke raja ek vishal haathi par baithe chamak rahe the.

Doosri taraf, Yudhishthira ne apni sena ko aadhe chand ke shape mein khada kiya. Unhone Dhrishtadyumna se kaha, "Drona mujhe pakad na paayein, iska dhyan rakhna."

Dhrishtadyumna ne bharosa dilaya, "Raja ji, aap bilkul chinta mat kijiye. Jab tak main yahan hoon, Drona aapko pakad nahi sakte." Yeh keh kar woh seedha Drona ki taraf badhe.

Dhrishtadyumna ko saamne dekh kar Drona thoda ruk gaye, par tabhi Duryodhana ke bhai Durmukha ne aage aakar Dhrishtadyumna ko rok liya. Dono ke beech tez ladai shuru ho gayi.

Is beech maidan mein bahut bada shor mach gaya. Ghode, rath aur bade-bade haathi aapas mein takra rahe the. Haathiyon ke daant takrane se toh chingariyan tak udne lagin!

Is bhaag-daud aur shor ke beech, Guru Drona ne mauka dekha aur Pandava sena ko todte hue seedha Raja Yudhishthira ki taraf hamla kar diya! """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.5.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")
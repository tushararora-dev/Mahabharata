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
            1: """  """, 2: """  """, 3: """  """, 4: """  """, 5: """  """, 6: """  """, 7: """  """, 8: """  """, 9: """  """, 10: """  """,
            11: """  """, 12: """  """, 13: """  """, 14: """  """, 15: """  """, 16: """  """, 17: """  """, 18: """  """
        }
        for index, section in enumerate(sections, start=1):
            with st.expander(f"Section 7.5.{index}  Section {section}"):
                text1 = section_text[index]
                create_image_text_layout(text_content=text1, layout="full")
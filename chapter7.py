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
            11: """ Raja Dhritarashtra ne Sanjaya se kaha, "Sanjaya, ab Bhagwan Krishna ki mahan baatein suno. Unhone aise kaam kiye hain jo is duniya mein koi aur nahi kar sakta.

Jab Krishna chhote the aur Nanda ji ke ghar bade ho rahe the, tabhi sabne unki taqat dekh li thi. Unhone bina kisi weapon ke, sirf apne haathon se bade-bade demons ko haraya aur cruel Raja Kansa ko bhi khatam kiya.

Bade hokar Krishna ne duniya ke kai strong rajaon ko haraya. Woh samundar ke andar jaakar apna special shankh, Panchajanya, jeet kar laaye. Phir unhe Sudarshana Chakra mila. Itna hi nahi, woh swarg se Parijata ka phool bhi le aaye, aur devtaon ke raja Indra bhi unhe rok nahi paaye.

Mujhe aaj bhi yaad hai jab Krishna mere darbar mein aaye the aur unhone apna Vishwaroop dikhaya tha. Maine khud apni aankhon se unki divya shakti dekhi thi.

Agar aaj Krishna ne Pandavon ke liye hathiyar utha liye, ya apne bade bhai Balarama aur apni army ko bula liya, toh koi unke saamne tik nahi payega. Sach toh yeh hai ki Krishna aur Arjuna ek hi aatma ke do roop hain—Nara aur Narayana. Agar woh chahein, toh sirf apne mann se hi is poori sena ko ek pal mein hara sakte hain. Par apni achhai ki wajah se woh aisa nahi karte.

Mera bewakoof beta Duryodhana yeh sach kabhi nahi samjha. Bhishma aur Drona jaise bade warriors ke girne ke baad ab mujhe sab saaf dikh raha hai. Yudhishthira ke saath sachai aur dharm hai, isliye jeet unhi ki hogi. Yeh sab meri hi galtiyon ka nateeja hai, aur ab kismat ko koi nahi badal sakta.

Ab tum mujhe aage ki poori kahani sunao ki yudh ke maidan mein kya-kya hua." """, 12: """ Sanjaya ne aage ki kahani shuru ki.

Jab Guru Drona Kaurava army ke commander bane, toh unhone Duryodhana se kaha, "Tumne mujhe itna bada honour diya hai. Bolo, tumhe kya wish chahiye?"

Duryodhana ne Karna aur Duhsasana ke saath baat ki. Phir usne Drona se kaha, "Gurudev, agar aap mujhe kuch dena chahte hain, toh bas Yudhishthira ko zinda pakad kar mere paas le aaiye."

Yeh sunkar Guru Drona ko thoda ajeeb laga, par woh khush bhi hue. Unhone kaha, "Wah! Yudhishthira itna achha insaan hai ki uska koi dushman hi nahi hai. Tumne uski jaan nahi maangi. Kya tum usse dosti karke shanti chahte ho?"

Par Duryodhana apne mann ki baat chhupa nahi saka. Usne apna chalak plan bata diya: "Nahi Gurudev! Agar Yudhishthira mara gaya, toh Arjuna gusse mein hum sabko khatam kar dega. Lekin Yudhishthira apni baat ka pakka hai. Agar hum use zinda pakad lein, toh hum use phir se dice game mein hara denge. Phir sabhi Pandavas chupchap jungle wapas chale jayenge, aur jeet hamesha ke liye hamari hogi!"

Samajhdar Drona Duryodhana ki chalaki samajh gaye. Unhone thoda socha aur ek shart rakhi. Unhone kaha, "Main Yudhishthira ko pakad toh lunga, par sirf tab jab Arjuna uske paas na ho. Main Arjuna ka pehla teacher zaroor hoon, par ab woh bahut powerful ho gaya hai. Jab tak Arjuna wahan hai, koi bhi Yudhishthira ko chhoo nahi sakta. Isliye pehle kisi tarah Arjuna ko wahan se door le jao."

Itna sunkar hi Duryodhana bahut khush ho gaya. Use laga ki Yudhishthira ab pakka pakda jayega. Duryodhana ko dar tha ki kahin Drona Pandavon par daya na kar dein, isliye usne poori army ke saamne yeh baat zor se announce kar di, taaki Drona apna vaada poora karein. """, 13: """ Sanjaya ne aage ki kahani sunayi.

Jab Kaurava soldiers ne Drona ka vaada suna, toh woh khushi se shankh bajane lage aur zor-zor se cheers karne lage.

Lekin Raja Yudhishthira ko apne spies se jaldi hi Drona ke is plan ka pata chal gaya. Unhone turant apne bhaiyon aur sabhi allies ko bulaya. Yudhishthira ne Arjuna se kaha, "Arjuna, Drona mujhe pakadne ka plan bana rahe hain. Aaj tum mere paas rehkar hi ladai karna, taaki Duryodhana ka plan poora na ho sake."

Arjuna ne bade bharose se jawab diya, "Bhaiya, main apne Guru ko maar toh nahi sakta, par aapko unke haathon mein bhi nahi jaane dunga. Chahe aasman toot kar gir jaye ya dharti phat jaye, jab tak main zinda hoon, koi aapko pakad nahi sakta. Aap bilkul chinta mat kijiye, main apna vaada hamesha poora karta hoon."

Phir dono taraf se shankh aur dhol bajne lage. Dono armies dhire-dhire aamne-saamne aayin aur ek zabardast ladai shuru ho gayi.

Shuruat mein dono teams barabar lag rahi thin—ek taraf Guru Drona apni sena ko bacha rahe the, aur doosri taraf Arjuna Pandavon ki raksha kar rahe the.

Lekin thodi hi der mein Guru Drona apne golden rath par itni tezi se aage badhe ki aisa laga jaise woh ek saath har jagah maujood hain. Dopahar ke tez suraj ki tarah chamakte hue Drona ne chaaron taraf teeron ki baarish kar di. Pandava sena ke liye unke saamne dekhna bhi mushkil ho gaya, aur Drona ne Dhrishtadyumna ki sena ko peeche dhakelna shuru kar diya! """, 14: """ Sanjaya ne aage ki kahani sunayi.

Yudh ke maidan mein Guru Drona ek tez toofan ki tarah aage badh rahe the. Unke dhanush ki aawaz badalon ki garaj jaisi lag rahi thi. Unhone itne teer chalaye ki Pandava sena mein har taraf halchal mach gayi.

Tab Yudhishthira aur unke saare brave warriors Drona ko rokne ke liye daude. Unhe rokne ke liye Kaurava warriors bhi saamne aa gaye, aur maidan mein kai zabardast one-on-one muqable shuru ho gaye!

Sahadeva aur Shakuni ke rath toot gaye, toh dono ne gada utha kar ladai ki. Bhima, Nakula, Satyaki, Drupada aur Shikhandi bhi apne-apne opponents se poori taqat se bhid gaye. Ek taraf Ghatotkacha aur Alamvusha apni magic powers dikha kar lad rahe the.

Lekin us din sabse zyada chamka Arjuna ka jawaan beta—Abhimanyu!

Pehle Paurava ne Abhimanyu par hamla kiya. Jab Abhimanyu ka dhanush toot gaya, toh usne turant apni talwar aur dhal utha li. Usne badi phurti se Paurava ko haraya aur apne kabze mein kar liya.

Paurava ko mushkil mein dekh kar Raja Jayadratha apne rath se kood pada. Abhimanyu ne Paurava ko chhod diya aur Jayadratha se talwar ki ladai shuru kar di. Dono sher aur cheete ki tarah lad rahe the. Aakhir mein, Jayadratha ki talwar Abhimanyu ki strong dhal se takra kar toot gayi, aur use peeche hat kar apne rath par bhaagna pada.

Iske baad Raja Salya ne Abhimanyu par ek chamakta hua loha ka bhala phenka. Par tez Abhimanyu ne ek baaz ki tarah us bhale ko hawa mein hi pakad liya aur wapas Salya ki taraf phenk diya, jisse Salya ka rath chalane wala gir gaya!

Abhimanyu ki yeh bahaduri dekh kar Yudhishthira, Bhima aur sabhi Pandava heroes khushi se chilla uthe, "Shabash! Shabash!"

Par Duryodhana aur uske bhaiyon ko yeh bilkul pasand nahi aaya. Gusse mein aakar un sabne Abhimanyu ko chaaron taraf se gher liya, aur Salya bhi badla lene ke liye uski taraf dauda! """, 15: """ Raja Dhritarashtra ne kaha, "Sanjaya, tumne bahut achhi ladaiyon ki kahani sunayi. Ab mujhe batao ki Salya aur Abhimanyu ke beech kya hua?"

Sanjaya ne aage ki kahani sunayi.

Apne rath chalane wale ko gira dekh kar Raja Salya bahut gussa ho gaya. Woh ek bhaari loha ki gada lekar rath se neeche kood pada. Abhimanyu bhi ek badi gada lekar taiyaar ho gaya aur bola, "Aao, lado!"

Lekin tabhi Bhima wahan aa gaye. Unhone pyaar se Abhimanyu ko samjha kar peeche hataya aur khud Salya ke saamne khade ho gaye.

Is poori duniya mein sirf Bhima aur Salya hi ek doosre ki taqat ka muqabla kar sakte the. Dono ke beech gada ki ladai shuru hui. Chaaron taraf shankh aur dhol bajne lage, aur saare soldiers "Shabash! Shabash!" chillane lage.

Bhima aur Salya do taqatwar saandon ki tarah ghoom-ghoom kar ladne lage. Jab unki gadayein aapas mein takrati, toh raat ke jugnuon ki tarah chingariyan udti thin! Dono ne ek doosre par bade zordaar vaar kiye, par woh pahad ki tarah apni jagah par date rahe.

Aakhir mein, dono tez daudte hue aaye aur ek hi pal mein ek doosre par aisa vaar kiya ki dono zameen par gir pade!

Turant hi Kritavarman daud kar aaya aur behosh Salya ko apne rath par bitha kar maidan se door le gaya. Lekin himmatwale Bhima palak jhapakte hi phir se khade ho gaye, unke haath mein abhi bhi gada thi!

Salya ko maidan se jaate dekh kar Kaurava sena darr gayi aur idhar-udhar bhaagne lagi. Pandavas ne khushi se shankh aur dhol bajaye aur jeet ka jashn manaya! """, 16: """ Sanjaya ne aage ki kahani sunayi.

Jab Kaurava sena haarne lagi, tab Karna ka brave beta Vrishasena akela hi aage aaya. Usne garmi ke suraj ki tarah tez teer chalaye aur har taraf dushmanon ko rok diya.

Use rokne ke liye Nakula ka beta Satanika aur Draupadi ke baaki bete saath aaye. Unhone Vrishasena par teeron ki baarish kar di. Phir Ashwatthama aur baaki Kaurava warriors bhi wahan aa gaye, aur ek badi ladai shuru ho gayi.

Apni sena ko peeche hat-ta dekh kar Guru Drona ne sabko himmat di aur kaha, "Daro mat, bhaago mat!" Phir Drona apne laal ghodon wale rath par baith kar seedha Raja Yudhishthira ko pakadne ke liye aage badhe.

Kumara, Yugandhara, Vyaghradatta aur Singhasena jaise brave Pandava warriors ne Drona ko rokne ki poori koshish ki. Lekin Drona ne sabko hara diya aur bilkul Yudhishthira ke rath ke saamne pahunch gaye!

Kaurava soldiers khushi se chillane lage, "Dekho! Aaj Drona Yudhishthira ko pakad lenge aur Duryodhana jeet jayega!"

Lekin theek usi pal, Arjuna bijli ki tezi se wahan pahunch gaye! Arjuna ne itni fast arrows chalaye ki poore aasman aur maidan mein teeron ka ek jaal bich gaya. Kisi ko kuch dikhai nahi de raha tha.

Usi waqt suraj bhi doob gaya aur chaaron taraf shaam ka andhera chha gaya. Ab yeh samajh nahi aa raha tha ki kaun dost hai aur kaun dushman. Isliye Drona aur Duryodhana ne apni sena ko wapas bula liya.

Arjuna ne bhi apni army ko safely camp wapas bheja aur khud Krishna ke saath peeche-peeche laute. Saare Pandavas ne khush hokar Arjuna ki tareef ki, kyunki unhone sahi waqt par aakar sabko bacha liya tha! """, 17: """ Sanjaya ne aage ki kahani sunayi.

Us din ka yudh khatam hone par sabhi soldiers apne-apne tents mein wapas chale gaye. Guru Drona ko bahut bura lag raha tha kyunki woh apna vaada poora nahi kar paaye the.

Unhone Duryodhana se kaha, "Maine pehle hi kaha tha ki jab tak Arjuna aur Krishna Yudhishthira ke saath hain, koi unhe pakad nahi sakta. Agar koi Arjuna ko challenge karke maidan ke doosre hisse mein le jaye, tabhi main Yudhishthira ko pakad paunga."

Yeh sunkar Trigarta ke Raja Susarman aur unke bhai aage aaye. Woh pehle se hi Arjuna se gussa the. Unhone aur unke saath aaye hazaaron warriors ne aag jala kar ek pakki kasam khayi—"Aaj ya toh hum Arjuna ko harayenge, ya phir maidan se wapas nahi lautenge!"

Phir woh maidan ke south side mein gaye aur Arjuna ko ladai ke liye challenge karne lage.

Brave Arjuna kabhi kisi challenge se peeche nahi hat-te the. Unhone Yudhishthira se wahan jaane ki permission maangi. Yudhishthira ko thodi chinta hui, toh Arjuna ne unki raksha ke liye ek bahut brave warrior, Satyajit, ko chuna. Arjuna ne kaha, "Jab tak Satyajit aapke paas hai, Drona aapko chhoo bhi nahi sakte. Par agar use kuch ho jaye, toh aap turant surakshit jagah chale jaana."

Yudhishthira ne Arjuna ko gale lagaya aur unhe aashirwad diya. Phir Arjuna ek sher ki tarah Trigartas se ladne nikal pade.

Arjuna ko jaate dekh kar Duryodhana ki sena bahut khush ho gayi. Woh Yudhishthira ko pakadne ke liye tezi se aage badhi, aur dono armies barish ki do badi nadiyon ki tarah aapas mein takra gayin! """, 18: """ Sanjaya ne aage ki kahani sunayi.

Trigarta ke warriors—jinhe Samsaptakas kaha jata tha—ek khule maidan mein aadhe chand ke shape mein khade ho gaye. Arjuna ko aate dekh kar woh khushi se zor-zor se chillane lage.

Arjuna thoda muskuraye aur Krishna se bole, "Dekho Krishna, yeh log kitne khush hain, jabki inhe pata hai ki aage bahut mushkil ladai hai. Par sachhe warriors bina dare ladne mein hi khushi maante hain."

Phir Arjuna ne apna golden shankh, Devadatta, itni zor se bajaya ki uski aawaz chaaron taraf goonj uthi. Us tez aawaz ko sunkar Samsaptakas aur unke ghode ek pal ke liye statue ki tarah jam gaye!

Thodi der mein unhone khud ko sambhala aur ek saath Arjuna par hazaaron teer chala diye, jaise baarish ke baadal baras rahe hon. Par tez Arjuna ne unke teeron ko hawa mein hi kaat diya. Unhone dushmanon ke golden flags gira diye aur Sudhanvan ko hara diya.

Apne ek leader ko girte dekh kar baaki soldiers darr gaye aur Duryodhana ki sena ki taraf bhaagne lage.

Tab Trigarta ke raja ne unhe rok kar kaha, "Ruko! Bhaago mat! Humne sabke saamne kasam khayi thi. Agar hum darr kar bhaag gaye, toh log hamara mazak udayenge. Apni poori himmat se lado!"

Raja ki baat sunkar unmein phir se himmat aa gayi. Unhone shankh bajaye aur ek saath milkar phir se Arjuna ka saamna karne laut aaye! """, 19: """ Sanjaya ne aage ki kahani sunayi.

Samsaptakas ko wapas aate dekh kar Arjuna ne Krishna se kaha, "Krishna, rath ko unki taraf le chalo. Aaj main inhe apni poori taqat dikhaunga." Krishna muskuraye aur safed ghodon ko tezi se maidan mein le gaye.

Jaldi hi dushman ke soldiers ne Arjuna aur Krishna ko chaaron taraf se gher liya aur itne teer chalaye ki dono bilkul chhup gaye.

Tab Arjuna ne apna shankh bajaya aur ek magical weapon—Tvashtra—chalaya. Achanak, poore maidan mein Arjuna aur Krishna ki hazaaron copies dikhne lagin! Dushman ke soldiers confuse ho gaye. Unhe laga har taraf Arjuna hi hai, aur woh galti se aapas mein hi ladne lage!

Phir bhi, bache hue Samsaptakas ne ek saath itne teer chalaye ki Arjuna aur Krishna phir se teeron ke badal mein chhup gaye. Unhe laga ki woh jeet gaye hain, isliye woh khushi se dhol aur shankh bajane lage.

Andhere mein Krishna ne thoda ghabra kar poocha, "Arjuna, tum kahan ho? Sab theek hai na?"

Krishna ki aawaz sunkar Arjuna ne turant Vayavya (hawa) weapon chalaya. Ek tez toofani hawa chali aur usne saare teeron ke jaal ko uda diya. Dushmanon ke rath aur soldiers sookhe patton ki tarah hawa mein ud kar door ja gire! Is tarah Arjuna ne Samsaptakas ko hara diya.

Lekin usi waqt, maidan ke doosre hisse mein, jab Arjuna yahan busy the, Guru Drona apni poori sena lekar Raja Yudhishthira ko pakadne ke liye aage badh gaye! """, 20: """ Sanjaya ne aage ki kahani sunayi.

Agli subah, Guru Drona ne Duryodhana se kaha, "Maine Arjuna ko Samsaptakas ke saath busy kar diya hai. Ab main Yudhishthira ko pakadne ja raha hoon!"

Drona ne apni army ko ek bade baaz (Garuda) ke shape mein khada kiya. Woh khud us baaz ki chonch par khade hue, Duryodhana sir par, aur Karna poonch par khade the. Beech mein Pragjyotisha ke raja ek vishal haathi par baithe chamak rahe the.

Doosri taraf, Yudhishthira ne apni sena ko aadhe chand ke shape mein khada kiya. Unhone Dhrishtadyumna se kaha, "Drona mujhe pakad na paayein, iska dhyan rakhna."

Dhrishtadyumna ne bharosa dilaya, "Raja ji, aap bilkul chinta mat kijiye. Jab tak main yahan hoon, Drona aapko pakad nahi sakte." Yeh keh kar woh seedha Drona ki taraf badhe.

Dhrishtadyumna ko saamne dekh kar Drona thoda ruk gaye, par tabhi Duryodhana ke bhai Durmukha ne aage aakar Dhrishtadyumna ko rok liya. Dono ke beech tez ladai shuru ho gayi.

Is beech maidan mein bahut bada shor mach gaya. Ghode, rath aur bade-bade haathi aapas mein takra rahe the. Haathiyon ke daant takrane se toh chingariyan tak udne lagin!

Is bhaag-daud aur shor ke beech, Guru Drona ne mauka dekha aur Pandava sena ko todte hue seedha Raja Yudhishthira ki taraf hamla kar diya! """,
            21: """ Sanjaya ne aage ki kahani sunayi.

Jab Guru Drona Raja Yudhishthira ke bilkul paas pahunch gaye, toh unhone teeron ki baarish shuru kar di. Tabhi brave Satyajit—jise Arjuna ne Yudhishthira ki raksha ke liye chuna tha—turant aage aaya aur Drona ke saamne khada ho gaya.

Satyajit aur Drona ke beech zabardast ladai hui. Satyajit ne badi bahaduri se Drona ke rath ka jhanda kaat diya aur un par kai teer chalaye. Yeh dekh kar Pandava soldiers khushi se jhoom uthe. Ek aur warrior, Vrika, bhi Satyajit ki madad karne aa gaya.

Par Guru Drona ke saamne tikna aasaan nahi tha. Drona ne apni poori taqat lagayi aur pehle Vrika ko haraya. Satyajit baar-baar naye dhanush utha kar ladta raha, par aakhir mein Drona ne use bhi hara diya.

Satyajit ke girte hi Yudhishthira ko Arjuna ki baat yaad aayi. Khud ko safe rakhne ke liye, Yudhishthira apne tez ghodon par baith kar maidan se door nikal gaye.

Iske baad Satanika, Shikhandi, Satyaki, aur Dhrishtadyumna jaise kai bade Pandava warriors ne milkar Drona ko gher liya. Sabne un par teer chalaye, par Guru Drona aag ki tarah chamak rahe the. Unhone kisi ko apne paas nahi aane diya aur ek-ek karke sabko peeche dhakel diya.

Drona ki taqat dekh kar Pandava sena mein darr phail gaya aur woh maidan chhod kar idhar-udhar bhaagne lagi! """, 22: """ Raja Dhritarashtra ne poocha, "Sanjaya, jab Guru Drona ne Pandava sena ko peeche dhakel diya, tab kya unke saamne koi brave warrior khada hua?"

Sanjaya ne aage ki kahani sunayi.

Pandava sena ko peeche hat-te dekh kar Duryodhana bahut khush ho gaya. Usne has kar Karna se kaha, "Dekho Karna, Drona ne unki army ko tod diya hai! Woh hiranon ki tarah darr kar bhaag rahe hain. Ab woh wapas nahi aayenge. Aur dekho, Bhima akela ghir gaya hai!"

Par Karna zyada samajhdar tha. Usne Duryodhana ko samjhaya, "Itni jaldi khush mat ho, Duryodhana. Jab tak Bhima zinda hai, woh kabhi haar nahi manega. Pandavas apne saath hue purane dhokhon ko nahi bhoole hain, isliye woh poori jaan laga kar ladenge."

Karna ne aage dikhaya, "Dekho, Bhima wapas mud chuka hai! Aur uske peeche saare Pandava, Pancala aur Matsya warriors milkar Guru Drona ko gherne aa rahe hain. Drona par abhi bahut bada bojh hai. Chalo, hum jaldi jaakar unki madad karte hain!"

Karna ki baat sunkar Duryodhana aur uske bhai turant Drona ke rath ki taraf daude. Doosri taraf, Pandava warriors bhi nayi himmat ke saath zor-zor se garajte hue Drona ka saamna karne wapas aa gaye! """, 23: """ Raja Dhritarashtra ne poocha, "Sanjaya, mujhe un sabhi brave warriors ke rath aur nishanon ke baare mein batao jo Bhima ke saath Guru Drona ki taraf badhe the."

Sanjaya ne woh rangeen nazara sunaya.

Yudh ka maidan kisi sundar painting jaisa lag raha tha! Har Pandava warrior ke rath mein alag-alag rang ke tez ghode jude the—kisi ke safed, kisi ke chandi jaise, toh kisi ke mor aur indradhanush ke rang ke.

Un sabke flags bhi bahut khaas the. Raja Yudhishthira ke rath par golden chand wala flag tha, jisme do dhol jude the jo meethi dhun baja rahe the. Bhima ke flag par chandi ka sher tha, Sahadeva ke flag par ghantiyon wala hans, aur young Abhimanyu ke flag par chamakta hua golden mor! Guru Drona ke rath ka flag bhi sabse alag aur shandar dikh raha tha.

Jaise hi yeh saare warriors Guru Drona ki taraf daude, Kaurava warriors unhe rokne ke liye aage aa gaye. Maidan mein har taraf zabardast muqable shuru ho gaye!

Raja Drupada aur Drona aamne-saamne aaye, aur Raja Virata ne Avanti ke rajkumaron ko roka. Young warriors bhi peeche nahi rahe—Ashwatthama ne Prativindhya se ladai ki, aur Arjuna ke bete Srutakirti ne Duhsasana ke bete ka dhanush tod diya.

Ek taraf Karna akele hi paanch Kekaya bhaiyon se lad raha tha. Dono taraf se itne teer chale ki woh sab teeron ke parde mein chhup gaye. Doosri taraf, Ghatotkacha aur Alambusha pathar, ped aur apni magic powers se ek doosre par hamla kar rahe the.

Ek team Guru Drona ko rokna chahti thi, aur doosri team unhe bachana chahti thi. Aisi badi aur romanchak ladai pehle kabhi kisi ne nahi dekhi thi! """, 24: """ Raja Dhritarashtra ne poocha, "Sanjaya, jab yudh itna tez ho gaya, tab hamari sena aur Pandavas kaise lade?"

Sanjaya ne aage ki kahani sunayi.

Duryodhana apne bade-bade haathiyon ki fauj lekar seedha Bhima ke saamne aa gaya. Lekin taqatwar Bhima ne turant un haathiyon ko peeche dhakel diya. Unhone Duryodhana ka dhanush aur jhanda bhi kaat diya.

Tabhi Pragjyotisha ke raja, Bhagadatta, apne vishal haathi Supratika par baith kar aaye. Supratika ne aate hi Bhima ke rath ko tod kar choor-choor kar diya!

Par Bhima dare nahi. Woh seedha haathi ke neeche ghus gaye aur apne haathon se use maarne lage. Haathi chakkar khaa kar kumhar ke pahiye ki tarah ghoomne laga! Jab haathi ne Bhima ko apni soondh se pakda, toh Bhima ne himmat dikha kar khud ko chhudaya aur bhaag kar apni jaan bachayi.

Charon taraf shor mach gaya ki Bhima haathi ke neeche aa gaye. Yeh sunkar Yudhishthira aur Pandava warriors ne Bhagadatta ko gher liya.

Lekin Bhagadatta aur unka haathi Supratika kisi se nahi ruke! Supratika ne Satyaki ke rath ko utha kar door phenk diya—Satyaki ne kood kar apni jaan bachayi. Jab Bhima phir se aage aaye, toh Supratika ne apni soondh se itna paani chhidka ki Bhima ke ghode darr kar door bhaag gaye!

Abhimanyu, Draupadi ke beton aur baaki Pandava warriors ne milkar Bhagadatta ko rokne ki koshish ki. Par Bhagadatta ne apne haathi ko itni chalaki se chalaya ki poori Pandava sena darr kar idhar-udhar bhaagne lagi! """, 25: """ Sanjaya ne aage ki kahani sunayi.

Jab Arjuna ne door se udti hui dhool aur Pandava soldiers ke rone ki aawaz suni, toh woh samajh gaye ki Bhagadatta ne apna haathi lekar hamla kar diya hai. Arjuna ne Krishna se kaha, "Krishna, Bhagadatta haathi chalane mein duniya ke sabse best warrior hain. Unhe aur unke taqatwar haathi ko sirf hum dono hi rok sakte hain. Chalo, jaldi wahan chalte hain!"

Krishna ne rath ko Bhagadatta ki taraf mod diya. Lekin tabhi, 14,000 Samsaptakas wapas laut aaye aur unhone Arjuna ko ladai ke liye challenge kar diya!

Arjuna ek mushkil mein phans gaye. Ek taraf Bhagadatta Pandavon ko pareshan kar rahe the, aur doosri taraf Samsaptakas peeche se hamla karne ko taiyaar the. Duryodhana aur Karna ne yahi trap banaya tha.

Arjuna ne thoda socha aur ek smart faisla liya. Unhone tay kiya ki pehle woh Samsaptakas ko hara kar khatam karenge, taaki woh peeche se hamla na kar sakein.

Samsaptakas ne Arjuna aur Krishna ko gher kar itne teer chalaye ki dono bilkul chhup gaye. Teeron ke is toofan mein Krishna ko bhi paseena aa gaya. Tab Arjuna ne apna sabse shaktishali Brahma weapon chalaya!

Dekhte hi dekhte Arjuna ne saare Samsaptakas ke rath, flags aur haathiyon ko gira kar unhe poori tarah hara diya.

Yeh dekh kar khud Krishna bhi hairan reh gaye! Unhone haath jod kar Arjuna ki tareef ki, "Arjuna, aaj tumne aisa kaam kiya hai jo devta bhi nahi kar sakte!"

Ab Samsaptakas ki chinta khatam ho chuki thi, isliye Arjuna ne Krishna se kaha, "Chalo Krishna, ab Bhagadatta ko rokne chalte hain!" """, 26: """ Sanjaya ne aage ki kahani sunayi.

Krishna apne safed ghodon ko tez dauda kar Guru Drona ki sena ki taraf le chale. Lekin tabhi, Raja Susarman aur uske bhai peeche se Arjuna ko rokne aa gaye!

Arjuna thodi der ke liye soch mein pad gaye ki pehle inhe rokein ya apne bhaiyon ke paas jayein. Par Krishna ne rath ko moda, aur Arjuna ne turant Susarman ka dhanush kaat diya. Unhone Susarman ke bheje hue bhaale ko hawa mein hi tod diya aur use behosh kar diya.

Ab Arjuna tezi se Kaurava sena ki taraf badhe. Woh aag ki tarah aage badh rahe the. Dus hazaar brave warriors ne unhe gherne ki koshish ki, par koi bhi Arjuna ko rok nahi paya.

Tabhi Raja Bhagadatta apne vishal haathi par baith kar Arjuna ke saamne aa gaye!

Ab Arjuna ke rath aur Bhagadatta ke haathi ke beech ek shandar muqabla shuru hua. Bhagadatta ne baarish ki tarah teer chalaye, par Arjuna ne sabko hawa mein hi kaat diya.

Jab woh gussa hua haathi seedha unhe kuchalne aaya, toh smart Krishna ne badi chalaki se rath ko ek taraf mod kar bacha liya.

Is dauran Arjuna ke paas mauka tha ki woh Bhagadatta par peeche se hamla kar dein. Lekin Arjuna ne aisa nahi kiya! Woh yudh ke sachhe rules maante the, aur peeche se vaar karna galat tha.

Par tabhi us haathi ne Pandava sena ke doosre soldiers aur rathon ko girana shuru kar diya. Yeh dekh kar Arjuna ko bahut gussa aa gaya! """, 27: """ Raja Dhritarashtra ne poocha, "Sanjaya, phir Arjuna aur Bhagadatta ke beech kya hua?"

Sanjaya ne aage ki kahani sunayi.

Bhagadatta ne apne haathi par baith kar Arjuna aur Krishna par teeron aur bhaalon ki baarish kar di. Par Arjuna ne unka dhanush kaat diya, bhaalon ke tukde kar diye, aur haathi ka armour bhi tod diya. Ek bhaale se Arjuna ka mukut thoda hila, par Arjuna ne use seedha kiya aur phir se ladne lage.

Jab Bhagadatta ko laga ki woh haarne wale hain, toh unhone ek special mantra padha. Unhone apne haathi chalane wale hook ko sabse khatarnak **Vaishnava weapon** mein badal diya aur seedha Arjuna par phenk diya!

Yeh dekh kar Krishna turant Arjuna ke aage aa gaye aur us weapon ko apni chhaati par le liya! Jaise hi woh weapon Krishna se takraya, woh ek sundar phoolon ki mala ban gaya!

Arjuna ko thoda bura laga. Unhone Krishna se kaha, "Krishna, aapne vaada kiya tha ki aap sirf rath chalayenge, ladenge nahi. Phir aap beech mein kyun aaye? Main khud lad sakta tha."

Krishna ne pyaar se ek secret bataya, "Arjuna, yeh Vaishnava weapon mera hi tha. Bahut pehle maine ise Narakasura ko diya tha, aur wahan se yeh Bhagadatta ko mila. Is duniya mein koi bhi is weapon ko nahi rok sakta tha. Tumhari jaan bachane ke liye mujhe yeh karna pada!"

Ab Bhagadatta ke paas woh special weapon nahi bacha tha. Tab Arjuna ne ek tez teer chalaya jisse woh vishal haathi zameen par gir gaya, aur uske baad Arjuna ne Raja Bhagadatta ko bhi hara diya.

Bhagadatta ke girte hi Arjuna ne baaki Kaurava sena ko bhi tez hawa ki tarah peeche dhakel diya! """, 28: """ Sanjaya ne aage ki kahani sunayi.

Raja Bhagadatta ko harane ke baad, Arjuna ne unhe respect diya. Tabhi Shakuni ke do brave bhai, Vrishaka aur Achala, Arjuna se ladne aa gaye. Dono ne aage aur peeche se Arjuna par teer chalaye.

Arjuna ne Vrishaka ka rath tod diya, par dono bhai ek hi rath par baith kar ladte rahe. Aakhir mein, Arjuna ne ek hi tez teer se dono ko hara diya.

Apne bhaiyon ko girte dekh kar Shakuni bahut gussa ho gaya. Usne Arjuna aur Krishna ko confuse karne ke liye apna magic shuru kar diya!

Achanak, maidan mein har taraf se weapons aur sher, bhalu, bhediye jaise jaanwar Arjuna ki taraf daudte dikhe. Par Arjuna bilkul nahi dare aur apne teeron se sabko rok diya.

Phir Shakuni ne Arjuna ke rath ke chaaron taraf ghanghor andhera kar diya. Tab Arjuna ne *Jyotishka* weapon chalaya aur har taraf roshni kar di! Uske baad Shakuni ne paani ki badi-badi lehrein paida kin, toh Arjuna ne *Aditya* (suraj) weapon se saara paani sukha diya.

Apne saare magic tricks fail hote dekh kar Shakuni darr gaya aur apne tez ghodon par bhaag gaya!

Phir Arjuna ne Kaurava sena par aisa hamla kiya ki poori army do hisson mein bat gayi—aadhe log Guru Drona ki taraf bhaage aur aadhe Duryodhana ki taraf. Chaaron taraf dhool ud gayi, aur maidan mein sirf Arjuna ke dhanush Gandiva ki aawaz goonj rahi thi! """, 29: """ Raja Dhritarashtra ne poocha, "Sanjaya, jab hamari army peeche hat gayi thi, toh sabne phir se himmat kaise jutayi?"

Sanjaya ne aage ki kahani sunayi.

Mushkil waqt mein bhi, kai brave Kaurava warriors bina dare Guru Drona ke saath khade rahe. Unhone Bhima, Satyaki aur Dhrishtadyumna ki ek chhoti si galti ka fayda uthaya aur Pandava sena par hamla kar diya!

Ab poori ladai Guru Drona ke aas-paas ghoom rahi thi. Ek team chilla rahi thi, "Drona ko roko!" aur doosri team chilla rahi thi, "Drona ko bachao!" Tabhi Dhrishtadyumna khud aage aaye aur unhone Drona ko rok liya. Dono ke beech bahut shandar ladai hui.

Isi beech, Pandavon ki taraf se Raja Nila aag ki tarah Kaurava soldiers ko peeche dhakel rahe the.

Yeh dekh kar Guru Drona ke bete, Ashwatthama, muskuraye aur unhone Nila se kaha, "Nila, in aam soldiers ko kyun pareshan kar rahe ho? Aao, mujhse one-on-one lado!"

Nila ne Ashwatthama par teer chalaye. Par Ashwatthama ne badi tezi se Nila ka dhanush, flag aur umbrella kaat diya. Nila talwar aur dhal lekar rath se koode, par Ashwatthama ne unhe hara diya.

Raja Nila ke girte hi Pandava sena udaas aur pareshan ho gayi. Sab sochne lage, "Arjuna toh maidan ke doosre hisse mein busy hain, ab hamari madad kaun karega?" """, 30: """ Sanjaya ne aage ki kahani sunayi.

Apni sena ko mushkil mein dekh kar Bhima ko bahut gussa aaya. Woh akele hi Drona, Karna, Ashwatthama aur Duryodhana se bhid gaye! Yeh dekh kar Yudhishthira ne Nakula, Sahadeva aur Satyaki ko bhi Bhima ki madad ke liye bhej diya.

Sabhi Pandava warriors milkar Guru Drona ke rath ki taraf badhe. Maidan mein itni dhool ud gayi ki kisi ko kuch saaf nahi dikh raha tha. Har taraf rath, ghode aur haathi aapas mein takra rahe the.

Theek usi waqt, Samsaptakas ko hara kar Arjuna wapas laut aaye! Unke rath par laga Hanuman ji wala jhanda suraj ki tarah chamak raha tha.

Arjuna ne aate hi Kaurava sena ko peeche dhakelna shuru kar diya. Par itni badi ladai mein bhi Arjuna ne apne achhe rules nahi bhoole—unhone kabhi kisi gire hue ya bhaagte hue soldier par hamla nahi kiya.

Kaurava soldiers darr kar Karna ko bulane lage. Karna turant aage aaya aur sabko himmat dete hue bola, "Daro mat!" Usne Arjuna par apna aag wala *Agneya* weapon chalaya, par Arjuna ne use rok diya.

Phir Bhima, Dhrishtadyumna aur Satyaki ne milkar Karna par itna tez hamla kiya ki Duryodhana, Drona aur Jayadratha ko daud kar Karna ko bachana pada!

Shaam ko jab suraj doob gaya, toh dono thaki hui armies ne ladai rok di aur dhire-dhire apne tents mein wapas laut gayin. """
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
            1: """ Sanjaya ne aage ki kahani sunayi.

Us raat Kaurava sena bahut udaas hokar apne tents mein lauti. Har taraf log Arjuna ki bahaduri aur Krishna ke saath unki dosti ki tareef kar rahe the.

Agli subah, Duryodhana ne gusse mein sabke saamne Guru Drona se kaha, "Gurudev, kal Yudhishthira aapke bilkul paas the, phir bhi aapne unhe nahi pakda. Kya aapne apna vaada tod diya?"

Drona ko yeh baat bahut buri lagi. Unhone kaha, "Mujh par shak mat karo, Duryodhana. Jahan Arjuna aur Krishna saath hon, wahan kisi ki nahi chalti. Par aaj main ek aisa gol Chakravyuha banaunga jise devta bhi nahi tod payenge, aur ek bade Pandava hero ko haraunga. Bas kisi tarah Arjuna ko wahan se door rakho!"

Usi waqt Samsaptakas ne phir se Arjuna ko challenge kiya aur unhe maidan ke south side mein le gaye.

Doosri taraf, Guru Drona ne apna woh mazboot Chakravyuha bana liya. Tab Raja Yudhishthira ke kehne par, young Abhimanyu badi himmat ke saath us gol ghere ko tod kar andar ghus gaya!

Abhimanyu ne akele hi hazaaron warriors se bahaduri se ladai ki. Par aakhir mein, Kaurava sena ke chhe bade warriors ne ek saath milkar use gher liya, aur Duhsasana ke bete se ladte hue Abhimanyu ne apni jaan de di.

Yeh sunkar Raja Dhritarashtra ka dil bhar aaya. Unhone dukh se kaha, "Sanjaya, itne bade-bade warriors ne milkar ek chhote ladke par hamla kaise kiya? Mujhe poori kahani batao ki us bahadur bachhe ne hamari army ka saamna kaise kiya."

Tab Sanjaya ne Abhimanyu ki bahaduri ki poori kahani sunana shuru kiya. """, 2: """ Sanjaya ne Abhimanyu ki kahani sunane se pehle uski aur Pandavon ki tareef ki.

Unhone kaha, "Raja ji, paanchon Pandavas aur Krishna ko koi nahi hara sakta. Yudhishthira hamesha sach bolte hain, Bhima sabse taqatwar hain, Arjuna apna har vaada poora karte hain, Nakula vinamra aur brave hain, aur Sahadeva bahut samajhdar hain. Aur young Abhimanyu mein toh in sabhi ke saath Krishna ke bhi saare achhe gun maujood the!"

Raja Dhritarashtra ne kaha, "Sanjaya, mujhe poori kahani sunao ki us bahadur bachhe ne ladai kaise ki."

Sanjaya ne kaha, "Apne dil ko sambhaliye, Raja ji. Main aapko batata hoon."

Guru Drona ne ek bahut bada Chakravyuha banaya tha. Uske gate par dus hazaar young princes khade the, jo sab laal kapde aur sone ki mala pehne hue the. Un sabke aage Duryodhana ka beta, Lakshmana, khada tha. Sabne ek saath milkar Abhimanyu ka saamna karne ki kasam khayi thi.

Chakravyuha ke beech mein Raja Duryodhana apne bhaiyon, Karna aur Kripa ke saath khade the. Sabse aage Guru Drona ugate hue suraj ki tarah chamak rahe the. Wahan Raja Jayadratha bhi ek pahad ki tarah mazbooti se khade the, aur unke paas Ashwatthama, Shakuni aur Salya jaise warriors maujood the.

Phir dono teams ke beech bina kisi darr ke ek bahut badi ladai shuru ho gayi! """, 3: """ Sanjaya ne aage ki kahani sunayi.

Bhima, Satyaki, Dhrishtadyumna, Nakula, Sahadeva aur baaki sabhi Pandava warriors Guru Drona ke Chakravyuha ko todne ke liye aage badhe. Lekin Drona ne teeron ki itni tez baarish ki ki koi bhi andar nahi ja saka, jaise samundar ki lehrein kisi mazboot pahad se takra kar wapas laut aati hain.

Raja Yudhishthira chinta mein pad gaye. Unhe pata tha ki is duniya mein sirf chaar log hi Chakravyuha todna jaante hain—Krishna, Arjuna, Pradyumna, aur young Abhimanyu. Abhi wahan sirf Abhimanyu hi maujood tha.

Yudhishthira ne Abhimanyu se kaha, "Beta, agar hum yeh ghera nahi tod paaye, toh Arjuna wapas aakar hamein kahenge ki humne koshish nahi ki. Yahan sirf tum hi ise tod sakte ho. Please hamari madad karo."

Abhimanyu ne sachai se jawab diya, "Main aap sabki jeet ke liye andar zaroor jaunga. Pitaji ne mujhe Chakravyuha mein ghusna sikhaya hai. Par agar andar koi khatra aaya, toh mujhe bahar nikalne ka rasta nahi pata."

Yudhishthira aur Bhima ne turant bharosa dilaya, "Tum bas ek baar andar jaane ka rasta bana do! Hum sab—Bhima, Dhrishtadyumna, Satyaki aur baaki sabhi—tumhare peeche-peeche andar aayenge aur tumhari raksha karenge."

Abhimanyu ke chehre par himmat aur chamak aa gayi. Usne kaha, "Aaj main aisi bahaduri dikhaunga jisse mere pitaji Arjuna, maa Subhadra aur mama Krishna ko mujh par garv hoga!"

Yudhishthira ne Abhimanyu ko pyaar se aashirwad diya. Phir Abhimanyu ne apne rath chalane wale Sumitra se kaha, "Sumitra, jaldi ghode daudao aur rath ko Guru Drona ki sena ki taraf le chalo!" """, 4: """ Sanjaya ne aage ki kahani sunayi.

Jab Abhimanyu ne apne rath chalane wale Sumitra se kaha, "Chalo, aage badho!", toh Sumitra thoda ghabra gaya. Usne kaha, "Beta, Pandavon ne tum par bahut badi zimmedari daal di hai. Guru Drona bahut experienced hain, aur tumne abhi tak aisi badi ladai nahi dekhi hai. Pehle soch lo!"

Abhimanyu has pada aur bola, "Daro mat! Mere liye yeh army kuch bhi nahi hai. Main toh kisi se bhi lad sakta hoon. Tum bas jaldi se rath ko Drona ki sena ki taraf le chalo!"

Abhimanyu ki baat maankar Sumitra ne tez ghodon ko dauda diya. Chamakte hue golden armour mein, young Abhimanyu aise aage badha jaise ek chhota sher haathiyon ke jhund ke saamne ja raha ho!

Guru Drona ki aankhon ke saamne hi Abhimanyu ne Chakravyuha ka mazboot ghera tod diya aur andar ghus gaya!

Jaise hi woh andar pahuncha, hazaaron Kaurava soldiers, haathi, ghode aur rath dhol bajate aur chillate hue us par toot pade. Unhone Abhimanyu ko chaaron taraf se gher liya.

Lekin Abhimanyu bilkul nahi dara. Uske haath bijli ki tezi se chal rahe the. Usne itne tez aur accurate teer chalaye ki dushmanon ke rath toot gaye, aur haathi-ghode idhar-udhar bhaagne lage.

Ek akela ladka poori badi sena par bhaari pad raha tha! Yeh dekh kar Kaurava soldiers aur Duryodhana ke bhaiyon ke hosh ud gaye. Unka gala sookh gaya, paseena chhootne laga, aur woh apni jaan bachane ke liye maidan chhod kar bhaagne lage! """, 5: """ Sanjaya ne aage ki kahani sunayi.

Apni army ko bhaagte dekh kar Duryodhana ko bahut gussa aaya, aur woh khud Abhimanyu se ladne aage badha. Yeh dekh kar Guru Drona ne sabhi Kaurava warriors se kaha, "Raja ko bachao! Abhimanyu bahut tez lad raha hai!"

Turant hi Drona, Karna, Kripa, Ashwatthama, Salya, Shakuni aur kai bade warriors Duryodhana ko bachane daude. Un sabne milkar Abhimanyu par teeron ki baarish kar di aur Duryodhana ko bacha liya.

Par young Abhimanyu bilkul nahi dara. Woh akela hi samundar ki lehron ko rokne wale kinare ki tarah sabke saamne khada raha. Sabne ek saath us par teer chalaye, par Abhimanyu rath par nachte hue sabke teeron ko hawa mein hi kaat-ta raha aur har kisi ko jawab deta raha!

Sabse pehle Asmaka ke rajkumar ne Abhimanyu ko roka, par Abhimanyu ne muskurate hue use hara diya. Phir Karna, Drona, Ashwatthama aur Duryodhana sabne ek saath Abhimanyu par hamla kiya.

Abhimanyu ne ek bahut tez teer Karna par chalaya, jo uske armour ko tod kar paar ho gaya! Dard se Karna bhookamp mein hilte pahad ki tarah kaampne laga.

Iske baad Abhimanyu ne Raja Salya par itne teer chalaye ki Salya apne rath par hi baith kar behosh ho gaya!

Guru Drona ke saamne hi Salya ko behosh dekh kar Kaurava sena phir se darr gayi aur sheron se bhaagte hiranon ki tarah idhar-udhar bhaagne lagi. Har koi young Abhimanyu ki himmat aur skill dekh kar uski tareef karne laga! """, 6: """ Raja Dhritarashtra ne poocha, "Sanjaya, phir hamari army mein se Abhimanyu ko kisne roka?"

Sanjaya ne aage ki kahani sunayi.

Raja Salya ko behosh dekh kar unka chhota bhai gusse mein Abhimanyu se ladne aaya. Lekin Abhimanyu itni tezi se lad raha tha ki kisi ko woh saaf dikh bhi nahi raha tha! Usne palak jhapakte hi Salya ke bhai ka poora rath tod diya aur use hara diya. Yeh dekh kar sabhi log khushi se chilla uthe, "Shabash! Shabash!"

Iske baad Salya ke saare loyal soldiers—ghodon, haathiyon aur rathon par—apna naam chillate hue Abhimanyu par toot pade. Woh bole, "Aaj tum humse bach kar nahi ja sakte!"

Par young Abhimanyu bas muskuraya. Usne wahi special skills dikhayin jo usne Krishna aur Arjuna se seekhi thin.

Shuruat mein woh shanti se lada, par phir uski speed badhti gayi. Uska gol muda hua dhanush aise chamak raha tha jaise aasman mein suraj! Kisi ko pata hi nahi chal raha tha ki woh kab teer uthata hai aur kab chalata hai.

Guru Drona ke saamne hi Abhimanyu ne Kaurava rathon par itne teer barsaye ki unki army ko phir se peeche hatna pada! """, 7: """ Raja Dhritarashtra ne kaha, "Sanjaya, mujhe hairani bhi ho rahi hai aur sharm bhi aa rahi hai ki ek chhote ladke ne hamari poori army ko rok diya. Mujhe aage ki poori baat batao."

Sanjaya ne aage ki kahani sunayi.

Abhimanyu apne rath par aag ke ek gole ki tarah tez ghoom raha tha. Usne Guru Drona, Karna, Kripa, Salya, Ashwatthama aur Duryodhana sab par teer chalaye. Woh itni tezi se lad raha tha ki har jagah wahi dikhai de raha tha!

Abhimanyu ki skill dekh kar Guru Drona ki aankhein khushi se chamak uthin. Unhone Kripa se kaha, "Dekho, Abhimanyu kitna shandar lad raha hai! Iske jaisa koi aur dhanush chalane wala nahi hai. Agar yeh chahe, toh hamari poori army ko hara sakta hai."

Par Guru Drona ke muh se Abhimanyu ki tareef sunkar Duryodhana ko bahut gussa aaya! Usne Karna, Duhsasana aur baaki warriors se kaha, "Guru Drona jaan-boojh kar is ladke ko bacha rahe hain kyunki yeh unke favourite student Arjuna ka beta hai. Ab hum sabko khud aage badh kar ise rokna hoga!"

Yeh sunkar Duhsasana bade ghamand se aage aaya. Usne Duryodhana se kaha, "Chinta mat karo, bhai! Aaj main sabke saamne Abhimanyu ko hara dunga. Uske girte hi Pandavon ki saari himmat toot jayegi!"

Garajte hue Duhsasana Abhimanyu ki taraf dauda aur teeron ki baarish kar di. Par brave Abhimanyu ne bhi turant 26 tez teer chala kar uska swagat kiya.

Dono apne rathon ko gol-gol ghumate hue—ek left aur ek right—ladne lage, aur chaaron taraf dhol-nagaadon ka shor goonj utha! """, 8: """ Sanjaya ne aage ki kahani sunayi.

Abhimanyu ne Duhsasana ki taraf dekha aur muskurate hue kaha, "Achha hua jo tum mere saamne aa gaye! Tumne bhare darbar mein Yudhishthira aur Bhima ka mazak udaya tha, aur dice game mein dhokha dekar hamara rajya chheena tha. Aaj tumhe apni galat baaton ka nateeja milega!"

Itna keh kar Abhimanyu ne aag jaise tez teer Duhsasana par chalaye. Teeron ki chot se Duhsasana behosh hokar apne rath par gir pada! Uska rath chalane wala jaldi se use maidan se door le gaya.

Duhsasana ko haarte dekh kar Pandavas aur unke allies khushi se jhoom uthe. Sabne dhol bajaye aur Abhimanyu ki madad ke liye aage badhe.

Ghabra kar Duryodhana ne Karna se kaha, "Dekho Karna, Duhsasana haar gaya aur Pandavas andar aane ki koshish kar rahe hain. Ab tum Abhimanyu ko roko!"

Karna turant aage aaya aur usne Abhimanyu par saikdon tez teer chalaye. Lekin brave Abhimanyu ko bilkul darr nahi laga. Usne muskurate hue Karna ka umbrella, flag, ghode aur dhanush sab kaat diya!

Karna ko mushkil mein dekh kar uska chhota bhai use bachane dauda. Doosri taraf, poori Pandava sena young Abhimanyu ki bahaduri dekh kar zordaar taaliyan aur dhol baja rahi thi! """, 9: """ Sanjaya ne aage ki kahani sunayi.

Karna ka chhota bhai zor se garajte hue Karna aur Abhimanyu ke beech aa gaya. Usne Abhimanyu par dus teer chalaye, jisse Kaurava soldiers thodi der ke liye khush ho gaye.

Lekin young Abhimanyu ne muskurate hue ek hi tez teer se Karna ke bhai ko hara diya! Apne bhai ko girte dekh kar Karna ko bahut dukh hua. Tab Abhimanyu ne Karna par itne teer chalaye ki Karna ko apne tez ghodon par baith kar maidan se peeche hatna pada!

Karna ke jaate hi Kaurava sena ka ghera toot gaya. Abhimanyu ne apna shankh bajaya aur sookhi ghaas mein aag ki tarah Kaurava army ke beech ghus gaya. Usne dushmanon ke rath tod diye aur haathi-ghodon ko bhaga diya.

Abhimanyu ki taqat dekh kar lagbhag saare Kaurava soldiers darr kar bhaag gaye. Sirf Sindhu ke Raja Jayadratha apni jagah par khade rahe.

Maidan mein itni dhool ud gayi ki Abhimanyu kisi ko dikh hi nahi raha tha. Lekin thodi hi der mein woh us bheed se bahar nikla—dopahar ke suraj ki tarah chamakta hua! """, 10: """ Raja Dhritarashtra ne poocha, "Sanjaya, jab young Abhimanyu hamari sena ke andar gaya, toh kya uske peeche koi Pandava warrior aaya?"

Sanjaya ne aage ki kahani sunayi.

Haan, Yudhishthira, Bhima, Nakula, Sahadeva, Satyaki aur Dhrishtadyumna sabhi Abhimanyu ke banaye hue raste se uske peeche daude. Unhe aate dekh kar Kaurava soldiers peeche hatne lage.

Lekin tabhi aapke damaad, Sindhu ke Raja Jayadratha, aage aa gaye. Unhone akele hi poori Pandava sena ko gate par rok diya!

Dhritarashtra hairan hokar bole, "Jayadratha ne akele sabhi Pandavon ko kaise roka? Uske paas kaun si shakti thi?"

Sanjaya ne bataya, "Bahut pehle, jab Bhima ne Jayadratha ko haraya tha, toh use bahut sharmindagi hui. Isliye usne Bhagwan Shiva ko khush karne ke liye bahut kathin tapasya ki.

Bhagwan Shiva uske sapne mein aaye aur ek wish maangne ko kaha. Jayadratha ne maanga ki woh akele hi sabhi Pandavon ko yudh mein rok sake. Tab Bhagwan Shiva ne use vardan diya—'Arjuna ko chhod kar, tum baaki chaaron Pandavon ko ek din ke liye rok sakoge!'

Usi vardan ki wajah se, Jayadratha ne akele hi poori Pandava sena ko bahar rok diya, aur woh Abhimanyu ke paas nahi pahunch sake. Jayadratha ko gate sambhalte dekh kar baaki Kaurava soldiers bhi himmat ke saath ladne laut aaye!" """,
            11: """ Sanjaya ne aage ki kahani sunayi.

Raja Jayadratha apne shandar rath par baith kar Pandavon ke saamne khade the. Unke rath mein tez daudne wale ghode jude the, aur unke flag par chandi ka suar bana tha. Safed chhatri ke neeche woh chand ki tarah chamak rahe the.

Jayadratha ne teeron ki baarish karke Chakravyuha ke us toote hue raste ko phir se band kar diya, jise Abhimanyu ne khola tha.

Unhone Satyaki, Bhima, Dhrishtadyumna, Drupada, Shikhandi, Draupadi ke beton aur Raja Yudhishthira sab par teer chalaye. Tab Yudhishthira ne muskurate hue Jayadratha ka dhanush kaat diya. Bhima ne bhi unka naya dhanush, flag aur umbrella gira diya.

Lekin Jayadratha bahut tez the! Unhone palak jhapakte hi ek aur dhanush uthaya aur Bhima ka dhanush, flag aur ghode sab tod diye! Bhima ko ek sher ki tarah kood kar Satyaki ke rath par chadhna pada.

Jayadratha ko akele hi sabhi Pandavon ko rokte dekh kar Kaurava sena khushi se chilla uthi, "Shabash! Shabash!"

Bhagwan Shiva ke vardan ki wajah se, Jayadratha ne rasta poori tarah block kar diya tha. Koi bhi Pandava warrior unhe paar karke Abhimanyu ki madad karne andar nahi ja saka! """, 12: """ Sanjaya ne aage ki kahani sunayi.

Bahar Raja Jayadratha ne Pandavon ko rok rakha tha, aur Chakravyuha ke andar young Abhimanyu akela lad raha tha. Woh samundar mein badi lehrein uthane wale kisi vishal jeev ki tarah poore maidan mein halchal macha raha tha!

Kaurava sena ke sabhi bade warriors ne apne rathon ke saath Abhimanyu ko gher liya. Par Abhimanyu bahut tez tha. Usne Vrishasena ka dhanush tod diya aur uske ghodon ko bhaga diya. Is mauke ka fayda utha kar Abhimanyu ka rath chalane wala bheed se nikal kar khuli jagah mein aa gaya.

Tabhi Vasatiya naam ka ek brave warrior Abhimanyu par toot pada. Usne Abhimanyu par 60 teer chalaye aur kaha, "Jab tak main hoon, tum yahan se bach kar nahi ja sakte!"

Par Abhimanyu ne ek hi tez teer se Vasatiya ka loha ka armour tod diya, aur Vasatiya zameen par gir pada.

Yeh dekh kar baaki saare Kaurava warriors gusse mein aa gaye aur unhone phir se Abhimanyu ko gher liya.

Lekin Abhimanyu itni tezi se ghoom-ghoom kar lad raha tha ki uska chehra tak dikhai nahi de raha tha! Bas uska chamakta hua golden armour, dhanush aur teer hi dikh rahe the. Woh dushmanon ke beech suraj ki tarah itna tez chamak raha tha ki koi uski taraf aankh utha kar dekh bhi nahi pa raha tha! """, 13: """ Sanjaya ne aage ki kahani sunayi.

Abhimanyu ek sher ki tarah Kaurava sena ke beech ghoom raha tha. Kai warriors ek doosre se aage nikalne ki hod mein chillate hue uski taraf daude, "Pehle main jaunga! Pehle main!"

Tab Raja Salya ke bete, Rukmaratha, ne sabko himmat dete hue kaha, "Daro mat! Mere hote hue Abhimanyu kya kar sakta hai? Main use abhi zinda pakad kar launga!"

Rukmaratha ne Abhimanyu par teer chalaye. Lekin tez Abhimanyu ne turant uska dhanush kaat diya aur use hara diya!

Apne dost Rukmaratha ko haarte dekh kar sau (100) young rajkumaron ne ek saath Abhimanyu ko gher liya. Unhone itne teer chalaye ki Abhimanyu aur uska rath teeron ke neeche bilkul chhup gaye! Yeh dekh kar Duryodhana bahut khush hua.

Par Abhimanyu haar manne wala nahi tha. Usne turant apna magical **Gandharva weapon** chalaya, jo uske pitaji Arjuna ne use sikhaya tha!

Achanak, aisa laga jaise Abhimanyu ek saath har jagah hai—kabhi ek, kabhi sau, aur kabhi hazaar! Aag ke pahiye ki tarah ghoomte hue, Abhimanyu ne un sabhi sau rajkumaron ko palak jhapakte hi hara diya.

Yeh dekh kar Duryodhana darr gaya. Woh khud gusse mein Abhimanyu se ladne aage aaya, par Abhimanyu ke tez teeron ne Raja Duryodhana ko bhi peeche hatne par majboor kar diya! """, 14: """ Raja Dhritarashtra ne kaha, "Sanjaya, Abhimanyu ki yeh kahani sunkar mujhe bahut hairani ho rahi hai. Par jinke paas sachai aur achhai hoti hai, woh aise hi bahadur hote hain. Batao, Duryodhana ke peeche hatne ke baad kya hua?"

Sanjaya ne aage ki kahani sunayi.

Abhimanyu ki taqat dekh kar Kaurava soldiers darr gaye aur maidan chhod kar bhaagne lage. Unhe bhaagte dekh kar Drona, Ashwatthama, Kripa, Karna aur Duryodhana phir se Abhimanyu ko rokne aaye. Par young Abhimanyu ne akela hi lagbhag sabko peeche dhakel diya!

Bas ek hi young prince wahan ruka—Duryodhana ka beta, Lakshmana. Apne bete ki chinta mein Duryodhana aur baaki warriors bhi wapas laut aaye. Sabne milkar Abhimanyu par teeron ki baarish kar di, par Abhimanyu ne sabko rok diya.

Phir Abhimanyu aur Lakshmana ke beech muqabla hua. Lakshmana ne Abhimanyu par tez teer chalaye. Gusse mein aakar Abhimanyu ne ek aisa teer chalaya ki Lakshmana sabke saamne hi maidan mein gir pada!

Apne bete ko girte dekh kar Duryodhana ko bahut dukh aur gussa aaya. Usne chilla kar kaha, "Ise abhi roko!"

Turant hi chhe bade warriors—Drona, Kripa, Karna, Ashwatthama, Vrihadvala aur Kritavarman—ne milkar Abhimanyu ko gher liya. Lekin fearless Abhimanyu unhe bhi peeche chhod kar Jayadratha ki sena ki taraf badh gaya!

Tab Kalinga, Nishada aur Kratha ke bete ne haathiyon ki fauj lekar Abhimanyu ka rasta roka. Par Abhimanyu ne un haathiyon ko aise bhaga diya jaise tez hawa badalon ko uda deti hai, aur Kratha ke bete ko bhi hara diya. Yeh dekh kar baaki warriors phir se peeche hat gaye! """, 15: """ Raja Dhritarashtra ne poocha, "Sanjaya, jab young Abhimanyu hamari sena ke andar lad raha tha, tab kis-kis ne use ghera?"

Sanjaya ne aage ki kahani sunayi.

Chakravyuha ke andar chhe bade Kaurava warriors—Drona, Kripa, Karna, Ashwatthama, Kritavarman aur Kosala ke Raja Vrihadvala—ne milkar Abhimanyu ko gher liya. Baaki soldiers bahar Jayadratha ki madad karne chale gaye.

Un chhe bade warriors ne ek saath Abhimanyu par teeron ki baarish kar di. Lekin brave Abhimanyu bilkul nahi dara. Usne akele hi sabko jawab diya!

Usne Drona, Karna, Kritavarman aur Ashwatthama par tez teer chalaye, aur Kripa ke rath ke ghode gira diye. Ashwatthama ne Abhimanyu par saath (60) teer chalaye, par Abhimanyu ek pahad ki tarah apni jagah par data raha aur usne Ashwatthama ko bhi peeche hataya.

Phir Raja Vrihadvala ne Abhimanyu par teer chalaya. Abhimanyu ne turant uska dhanush, flag aur rath tod diya! Jab Vrihadvala talwar lekar aage badha, toh Abhimanyu ne ek strong teer chala kar use bhi hara diya.

Raja Vrihadvala ko girte dekh kar dus hazaar raja darr gaye aur maidan chhod kar bhaag gaye! Young Abhimanyu akela hi dushmanon ke beech suraj ki tarah chamak raha tha. """, 16: """ Sanjaya ne aage ki kahani sunayi.

Abhimanyu ne phir se Karna par tez teer chalaye aur uske saath aaye kai warriors ko hara diya. Usne Salya ka dhanush bhi tod diya, jisse Salya ko doosra rath lena pada.

Yeh dekh kar Shakuni ne Duryodhana se kaha, "Agar hum sabne milkar ise nahi roka, toh yeh akela hi hum sabko hara dega!"

Karna bhi Guru Drona ke paas gaya aur bola, "Gurudev, Abhimanyu ke teer bahut tez hain. Please batayein ki hum ise kaise rokein?"

Guru Drona ne muskurate hue kaha, "Dekho toh sahi, yeh ladka kitni tezi se lad raha hai! Iska armour bahut mazboot hai, aur jab tak iske haath mein dhanush hai, koi ise hara nahi sakta. Ise rokne ke liye pehle iska dhanush aur rath todna hoga."

Yeh sunkar Karna ne turant teer chala kar Abhimanyu ka dhanush kaat diya! Kritavarman aur Kripa ne uske rath ke ghode aur saarthi ko rok diya. Phir chhe bade warriors ne milkar us akele, bina rath wale ladke par teeron ki baarish kar di!

Par brave Abhimanyu ne phir bhi haar nahi maani. Usne apni talwar aur dhal uthayi aur ek baaz ki tarah hawa mein oonchi chhalang laga di!

Lekin tabhi Guru Drona ne uski talwar tod di, aur Karna ne uski dhal kaat di.

Ab Abhimanyu ke paas koi weapon nahi bacha tha. Phir bhi woh zameen par utara, usne apne haathon mein ek toote hue rath ka bhaari pahiya uthaya—bilkul Bhagwan Krishna ke Sudarshana Chakra ki tarah—aur zor se garajte hue Guru Drona ki taraf daud pada! """, 17: """ Sanjaya ne aage ki kahani sunayi.

Rath ka pahiya haath mein uthaye Abhimanyu bilkul Bhagwan Krishna ki tarah chamak raha tha. Yeh dekh kar Kaurava raja darr gaye aur unhone teer chala kar us pahiye ke tukde-tukde kar diye!

Par Abhimanyu ne phir bhi himmat nahi haari. Usne ek bhaari gada uthayi aur Ashwatthama ki taraf dauda. Ashwatthama darr kar apne rath se kood kar peeche hat gaya.

Teeron se ghira hua Abhimanyu aise lag raha tha jaise koi saahi (porcupine) ho, par woh rukne ka naam nahi le raha tha. Usne Kalikeya aur uske soldiers ko haraya, aur phir Duhsasana ke bete ka rath bhi tod diya!

Tab Duhsasana ka beta bhi apni gada lekar saamne aaya. Dono ke beech gada ki zabardast ladai hui, aur ek hi saath dono zameen par gir pade.

Duhsasana ka beta jaldi uth gaya. Jab thaka hua Abhimanyu abhi uthne ki koshish hi kar raha tha, tabhi usne Abhimanyu par vaar kar diya. Din bhar akele itne bade warriors se ladne ke baad, brave Abhimanyu shaam ke dhalte suraj ki tarah zameen par gir kar shant ho gaya.

Kaurava sena khushi se naachne lagi, par Pandava heroes ki aankhon mein aansu aa gaye. Aasman mein udne wale pakshiyon ne bhi dukh se kaha, "Chhe bade warriors ne milkar ek akele ladke par hamla kiya—yeh bilkul galat tha!"

Abhimanyu ke girne se Pandava soldiers ka dil toot gaya aur woh peeche hatne lage. Tab Raja Yudhishthira ne sabko pyaar se sambhala aur kaha, "Himmat mat haaro! Bahadur Abhimanyu bina peeche hate lada aur swarg chala gaya. Usne apna farz poori sachai se nibhaya. Ab hamein bhi himmat rakhni hogi." """, 18: """ Sanjaya ne aage ki kahani sunayi.

Shaam hone par, thake hue aur chotil Kaurava soldiers dhire-dhire apne camp ki taraf lautne lage. Bhale hi unhone Abhimanyu ko gira diya tha, par unhe khud bhi bahut bada nuksan uthana pada tha. Sabhi shant aur gumsum the.

Din aur raat ke beech ka waqt aa gaya. Suraj pashchim ki pahadiyon ke peeche doobne laga. Uski halki laal roshni ne aasman aur dharti ko ek hi rang mein rang diya, aur talwaron-dhalon ki chamak bhi dhire-dhire gayab ho gayi.

Jo maidan din bhar shor se goonj raha tha, ab wahan gehri shanti chha gayi thi. Toote hue rath, jhande, aur thake-haare haathi-ghode maidan mein idhar-udhar bikhre pade the. Door kahin siyar (jackals) bolne ki aawaz aa rahi thi.

Jaate-jaate sabhi soldiers ne ek aakhri baar peeche mud kar dekha. Bahadur Abhimanyu zameen par bilkul shant leta tha—bilkul us tez aag ki tarah jo apni poori roshni dene ke baad shant ho gayi ho. Sabhi bhaari mann se wapas apne tents mein laut gaye. """, 19: """ Sanjaya ne aage ki kahani sunayi.

Abhimanyu ke jaane ke baad, sabhi Pandava warriors apne rath se utar aaye. Unhone apna armour aur dhanush neeche rakha aur chupchap Raja Yudhishthira ke paas baith gaye. Sabke dil mein ek hi baat thi—pyaare Abhimanyu ka dukh.

Yudhishthira ki aankhein nam thin. Unhone dukh se kaha, "Abhimanyu ne hamari madad ke liye Guru Drona ka ghera toda. Usne bade-bade warriors aur Duhsasana ko bhi peeche hataya, par aakhir mein akela ladte hue hamara bachha chala gaya."

Yudhishthira khud ko dosh de rahe the. Woh bole, "Main ab Arjuna, Subhadra aur Krishna ko kya jawab dunga? Unse aankhein kaise milaunga? Jeet ki chah mein maine ek chhote bachhe ko itne bade khatre mein bhej diya—jiski umar abhi khelne aur khush rehne ki thi. Aur usne bhi bina kuch kahe hamari baat maan li."

Unhone aage kaha, "Arjuna itna brave aur dayalu hai ki woh maafi maangne wale dushmanon ko bhi maaf kar deta hai. Lekin aaj hum uske hi bete ko nahi bacha paaye. Jab Arjuna ko yeh baat pata chalegi, toh woh Kauravon ko bilkul nahi chhodenge. Ab toh mujhe na jeet ki khushi hai, aur na hi rajya ki!" """, 20: """ Sanjaya ne aage ki kahani sunayi.

Jab Raja Yudhishthira Abhimanyu ke liye bahut udaas the, tab mahan Rishi Vyasa unse milne aaye. Yudhishthira ne unhe respect diya aur apna dukh bataya ki kaise itne saare warriors ne milkar ek chhote ladke par galat tarike se hamla kiya.

Rishi Vyasa ne Yudhishthira ko pyaar se samjhaya, "Yudhishthira, tum toh bahut samajhdar ho. Abhimanyu bhale hi chhota tha, par usne ek bade hero ki tarah ladai ki aur ab swarg chala gaya hai. Duniya mein har kisi ko ek din jaana hota hai—yeh nature ka rule hai."

Tab Yudhishthira ne ek gehra sawal poocha, "Par yeh Death kya hai? Yeh kahan se aayi, aur yeh sabko kyun le jaati hai?"

Unka dukh kam karne ke liye, Rishi Vyasa ne ek purani kahani sunana shuru kiya, jo kabhi Narada Muni ne Raja Akampana ko sunayi thi. Raja Akampana bhi apne brave bete Hari ke jaane par bahut udaas the.

Narada Muni ki kahani duniya ki shuruat se shuru hui:

"Bahut pehle, jab Brahma ji ne duniya banayi, tab koi bhi cheez khatam nahi hoti thi. Dhire-dhire duniya bahut bhar gayi. Brahma ji ko samajh nahi aaya ki balance kaise banayein. Gusse aur chinta mein unke andar se ek badi aag nikli, jo sab kuch jalane lagi.

Sabhi jeev-jantuon ko khatre mein dekh kar dayalu Bhagwan Shiva wahan aaye aur Brahma ji ke aage jhuke. Tab Brahma ji ne Shiva se kaha, 'Bolo, tum kya chahte ho? Main tumhari har wish poori karunga! """,
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
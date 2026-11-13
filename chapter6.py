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
    create_image_text_layout("attached_assets/chapter6/chapter6.jpg", layout="full")


    text0 = """
    <h2>Book 6 - Bhishma Parva</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
# ==================================================
# Chapter 6.1 - Jambukhanda Nirmana Parva
# ==================================================

    with st.expander("Chapter 6.1  Jambukhanda Nirmana Parva"):

        # Section 6.1.1
        with st.expander("Section 6.1.1  Section I"):
            text1 = """ Section I – Hinglish Story

Sabse pehle Bhagwan Narayan, Maharishi Nara aur Maa Saraswati ko pranam kiya gaya.

Phir Raja Janamejaya ne poocha,

"Kurukshetra mein Kaurav, Pandav aur unke saath aaye sabhi rajaon ne yudh kaise kiya?"

Vaisampayan bole,

"Dhyan se suniye."

"Pandav apni vishaal sena ke saath Kurukshetra pahunch gaye."

"Unke saath Somak aur kai veer raja bhi the."

Sabka ek hi lakshya tha...

Yudh jeetna. """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Yudhishthir ne niyam ke anusaar hazaaron tambu lagwaye.

Poore Bharat se itni badi sena aayi thi ki gaon aur shehar lagbhag khaali ho gaye the.

Sirf bachche aur buzurg hi gharon mein bache the.

Har desh aur har jaati ke yoddha Kurukshetra mein ikattha hue.

Yudhishthir ne sabke liye khaane, paani aur aaram ka poora intezaam kiya.

Unhone har sena ke liye alag pehchaan aur gupt sanket bhi tay kiye, taaki yudh ke dauraan apne aur dushman mein farq kiya ja sake.

Udhar Duryodhan bhi apni sena ke beech khada tha.

Uske sir par safed chhatra tha aur uske aas-paas uske sabhi bhai aur hazaaron haathi the.

Jaise hi dono senaein ek-doosre ke saamne aayi, Panchal ke veeron ne zor se shankh aur nagaade bajaye.

Yeh dekhkar Shri Krishna aur Arjun bhi khush hue.

Dono ne apne divya shankh bajaye.

Unki awaaz itni shaktishaali thi ki kai yoddha darr se kaanp uthe.

Kuch logon ka darr itna badh gaya ki unse apne sharir par bhi kabu nahi raha.

Tab achanak aasman mein ajeeb ghatnayein hone lagi.

Dhool ka bada toofan uth gaya.

Sooraj bhi us dhool mein chhup gaya.

Kaale baadal chha gaye.

Aisa laga jaise khoon aur maans ki baarish ho rahi ho.

Tez hawa chalne lagi aur chhote patthar udkar har taraf girne lage.

Yeh sab dekhkar bhi dono senaein apni jagah majbooti se khadi rahi.

Dono ek-doosre ke saamne do bade samundaron ki tarah dikh rahi thi.

Yudh shuru hone se pehle dono pakshon ne kuch zaroori niyam banaye.

Unhone faisla kiya,

Barabar shakti wale yoddha aapas mein ladenge.
Jo yoddha peeche hat jaaye ya haar maan le, us par hamla nahi kiya jayega.
Jo sirf baat kar raha ho, usse baaton se hi jawab diya jayega.
Rath wala rath wale se ladega.
Haathi wala haathi wale se.
Ghode wala ghode wale se.
Paidal sainik paidal sainik se ladega.
Bina chetavani ke kisi par hamla nahi hoga.
Jo nishastr ho, ghaayal ho, bhaag raha ho ya sharan maang raha ho, us par vaar nahi kiya jayega.
Saarthi, dhol bajane wale, shankh bajane wale aur hathiyaar le jaane wale logon par bhi hamla nahi hoga.

Yeh sab niyam maan kar Kaurav aur Pandav ek-doosre ko dekhne lage.

Ab sab kuch taiyaar tha.

Kurukshetra ka Mahayudh shuru hone wala tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.2
        with st.expander("Section 6.1.2  Section II"):
            text1 = """ Section II – Hinglish Story

Vaisampayan bole,

"Jab dono senaein Kurukshetra mein ek-doosre ke saamne khadi thi, tab Maharishi Ved Vyasa wahan aaye.

Unhe bhoot, vartamaan aur bhavishya sab dikhai deta tha.

Unhone Raja Dhritarashtra ko udaas dekha.

Woh apne putron ke faislon ko yaad karke bahut dukhi the.

Vyasa ji bole,

"Rajan, samay aa chuka hai."

"Ab tumhare putra aur sabhi raja yudh mein ek-doosre se ladenge."

"Bahut se veer apni jaan gawa denge."

"Yeh sab samay ka niyam hai."

"Dukhi mat ho." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Agar tum chaho, toh main tumhe divya drishti de sakta hoon."

"Tum yeh poora yudh apni aankhon se dekh sakoge."

Dhritarashtra bole,

"Hey Maharishi, main apne hi parivaar ka vinaash dekhna nahi chahta."

"Lekin main yudh ki har baat zaroor sunna chahta hoon."

Tab Maharishi Vyasa ne Sanjay ko ek divya vardaan diya.

Woh bole,

"Sanjay ko divya drishti milti hai."

"Woh yudh ki har ghatna dekh sakega."

"Chahe din ho ya raat."

"Chahe baat khuli ho ya chhupi hui."

"Woh logon ke mann ki baat bhi jaan sakega."

"Koi bhi astra uska kuch nahi bigaad paayega."

"Thakaan bhi us par asar nahi karegi."

"Woh surakshit yudh se laut aayega."

"Ab wahi tumhe yudh ka poora varnan sunayega."

Phir Vyasa ji bole,

"Ek baat hamesha yaad rakhna."

"Jeet hamesha usi ki hoti hai jo dharm ke saath khada hota hai."

Uske baad Vyasa ji ne bahut saare ajeeb sanket bataye.

Woh bole,

"Mujhe bure shagun dikh rahe hain."

"Giddh, baaz aur kawe jhund bana kar pedon par baithe hain."

"Jaise woh kisi bade vinaash ka intezaar kar rahe hon."

"Jangli jaanwar bhi bechain hain."

"Sooraj aur Chand dono ajeeb dikh rahe hain."

"Kabhi unki roshni kam ho jaati hai."

"Kabhi aasman mein laal aur kaale baadal chha jaate hain."

"Raat ko ajeeb awaazein sunai deti hain."

"Kabhi suar aur billiyon ke ladne ki awaaz aati hai."

"Mandiron mein rakhi devtaon ki moortiyan bhi ajeeb sanket de rahi hain."

"Kabhi woh hansti hain."

"Kabhi kaanpti hain."

"Kabhi unse paseena ya khoon jaisa dikhai deta hai."

"Bina kisi ke bajaye dhol ki awaaz sunai deti hai."

"Kabhi rath apne aap hilne lagte hain."

"Pakshi bhi daraavni awaazein nikaal rahe hain."

"Subah aur shaam aasman aag jaisa laal dikhai deta hai."

"Kabhi dhool aur maans jaisi baarish bhi hoti hai."

"Taaron aur grahon ki chaal bhi badli hui lag rahi hai."

"Yeh sab ek hi baat ka sanket de rahe hain..."

"Kurukshetra mein bahut bada vinaash hone wala hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.3
        with st.expander("Section 6.1.3  Section III"):
            text1 = """ Section III – Hinglish Story

Vaisampayan bole,

"Maharishi Ved Vyasa ne Dhritarashtra se kaha,

'Mujhe bahut bure sanket dikh rahe hain.'

'Yeh sab batate hain ki Kurukshetra mein bahut bada vinaash hone wala hai.'

Vyasa ji bole,

"Gaay ajeeb bachchon ko janm de rahi hain."

"Jungle ke ped bina mausam ke phool aur phal de rahe hain." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Kai mahilaon ke ghar ajeeb roop wale bachche paida ho rahe hain."

"Jaanwar aur pakshi bhi ajeeb tarah se vyavhaar kar rahe hain."

"Kuch jaanwar do sir, chaar aankhen ya zyada pairon ke saath paida ho rahe hain."

"Woh daraavni awaazein nikaal rahe hain."

"Tez aandhiyaan chal rahi hain."

"Dharti baar-baar kaanp rahi hai."

"Sooraj, Chand aur grahon ki chaal bhi badli hui lag rahi hai."

"Rahu aur Ketu ke ajeeb yog ban rahe hain."

"Aasman mein dhoomketu dikh rahe hain."

"Yeh sab bahut bade yudh ka sanket hai."

Vyasa ji ne aage kaha,

"Gaayon ke doodh ki jagah khoon jaisa dikh raha hai."

"Hathiyaar bina istemaal ke hi chamak rahe hain."

"Jaise unhe bhi aane wale yudh ka ehsaas ho."

"Nadiyon ka paani laal dikh raha hai."

"Kuen ajeeb awaazein nikaal rahe hain."

"Aasman se toot-te taare gir rahe hain."

"Ped toot rahe hain."

"Haathi aur ghode bhi bechain hain."

"Har taraf prakriti ek hi baat keh rahi hai..."

"Bahut bada vinaash aane wala hai."

Yeh sab sunkar Dhritarashtra bole,

"Mujhe lagta hai yeh sab pehle se hi likha hua tha."

"Bahut se raja is yudh mein marenge."

"Lekin jo Kshatriya apna kartavya nibhate hue veergati paayenge, unhe swarg milega."

Phir Vyasa ji bole,

"Samay hi sab kuch banata bhi hai aur mitaata bhi hai."

"Ab bhi waqt hai."

"Apne putron ko dharm ka raasta dikhao."

"Pandavon ko unka rajya wapas de do."

"Yudh rok do."

"Kyunki apno ka vinaash kabhi achha nahi hota."

Dhritarashtra udaas hokar bole,

"Mujhe sahi aur galat ka gyaan hai."

"Lekin jab baat apne bachchon ki aati hai, mera mann kamzor pad jaata hai."

"Mere putra meri baat nahi maante."

"Main unhe rok nahi paa raha."

Phir Dhritarashtra ne poocha,

"Maharishi, mujhe yeh bhi batayiye ki jeet ke shubh sanket kya hote hain?"

Vyasa ji bole,

"Jab yagya ki agni saaf aur tej jalti hai..."

"Jab shankh aur nagaade zor se bajte hain..."

"Jab Sooraj aur Chand ki roshni saaf hoti hai..."

"Jab pakshi meethi awaaz nikaalte hain..."

"Jab sainik khush, utsaahi aur bina dare khade rehte hain..."

"Tab jeet ke achhe sanket hote hain."

"Lekin yaad rakho..."

"Jeet sirf badi sena se nahi milti."

"Kabhi-kabhi kuch hi bahadur yoddha poori sena par bhaari pad jaate hain."

"Aur sabse achhi jeet wahi hoti hai..."

"Jo bina yudh ke, shanti aur samajhdari se mil jaaye."

"Lekin agar yudh hi karna pade..."

"Toh usmein jeetne wala bhi nuksaan zaroor uthata hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.4
        with st.expander("Section 6.1.4  Section IV"):
            text1 = """ Section IV – Hinglish Story

Vaisampayan bole,

"Yeh sab kehkar Maharishi Ved Vyasa wahan se chale gaye."

Raja Dhritarashtra chup-chaap gehri soch mein doob gaye.

Woh baar-baar gehri saans bharne lage.

Thodi der baad unhone Sanjay se poocha,

"Sanjay, itne saare veer raja aur yoddha is dharti ke liye apni jaan dene ko taiyaar hain."

"Woh ek-doosre ko maarne ke liye yudh kar rahe hain."

"Mujhe samajh nahi aata..."

"Aakhir is dharti mein aisi kya baat hai, jiske liye sab kuch daav par laga diya jaata hai?" """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Mujhe yeh bhi batao ki itne saare raja kin-kin deshon aur nagaron se aaye hain."

"Tumhe Maharishi Ved Vyasa ki kripa se divya drishti mili hai."

"Isliye mujhe sab kuch vistaar se batao."

Sanjay ne haath jodkar kaha,

"Rajan, main apni samajh ke anusaar sab kuch batata hoon."

"Is sansaar mein do tarah ke jeev hote hain."

"Ek jo chalte-phirte hain."

"Aur doosre jo ek hi jagah rehte hain."

"Jo chal sakte hain, unmein bhi alag-alag prakaar ke jeev hote hain."

"Unmein insaan aur jaanwar sabse mahatvapurn maane gaye hain."

Sanjay ne aage kaha,

"Jaanwaron ki bhi do shreniyan hoti hain."

"Jungle mein rehne wale."

"Aur gharon mein rehne wale."

"Jungle ke raja hain..."

"Sher, baagh, jangli suar, bhains, haathi, bhalu aur bandar."

"Gharon mein rehne wale hain..."

"Gaay, bakri, bhed, ghoda, khacchar, gadha aur insaan."

"Yeh sab prakriti ka hissa hain."

Phir Sanjay bole,

"Ped-paudhe bhi jeevan ka ek zaroori hissa hain."

"Bade ped, jhaadiyan, bel aur ghaas..."

"Sab dharti se hi paida hote hain."

Phir Sanjay ne sabse gehri baat kahi,

"Is duniya ki har cheez dharti se hi janm leti hai."

"Aur ek din wapas isi dharti mein sama jaati hai."

"Dharti hi sabka sahara hai."

"Dharti hi sabka ghar hai."

"Jiske paas dharti hoti hai..."

"Uske paas jaise poora sansaar hota hai."

"Isi liye raja usse paane ke liye yudh karte hain."

"Kabhi-kabhi toh apne hi rishtedaron se bhi lad jaate hain."

"Dharti bahut keemti hai..."

"Lekin uske liye apnon ka khoon bahaana hamesha dukh ki baat hoti hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.5
        with st.expander("Section 6.1.5  Section V"):
            text1 = """ Section V – Hinglish Story

Dhritarashtra bole,

"Sanjay, mujhe dharti ke baare mein aur batao."

"Nadiyon, pahaadon, deshon aur is poori dharti ki rachna ka varnan karo."

Sanjay bole,

"Rajan, is poore sansaar ki har cheez paanch tatvon se bani hai."

"Yeh paanch tatv hain..."

"Aakash, Vayu, Agni, Jal aur Prithvi."

"Har tatv ki apni ek khaas pehchaan hoti hai."

"Aakash se awaaz aati hai."

"Vayu se sparsh ka ehsaas hota hai."

"Agni se roshni milti hai."

"Jal se swaad milta hai." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Aur Prithvi se sugandh milti hai."

"Prithvi sabse vishesh hai."

"Kyunki isme baaki chaaron tatvon ke gun bhi hote hain."

Sanjay ne aage kaha,

"Jab yeh paanch tatv alag-alag rehte hain, tab jeevan nahi hota."

"Lekin jab yeh ek saath milte hain..."

"Tab sabhi jeevon ka janm hota hai."

"Ek din sab kuch phir inhi tatvon mein sama jaata hai."

"Yahi prakriti ka niyam hai."

Phir Sanjay bole,

"Kuch baatein insaan ki samajh se bahar hoti hain."

"Unhe sirf tark se samajhna mumkin nahi hota."

"Unhe shraddha aur gyaan se samajhna padta hai."

Uske baad Sanjay ne dharti ka varnan shuru kiya.

Woh bole,

"Is dharti ka ek bada dweep hai jiska naam Sudarshan Dweep hai."

"Yeh gol hai, bilkul ek chakra ki tarah."

"Isme sundar nadiyan, jheelen aur bade-bade pahaad hain."

"Yahan bahut saare nagar aur samriddh desh baste hain."

"Har taraf hare-bhare ped hain."

"Un par phool aur phal lage rehte hain."

"Kheton mein anek prakaar ki faslen ugti hain."

"Yeh poora dweep namkeen samundar se ghira hua hai."

Sanjay ne phir ek rochak baat kahi.

"Jab tum Chandrama ko dekhte ho..."

"Toh uske andar jo aakriti dikhai deti hai..."

"Wahi Sudarshan Dweep ka pratibimb maana jaata hai."

"Kuch hissa Peepal ke ped jaisa dikhta hai."

"Aur kuch hissa ek bade khargosh jaisa."

"Baaki jagah paani hi paani hai."

"Abhi maine iska sirf chhota sa varnan kiya hai."

"Aage main iske baare mein aur bhi vistaar se bataunga." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.6
        with st.expander("Section 6.1.6  Section VI"):
            text1 = """ Section VI – Hinglish Story

Dhritarashtra bole,

"Sanjay, tumne Sudarshan Dweep ka chhota sa varnan kiya tha."

"Ab mujhe uske baare mein aur vistaar se batao."

Sanjay bole,

"Rajan, is dharti par chhe mahaan parvat hain."

"Inke naam hain..."

Himavat, Hemakut, Nishadh, Neel, Shvet aur Sringavat.

"Yeh sab poorab se lekar paschim tak faile hue hain."

"Inke beech bahut sundar desh aur rajya baste hain."

"Inhi bade-bade bhaagon ko Varsha kaha jaata hai." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Hum jis bhoomi par rehte hain, uska naam Bharat Varsha hai."

Uske baad Sanjay bole,

"In sabke beech ek adbhut parvat hai."

"Uska naam hai..."

Sumeru Parvat.

"Yeh sone se bana hua hai."

"Yeh itna chamakta hai jaise subah ka Sooraj."

"Iski unchai bahut zyada hai."

"Aisa lagta hai jaise yeh poore sansaar ko sambhale khada ho."

"Sumeru ke aas-paas kai pavitra bhoomiyan hain."

"Wahan devta, Gandharv, Apsarayein aur rishi-muni aakar rehte aur pooja karte hain."

"Narad ji aur doosre mahan rishi bhi wahan Bhagwan ka stuti gaan karte hain."

Sanjay ne aage kaha,

"Sumeru ke paas Kubera ka bhi divya nagar hai."

"Wahin Bhagwan Shiv Mata Parvati ke saath anand se nivaas karte hain."

"Sirf pavitra aur satya ka paalan karne wale log hi unka darshan kar sakte hain."

Phir Sanjay bole,

"Sumeru ki choti se pavitra Maa Ganga ka janm hua."

"Woh bahut tez gati se neeche girne lagi."

"Lekin dharti uska veg seh nahi sakti thi."

"Tab Bhagwan Shiv ne use apni jataon mein rok liya."

"Kai varshon baad Maa Ganga dharti par utari aur saat pavitra dhaaron mein baant gayi."

"Unmein Saraswati, Sindhu aur Ganga jaise pavitra nadiyan shamil hain."

Sanjay ne bataya,

"Uttar ki taraf kuch aise desh bhi hain jahan log bahut lambi umar jeete hain."

"Wahan ke log hamesha swasth, khush aur shaant rehte hain."

"Wahan dukh aur bimari bahut kam hoti hai."

"Har jagah prakriti ki sundarta hi sundarta hai."

Phir Sanjay bole,

"Kailash Parvat bhi isi pavitra kshetra ka hissa hai."

"Wahan Kubera aur unke sevak rehte hain."

"Wahin Raja Bhagirath ne bahut saalon tak tapasya ki thi."

"Unki tapasya se hi Maa Ganga dharti par aayi thi."

Aakhir mein Sanjay bole,

"Is dharti par alag-alag Varsha, parvat aur pavitra sthal hain."

"Har jagah alag jeev, alag prakriti aur alag sampatti hai."

"Yeh sab Bhagwan ki adbhut rachna ka hissa hain."

"Isi ka maine aaj tumhe varnan kiya hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.7
        with st.expander("Section 6.1.7  Section VII"):
            text1 = """ Section VII – Hinglish Story

Dhritarashtra bole,

"Sanjay, ab mujhe Meru Parvat ke uttar aur poorab ke pavitra deshon ke baare mein batao."

Sanjay bole,

"Meru Parvat ke uttar mein Uttar Kuru naam ka ek adbhut desh hai."

"Wahan Siddh purush rehte hain."

"Wahan ke ped hamesha phoolon aur phalon se bhare rehte hain."

"Unke phal bahut meethe hote hain."

"Kuch ped toh logon ki ichchha ke hisaab se phal dete hain."

"Kuch ped doodh aur Amrit jaisa bhojan bhi dete hain."

"Kuch ped kapde aur gehne bhi pradaan karte hain." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Poore desh ki zameen sunehri ret se dhaki hui hai."

"Kahin-kahin zameen heere aur neelam ki tarah chamakti hai."

"Wahan hamesha suhana mausam rehta hai."

"Jheelon ka paani bilkul saaf aur sheeshe ki tarah chamakta hai."

"Wahan ke log bahut sundar, swasth aur hamesha khush rehte hain."

"Bachche hamesha judwa janm lete hain."

"Ek ladka aur ek ladki."

"Dono saath-saath bade hote hain."

"Dono ek-doosre se bahut prem karte hain."

"Wahan koi bimaar nahi padta."

"Log bahut lambi umar jeete hain."

Uske baad Sanjay bole,

"Ab suno Meru ke poorab ki kahani."

"Wahan ek sundar desh hai jiska naam Bhadrasva hai."

"Wahan ek bahut bada pavitra ped hai."

"Uska naam Kalamra hai."

"Woh hamesha phoolon aur phalon se bhara rehta hai."

"Siddh aur Rishi uski pooja karte hain."

"Wahan ke log gora rang, bahut balwaan aur tejvaan hote hain."

"Wahan ki mahilaayein Chandrama ki roshni jaisi sundar hoti hain."

"Woh gaana aur nritya bahut achhi tarah jaanti hain."

"Woh Kalamra ke phalon ka ras peeti hain."

"Usse woh hamesha jawaan aur tandurust rehti hain."

Phir Sanjay bole,

"Neel aur Nishadh Parvat ke beech ek bahut bada Jambu Vriksh hai."

"Isi vriksh ke naam par is bhoomi ka naam Jambudweep pada."

"Yeh vriksh itna ooncha hai ki aasman ko chhoota hua lagta hai."

"Iske phal bahut bade hote hain."

"Jab woh pak kar girte hain, toh zor ki awaaz hoti hai."

"Unmein se chandi jaisa chamakta ras nikalta hai."

"Wahi ras ek pavitra nadi ban jaata hai."

"Jo uska jal peeta hai, uske mann ko shanti milti hai."

"Use kabhi budhapa ya pyaas pareshan nahi karti."

"Wahin ek bahut hi keemti sona bhi milta hai."

"Usse devta apne gehne banate hain."

Aakhir mein Sanjay bole,

"Malyavat Parvat ki choti par ek divya agni hamesha jalti rehti hai."

"Kaha jaata hai ki yug ke ant mein wahi agni srishti ka vinaash karegi."

"Wahan rehne wale mahan tapasvi bahut kathor tapasya karte hain."

"Woh apni shakti se Surya Dev ki seva karte hain."

"Bahut lambe samay tak Surya ke saath rehkar, baad mein Chandralok ki yatra karte hain."

"Yeh sab pavitra bhoomiyan Bhagwan ki adbhut rachna ka hissa hain." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.8
        with st.expander("Section 6.1.8  Section VIII"):
            text1 = """ Section VIII – Hinglish Story

Dhritarashtra bole,

"Sanjay, mujhe sabhi Varshon, Parvaton aur wahan rehne wale logon ke baare mein aur batao."

Sanjay bole,

"Rajan, Shvet Parvat ke dakshin aur Nishadh Parvat ke uttar ek sundar bhoomi hai."

"Uska naam Romanaka Varsha hai."

"Wahan ke log gore rang ke, sundar aur achhe swabhav ke hote hain."

"Unka koi dushman nahi hota."

"Woh hamesha khush rehte hain."

"Aur bahut lambi umar jeete hain." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Phir Sanjay bole,

"Nishadh Parvat ke dakshin Hiranmaya Varsha hai."

"Wahan Hiranvati naam ki pavitra nadi bahti hai."

"Wahin Pakshiraj Garud ka nivaas hai."

"Wahan ke log dhanvaan, balwaan aur Yakshon ke mitra hote hain."

"Woh bhi bahut lambi umar tak jeete hain."

Uske baad Sanjay ne kaha,

"Sringavat Parvat ke teen adbhut shikhar hain."

"Ek ratnon se bana hai."

"Doosra anek keemti mani aur sundar mahallon se saja hua hai."

"Wahan Sandili naam ki divya devi nivaas karti hain."

Phir Sanjay bole,

"Iske uttar mein Airavat Varsha hai."

"Yeh sabse sundar aur pavitra bhoomiyon mein se ek hai."

"Wahan Sooraj ki garmi nahi padti."

"Chandrama aur taare hi roshni dete hain."

"Wahan ke log kamal ke phool jaise sundar hote hain."

"Unke sharir se kamal ki sugandh aati hai."

"Woh bina bhojan ke bhi jee sakte hain."

"Unka mann aur indriyan poori tarah niyantrit rehte hain."

"Woh paap se door aur bahut pavitra jeevan jeete hain."

"Unki umar bhi bahut lambi hoti hai."

Phir Sanjay ne sabse pavitra baat batayi.

"Wahan Ksheer Sagar ke uttar Bhagwan Hari Vishnu ka divya nivaas hai."

"Woh ek sone ke divya rath par virajmaan rehte hain."

"Unka rath bahut tej aur man ki gati se chalne wala hai."

"Bhagwan Vishnu hi poore sansaar ke paalanhaar hain."

"Jab srishti ka ant hota hai..."

"Tab sab kuch unmein sama jaata hai."

"Aur jab nayi srishti shuru hoti hai..."

"Tab sab kuch phir unhi se janm leta hai."

"Wahi Prithvi hain."

"Wahi Jal hain."

"Wahi Agni, Vayu aur Aakash bhi hain."

"Wahi sab jeevon ke rakshak aur is poore brahmand ke swaami hain."

Vaisampayan bole,

"Yeh sab sunkar Dhritarashtra phir gehri soch mein doob gaye."

Unhone dheere se kaha,

"Ab mujhe samajh aa raha hai..."

"Is sansaar mein sab kuch Samay ke adheen hai."

"Samay hi sab kuch banata hai."

"Aur Samay hi sab kuch mita deta hai."

"Is duniya mein kuch bhi hamesha ke liye nahi rehta."

"Bhagwan Narayan hi is poori srishti ko chalate hain."

"Devta unhe Vaikunth kehte hain."

"Aur log unhe Bhagwan Vishnu ke naam se jaante hain." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.9
        with st.expander("Section 6.1.9  Section IX"):
            text1 = """ Section IX – Hinglish Story

Dhritarashtra bole,

"Sanjay, mujhe Bharat Varsha ke baare mein batao."

"Wahi dharti jiske liye Kaurav aur Pandav yudh karne ja rahe hain."

"Wahi rajya jiske liye Duryodhan itna lalchi ho gaya hai."

"Mujhe us pavitra bhoomi ka varnan karo."

Sanjay bole,

"Rajan, Pandav lalchi nahi hain."

"Woh sirf apna adhikaar chahte hain."

"Lekin Duryodhan aur uske saathi lalach mein andhe ho gaye hain."

"Isi lalach ki wajah se yeh Mahayudh hone ja raha hai."

Phir Sanjay bole,

"Bharat Varsha bahut pavitra bhoomi hai." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Is dharti se Indra, Manu, Raja Prithu, Ikshvaku, Yayati, Mandhata aur anek mahaan raja prem karte the."

"Bahut se dharmik aur veer rajaon ne isi dharti par raj kiya."

Uske baad Sanjay ne Bharat ke bade-bade parvaton ka varnan kiya.

"Wahan Mahendra, Malaya, Sahya, Vindhya aur kai mahaan parvat hain."

"Inke alawa hazaaron chhote-bade pahaad bhi hain."

"Har jagah alag-alag log aur sabhyataayein basti hain."

Phir Sanjay bole,

"Bharat Varsha mein bahut si pavitra nadiyan bahti hain."

"Jaise Ganga..."

"Yamuna..."

"Saraswati..."

"Sindhu..."

"Narmada..."

"Godavari..."

"Kaveri..."

"Aur bahut si anya pavitra nadiyan."

"Yeh sab is dharti ko jeevan deti hain."

"Isi liye inhe sabki maa maana gaya hai."

Uske baad Sanjay ne bataya,

"Is bhoomi mein anek rajya hain."

"Jaise Kuru..."

"Panchal..."

"Kashi..."

"Koshal..."

"Magadh..."

"Videh..."

"Ang..."

"Vang..."

"Kaling..."

"Keral..."

"Dravid..."

"Gandhar..."

"Kashmir..."

"Aur bahut se anya desh."

"Har jagah alag log, alag bhaasha aur alag parampara hai."

"Phir bhi sab isi Bharat bhoomi ka hissa hain."

Aakhir mein Sanjay ne ek gehri baat kahi.

"Dharti ek Kamdhenu gaay ki tarah hai."

"Agar uski achhi tarah dekhbhaal ki jaaye, toh woh sabko dhan, sukh aur samriddhi deti hai."

"Lekin jab log lalach mein aa jaate hain..."

"Tab woh isi dharti ke liye ek-doosre se ladne lagte hain."

"Raja kabhi-kabhi maans ke tukde ke liye ladte kutto ki tarah vyavhaar karte hain."

"Unka lalach kabhi khatam nahi hota."

"Isi lalach ki wajah se Kaurav aur Pandav bhi yudh ke raaste par chal pade hain."

"Lekin yaad rakhiye, Rajan..."

"Jo dharti ki raksha karta hai, wahi dharti uski raksha karti hai."

"Dharti hi sabki maa hai."

"Uska samman karna hi sabse bada dharm hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.1.10
        with st.expander("Section 6.1.10  Section X"):
            text1 = """ Section X – Hinglish Story

Dhritarashtra bole,

"Sanjay, mujhe Bharat Varsha aur uske paas ke doosre pavitra deshon ke baare mein batao."

"Mujhe yeh bhi batao ki alag-alag yugon mein log kaise rehte the."

Sanjay bole,

"Rajan, Bharat Varsha mein chaar yug hote hain."

"Unke naam hain..."

Satya Yug (Krita), Treta Yug, Dwapar Yug aur Kali Yug.

"Sabse pehle Satya Yug aata hai."

"Uske baad Treta."

"Phir Dwapar."

"Aur sabse aakhir mein Kali Yug." """
            create_image_text_layout(
                "attached_assets/chapter6/6.1.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Sanjay ne aage kaha,

"Satya Yug mein log bahut lambi umar jeete the."

"Woh lagbhag 4000 saal tak jeevit rehte the."

"Treta Yug mein logon ki umar 3000 saal hoti thi."

"Dwapar Yug mein yeh lagbhag 2000 saal reh gayi."

"Lekin Kali Yug mein..."

"Insaan ki umar ka koi nishchit samay nahi hai."

"Kuch bachche toh janm se pehle ya janm ke turant baad hi duniya chhod dete hain."

Phir Sanjay bole,

"Satya Yug ke log bahut balwaan aur buddhimaan hote the."

"Woh satya bolte the."

"Dharm ka paalan karte the."

"Rishi-Muni kathin tapasya karte the."

"Raja nyaay aur imaandari se rajya chalate the."

"Sab log shaant aur sukhi jeevan jeete the."

Uske baad Sanjay bole,

"Treta Yug mein bhi mahaan aur veer raja hote the."

"Woh samundar se samundar tak rajya chalate the."

"Woh bahadur, nyaaypriya aur dhanurvidya mein nipun hote the."

Phir Dwapar Yug ka varnan karte hue Sanjay bole,

"Dwapar Yug mein log bahut mehnati aur shaktishaali the."

"Lekin dheere-dheere sab ek-doosre se aage badhne ki ichchha rakhne lage."

"Pratiyogita aur sangharsh badhne laga."

Aakhir mein Sanjay bole,

"Kali Yug mein logon ki taakat kam ho jaati hai."

"Gussa zyada hota hai."

"Lalach badh jaata hai."

"Log jhooth bolne lagte hain."

"Irshya, ahankaar, dhokha aur dushmani badh jaati hai."

"Yahi Kali Yug ki pehchaan hai."

Phir Sanjay ne kaha,

"Ab Dwapar Yug ka sirf thoda sa samay bacha hai."

"Uske baad Kali Yug shuru hoga."

"Ek aur baat yaad rakhiye, Rajan."

"Himavat Varsha, Bharat Varsha se bhi adhik pavitra maana gaya hai."

"Aur Harivarsha, Himavat Varsha se bhi zyada uttam maana gaya hai."

"Har agla Varsha apne gunon mein pichhle se aur bhi shreshth hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    # ==================================================
    # Chapter 6.2 - Bhumi Parva
    # ==================================================

    with st.expander("Chapter 6.2  Bhumi Parva"):

        # Section 6.2.1
        with st.expander("Section 6.2.1  Section XI"):
            text1 = """ Section XI – Hinglish Story

Dhritarashtra bole,

"Sanjay, tumne Jambudweep ke baare mein bataya."

"Ab mujhe uski size aur doosre bade dweep aur samundaron ke baare mein batao."

"Shakdweep, Kushdweep, Shalmalidweep aur Kraunchdweep kitne bade hain?"

"Aur Rahu, Chandrama aur Surya ke baare mein bhi batao."

Sanjay bole,

"Rajan, dharti par bahut saare dweep hain."

"Lekin main abhi tumhe saat bade dweep, Chandrama, Surya aur Rahu ke baare mein bataunga." """
            create_image_text_layout(
                "attached_assets/chapter6/6.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Jambudweep ka vistaar 18,600 Yojan bataya gaya hai."

"Uske chaaron taraf namkeen samundar hai."

"Yeh samundar usse bhi lagbhag do guna bada hai."

"Is samundar mein bahut se rajya, pahaad, ratna aur moonga hain."

"Ab suno Shakdweep ke baare mein."

"Shakdweep, Jambudweep se do guna bada hai."

"Aur uske chaaron taraf ka samundar bhi usi ke anusaar bahut bada hai."

"Wahan ke log dharm ko bahut maante hain."

"Wahan logon mein bhookh aur akaal nahi hota."

"Sab log swasth, shaktishaali aur shaant swabhav ke hote hain."

Dhritarashtra bole,

"Sanjay, Shakdweep ke baare mein aur detail mein batao."

Sanjay bole,

"Shakdweep mein saat bade parvat hain."

"Yeh sab parvat ratnon aur keemti pattharon se bhare hue hain."

"Sabse pehla hai Meru Parvat."

"Yeh devtaon, Rishiyon aur Gandharvon ka nivaas hai."

"Uske baad Malaya Parvat hai."

"Yahin se baadal bante hain aur phir alag-alag jagah baarish lekar jaate hain."

"Uske baad Jaladhara Parvat hai."

"Indra yahan se jal grahan karte hain, jisse baarish hoti hai."

"Phir aata hai Raivatak Parvat."

"Iske upar Revati Nakshatra ko sthapit kiya gaya hai."

"Uske uttar mein Shyam Parvat hai."

"Yeh bahut ooncha aur sundar hai."

"Iska rang gehra hai, isliye wahan ke logon ka rang bhi gehra bataya gaya hai."

Dhritarashtra ne poocha,

"Lekin Sanjay, wahan ke log dark complexion ke kyun hain?"

Sanjay bole,

"Rajan, har dweep mein alag-alag rang ke log hote hain."

"Lekin Shyam Parvat ke kshetra mein logon ka rang gehra hone ke kaaran uska naam Shyam Parvat pada."

"Iske baad Durgashail aur phir Kesari Parvat aata hai."

"Kesari Parvat se chalne wali hawa bahut sugandhit hoti hai."

"Yeh sabhi parvat ek-doosre se bahut bade hain."

Phir Sanjay ne Shakdweep ke saat Varshon ke naam bataye.

"Meru ka Varsha Mahakasa hai."

"Malaya ka Kumudottara."

"Jaladhara ka Sukumara."

"Raivatak ka Kaumara."

"Shyam ka Manikanchana."

"Kesari ka Mandaki."

"Aur aakhri Varsha ka naam Mahapuman hai."

Sanjay ne aage kaha,

"Shakdweep ke beech ek bahut bada Saka Vriksh hai."

"Yeh Jambudweep ke Jambu Vriksh jitna hi bada hai."

"Wahan ke log is pavitra ped ki pooja karte hain."

"Wahan Bhagwan Shiv ki bhi pooja hoti hai."

"Siddh, Charan aur Devta bhi wahan aate hain."

"Wahan ke log dharmik aur apne kartavya ke prati imaandaar hote hain."

"Chori jaisi koi baat wahan dekhne ko nahi milti."

"Log budhape aur mrityu se bhi door rehte hain aur bahut lambi umar jeete hain."

"Wahan bahut si pavitra nadiyan bhi hain."

"Unka jal paap ko door karne wala maana jaata hai."

"Un nadiyon mein Sukumari, Kumari, Seta, Keveraka, Mahanadi, Manijala aur Chakshu jaise naam hain."

"Iske alawa hazaaron aur nadiyan bhi hain."

Phir Sanjay bole,

"Shakdweep mein chaar bade pavitra pradesh bhi hain."

"Unke naam hain Mriga, Masaka, Manasa aur Mandaga."

"Mriga mein zyada tar Brahman apne kartavya mein lage rehte hain."

"Masaka mein dharmik Kshatriya rehte hain."

"Manasa ke log Vaishya ke kartavya nibhate hain aur dharm aur samriddhi ke prati samarpit hain."

"Mandaga ke log bahadur aur dharmik Shudra hain."

"Sabse khaas baat yeh hai ki wahan koi raja nahi hai."

"Kisi ko dand dene wala bhi koi nahi hai."

"Log apne-apne kartavya ko samajhte hain aur ek-doosre ki raksha karte hain."

"Yahi Shakdweep ka sankshipt varnan hai." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.2.2
        with st.expander("Section 6.2.2  Section XII"):
            text1 = """ Section XII – Hinglish Story

Sanjay bole,

"Rajan, ab main tumhe uttar ki taraf ke dweep aur unke adbhut samundaron ke baare mein bataata hoon."

"Sabse pehle ek aisa samundar hai jisme ghee jaisa jal hai."

"Uske baad ek samundar hai jisme dahi jaisa jal hai."

"Phir ek samundar hai jisme madira jaisa jal hai."

"Aur uske baad ek aur bada samundar hai."

"Jaise-jaise hum uttar ki taraf badhte hain, har agla dweep pehle wale se do guna bada hota jaata hai." """
            create_image_text_layout(
                "attached_assets/chapter6/6.2.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Kusadweep aur Kraunchdweep

"Beech wale dweep mein Goura Parvat hai."

"Woh laal rang ke ek khaas padarth se bana hua bataya gaya hai."

"Ek doosre dweep mein Krishna Parvat hai."

"Yeh Bhagwan Narayan ka priya sthaan hai."

"Wahin Keshav divya ratnon ki raksha karte hain."

"Aur apni kripa se sabhi jeevon ko sukh dete hain."

"Kusadweep mein pavitra Kusha ghaas ka ek bada kshetra hai."

"Log uski pooja karte hain."

"Salmalidweep mein ek vishal Shalmali vriksh hai."

"Uski bhi log shraddha se pooja karte hain."

"Kraunchdweep mein Maha-Krauncha naam ka ek bada parvat hai."

"Woh har tarah ke ratnon se bhara hua hai."

"Wahan Gomanta naam ka ek aur mahaan parvat hai."

"Us par Bhagwan Narayan, yani Hari, ka nivaas bataya gaya hai."

Kusadweep ke saat Varsha

"Kusadweep mein chhe bade parvat aur saat Varsha bataye gaye hain."

"Un Varshon ke naam hain Audhido, Venumandala, Suratha, Kamvala, Dhritimat, Prabhakara aur Kapila."

"Yeh bhoomi devtaon aur Gandharvon ke liye bhi bahut priya hai."

"Wahan ke log bahut komal aur sundar hote hain."

"Wahan koi chor nahi hota."

"Koi Mleccha jaati bhi nahi hoti."

"Sabse khaas baat..."

"Wahan ke log marte nahi hain."

Kraunchdweep

"Kraunchdweep mein Krauncha ke baad Vamanaka, Andhakara, Mainaka, Govinda aur Nivida naam ke bade parvat hain."

"Inke beech alag-alag sundar desh hain."

"Unmein Kusala, Manonuga, Ushna, Pravaraka, Andhakaraka, Munidesh aur Dundubhiswana jaise kshetra hain."

"Wahan Siddh aur Charan bhi rehte hain."

"Yeh desh devtaon aur Gandharvon ke nivaas ke roop mein bataye gaye hain."

Pushkaradweep

"Ab aata hai Pushkaradweep."

"Wahan Pushkar naam ka ek bahut bada parvat hai."

"Woh keemti ratnon se bhara hua hai."

"Wahin swayam Prajapati ka nivaas bataya gaya hai."

"Devta aur mahaan Rishi unki pooja karte hain."

"Jaise-jaise dweep uttar ki taraf door hote jaate hain..."

"Wahan logon ka swasthya, jeevan, sanyam aur satya ke prati lagav aur badhta jaata hai."

Sama aur chaar divya haathi

"In sab bhoomiyon ke baad ek jagah aati hai jiska naam Sama hai."

"Uska aakar taaron jaisa hai aur uske chaar kone hain."

"Wahan chaar mahaan haathi rehte hain."

"Unke naam hain Vamana, Airavata, Supratika aur ek anya divya haathi."

"Yeh chaaron dishaon ke rakshak maane jaate hain."

"Unka aakar itna vishal hai ki unki lambai aur chaudai ko naapna bhi sambhav nahi bataya gaya."

"Jab hawa alag-alag dishaon se chalti hai..."

"Yeh divya haathi use apni soond se kheench lete hain."

"Phir thodi der baad woh hawa ko dobara chhod dete hain."

"Isi hawa ke chalne se dharti ke jeev saans le paate hain."

Surya, Chandra aur Rahu

Dhritarashtra bole,

"Sanjay, ab mujhe Surya, Chandra aur Rahu ke baare mein batao."

Sanjay bole,

"Rajan, Shastron ke anusaar Rahu ka aakar gol hai."

"Uska diameter 12,000 Yojan bataya gaya hai."

"Uski circumference 42,000 Yojan batayi gayi hai."

"Chandrama ka diameter 11,000 Yojan bataya gaya hai."

"Uski circumference lagbhag 38,900 Yojan hai."

"Surya ka diameter 10,000 Yojan bataya gaya hai."

"Uski circumference lagbhag 35,800 batayi gayi hai."

"Rahu bahut bada hai."

"Isi wajah se woh samay aane par Surya aur Chandra ko dhak leta hai."

Sanjay ne ant mein kaha,

"Rajan, maine tumhe Shastron mein bataye gaye brahmand ke is roop ka varnan kar diya hai."

"Ab meri ek baat maan lo."

"Apne putra Duryodhan ko shant karo."

"Yudh se kuch achha nahi hoga."

"Shanti hi sabke liye behtar raasta hai."

Aur is tarah Bhumi Parva ka yeh adbhut varnan samaapt hua. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


    # ==================================================
    # Chapter 6.3 - Bhagavat-Gita Parva
    # ==================================================

    with st.expander("Chapter 6.3  Bhagavat-Gita Parva"):

        # Section 6.3.1
        with st.expander("Section 6.3.1  Section XIII"):
            text1 = """ Section XIII – Bhishma ka Patan

Yudh ka maidan bahut bhayanak ho chuka tha.

Sanjay bahut dukhi hokar Hastinapur ke rajmahal mein wapas aaye.

Dhritarashtra pehle se hi gehri chinta mein doobe hue the.

Sanjay ne unke saamne jaakar kaha,

"Rajan, main Sanjay hoon."

"Main aapko ek bahut dukhad khabar dene aaya hoon."

"Bhishma Pitamah shaheed ho gaye hain." """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Shantanu ke putra aur Kuru vansh ke sabse bade Pitamah..."

"Jo sabse mahaan yoddhaon mein se ek the..."

"Aaj woh baanon ki shayya par lete hue hain."

Dhritarashtra yeh sunkar aur bhi dukhi ho gaye.

Sanjay ne kaha,

"Rajan, aapke putra Duryodhan ko Bhishma par bahut bharosa tha."

"Dice game ke samay bhi Duryodhan ko Bhishma ki shakti par poora vishwas tha."

"Lekin aaj wahi mahaan yoddha yudh ke maidan mein gir chuke hain."

"Unhe Sikhandi ke saamne ladte hue baan lage."

Sanjay ne Bhishma ki mahaanta yaad karte hue kaha,

"Rajan, yeh wahi Bhishma the..."

"Jinhone Kashi ke sabhi rajaon ko ek hi rath par hara diya tha."

"Yeh wahi veer the jinhone Parashurama jaise mahaan yoddha se bhi yudh kiya tha."

"Parashurama bhi unhe hara nahi sake."

"Bhishma itne shaktishaali the."

"Unki himmat Indra jaisi thi."

"Unki majbooti Himavat Parvat jaisi thi."

"Unka mann samundar jaisa gehra tha."

"Aur unka dhairya Dharti jaisa tha."

"Yudh mein unke baan unke daanton jaise the."

"Unka dhanush unke muh jaisa tha."

"Aur unki talwar unki jeebh jaisi lagti thi."

"Unhe dekhkar Pandav sena bhi kabhi-kabhi darr jaati thi."

"Jaise sher ko dekhkar gaayen dar jaati hain..."

"Waise hi Bhishma ko dekhkar bade-bade yoddha bhi ghabra jaate the."

Lekin Bhishma ne haar nahi maani.

"Unhone 10 din tak Kaurav sena ki raksha ki."

"Har din woh bahut bade-bade yoddhaon ko haraate rahe."

"Har din woh lagbhag 10,000 warriors ko yudh mein gira dete the."

"Unki shakti dekhkar sab hairaan the."

"Lekin aaj..."

"Woh mahaan Bhishma bhi dharti par gir gaye."

"Unka sharir baanon se bhar gaya."

"Woh ek bade ped ki tarah dharti par gir pade, jaise tez hawa kisi bade ped ko tod de."

Sanjay ne ant mein Dhritarashtra se kaha,

"Rajan, Bhishma jaise mahaan yoddha ka patan sirf yudh ki wajah se nahi hua."

"Iske peeche aapke putra ke galat faisle bhi the."

"Galat salah aur ahankaar ne sabko is vinash ki taraf dhakel diya."

"Bhishma jaise mahaan vyakti bhi is yudh ko rok nahi sake."

"Ab yudh aur bhi bhayanak hone wala tha." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.2
        with st.expander("Section 6.3.2  Section XIV"):
            text1 = """ Section XIV – Bhishma ke girne ke baad

Dhritarashtra bahut dukhi the.

Unhone Sanjay se poocha,

"Bhishma jaise mahaan yoddha ko Sikhandi kaise hara saka?"

"Jis Bhishma ko devta bhi hara nahi sakte the, woh yudh mein kaise gir gaye?"

"Jab Bhishma Pandav sena par toot pade, tab unke saath kaun tha?"

"Kaun unke aage chal raha tha?"

"Kaun unke peeche se raksha kar raha tha?"

"Kaun unke rath ke dono taraf khada tha?"

"Jab Pandavon ne Sikhandi ko aage karke Bhishma par hamla kiya, tab mere Kuru yoddha kahan the?"

Dhritarashtra ka dukh aur badh gaya.

Woh bole, """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Bhishma sirf ek yoddha nahi the."

"Woh hamare sabse bade sahare the."

"Unki himmat bahut mahaan thi."

"Unka gyaan bahut gehra tha."

"Unki neeti aur samajh bhi bahut tez thi."

"Unhone das din tak hamari sena ki raksha ki."

"Har din woh hazaaron yoddhaon ko haraate rahe."

"Phir aisa kya hua ki woh khud haar gaye?"

Dhritarashtra ne hairani se kaha,

"Jab Drona, Kripa aur Ashwatthama jaise mahaan yoddha Bhishma ke paas the, tab unhe koi kaise hara saka?"

"Bhishma ko Atiratha kaha jaata tha."

"Woh Parashurama jaise mahaan yoddha se bhi yudh kar chuke the."

"Parashurama bhi unhe hara nahi paaye the."

"Phir Sikhandi unhe kaise gira saka?"

Dhritarashtra ki aankhon ke saamne jaise poora yudh ka maidan aa gaya.

Unhone kaha,

"Bhishma jab apne rath par khade hote the, toh Pandav sena kaanp jaati thi."

"Unke baanon ki baarish se poora maidan bhar jaata tha."

"Unka dhanush garajta tha."

"Unki talwar bijli ki tarah chamakti thi."

"Unke aas-paas yudh ka maidan ek bhayanak samundar jaisa lagta tha."

"Us samundar mein baan magarmachh jaise the."

"Talwar aur gada jaise bade jaanwar the."

"Rath, ghode aur haathi usmein ghoomti hui lehron jaise lagte the."

"Aur yoddha usmein tairti hui machhliyon jaise the."

"Bhishma khud us samundar ke beech ek bhayanak toofan jaise the."

Phir Dhritarashtra ne poocha,

"Jab Bhishma Duryodhan ke liye lad rahe the, tab unke aage kaun tha?"

"Unke right side ki raksha kaun kar raha tha?"

"Unke left side par kaun tha?"

"Unke rath ke aage aur peeche kaun lad raha tha?"

"Unki sena ke wings ki raksha kaun kar raha tha?"

"Agar itne mahaan yoddha Bhishma ke saath the, toh Pandav un tak pahunch kaise gaye?"

Dhritarashtra bahut dukhi hokar bole,

"Bhishma hamari sena ka sahara the."

"Unke bharose Duryodhan Pandavon se yudh kar raha tha."

"Ab woh sahara hi chala gaya."

"Jaise samundar paar karne wala aadmi beech samundar mein apni boat doobti hui dekh le..."

"Waise hi mere putron ki haalat hogi."

Phir Dhritarashtra ne ek gehri baat kahi,

"Ab mujhe samajh aa raha hai ki koi bhi vyakti maut se bach nahi sakta."

"Na shastra se..."

"Na himmat se..."

"Na buddhi se..."

"Na tapasya se..."

"Na apni shakti se."

"Jab Samay aa jaata hai, toh sabko jaana padta hai."

"Bhishma jaise mahaan yoddha bhi Samay ke saamne nahi tik sake."

Dhritarashtra phir bole,

"Ab mujhe yudh ka poora sach batao."

"Duryodhan, Karna, Shakuni aur Dushasan ne Bhishma ke girne par kya kaha?"

"Pandavon ne kya kiya?"

"Kisne jeeta?"

"Kisne haar maana?"

"Aur Bhishma ke alawa aur kaun-kaun yudh mein maara gaya?"

"Main sab kuch sunna chahta hoon."

"Jo kuch bhi hua, achha ya bura, mujhe poori sachchai batao."

"Bhishma ne yudh mein jo kuch kiya, woh bhi detail mein batao."

"Main jaanna chahta hoon ki Kaurav aur Pandav sena ke beech yeh bhayanak yudh aakhir hua kaise." """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.3
        with st.expander("Section 6.3.3  Section XV"):
            text1 = """ Section XV — Sanjaya begins describing Bhishma’s final battle

Sanjaya first tells Dhritarashtra that Duryodhana should not simply be blamed for everything. A person ultimately suffers the consequences of his own actions. He reminds Dhritarashtra that the Pandavas had tolerated many injuries for a long time and had even gone into the forest without immediately retaliating.

Then Sanjaya says that, through Vyasa’s boon and Yoga-power, he has been given extraordinary perception: he can see and hear things beyond ordinary human senses, understand the past and future, perceive the thoughts of others, and even move through the sky. With this ability, he will now narrate the terrifying battle in detail.

Duryodhana’s first priority: protect Bhishma

When both armies are ready for battle, Duryodhana immediately orders Dushasana to protect Bhishma.

His reasoning is very clear:

If Bhishma remains protected, he believes Bhishma can destroy the Pandavas, Somakas and Srinjayas. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Duryodhana therefore considers protecting Bhishma more important than anything else on the battlefield.

Why Sikhandi is so important

Bhishma himself has made one crucial declaration:

He will not fight Sikhandi.

His reason is that Sikhandi had previously been female. Because of this, Bhishma refuses to attack Sikhandi in battle.

This creates a major tactical weakness.

Duryodhana understands it and therefore orders the entire Kuru army to prevent Sikhandi from reaching Bhishma.

He compares the danger to a lion being killed by a jackal: even a tremendously powerful warrior can be brought down if the right weakness is exploited.

The Pandava formation around Sikhandi

The passage then gives the important protection arrangement:

Sikhandi is at the front.
Arjuna (Phalguni) protects Sikhandi.
Yudhamanyu protects Arjuna's left wheel.
Uttamauja protects Arjuna's right wheel.
Bhishma is the target they are trying to reach.

So the tactical problem is essentially:

Kuru army → protect Bhishma → prevent Sikhandi from reaching him

while the Pandava side is arranged as:

Yudhamanyu + Uttamauja → Arjuna → Sikhandi → Bhishma

The crucial point is that Sikhandi himself is not necessarily the most powerful warrior in this arrangement. His importance comes from Bhishma's own vow/refusal to fight him, while Arjuna is the warrior capable of exploiting that opening.

This sets up the actual explanation of how Bhishma, despite being virtually unbeatable, finally fell on the tenth day. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.4
        with st.expander("Section 6.3.4  Section XVI"):
            text1 = """ Section XVI — Yudh ke liye dono senaayein taiyaar

Raat khatam ho gayi.

Subah hote hi Kurukshetra mein har taraf yudh ki taiyaari shuru ho gayi.

"Taiyaar ho jao! Taiyaar ho jao!"

Aisi awaazein har taraf sunai dene lagi.

Shankh bajne lage.

Nagaade garajne lage.

Ghode zor-zor se hinahina rahe the.

Haathi zor se awaaz kar rahe the. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Rathon ke pahiyon ki awaaz poore maidan mein goonj rahi thi.

Yoddha zor se chillate aur apne sharir par haath maar kar yudh ke liye utsaah badha rahe the.

Dono senaayein suraj nikalte hi apni-apni jagah par khadi ho gayi.

Jab suraj ki roshni poore maidan par padi, toh hazaaron talwarein, dhanush, bhale, gada aur kavach chamakne lage.

Sone se saje hue rath aur haathi aise lag rahe the jaise bijli wale badal aasman mein tair rahe hon.

Hazaaron rath ek saath khade the.

Door se woh kisi bade shehar jaise dikh rahe the.

Kaurav sena ki taiyaari

Kauravon ki sena bahut badi thi.

Unke saath bahut saare raja aur mahaan yoddha khade the.

Shakuni, Shalya, Jayadratha, Vinda, Anuvinda, Kekaya ke raja, Sudakshina, Srutayudha, Jayatsena, Brihadvala aur Kritavarman jaise bade yoddha apni-apni sena ke saath taiyaar the.

Har yoddha apni ek badi division ko lead kar raha tha.

Kaurav sena mein 11 Akshauhini sena thi.

Sabhi yoddha kavach pehne hue the.

Unke haath mein powerful weapons the.

Sab Duryodhana ke liye poori tarah se ladne ke liye ready the.

Sabse aage kaun tha?

Kaurav sena ki sabse aage wali division mein ek mahaan yoddha khada tha.

Woh the...

Bhishma Pitamah.

Bhishma safed kapde aur safed kavach pehne hue the.

Unke sir par safed pagdi thi.

Unke upar safed chhatra tha.

Unka rath chandi jaisa chamak raha tha.

Aur unke rath par sone ka palmyra tree wala flag laga hua tha.

Door se Bhishma aise lag rahe the jaise safed baadalon ke beech poora chaand chamak raha ho.

Unhe dekhkar Pandav sena ke kai yoddha darr gaye.

Dhrishtadyumna ke saath khade Srinjaya warriors bhi Bhishma ko dekhkar kaanpne lage.

Unhe Bhishma ek bhookhe sher jaise lag rahe the.

Aur Pandav yoddha us sher ke saamne chhote jaanwaron jaise lag rahe the.

Pandav sena

Dusri taraf Pandavon ki bhi badi sena taiyaar thi.

Unke paas 7 Akshauhini sena thi.

Unki sena bhi bade-bade warriors se protected thi.

Dono senaayein ek-doosre ke saamne khadi thi.

Ek taraf 11 Akshauhini Kaurav sena.

Dusri taraf 7 Akshauhini Pandav sena.

Maidan mein haathi, ghode, rath aur hazaaron yoddha bhare hue the.

Dono senaayein door se aise lag rahi thi jaise do bade samundar ek-doosre ke saamne khade hon.

Har taraf weapons chamak rahe the.

Har taraf yoddha yudh ke liye ready the.

Sabko pata tha ki ab kuch hi der mein...

Mahabharat ka sabse bhayanak yudh shuru hone wala hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.5
        with st.expander("Section 6.3.5  Section XVII"):
            text1 = """ Section XVII — Yudh ka Pehla Din

Subah ho chuki thi.

Kurukshetra mein dono senaayein yudh ke liye poori tarah ready thi.

Aasman mein ajeeb signs dikh rahe the.

Suraj kuch ajeeb sa lag raha tha, jaise do hisson mein baant gaya ho.

Aasman mein kai grah bahut teekhe aur chamakte hue dikh rahe the.

Door-door se jackals aur crows ki bhayanak awaazein aa rahi thi.

Aisa lag raha tha jaise prakriti bhi hone wale yudh ka signal de rahi ho.

Bhishma ki ek ajeeb baat """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Sanjay batate hain ki har subah Bhishma aur Drona mann ko shaant karke ek ajeeb baat kehte the:

"Pandav putron ki victory ho."

Lekin phir bhi woh Duryodhana ke liye lad rahe the.

Yeh unki duty aur unke personal feelings ke beech ka bada conflict tha.

Bhishma ka warriors ko message

Bhishma ne sabhi Kshatriya kings ko bulaya.

Unhone kaha,

"Yudh mein marna Kshatriya ke liye ek honour hai."

"Purane samay ke mahaan kings jaise Nabhaga, Yayati, Mandhata, Nahusha aur Nriga bhi battle mein apni bravery dikhakar great destiny ko prapt hue."

"Isliye yudh se daro mat."

"Yeh tumhare liye heaven tak jaane ka ek raasta hai."

"Battlefield mein brave hokar marna Kshatriya ki duty hai."

Sabhi kings ne Bhishma ki baat suni.

Phir woh apni-apni divisions ki taraf chale gaye.

Karna ne yudh se door rehne ka decision liya

Lekin ek important warrior battlefield mein nahi lada.

Woh tha Karna.

Karna ne Bhishma ke respect mein apne weapons side mein rakh diye.

Jab tak Bhishma army ke commander the, Karna ne yudh mein participate nahi kiya.

Isliye us din Kaurav army mein Karna ki kami clearly feel ho rahi thi.

Bhishma sabse aage

Kaurav army ke commander Bhishma the.

Unka bada palmyra tree wala flag hawa mein lehra raha tha.

Unka rath chamak raha tha.

Door se Bhishma aise lag rahe the jaise khud Suraj battlefield mein aa gaya ho.

Unke peeche bahut saare powerful warriors khade the.

Ashwatthama, Shalya, Bhurisravas, Vikarna, Drona aur kai anya warriors apni-apni jagah par ready the.

Drona ke flag par ek golden altar aur water-pot ka symbol tha.

Duryodhana ke flag par gems se bana hua elephant tha.

Har taraf alag-alag warriors ke beautiful flags chamak rahe the.

Jayadratha ki massive army

Jayadratha bhi apni huge army ke saath battlefield mein tha.

Uske paas:

1 lakh chariots
8,000 elephants
60,000 cavalry

the.

Uski army bahut powerful thi.

Kalinga ki army

Kalinga king bhi ek huge army ke saath aaya.

Uske paas:

60,000 chariots
10,000 elephants

the.

Unke elephants itne bade the ki door se chalte hue mountains jaise lag rahe the.

Kalinga king golden armour pehne hue tha.

Uska standard fire ki tarah chamak raha tha.

Bhagadatta ka arrival

Phir aaya ek aur mahaan warrior — Bhagadatta.

Woh apne huge elephant par sawar tha.

Woh elephant battlefield mein kisi mountain jaisa lag raha tha.

Bhagadatta bhi apne elephant par baithkar aise dikh raha tha jaise Indra apne divine elephant par aa gaya ho.

Avanti ke Vinda aur Anuvinda bhi elephants par sawar hokar uske saath aa gaye.

Kauravon ka battle formation

Drona, Bhishma, Ashwatthama, Valhika aur Kripa ne milkar Kaurav army ka ek powerful Vyuha banaya.

Is formation mein:

Elephants = body

Kings = head

Horses = wings

Aur chariots har taraf arranged the.

Puri formation aisi lag rahi thi jaise koi bada dangerous creature battlefield mein khada ho aur kisi bhi moment attack karne wala ho.

Dono armies ab bilkul saamne thi.

Har warrior apni position par tha.

Har weapon ready tha.

Har taraf drums aur conches ki awaaz goonj rahi thi.

Aur ab...

Kurukshetra ka mahaan yudh shuru hone wala tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.6
        with st.expander("Section 6.3.6  Section XVIII"):
            text1 = """ Section XVIII — Bhishma ki protection aur Kaurav sena ka samundar

Ab yudh ka samay aa gaya tha.

Achaanak poore Kurukshetra mein bahut tez shor hone laga.

Shankh zor-zor se bajne lage.

Nagaade garajne lage.

Haathi zor se chillane lage.

Rathon ke pahiyon ki awaaz poore maidan mein goonj uthi.

Ghode zor se hinahina rahe the.

Yoddha zor-zor se yudh ke naare laga rahe the. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Aisa lag raha tha jaise poori Dharti hil rahi ho.

Dono senaayein ek-doosre ke saamne aakar khadi ho gayi.

Kaurav aur Pandav dono taraf ke yoddha bhi ek pal ke liye is mahaan sena ko dekhkar hil gaye.

Sone se saje hue haathi aur rath bijli wale baadal jaise lag rahe the.

Hazaaron flags hawa mein lehra rahe the.

Kuch flags sone se bane the aur fire ki tarah chamak rahe the.

Poora battlefield kisi devtaon ke mahal jaisa dikh raha tha.

Bhishma ki protection

Duryodhana ne pehle hi kaha tha ki Bhishma ko kisi bhi haal mein protect karna hai.

Isliye Bhishma ke peeche bahut saare powerful warriors khade the.

Unmein Dushasana, Durvishaha, Durmukha, Dussaha, Vivinsati, Chitrasena aur Vikarna jaise warriors the.

Inke saath aur bhi bade warriors the:

Satyavrata, Purumitra, Jaya, Bhurisravas aur Sala.

Inke peeche lagbhag 20,000 chariots bhi the.

Sabka ek hi goal tha:

Bhishma ko safe rakhna.

Bhishma ke aas-paas poori army

Sirf Kaurav princes hi nahi, balki bahut saari kingdoms ki armies bhi Bhishma ki protection mein thi.

Abhishahas, Surasenas, Sivis, Vasatis, Matsyas, Amvashtas, Trigartas, Kekayas, Sauviras aur doosre regions ke warriors bhi wahan khade the.

In sabhi warriors ne decide kar liya tha ki woh Bhishma ke liye apni jaan tak dene ko ready hain.

Unke paas hazaaron chariots the.

Unke peeche Magadha ka king apni 10,000 elephants wali division ke saath aaya.

Haathi itne zyada the ki poora area bhar gaya.

Unke chariots aur elephants ki protection ke liye bhi bahut badi force thi.

Aur sabse aage lakho foot-soldiers weapons lekar khade the.

Kisi ke paas bow tha.

Kisi ke paas sword.

Kisi ke paas shield.

Kuch warriors apne haathon aur special darts se bhi fight karne ke liye ready the.

Kaurav sena ka size

Duryodhana ke paas total 11 Akshauhini ki huge army thi.

Itni badi army battlefield mein ek saath khadi thi ki door se dekhne par woh kisi bahut bade samundar jaisi lag rahi thi.

Sanjay kehte hain ki Kaurav sena ka scene aisa tha jaise:

Ganga aur Yamuna alag-alag direction se aakar ek jagah mil rahi hon.

Har taraf warriors hi warriors the.

Rath.

Ghode.

Haathi.

Foot-soldiers.

Flags.

Weapons.

Aur beech mein sabse important warrior—

Bhishma Pitamah.

Unki protection ke liye poori Kaurav sena ek shield ki tarah khadi thi.

Lekin doosri taraf Pandav bhi chup nahi the.

Ab bas ek signal ki zarurat thi...

Aur Kurukshetra mein asli yudh shuru hone wala tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.7
        with st.expander("Section 6.3.7  Section XIX"):
            text1 = """ Section XIX — Pandavon ki Vajra Vyuha rachna

Dhritarashtra ka sawal bahut important tha:

“Kauravon ke paas 11 Akshauhini sena hai, jabki Pandavon ki sena chhoti hai. Phir Yudhishthira ne Bhishma ki itni badi sena ka saamna kaise kiya?”

1. Yudhishthira ne strategy banayi

Yudhishthira ne Arjuna se kaha:

Hamari sena unse kam hai, isliye humein apni sena ko failana nahi chahiye. Kam sena ko condensed formation mein ladna chahiye.

Iske liye unhone Rishi Brihaspati ki military teaching ka reference diya.

Arjuna ne kaha:

“Main Vajra Vyuha banaunga.”

Vajra ka matlab yahan thunderbolt / vajra jaisi mazboot battle formation hai. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 2. Sabse aage — Bhima 🔥

Arjuna ne decide kiya ki Bhima ko front mein rakha jayega.

Reason simple tha:

Bhima close combat aur heavy striking mein bahut powerful tha.

Sanjaya ke description mein Bhima ko aisa warrior bataya gaya hai jiske saamne Duryodhana aur doosre warriors bhi lion ko dekhkar chhote animals ki tarah retreat kar sakte hain.

Bhima ki presence ka matlab tha:

enemy ka first attack = Bhima se takraana.

Arjuna ne kaha ki Pandav warriors Bhima ko ek wall/shield ki tarah use karenge.

3. Pandav formation ke main commanders

Vajra formation mein front/leading portion ko:

Bhima
Dhrishtadyumna
Nakula
Sahadeva
Dhrishtaketu

lead kar rahe the.

Unke peeche King Virata apni Akshauhini ke saath tha.

4. Bhima ke protection ka arrangement

Bhima ko akela front par nahi chhoda gaya.

Nakula aur Sahadeva — Bhima ke chariot wheels ko protect kar rahe the.

Draupadi ke 5 sons + Abhimanyu — Bhima ko rear se protect kar rahe the.

Phir:

Dhrishtadyumna + Prabhadrakas — in princes ko protect kar rahe the.

Yaani formation layered thi:

Front → Bhima → supporting warriors → rear protection

5. Sabse important: Shikhandi → Arjuna → Bhishma

Is formation ka ek bahut important objective tha:

Bhishma ko target karna.

Dhrishtadyumna ke baad Shikhandi tha.

Shikhandi ko Arjuna protect kar raha tha.

Aur Shikhandi ka primary objective tha:

Bhishma ka destruction.

Yeh Section XV mein Bhishma ke statement se bhi connect hota hai—Bhishma ne kaha tha ki woh Shikhandi par attack nahi karega.

Isliye strategic chain kuch aisi thi:

Shikhandi → Arjuna → Bhishma

Arjuna khud Shikhandi ko protect kar raha tha taaki woh Bhishma tak pahunch sake.

6. Arjuna ki protection

Arjuna ke peeche:

Yuyudhana (Satyaki)
Yudhamanyu
Uttamaujas
Kekaya brothers
Dhrishtaketu
Chekitana

jaise warriors the.

Yudhamanyu aur Uttamaujas specifically Arjuna ke chariot wheels ke protectors the.

7. Yudhishthira kahaan the?

Yudhishthira ko army ke centre mein rakha gaya.

Unke aas-paas huge elephants the jo moving hills jaise dikh rahe the.

Unke peeche King Drupada/Pancala king Yajnasena apni Akshauhini ke saath tha.

Aur Dhrishtadyumna ne Yudhishthira ki rear protection bhi sambhali.

8. Vajra Vyuha ka basic idea

Text ke according ye formation:

all directions ki taraf face kar sakti thi,
fearless thi,
aur iski protection Arjuna/Gandiva-dhari kar raha tha.

Isliye Pandavon ki army numbers mein chhoti hone ke bawajood ek compact, highly protected formation mein thi.

Simple visual:

                    BHISHMA
                       ↑
                 SHIKHANDI
                    ↑
                  ARJUNA
                    ↑
          YUYUDHANA / SUPPORT
                    ↑
       ┌─────────────────────────┐
       │       DHRISHTADYUMNA    │
       │                          │
       │          BHIMA           │
       │       ⚔ FRONT ⚔         │
       │                          │
       │   NAKULA   SAHADEVA      │
       └─────────────────────────┘
                    ↓
              YUDHISHTHIRA
                    ↓
          DRUPADA / PANCHALA

Note: Yeh diagram text ke strategic relationships ko simplify karke dikhata hai; actual battlefield geometry ko exact map ki tarah nahi samajhna chahiye.

9. Phir battlefield mein supernatural omens

Jab dono armies sunrise ka wait kar rahi thi, tab ajeeb events hone lage:

bina clouds ke thunder suna gaya
paani ki boondein girne lagi
tez dry winds chalne lagi
pointed pebbles hawa ke saath aaye
thick dust ne battlefield ko dark kar diya
meteors east ki taraf gire
rising Sun ki brightness kam ho gayi
Earth tremble hui
Earth kai jagah crack hone lagi
thunder baar-baar sunai diya
warriors ke standards hawa mein violently hilne lage

Aur in sab ke beech Pandav army Vajra formation mein ready khadi thi.

Unki nazar front par khade Bhima par thi.

Core point

Section XIX ka main military idea ye hai:

Kaurav = quantity + 11 Akshauhini

Pandav = smaller force + concentrated Vajra formation + Bhima as shock/front force + Arjuna as key protector + Shikhandi as Bhishma-target + layered protection.
Yaani Pandavon ne numbers ki kami ko formation aur warrior placement se compensate karne ki koshish ki. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.8
        with st.expander("Section 6.3.8  Section XX"):
            text1 = """ Section XX — Kurukshetra ka Pehla Din

Subah hote hi Suraj aasman mein aa gaya.

Dono armies battlefield mein apni-apni jagah khadi thi. Kauravon ki army ko Bhishma lead kar rahe the, aur Pandavon ki army ke aage Bhima khade the.

Dono taraf ke warriors fight ke liye ready the.

Kauravon ki army west ki taraf face karke khadi thi. Pandav east ki taraf.

Dono armies bahut badi aur powerful thi. Har taraf elephants, horses aur chariots hi dikh rahe the.

Lekin ek ajeeb baat hui. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Hawa Pandavon ke peeche se chal rahi thi aur Kauravon ki taraf ja rahi thi. Jungle ke dangerous animals bhi Kauravon ki taraf dekhkar ajeeb aur scary awaazein kar rahe the.

Ye signs Kauravon ke liye achhe nahi maane ja rahe the.

Duryodhana ka roop

Duryodhana ek bade aur powerful elephant par baitha tha.

Elephant ko strong armour se cover kiya gaya tha. Duryodhana ke upar ek safed umbrella tha, jo chaand ki roshni jaisa chamak raha tha.

Uske aas-paas Gandhara ke warriors the. Shakuni bhi uske saath tha.

Army ke bilkul front mein Bhishma khade the.

Unke paas safed ghode the. Unka armour, umbrella, turban aur banner bhi safed tha.

Door se Bhishma ek safed pahaad jaise dikh rahe the.

Unke saath Dhritarashtra ke sabhi bete aur kai bade warriors khade the.

Drona ki position

Bhishma ke peeche Drona apne golden chariot par khade the.

Unke chariot ko laal ghode kheench rahe the.

Drona ke haath mein bow tha. Woh poori army ko peeche se protect kar rahe the.

Jaise Indra apni army ko protect karta hai, waise hi Drona Kauravon ki army ki raksha kar rahe the.

Army ke north side par Kripa apne warriors ke saath khade the.

South side par Kritavarman ki powerful force thi.

Is tarah Bhishma ne army ke har side par strong warriors ko place kiya tha.

Arjuna ke peeche Samshaptakas

Kauravon ne Arjuna ke liye ek special plan bhi banaya tha.

10,000 chariots wale Samshaptakas Arjuna ka peecha karne ke liye ready the.

Unhone decide kiya tha ki woh Arjuna ko tab tak follow karenge jab tak ya to Arjuna marega ya woh khud.

Unke saath Trigarta ke brave warriors bhi the.

Iska matlab tha ki Arjuna ko battlefield mein baar-baar ek dangerous challenge ka saamna karna padega.

Bhishma ki powerful formation

Bhishma bahut experienced commander the.

Woh har din situation ke hisaab se army ki formation badalte the.

Kabhi woh Human formation banate.

Kabhi Celestial formation.

Kabhi Gandharva formation.

Aur kabhi Asura formation.

Unki army mein bahut saare powerful Maharathis the.

Isliye Kauravon ki army samundar ki tarah bahut badi aur scary lag rahi thi.

Lekin Sanjaya ne ek important baat kahi

Dhritarashtra ki army bahut badi thi.

Uske paas soldiers ki sankhya bhi zyada thi.

Phir bhi Sanjaya ko Pandavon ki army bahut powerful aur almost unbeatable lag rahi thi.

Kyun?

Kyunki Pandavon ki army ke saath Krishna aur Arjuna khade the.

Sanjaya ko laga ki un dono ki leadership Pandavon ki chhoti army ko bhi bahut powerful bana rahi thi.

Aur ab...

Dono armies ek-doosre ke saamne khadi thi.

Kurukshetra mein yudh shuru hone wala tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.9
        with st.expander("Section 6.3.9  Section XXI"):
            text1 = """ Section XXI — Yudhishthira ka Dar aur Arjuna ka Bharosa

Jab Yudhishthira ne Kauravon ki bahut badi army ko dekha, toh unke mann mein tension aa gayi.

Bhishma ne ek aisi strong battle formation banayi thi jise dekhkar Yudhishthira ko laga ki ise todna bahut mushkil hoga.

Yudhishthira ka chehra udaas ho gaya.

Unhone Arjuna se kaha,

“Arjuna, hum itni badi army ka saamna kaise karenge?”

“Kauravon ke paas Bhishma jaise mahaan warrior hain. Unhone aisi formation banayi hai jise todna almost impossible lag raha hai.” """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Yudhishthira ko doubt hone laga ki kya Pandav is battle mein jeet paayenge.

Arjuna ne unki baat dhyaan se suni.

Phir Arjuna ne kaha,

“Maharaj, sirf badi army hone se victory nahi milti.”

“Kabhi-kabhi chhoti army bhi badi army ko hara sakti hai.”

Arjuna ne kaha ki is baat ko Rishi Narada, Bhishma aur Drona bhi jaante hain.

Purane samay mein Bhishma ne bhi Indra aur doosre Devas ko yahi baat samjhayi thi.

Victory kiski hoti hai?

Arjuna ne kaha,

“Victory sirf strength aur numbers se nahi milti.”

Jo log truth, kindness, righteousness aur hard work ke saath fight karte hain, unki jeet ke chances zyada hote hain.

Isliye Arjuna ne Yudhishthira se kaha,

“Humein bina ghamand ke fight karna hai.”

“Humein right aur wrong ko samajhna hai.”

“Greed ko side mein rakhkar apna duty karna hai.”

Phir Arjuna ne ek bahut important baat kahi:

“Jahan righteousness hoti hai, wahi victory hoti hai.”

Krishna par Arjuna ka bharosa

Arjuna ko sabse bada bharosa Krishna par tha.

Usne kaha,

“Narada ne bhi kaha hai—jahan Krishna hain, wahi victory hai.”

Krishna ke paas unlimited strength thi.

Woh bade se bade enemy ke saamne bhi bina dare khade reh sakte the.

Arjuna ko yaad tha ki purane samay mein Devas aur Asuras ke beech bhi battle hui thi.

Tab Krishna ke leadership ko follow karne wale Devas victorious hue the.

Krishna ki help se Devas ne teenon worlds par apna control paaya tha.

Isliye Arjuna ne Yudhishthira ko samjhaya:

“Aapko darne ki zarurat nahi hai.”

“Hamare saath Krishna khud hain.”

“Jab Krishna hamare saath hain, toh humein victory ki umeed zaroor rakhni chahiye.”

Yudhishthira ka mann dheere-dheere shaant hone laga.

Unhe samajh aa gaya ki battle jeetne ke liye sirf army ki sankhya nahi, balki righteousness, courage aur sahi leadership bhi zaroori hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.10
        with st.expander("Section 6.3.10  Section XXII"):
            text1 = """ Section XXII — Yudhishthira ne Sena ko Taiyaar Kiya

Yudhishthira ne Bhishma ki army ke saamne apni Pandav sena ko achhe se arrange kiya.

Unhone apne soldiers se kaha:

“Humne apni army ko rules ke according taiyaar kar liya hai. Ab sab log honestly aur courage ke saath fight karo.”

Pandav army ke centre mein Shikhandi apni sena ke saath khade the. Unki protection Arjuna kar rahe the.

Army ke front par Dhrishtadyumna the aur unki protection Bhima kar rahe the.

South side ki protection Yuyudhana kar rahe the. Woh bahut powerful warrior the.

Yudhishthira ka Shandar Rath

Yudhishthira khud apne elephants ke beech ek bahut sundar rath par khade the.

Unke rath par gold aur precious stones se bana hua ek beautiful flag tha.

Unke upar ek pure white umbrella laga tha, jiska handle ivory ka tha.

Bahut saare Rishis unke aas-paas chal rahe the aur unki praise kar rahe the. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Priests aur Rishis mantras aur prayers kar rahe the. Woh Yudhishthira ki victory ke liye blessings de rahe the.

Yudhishthira ne bhi Brahmanas ko cows, fruits, flowers, gold coins aur clothes gift kiye.

Is tarah woh ek great king ki tarah apni army ke saamne khade the.

Arjuna ka Divya Rath

Ab sabki nazar Arjuna ke rath par gayi.

Arjuna ka rath bahut hi magnificent tha.

Usmein hundreds of bells, beautiful gold decoration aur shining wheels the.

Uske saath white horses jude hue the.

Rath itna bright tha ki woh hazaar suns ki tarah chamak raha tha.

Rath ke upar Hanuman ji ka flag laga tha.

Aur rath ki reins khud Krishna ke haath mein thi.

Arjuna apna famous Gandiva bow lekar rath par khade the.

Woh duniya ke greatest archers mein se ek the.

Bhima ko Dekhkar Kaurav Dare

Arjuna ke saath Bhima bhi front par khade the.

Bhima bahut powerful the.

Kaha gaya ki agar Bhima chahein, toh bina weapon ke bhi apne haathon se men, horses aur elephants ko hara sakte the.

Unke saath Nakula aur Sahadeva bhi the.

Bhima ko army ke front par dekhkar Kaurav soldiers ke andar fear aa gaya.

Unhe Bhima ek gusse wale lion jaise dikh rahe the.

Kuch soldiers toh darr ke maare waise hi kaanpne lage jaise koi elephant kichad mein phans kar dar jaata hai.

Krishna ne Arjuna ko Bhishma Dikhaya

Tab Krishna ne Arjuna se kaha:

“Arjuna, dekho. Wahan Bhishma khade hain.”

“Wahi Bhishma jo gusse mein lion ki tarah hamari army par attack karenge.”

“Unhone bahut bade sacrifices kiye hain aur woh Kuru vansh ke greatest warriors mein se ek hain.”

Bhishma ke aas-paas bhi bahut saare powerful warriors khade the.

Krishna ne Arjuna se kaha:

“Pehle in soldiers ko defeat karo. Phir Bhishma ka saamna karo.”

Ab dono armies ready thi.

Battle shuru hone wali thi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.11
        with st.expander("Section 6.3.11  Section XXIII"):
            text1 = """ Section XXIII — Arjuna ne Maa Durga se Prarthana Ki

Battle shuru hone wali thi. Kaurav army saamne aa chuki thi.

Tab Krishna ne Arjuna se kaha:

“Arjuna, battle se pehle apne mann ko shaant karo. Maa Durga ki prarthana karo aur unka ashirwad lo.”

Arjuna turant apne rath se neeche utare. Unhone apne haath jod liye aur pure mann se Maa Durga ko yaad kiya.

Arjuna ne kaha:

“Hey Maa Durga, main aapko pranam karta hoon. Aap sabki raksha karne wali hain. Aap apne bhakton ki madad karti hain.”

“Aap Mahakali hain. Aap dushton ko haraane wali hain. Aapke paas shakti, courage aur victory dene ki power hai.”

Arjuna ne Maa ko unke kai roopon ke naam se yaad kiya.

Unhone kaha: """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Hey Maa, aap Uma hain, Kali hain, Mahakali hain aur Shakambhari hain. Aap hi knowledge hain, aap hi strength hain aur aap hi protection hain.”

“Mujhe battle mein sahi raasta dikhaiye. Mujhe courage dijiye. Aapki kripa se mujhe victory mile.”

Arjuna ki prayer bahut sincere thi.

Maa Durga ka Aashirwad

Arjuna ki devotion dekhkar Maa Durga aakash mein prakat hui.

Unhone Arjuna ko dekha aur kaha:

“Hey Pandava, tum bahut jaldi apne enemies ko defeat karoge.”

“Tumhare saath Narayana khud hain. Isliye tumhe koi hara nahi sakta. Tumhe Indra bhi defeat nahi kar sakte.”

Itna kehkar Maa Durga antardhaan ho gayi.

Arjuna ko Maa ka ashirwad mil chuka tha.

Unka confidence aur strong ho gaya.

Woh wapas apne rath par chadh gaye.

Krishna Aur Arjuna Ke Shankh

Ab Krishna aur Arjuna ek hi rath par khade the.

Dono ne apne divine conches bajaye.

Unki awaaz poore battlefield mein goonj uthi.

Kaurav aur Pandav dono samajh gaye ki ab maha-yuddh shuru hone wala hai.

Sanjaya ne Dhritarashtra se kaha:

“Jahan righteousness hai, wahan glory aur prosperity hoti hai.”

“Aur jahan Krishna hain, wahan victory hoti hai.”

Kauravon ko bahut baar samjhaya gaya tha ki woh galat raasta chhod dein.

Lekin Duryodhana ne kisi ki baat nahi maani.

Ab samay aa gaya tha ki unke decisions ka result saamne aaye.

Jahan Dharma hai, jahan Krishna hain — wahi asli Vijay hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.12
        with st.expander("Section 6.3.12  Section XXIV"):
            text1 = """ Section XXIV — Yudh Ki Shuruaat

Dhritarashtra bahut chintit the. Unhone Sanjaya se poocha:

“Sanjaya, battlefield mein sabse pehle kis army ne attack kiya? Kaurav ya Pandav?”

“Kis side ke warriors zyada confident the? Aur kis side ke warriors fear ya sadness se weak ho gaye the?”

“Aur batao, dono armies mein se kiski garlands aur perfumes ki khushboo zyada aa rahi thi?”

Sanjaya ne jawab diya:

“Maharaj, us waqt dono armies ke warriors confident the.”

Dono taraf ke soldiers ne beautiful flower garlands pehni hui thi. Unke body par fragrant perfumes bhi lage hue the. Dono armies se almost same sweet fragrance aa rahi thi.

Phir dono armies ek-doosre ke bilkul saamne aa gayi.

Yudh ab shuru hone wala tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Achaanak battlefield mein bahut zor ka noise hone laga.

Conches bajne lage.

Drums zor-zor se bajne lage.

Warriors ek-doosre ko challenge karte hue zor se roar karne lage.

Elephants bhi zor-zor se garajne lage.

Dono armies ke soldiers excitement aur courage se ek-doosre ko dekh rahe the.

Phir dono armies ki lines aapas mein takra gayi.

Battlefield ka scene bahut hi fierce ho gaya.

Har taraf conches, drums, elephants aur warriors ki awaaz goonj rahi thi.

Aur isi ke saath Kurukshetra ka maha-yuddh sach mein shuru ho gaya. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.13
        with st.expander("Section 6.3.13  Section XXV (Bhagavad Gita Chapter I)"):
            text1 = """ Section XXV — Arjuna Ka Moh Aur Yudh Se Peeche Hatna

Kurukshetra mein dono armies saamne khadi thi.

Dhritarashtra ne Sanjaya se poocha:

“Sanjaya, mere bete aur Pandav yudh ke liye saamne aa gaye hain. Ab kya hua?”

Sanjaya ne batana shuru kiya.

Duryodhana Ne Drona Se Baat Ki

Duryodhana ne Pandavon ki huge army dekhi.

Woh turant apne guru Drona ke paas gaya aur bola:

“Guruji, dekhiye Pandavon ki kitni badi army hai.”

“Is army ko Dhrishtadyumna ne arrange kiya hai. Woh aapka hi student hai.”

Duryodhana ne Pandav side ke powerful warriors ke naam ginaye. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Usne Bhima, Arjuna, Yuyudhana, Virata, Drupada, Dhrishtaketu, Chekitana, Kashiraj, Yudhamanyu, Uttamauja, Abhimanyu aur Draupadi ke sons ka naam liya.

Phir Duryodhana ne apni army ke great warriors ka bhi naam liya.

Drona, Bhishma, Karna, Kripa, Ashwatthama, Vikarna aur Jayadratha jaise bade warriors uski side mein the.

Duryodhana ne kaha:

“Hamari army Bhishma ki protection mein hai. Isliye sab log apni jagah sambhalo aur Bhishma ki protection karo.”

Yudh Ka Shankhnaad

Tab Bhishma ne zor se lion ki tarah roar kiya.

Phir unhone apna conch bajaya.

Uske baad Kaurav army mein conches, drums aur horns ek saath bajne lage.

Poora battlefield awaaz se bhar gaya.

Phir Krishna aur Arjuna ne bhi apne divine conches bajaye.

Krishna ne Panchajanya bajaya.

Arjuna ne Devadatta bajaya.

Bhima ne apna huge conch Paundra bajaya.

Yudhishthira ne Anantavijaya bajaya.

Nakula ne Sughosha aur Sahadeva ne Manipushpaka bajaya.

Pandav side ke baaki great warriors ne bhi apne conches bajaye.

Unki awaaz itni powerful thi ki Kaurav soldiers ke hearts mein fear bhar gaya.

Arjuna Ne Krishna Se Kaha

Ab actual battle start hone wali thi.

Arjuna ne apna Gandiva bow uthaya aur Krishna se kaha:

“Krishna, mera rath dono armies ke beech mein le chalo.”

“Main dekhna chahta hoon ki mere saamne kaun-kaun fight karne ke liye khada hai.”

Krishna ne Arjuna ki baat maani.

Unhone rath ko dono armies ke beech mein laakar khada kar diya.

Krishna ne kaha:

“Arjuna, dekho. Saamne tumhare apne Kuru warriors khade hain.”

Arjuna Ne Apno Ko Dekha

Arjuna ne saamne dekha.

Usne sirf enemies nahi dekhe.

Usne apne grandfather Bhishma ko dekha.

Apne guru Drona ko dekha.

Usne apne relatives, friends, cousins, uncles, sons aur doosre apne logon ko bhi dekha.

Dono armies mein uske apne hi log khade the.

Yeh dekhkar Arjuna ka heart heavy ho gaya.

Uska body kaanpne laga.

Uska mouth dry ho gaya.

Uske baal khade ho gaye.

Uska Gandiva haath se slip hone laga.

Arjuna ne Krishna se kaha:

“Krishna, main in apne logon ke against kaise fight kar sakta hoon?”

“Mujhe victory, kingdom ya pleasures nahi chahiye, agar unke liye mujhe apne hi family members ko maarna pade.”

Arjuna Ka Dard

Arjuna bola:

“Jinke liye hum kingdom aur happiness chahte hain, wahi log aaj mere saamne khade hain.”

“Mere teachers, elders, relatives, friends aur family members.”

“Agar mujhe poori duniya ka kingdom bhi mil jaye, tab bhi main apno ko maarna nahi chahta.”

Arjuna ko laga ki apne relatives ko maarna paap hoga.

Usne Krishna se kaha:

“Agar woh mujhe maar bhi dein, main unhe maarna nahi chahta.”

Arjuna ko darr tha ki family members ke marne se family traditions aur values khatam ho jayengi.

Uske hisaab se family tootne par society mein problems badhengi aur purane rituals bhi khatam ho jayenge.

Phir Arjuna ne kaha:

“Krishna, mujhe lagta hai hum ek bahut bada wrong kaam karne ja rahe hain.”

“Main apne hi relatives ko maar kar kingdom nahi chahta.”

Arjuna Ne Gandiva Rakh Diya

Itna kehkar Arjuna bahut dukhi ho gaya.

Uska mind completely confused tha.

Usne apna Gandiva bow aur arrows neeche rakh diye.

Phir woh apne rath par baith gaya.

Arjuna ne yudh karne se mana kar diya.

Yahin se Bhagavad Gita ki sabse important conversation shuru hoti hai — Arjuna ke confusion aur Krishna ke teachings ki. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.14
        with st.expander("Section 6.3.14  Section XXVI (Bhagavad Gita Chapter II)"):
            text1 = """ Arjuna battlefield mein apna bow neeche rakh chuka tha.

Uski aankhon mein aansu the.
Uska mind confusion aur sadness se bhar gaya tha.

Krishna ne Arjuna ko dekha aur kaha:

“Arjuna, tum itne dukhi kyun ho? Yeh weakness tumhare liye theek nahi hai. Apna courage wapas lao aur khade ho jao.”

Arjuna ne kaha:

“Krishna, main Bhishma aur Drona jaise apne elders aur gurus ke against kaise fight kar sakta hoon?”

“Agar unhe maar kar mujhe kingdom bhi mil jaye, toh woh happiness mere liye kya meaning rakhegi?” """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Arjuna bahut confused tha.

Usne Krishna se kaha:

“Mujhe samajh nahi aa raha ki mere liye kya right hai. Ab aap hi mujhe batao. Main aapka disciple hoon.”

Phir Arjuna ne kaha:

“Mujhe aisa koi solution nahi dikh raha jo mere is grief ko khatam kar sake. Chahe mujhe poori duniya ka kingdom mil jaye, ya gods ka kingdom bhi, mera dukh door nahi hoga.”

Phir Arjuna ne clearly kaha:

“Krishna, main fight nahi karunga.”

Aur woh chup ho gaya.

Krishna Ne Atma Ka Gyaan Diya

Krishna calmly bole:

“Arjuna, tum un logon ke liye dukhi ho jinke liye wise person ko dukhi nahi hona chahiye.”

“Wise person na living logon ke liye unnecessarily dukhi hota hai, na dead logon ke liye.”

Krishna ne samjhaya:

“Body change hoti rehti hai. Childhood ke baad youth aata hai, phir old age. Isi tarah death ke baad Atma ek naya body leti hai.”

“Isliye ek wise person in changes se confuse nahi hota.”

Arjuna ko samjhate hue Krishna bole:

“Life mein happiness aur pain, heat aur cold jaise experiences aate-jaate rehte hain.”

“Inka beginning aur ending hota hai. Isliye inhe patience ke saath handle karo.”

Atma Kabhi Destroy Nahi Hoti

Krishna ne kaha:

“Arjuna, Atma eternal hai.”

“Usse koi destroy nahi kar sakta.”

“Body ek din khatam hoti hai, lekin Atma khatam nahi hoti.”

Krishna ne ek simple example diya:

“Jaise koi person purane clothes hata kar new clothes pehenta hai, waise hi Atma old body chhodkar new body leti hai.”

Weapons Atma ko cut nahi kar sakte.

Fire use burn nahi kar sakti.

Water use wet nahi kar sakta.

Wind use dry nahi kar sakti.

Atma permanent hai.

Isliye Krishna bole:

“Arjuna, jo eternal hai uske liye itna grief mat karo.”

Apna Duty Karo

Krishna ne Arjuna ko uska duty yaad dilaya.

“Tum ek Kshatriya ho. Tumhare liye ek fair aur righteous battle se badhkar koi duty nahi hai.”

“Agar tum justice ke liye hone wali is fight se peeche hatoge, toh tum apna duty chhod doge.”

“Log tumhari courage par question karenge. Tumhare enemies tumhara mazaak banayenge.”

Krishna ne kaha:

“Agar tum battle mein maroge, toh heaven milega. Aur agar jeetoge, toh Earth par kingdom milega.”

Phir Krishna ne sabse important baat kahi:

“Pleasure aur pain ko equal samjho.”

“Gain aur loss ko equal samjho.”

“Victory aur defeat ko bhi equal samjho.”

“Apna duty karo, lekin result ki attachment mat rakho.”

Karma Ka Secret

Krishna ne Arjuna ko Yoga ka ek important lesson diya:

“Tumhara right action karne par hai, result par nahi.”

Matlab:

Kaam honestly karo.
Result ke peeche mat bhaago.
Aur failure ke fear se kaam karna mat chhodo.

Jo person sirf result ke liye kaam karta hai, woh hamesha tension mein rehta hai.

Lekin jo person apna best effort deta hai aur result ko accept karta hai, uska mind peaceful rehta hai.

Krishna ne kaha:

“Success aur failure mein same rehna hi Yoga hai.”

Steady Mind Wala Person

Arjuna ne poocha:

“Krishna, ek aise person ki pehchaan kya hai jiska mind truly stable hai?”

Krishna bole:

“Jab person unnecessary desires ko chhod deta hai aur apne andar hi satisfied rehta hai, tab uska mind steady hota hai.”

Aisa person:

Problems mein panic nahi karta.
Happiness mein over-excited nahi hota.
Anger aur fear ko control karta hai.
Har situation mein balanced rehta hai.
Apni senses ko control mein rakhta hai.

Krishna ne tortoise ka example diya.

Jaise tortoise danger aane par apne legs aur head ko shell ke andar le leta hai, waise hi wise person apni senses ko control kar leta hai.

Attachment Se Anger Tak

Krishna ne ek important chain samjhayi:

Sense objects ke baare mein baar-baar sochne se attachment hoti hai.

Attachment se desire badhti hai.

Desire poori na ho toh anger aata hai.

Anger se discrimination weak hoti hai.

Discrimination weak hone se memory aur understanding disturb hoti hai.

Aur jab understanding chali jaati hai, toh person apna direction kho deta hai.

Isliye Krishna kehte hain:

“Apne mind aur senses ko control karo.”

Real Peace

Jo person apni senses ko control karta hai, attachment aur hatred se free rehta hai, uska mind peaceful ho jaata hai.

Aur peaceful mind mein clarity aati hai.

Aisa person difficult situations mein bhi stable rehta hai.

Krishna ne end mein kaha:

“Jab tum desires ke peeche bhaagna chhod doge, attachment aur pride ko chhod doge aur peaceful mind ke saath jeeyoge, tab tum divine state ko achieve karoge.”

“Is state ko paane ke baad person easily confuse nahi hota.”

Yahi Krishna ne Arjuna ko samjhaya:

Atma eternal hai.
Duty se bhaagna nahi hai.
Action karo, result ki attachment chhodo.
Aur har situation mein apna mind balanced rakho. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.15
        with st.expander("Section 6.3.15  Section XXVII (Bhagavad Gita Chapter III)"):
            text1 = """ Section XXVII — Karma Yoga: Apna Karma Karo

Arjuna abhi bhi confused tha.

Usne Krishna se poocha:

“Krishna, agar knowledge aur devotion itne important hain, toh phir aap mujhe itni difficult action wali situation mein kyun daal rahe ho?”

“Mujhe clearly batao ki mere liye kya sahi hai.”

Krishna ne calmly kaha:

“Arjuna, duniya mein log spiritual progress ke do main raaste follow karte hain.”

“Ek raasta knowledge ka hai.”

“Aur doosra raasta selfless action ka hai.”

Lekin Krishna ne ek important baat samjhayi:

“Koi bhi person bina action ke nahi reh sakta.”

Har insaan kuch na kuch karta hi rehta hai. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Sirf bahar se kaam chhod dena enough nahi hai.

Agar koi person kaam toh nahi karta, lekin mind mein constantly worldly desires ke baare mein sochta rehta hai, toh woh actually free nahi hai.

Lekin jo person apne mind ko control karke bina attachment ke apna duty karta hai, woh truly better path par hai.

Krishna bole:

“Isliye action se bhaago mat. Apna duty sincerely karo.”

Karma Kisliye Karna Chahiye?

Krishna ne kaha:

“Aisa kaam karo jo sirf tumhare personal benefit ke liye na ho.”

Purane time mein Creation ke Lord ne humans ko Yajna, yani selfless offering, ke saath create kiya tha.

Unhone kaha tha:

“Tum ek doosre ki help karo. Tumhare actions se society aur nature dono grow karein.”

Jaise nature hume food, water aur resources deti hai, waise hume bhi apna contribution dena chahiye.

Jo person sirf leta hai aur kabhi contribute nahi karta, woh selfish hai.

Isliye Krishna kehte hain:

“Jo kuch bhi karo, gratitude aur responsibility ke saath karo.”

Karma Ka Ek Cycle

Krishna ne ek simple cycle samjhayi:

Work se Yajna hota hai.

Yajna se nature ka balance bana rehta hai.

Nature se rain aur food milta hai.

Food se living beings survive karte hain.

Aur living beings phir apna work karte hain.

Is tarah sab kuch ek doosre se connected hai.

Jo person is cycle mein apna contribution nahi deta aur sirf apni enjoyment ke baare mein sochta hai, woh apni life waste karta hai.

Lekin Wise Person Ko Bhi Kaam Kyun Karna Chahiye?

Arjuna ke liye ek interesting question tha.

Agar koi person spiritually complete ho gaya hai, toh usse kaam karne ki zarurat kyun hai?

Krishna ne kaha:

“Wise person ko bhi work karna chahiye.”

King Janaka jaise great leaders ne bhi action ke through apna goal achieve kiya tha.

Aur ek important reason tha.

Common people great people ko follow karte hain.

Agar ek great person responsibility se bhaagega, toh doosre bhi wahi karenge.

Krishna ne kaha:

“Main khud bhi action karta hoon, even though mujhe personally kuch achieve karna baaki nahi hai.”

“Agar main action karna chhod doon, toh log bhi apna duty chhod sakte hain.”

Isliye Krishna khud bhi continuously action karte hain.

Wise Person Kaise Kaam Karta Hai?

Krishna ne Arjuna ko samjhaya:

“Wise person bhi work karta hai, lekin attachment ke bina.”

Ek normal person sochta hai:

“Maine ye kiya.”

“Mujhe iska result chahiye.”

“Mujhe credit milna chahiye.”

Lekin wise person samajhta hai ki actions nature aur body ke through hote hain.

Isliye woh ego mein nahi aata.

Woh apna kaam karta hai aur result ko unnecessarily apne ego se attach nahi karta.

Doosron Ko Confuse Mat Karo

Krishna ne ek aur important lesson diya:

Agar koi person abhi spiritually mature nahi hai, toh usse suddenly yeh kehna ki “kuch mat karo” usko confuse kar sakta hai.

Wise person ko khud example set karna chahiye.

Khud sincerely kaam karo.

Aur doosron ko bhi unke duties sincerely karne ke liye encourage karo.

Apna Duty Sabse Important Hai

Krishna ne kaha:

“Har person ka apna duty hota hai.”

Apna duty imperfectly karna bhi better hai than kisi doosre ka duty perfectly karna.

“Apna raasta follow karo.”

“Doosron ko dekhkar apna duty mat badlo.”

Kyuki doosre ka path tumhare liye natural nahi ho sakta.

Isliye apni responsibility se bhaagna nahi chahiye.

Arjuna Ka Important Question

Arjuna ne phir poocha:

“Krishna, kabhi-kabhi insaan galat kaam karna nahi chahta, phir bhi woh galat kaam kyun kar deta hai?”

Krishna ne jawab diya:

“Uska sabse bada enemy hai — desire.”

Jab desire control se bahar ho jaati hai aur poori nahi hoti, toh wahi anger ban jaati hai.

Desire aur anger dono insaan ke knowledge ko cover kar dete hain.

Krishna ne iska example diya:

Jaise smoke fire ko cover kar deta hai.

Jaise dust mirror ko dirty kar deta hai.

Waise hi desire knowledge ko cover kar deti hai.

Desire Ko Kaise Control Karein?

Krishna ne kaha:

“Sabse pehle apni senses ko control karo.”

Uske baad mind ko control karo.

Phir understanding ko strong banao.

Aur finally apne higher self ko samjho.

Krishna ne kaha:

“Tumhari senses se upar mind hai.”

“Mind se upar understanding hai.”

“Aur understanding se bhi upar Supreme Self hai.”

Isliye apne andar ki strength ko jagao.

Desire ko apne upar control mat karne do.

Krishna Ka Final Message

Krishna ne Arjuna se kaha:

“Desire tumhara difficult enemy hai.”

“Use control karo.”

“Apna duty karo.”

“Kaam se bhaago mat.”

“Result ki attachment mat rakho.”

“Aur apne actions ko selfless banao.”

Yahi Karma Yoga ka simple lesson hai:

Kaam karo, lekin sirf apne benefit ke liye nahi.

Apni responsibility nibhao, bina ego aur unnecessary desire ke.

Jab insaan apne karma ko sahi intention ke saath karta hai, toh wahi karma uski spiritual growth ka raasta ban jaata hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.16
        with st.expander("Section 6.3.16  Section XXVIII (Bhagavad Gita Chapter IV)"):
            text1 = """ Section XXVIII — Jnana Karma Yoga: Knowledge Aur Karma Ka Raaz

Kurukshetra ke battlefield mein Krishna Arjuna ko ek bahut purani baat batane lage.

Krishna bole:

“Ye knowledge koi nayi baat nahi hai.”

Sabse pehle maine ye sacred knowledge Vivasvat ko diya tha.

Vivasvat ne ise Manu ko bataya.

Manu ne ise Ikshaku ko diya.

Aise ye knowledge generations tak chalta raha.

Lekin bahut samay beetne ke baad duniya mein ye knowledge dheere-dheere lost ho gaya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Ab main wahi ancient knowledge tumhe bata raha hoon, Arjuna.”

“Tum mere devotee bhi ho aur mere friend bhi.”

Arjuna ko ye baat strange lagi.

Usne poocha:

“Krishna, aapka birth toh Vivasvat ke baad hua tha. Phir aapne Vivasvat ko ye knowledge kaise diya?”

Krishna muskuraye aur bole:

Krishna Ke Janmon Ka Raaz

“Arjuna, mere aur tumhare bahut saare births ho chuke hain.”

“Mujhe apne sabhi births yaad hain.”

“Lekin tumhe apne previous births yaad nahi hain.”

Krishna ne kaha:

“Main normally unborn hoon.”

Lekin jab duniya mein dharma kam hone lagta hai aur adharma badhne lagta hai, tab Krishna apni divine power se appear hote hain.

Unka purpose hota hai:

Achhe logon ki protection karna.
Evil ko rokna.
Dharma ko dobara establish karna.

Isliye Krishna kehte hain:

“Jab-jab dharma weak hota hai, main baar-baar aata hoon.”

Jo person Krishna ke divine birth aur actions ko truly samajh leta hai, woh spiritual freedom ki taraf badhta hai.

Krishna Sabko Accept Karte Hain

Krishna ne Arjuna se kaha:

“Log jis bhi sincere way se mere paas aate hain, main unhe usi way se accept karta hoon.”

Koi devotion se aata hai.

Koi knowledge se.

Koi selfless work se.

Lekin sincere intention important hai.

Karma Ka Raaz

Krishna ne kaha:

“Action kya hai aur inaction kya hai, ye samajhna easy nahi hai.”

Even intelligent people bhi kabhi-kabhi ismein confuse ho jaate hain.

Isliye person ko teen cheezein samajhni chahiye:

Kya karna hai.

Kya nahi karna hai.

Aur kab action se bhi beyond jaana hai.

Wise person woh hai jo action ke beech bhi inner peace dekhta hai.

Aur action karte hue bhi result ki unnecessary desire nahi rakhta.

Selfless Action

Krishna ne kaha:

“Jo person apne actions ke result se attached nahi hota, woh actually free rehta hai.”

Woh kaam karta hai.

Lekin har baar ye nahi sochta:

“Mujhe iske badle kya milega?”

Aise person ka mind peaceful rehta hai.

Woh success aur failure ko bhi calmly accept karta hai.

Uske liye dono situations life ka part hain.

Yajna Ke Alag-Alag Forms

Krishna ne bataya ki sacrifice sirf ek particular ritual nahi hai.

Log alag-alag ways mein sacrifice karte hain.

Koi apna wealth donate karta hai.

Koi meditation karta hai.

Koi study aur learning ko sacrifice ke roop mein karta hai.

Koi apni senses ko control karta hai.

Koi apni breathing aur body ko discipline karta hai.

Aur koi sabse important sacrifice karta hai:

Knowledge ka sacrifice.

Knowledge Sabse Powerful Hai

Krishna ne kaha:

“Knowledge ka sacrifice bahut powerful hai.”

Kyuki jab true knowledge mil jaata hai, toh person apne actions ko sahi way mein samajhne lagta hai.

Jaise ek strong fire wood ko ashes mein badal deti hai, waise hi knowledge ka fire past actions ke effects ko destroy kar sakta hai.

Isliye Krishna kehte hain:

“Knowledge se zyada purifying cheez kuch nahi hai.”

Knowledge Kaise Milegi?

Krishna ne Arjuna ko ek simple way bataya:

Seekho.

Questions poochho.

Respect ke saath knowledgeable logon se guidance lo.

Aur jo seekho, use life mein apply karo.

Jab person sincere hota hai, faith rakhta hai aur apni senses ko control karta hai, toh dheere-dheere usse true knowledge milta hai.

Aur knowledge ke saath inner peace aati hai.

Doubt Sabse Bada Problem Hai

Krishna ne kaha:

“Jiske mind mein constant doubt hai, woh na properly progress kar pata hai aur na peace paata hai.”

Doubt person ko andar se weak kar deta hai.

Isliye Arjuna ko apne confusion ko knowledge se remove karna tha.

Krishna ne kaha:

“Tumhare mind mein jo ignorance se paida hua doubt hai, use knowledge ki sword se cut karo.”

“Apne duty ke path par wapas aao.”

“Aur khade ho jao, Arjuna.”

Is Chapter Ka Simple Lesson

Krishna Arjuna ko samjha rahe the:

Karma karo, lekin attachment ke bina.

Knowledge seekho.

Questions poochho.

Apne doubts ko clear karo.

Apni senses ko control karo.

Aur sabse important—

Dharma ke raaste par chal kar apni responsibility nibhao.

Kyuki right knowledge + selfless action + faith insaan ko inner peace aur spiritual freedom ki taraf le jaate hain. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.17
        with st.expander("Section 6.3.17  Section XXIX (Bhagavad Gita Chapter V)"):
            text1 = """ Section XXIX — Karma Yoga aur Sannyasa: Kaam Karte Hue Bhi Freedom

Kurukshetra mein Arjuna ke mind mein ek aur question aaya.

Arjuna ne Krishna se poocha:

“Krishna, kabhi aap actions ko chhodne ki baat karte ho, aur kabhi action karne ko kehte ho. In dono mein better kya hai?”

Krishna ne calmly jawab diya:

“Arjuna, dono paths freedom ki taraf le ja sakte hain.”

Lekin Krishna ne kaha:

“Action ko completely chhod dene se better hai ki tum action karo, lekin """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ attachment ke bina.”

Sacha Sannyasi Kaun Hai?

Krishna ne samjhaya:

“Sannyasi woh nahi jo sirf kaam chhod deta hai.”

Sacha sannyasi woh hai jo:

Kisi se unnecessary hatred nahi rakhta.
Har cheez ki excessive desire nahi karta.
Success aur failure mein balanced rehta hai.
Apne mind aur senses ko control karta hai.

Aisa person action karte hue bhi free reh sakta hai.

Krishna ne kaha:

“Sankhya aur Yoga ko alag samajhna mistake hai.”

Knowledge ka path aur selfless action ka path, dono ka ultimate goal ek hi hai.

Action Karo, Lekin Attachment Mat Rakho

Krishna ne Arjuna ko ek beautiful example diya.

“Jaise lotus leaf paani mein rehta hai, lekin paani usse chipakta nahi…”

Waise hi ek wise person duniya mein rehkar kaam karta hai, lekin attachment ko apne mind par control nahi karne deta.

Woh kaam karta hai.

Lekin kaam ke result ko apni happiness ka source nahi banata.

“Main Kuch Nahi Kar Raha”

Krishna kehte hain ki truly wise person andar se samajhta hai:

“Main actually kuch nahi kar raha.”

Jab woh dekhta hai, sunta hai, touch karta hai, khana khata hai, walk karta hai, sota hai ya bolta hai—

woh samajhta hai ki ye sab body aur senses ke natural actions hain.

Uska inner self un actions se alag hai.

Result Ki Desire Se Freedom

Jo person apne actions ka result Bhagwan ko dedicate karta hai aur attachment chhod deta hai, uska mind gradually pure hota hai.

Lekin jo har action ke badle result chahta hai—

“Mujhe ye milega kya?”

woh apne hi desires ke trap mein phas jaata hai.

Isliye Krishna kehte hain:

“Action karo, lekin result ke attachment ko chhod do.”

Sabke Liye Equal Respect

Knowledge milne ke baad ek wise person sabhi living beings ko equality se dekhta hai.

Woh ek learned Brahmana ko bhi respect se dekhta hai.

Ek cow ko bhi.

Ek elephant ko bhi.

Ek dog ko bhi.

Aur society ke lowest position par khade person ko bhi.

Uske liye sabke andar ek hi Supreme presence hai.

Real Happiness Kahan Hai?

Krishna ne kaha:

“Jo happiness sirf outside objects se milti hai, woh permanent nahi hoti.”

Aaj koi cheez achhi lagti hai.

Kal wahi boring ho sakti hai.

Aaj success milti hai.

Kal failure aa sakta hai.

Isliye wise person apni happiness ko outside world par depend nahi karta.

Woh apne andar peace find karta hai.

Jiska mind steady hai, woh pleasant cheez milne par over-excited nahi hota.

Aur unpleasant cheez aane par completely टूटता bhi nahi.

Desire Aur Anger Ko Control Karna

Krishna ne Arjuna se kaha:

“Jo person apne desire aur anger ko control kar leta hai, woh real happiness pa sakta hai.”

Desire aati hai.

Phir desire puri na ho toh anger aa sakta hai.

Anger mind ko disturb karta hai.

Isliye person ko apne mind ko train karna chahiye.

Body ko control karna enough nahi hai.

Mind ko control karna bhi zaroori hai.

Sabke Hit Mein Kaam Karna

Jo person apne sins aur doubts se free ho jaata hai, apne senses ko control karta hai aur sabhi creatures ke welfare ke liye kaam karta hai, woh higher spiritual state ko attain karta hai.

Uske andar desire aur anger gradually kam hote jaate hain.

Uska mind peaceful hota hai.

Aur woh apne true self ko samajhne lagta hai.

Meditation Aur Inner Peace

Krishna ne meditation ka bhi simple idea diya.

Person ko external distractions se apna mind hataana chahiye.

Mind ko calm karna chahiye.

Breathing ko steady karna chahiye.

Senses aur thoughts ko control karna chahiye.

Desire, fear aur anger ko gradually release karna chahiye.

Aisa person inner freedom ki taraf badhta hai.

Aur phir Krishna ne sabse important baat kahi:

“Main sabhi sacrifices aur spiritual practices ka ultimate enjoyer hoon.”

“Main sabhi worlds ka Lord hoon.”

“Aur main har living being ka friend hoon.”

Jo person Krishna ko is tarah samajh leta hai, usse real tranquillity—sachchi inner peace—milti hai.

Simple Lesson

Is chapter ka message simple hai:

Kaam chhodna hi freedom nahi hai.

Kaam karte hue attachment chhodna real freedom hai.

Apna duty karo.

Result ki unnecessary desire mat rakho.

Sabko equality se dekho.

Desire aur anger ko control karo.

Aur apni happiness ko sirf outside world par depend mat karo.

Jab mind andar se peaceful ho jaata hai, tab insaan duniya mein rehkar bhi free ho sakta hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.18
        with st.expander("Section 6.3.18  Section XXX (Bhagavad Gita Chapter VI)"):
            text1 = """ Section XXX — Dhyana Yoga: Mind Ko Control Karne Ka Raasta

Krishna ne Arjuna ko bataya ki real renunciation ka matlab kaam chhod dena nahi hai.

Jo person apna duty karta hai, lekin result ki expectation nahi rakhta, wahi true renouncer aur true yogi hai.

Sirf fire rituals chhod dena ya kaam na karna renunciation nahi hai.

Apna Mind Apna Friend Hai

Krishna bole:

“Arjuna, insaan ko khud apne aap ko upar uthana chahiye. Khud ko neeche nahi girana chahiye.”

Sabse important cheez hai mind.

Agar mind control mein hai, toh woh tumhara friend hai.

Agar mind control mein nahi hai, toh wahi tumhara enemy ban jaata hai. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Jo person apne mind ko control kar leta hai, woh difficult situations mein bhi peaceful rehta hai.

Uske liye:

Heat aur cold same hain.
Pleasure aur pain same hain.
Honour aur insult bhi same hain.

Woh har situation mein balanced rehta hai.

Wise Person Sabko Equal Dekhta Hai

Ek true yogi sabhi logon ko equality se dekhta hai.

Friend ho ya enemy.

Apna ho ya stranger.

Koi uski help kare ya oppose kare.

Good person ho ya bad person.

Woh sabke andar ek hi divine presence ko dekhta hai.

Uske liye gold, stone aur mitti mein bhi excessive attachment nahi hoti.

Meditation Kaise Karein?

Krishna ne Arjuna ko meditation ka simple method bataya.

Ek clean aur quiet place choose karo.

Bahut high ya bahut low seat na ho.

Comfortably baitho.

Body, head aur neck ko straight rakho.

Mind ko ek point par focus karo.

Idhar-udhar baar-baar mat dekho.

Apne senses ko calm karo.

Fear ko side karo.

Aur apna mind Krishna par focus karo.

Aise regularly practice karne se mind gradually peaceful hone lagta hai.

Balance Bahut Zaroori Hai

Krishna ne ek important baat kahi:

“Yoga extreme logon ke liye nahi hai.”

Jo bahut zyada khata hai, uske liye bhi yoga difficult hai.

Jo bilkul khana chhod deta hai, uske liye bhi.

Jo bahut zyada sota hai, uske liye bhi.

Jo bilkul sleep nahi karta, uske liye bhi.

Isliye life mein balance zaroori hai.

Food mein balance.

Sleep mein balance.

Work mein balance.

Rest mein balance.

Entertainment mein bhi balance.

Jab lifestyle balanced hoti hai, tab mind ko control karna easier ho jaata hai.

Mind Ek Lamp Ki Tarah

Krishna ne ek beautiful example diya.

Jaise hawa se protected place mein rakha hua lamp stable rehta hai aur flicker nahi karta, waise hi controlled mind bhi stable ho jaata hai.

Meditation se mind dheere-dheere quiet hota hai.

Phir person ko ek aisi happiness milti hai jo external objects se nahi milti.

Ye happiness andar se aati hai.

Aur jab person ise experience karta hai, toh heavy problems bhi usse easily shake nahi kar paati.

Mind Baar-Baar Bhatkega

Arjuna ke liye ye sab sunna easy tha, lekin practical karna difficult.

Usne kaha:

“Krishna, mind bahut restless hai.”

“Ye noisy hai, stubborn hai aur baar-baar idhar-udhar bhaagta hai.”

“Mujhe lagta hai ise control karna hawa ko rokne jaisa difficult hai.”

Krishna ne agree kiya:

“Haan Arjuna, mind ko control karna difficult hai.”

Lekin impossible nahi hai.

Krishna ne do important tools bataye:

Practice.

Desire ko gradually chhodna.

Agar person regularly practice kare aur unnecessary desires ko control kare, toh mind slowly stable ho sakta hai.

Agar Yogi Beech Mein Fail Ho Jaye Toh?

Arjuna ne ek aur important question poocha:

“Krishna, agar koi person faith ke saath yoga start kare, lekin successful hone se pehle hi uska mind bhatak jaye, toh uska kya hoga?”

“Kya uski saari mehnat waste ho jaati hai?”

Krishna ne kaha:

“Nahi, bilkul nahi.”

Jo person sincerely good path par chalta hai, uska effort kabhi completely waste nahi hota.

Agar woh apni spiritual journey complete nahi kar pata, toh bhi uski progress continue hoti hai.

Usse future mein ek achha environment aur achhe circumstances mil sakte hain.

Woh dobara spiritual knowledge ki taraf attract hota hai.

Aur purani practice uski help karti hai.

Isliye spiritual journey mein failure bhi final failure nahi hota.

Practice Kabhi Waste Nahi Hoti

Krishna kehte hain:

“Jo person sincerely effort karta hai, woh eventually progress karta hai.”

Chahe usse time lage.

Chahe ek life mein complete na ho.

Uski practice aur knowledge uske saath aage badhti hai.

Bahut effort ke baad devotee apne inner impurities ko overcome karta hai aur highest goal ki taraf pahunchta hai.

Sabse Best Yogi Kaun?

Krishna ne finally Arjuna ko kaha:

“Yogi ascetic se superior hai.”

“Yogi sirf knowledge wale person se bhi superior hai.”

“Yogi sirf action karne wale person se bhi superior hai.”

Isliye Krishna ne Arjuna se kaha:

“Arjuna, tum yogi bano.”

Aur sabhi yogiyon mein Krishna us person ko sabse dear maante hain jo:

Faith ke saath Krishna ko yaad karta hai,

apna mind Krishna mein rakhta hai,

aur pure heart se unki devotion karta hai.

Simple Lesson

Is chapter ka main message hai:

Mind ko control karo.

Regular practice karo.

Desires ko control karo.

Life mein balance rakho.

Failure se discourage mat ho.

Aur sabse important—

Spiritual journey mein kiya gaya sincere effort kabhi waste nahi hota.

Jo person apne mind ko control karke, faith aur devotion ke saath aage badhta hai, woh dheere-dheere inner peace aur highest spiritual goal ki taraf pahunchta hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # Section 6.3.19
        with st.expander("Section 6.3.19  Section XXXI (Bhagavad Gita Chapter VII)"):
            text1 = """ Bhagavad Gita – Chapter VII
Bhagwan Shri Krishna aur Arjuna ki Baat

Sanjaya ne Dhritarashtra ko bataya ki Bhagwan Shri Krishna ne Arjuna se kaha:

“Hey Arjuna, dhyaan se meri baat suno.

Agar tum apna mind mujh par laga kar, pure faith ke saath meri bhakti karoge aur meri sharan loge, to tum mujhe truly samajh sakoge.

Main tumhe ab knowledge aur experience dono ke baare mein bataunga. Inhe samajhne ke baad duniya mein jaanne ke liye bahut kuch baaki nahi rahega.

Hazaaron logon mein se sirf kuch log perfection ke liye mehnat karte hain. Aur unmein se bhi bahut hi kam log mujhe sach mein samajh paate hain.”

Krishna ne phir apni nature ke baare mein bataya.

“Arjuna, meri nature ke do forms hain. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Pehla hai meri lower nature. Ismein earth, water, fire, air, space, mind, intelligence aur consciousness aate hain.

Lekin meri ek higher nature bhi hai. Woh living beings ke form mein hai. Isi higher nature ki wajah se poora universe exist karta hai.

Samajh lo ki har living creature ka source main hi hoon. Universe ka creation bhi mujhse hota hai aur end mein iska dissolution bhi mujh mein hi hota hai.

Mere se upar kuch bhi nahi hai.

Jaise ek thread par pearls lage hote hain, waise hi poora universe mujh par depend karta hai.”

Krishna ne kaha:

“Arjuna, paani mein jo taste tum feel karte ho, woh main hoon.

Sun aur Moon ki jo brightness hai, woh bhi main hoon.

Vedas mein jo Om hai, woh main hoon.

Space mein jo sound hai, woh main hoon.

Insaan ke andar jo courage aur strength hai, woh bhi main hoon.

Earth ki fragrance, fire ki brightness aur living beings ke andar jo life hai, woh sab meri hi presence hai.

Jo log intelligence se blessed hain, unki intelligence bhi main hoon.

Jo powerful hain, unki strength bhi main hoon.

Aur jo desire duty ke according hai, woh bhi mujhse hi aata hai.”

Phir Krishna ne ek important baat samjhayi.

“Is duniya mein goodness, passion aur darkness—ye teen qualities hain. Ye sab mujhse hi aati hain.

Lekin main in qualities se beyond hoon.

Duniya ke log in teen qualities ke illusion mein phans jaate hain. Isliye woh mujhe truly samajh nahi paate.

Ye illusion cross karna bahut difficult hai.

Lekin jo log sincerely meri sharan lete hain, woh is illusion ko cross kar sakte hain.”

Krishna ne Arjuna ko bataya ki har insaan ka nature same nahi hota.

“Jo log evil kaam karte hain aur ignorance mein jeete hain, woh meri sharan nahi lete.

Lekin chaar types ke achhe log mujhe worship karte hain.

Koi trouble mein hota hai aur help ke liye mujhe yaad karta hai.

Koi knowledge paane ke liye mujhe worship karta hai.

Koi devotion ke saath mujhe yaad karta hai.

Aur koi mujhe hi apna highest goal maanta hai.

Inmein se sabhi good hain. Lekin jo person mujhe true knowledge ke saath samajhta hai, woh mujhe sabse dear hai.

Aisa person mujhe apna sab kuch maanta hai.

Bahut saare births ke baad, jab kisi person ko true knowledge milti hai, tab woh samajhta hai:

‘Vasudeva hi sab kuch hai.’

Lekin aisa person bahut rare hota hai.”

Krishna ne phir worship ke baare mein samjhaya:

“Arjuna, jis bhi form ko koi person faith ke saath worship karna chahta hai, main uski faith ko strong karta hoon.

Phir woh us form ki worship karta hai aur apni wishes ke according results paata hai.

Lekin aise results permanent nahi hote. Woh time ke saath khatam ho jaate hain.

Jo log different divine forms ko worship karte hain, woh unhi divine worlds ko attain karte hain.

Lekin jo mujhe worship karte hain, woh ultimately mujhe attain karte hain.”

Krishna ne kaha:

“Bahut se log mujhe sirf mere visible forms se dekhte hain. Woh meri real, eternal nature ko nahi samajh paate.

Meri power ka illusion itna strong hai ki har koi mujhe directly nahi dekh sakta.

Main unborn hoon aur mera destruction nahi hota.

Mujhe past, present aur future—sab kuch pata hai.

Lekin duniya mein bahut kam log hain jo mujhe truly jaante hain.”

Phir Krishna ne human nature ki ek simple baat samjhayi.

“Jab insaan duniya mein aata hai, tab woh desire aur hatred, yani attraction aur dislike ke beech phans jaata hai.

In opposite feelings ki wajah se uska mind confused rehta hai.

Lekin jo log apne good actions se apne sins ko khatam karte hain, woh dheere-dheere is confusion se free ho jaate hain.

Phir woh strong faith ke saath meri worship karte hain.

Jo log old age aur death se freedom paane ke liye meri sharan lete hain, woh Brahman, Adhyatma aur Karma ko samajhne lagte hain.”

Ant mein Krishna ne kaha:

“Jo log mujhe Adhibhuta, Adhidaiva aur Adhiyajna ke saath samajhte hain aur apna mind mujh par fix karte hain, woh apni life ke final moment par bhi mujhe yaad rakhte hain.

Aur jo mujhe truly jaante hain, woh mere highest reality ko samajh kar mujhe hi attain karte hain.”

Arjuna silently Krishna ki baatein sun raha tha.

Uske mind mein ab ek baat clear hone lagi thi—

Krishna sirf uske saamne khade ek friend nahi the. Krishna poore universe ke source aur har living being ke andar present divine truth the. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.20
        with st.expander("Section 6.3.20  Section XXXII (Bhagavad Gita Chapter VIII)"):
            text1 = """ Bhagavad Gita – Chapter VIII
Arjuna ke Questions aur Krishna ke Answers

Sanjaya ne Dhritarashtra ko bataya ki Arjuna ne Shri Krishna se kuch important questions pooche.

Arjuna bola:

“Hey Krishna, mujhe batao ki Brahman kya hai? Adhyatma kya hai? Karma kise kehte hain?

Adhibhuta aur Adhidaiva kya hain?

Aur is body ke andar Adhiyajna kaun hai?

Jab ek insaan apni body chhodta hai, us final moment mein aapko kaise jaana ja sakta hai?”

Krishna ne calmly Arjuna ko answer diya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Arjuna, Brahman woh Supreme aur eternal reality hai jo kabhi destroy nahi hoti.

Adhyatma us Supreme reality ka inner nature hai.

Aur jo offering ya action creation aur growth ka reason banta hai, use Karma kaha jaata hai.”

Phir Krishna ne ek bahut important baat kahi:

“Arjuna, insaan apni life ke last moment mein jis cheez ko yaad karta hai, uski consciousness usi direction mein jaati hai.

Agar koi person last time mujhe yaad karta hua body chhodta hai, to woh mujhe attain karta hai.

Ismein koi doubt nahi hai.

Isliye tum mujhe sirf last moment mein hi yaad mat karna.

Har waqt mujhe yaad karo aur apna duty bhi perform karo.

Tumhara mind aur understanding mujh par fixed rahe. Tab tum definitely mujhe attain karoge.”

Arjuna dhyaan se sun raha tha.

Krishna ne aage kaha:

“Jo person apna mind unnecessary things se hata kar continuously Supreme Being par focus karta hai, woh Divine Supreme Being ko attain karta hai.

Jab body chhodne ka time aata hai, agar person ka mind stable ho, faith strong ho aur woh apni life-energy ko control karke Supreme Being ko yaad kare, to woh highest goal ko attain karta hai.”

Krishna ne phir Om ke importance ke baare mein bataya.

“Jo person body chhodte waqt apne senses ko control karta hai, mind ko andar ki taraf lekar jaata hai aur Om ka dhyaan karta hai, saath hi mujhe yaad karta hai, woh highest destination ko attain karta hai.”

Phir Krishna ne Arjuna ko ek simple hope di:

“Jo devotee mujhe continuously yaad karta hai aur apna mind doosri cheezon mein bhatakne nahi deta, uske liye mujhe attain karna easy ho jaata hai.

Jo high-souled people mujhe attain kar lete hain, unhe phir is temporary aur painful world mein baar-baar birth nahi lena padta.

Duniya ke almost sabhi levels par birth aur death ka cycle hai.

Lekin jo mujhe attain kar leta hai, uske liye rebirth nahi hota.”

Krishna ne phir universe ke bahut bade cycle ke baare mein samjhaya.

“Arjuna, Brahma ka ek day aur night humare normal day aur night jaise nahi hain.

Brahma ka day bahut, bahut long hota hai. Aur uski night bhi utni hi long hoti hai.

Brahma ke day ke beginning mein jo kuch unmanifest hota hai, woh manifest hone lagta hai.

Aur jab Brahma ki night aati hai, to wahi sab kuch phir unmanifest mein dissolve ho jaata hai.

Creatures baar-baar appear hote hain aur phir dissolve ho jaate hain.

Phir day aata hai aur woh dobara appear hote hain.

Ye cycle continuously chalti rehti hai.”

Lekin Krishna ne kaha ki is sabke beyond bhi ek reality hai.

“Arjuna, is temporary universe ke beyond ek aur eternal reality hai.

Woh kabhi destroy nahi hoti.

Jab poora universe dissolve ho jaata hai, tab bhi woh Supreme reality remain karti hai.

Usi ko highest goal kaha gaya hai.

Jo us Supreme Being ko attain kar leta hai, usse dobara is world mein return nahi karna padta.

Wahi mera Supreme seat hai.

Us Supreme Being ke andar poora universe exist karta hai aur usi se poora universe filled hai.

Jo person pure devotion ke saath usse attain karna chahta hai, woh us highest reality tak pahunch sakta hai.”

Phir Krishna ne life ke baad ke do spiritual paths ke baare mein bataya.

“Arjuna, scriptures mein do important paths bataye gaye hain.

Pehla bright path hai.

Is path ko fire, light, day aur bright fortnight ke symbols se samjhaya gaya hai. Jo enlightened devotees is path se jaate hain, woh Supreme reality ko attain karte hain aur wapas nahi aate.

Doosra dark path hai.

Ismein darkness, night aur dark fortnight ke symbols hain. Is path se jaane wala person lunar world tak pahunch sakta hai, lekin usse eventually wapas return karna padta hai.

Ye dono paths bahut old aur eternal maane gaye hain.

Jo person in dono paths ko samajh leta hai, woh confused nahi hota.”

Krishna ne end mein Arjuna se kaha:

“Isliye Arjuna, har waqt devotion mein raho.

Jo person is knowledge ko truly samajh leta hai, woh sirf Vedas ka knowledge, sacrifices, penance aur charity ke rewards hi nahi paata.

Woh in sabse bhi higher reward paata hai—

Supreme aur eternal reality ko attain karta hai.”

Arjuna ne Krishna ki baatein suni.

Ab usse samajh aa raha tha ki life sirf birth aur death ka cycle nahi hai.

Insaan ka mind, actions aur final focus uski journey ko decide karte hain.

Aur Krishna ka message simple tha:

“Mujhe yaad karo, apna duty karo, aur apna mind Supreme truth par rakho.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.21
        with st.expander("Section 6.3.21  Section XXXIII (Bhagavad Gita Chapter IX)"):
            text1 = """ Bhagavad Gita – Chapter IX
Krishna ka Sabse Secret aur Powerful Knowledge

Sanjaya ne Dhritarashtra ko bataya ki Shri Krishna ne Arjuna se kaha:

“Arjuna, ab main tumhe ek bahut special knowledge bataunga.

Ye knowledge bahut secret hai, lekin ise samajhna possible hai. Isse tum apne andar ke doubts aur negativity se free ho sakte ho.

Ye royal knowledge hai aur royal secret bhi.

Ye pure aur powerful hai. Isse experience bhi kiya ja sakta hai.

Aur sabse achhi baat—ye samajhna relatively easy hai aur iska truth kabhi destroy nahi hota.”

Krishna ne kaha: """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Jo log is knowledge par faith nahi rakhte, woh mujhe attain nahi kar paate. Woh baar-baar isi temporary world ke cycle mein return karte hain.

Arjuna, poora universe meri unmanifest form se filled hai.

Sabhi living beings mujh par depend karte hain, lekin main unke physical form mein limited nahi hoon.

Meri divine power ko dekho.

Main sabko support karta hoon aur sabke existence ka source hoon, phir bhi main kisi ek body mein limited nahi hoon.

Jaise hawa poori space mein spread hoti hai, waise hi saare beings mujh mein exist karte hain.”

Krishna ne universe ke cycle ke baare mein bataya:

“Jab ek Kalpa end hota hai, sabhi beings meri unmanifest nature mein merge ho jaate hain.

Aur jab naya Kalpa start hota hai, main unhe phir se create karta hoon.

Nature ke rules ke according ye creation ka process baar-baar hota rehta hai.

Main is poore process ko observe karta hoon, lekin main in actions se attached nahi hota.

Meri supervision mein nature moving aur non-moving sabhi beings ko create karti hai.

Isi wajah se universe birth aur destruction ke cycle mein chalta rehta hai.”

Phir Krishna ne un logon ke baare mein bataya jo unhe samajh nahi paate.

“Jo log meri supreme nature ko nahi samajhte, woh mujhe sirf ek normal human body ke roop mein dekhte hain.

Unki hopes aur efforts wrong direction mein chale jaate hain.

Lekin jo high-souled people meri divine nature ko samajhte hain, woh mujhe sabhi beings ka source aur eternal reality maankar worship karte hain.

Koi mujhe continuously praise karta hai.

Koi strong discipline ke saath devotion karta hai.

Aur koi respect ke saath mujhe bow karta hai.

Unka mind kisi aur direction mein nahi bhatakta.”

Krishna ne kaha:

“Kuch log knowledge ke through worship karte hain.

Woh mujhe ek Supreme reality ke roop mein dekhte hain.

Kuch log mujhe different forms mein dekhte hain.

Lekin unka ultimate goal mujhe hi samajhna hota hai.”

Phir Krishna ne bataya ki woh har jagah present hain.

“Arjuna, sacrifice mein jo offering hoti hai, woh main hoon.

Sacred mantra main hoon.

Fire main hoon.

Sacrifice mein diya gaya offering bhi main hoon.

Main is universe ka father hoon.

Main mother hoon.

Main creator hoon.

Main sabka ancient source hoon.

Main woh truth hoon jise jaana chahiye.

Main Om hoon.

Main Vedas ka knowledge hoon.

Main goal hoon.

Main support hoon.

Main protector hoon.

Main witness hoon.

Main refuge hoon.

Main friend hoon.

Main creation ka source bhi hoon aur destruction ka reason bhi.

Main eternal seed hoon jisse sab kuch originate hota hai.

Main heat deta hoon.

Main rain ko create aur control karta hoon.

Main immortality bhi hoon aur death bhi.

Jo exist karta hai aur jo unmanifest hai, dono mujhse hi connected hain.”

Arjuna Krishna ki baatein sun kar deeply sochne laga.

Krishna ne phir bataya ki sirf temporary rewards ke liye ki gayi worship ka result bhi temporary hota hai.

“Jo log Vedas ke rituals follow karte hain, sacrifices karte hain aur heavenly pleasures ki desire rakhte hain, woh apne good actions ke result se heaven tak pahunch sakte hain.

Wahan unhe bahut happiness milti hai.

Lekin jab unke good deeds ka result khatam ho jaata hai, to unhe dobara mortal world mein return karna padta hai.

Isliye jo log sirf desires ke peeche worship karte hain, woh baar-baar going and coming ke cycle mein rehte hain.”

Krishna ne kaha:

“Lekin jo devotees mujhe hi apna main goal bana kar worship karte hain, main unki needs ka dhyaan rakhta hoon.

Jo mere devotees hain aur pure faith ke saath mujhe yaad karte hain, main unhe support karta hoon.”

Phir Krishna ne ek beautiful baat kahi:

“Jo log faith ke saath kisi aur divine form ko worship karte hain, woh bhi ultimately mujhe hi worship kar rahe hote hain, although unka method direct nahi hota.”

Krishna ne sacrifice ke baare mein kaha:

“Main hi sabhi sacrifices ka true enjoyer aur Lord hoon.

Lekin jo log mujhe truly nahi samajhte, unhe permanent result nahi milta.

Jo ancestors ko worship karte hain, woh ancestors ke world ko attain karte hain.

Jo lower spirits ko worship karte hain, woh unhi worlds ko attain karte hain.

Aur jo mujhe worship karte hain, woh mujhe attain karte hain.”

Phir Krishna ne ek bahut simple example diya:

“Arjuna, agar koi person mujhe pure heart se ek leaf, flower, fruit ya water bhi offer karta hai, main us offering ko accept karta hoon.

Important ye nahi hai ki offering kitni expensive hai.

Important hai ki woh pure heart aur devotion se di gayi hai.”

Krishna ne Arjuna ko daily life ka ek simple rule diya:

“Tum jo bhi karte ho, jo bhi khaate ho, jo bhi peete ho, jo bhi donate karte ho, aur jo bhi discipline ya austerity follow karte ho—

use mujhe offering samajhkar karo.

Aisa karne se tum apne actions ke good aur bad results ke bondage se gradually free ho jaoge.

Tumhara mind attachment se free hoga aur tum mujhe attain karoge.”

Phir Krishna ne equality ki baat samjhayi:

“Main sabhi beings ko equally dekhta hoon.

Mere liye koi hateful nahi hai aur koi specially favourite bhi nahi.

Lekin jo mujhe pure devotion se worship karte hain, woh mere saath connected ho jaate hain aur main unke saath.”

Krishna ne Arjuna ko hope dete hue kaha:

“Arjuna, agar koi person bahut galat life jee raha tha, lekin ab sincerely mujhe worship karne laga hai aur apna direction change kar raha hai, to usse bhi good person maana jaana chahiye.

Kyuki ab uska direction sahi hai.

Aisa person jaldi hi apne andar goodness develop karta hai aur eternal peace paata hai.”

Phir Krishna ne ek bahut powerful message diya:

“Mera devotee kabhi lost nahi hota.”

“Chahe koi bhi person ho, agar woh sincerely meri sharan leta hai, woh highest goal attain kar sakta hai.

Isliye Arjuna, is temporary aur difficult world mein rehkar apna mind mujh par fix karo.

Mere devotee bano.

Mujhe sincerely worship karo.

Mujhe respect ke saath bow karo.

Mujhe apna refuge banao.

Apne mind ko mujh par focus karo.

Aisa karoge to tum definitely mujhe attain karoge.”

Arjuna ne Krishna ki baat ko deeply feel kiya.

Usse samajh aa gaya ki Krishna ke liye expensive offerings ya special rituals se zyada important ek pure heart aur true devotion hai.

Aur Krishna ka simple message tha:

“Jo bhi karo, mujhe yaad karke karo. Pure heart se karo. Aur mujhe apna highest goal banao.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.22
        with st.expander("Section 6.3.22  Section XXXIV (Bhagavad Gita Chapter X)"):
            text1 = """ Bhagavad Gita – Chapter X
Krishna ki Divine Powers

Sanjaya ne Dhritarashtra ko bataya ki Shri Krishna ne Arjuna se kaha:

“Arjuna, ek baar phir meri baat dhyaan se suno.

Main tumhare good ke liye tumhe apni kuch special aur divine baatein bataunga.

Meri real beginning ko gods aur great Rishis bhi completely nahi jaante.

Kyunki main hi gods aur Rishis ka source hoon.

Jo person mujhe Supreme Lord maanta hai aur samajhta hai ki mera koi beginning ya birth nahi hai, woh confusion aur sins se free ho jaata hai.”

Krishna ne kaha: """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Arjuna, duniya mein jo bhi qualities tum dekhte ho—intelligence, knowledge, forgiveness, truth, self-control, peace, happiness, sadness, birth, death, fear, courage, contentment, charity aur fame—ye sab kisi na kisi form mein mujhse hi aati hain.

Great Rishis aur Manus bhi meri divine nature se hi aaye hain.

Aur unse hi duniya mein bahut saari living beings ka creation hua.”

Phir Krishna ne ek important baat kahi:

“Jo person meri divine powers ko truly samajh leta hai, uski devotion strong ho jaati hai.

Woh samajhta hai:

‘Krishna hi sab kuch ka source hain. Jo kuch bhi exist karta hai, woh Krishna se hi aaya hai.’

Aise wise people pure heart se meri worship karte hain.

Unka mind mujh par laga rehta hai.

Unki life mujhe dedicated hoti hai.

Woh ek-doosre se mere baare mein baat karte hain, meri greatness discuss karte hain aur mujhe yaad karke khush rehte hain.

Aur jo devotees mujhe pure love se worship karte hain, main unhe woh knowledge deta hoon jisse woh mujhe truly samajh sakein.

Main unke heart mein knowledge ka light jala deta hoon.

Aur us light se unki ignorance ka darkness khatam ho jaata hai.”

Arjuna ne Krishna ki baat sun kar kaha:

“Krishna, ab mujhe samajh aa raha hai ki aap kitne great hain.

Aap Supreme Brahman hain.

Aap highest destination hain.

Aap sabse pure aur eternal Divine Being hain.

Aap beginning ke bina hain.

Aap sabke Lord hain.

Great Rishis bhi aapko isi tarah describe karte hain.

Narada, Asita, Devala aur Vyasa jaise great Rishis bhi aapki greatness ko accept karte hain.

Aur aap khud bhi mujhe yahi bata rahe hain.

Main aapki baaton ko completely true maanta hoon.

Gods aur Danavas bhi aapki complete nature ko nahi samajh sakte.

Sirf aap hi khud ko completely jaante hain.”

Arjuna ne phir kaha:

“Hey Krishna, aap poore universe ke creator hain.

Aap sabke Lord hain.

Isliye please mujhe apni divine powers ke baare mein aur bataiye.

Aap kin-kin forms mein is world mein present hain?

Main jab meditation karun, to kis-kis form mein aapko yaad karun?

Aapki baatein sun kar mera mind kabhi satisfied nahi hota.

Mujhe aapke divine words sunna bahut achha lagta hai.”

Krishna muskuraaye aur bole:

“Arjuna, meri divine powers ka koi end nahi hai.

Main tumhe unmein se kuch important examples bataunga.”

Krishna Har Jagah Present Hain

Krishna ne kaha:

“Main har living being ke heart mein present Soul hoon.

Main sabhi beings ka beginning hoon.

Main unka middle hoon.

Aur main unka end bhi hoon.

Adityas mein main Vishnu hoon.

Bright objects mein main Sun hoon.

Maruts mein main Marichi hoon.

Aur stars ke beech main Moon hoon.

Vedas mein main Sama Veda hoon.

Gods mein main Indra hoon.

Senses mein main Mind hoon.

Aur living beings mein main Intelligence hoon.”

Krishna ne aage kaha:

“Rudras mein main Shankara hoon.

Yakshas aur Rakshasas mein main Kubera hoon.

Vasus mein main Pavaka hoon.

Mountains mein main Meru hoon.

Great Rishis mein main Bhrigu hoon.

Words mein main Om hoon.

Sacrifices mein main Japa, yani mantra ka continuous remembrance, hoon.

Mountains mein main Himalaya hoon.

Trees mein main Peepal tree hoon.

Celestial Rishis mein main Narada hoon.

Gandharvas mein main Chitraratha hoon.

Aur great Yogis mein main Kapila hoon.”

Arjuna aur bhi dhyaan se sunne laga.

Krishna ne kaha:

“Horses mein main Uccaisravas hoon.

Elephants mein main Airavata hoon.

Human beings mein main King hoon.

Weapons mein main Thunderbolt hoon.

Cows mein main Kamadhenu hoon.

Serpents mein main Vasuki hoon.

Nagas mein main Ananta hoon.

Water beings mein main Varuna hoon.

Aur justice dene walon mein main Yama hoon.”

Phir Krishna ne kaha:

“Daityas mein main Prahlada hoon.

Time ko count karne walon mein main Time hoon.

Animals mein main Lion hoon.

Birds mein Garuda hoon.

Purifying things mein main Wind hoon.

Weapons use karne walon mein main Rama hoon.

Fishes mein main Makara hoon.

Aur rivers mein main Ganga hoon.”

Krishna ne thoda rukkar kaha:

“Arjuna, created things mein main beginning, middle aur end hoon.

Knowledge ke different forms mein main Supreme Spirit ka knowledge hoon.

Debate karne walon mein main strong reasoning hoon.

Letters mein main A hoon.

Time mein main eternal Time hoon.

Main woh force hoon jo sabke actions aur results ko order karti hai.

Main Death hoon jo sabko eventually apne paas le jaati hai.

Aur main future mein hone wali creation ka source bhi hoon.”

Krishna ne women ki qualities ke baare mein bhi bataya:

“Women mein jo fame, fortune, speech, memory, intelligence, patience aur forgiveness jaise qualities hain, woh bhi meri divine powers hain.

Songs mein main best Sama hymn hoon.

Poetic metres mein main Gayatri hoon.

Months mein main Margashirsha hoon.

Aur seasons mein main Spring hoon, jab nature flowers se bhar jaati hai.”

Phir Krishna ne kaha:

“Cheating games mein main dice ka skill hoon.

Brilliant people mein main unki brilliance hoon.

Victory mein main victory hoon.

Effort mein main effort hoon.

Aur good people mein main unki goodness hoon.

Vrishnis mein main Vasudeva hoon.

Pandavas mein main Arjuna hoon.

Ascetics mein main Vyasa hoon.

Wise seers mein main Ushanas hoon.

Jo log punish karte hain, unke discipline mein main hoon.

Jo victory ke liye strategy banate hain, unki policy mein main hoon.

Secrets mein main silence hoon.

Aur knowledgeable people ki knowledge bhi main hoon.”

Arjuna silently Krishna ki baatein sun raha tha.

Krishna ne end mein kaha:

“Arjuna, main hi sabhi things ka seed, yani source hoon.

Koi bhi moving ya non-moving thing mere bina exist nahi kar sakti.

Meri divine powers ki koi limit nahi hai.

Maine tumhe sirf kuch examples diye hain.

Duniya mein jo bhi truly great, beautiful, powerful ya glorious hai, samajh lo ki woh meri divine energy ke ek small part se hi aata hai.

Isliye tumhe meri powers ko count karne ki zarurat nahi hai.

Bas itna samajh lo—

Main apne sirf ek small part se poore universe ko support karta hoon.”

Arjuna ke liye ab Krishna sirf ek guide nahi rahe the.

Usse har taraf Krishna ki presence feel hone lagi.

Sun mein Krishna.

Ganga mein Krishna.

Mountains mein Krishna.

Animals mein Krishna.

Knowledge mein Krishna.

Aur sabse important—

har living being ke heart mein Krishna.

Krishna ka message simple tha:

“Duniya mein jo bhi sabse achha, powerful aur glorious hai, usmein meri divine energy ki ek jhalak hai.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.23
        with st.expander("Section 6.3.23  Section XXXV (Bhagavad Gita Chapter XI)"):
            text1 = """ Bhagavad Gita – Chapter XI
Arjuna ne Dekha Krishna ka Vishwaroop

Arjuna ne Krishna ki baatein dhyaan se suni. Krishna ne use universe ki creation, destruction aur apni divine powers ke baare mein samjhaya tha.

Arjuna bola:

“Hey Krishna, aapne jo mujhe Supreme truth ke baare mein bataya hai, usse mera confusion door ho gaya hai.

Ab main aapki greatness ko samajhne laga hoon.

Aapne mujhe bataya ki ye poora universe kaise create aur dissolve hota hai. Aapki divine powers ke baare mein bhi maine suna.

Ab meri ek wish hai.

Agar aapko lagta hai ki main aapke us Supreme form ko dekhne ke capable hoon, to please mujhe apna eternal form dikhaaiye.”

Krishna ne Arjuna ki request accept kar li.

Krishna bole: """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Arjuna, mere forms sirf ek ya do nahi hain.

Tum mere hundreds aur thousands of divine forms dekh sakte ho.

Different colours, different shapes aur different divine powers ke saath.

Adityas, Vasus, Rudras, Ashvins aur Maruts—sabko dekho.

Aur unke alawa bhi bahut saare aise wonders dekho jo tumne pehle kabhi nahi dekhe.

Tum mere andar poora universe dekh sakte ho.

Jo kuch moving hai aur jo kuch still hai, sab ek hi place par mere andar present hai.”

Phir Krishna ne ek important baat kahi:

“Lekin Arjuna, tum apni normal human eyes se mera ye form nahi dekh sakte.

Isliye main tumhe divine sight deta hoon.

Ab meri Supreme divine power ko dekho.”

Krishna ne itna kaha aur apna Vishwaroop reveal kar diya.

Sanjaya ne Dhritarashtra ko bataya:

Krishna ne Arjuna ke saamne apna Supreme Universal Form dikha diya.

Arjuna ne ek aisa roop dekha jisme bahut saare faces, eyes, arms aur bodies the.

Us form par countless divine ornaments the.

Uske haath mein divine weapons the.

Woh celestial clothes aur garlands se decorated tha.

Us form se ek extraordinary light nikal rahi thi.

Woh form endless tha aur uski direction har taraf thi.

Agar sky mein ek saath hazaar suns rise kar jaate, to unki combined brightness bhi us divine form ki brightness ke saamne chhoti lagti.

Arjuna ne Krishna ke us form ke andar poora universe dekha.

Gods, Rishis aur countless beings sab usi Universal Form ke andar dikh rahe the.

Arjuna ye sab dekh kar completely amazed ho gaya.

Uske body ke hairs stand ho gaye.

Usne apne hands join kiye aur Krishna ke saamne head bow kar diya.

Arjuna bola:

“Hey Krishna, main aapke andar sabhi gods ko dekh raha hoon.

Main different types ke creatures ko dekh raha hoon.

Main Brahma ko bhi dekh raha hoon.

Main great Rishis aur divine snakes ko bhi dekh raha hoon.

Aapke innumerable arms hain.

Bahut saare stomachs hain.

Bahut saare mouths aur eyes hain.

Aap har direction mein present hain.

Main aapka beginning nahi dekh pa raha.

Main aapka middle nahi dekh pa raha.

Aur main aapka end bhi nahi dekh pa raha.

Aap truly Infinite hain.”

Arjuna ne Krishna ke weapons aur divine energy ko dekha.

“Main aapko crown, mace aur discus ke saath dekh raha hoon.

Aapki energy itni powerful hai ki aapko directly dekhna bhi difficult hai.

Aap blazing fire aur Sun ki tarah glow kar rahe hain.

Aap immeasurable hain.

Aap eternal hain.

Aap is entire universe ke Supreme reality hain.

Sun aur Moon aapki eyes jaise dikh rahe hain.

Aapka mouth blazing fire ki tarah hai.

Aapki energy poore universe ko heat kar rahi hai.

Heaven aur Earth ke beech ki poori space aapse filled hai.”

Lekin Krishna ka Vishwaroop sirf beautiful nahi tha.

Uska ek terrible aur frightening side bhi tha.

Arjuna ne dekha ki bahut saare gods Krishna ke form mein enter kar rahe hain.

Kuch beings fear ke saath hands join karke Krishna ko pray kar rahe the.

Great Rishis aur Siddhas Krishna ki praise kar rahe the.

Rudras, Adityas, Vasus, Ashvins, Maruts, Gandharvas, Yakshas aur other divine beings bhi us form ko dekh kar amazed the.

Arjuna ka fear aur badh gaya.

Usne Krishna ka ek aisa form dekha jisme countless mouths, eyes, arms, legs aur terrifying teeth the.

Woh form sky tak spread ho raha tha.

Uski brightness bahut intense thi.

Uske mouths huge aur frightening the.

Arjuna ka mind tremble karne laga.

Usse peace feel nahi ho rahi thi.

Usne kaha:

“Hey Krishna, main aapka ye terrifying form dekh kar bahut dar gaya hoon.

Mujhe directions tak samajh nahi aa rahi hain.

Mera mind completely disturbed ho gaya hai.

Please mujh par mercy kijiye.

Aap hi universe ka refuge hain.”

Phir Arjuna ne ek aur frightening scene dekha.

Dhritarashtra ke sons, bahut saare kings, Bhishma, Drona, Karna aur doosre great warriors Krishna ke terrifying mouths ki taraf rapidly ja rahe the.

Kuch warriors Krishna ke teeth ke beech crush hote hue dikh rahe the.

Arjuna ne kaha:

“Ye sab warriors aapki taraf aise ja rahe hain jaise rivers fast flow karke ocean mein jaati hain.

Aur jaise moths jalti hui fire ki taraf khud hi chale jaate hain, waise hi ye warriors aapke flaming mouths mein enter kar rahe hain.

Aap unhe har taraf se swallow kar rahe hain.

Aapki energy poore universe ko fill kar rahi hai.

Aapki powerful radiance sab kuch heat kar rahi hai.

Hey Krishna, aap kaun hain?

Aap itne fierce form mein kya kar rahe hain?

Please mujhe bataiye.

Main aapki reality samajhna chahta hoon.”

Krishna ne Arjuna ko answer diya:

“Arjuna, main Death hoon—the destroyer of worlds.

Ab main in warriors ke destruction ke liye present hoon.

Tumhare bina bhi ye warriors apne end ki taraf ja rahe hain.

Isliye ab tum sirf mera instrument bano.

Utho.

Fight karo.

Apna duty perform karo.

Victory hasil karo.

Drona, Bhishma, Jayadratha, Karna aur doosre warriors already mere divine plan mein defeated hain.

Tum bas apna role perform karo.

Dar mat.

Battle karo.

Tum apne enemies ko defeat karoge.”

Krishna ki ye baat sunkar Arjuna ka body tremble kar raha tha.

Usne hands join kiye aur Krishna ke saamne bow kiya.

Fear ke kaaran uski voice bhi properly nahi nikal rahi thi.

Phir Arjuna bola:

“Hey Krishna, aapki praise karna bilkul natural hai.

Aapko dekh kar good beings aapko respect karte hain.

Aur Rakshasas fear ke saath har direction mein bhaag rahe hain.

Siddhas aapko bow kar rahe hain.

Aisa hona hi chahiye.

Aap Supreme Soul hain.

Aap Brahma se bhi greater hain.

Aap sabke original cause hain.

Aap Infinite hain.

Aap universe ke refuge hain.

Aap eternal hain.

Aap hi woh reality hain jo exist karti hai aur jo unmanifest hai.

Aap hi sabse ancient Divine Being hain.

Aap hi Knower hain.

Aap hi woh Supreme truth hain jise jaana chahiye.

Aur poora universe aapse hi filled hai.”

Arjuna ko achanak apni purani baatein yaad aayi.

Usne Krishna ko hamesha apna friend samjha tha.

Kabhi woh Krishna ko casually “O Krishna,” “O Yadava,” “O friend” keh deta tha.

Kabhi unke saath mazaak karta tha.

Saath mein baithta tha.

Saath mein khana khata tha.

Kabhi private mein aur kabhi doosre logon ke saamne bhi usne Krishna ke saath casual behaviour kiya tha.

Ab Krishna ka Universal Form dekh kar Arjuna ko samajh aa gaya ki woh kitni great divine personality ke saamne tha.

Arjuna bola:

“Hey Krishna, agar maine friendship ya love ki wajah se kabhi aapke saath disrespectfully behave kiya ho, to please mujhe forgive kijiye.

Mujhe aapki real greatness pata nahi thi.

Ab mujhe samajh aa gaya hai ki aap mere normal friend se kahin zyada hain.

Aap poore universe ke father hain.

Aap great master hain.

Aapke equal koi nahi hai.

Aapse greater bhi koi nahi ho sakta.

Isliye main aapke saamne bow karta hoon.

Please mere mistakes ko waise hi forgive kijiye jaise ek father apne child ki mistakes forgive karta hai.”

Phir Arjuna ne request ki:

“Krishna, aapka ye Universal Form dekh kar main amazed bhi hoon aur frightened bhi.

Please ab apna woh familiar form dikhaaiye.

Wahi form jisme crown ho, mace ho aur discus ho.

Main aapko phir se us gentle form mein dekhna chahta hoon.”

Krishna ne Arjuna ki request accept kar li.

Krishna bole:

“Arjuna, maine tumhe apna ye Supreme Universal Form apni divine power se dikhaya hai.

Ye form bahut rare hai.

Tumhare alawa kisi human ne ise is tarah nahi dekha.

Sirf Vedas padhne, sacrifices karne, gifts dene ya severe austerities karne se bhi ye form directly dekhna possible nahi hai.

Lekin tum daro mat.

Apna fear chhod do.

Ab tum mujhe mere gentle form mein dobara dekhoge.”

Krishna ne apna terrifying Universal Form withdraw kar liya.

Phir woh apne familiar, gentle human form mein Arjuna ke saamne khade ho gaye.

Krishna ne Arjuna ko comfort kiya.

Arjuna ne Krishna ka normal form dekha aur uska mind finally calm ho gaya.

Woh bola:

“Hey Krishna, ab aapko apne familiar human form mein dekhkar mera mind stable ho gaya hai.

Ab main normal feel kar raha hoon.”

Krishna ne kaha:

“Arjuna, jo form tumne abhi dekha, woh bahut rare hai.

Even gods bhi us form ko dekhne ki wish rakhte hain.

Sirf Vedas, austerities, charity ya sacrifices se mujhe us form mein truly nahi jaana ja sakta.

Lekin pure devotion se mujhe truly know kiya ja sakta hai.

Jo person mere liye apne actions karta hai, mujhe apna highest goal maanta hai, attachment se free rehta hai aur kisi being se hatred nahi rakhta—

woh ultimately mujhe attain karta hai.”

Arjuna ne Krishna ki baat samajh li.

Usne dekha tha ki Krishna sirf uske friend nahi the.

Krishna ke andar poora universe tha.

Creation bhi unhi se connected thi.

Destruction bhi unhi ke control mein tha.

Aur Arjuna ka role simple tha—

apna duty karo, fear ko chhodo, aur Krishna par trust rakho. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.24
        with st.expander("Section 6.3.24  Section XXXVI (Bhagavad Gita Chapter XII)"):
            text1 = """ Bhagavad Gita – Chapter XII
Bhakti Yoga – Krishna ko Kaise Bhakti Karni Chahiye

Arjuna ne Krishna se ek important question poocha:

“Hey Krishna, jo log continuously aapki devotion karte hain aur aapke personal form ko worship karte hain, aur jo log aapko formless aur unmanifest reality ke roop mein meditate karte hain—inn dono mein se kaun devotion ko better samajhta hai?”

Krishna ne calmly jawab diya:

“Arjuna, jo log apna mind mujh par fix karte hain, strong faith ke saath continuously mujhe worship karte hain, main unhe sabse devoted maanta hoon.

Lekin jo log Unmanifest, Eternal aur All-pervading reality par meditation karte hain, woh bhi mujhe attain kar sakte hain.

Woh apne senses ko control karte hain.

Sabhi beings ko equal nazar se dekhte hain. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Aur sabke welfare ke liye kaam karte hain.

Lekin unke liye ye path difficult hai.

Kyunki jo log body mein reh rahe hain, unke liye completely formless reality par mind fix karna easy nahi hota.”

Phir Krishna ne Arjuna ko ek simple path bataya:

“Jo log apne saare actions mujhe dedicate karte hain aur mujhe apna highest goal maante hain, woh devotion ke saath mujhe yaad karte hain.

Aise devotees ko main khud is mortal world ke ocean se cross karne mein help karta hoon.

Isliye apna heart mujh par fix karo.

Apni understanding bhi mujh par rakho.

Aisa karoge to tum eventually mere saath connected rahoge.”

Arjuna ke liye Krishna ne phir devotion ke different levels samjhaye.

“Lekin agar tum apna mind continuously mujh par fix nahi kar paate, to practice karo.

Bar-bar apna mind mujhe yaad karne ki habit banao.

Agar continuous meditation bhi difficult lagti hai, to mere liye actions karo.

Apna kaam mujhe dedicate karo.

Aur agar ye bhi difficult hai, to kam se kam apne actions ke results ka attachment chhod do.

Apna duty karo, lekin result ko lekar excessive attachment mat rakho.”

Krishna ne bataya ki spiritual growth ek step-by-step journey bhi ho sakti hai.

“Knowledge achhi hai.

Knowledge se bhi better meditation hai.

Aur meditation se bhi important hai actions ke fruits ko release karna.

Jab insaan apne actions ke results ka attachment chhod deta hai, tab uske andar peace aati hai.”

Phir Krishna ne bataya ki unka favourite devotee kaisa hota hai.

“Jo kisi living being se hatred nahi karta, woh mujhe dear hai.

Jo friendly aur compassionate hai, woh mujhe dear hai.

Jo ego se free hai aur unnecessary pride nahi karta, woh mujhe dear hai.

Jo attachment se free hai.

Jo happiness aur sadness dono mein balanced rehta hai.

Jo forgiving hai.

Jo satisfied rehta hai.

Jo disciplined hai.

Jo strong determination rakhta hai.

Aur jiska heart aur understanding mujh par fixed hai—

aisa devotee mujhe bahut dear hai.”

Krishna ne aage kaha:

“Jo person duniya ko unnecessary trouble nahi deta aur khud bhi duniya ki har baat se disturb nahi hota, woh mujhe dear hai.

Jo excessive happiness, anger, fear aur anxiety se free hai, woh mujhe dear hai.

Jo pure heart ka hai, hardworking hai aur worldly attachments mein unnecessarily involved nahi hota, woh bhi mujhe dear hai.

Aur jo actions karta hai lekin unke fruits ke peeche nahi bhaagta, woh mujhe dear hai.”

Krishna ne phir ek aur simple quality batayi:

“Jo person unnecessary excitement ya hatred mein nahi rehta.

Jo na excessive grief karta hai aur na unnecessary desires ke peeche bhaagta hai.

Jo good aur bad results ke attachment ko bhi chhod deta hai.

Aur jo mujh par complete faith rakhta hai—

woh mujhe dear hai.”

Krishna ne Arjuna ko bataya ki true devotee har situation mein balanced rehta hai.

“Jo friend aur enemy ko equal respect deta hai.

Jo honour aur insult mein same rehta hai.

Jo cold aur heat mein balanced rehta hai.

Jo pleasure aur pain dono mein stable rehta hai.

Jo praise aur criticism dono ko equally leta hai.

Jo unnecessary talking se bachta hai.

Jo simple life se satisfied hai.

Jo kisi particular place ya possession se overly attached nahi hai.

Aur jiska mind steady hai aur faith strong hai—

aisa devotee mujhe bahut dear hai.”

Krishna ne end mein kaha:

“Arjuna, jo log is path of devotion ko sincerely follow karte hain, faith ke saath mujhe apna highest goal maante hain aur isi dharma par chalte hain—

woh mujhe sabse dear hain.”

Arjuna ne Krishna ki baat samajh li.

Krishna ka message simple tha:

Bhakti ka matlab sirf worship karna nahi hai.

True bhakti ka matlab hai—

ego kam karna, sabke saath kindness rakhna, mind ko balanced rakhna, apna duty karna aur actions ke results ka unnecessary attachment chhod dena.

Aisa person dheere-dheere inner peace paata hai aur Krishna ke aur close hota jaata hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.25
        with st.expander("Section 6.3.25  Section XXXVII (Bhagavad Gita Chapter XIII)"):
            text1 = """ Bhagavad Gita – Chapter XIII
Kshetra aur Kshetrajna – Body aur Soul ka Sach

Sanjaya ne Dhritarashtra ko bataya ki Shri Krishna ne Arjuna ko body aur soul ke baare mein ek deep truth samjhaya.

Krishna bole:

“Arjuna, is body ko Kshetra kaha jaata hai.

Aur jo is body ko jaanta hai, use Kshetrajna kaha jaata hai.

Simple words mein samjho—

Body ek field hai, aur jo is body ko experience karta hai, woh Kshetrajna hai.

Main bhi sabhi bodies mein Kshetrajna ke roop mein present hoon. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Kshetra aur Kshetrajna ko truly samajhna hi real knowledge hai.”

Krishna ne phir bataya ki Kshetra sirf physical body nahi hai.

Ismein five great elements, ego, intelligence, unmanifest nature, ten senses, mind aur five sense objects shamil hain.

Saath hi desire, dislike, happiness, pain, body-consciousness aur courage bhi Kshetra ka part hain.

Yaani jo kuch body aur mind ke experience se related hai, woh Kshetra ke andar aata hai.

Phir Krishna ne bataya ki true knowledge kya hota hai.

“Knowledge ka matlab sirf books padhna nahi hai.

True knowledge tab hai jab insaan mein humility ho.

Woh show-off na kare.

Kisi ko hurt na kare.

Forgiving ho.

Straightforward ho.

Apne teacher ka respect kare.

Pure rahe.

Apne mind aur senses ko control kare.

Sense pleasures ke peeche blindly na bhaage.

Ego ko kam kare.

Aur ye samjhe ki birth, old age, disease aur death mein suffering bhi hoti hai.”

Krishna ne aage kaha:

“True knowledge ka matlab attachment ko kam karna bhi hai.

Insaan ko family, home aur possessions se unnecessary attachment nahi rakhna chahiye.

Good situation aaye ya bad situation, mind ko balanced rakhna chahiye.

Mere prati steady devotion rakhni chahiye.

Mind ko sirf external duniya mein busy rakhne ke bajay kabhi-kabhi solitude mein bhi rehna chahiye.

Aur ye samajhna chahiye ki individual soul ka Supreme reality ke saath kya relation hai.

Ye sab Knowledge hai.

Aur jo iska opposite hai, woh Ignorance hai.”

Phir Krishna ne bataya ki ab woh us Supreme reality ke baare mein batayenge jise truly jaanne par insaan immortality ki taraf badhta hai.

“Woh Supreme Brahman beginning ke bina hai.

Uska koi simple physical form nahi hai.

Uske hands aur feet har taraf hain.

Uski eyes, heads aur faces har direction mein hain.

Woh poore universe mein present hai.

Woh senses ke through experience hone wali qualities ko support karta hai, lekin khud physical senses tak limited nahi hai.

Woh kisi ek cheez se attached nahi hai, phir bhi sabko support karta hai.

Woh creatures ke andar bhi hai aur unke bahar bhi.

Woh bahut subtle hai, isliye normal senses se easily samajh nahi aata.

Woh door bhi lag sakta hai aur bahut near bhi.

Woh sabhi beings ko sustain karta hai.

Wahi creation ka source hai aur dissolution ka bhi.

Woh sabhi lights ke beyond ki light hai.

Aur sabse important—

woh knowledge bhi hai, knowledge ka object bhi hai aur knowledge ka ultimate goal bhi.

Wahi sabke heart mein present hai.”

Krishna bole:

“Arjuna, ab maine tumhe Kshetra, Knowledge aur Object of Knowledge ke baare mein short mein bata diya.

Jo mera devotee is truth ko truly samajh leta hai, woh mere saath spiritually united ho jaata hai.”

Phir Krishna ne Nature aur Spirit ka difference samjhaya.

“Nature, yani Prakriti, aur Spirit, yani Purusha, dono beginning-less hain.

Nature se body aur uski different qualities arise hoti hain.

Pleasure aur pain jaise experiences bhi Nature se connected hain.

Jab Spirit Nature ke saath connected hoti hai, tab woh Nature ki qualities ko experience karti hai.

Isi connection ki wajah se different types ke births ka cycle continue hota hai.”

Krishna ne kaha:

“Is body mein Supreme Purusha ek witness ki tarah present hai.

Woh observe karta hai.

Woh support karta hai.

Woh experience ka witness hai.

Aur wahi Supreme Soul hai.

Jo person Spirit, Nature aur Nature ki qualities ko truly samajh leta hai, woh birth ke cycle se free ho sakta hai.”

Krishna ne bataya ki har person ka path same hona zaroori nahi hai.

“Kuch log meditation ke through apne true Self ko discover karte hain.

Kuch log knowledge ke path ko follow karte hain.

Kuch log selfless actions aur devotion ke through truth tak pahunchte hain.

Aur kuch log khud se ye sab nahi samajh paate, lekin knowledgeable people se sun kar faith ke saath follow karte hain.

Aise log bhi gradually death aur ignorance ke cycle se cross kar sakte hain.”

Phir Krishna ne ek important truth bataya:

“Arjuna, jo bhi moving ya non-moving being duniya mein exist karti hai, woh Kshetra aur Kshetrajna, yani matter aur spirit ke connection se exist karti hai.

Jo person sabhi beings mein same Supreme Lord ko dekhta hai, woh truly see karta hai.

Woh samajhta hai ki body temporary hai, lekin Supreme Self imperishable hai.

Isliye woh kisi being ko unnecessary harm nahi karta.

Aur aisa person highest goal ki taraf badhta hai.”

Krishna ne kaha:

“Jo person ye samajh leta hai ki actions Nature ke through hote hain aur true Self actual doer nahi hai, woh deeper truth ko dekhne lagta hai.

Jab kisi ko ye samajh aa jaata hai ki different beings ke peeche ek hi Supreme reality hai, aur sab kuch usi One source se aata hai, tab woh Brahman ko attain karta hai.”

Krishna ne soul ki purity samjhane ke liye ek simple example diya:

“Jaise space sab jagah present hoti hai, lekin kisi cheez se easily dirty nahi hoti, waise hi Soul body mein present hote hue bhi body ke actions se actually stained nahi hoti.

Aur jaise ek hi Sun poori duniya ko light deta hai, waise hi Spirit poore field of matter ko consciousness ki light deta hai.”

Krishna ne end mein kaha:

“Arjuna, jo person knowledge ki eyes se Matter aur Spirit ka difference samajh leta hai, aur Nature ke bondage se freedom ka path samajh leta hai—

woh Supreme reality ko attain kar leta hai.”

Arjuna ab samajhne laga tha ki woh sirf apni body nahi hai.

Body ek Kshetra hai.

Mind aur senses bhi is field ka part hain.

Lekin in sabko observe karne wala Kshetrajna, yani deeper Self, alag hai.

Aur sabse deep truth ye hai—

Har body ke andar ek eternal Supreme presence hai.

Jo insaan is truth ko truly samajh leta hai, uski thinking badal jaati hai.

Woh body aur temporary situations se beyond apne real Self ko dekhna shuru kar deta hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.26
        with st.expander("Section 6.3.26  Section XXXVIII (Bhagavad Gita Chapter XIV)"):
            text1 = """ Bhagavad Gita – Chapter XIV
Teen Gunas – Sattva, Rajas aur Tamas

Krishna ne Arjuna se kaha:

“Arjuna, ab main tumhe ek aur bahut important knowledge bataunga.

Ye knowledge samajhne ke baad great sages ne body ke bondage se freedom paayi hai.

Jo person is knowledge ko samajh kar meri nature ko attain karta hai, woh dobara birth ke cycle mein nahi phasta.

Universe ki creation ke time bhi woh disturb nahi hota aur destruction ke time bhi nahi.” """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Phir Krishna ne creation ka ek simple secret samjhaya.

“Brahma ek great cosmic womb ki tarah hai.

Main usmein life ka seed place karta hoon.

Usi se different living beings ka birth hota hai.

Chahe koi bhi body ho aur chahe koi bhi womb ho, creation ke peeche Nature aur meri divine energy ka connection hota hai.”

Teen Gunas

Krishna bole:

“Arjuna, Nature se teen qualities arise hoti hain.

Inhe Sattva, Rajas aur Tamas kaha jaata hai.

Ye teen Gunas eternal Soul ko body ke saath bind karte hain.”

1. Sattva – Goodness aur Clarity

“Sattva pure aur bright nature ka hai.

Ye mind ko knowledge aur happiness ki taraf le jaata hai.

Jab Sattva strong hota hai, insaan ka mind clear hota hai.

Usse right aur wrong ko samajhne mein help milti hai.

Lekin Sattva bhi ek attachment create kar sakta hai—knowledge aur happiness ka attachment.”

2. Rajas – Desire aur Action

“Rajas ka main nature hai desire aur attachment.

Jab Rajas strong hota hai, insaan constantly kuch achieve karna chahta hai.

Usse results chahiye.

Woh kaam karta rehta hai.

Naye goals, new desires aur achievements ke peeche bhaagta hai.

Isliye Rajas insaan ko action aur work ke attachment se bind karta hai.”

3. Tamas – Darkness aur Ignorance

“Tamas ignorance se born hota hai.

Ye insaan ke knowledge ko cover kar deta hai.

Phir confusion, laziness aur excessive sleep badhne lagti hai.

Insaan ko right direction samajh nahi aati.

Isliye Tamas insaan ko error, laziness aur ignorance se bind karta hai.”

Krishna ne simple way mein samjhaya:

Sattva → happiness aur knowledge se connect karta hai.

Rajas → action aur desire se connect karta hai.

Tamas → confusion, laziness aur ignorance se connect karta hai.

Kaunsa Guna Kab Strong Hota Hai?

Krishna bole:

“Jab Rajas aur Tamas weak hote hain, Sattva strong hota hai.

Jab Sattva aur Tamas weak hote hain, Rajas strong hota hai.

Aur jab Sattva aur Rajas weak hote hain, Tamas strong ho jaata hai.

Isliye insaan ke mind mein ye teen qualities continuously rise aur fall karti rehti hain.”

Krishna ne unke signs bhi bataye.

“Jab Sattva strong hota hai, body aur mind ke andar knowledge ki light appear hoti hai.

Jab Rajas strong hota hai, insaan mein greed, constant activity, restlessness aur desires badh jaati hain.

Aur jab Tamas strong hota hai, insaan mein darkness, inactivity, confusion aur delusion badhne lagta hai.”

Death ke Time Kaunsa Guna?

Krishna ne kaha:

“Arjuna, agar koi person Sattva ke strong state mein body chhodta hai, to woh higher aur pure regions ko attain karta hai.

Agar Rajas dominate kar raha ho, to person un logon ke beech birth leta hai jo action aur work ke strongly attached hain.

Aur agar Tamas dominate kar raha ho, to birth aisi conditions mein hota hai jahan ignorance zyada hoti hai.

Good actions ka result good hota hai.

Rajas ka result suffering hota hai.

Aur Tamas ka result ignorance hota hai.”

Krishna ne aur clearly samjhaya:

Sattva se knowledge develop hoti hai.

Rajas se greed develop hoti hai.

Tamas se confusion aur ignorance develop hoti hai.

Jo log Sattva mein jeete hain, woh higher direction mein move karte hain.

Jo Rajas mein attached hain, woh middle level par rehte hain.

Aur jo Tamas mein deeply trapped hain, woh lower direction mein chale jaate hain.

Teen Gunas Se Beyond Kaise Jaayein?

Krishna ne kaha:

“Arjuna, real freedom tab aati hai jab insaan in teen Gunas ko bhi cross kar leta hai.

Jab person samajhta hai ki Nature ke Gunas hi actions perform kar rahe hain, aur true Self unse beyond hai, tab woh meri nature ko attain kar sakta hai.

Jo person Sattva, Rajas aur Tamas—teeno ko transcend kar leta hai, woh birth, death, old age aur suffering ke cycle se free ho jaata hai.

Aur woh immortality ko attain karta hai.”

Arjuna ne Krishna se poocha:

“Hey Krishna, jo person in teen Gunas ko cross kar chuka hai, uski pehchaan kya hai?

Woh kaise behave karta hai?

Aur koi person in teen Gunas se beyond kaise ja sakta hai?”

Krishna ne answer diya:

“Jo person light, activity ya confusion ke aane par unse hate nahi karta, aur jab woh chale jaayein to unhe wapas paane ki desire bhi nahi karta—

woh Gunas se beyond jaane laga hai.

Woh in qualities ko observe karta hai, lekin unse control nahi hota.”

Aisa person samajhta hai:

“Ye Gunas apna kaam kar rahe hain. Main inka slave nahi hoon.”

Krishna ne kaha:

“Us person ke liye pleasure aur pain almost same ho jaate hain.

Woh apne andar satisfied rehta hai.

Uske liye mitti ka tukda, stone aur gold equally valuable hote hain.

Usse kisi cheez ka unnecessary attraction nahi hota.

Jo pasand hai aur jo pasand nahi hai, dono mein woh balanced rehta hai.

Praise mile ya criticism, woh easily disturb nahi hota.

Honour mile ya insult, uska mind stable rehta hai.

Friend ho ya enemy, woh dono ko balanced nazar se dekhta hai.

Woh unnecessary worldly competition aur attachment se free ho jaata hai.”

Krishna ne end mein ek important baat kahi:

“Arjuna, jo person exclusive devotion ke saath mujhe worship karta hai, woh in teen Gunas ko transcend karne ke capable ho jaata hai.

Aur jab woh Gunas se beyond chala jaata hai, tab woh Brahman ki nature ko attain karne ke worthy ho jaata hai.

Main hi Brahman ka support hoon.

Main hi immortality ka support hoon.

Main eternal truth ka support hoon.

Aur main hi unbroken happiness ka source hoon.”

Arjuna ne samjha ki real freedom sirf duniya se door bhaagne mein nahi hai.

Real freedom tab hai jab insaan apne andar ke Sattva, Rajas aur Tamas ko pehchane.

Unke influence ko samjhe.

Aur dheere-dheere unse beyond uthne ki koshish kare.

Krishna ka message simple tha:

“Gunas ko dekho, unke slave mat bano. Apna mind steady rakho, attachment kam karo aur devotion ke through unse beyond uthne ki koshish karo.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.27
        with st.expander("Section 6.3.27  Section XXXIX (Bhagavad Gita Chapter XV)"):
            text1 = """ Bhagavad Gita – Chapter XV
Purushottama Yoga – Duniya ka Ulta Tree aur Supreme Being

Sanjaya ne Dhritarashtra ko bataya ki Shri Krishna ne Arjuna ko ek unique example diya.

Krishna bole:

“Arjuna, imagine karo ek bahut bada Ashvattha tree hai.

Lekin ye normal tree jaisa nahi hai.

Iski roots upar hain aur branches neeche faili hui hain.

Iske leaves Vedas ke sacred teachings jaise hain.

Jo is tree ka real meaning samajh leta hai, woh Vedas ka true message samajh leta hai.”

Ye tree actually worldly life ko represent karta hai.

Iski branches upar aur neeche har taraf spread hoti hain.

Teen Gunas—Sattva, Rajas aur Tamas—ise grow karte hain.

Aur sense objects, yani jo hum dekhte, sunte, taste karte aur enjoy karte hain, is tree ke new sprouts jaise hain. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Iski kuch roots human world mein bhi spread hoti hain.

Ye roots insaan ko actions aur unke results ke saath bind karti hain.

Krishna ne kaha:

“Is tree ka true beginning aur end easily samajh nahi aata.

Iski roots bahut strongly fixed hain.

Isliye ise ek powerful weapon se cut karna hoga.

Aur woh weapon hai—

Detachment.”

Yaani worldly desires aur attachments ko control karna hoga.

Tree ko cut karne ka matlab duniya chhod dena nahi tha.

Iska matlab tha duniya ke attachment mein trapped na hona.

Krishna bole:

“Uske baad insaan ko us Supreme place ki search karni chahiye jahan pahunchne ke baad dobara return nahi karna padta.

Us Primeval Supreme Being ki sharan lo jisse ye ancient creation start hui.”

Supreme Place Tak Kaun Pahunchta Hai?

Krishna ne kaha:

“Jo pride aur confusion se free ho jaata hai,

jo attachment ko control kar leta hai,

jo Supreme Self ko samajhne mein steady rehta hai,

jiski unnecessary desires khatam hone lagti hain,

aur jo pleasure aur pain jaise opposites se disturb nahi hota—

woh us eternal destination ko attain kar sakta hai.”

Krishna ne us Supreme place ke baare mein kaha:

“Us place ko light dene ke liye Sun ki zarurat nahi hai.

Moon ki bhi nahi.

Fire ki bhi nahi.

Woh khud divine light se filled hai.

Aur jo wahan pahunch jaata hai, use dobara is worldly cycle mein return nahi karna padta.

Wahi mera Supreme abode hai.”

Har Living Being Mein Divine Soul

Phir Krishna ne Arjuna ko soul ke baare mein samjhaya.

“Is living world mein individual soul meri hi eternal portion hai.

Jab Soul body ke saath connect hoti hai, to woh mind aur five senses ke through duniya ko experience karti hai.”

Krishna ne ek beautiful example diya:

“Jab Soul ek body chhod kar doosri body ki taraf jaati hai, to woh mind aur senses ko apne saath le jaati hai.

Bilkul waise hi jaise wind kisi flower ki fragrance ko apne saath le jaati hai.”

Soul ears ke through sounds experience karti hai.

Eyes ke through forms dekhti hai.

Skin se touch.

Tongue se taste.

Nose se smell.

Aur mind in sab experiences ko process karta hai.

Krishna bole:

“Lekin confused people Soul ko nahi dekh paate.

Woh nahi samajh paate ki Soul body mein kab enter karti hai, kab leave karti hai aur kaise Nature ke Gunas ko experience karti hai.

Lekin jinke paas knowledge ki eyes hain, woh is truth ko samajh lete hain.”

Jo devotees sincerely apne true Self ko jaanne ki koshish karte hain, woh Soul ko apne andar recognize kar sakte hain.

Lekin jinka mind uncontrolled hai, unke liye ye truth samajhna difficult hota hai.

Krishna ki Energy Har Jagah Hai

Krishna ne Arjuna se kaha:

“Sun mein jo light hai aur poore universe ko illuminate karti hai—

woh meri energy hai.

Moon ki light mein jo splendour hai, woh bhi mera hai.

Fire ki brightness bhi mujhse hi aati hai.”

Krishna ne Earth ke baare mein kaha:

“Main apni energy se Earth mein enter karke living beings ko support karta hoon.

Moon ke through main plants aur herbs ko nourish karta hoon.”

Phir Krishna ne daily life ka ek bahut simple example diya.

“Arjuna, living beings ke body ke andar jo digestive fire hai, woh bhi main hoon.

Life-breath ke saath milkar main different types ke food ko digest karta hoon.”

Yaani hum jo food chew karte hain, drink karte hain, lick ya suck karte hain—un sabke digestion ke peeche bhi divine life-energy ka role hai.

Krishna Sabke Heart Mein Hain

Krishna bole:

“Main sabhi living beings ke heart mein present hoon.

Memory mujhse aati hai.

Knowledge mujhse aati hai.

Aur memory aur knowledge ka loss bhi mujhse connected hai.

Saare Vedas ka ultimate purpose mujhe jaana hai.

Main Vedanta ka source hoon.

Aur main hi Vedas ko truly jaanta hoon.”

Teen Levels of Existence

Krishna ne phir Arjuna ko ek aur deep truth samjhaya.

“Is world mein do types ki realities samjhi ja sakti hain.

Ek hai mutable, yani jo continuously change aur destroy hoti hai.

Saare physical living beings aur material forms is category mein aate hain.

Doosri hai immutable, yani jo change nahi hoti.”

Lekin Krishna ne kaha:

“In dono se bhi beyond ek Supreme Being hai.

Use Paramatman kaha jaata hai.

Woh eternal Lord hai.

Woh three worlds mein present hai aur unhe support karta hai.”

Krishna bole:

“Main changing world se beyond hoon.

Aur main immutable reality se bhi higher hoon.

Isi wajah se Vedas aur duniya mujhe Purushottama ke naam se jaante hain.”

Purushottama Ka Meaning

Purushottama ka matlab hai—

The Supreme Being.

Krishna ne kaha:

“Arjuna, jo person confusion se free hokar mujhe Purushottama ke roop mein truly jaan leta hai, woh real knowledge ko attain karta hai.

Phir woh pure heart se mujhe har way mein worship karta hai.”

Krishna ne end mein kaha:

“Arjuna, maine tumhe ek bahut deep aur secret knowledge bata diya hai.

Jo person ise truly samajh leta hai, woh wise ho jaata hai.

Aur usse life ke true purpose ka knowledge mil jaata hai.”

Arjuna silently Krishna ki baat samajhne laga.

Duniya ab use ek huge tree ki tarah dikh rahi thi.

Desires uski branches thi.

Sense pleasures uske sprouts the.

Actions aur attachments uski roots thi.

Aur in sabke beyond tha ek Supreme source—

Purushottama.

Krishna ka message simple tha:

“Duniya mein raho, lekin attachment mein mat phanso. Apne true Self ko samjho, desires ko control karo aur us Supreme source ko seek karo jahan pahunchne ke baad worldly cycle mein return nahi karna padta.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.28
        with st.expander("Section 6.3.28  Section XL (Bhagavad Gita Chapter XVI)"):
            text1 = """ Bhagavad Gita – Chapter XVI
Divine aur Demonic Nature – Insaan ki Asli Pehchaan

Krishna ne Arjuna se kaha:

“Arjuna, har insaan ke andar kuch qualities hoti hain jo uski nature ko show karti hain.

Kuch qualities divine hoti hain, jo insaan ko freedom aur higher life ki taraf le jaati hain.

Aur kuch qualities demonic hoti hain, jo insaan ko bondage aur darkness ki taraf le jaati hain.”

Divine Nature

Krishna bole:

“Jis person mein fearlessness hoti hai, uska heart pure hota hai.

Woh knowledge paane ke liye sincerely effort karta hai.

Yoga aur meditation mein discipline rakhta hai. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Woh charity karta hai.

Apne senses ko control karta hai.

Sacred studies karta hai.

Discipline aur penance follow karta hai.

Truth bolta hai.

Kisi ko unnecessarily hurt nahi karta.

Anger ko control karta hai.

Forgiving hota hai.

Calm rehta hai.

Doosron ki mistakes aur faults ko baar-baar discuss nahi karta.

Sabhi living beings ke liye compassion rakhta hai.

Greedy nahi hota.

Gentle aur humble hota hai.

Unnecessarily restless nahi rehta.

Strong aur energetic hota hai.

Difficult situations mein bhi firm rehta hai.

Clean aur disciplined life jeeta hai.

Fights aur unnecessary arguments se door rehta hai.

Aur sabse important—pride aur vanity se free rehta hai.”

Krishna ne kaha:

“Arjuna, ye sab qualities divine nature ki signs hain.

Aisi qualities insaan ko freedom ki taraf le jaati hain.”

Demonic Nature

Phir Krishna ne opposite nature ke baare mein bataya.

“Hypocrisy, pride, arrogance, anger, rude behaviour aur ignorance—

ye demonic nature ki qualities hain.

Aise log right aur wrong ko clearly samajhne ki koshish nahi karte.

Unhe ye bhi properly pata nahi hota ki kya karna chahiye aur kya avoid karna chahiye.

Unke andar purity, good conduct aur truth ki value kam ho jaati hai.”

Krishna ne kaha:

“Demonic nature wale log believe karte hain ki universe ke peeche koi higher truth ya guiding principle nahi hai.

Unke liye life mainly desires aur enjoyment ke around revolve karti hai.

Is thinking ki wajah se unki intelligence weak hoti jaati hai aur unke actions harsh aur destructive ban sakte hain.”

Endless Desires

Aise logon ki desires kabhi easily satisfy nahi hoti.

“Unke mind mein constantly new desires chalti rehti hain.

Woh kehte hain:

‘Mujhe ye wealth aaj mil jayegi.’

‘Baad mein aur wealth kamaunga.’

‘Ye wealth already mere paas hai.’

‘Ab aur bhi meri hogi.’

‘Maine apne enemy ko defeat kar diya.’

‘Ab main doosre enemies ko bhi defeat karunga.’

‘Main powerful hoon.’

‘Main successful hoon.’

‘Main rich hoon.’

‘Mere jaisa aur kaun hai?’

Aise thoughts mein phanskar unka mind restless hota rehta hai.

Woh wealth, power aur pleasure ko hi life ka highest goal samajhne lagte hain.

Aur dheere-dheere woh apne hi desires ke trap mein phans jaate hain.”

Krishna ne bataya ki ye attachment bahut dangerous ho sakti hai.

“Aise person ki hopes ke bahut saare ropes ban jaate hain.

Desire aur anger usse aur tightly bind karte hain.

Woh constantly wealth aur status ke peeche bhaagta rehta hai.

Uska mind unnecessary thoughts se full rehta hai.

Aur delusion ke trap mein phanskar woh wrong direction mein chala jaata hai.”

Pride aur Power ka Trap

Krishna bole:

“Kuch log wealth aur power ke pride mein itne lost ho jaate hain ki woh religious ya charitable actions bhi sirf show ke liye karte hain.

Unka purpose spiritual growth nahi hota.

Unhe apni wealth, power, status aur success par bahut pride hota hai.

Lust aur anger bhi unke mind ko control karte hain.

Aise log doosron ko disrespect karte hain aur apne andar bhi divine presence ko ignore karte hain.”

Krishna ne kaha:

“Jo log cruelty aur hatred mein jeete hain aur continuously wrong actions karte hain, woh baar-baar lower states mein chale jaate hain.

Unka mind ignorance mein phasta jaata hai.

Aur woh higher truth ko attain nahi kar paate.”

Hell ke Teen Gates

Phir Krishna ne Arjuna ko ek bahut important warning di:

“Arjuna, self-destruction ke teen main gates hain:

Lust.

Anger.

Greed.

In teenon se bachna chahiye.”

Krishna bole:

“Jo person lust, anger aur greed ko control kar leta hai, woh apne welfare ke liye sahi path choose kar sakta hai.

Phir woh gradually highest goal ki taraf move karta hai.”

Scriptures ka Importance

Krishna ne end mein kaha:

“Arjuna, agar koi person scriptures ke guidance ko completely ignore karke sirf apni desires ke according actions karta hai, to woh true perfection, happiness ya highest goal attain nahi kar sakta.

Isliye scriptures ko authority ke roop mein samjho.

Kya karna chahiye aur kya nahi karna chahiye, ye decide karte waqt proper guidance follow karo.

Phir us understanding ke according apna duty perform karo.”

Arjuna ne Krishna ki baat ko deeply samjha.

Usse samajh aa gaya ki divine aur demonic nature kisi special birth ya outer appearance se decide nahi hoti.

Insaan ki daily qualities aur actions uski direction batate hain.

Agar koi truth, compassion, humility, self-control aur forgiveness choose karta hai, to woh higher direction mein badhta hai.

Aur agar koi lust, anger, greed, pride aur hatred ko follow karta hai, to woh khud ko bondage mein daalta hai.

Krishna ka message simple tha:

“Apne andar ke lust, anger aur greed ko control karo. Truth, compassion, humility aur self-discipline ko grow karo. Aur apne actions ko right guidance ke according rakho.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.29
        with st.expander("Section 6.3.29  Section XLI (Bhagavad Gita Chapter XVII)"):
            text1 = """ Bhagavad Gita – Chapter XVII
Shraddha ke Teen Types – Sattva, Rajas aur Tamas

Arjuna ne Krishna se poocha:

“Hey Krishna, jo log scriptures ke rules ko follow nahi karte, lekin faith ke saath worship aur sacrifices karte hain, unki faith kis type ki hoti hai—Sattva, Rajas ya Tamas?”

Krishna bole:

“Arjuna, har insaan ki faith uski nature ke according hoti hai.

Faith bhi teen types ki hoti hai:

Sattvic, Rajasic aur Tamasic.

Insaan jaisi faith rakhta hai, dheere-dheere waisa hi ban jaata hai.”

Teen Types ki Faith

“Jo log Sattva se influenced hote hain, woh higher divine beings ko worship karte hain. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Jo Rajas se influenced hote hain, woh power aur material benefits se related beings ko worship karte hain.

Aur jo Tamas se influenced hote hain, woh dark aur lower forms ki worship ki taraf attract hote hain.”

Krishna ne kuch logon ke baare mein warning bhi di.

“Jo log scriptures ki guidance ke bina bahut harsh penance karte hain, sirf pride, show-off, desire ya attachment ke liye apne body ko torture karte hain, unhe wise nahi kaha ja sakta.

Aise actions unki ignorance ko show karte hain.”

Food bhi Teen Types ka Hota Hai

Krishna ne Arjuna ko food ka example diya.

“Food bhi teen qualities ko reflect karta hai.

Sattvic Food

Jo food life, energy, strength, health aur happiness ko increase karta hai, woh Sattvic hai.

Aisa food fresh, tasty, nutritious aur pleasant hota hai.

Ye body aur mind ko support karta hai.”

Rajasic Food

“Jo food bahut bitter, sour, salty, extremely hot, spicy, dry ya burning hota hai, woh Rajasic nature ka hai.

Aisa food body mein discomfort, pain aur restlessness create kar sakta hai.”

Tamasic Food

“Jo food stale, tasteless, rotten, bad-smelling ya impure ho, woh Tamasic nature ka hai.

Aisa food darkness aur unhealthy habits ko support karta hai.”

Sacrifice ke Teen Types

Krishna bole:

“Sacrifice bhi teen types ka hota hai.

Jo sacrifice scriptures ke according kiya jaata hai aur result ki desire ke bina, sirf duty samajhkar kiya jaata hai—

woh Sattvic hai.

Jo sacrifice reward, benefit ya show-off ke liye kiya jaata hai—

woh Rajasic hai.

Aur jo sacrifice proper rules ke against ho, jisme proper faith na ho, sacred mantras na hon aur respect bhi na ho—

woh Tamasic hai.”

Penance ke Teen Types

Krishna ne bataya ki penance sirf body ko difficult conditions mein rakhna nahi hai.

Penance ke body, speech aur mind—teen forms hote hain.

Body ki Penance

“Gods, teachers aur knowledgeable people ka respect karna.

Clean aur disciplined rehna.

Straightforward behaviour rakhna.

Aur kisi ko unnecessarily hurt na karna—

ye body ki penance hai.”

Speech ki Penance

“Jo speech doosron ko unnecessarily disturb na kare.

Jo truthful ho.

Jo kind aur useful ho.

Aur sacred knowledge ka sincere study kiya jaaye—

ye speech ki penance hai.”

Mind ki Penance

“Mind ko calm rakhna.

Gentle rehna.

Unnecessary talking se bachna.

Apne mind ko control karna.

Aur thoughts ko clean rakhna—

ye mind ki penance hai.”

Krishna ne kaha:

“Jab ye teen types ki penance faith ke saath aur bina reward ki desire ke ki jaati hain, tab woh Sattvic hoti hain.”

Agar penance sirf respect, fame ya honour paane ke liye ki jaaye, to woh Rajasic hai.

Aur agar koi person ignorance mein khud ko torture kare ya kisi doosre ko harm karne ke purpose se penance kare, to woh Tamasic hai.

Charity ke Teen Types

Krishna ne charity ka bhi example diya.

“Jo gift kisi deserving person ko, right time aur right place par diya jaata hai, aur return mein kuch expect nahi kiya jaata—

woh Sattvic charity hai.

Jo gift reluctantly diya jaata hai, ya is hope mein diya jaata hai ki saamne wala future mein favour return karega—

woh Rajasic charity hai.

Aur jo gift wrong place, wrong time ya unworthy person ko disrespect ke saath diya jaata hai—

woh Tamasic charity hai.”

Yaani charity ka value sirf amount se decide nahi hota.

Intention bhi important hai.

OM, TAT, SAT

Krishna ne phir teen sacred words ke baare mein bataya:

OM, TAT aur SAT.

Ye teen Brahman ke traditional designations bataye gaye hain.

OM

“Sacrifice, charity aur penance jaise prescribed actions ko start karte waqt OM ka uchcharan kiya jaata hai.”

TAT

“Jo log liberation ki desire rakhte hain, woh sacrifice, penance aur charity jaise actions ko TAT ke bhaav se karte hain—yaani unke personal reward ki expectation nahi hoti.”

SAT

“SAT ka meaning existence aur goodness ke sense mein use hota hai.

Koi bhi auspicious aur good action bhi SAT se connected maana jaata hai.

Sacrifice, penance aur charity mein steady commitment ko bhi SAT kaha jaata hai.”

Krishna ne end mein ek important baat kahi:

“Arjuna, agar koi person sacrifice kare, charity de, penance kare ya koi bhi good action kare, lekin usmein faith hi na ho, to us action ka real spiritual value nahi hota.

Faith ke bina kiya gaya action SAT ka opposite maana jaata hai.

Aur aisa action na yahan true benefit deta hai, na future mein.”

Chapter ka Simple Message

Krishna Arjuna ko samjha rahe the ki sirf action karna enough nahi hai.

Food kya hai, faith kaisi hai, charity kyun kar rahe ho, penance kis intention se kar rahe ho aur sacrifice kis purpose se kar rahe ho—ye sab matter karta hai.

Sattva insaan ko clarity, health aur goodness ki taraf le jaata hai.

Rajas desire, reward aur restlessness ki taraf le jaata hai.

Tamas ignorance, carelessness aur darkness ki taraf le jaata hai.

Isliye Krishna ka simple message hai:

“Apne actions ke saath apni intention ko bhi pure rakho. Faith, discipline, kindness aur self-control ke saath kaam karo, bina unnecessary reward ki expectation ke.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.30
        with st.expander("Section 6.3.30  Section XLII (Bhagavad Gita Chapter XVIII)"):
            text1 = """ Bhagavad Gita – Chapter XVIII
Moksha Sannyasa Yoga – Tyag, Duty aur Krishna ki Final Teaching

Arjuna ne Krishna se poocha:

“Hey Krishna, main Sannyasa aur Tyag ka real meaning samajhna chahta hoon. Dono mein actual difference kya hai?”

Krishna bole:

“Arjuna, kuch wise people kehte hain ki desire ke saath kiye jaane wale actions ko chhod dena Sannyasa hai.

Aur apne actions ke fruits yani results ka attachment chhod dena Tyag hai.

Lekin meri teaching simple hai.

Sacrifice, charity aur penance ko completely chhodna nahi chahiye.

Inhe karna chahiye, lekin bina attachment aur bina personal reward ki expectation ke.

Ye actions mind ko pure karte hain.”

Tyag ke Teen Types

Krishna bole: """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ “Jo person ignorance ki wajah se apna duty chhod deta hai, uska Tyag Tamasic hai.

Jo person physical difficulty ya pain ke fear se apna duty chhod deta hai, uska Tyag Rajasic hai.

Lekin jo person duty karta hai aur uske result se attachment chhod deta hai—

woh Sattvic Tyag hai.

Aisa person pleasant ya unpleasant work se unnecessary attachment nahi rakhta.

Woh apna duty karta hai, lekin result ko apni identity nahi banata.”

Krishna ne ek important baat kahi:

“Body mein rehne wala person completely actions ko abandon nahi kar sakta.

Isliye real renunciation ka matlab action chhodna nahi hai.

Real Tyag hai—action ke fruit ka attachment chhodna.”

Har Action ke Peeche Five Causes

Krishna ne Arjuna ko bataya:

“Har action ke peeche sirf ek person responsible nahi hota.

Action ke five causes hote hain:

Body ya situation
Agent, yani jo action karta hai
Different organs aur senses
Different efforts
Presiding forces

Body, speech ya mind se kiya gaya koi bhi action in factors ke through complete hota hai.

Isliye jo person ego ke through sochta hai—

‘Main hi sab kuch kar raha hoon’

woh complete truth nahi dekh raha.

Jo person ego se free hai aur apne actions ke fruits se attached nahi hai, woh actions se deeply bound nahi hota.”

Knowledge, Action aur Doer ke Teen Types

Krishna ne phir bataya ki knowledge, action aur doer bhi Sattva, Rajas aur Tamas ke according different hote hain.

Sattvic Knowledge

“Jo person different beings ke andar ek hi eternal reality ko dekhta hai, uska knowledge Sattvic hai.

Woh differences ke peeche unity ko samajhta hai.”

Rajasic Knowledge

“Jo person har being ko completely separate aur different samajhta hai, uska knowledge Rajasic hai.”

Tamasic Knowledge

“Aur jo person sirf ek limited object ko hi complete truth samajh leta hai, bina proper reason aur understanding ke—

uska knowledge Tamasic hai.”

Teen Types ke Actions

“Jo action duty ke according kiya jaata hai, bina attachment aur bina desire ke, woh Sattvic action hai.

Jo action personal desires, ego aur reward ke liye kiya jaata hai aur jisme bahut stress aur struggle hota hai, woh Rajasic action hai.

Aur jo action ignorance mein kiya jaata hai, bina consequences, loss, harm ya apni capability ko samjhe—

woh Tamasic action hai.”

Teen Types ke Doers

“Jo person attachment se free hai, apne achievements ka unnecessary show nahi karta, disciplined aur energetic hai, aur success-failure mein stable rehta hai—

woh Sattvic doer hai.

Jo reward chahta hai, greedy hai, egoistic hai aur success-failure mein extreme happiness aur sadness experience karta hai—

woh Rajasic doer hai.

Aur jo lazy, careless, stubborn, dishonest, confused aur procrastinating hai—

woh Tamasic doer hai.”

Intellect aur Determination

Krishna ne Arjuna ko intellect ke baare mein samjhaya.

“Jo intellect clearly samajhta hai ki:

kya karna hai aur kya nahi karna,

kya right hai aur kya wrong,

kis cheez se fear hona chahiye aur kis se nahi,

aur bondage kya hai aur freedom kya hai—

woh Sattvic intellect hai.”

Rajasic intellect right aur wrong ko clearly distinguish nahi kar pata.

Aur Tamasic intellect darkness ki wajah se wrong ko right aur right ko wrong samajh sakta hai.

Determination bhi teen types ka hota hai.

Jo person apne mind, senses aur life-energy ko discipline aur devotion ke through control karta hai, uski determination Sattvic hai.

Jo person attachment ke through wealth, desires aur achievements ko pakadkar rakhta hai, uski determination Rajasic hai.

Aur jo person sleep, fear, sadness, laziness aur confusion ko chhod nahi paata, uski determination Tamasic hai.

Happiness ke Teen Types

Krishna bole:

“Arjuna, happiness bhi teen types ki hoti hai.”

Sattvic Happiness

“Jo happiness starting mein difficult lagti hai, lekin practice ke saath gradually peaceful aur deeply satisfying ho jaati hai—

woh Sattvic happiness hai.

Starting mein poison jaisi lag sakti hai, lekin end mein nectar jaisi ban jaati hai.”

Jaise discipline, meditation, self-control aur knowledge.

Rajasic Happiness

“Jo happiness starting mein bahut enjoyable lagti hai, lekin baad mein pain create karti hai—

woh Rajasic happiness hai.

Ye mostly senses aur external pleasures se aati hai.”

Tamasic Happiness

“Jo happiness sleep, laziness aur ignorance se aati hai aur starting se hi mind ko dull banati hai—

woh Tamasic happiness hai.”

Krishna ne kaha:

“Nature se born in teen Gunas se koi bhi completely free nahi hai.”

Apna Duty Karo

Krishna ne phir society mein different natural duties ke baare mein bataya.

“Different people ki natural tendencies ke according different duties hoti hain.

Kuch logon ka nature knowledge, discipline, purity aur forgiveness ki taraf hota hai.

Kuch logon ka nature bravery, leadership, protection aur responsibility ki taraf hota hai.

Kuch log agriculture, cattle-care aur trade jaise work karte hain.

Aur kuch log service aur support ke work mein apna contribution dete hain.”

Krishna ne ek important lesson diya:

“Apna duty imperfectly karna bhi better hai than kisi aur ka duty perfectly karna.”

Yaani doosron ki life copy karne ke bajay apni responsibility ko sincerely perform karna chahiye.

Krishna bole:

“Apne natural duty ko sirf isliye mat chhodo kyunki usmein kuch imperfections hain.

Har action mein kuch na kuch limitation hoti hai, bilkul fire ke saath smoke ki tarah.”

Perfection Kaise Milegi?

Krishna ne kaha:

“Jo person apne duties ko sincerely perform karta hai aur attachment gradually chhod deta hai, woh perfection ki taraf badhta hai.

Mind ko control karo.

Unnecessary desires ko reduce karo.

Ego, anger, pride, selfishness aur excessive attachment ko chhodo.

Mind ko peaceful banao.

Meditation aur self-discipline mein steady raho.

Aise person ka mind gradually pure hota jaata hai.

Aur woh Brahman ke highest truth ko understand karne ke worthy ban jaata hai.”

Brahman ko Attain Karna

Krishna bole:

“Jab person Brahman ke saath spiritually united hota hai, tab uske andar deep peace aa jaati hai.

Woh unnecessary grief nahi karta.

Excessive desires bhi nahi rakhta.

Sabhi beings ko equal nazar se dekhta hai.

Aur phir uske andar mere liye highest devotion develop hoti hai.”

“Devotion ke through woh mujhe truly understand karta hai.

Aur jab woh mujhe truly samajh leta hai, tab woh mere saath spiritually united ho jaata hai.”

Krishna ka Final Message to Arjuna

Krishna ne Arjuna se kaha:

“Apne saare actions mere naam dedicate karo.

Mujhe apna refuge banao.

Apne mind ko continuously mujh par fix karo.

Aisa karoge to meri grace se tum difficulties ko cross kar loge.

Lekin agar ego ke influence mein aakar meri baat nahi maanoge, to tumhari problems aur badhengi.”

Arjuna ne kaha:

“Main fight nahi karunga.”

Lekin Krishna bole:

“Arjuna, sirf ego se keh dene se tum apni nature aur duty se escape nahi kar sakte.

Tumhari nature tumhe wahi karne ke liye push karegi jo tumhare duty ka part hai.

Jo kaam tum confusion ki wajah se nahi karna chahte, ho sakta hai circumstances tumhe wahi karne par majboor kar dein.”

Krishna Sabke Heart Mein Hain

Krishna ne kaha:

“Supreme Lord sabhi beings ke heart mein present hai.

Woh Nature ke through sabhi beings ko move karta hai.

Isliye completely uski sharan mein jao.

Uski grace se tumhe supreme peace aur eternal state mil sakti hai.”

Phir Krishna ne Arjuna ko freedom diya:

“Arjuna, maine tumhe ye deep knowledge bata di hai.

Ab ise properly socho.

Samjho.

Aur phir jo tumhe right lage, woh karo.”

Lekin Krishna ne ek baar phir apna sabse loving message diya:

“Tum mujhe bahut dear ho.

Isliye main tumhe tumhare benefit ki baat bata raha hoon.

Apna heart mujh par rakho.

Mere devotee bano.

Mujhe worship karo.

Mujhe bow karo.

Aisa karoge to tum mere paas aaoge.”

Phir Krishna ne kaha:

“Sab kuch chhodkar meri sharan mein aao.

Main tumhe sins aur bondage se free karunga.

Isliye grief mat karo.”

Arjuna ka Final Decision

Krishna ki baat sunne ke baad Arjuna ka confusion completely disappear ho gaya.

Usne kaha:

“Hey Krishna, aapki grace se mera delusion destroy ho gaya hai.

Mujhe apni real understanding yaad aa gayi hai.

Mere doubts clear ho gaye hain.

Ab main firm hoon.

Main aapki baat follow karunga.”

Sanjaya ye sab sun kar bahut amazed tha.

Usne Dhritarashtra se kaha:

“Krishna aur Arjuna ke beech jo conversation maine suni, woh extraordinary thi.

Vyasa ki grace se mujhe Krishna ke mouth se ye supreme knowledge sunne ka opportunity mila.

Jab bhi main Krishna aur Arjuna ki us wonderful conversation ko yaad karta hoon, mujhe baar-baar happiness hoti hai.

Aur jab main Krishna ka divine form yaad karta hoon, mera wonder aur bhi badh jaata hai.”

Sanjaya ne end mein kaha:

“Jahan Krishna hain, aur jahan great warrior Arjuna hai, mere according wahan prosperity, victory, greatness aur eternal righteousness zaroor hoti hai.”

Chapter XVIII ka Simple Moral

Duty karo, lekin result ka attachment mat rakho.

Ego ko kam karo.

Apni nature aur responsibility ko samjho.

Right aur wrong ko clearly samjho.

Mind ko discipline karo.

Aur sabse important—

Krishna par faith rakho aur unki sharan mein jao.

Gita ka final message yahi hai:

“Apna duty sincerely karo, ego aur attachment chhodo, aur Supreme par trust rakho.” """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.31
        with st.expander("Section 6.3.31  Section XLIII"):
            text1 = """ 
            Mahabharat – Section 43: Yudhishthira ka Bado Se Aashirwad Lena
Kurukshetra ka maidan taiyaar tha. Dono taraf ki sena samundar ki tarah faili hui thi. Har taraf yudh ke nagade baj rahe the. Shankh ki awaaz se poora maidan goonj raha tha.

Jab Arjun ne dobara apna dhanush Gandiva uthaya, toh Pandav sena khushi se jhoom uthi. Sabhi yoddhaon ne zor-zor se shankh bajaye.

Tabhi aasman se Devta, Gandharva, Rishi-Muni aur Pitron ki bheed bhi yudh dekhne ke liye aa pahunchi. Sabhi ko pata tha ki aaj ek bahut bada yudh hone wala hai.
Yudhishthira ka achanak faisla
Dono senaein yudh ke liye taiyaar khadi thi. Tabhi Yudhishthira ne ek aisa kaam kiya jise dekhkar sab hairaan reh gaye. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Unhone apna kavach utaar diya, apne hathiyaar rakh diye aur rath se neeche utar aaye.

Phir haath jodkar, bina kuch bole, woh Kaurav sena ki taraf chal pade.

Unke peeche Arjun, Bhim, Nakul, Sahadev aur Shri Krishna bhi chalne lage.

Arjun ne hairaan hokar poocha,

"Jyeshth bhaiya, aap ye kya kar rahe hain? Aap apne hathiyaar chhodkar dushman ki sena ki taraf kyun ja rahe hain?"

Bhim ne kaha,

"Bhaiya, aapne apna kavach aur hathiyaar kyun utaar diye? Saamne dushman ki sena khadi hai. Aap akele unki taraf kyun ja rahe hain?"

Nakul aur Sahadev bhi chinta mein pad gaye.

Lekin Yudhishthira ne kisi ko jawab nahi diya.

Tab Shri Krishna muskuraaye aur bole,

"Main jaanta hoon Yudhishthira kya karne ja rahe hain. Woh yudh shuru hone se pehle apne bado ka aashirwad lene ja rahe hain. Pehle Bhishma Pitamah, Guru Dronacharya, Kripacharya aur Shalya ka samman karenge. Uske baad hi yudh shuru karenge."

Krishna ne aage kaha,

"Hamare shastron mein bhi kaha gaya hai ki jo vyakti apne guru aur bado ka samman karke yudh karta hai, uski jeet ki sambhavna badh jaati hai."
Kaurav sena ka mazaak
Jab Kaurav sena ne Yudhishthira ko apni taraf aate dekha, toh woh hansne lagi.

Kuch yoddha bole,

"Lagta hai Yudhishthira dar gaye hain. Shayad woh Bhishma Pitamah ki sharan mein ja rahe hain!"

Doosre yoddha bole,

"Jiske saath Arjun aur Bhim jaise mahaan yoddha hain, woh khud itna dara hua kyun hai?"

Kaurav sena ke log Yudhishthira aur Pandav bhaiyon ka mazaak udaane lage.

Lekin Yudhishthira bina ruke aage badhte rahe.
Bhishma Pitamah se aashirwad
Yudhishthira sabse pehle Bhishma Pitamah ke paas pahunche.

Unhone Pitamah ke charan pakde aur kaha,

"Pitamah, main aapko pranam karta hoon. Aaj humein aapke khilaaf yudh karna padega. Kripya humein iski anumati dijiye aur apna aashirwad dijiye."

Bhishma Pitamah bahut khush hue.

Unhone kaha,

"Beta, agar tum yudh se pehle mera aashirwad lene nahi aate, toh main tumse bahut naraaz hota. Tumne apne bado ka samman karke bahut achha kiya hai."

Phir unhone kaha,

"Main Kauravon ke dhan aur unki zimmedariyon se bandha hua hoon. Isliye mujhe unki taraf se yudh karna padega. Lekin meri shubhkamnayein hamesha tumhare saath hain."

Yudhishthira ne poocha,

"Pitamah, aapko yudh mein harana lagbhag namumkin hai. Kripya batayein ki hum aapko kaise hara sakte hain?"

Bhishma Pitamah bole,

"Beta, abhi aisa koi yoddha nahi hai jo mujhe yudh mein hara sake. Mere mrityu ka samay bhi abhi nahi aaya hai."

Yudhishthira ne unhe dobara pranam kiya aur aage badh gaye.
Guru Dronacharya se aashirwad
Ab Yudhishthira Guru Dronacharya ke paas pahunche.

Unhone guru ke charan chhuye aur kaha,

"Gurudev, main aapse anumati chahta hoon. Main chahta hoon ki aapke aashirwad se bina kisi paap ke yudh kar sakun aur apne dushmanon par vijay paa sakun."

Dronacharya bahut prasann hue.

Unhone kaha,

"Beta, agar tum mujhse aashirwad lene nahi aate, toh main tumhe shraap de deta. Lekin tumne guru ka samman kiya hai. Main tumhe yudh karne ki anumati deta hoon."

Phir Dronacharya bole,

"Main Kauravon ke dhan se bandha hua hoon. Isliye mujhe unki taraf se ladna padega. Lekin meri prarthana tumhari jeet ke liye hi hogi."

Yudhishthira ne poocha,

"Gurudev, aapko yudh mein kaise haraya ja sakta hai?"

Dronacharya ne jawab diya,

"Jab tak mere haath mein hathiyaar hain aur main yudh kar raha hoon, tab tak tum mujhe nahi hara sakte. Lekin agar mujhe kisi bharosemand vyakti se koi aisi khabar mile jo mere mann ko gehra dukh pahunchaye, toh main apne hathiyaar rakh dunga aur dhyaan mein baith jaunga. Us samay mujhe haraya ja sakta hai."

Yudhishthira ne guru ko pranam kiya aur aage badh gaye.
Kripacharya se mulaqat
Ab Yudhishthira Kripacharya ke paas pahunche.

Unhone unhe pranam karke kaha,

"Acharya, mujhe aapki anumati aur aashirwad chahiye. Main chahta hoon ki aapke aashirwad se hum yudh mein vijay paayein."

Kripacharya ne kaha,

"Beta, agar tum yahan aakar mera samman nahi karte, toh main tumhe shraap de deta. Lekin tumne bahut achha kiya. Main Kauravon ke dhan se bandha hoon, isliye unki taraf se yudh karunga."

Phir unhone kaha,

"Main har din Bhagwan se tumhari jeet ki prarthana karunga."

Yudhishthira ne unhe bhi pranam kiya.
Shalya Mama se aashirwad
Iske baad Yudhishthira apne mama Shalya ke paas pahunche.

Unhone Shalya ko pranam karke kaha,

"Mama, main aapse aashirwad lene aaya hoon. Kripya humein yudh karne ki anumati dijiye."

Shalya bahut khush hue.

Unhone kaha,

"Beta, tumne apne bado ka samman karke bahut achha kiya. Main Kauravon ki taraf se yudh karne ke liye majboor hoon, lekin meri shubhkamnayein tumhare saath hain."

Tab Yudhishthira ne ek khaas madad maangi.

Unhone kaha,

"Mama, jab aapka saamna Karna se ho, toh kripya uska hausla aur uski shakti kam karne ka prayas karna."

Shalya ne kaha,

"Beta, main tumhari ye ichha zaroor poori karunga. Tum nishchint hokar yudh karo."
Krishna aur Karna ki baat
Idhar Shri Krishna Karna ke paas gaye.

Krishna ne Karna se kaha,

"Karna, mujhe pata chala hai ki tum Bhishma Pitamah ke jeevit rehne tak yudh nahi karoge. Tum kuch samay ke liye Pandavon ki taraf aa jao. Bhishma Pitamah ke baad tum chaaho toh dobara Kauravon ki taraf se lad sakte ho."

Lekin Karna ne saaf mana kar diya.

Usne kaha,

"Krishna, main Duryodhana ka saath kabhi nahi chhod sakta. Maine uske liye apni jaan tak dene ka faisla kar liya hai."

Karna ki baat sunkar Krishna wapas Pandavon ke paas aa gaye.
Yuyutsu ka Pandavon ke saath aana
Tabhi Yudhishthira ne zor se kaha,

"Jo bhi hamari taraf se yudh karna chahta hai, woh hamare saath aa sakta hai. Hum uska swagat karenge."

Ye sunkar Dhritarashtra ke bete Yuyutsu aage aaye.

Unhone kaha,

"Maharaj, main aapke saath milkar yudh karna chahta hoon. Main Pandavon ka saath dena chahta hoon. Kya aap mujhe apni sena mein jagah denge?"

Yudhishthira bahut khush hue.

Unhone kaha,

"Yuyutsu, hum tumhara swagat karte hain. Aaj se tum hamare saath ho."

Is tarah Yuyutsu ne apne bhaiyon ka saath chhodkar Pandavon ki sena join kar li.
Yudh ki dobara taiyaari
Ab Yudhishthira ne apna kavach dobara pehna aur apne rath par sawar ho gaye.

Sabhi Pandav yoddha apne-apne rathon par baith gaye.

Dono taraf se nagade aur shankh bajne lage.

Pandav sena mein khushi ki lehar daud gayi.

Sabhi raja aur yoddha Yudhishthira ke vyavhaar ki tareef karne lage.

Unhone kaha,

"Yudhishthira ne yudh se pehle apne guru aur bado ka samman karke bahut bada udaharan diya hai."

Kuch logon ki aankhon mein aansu bhi aa gaye. Sabhi Pandavon ke achhe sanskaar aur bado ke prati samman se prabhavit the.

Aur is tarah, yudh shuru hone se pehle hi Yudhishthira ne apne vyavhaar se sabka dil jeet liya.

Moral of the Story:

Bado aur guruon ka samman karna kabhi nahi chhodna chahiye. Chahe saamne wala hamara dushman hi kyun na ho, uske prati samman aur apne sanskaaron ko hamesha banaye rakhna chahiye. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.32
        with st.expander("Section 6.3.32  Section XLIV"):
            text1 = """ Mahabharat – Section 44: Kurukshetra Yudh Ka Pehla Din
Dhritarashtra ke mann mein ek sawaal tha. Unhone Sanjaya se poocha,

"Jab Kaurav aur Pandav dono ki sena yudh ke liye taiyaar ho gayi thi, toh sabse pehla vaar kisne kiya? Kauravon ne ya Pandavon ne?"

Sanjaya ne jawab dena shuru kiya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Yudh ka pehla kadam
Duryodhana ke bhai Dushasan ne apni sena ke saath aage badhna shuru kiya. Uske saath sabse aage Bhishma Pitamah the.

Dusri taraf Pandav sena bhi poore josh ke saath aage badhi. Unki sena ke aage Bhim khade the.

Dono taraf se yoddha zor-zor se garajne lage. Shankh bajne lage, nagade goonjne lage aur dhol ki awaaz se poora Kurukshetra hilne laga.

Phir dono senaein ek-doosre par toot padi.

Aisa lag raha tha jaise do bade samundar aapas mein takra rahe hon.
Bhim ka bhayankar garjana
Yudh ka shor bahut badh gaya tha. Haathiyon ki awaaz, ghodon ki hin-hinahat aur yoddhaon ki lalkaar se aasman goonj raha tha.

Tabhi Bhim ne ek bhayankar garjana ki.

Unki awaaz itni tez thi ki shankh aur nagadon ka shor bhi uske saamne chhota pad gaya.

Bhim ki garjana badalon ki garaj aur Indra ke vajra ki tarah sunai de rahi thi.

Unki awaaz sunkar Kaurav sena ke yoddha darne lage. Haathi aur ghode bhi ghabra gaye.

Bhim ne apna bhayankar roop dikhaya aur seedhe Kaurav sena par toot pade.
Kaurav Rajkumaron ka Bhim par hamla
Bhim ko aage badhte dekh Duryodhana aur uske kai bhaiyon ne unhe rokne ka faisla kiya.

Unke saath Dushasan, Durmukha, Dussaha, Durmarshana, Vikarna, Chitrasena aur kai doosre bade yoddha bhi the.

Sabhi ne apne dhanush uthaye aur Bhim par teeron ki baarish shuru kar di.

Aisa lag raha tha jaise badal suraj ko poori tarah dhak rahe hon.

Lekin Bhim bhi peeche hatne waalon mein se nahi the.
Pandav Yoddhaon ka jawab
Jab Kaurav yoddhaon ne Bhim ko gher liya, tab Pandav sena ke mahaan yoddha bhi aage aa gaye.

Draupadi ke paanchon bete, Abhimanyu, Nakul, Sahadev aur Dhrishtadyumna ne milkar Kaurav sena par hamla kar diya.

Unke teer itni tezi se chal rahe the jaise aasman se bijli gir rahi ho.

Dono taraf ke yoddha ek-doosre par lagataar teer chala rahe the.

Kisi bhi yoddha ne haar maankar peeche hatna manzoor nahi kiya.
Teeron ki baarish
Ab poora Kurukshetra teeron se bhar gaya tha.

Dhanush ki tankaar ek pal ke liye bhi band nahi ho rahi thi. Teer aasman mein aise chamak rahe the jaise raat ke aasman mein ulkaayein gir rahi hon.

Guru Dronacharya ke shishya apni archery skills dikha rahe the. Woh bina chooke apne nishane par teer maar rahe the.

Dono taraf ke yoddha apne purane dushmani aur badle ko yaad karke poori taakat se lad rahe the.

Maidan mein haathi, ghode aur rath har taraf daud rahe the.
Dhool se dhak gaya Suraj
Jaise-jaise yudh aage badha, zameen par itni dhool udne lagi ki Suraj bhi dhundhla pad gaya.

Hazaaron raja apni-apni sena ke saath yudh mein shaamil ho gaye.

Yudhishthira ke aadesh par Pandav sena ke yoddha Kaurav sena par toot pade.

Dono senaon ke beech itna bhayankar sangharsh hua ki apne aur dushman mein fark karna bhi mushkil ho gaya.

Kabhi koi sena aage badhti, toh kabhi doosri sena use peeche dhakel deti.

Poora maidan ek bade samundar jaisa dikh raha tha. Teer uske magarmachh jaise, dhanush saanp jaise aur talwaarein kachhuon jaise lag rahi thi.

Aur is bhayankar yudh ke beech Bhishma Pitamah apni veerta aur yudh kaushal se sabse alag chamak rahe the.

Is tarah Kurukshetra ke maidan mein Mahabharat ka pehla yudh apni poori bhayankarata ke saath shuru ho gaya.

Moral of the Story:

Mushkil samay mein himmat aur hausla banaye rakhna chahiye. Lekin yaad rakho, kisi bhi yudh ya sangharsh mein sirf taakat hi nahi, balki samajh, dhairya aur sahi faisle bhi bahut zaroori hote hain. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.33
        with st.expander("Section 6.3.33  Section XLV"):
            text1 = """ Mahabharat – Section 45: Yudh Ke Maidan Mein Bhayankar Sangharsh
Subah hote hi Kurukshetra ke maidan mein yudh dobara shuru ho gaya.

Dono taraf ki sena jeetne ke liye taiyaar thi. Har taraf yoddhaon ki garjana, shankh ki awaaz aur hathiyaaron ki takkar sunai de rahi thi.

Ghode zor-zor se hinhina rahe the. Haathi ek-doosre par hamla kar rahe the. Rathon ke pahiyon ki awaaz se poora maidan goonj raha tha.

Aisa lag raha tha jaise poori dharti hil rahi ho. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhishma aur Arjun aamne-saamne
Kaurav sena ki taraf se Bhishma Pitamah apna dhanush lekar Arjun ki taraf badhe.

Arjun ne bhi apna prasiddh dhanush Gandiva utha liya.

Ab dada Bhishma aur unke apne pote jaise Arjun ek-doosre ke saamne the.

Dono ne ek-doosre par teeron ki baarish shuru kar di.

Bhishma ke teer Arjun ko lag rahe the, lekin Arjun zara bhi peeche nahi hate.

Wahin Arjun ke teer bhi Bhishma ko hila nahi paaye.

Dono mahaan yoddha apni poori shakti se lad rahe the.
Satyaki aur Kritavarma ka yudh
Dusri taraf Satyaki aur Kritavarma ke beech bhayankar yudh shuru ho gaya.

Dono ek-doosre par lagataar teer chala rahe the.

Dono ke shareer teeron se bhar gaye the, phir bhi koi haar maanne ko taiyaar nahi tha.

Dono yoddha door se dekhne par aise lag rahe the jaise basant ke mausam mein khile hue do laal phool hon.
Abhimanyu ka shaurya
Arjun ke bete Abhimanyu ka saamna Raja Vrihadvala se hua.

Vrihadvala ne Abhimanyu ke rath ka dhwaj kaat diya aur unke saarathi ko gira diya.

Ye dekhkar Abhimanyu ko bahut gussa aaya.

Unhone turant Vrihadvala par nau teer chalaye. Phir kuch aur teeron se uske rath ka dhwaj, ek rath-rakshak aur saarathi ko bhi nishana banaya.

Dono ke beech yudh jaari raha.
Bhima aur Duryodhana ka saamna
Idhar Bhima aur Duryodhana ek-doosre ke saamne aa gaye.

Dono ke beech pehle se hi gehri dushmani thi.

Duryodhana ne Pandavon ko bahut dukh diya tha. Bhima bhi usse badla lena chahta tha.

Dono ne ek-doosre par teeron ki baarish kar di.

Unka yudh dekhkar wahan maujood sabhi log hairaan reh gaye.
Nakul aur Sahadev ka yudh
Dushasan ne Nakul par kai teer chalaye.

Nakul ne muskuraate hue uska dhanush aur dhwaj kaat diya. Phir us par 25 teer chala diye.

Lekin Duryodhana ne Nakul ke rath ke ghodon ko maar diya aur uska dhwaj bhi gira diya.

Dusri taraf Durmukh ne Sahadev par teeron se hamla kiya.

Sahadev ne bhi jawaab mein ek teer se Durmukh ke saarathi ko gira diya.

Dono ke beech bhayankar yudh hone laga.
Yudhishthira aur Shalya ki takkar
Yudhishthira ka saamna Madra desh ke raja Shalya se hua.

Shalya ne sabke saamne Yudhishthira ka dhanush do tukdon mein kaat diya.

Lekin Yudhishthira ne haar nahi maani.

Unhone turant doosra mazboot dhanush uthaya aur Shalya par teeron se hamla kar diya.
Dhrishtadyumna aur Dronacharya ka yudh
Dhrishtadyumna ne Dronacharya ko yudh ke liye lalkaara.

Dronacharya ne turant Dhrishtadyumna ka dhanush kaat diya aur ek khatarnak teer unke shareer mein maar diya.

Lekin Dhrishtadyumna ne doosra dhanush uthaya aur chaudah teeron se Dronacharya par hamla kar diya.

Dono ke beech zabardast yudh hone laga.
Baaki yoddhaon ke beech bhi sangharsh
Kurukshetra ke doosre hisson mein bhi bhayankar yudh chal raha tha.
- Sankha aur Somadatta ke bete ke beech zabardast takkar hui.
- Dhrishtaketu ne Valhika par hamla kiya.
- Ghatotkacha ka saamna Rakshas Alambusha se hua. Ghatotkacha ne us par 90 teer chala diye.
- Shikhandi aur Ashwatthama ek-doosre par teer barsane lage.
- Raja Virat aur Bhagadatta ke beech yudh hua.
- Kripacharya aur Kaikeya ke raja Brihadkshatra bhi ladne lage.
- Raja Drupad ne Jayadrath ko yudh ke liye lalkaara.
- Vikarna aur Sutasoma ke beech takkar hui.
- Shakuni ka saamna Yudhishthira ke bete Prativindhya se hua.
- Sahadev ke bete Shrutakarma ne Kamboj raja Sudakshina se yudh kiya.
- Arjun ke bete Iravan ne Shrutayush ke ghodon ko maar giraaya.
- Avanti ke raja Vinda aur Anuvinda ne Kuntibhoja par hamla kiya.
Har taraf bade-bade yoddha apni shakti dikha rahe the.
Poora Kurukshetra yudh ka maidan ban gaya
Shuru mein yudh alag-alag jagahon par ho raha tha.

Lekin dheere-dheere sab kuch itna ulajh gaya ki kisi ko samajh nahi aa raha tha ki kaun kiske saath lad raha hai.

Haathi haathiyon se takra rahe the.

Rath wale rath walon se lad rahe the.

Ghudsawar ek-doosre par hamla kar rahe the aur paidal sainik bhi aapas mein bhid rahe the.

Kabhi-kabhi rath ke yoddha zameen par utarkar ladne lagte aur haathiyon ke aas-paas bhi alag-alag tarah ke yoddha yudh karne lagte.

Aasman se Rishi, Siddha aur doosre divya prani bhi is bhayankar yudh ko dekh rahe the.

Unhe ye yudh devtaon aur asuron ke beech hone wale sangharsh jaisa lag raha tha.

Kurukshetra ka maidan ab ek aise bhayankar yudh mein badal chuka tha, jahan har taraf sirf teer, talwaarein, garjana aur yoddhaon ka sangharsh dikhai de raha tha.

Moral of the Story:

Sahas aur himmat mushkil samay mein bahut zaroori hote hain. Lekin yudh mein dono taraf ke logon ko nuksaan hota hai. Isliye gusse aur dushmani se bachkar samajhdari se faisle lena chahiye. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.34
        with st.expander("Section 6.3.34  Section XLVI"):
            text1 = """ Mahabharat – Section 46: Kurukshetra Yudh Ka Bhayankar Roop
Sanjaya ne Dhritarashtra se kaha,

"Maharaj, ab main aapko Kurukshetra ke yudh ka woh bhayankar drishya batata hoon, jahan hazaaron yoddha ek-doosre se lad rahe the."

Yudh ab itna bhayankar ho chuka tha ki kisi ko kisi ki pehchaan nahi reh gayi thi.

Na beta apne pita ko pehchaan raha tha, na pita apne bete ko. Bhai apne bhai se lad raha tha. Mama apne bhanje par hamla kar raha tha aur dost apne hi dost ke saamne khada tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Pandav aur Kaurav dono taraf ke yoddha aise lad rahe the jaise unke andar koi alag hi shakti aa gayi ho.
Rath aur haathiyon ka bhayankar takraav
Yudh ke maidan mein rath ek-doosre se takra rahe the. Kai rathon ke pahiye toot gaye aur kuch rath beech mein hi phans gaye.

Haathi bhi gusse mein ek-doosre par hamla kar rahe the. Woh apne bade-bade daanton se doosre haathiyon ko ghaayal kar rahe the.

Kuch haathi dard se zor-zor se chillane lage. Kuch apne mahawat ke control se bahar hokar idhar-udhar bhaagne lage.

Yudh ke liye trained haathiyon ko bhi unke mahawat bhale aur ankush se aage badha rahe the.

Kai haathi teer, talwaar aur bhale se ghaayal hokar zameen par girne lage.
Paidal sainikon ki ladai
Haathiyon ke aas-paas khade sainik bhi poori taakat se lad rahe the.

Kisi ke haath mein talwaar thi, kisi ke paas gada, bhala, kulhadi ya dhanush tha.

Sabhi yoddha ek-doosre par hamla kar rahe the.

Talwaaron ki takraane ki awaaz poore maidan mein goonj rahi thi.

Kai yoddha ghaayal hokar zameen par gir rahe the. Kuch apne saathiyon ko awaaz laga rahe the, toh kuch apne parivaar walon ko yaad kar rahe the.
Ghudsawaron ka zabardast hamla
Ab ghudsawar bhi yudh mein tezi se aage badhne lage.

Unke ghode bahut tez daud rahe the. Ghudsawar apne haathon mein chamakte hue bhale aur teer lekar dushman par hamla kar rahe the.

Kuch veer ghudsawar uchhal kar doosre rathon ke yoddhaon par vaar kar rahe the.

Kuch rath ke yoddha bhi apne teeron se kai ghudsawaron ko gira rahe the.

Haathi apni soond aur pairon se ghodon aur unke sawaron ko kuchal rahe the.

Poora maidan dhool, teeron aur yoddhaon ki awaazon se bhar gaya tha.
Yudh ka sabse dardnaak drishya
Sanjaya ne bataya ki yudh ab itna khatarnak ho gaya tha ki har taraf ghaayal yoddha pade hue the.

Kisi ka hathiyaar chhoot gaya tha, kisi ke pair mein chot lagi thi aur kisi ke haath ghaayal ho gaye the.

Kai yoddha khoon se lathpath zameen par pade the.

Kuch pyaas se tadap rahe the aur paani maang rahe the.

Kuch apne beton ko bula rahe the, kuch apne pita ko aur kuch apne bhaiyon aur mama ko.

Lekin yudh mein kisi ke paas rukne ka samay nahi tha.

Kuch bahadur yoddha itne ghaayal hone ke baad bhi himmat nahi haar rahe the. Woh dard mein bhi apne hathiyaar pakde hue the.

Kuch yoddha apne rath kho dene ke baad doosre yoddhaon ke rath par jagah maang rahe the, taaki dobara yudh kar sakein.

Kai ghaayal yoddha door se dekhne par khile hue Palash ke phoolon jaise laal dikh rahe the.
Apne hi apno ke saamne
Maharaj, us din Kurukshetra mein sabse dardnaak baat ye thi ki log apne hi rishtedaaron ko maar rahe the.

Kahin pita apne bete ke saamne tha, toh kahin beta apne pita ke saamne.

Kahin mama apne bhanje se lad raha tha, toh kahin dost apne dost ke khilaaf talwaar utha raha tha.

Kisi ko kisi par daya nahi aa rahi thi.

Dono senaon mein har taraf cheekhne aur chillane ki awaazein sunai de rahi thi.
Bhishma Pitamah ka bhayankar roop
Yudh ke beech Pandav sena dheere-dheere kamzor padne lagi.

Jab Pandav yoddha Bhishma Pitamah ke saamne pahunche, toh unke kadam dagmagane lage.

Bhishma Pitamah apne bade se rath par sawar the. Unke rath par chandi se bana ek sundar dhwaj laga tha, jis par taad ke ped aur paanch sitaaron ka nishaan tha.

Woh apne rath par aise chamak rahe the jaise Meru Parvat ki choti par Chandrama chamakta hai.

Unki veerta aur yudh kaushal dekhkar bade-bade yoddha bhi hairaan the.

Aur is tarah Kurukshetra ka yudh aur bhi bhayankar hota chala gaya.

Moral of the Story:

Yudh mein aksar sirf dushman hi nahi, apne bhi kho jaate hain. Gusse aur badle ki aag mein insaan apne rishton ko bhi bhool jaata hai. Isliye kisi bhi vivaad ko samajhdaari aur shanti se suljhane ki koshish karni chahiye. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.35
        with st.expander("Section 6.3.35  Section XLVII"):
            text1 = """ Mahabharat – Section 47: Abhimanyu Aur Bhishma Pitamah Ka Bhayankar Yudh
Sanjaya ne Dhritarashtra se kaha,

"Maharaj, din ka kaafi samay beet chuka tha. Kurukshetra mein yudh lagataar chal raha tha. Har taraf yoddha ek-doosre par hamla kar rahe the."

Duryodhana ne dekha ki Bhishma Pitamah Pandav sena ke beech akele aage badh rahe hain. Unki suraksha ke liye usne paanch mahaan yoddhaon ko bheja.

Ye paanch yoddha the – Durmukha, Kritavarma, Kripacharya, Shalya aur Vivinsati. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ In sabne milkar Bhishma Pitamah ko gher liya aur unki raksha karne lage.

Ab Bhishma Pitamah aur bhi tezi se Pandav sena ke andar ghusne lage.

Unke rath par laga taad ke ped wala dhwaj door se hi dikhai de raha tha.

Bhishma Pitamah apne teeron se dushmanon ke rath aur unke dhwaj kaat rahe the. Unki speed itni tez thi ki aisa lag raha tha jaise woh apne rath par yudh karte hue naach rahe hon.

Unke hamlon se haathi bhi ghaayal hokar zor-zor se chillane lage.
Abhimanyu ne Bhishma Pitamah ko lalkara
Jab Abhimanyu ne dekha ki Bhishma Pitamah Pandav sena ko lagataar nuksaan pahuncha rahe hain, toh unhe bahut gussa aaya.

Woh apne sundar rath par sawar hue. Unke rath ko sundar bhure rang ke ghode kheench rahe the.

Abhimanyu ne bina dare seedha Bhishma Pitamah ki taraf apna rath badha diya.

Unke rath par sone se bana hua ek sundar dhwaj laga tha, jo Karnikar ke ped jaisa dikh raha tha.

Abhimanyu ne sabse pehle apne teer se Bhishma Pitamah ka dhwaj nishana banaya aur use gira diya.

Iske baad unhone Bhishma Pitamah aur unki raksha kar rahe paanchon mahaan yoddhaon par hamla shuru kar diya.
Abhimanyu ki veerta dekh sab hairaan
Abhimanyu ne apne dhanush se ek ke baad ek teer chalane shuru kiye.

Unhone Kritavarma ko ek teer maara, Shalya ko paanch teer maare aur Bhishma Pitamah ko nau teeron se ghaayal kar diya.

Phir unhone apne dhanush ko poori taakat se kheenchkar ek teer chhoda aur dushman ka sone se saja hua dhwaj gira diya.

Unhone Durmukha ke saarathi ko bhi apne teer se nishana banaya aur Kripacharya ka dhanush kaat diya.

Abhimanyu itni tezi se teer chala rahe the ki sab dekhte hi reh gaye.

Unki archery skills dekhkar Devta bhi khush ho gaye.

Wahan maujood sabhi yoddha sochne lage ki Abhimanyu mein bilkul apne pita Arjun jaisi veerta aur nishana lagane ki kala hai.

Unke dhanush ki tankaar bhi Arjun ke Gandiva jaisi sunai de rahi thi.
Bhishma Pitamah ka palatwar
Ab Bhishma Pitamah ne bhi Abhimanyu ko rokne ka faisla kiya.

Unhone turant nau teer chala kar Abhimanyu ko ghaayal kar diya.

Phir teen bade teeron se Abhimanyu ka dhwaj kaat diya.

Unhone Abhimanyu ke saarathi par bhi hamla kiya.

Kritavarma, Kripacharya aur Shalya ne bhi milkar Abhimanyu par teeron ki baarish kar di.

Lekin Abhimanyu bilkul nahi ghabraye.

Woh pahaad ki tarah mazbooti se apne rath par khade rahe aur paanchon yoddhaon ka saamna karte rahe.

Unhone apne teeron se dushmanon ke hamlon ko beasar kar diya aur dobara Bhishma Pitamah par teer barsane lage.
Abhimanyu ne gira diya Bhishma ka dhwaj
Abhimanyu aur Bhishma Pitamah ke beech yudh aur bhi tez ho gaya.

Bhishma Pitamah ne Abhimanyu par kai teer chalaaye, lekin Abhimanyu ne apne teeron se un sabhi ko hawa mein hi kaat diya.

Phir Abhimanyu ne nau teer ek saath chalaye aur Bhishma Pitamah ke rath par lage unke mashhoor dhwaj ko kaat diya.

Woh dhwaj chandi se bana tha aur us par taad ke ped ka nishaan tha.

Jaise hi Bhishma Pitamah ka dhwaj zameen par gira, poora maidan zor-zor se goonj utha.

Bhim ne Abhimanyu ka hausla badhane ke liye zor se garjana ki.

Lekin Bhishma Pitamah bhi haar maanne waale nahi the.

Unhone ab apne divya astron ka istemaal karna shuru kar diya aur hazaaron teeron se Abhimanyu ko gher liya.
Pandav sena Abhimanyu ki madad ke liye aayi
Jab Pandavon ne dekha ki Abhimanyu akele hi itne saare mahaan yoddhaon se lad rahe hain, toh unki raksha ke liye das bade yoddha apne rathon ke saath aage badhe.

Inmein Raja Virat aur unke bete, Dhrishtadyumna, Bhim, paanch Kekaya bhai aur Satyaki shaamil the.

Sabhi Abhimanyu ki madad ke liye Bhishma Pitamah ki taraf badhe.

Lekin Bhishma Pitamah ne unhe bhi nahi chhoda.

Unhone Dhrishtadyumna par teen teer aur Satyaki par das teer chala diye.

Phir ek tez teer se Bhim ke rath par laga sone ka sher wala dhwaj bhi kaat diya.

Bhim ne jawab mein Bhishma Pitamah par teen teer chalaaye. Saath hi Kripacharya aur Kritavarma par bhi hamla kiya.
Uttara aur Shalya ka bhayankar yudh
Isi beech Raja Virat ke bete Uttara ek bade haathi par sawar hokar Shalya ki taraf badhe.

Unka haathi bahut gusse mein tha aur seedha Shalya ke rath par hamla karne laga.

Haathi ne apna pair Shalya ke rath ke aage wale hisse par rakha aur unke chaaron ghodon ko maar diya.

Ab Shalya ka rath wahin ruk gaya.

Shalya ne turant ek lohe ka bhala uthaya aur Uttara par zor se phenk diya.

Woh bhala Uttara ke kavach ko cheer gaya. Uttara apna hosh kho baithe aur haathi se neeche gir pade.

Iske baad Shalya apni talwaar lekar rath se neeche utare.

Unhone Uttara ke haathi ki soond kaat di.

Ghaayal haathi zor se chillaya aur zameen par girkar mar gaya.

Is tarah Shalya ne Uttara ko bhi maar diya.
Bhai ki maut dekh Sveta ka gussa
Jab Raja Virat ke doosre bete Sveta ne apne bhai Uttara ko mara hua dekha, toh woh gusse se aag-baboola ho gaya.

Usne Shalya ko maarne ki kasam kha li.

Sveta ne apna bada dhanush uthaya aur Shalya ke rath ki taraf teeron ki baarish karte hue badhne laga.

Uski taakat dekhkar Kaurav sena ke saat mahaan yoddha Shalya ki raksha ke liye aa gaye.

Ye saat yoddha the:
- Kosala ke Raja Brihadbala
- Magadh ke Jayatsena
- Shalya ke bete Rukmaratha
- Avanti ke Vinda aur Anuvinda
- Kamboj ke Raja Sudakshina
- Sindhu ke Raja Jayadratha
Sabhi ne milkar Sveta ko chaaron taraf se gher liya.
Sveta ka zabardast palatwar
Saaton yoddhaon ne ek saath Sveta par teeron ki baarish kar di.

Lekin Sveta ne himmat nahi haari.

Usne apne saat tez teeron se un saat yoddhaon ke dhanush kaat diye.

Kaurav yoddhaon ne turant naye dhanush uthaye aur dobara hamla kiya.

Lekin Sveta ne phir se apne saat teeron se unke dhanush kaat diye.

Ab saat yoddha gusse se bhar gaye.

Unhone apne-apne bhale uthaye aur ek saath Sveta ke rath ki taraf phenk diye.

Lekin Sveta ne apni teerandaazi se un saat bhallon ko hawa mein hi kaat diya.

Uski veerta dekhkar sab hairaan reh gaye.
Rukmaratha par Sveta ka vaar
Ab Sveta ne apna dhyaan Rukmaratha ki taraf kiya.

Usne ek bahut shaktishaali teer uthaya aur poori taakat se Rukmaratha par chala diya.

Teer seedha Rukmaratha ke sharir mein ja laga.

Woh dard se tadapne laga aur apne rath mein hi behosh hokar gir gaya.

Uska saarathi bina dare use wahan se door le gaya.

Iske baad Sveta ne chhe aur teer chala kar baaki chhe yoddhaon ke rathon ke dhwaj gira diye.

Usne unke ghodon aur saarathiyon ko bhi nishana banaya.

Ab Sveta seedha Shalya ki taraf badhne laga.

Use itni tezi se aata dekh Kaurav sena mein ghabrahat phail gayi.
Duryodhana aur Bhishma ne Shalya ko bachaya
Jab Duryodhana ne dekha ki Sveta Shalya ko maarne ke bahut kareeb pahunch gaya hai, toh woh turant Bhishma Pitamah ke saath apni sena lekar aage badha.

Unhone Shalya ko Sveta ke hamle se bacha liya.

Ab dono senaon ke beech ek aur bhayankar yudh shuru ho gaya.

Rath, haathi aur ghode sab ek-doosre ke beech ulajh gaye.

Bhishma Pitamah ne dobara apne teeron ki baarish shuru kar di.

Unhone Abhimanyu, Bhim, Satyaki, Kekaya ke yoddhaon, Raja Virat, Dhrishtadyumna aur Chedi sena ko apne teeron se gher liya.

Is tarah Kurukshetra ka yudh aur bhi bhayankar hota gaya. Ab Sveta aur Bhishma Pitamah ke beech ek bade sangharsh ki bhoomika taiyaar ho chuki thi.

Moral of the Story:

Asli veerta ka matlab mushkil samay mein himmat nahi haarna hai. Abhimanyu aur Sveta ne dikhaya ki jab saamne kitne bhi bade yoddha kyun na hon, apne hausle aur himmat se unka saamna kiya ja sakta hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.36
        with st.expander("Section 6.3.36  Section XLVIII"):
            text1 = """ Mahabharat – Section 48: Bhishma Pitamah Aur Sveta Ka Antim Yudh
Dhritarashtra ne Sanjaya se poocha,

"Hey Sanjaya, jab Sveta Raja Shalya ko maarne ke liye aage badh raha tha, tab Kaurav aur Pandav sena ne kya kiya? Aur Bhishma Pitamah ne us samay kya kiya? Mujhe poori baat batao."

Sanjaya ne jawab diya,

"Maharaj, jab Sveta Shalya ki taraf badh raha tha, tab dono senaon ke hazaaron veer yoddha yudh ke liye taiyaar ho gaye. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Pandav sena ke kai mahaan yoddha apne senapati Sveta ki madad ke liye aage badhe. Shikhandi bhi unke saath tha.

Sabhi ka ek hi maksad tha – Bhishma Pitamah ko rokna aur apne senapati Sveta ki raksha karna."
Bhishma Pitamah ka bhayankar hamla
Bhishma Pitamah ne apne saamne hazaaron yoddhaon ko dekha, lekin woh bilkul nahi dare.

Unhone apne dhanush se teeron ki baarish shuru kar di.

Unke teer itni tezi se chal rahe the ki aasman tak dhak gaya. Kai yoddhaon ke sir, rath aur dhwaj zameen par girne lage.

Haathi aur ghode bhi unke hamlon se bach nahi pa rahe the.

Bhishma Pitamah akele hi hazaaron yoddhaon ka saamna kar rahe the.

Unki veerta dekhkar Kaurav sena ka hausla badh gaya.
Sveta ne Kaurav sena mein machaya halla
Dusri taraf Sveta bhi apni poori taakat se lad raha tha.

Usne Kaurav sena ke kai bade-bade rajkumaron ko maar giraya.

Uske teeron se kai yoddhaon ke sir, haath aur dhanush katkar zameen par girne lage.

Usne kai rathon, ghodon aur sainikon ko bhi nasht kar diya.

Sveta ka yudh kaushal dekhkar Kaurav sena ke yoddha darne lage.

Kuch yoddha Bhishma Pitamah ko akela chhodkar peeche hat gaye.

Lekin Bhishma Pitamah apni jagah par bilkul mazbooti se khade rahe.

Woh akele hi poori Pandav sena ka saamna kar rahe the.
Bhishma aur Sveta ka aamna-saamna
Jab Bhishma Pitamah ne dekha ki Sveta unki sena ko lagataar nuksaan pahuncha raha hai, toh woh seedhe uski taraf badhe.

Ab dono mahaan yoddha ek-doosre ke saamne the.

Sveta ne Bhishma Pitamah par teeron ki baarish kar di.

Bhishma Pitamah ne bhi turant jawab diya.

Dono ek-doosre ke teeron ko apne teeron se kaat rahe the.

Unka yudh aisa lag raha tha jaise do bade haathi ya do shaktishaali sher aapas mein lad rahe hon.

Bhishma Pitamah itne shaktishaali the ki agar Sveta unhe nahi rokta, toh woh ek hi din mein Pandav sena ko bahut bada nuksaan pahuncha sakte the.

Sveta ko Bhishma Pitamah par bhaari padte dekh Pandav sena khush ho gayi.

Lekin Duryodhana ko ye dekhkar bahut gussa aaya.

Usne apni sena lekar Pandavon par hamla kar diya.
Sveta ka dobara Bhishma par hamla
Sveta ne kuch samay ke liye Bhishma Pitamah ko chhod diya aur Duryodhana ki sena par toot pada.

Usne Kaurav sena ko buri tarah peeche dhakel diya.

Phir gusse se bhara hua Sveta dobara Bhishma Pitamah ke paas pahunch gaya.

Dono ke beech ek baar phir bhayankar yudh shuru ho gaya.

Sveta ne apne dhanush ko poori taakat se kheencha aur saat teer Bhishma Pitamah ke sharir mein maar diye.

Bhishma Pitamah ne bhi turant palatwar kiya aur das teer Sveta par chala diye.

Lekin Sveta pahaad ki tarah apni jagah khada raha.

Usne dobara pachchees teer Bhishma Pitamah par chala diye.

Wahan maujood sabhi yoddha uski veerta dekhkar hairaan reh gaye.
Bhishma Pitamah ka dhanush toot gaya
Ab Sveta ne ek aisa kaam kiya jise dekhkar sabhi dang reh gaye.

Usne lagataar das teer chala kar Bhishma Pitamah ka dhanush das tukdon mein tod diya.

Phir ek aur teer se unke rath par laga taad ke ped wala dhwaj bhi gira diya.

Jaise hi Bhishma Pitamah ka dhwaj zameen par gira, Pandav sena khushi se jhoom uthi.

Sabhi ko laga ki shayad Bhishma Pitamah ab haarne wale hain.

Pandavon ne apne shankh bajane shuru kar diye.

Lekin Duryodhana ye sab dekhkar bahut gusse mein aa gaya.

Usne apne sabhi yoddhaon ko aadesh diya,

"Aaj ya toh Sveta marega ya phir Bhishma Pitamah! Sabhi yoddha Bhishma ki raksha karo!"
Kaurav sena ne Sveta ko gher liya
Duryodhana ke aadesh par kai bade yoddha Bhishma Pitamah ki madad ke liye aage aaye.

Inmein Valhika, Kritavarma, Kripacharya, Shalya, Vikarna, Chitrasena aur kai doosre mahaan yoddha shaamil the.

Sabhi ne milkar Sveta ko chaaron taraf se gher liya.

Lekin Sveta ne bhi haar nahi maani.

Usne apne teeron se sabhi yoddhaon ko rok diya.

Phir usne dobara Bhishma Pitamah ka dhanush kaat diya.

Bhishma Pitamah ne turant doosra dhanush uthaya aur Sveta par teer barsane lage.

Dono ke beech yudh aur bhi bhayankar ho gaya.
Bhishma Pitamah aur Sveta ka antim sangharsh
Sveta ne Bhishma Pitamah ko kai teeron se ghaayal kar diya.

Duryodhana ye dekhkar bahut pareshan ho gaya.

Uski poori sena ko lagne laga ki Bhishma Pitamah shayad ab Sveta se haar jayenge.

Lekin Bhishma Pitamah ne haar nahi maani.

Unhone apna dhairya banaye rakha aur dobara Sveta par hamla shuru kar diya.

Sveta ne bhi unke teeron ko kaat diya aur ek baar phir unka dhanush tod diya.

Bhishma Pitamah ne bina samay gawaaye ek aur bada dhanush utha liya.

Ab unhone faisla kar liya tha ki Sveta ka ant karna hi hoga.
Sveta ka sone ka bhala
Bhishma Pitamah ke teeron se ghaayal hokar Sveta ka rath kamzor pad gaya.

Ab usne apna dhanush chhod diya aur sone se saja hua ek bahut bada bhala uthaya.

Woh bhala itna khatarnak tha ki dekhne mein khud mrityu ke hathiyaar jaisa lag raha tha.

Sveta ne Bhishma Pitamah ko lalkaarte hue kaha,

"Pitamah, thodi der rukiye! Ab mera vaar dekhiye!"

Itna kehkar usne poori taakat se woh bhala Bhishma Pitamah ki taraf phenk diya.

Bhala aasman se girte hue jalte hue ulka pind jaisa dikh raha tha.

Kaurav sena ke yoddha ye dekhkar ghabra gaye.

Lekin Bhishma Pitamah bilkul nahi dare.

Unhone apne dhanush se aath tez teer chalaaye aur Sveta ke bhale ko nau tukdon mein kaat diya.

Bhala zameen par gir gaya.
Sveta ka gada se hamla
Apna bhala tootne ke baad Sveta gusse se bhar gaya.

Usne ek bhaari gada uthayi aur Bhishma Pitamah ki taraf daud pada.

Woh itne gusse mein tha ki uska chehra laal ho gaya tha.

Bhishma Pitamah ne Sveta ka hamla dekha aur turant apne rath se neeche utar gaye.

Sveta ne poori taakat se apni gada ghumayi aur Bhishma Pitamah ke rath par de maari.

Gada ke vaar se Bhishma Pitamah ka poora rath jal kar nasht ho gaya.

Uska dhwaj, saarathi, ghode aur rath ka baaki hissa sab barbaad ho gaya.

Ab Bhishma Pitamah zameen par khade the.

Unhe bachane ke liye Shalya aur doosre Kaurav yoddha turant aage aaye.

Bhishma Pitamah doosre rath par sawar hue.

Tabhi unhe aasman se ek divya awaaz sunai di.

Awaaz ne kaha,

"Hey Bhishma! Der mat karo. Brahma ne is yoddha par vijay paane ka samay nirdharit kar diya hai. Ye tumhare liye sahi samay hai."

Ye awaaz sunkar Bhishma Pitamah ka hausla aur badh gaya.

Unhone Sveta ko maarne ka pakka faisla kar liya.
Pandav yoddha Sveta ki madad ke liye aaye
Jab Pandavon ne dekha ki Sveta ab paidal hi yudh kar raha hai, toh kai bade yoddha uski madad ke liye aage aaye.

Inmein Bhim, Satyaki, Dhrishtadyumna, paanch Kekaya bhai, Dhrishtaketu aur Abhimanyu shaamil the.

Sabhi milkar Bhishma Pitamah ko rokne lage.

Lekin Bhishma Pitamah ne Dronacharya, Shalya aur Kripacharya ki madad se un sabhi yoddhaon ko rok diya.

Ab Sveta ke saamne Bhishma Pitamah khud aa gaye.

Sveta ne ek talwaar uthayi aur Bhishma Pitamah ka dhanush kaat diya.

Bhishma Pitamah ne turant doosra dhanush uthaya aur use taiyaar kar liya.

Ab yudh apne sabse khatarnak mod par pahunch chuka tha.
Bhishma Pitamah ka antim teer
Bhishma Pitamah ne apne tarkash se ek bahut hi shaktishaali teer nikala.

Woh teer kisi aam teer jaisa nahi tha. Usmein Brahmastra jaisi divya shakti thi.

Uski chamak jalti hui aag jaisi thi.

Devta, Gandharva aur doosre divya praani bhi aasman se is yudh ko dekh rahe the.

Bhishma Pitamah ne us teer ko apne dhanush par chadhaya aur poori taakat se Sveta par chala diya.

Woh teer Sveta ke kavach ko cheerkar uske sharir ke paar nikal gaya aur zameen mein ja laga.

Teer ke saath hi Sveta ke praan bhi uske sharir se nikal gaye.

Sveta ek bade pahaad ki choti ki tarah zameen par gir pada.

Is tarah Bhishma Pitamah ne Pandav sena ke mahaan senapati Sveta ka ant kar diya.
Sveta ki maut se dono senaon mein halchal
Sveta ko gira hua dekh Pandav sena ke yoddha dukhi ho gaye.

Unki aankhon mein aansu aa gaye.

Dusri taraf Kaurav sena mein khushi ki lehar daud gayi.

Dushasan toh khushi se yudh ke maidan mein naachne laga.

Kaurav sena ne shankh aur nagade bajakar apni khushi zahir ki.

Pandav sena ke yoddha ab darne lage the, kyunki unke senapati Sveta ki mrityu ho chuki thi.

Apne senapati ko khone ke baad Pandav sena ka hausla toot gaya.

Aakhirkar Arjun aur Shri Krishna ne faisla kiya ki ab dono senaon ko raat ke aaram ke liye wapas apne-apne shiviron mein le jaana chahiye.

Is tarah pehle din ka yudh samaapt hua.

Pandav yoddha apne shiviron mein laut gaye, lekin unke mann mein Sveta ki veerta aur uski dardnaak maut ki yaadein chal rahi thi.

Moral of the Story:

Kabhi-kabhi bahaduri aur poori koshish ke baad bhi jeet nahi milti. Lekin iska matlab ye nahi ki hamari koshish bekaar thi. Sveta ne dikhaya ki asli veer wahi hai jo mushkil se mushkil samay mein bhi apna kartavya nibhata hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.37
        with st.expander("Section 6.3.37  Section XLIX"):
            text1 = """ Mahabharat – Section 49: Bhishma Pitamah Ka Pralayankari Yudh
Sveta ki mrityu ke baad Dhritarashtra ne Sanjaya se poocha,

"Sanjaya, jab Bhishma Pitamah ne Pandav sena ke senapati Sveta ko maar diya, toh Pandavon ne kya kiya? Kya unhone apne senapati ki maut ka badla liya? Aur Arjun ne iske baad kya kiya?"

Dhritarashtra apni sena ki jeet sunkar khush toh the, lekin unke mann mein ek dar bhi tha.

Unhone kaha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ "Mujhe pata hai ki Duryodhana ne Pandavon ke saath bahut galat kiya hai. Maine, Gandhari ne aur Vidur ne use kai baar samjhaya tha. Bhishma Pitamah, Dronacharya aur Kripacharya bhi is yudh ke paksh mein nahi the.

Phir bhi Duryodhana ne Karna aur Shakuni ki baaton mein aakar Pandavon ke saath dushmani ki.

Ab mujhe Arjun ki chinta ho rahi hai. Woh bahut shaktishaali yoddha hai. Jab use Sveta ki maut ka pata chalega, toh woh zaroor gusse mein aa jayega.

Sanjaya, mujhe batao ki uske baad yudh mein kya hua?"
Sanjaya ne Dhritarashtra ko samjhaya
Sanjaya ne kaha,

"Maharaj, ab aapko apni galtiyon ka ehsaas ho raha hai. Lekin ab pachtane se kya fayda?

Ye toh aisa hai jaise paani khatam hone ke baad koi bandh banaye ya ghar mein aag lagne ke baad koi kuaan khodne lage.

Aapko pehle hi galat kaam rokne chahiye the."

Phir Sanjaya ne aage ki kahani sunani shuru ki.
Sankha ka Shalya par hamla
Sveta ki mrityu ke baad Raja Virat ke bete Sankha ne Shalya ko dekha.

Shalya us samay Kritavarma ke saath apne rath par khade the.

Sankha apne bhai Uttara ki maut aur Sveta ke vadh ke baad bahut gusse mein tha.

Usne apna bada dhanush uthaya aur seedha Shalya ko maarne ke liye aage badha.

Sankha ne apne teeron se Shalya ke rath par hamla kar diya.

Use itni tezi se aata dekh Kaurav sena ke saat bade yoddha Shalya ki raksha ke liye aage aa gaye.

Tabhi Bhishma Pitamah bhi ek bahut bada dhanush lekar Sankha ki taraf badhe.

Unki garjana sunkar Pandav sena ghabra gayi.
Arjun ne Sankha ki raksha ki
Jab Arjun ne dekha ki Bhishma Pitamah Sankha ki taraf badh rahe hain, toh woh turant apna rath lekar Sankha ke saamne aa gaye.

Arjun ka maksad Sankha ko Bhishma Pitamah se bachana tha.

Ab ek baar phir mahaan yoddha Bhishma Pitamah aur unke apne shishya Arjun aamne-saamne khade the.

Dono ke beech bhayankar yudh shuru ho gaya.

Dono taraf ke yoddha ye drishya dekhkar hairaan reh gaye.
Sankha ka rath nasht ho gaya
Idhar Shalya ne apni gada uthayi aur Sankha ke rath ke chaaron ghodon ko maar giraaya.

Ab Sankha ka rath wahin ruk gaya.

Sankha turant apne rath se neeche utara aur talwaar lekar Arjun ke rath ki taraf bhaaga.

Woh Arjun ke rath par chadh gaya aur wahan se dobara yudh ke liye taiyaar ho gaya.

Udhar Bhishma Pitamah ke rath se hazaaron teer nikal rahe the.

Aisa lag raha tha jaise aasman aur zameen dono teeron se bhar gaye hon.
Bhishma Pitamah ka bhayankar hamla
Ab Bhishma Pitamah ne apna dhyaan Pandav sena ki taraf kar diya.

Unhone Panchal, Matsya, Kekaya aur Prabhadraka senaon par teeron ki baarish shuru kar di.

Kai yoddha unke hamlon se ghaayal hokar zameen par girne lage.

Phir Bhishma Pitamah ne Arjun ko chhodkar Raja Drupad ki sena ki taraf apna rath badha diya.

Raja Drupad apni sena ke saath yudh kar rahe the.

Bhishma Pitamah ne unki poori sena ko apne teeron se gher liya.

Unke hamlon se aisa lag raha tha jaise sardiyon ke baad kisi sukhe jungle mein bhayankar aag lag gayi ho.

Raja Drupad ki sena dheere-dheere kamzor padne lagi.
Pandav sena mein dar ka mahaul
Bhishma Pitamah ab ek jalti hui aag ki tarah yudh kar rahe the.

Unke teeron ki chamak aur unki speed dekhkar koi bhi unke saamne tik nahi paa raha tha.

Pandav sena ke yoddha unhe dekhkar darne lage.

Unhe samajh nahi aa raha tha ki Bhishma Pitamah ko kaun rokega.

Kai yoddha yudh ka maidan chhodkar peeche hatne lage.

Kuch ghaayal hokar zameen par gir gaye aur kuch apne saathiyon ko awaaz lagane lage.

Bhishma Pitamah har disha mein teer chala rahe the.

Woh jis yoddha ko nishana banate, us par teeron ki baarish kar dete.

Unki veerta dekhkar Kaurav sena ka hausla aur badh gaya.
Suraj dhalne ke saath yudh samaapt
Dheere-dheere Pandav sena poore maidan mein peeche hatne lagi.

Bhishma Pitamah ne apne teeron se unhe buri tarah hara diya tha.

Tabhi aasman mein Suraj dhalne laga aur andhera chhaane laga.

Ab yudh rokne ka samay aa gaya tha.

Bhishma Pitamah apne rath par ab bhi garv ke saath khade the.

Pandav sena apne rathon ke saath wapas apne shivir ki taraf laut gayi.

Unke mann mein apne senapati Sveta ki maut aur aaj ke bhayankar yudh ki yaadein chal rahi thi.

Is tarah Mahabharat ke pehle din ka yudh samaapt hua. Bhishma Pitamah ne apni veerta se Kaurav sena ko badi jeet dilayi, lekin Pandavon ke mann mein ab badle ki aag aur tez ho chuki thi.

Moral of the Story:

Galti hone ke baad pachtane se achha hai ki samay rehte sahi faisla liya jaaye. Galat salah aur ahankaar insaan ko aise raaste par le ja sakte hain jahan se wapas aana bahut mushkil ho jaata hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.38
        with st.expander("Section 6.3.38  Section L"):
            text1 = """ Mahabharat – Section 50: Yudhishthira Ka Hausla Aur Krauncharuma Vyuha
Pehle din ka yudh khatam ho chuka tha. Bhishma Pitamah ne apne teeron se Pandav sena ko buri tarah hara diya tha.

Kaurav sena mein khushi ka mahaul tha. Duryodhana bhi Bhishma Pitamah ki veerta dekhkar bahut prasann tha.

Lekin Pandav shivir mein sabhi udaas the.

Yudhishthira apne bhaiyon aur doosre rajaon ke saath Shri Krishna ke paas gaye. Unke mann mein bahut dukh tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Yudhishthira ki chinta
Yudhishthira ne Krishna se kaha,

"Hey Krishna! Aapne dekha ki Bhishma Pitamah ne hamari sena ka kya haal kar diya hai.

Woh apne teeron se hamare sainikon ko aise khatam kar rahe hain jaise aag sukhi ghaas ko jala deti hai.

Unke saamne hamari sena tik hi nahi paa rahi. Mujhe toh lagta hai ki Yama, Indra, Varuna aur Kubera jaise devta bhi unhe yudh mein nahi hara sakte.

Aisa lag raha hai jaise main Bhishma ke roop mein ek gehre samundar mein doob raha hoon aur mere paas bachne ke liye koi naav bhi nahi hai."

Yudhishthira bahut dukhi hokar bole,

"Krishna, agar aise hi chalta raha toh main apne bhaiyon aur saare mitron ko kho dunga.

Isse achha toh main rajya chhodkar jungle chala jaun aur apni zindagi tapasya mein bita doon.

Main apne bhaiyon aur doston ko apni wajah se marte hue nahi dekh sakta."
Yudhishthira ne Arjun par bhi sawaal uthaya
Yudhishthira ne Krishna se kaha,

"Bhima toh apni poori taakat se lad raha hai. Woh apni gada se paidal sainikon, ghodon, rathon aur haathiyon ko hara raha hai.

Lekin sirf Bhima ke bal par poori Kaurav sena ko harana mumkin nahi hai.

Arjun ke paas divya astron ka gyaan hai. Lekin woh Bhishma aur Dronacharya ko hamari sena ka vinash karte hue dekh raha hai.

Mujhe samajh nahi aa raha ki woh apni poori shakti se yudh kyun nahi kar raha.

Krishna, mujhe koi aisa yoddha bataiye jo Bhishma Pitamah ko rok sake. Warna woh hamari poori sena ko khatam kar denge."

Itna kehkar Yudhishthira chup ho gaye. Unka mann dukh aur chinta se bhara hua tha.
Krishna ne Yudhishthira ko hausla diya
Krishna ne Yudhishthira ko samjhaya,

"Hey Maharaj! Aap itne dukhi mat hoiye.

Aapke saath Bhima, Arjun, Nakul aur Sahadev jaise mahaan yoddha hain.

Main khud aapki madad kar raha hoon. Satyaki, Raja Virat, Raja Drupad aur Dhrishtadyumna bhi aapke saath hain.

Aapki sena mein kai shaktishaali raja aur yoddha hain.

Aur sabse khaas baat, Dhrishtadyumna aapki sena ka senapati hai. Shikhandi bhi aapke saath hai, jo Bhishma Pitamah ki mrityu ka kaaran banega.

Isliye himmat mat hariye."

Krishna ki baatein sunkar Yudhishthira ko thoda hausla mila.
Dhrishtadyumna ne liya yudh ka sankalp
Yudhishthira ne Dhrishtadyumna ko apne paas bulaya aur kaha,

"Dhrishtadyumna! Aap hamari sena ke senapati hain. Ab aapko apni poori shakti se Kaurav sena ka saamna karna hoga.

Jaise devtaon ki sena ka netritva Kartikeya karte the, waise hi aap hamari sena ka netritva kijiye.

Main, Bhima, Krishna, Nakul, Sahadev, Draupadi ke putra aur sabhi mitra raja aapke saath yudh karenge."

Dhrishtadyumna ne garv ke saath jawab diya,

"Maharaj! Mera janm hi Dronacharya ka vadh karne ke liye hua hai. Main Bhishma, Drona, Kripa, Shalya, Jayadratha aur Kaurav sena ke sabhi bade yoddhaon se ladunga.

Main peeche nahi hatunga!"

Unki baat sunkar Pandav sena ke sabhi yoddhaon ne zor se jaykaar ki.
Krauncharuma Vyuha ki rachna
Ab Yudhishthira ne Dhrishtadyumna ko ek khaas yudh-ranneeti banane ka aadesh diya.

Unhone kaha,

"Ek bahut shaktishaali sena-vyuh banao, jiska naam Krauncharuma Vyuha hai. Is vyuh ka gyaan pracheen samay mein Brihaspati ne Indra ko diya tha, jab devta aur asur yudh kar rahe the."

Dhrishtadyumna ne agle din subah is vyuh ki rachna ki.

Ye vyuh ek bade pakshi ke aakar jaisa tha.


Ismein alag-alag yoddhaon ko pakshi ke sir, gardan, pankhon aur peeche ke hisse mein jagah di gayi.
- Sir: Raja Drupad apni badi sena ke saath sabse aage khade hue.
- Aankhen: Raja Kuntibhoja aur Raja Shaivya ko dono aankhon ki jagah rakha gaya.
- Gardan: Dasarna, Prayaga, Kirata aur doosre rajyon ki sena ko yahan rakha gaya.
- Dono pankh: Yudhishthira apni sena ke saath ek pankh par khade hue. Nakul aur Sahadev doosre pankh par tainaat hue.
- Peechhe ka hissa: Raja Virat, Kekaya, Kashi aur Chedi ke rajaon ne sena ki raksha ki.
Iske alawa hazaaron rath aur bade-bade haathi alag-alag jagah par tainaat kiye gaye.
Arjun ka divya rath
Is vyuh ke sabse aage Arjun ko rakha gaya.

Unke rath par laga dhwaj bahut sundar tha. Ye dhwaj devtaon ke shilpkar ne Indra ke aadesh par banaya tha.

Usmein indradhanush jaise rang chamak rahe the.

Arjun apne prasiddh dhanush Gandiva ke saath rath par khade the. Unka dhwaj aasman mein lehrata hua bahut shandaar lag raha tha.

Ab poori Pandav sena kavach pehenkar yudh ke liye taiyaar thi.

Sabhi ko Suraj nikalne ka intezaar tha.

Agla din ek naye aur bhayankar yudh ki shuruaat karne wala tha. Moral of the Story:

Mushkil samay mein himmat haarna nahi chahiye. Sahi salah, achhi planning aur ek-doosre par bharosa rakhkar badi se badi mushkil ka saamna kiya ja sakta hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # Section 6.3.39
        with st.expander("Section 6.3.39  Section LI"):
            text1 = """ Mahabharat – Section 51: Yudh Ke Liye Dono Senaon Ki Taiyari
Sanjaya ne Dhritarashtra se kaha:

Hey Maharaj! Pandavon ki sena ne ek bahut hi powerful aur darawna Krauncha Vyuha banaya tha. Isse dekhkar Duryodhan samajh gaya ki Pandav yudh ke liye poori tarah ready hain.

Woh turant apne Guru Dronacharya, Kripacharya, Shalya, Ashwatthama, Vikarna aur apne bhaiyon ke paas gaya. Uske saath kai bade-bade yoddha bhi khade the.

Duryodhan ne sabhi yoddhaon se kaha:

"Veer yoddhao! Aap sabhi alag-alag tarah ke weapons chalane mein expert hain. Aap mein se har ek akela hi Pandavon ki sena ka saamna kar sakta hai. Aur jab aap sab ek saath ladenge, toh hamari jeet aur bhi pakki ho jayegi.

Hamari sena ki raksha mahaan Pitamah Bhishma kar rahe hain. Isliye hamari sena bahut powerful hai.

Aap sab apni-apni sena ke saath Pitamah Bhishma ki suraksha karein."

Duryodhan ki baatein sunkar sabhi yoddhaon mein josh bhar gaya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dono Senaon Ki Position
Iske baad Bhishma Pitamah aur Dronacharya ne Kaurav sena ko Pandavon ke Vyuha ka saamna karne ke liye arrange kiya.

Sabse aage Bhishma Pitamah apni bahut badi sena ke saath khade hue. Unke peeche Dronacharya apne kai veer yoddhaon ke saath aaye.

Shakuni ne bhi apni sena ke saath Dronacharya ki suraksha ki.

Duryodhan apne sabhi bhaiyon aur kai rajyon ke yoddhaon ke saath khushi-khushi Pandav sena ki taraf badha.

Kaurav sena ke alag-alag hisso ki zimmedari bade-bade yoddhaon ko di gayi.
- Left side: Bhurisrava, Shalya aur Bhagadatta jaise mahaan yoddha tainaat the.
- Right side: Somadatta, Susharma aur Sudakshina jaise yoddha khade the.
- Back side: Ashwatthama, Kripacharya aur Kritavarma apni badi sena ke saath maujood the.
Is tarah Kaurav sena ne har taraf se apni position strong kar li.
Yudh Ka Shankhnaad
Ab dono taraf ki sena yudh ke liye poori tarah taiyaar thi.

Kaurav sena ke yoddhaon ne khushi aur josh ke saath apne-apne shankh bajane shuru kar diye. Poora maidan shankhon aur yoddhaon ki garjana se goonj utha.

Yeh awaaz sunkar mahaan Pitamah Bhishma ne bhi zor se garjana ki aur apna shankh baja diya.

Uske baad Kaurav sena mein dhol, nagade aur kai tarah ke musical instruments bajne lage. Unki awaaz se poora aasman aur dharti goonj uthi.

Lekin Pandav sena bhi peeche nahi thi.

Bhagwan Shri Krishna aur Arjun apne safed ghodon wale divya rath par khade the. Dono ne apne shankh bajaye.
- Shri Krishna ne Panchajanya shankh bajaya.
- Arjun ne Devadatta shankh bajaya.
- Bheem ne apna bada Paundra shankh bajaya.
- Yudhishthir ne Anantavijaya shankh bajaya.
- Nakula ne Sughosha shankh bajaya.
- Sahadev ne Manipushpaka shankh bajaya.
Iske baad Raja Kashi, Shikhandi, Dhrishtadyumna, Virat, Satyaki, Raja Panchal aur Draupadi ke paanchon putron ne bhi apne-apne shankh bajaye.
Yudh Ki Shuruaat
Pandavon ke shankhon ki awaaz itni powerful thi ki poori dharti aur aasman goonj uthe.

Dono taraf ke yoddha apne-apne hathiyaar lekar yudh ke liye aage badhne lage.

Kaurav aur Pandav, dono senaon ke mann mein jeetne ka josh tha.

Ab ek baar phir Kurukshetra ke maidan mein bhayankar yudh shuru hone wala tha! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.40
        with st.expander("Section 6.3.40  Section LII"):
            text1 = """ Mahabharat – Section 52: Arjun Aur Bhishma Pitamah Ka Bhayankar Yudh
Yudh Ki Shuruaat
Dhritarashtra ne Sanjaya se poocha:

"Hey Sanjaya! Jab Kaurav aur Pandav dono senaon ne apni-apni position le li thi, toh sabse pehle yudh kis tarah shuru hua?"

Sanjaya ne jawab diya:

"Hey Maharaj! Dono taraf ke yoddha apne armour aur weapons ke saath yudh ke liye taiyaar khade the. Sabhi ke rathon par unke flags lehra rahe the.

Kaurav sena samundar ki tarah bahut vishal dikh rahi thi. Duryodhan ne apni sena ko dekha aur sabhi yoddhaon se kaha,

'Ab der mat karo! Apne weapons uthao aur yudh shuru karo!'"

Duryodhan ka order milte hi Kaurav sena ke yoddha Pandavon ki taraf daud pade.   """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Kuch hi palon mein Kurukshetra ka maidan bhayankar yudh se bhar gaya. Rathon aur haathiyon ki bheed ek-doosre se takrane lagi. Ghode tezi se daud rahe the aur har taraf arrows ki baarish hone lagi.
Bhishma Pitamah Ka Bhayankar Hamla
Yudh shuru hote hi mahaan Bhishma Pitamah ne apna dhanush uthaya.

Unhone Arjun, Abhimanyu, Raja Kekaya, Raja Virat, Dhrishtadyumna aur Chedi-Matsya sena ke yoddhaon par tezi se arrows barsane shuru kar diye.

Bhishma Pitamah ke attack se Pandav sena mein halchal mach gayi. Kai yoddha apne rath chhodkar peeche hatne lage.

Yeh dekhkar Arjun ko bahut gussa aaya.

Unhone Shri Krishna se kaha:

"Hey Madhav! Hamare Pitamah Bhishma apni poori power se hamari sena par attack kar rahe hain. Agar unhe nahi roka gaya, toh woh hamari poori sena ko khatam kar denge.

Dronacharya, Kripacharya, Shalya aur Vikarna bhi Duryodhan ke saath milkar hamare yoddhaon par hamla kar rahe hain.

Isliye mujhe Pitamah Bhishma ke saamne le chaliye. Main apni sena ki raksha ke liye unka saamna karunga."

Shri Krishna ne jawab diya:

"Chinta mat karo, Parth! Main tumhe abhi Pitamah Bhishma ke rath ke paas lekar chalta hoon."
Arjun Aur Bhishma Aamne-Saamne
Shri Krishna ne apna divya rath Bhishma Pitamah ki taraf badha diya.

Arjun ke rath par Hanuman ji ka flag lehra raha tha. Safed ghode bahut tezi se daud rahe the. Rath ki awaaz badalon ki garjana jaisi thi.

Arjun ne apne Gandiva dhanush se Kaurav sena par arrows barsane shuru kar diye.

Unke attack se kai Kaurav yoddha peeche hatne lage.

Lekin Bhishma Pitamah bhi kisi se kam nahi the. Unhone Arjun ka saamna karne ke liye apni poori power laga di.

Dono mahaan yoddha ek-doosre par arrows barsane lage.

Bhishma Pitamah ne Arjun par 77 arrows chalaye. Dronacharya, Kripacharya, Duryodhan, Shalya, Ashwatthama, Vikarna aur Shakuni ne bhi Arjun par ek saath hamla kiya.

Arjun ka poora sharir arrows se ghira hua tha. Lekin woh bilkul nahi dare. Woh ek pahaad ki tarah apni jagah par date rahe.

Arjun ne bhi jawab mein apne Gandiva se arrows chalaye aur Bhishma, Drona, Kripa aur Duryodhan ko nishana banaya.
Pandav Yoddha Arjun Ki Madad Ke Liye Aaye
Arjun ko akele itne saare Kaurav yoddhaon se ladte dekhkar Satyaki, Virat, Dhrishtadyumna, Abhimanyu aur Draupadi ke paanchon putra unki madad ke liye aa gaye.

Dusri taraf Panchal ke rajkumar ne bhi apni sena ke saath Dronacharya par hamla kar diya.

Ab poora maidan ek bade yudh mein badal chuka tha.

Bhishma Pitamah ne ek baar phir Arjun par 80 sharp arrows chalaye.

Lekin Arjun ne himmat nahi haari. Woh apne dhanush se lagataar arrows chalate rahe.
Duryodhan Ki Chinta
Duryodhan apni sena ko Arjun ke saamne kamzor padte dekhkar pareshan ho gaya.

Woh Bhishma Pitamah ke paas gaya aur bola:

"Hey Pitamah! Arjun aur Shri Krishna milkar hamari sena ko bahut nuksan pahuncha rahe hain. Aap aur Dronacharya jaise mahaan yoddha hamari taraf hain, phir bhi Arjun hamari sena ko khatam kar raha hai.

Karna bhi mere liye yudh nahi kar raha, kyunki woh aapke saamne apne weapons nahi uthana chahta.

Kripya kuch aisa kijiye ki Arjun ko yudh mein haraya ja sake."

Duryodhan ki baatein sunkar Bhishma Pitamah ko gussa aa gaya.

Unhone kaha:

"Kshatriya hone ke naate main apna kartavya zaroor nibhaunga!"

Itna kehkar Bhishma Pitamah apna rath lekar Arjun ki taraf badh gaye.
Bhishma Aur Arjun Ka Maha-Sangram
Dono taraf ke yoddha apne-apne mahaan warriors ko support karne ke liye unke aas-paas khade ho gaye.

Ek taraf Bhishma Pitamah ke saath Duryodhan, Ashwatthama aur Vikarna the.

Dusri taraf Arjun ke saath Shri Krishna aur Pandav sena ke veer yoddha khade the.

Phir dono mahaan dhanurdharon ke beech yudh shuru hua.

Bhishma Pitamah ne Arjun par 9 arrows chalaye. Arjun ne jawab mein 10 arrows chala diye.

Uske baad Arjun ne hazaaron arrows ki baarish kar di. Poora aasman arrows se dhak gaya.

Lekin Bhishma Pitamah ne bhi apne arrows se Arjun ke har attack ko rok diya.

Dono ek-doosre ke attacks ko baar-baar rok rahe the. Kisi ko bhi haar milti nazar nahi aa rahi thi.

Kabhi Arjun ke arrows hawa mein hi katkar gir jaate, toh kabhi Bhishma ke arrows Arjun rok dete.

Dono ne ek-doosre ke ghodon, rathon aur dhanushon ko bhi nishana banaya.
Shri Krishna Par Bhishma Ka Hamla
Yudh ke beech Bhishma Pitamah ne Shri Krishna ke seene par teen arrows chala diye.

Arrows lagne ke baad bhi Shri Krishna bilkul shaant rahe. Unka roop chamakte hue Kinsuka flower jaisa dikh raha tha.

Yeh dekhkar Arjun ko bahut gussa aaya.

Unhone Bhishma Pitamah ke rath ke saarathi par teen arrows chala diye.

Lekin dono taraf ke saarathi bhi bahut skilled the. Woh apne rathon ko itni tezi se ghumate aur aage-peeche le jaate ki kisi ko bhi sahi nishana lagana mushkil ho raha tha.

Dono yoddha baar-baar apni position badal rahe the.

Unke shankhon ki awaaz, dhanushon ki tankaar aur rathon ke pahiyon ki garjana se poori dharti kaanpne lagi.
Devta Bhi Yudh Dekhkar Hairaan Ho Gaye
Bhishma Pitamah aur Arjun ke beech ka yudh itna zabardast tha ki dono taraf ki sena ke yoddha hairaan reh gaye.

Kabhi dono arrows ke baadal ke peeche chhup jaate, toh kabhi achanak sabke saamne aa jaate.

Aasman mein maujood Devta, Gandharva aur Rishis bhi is mahaan yudh ko dekh rahe the.

Unhone ek-doosre se kaha:

"Yeh dono mahaan yoddha hain. Inhe harana kisi ke liye bhi aasaan nahi hai. Na Devta, na Asur aur na hi Gandharva inhe aasani se hara sakte hain.

Aisa yudh shayad hi kabhi dobara dekhne ko mile!"

Sabhi ko lag raha tha ki Arjun aur Bhishma mein se kisi ek ko bhi harana lagbhag namumkin hai.

Dono apni-apni jagah par barabar ki takkar de rahe the.
Kurukshetra Mein Bhayankar Khoon-Kharaba
Jab Arjun aur Bhishma ka maha-sangram chal raha tha, tab baaki Kaurav aur Pandav yoddha bhi ek-doosre se lad rahe the.

Talwarein, kulhadiyan, arrows aur kai tarah ke weapons se yoddha ek-doosre par hamla kar rahe the.

Har taraf bhayankar sangharsh chal raha tha.

Dusri taraf Dronacharya aur Panchal ke rajkumar ke beech bhi ek khatarnak yudh shuru ho gaya.

Is tarah Kurukshetra ka maidan ek bhayankar yudh ka gawah ban gaya, jahan har yoddha apni poori taakat se lad raha tha.

Aur Arjun aur Bhishma Pitamah ka yeh mahaan sangram abhi bhi jaari tha! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.41
        with st.expander("Section 6.3.41  Section LIII"):
            text1 = """ Mahabharat – Section 53: Dronacharya Aur Dhrishtadyumna Ka Bhayankar Yudh
Dhritarashtra Ka Sawaal
Dhritarashtra ne Sanjaya se poocha:

"Hey Sanjaya! Mujhe batao ki Dronacharya aur Panchal ke rajkumar Dhrishtadyumna ke beech yudh kaisa hua?

Mujhe lagta hai ki insaan ki mehnat se zyada kismat powerful hoti hai. Jab mahaan Bhishma Pitamah bhi Arjun ko yudh mein nahi hara paaye, toh iska kya matlab hai?

Bhishma Pitamah toh itne powerful hain ki woh poori duniya ke jeev-jantuon ko hara sakte hain. Phir bhi woh Arjun ke saamne kyun nahi jeet paaye?" """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.41.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dronacharya Ka Dhrishtadyumna Par Hamla
Sanjaya ne jawab diya:

"Hey Maharaj! Ab main aapko Dronacharya aur Dhrishtadyumna ke beech hue bhayankar yudh ke baare mein batata hoon.

Dronacharya ne apne dhanush se Dhrishtadyumna par kai sharp arrows chalaye.

Unhone Dhrishtadyumna ke saarathi ko bhi gira diya aur unke chaaron ghodon ko arrows se ghaayal kar diya.

Lekin Dhrishtadyumna ne bhi haar nahi maani. Unhone Dronacharya par nau arrows chalaye aur zor se kaha,

'Rukiye Guru Dronacharya! Ab mera saamna kijiye!'"

Dhrishtadyumna ka challenge sunkar Dronacharya ne aur bhi powerful attack kiya.

Unhone ek bahut hi khatarnak arrow nikala. Uski power Bhagwan Indra ke vajra jaisi thi.

Woh arrow Dhrishtadyumna ko khatam kar sakta tha.

Yeh dekhkar dono senaon ke yoddha dar gaye. Sabhi ko laga ki ab Dhrishtadyumna bach nahi paayenge.
Dhrishtadyumna Ne Dikhayi Apni Himmat
Lekin Dhrishtadyumna bilkul nahi dare.

Woh ek pahaad ki tarah apni jagah par khade rahe.

Jaise hi Dronacharya ka powerful arrow unki taraf aaya, Dhrishtadyumna ne apne arrows se usse beech mein hi kaat diya.

Phir unhone Dronacharya par arrows ki baarish kar di.

Yeh dekhkar Pandav aur Panchal sena khushi se zor-zor se chillane lagi.

Dhrishtadyumna ne ab Dronacharya ko harane ka faisla kar liya tha.

Unhone ek powerful spear uthaya, jo gold aur sundar neele gemstones se saja hua tha.

Unhone poori taakat se woh spear Dronacharya ki taraf phenk diya.

Lekin Dronacharya ne apne dhanush se us spear ko hawa mein hi teen tukdon mein kaat diya.

Dhrishtadyumna ne phir se arrows barsane shuru kar diye.

Dronacharya ne unke saare attacks rok diye aur mauka milte hi unka dhanush kaat diya.
Dronacharya Ka Zabardast Attack
Dhanush tootne ke baad bhi Dhrishtadyumna ne haar nahi maani.

Unhone ek bahut bhaari gada uthayi aur poori taakat se Dronacharya ki taraf phenk di.

Lekin Dronacharya ne apne rath ko tezi se ghumakar us gada se khud ko bacha liya.

Phir unhone Dhrishtadyumna par bahut saare sharp arrows chalaye.

Arrows unke armour ko paar kar gaye aur Dhrishtadyumna ghaayal ho gaye.

Lekin Dhrishtadyumna ne phir se ek naya dhanush uthaya aur Dronacharya par paanch arrows chala diye.

Dono mahaan yoddha arrows se ghaayal ho chuke the. Unke sharir par khoon laga hua tha.

Phir bhi dono apni poori taakat se lad rahe the.
Dronacharya Ne Dhrishtadyumna Ka Rath Tod Diya
Dronacharya ab aur bhi gusse mein aa gaye.

Unhone ek baar phir Dhrishtadyumna ka dhanush kaat diya.

Uske baad unhone lagataar arrows chalakar:
- Dhrishtadyumna ke saarathi ko gira diya.
- Unke chaaron ghodon ko maar diya.
- Unke rath ko bekaar kar diya.
- Unke haath mein pehne leather protection ko bhi kaat diya.
Ab Dhrishtadyumna ke paas na rath tha, na ghode aur na hi dhanush.

Woh apne rath se neeche utare aur ek bhaari gada lekar Dronacharya ki taraf badhne lage.

Lekin Dronacharya ne apne arrows se us gada ko bhi tukdon mein kaat diya.

Yeh dekhkar sabhi yoddha hairaan reh gaye.
Dhrishtadyumna Ka Aakhri Attack
Dhrishtadyumna ne ab ek bada shield aur tez talwar uthayi.

Unka shield bahut sundar tha aur uspar chaand jaisi designs bani hui thi.

Woh ek gusse se bhare sher ki tarah Dronacharya ki taraf daude.

Lekin Dronacharya ne apne arrows se unka raasta rok diya.

Dhrishtadyumna apne shield se arrows ko rok rahe the, lekin Dronacharya ke attacks itne powerful the ki woh aage nahi badh paa rahe the.
Bheem Ne Dhrishtadyumna Ki Madad Ki
Jab Dhrishtadyumna mushkil mein the, tab mahaan Bheem unki madad ke liye aa gaye.

Bheem ne Dronacharya par saat sharp arrows chalaye.

Phir unhone Dhrishtadyumna ko apne doosre rath par surakshit jagah pahucha diya.

Yeh dekhkar Duryodhan ne apni sena ke Kalinga yoddhaon ko order diya:

"Jao! Dronacharya ki raksha karo aur Bheem ko roko!"

Duryodhan ka order milte hi Kalinga sena apni badi army ke saath Bheem ki taraf daud padi.

Dusri taraf Dronacharya ne Dhrishtadyumna ko chhodkar Raja Virat aur Raja Drupad par hamla kar diya.

Dhrishtadyumna bhi ab Raja Yudhishthir ki madad ke liye pahunch gaye.
Bheem Aur Kalinga Sena Ka Maha-Sangram
Ab ek naya aur bhayankar yudh shuru hone wala tha.

Ek taraf mahaan Bheem the aur doosri taraf Kalinga ki bahut badi sena.

Kalinga ke yoddha Bheem ko chaaron taraf se gherne ke liye aage badhe.

Lekin Bheem bhi kisi se darne wale nahi the.

Dono taraf ke yoddha apne weapons lekar ek-doosre par toot pade.

Kurukshetra ka maidan ek baar phir bhayankar yudh se goonj utha!

Ab dekhna tha ki Bheem akele Kalinga ki itni badi sena ka saamna kaise karenge! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.42
        with st.expander("Section 6.3.42  Section LIV"):
            text1 = """ Mahabharat – Section 54: Bheem Aur Kalinga Sena Ka Bhayankar Sangram
Dhritarashtra Ka Sawaal
Dhritarashtra ne Sanjaya se poocha:

"Hey Sanjaya! Mujhe batao ki mere bete Duryodhan ke kehne par Kalinga ke raja ne apni badi sena ke saath mahaan Bheem ka saamna kaise kiya?

Bheem apni gada lekar yudh ke maidan mein ghoom rahe the. Woh kisi kaal ki tarah dikh rahe the. Kalinga ki sena unke saamne kaise tik paayi?" """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.42.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Kalinga Sena Ne Bheem Ko Gher Liya
Sanjaya ne jawab diya:

"Hey Maharaj! Duryodhan ka order milte hi Kalinga ke raja apni vishal sena lekar Bheem ki taraf badhe.

Bheem ke saath Chedi sena ke yoddha bhi the. Unhone Kalinga sena ka saamna karne ke liye aage badhna shuru kiya.

Kalinga sena mein hazaaron rath, ghode aur haathi the. Unke saath Nishad rajkumar Ketumat aur yoddha Shrutayu bhi maujood the.

Kalinga ke raja ke paas hazaaron rath the, jabki Ketumat ke saath 10,000 haathiyon ki sena thi.

Un sabhi ne milkar Bheem ko chaaron taraf se gher liya.

Lekin Bheem bilkul nahi dare."
Bheem Aur Kalinga Sena Ka Maha-Yudh
Chedi, Matsya aur Karusha ke yoddha bhi Bheem ke saath Kalinga sena par toot pade.

Dono taraf se yoddha ek-doosre par hamla karne lage.

Yudh itna bhayankar tha ki poora maidan hilne laga. Har taraf arrows aur weapons chal rahe the.

Yoddha itni tezi se lad rahe the ki kai baar unhe apne aur dushman ke beech ka fark bhi samajh nahi aa raha tha.

Kuch yoddha galti se apne hi saathiyon par hamla karne lage.

Chedi sena ne apni poori taakat laga di, lekin Kalinga aur Nishad sena ki sankhya bahut zyada thi.

Aakhirkar Chedi ke kai yoddha peeche hat gaye.

Lekin Bheem ne haar nahi maani.

Woh akele hi Kalinga sena ka saamna karte rahe.
Bheem Ka Rath Nasht Ho Gaya
Bheem ne apne rath se Kalinga sena par tezi se arrows barsane shuru kar diye.

Yeh dekhkar Kalinga ke raja aur unke bete Sakradev ne bhi Bheem par arrows chalaye.

Dono taraf se lagataar hamle hone lage.

Kalinga ke raja ne Bheem ke ghodon ko arrows se maar diya.

Ab Bheem ka rath ruk gaya.

Yeh mauka dekhkar Sakradev apne rath se Bheem ki taraf badha aur un par arrows ki baarish karne laga.

Lekin Bheem ne apni bhaari lohe ki gada uthayi aur poori taakat se Sakradev ke rath par phenk di.

Gada seedha Sakradev ko lagi.

Sakradev apne saarathi aur rath ke saath zameen par gir gaya aur uski mrityu ho gayi.

Apne bete ko mara hua dekhkar Kalinga ke raja ko bahut gussa aaya.

Unhone hazaaron rathon ke saath Bheem ko chaaron taraf se gher liya.
Bheem Ki Talwar Ka Kamal
Ab Bheem ne apni gada chhodkar ek badi aur tez talwar utha li.

Dusri taraf Kalinga ke raja ne ek zehrele saanp jaisa khatarnak arrow Bheem par chala diya.

Lekin Bheem ne apni talwar se us arrow ko hawa mein hi do tukdon mein kaat diya.

Yeh dekhkar Kalinga sena hairaan reh gayi.

Kalinga ke raja ne phir 14 khatarnak darts Bheem ki taraf phenke.

Lekin Bheem ne apni talwar se un sabhi ko bhi hawa mein hi kaat diya.

Ab Bheem ne Kalinga ke ek aur rajkumar Bhanumat ko apna nishana banaya.

Bhanumat ne Bheem par arrows barsaye aur zor se garjana ki.

Bheem ne bhi itni zor se garjana ki ki Kalinga sena ke yoddha darne lage.

Unhe lagne laga ki Bheem koi aam insaan nahi, balki khud Mrityu hain.
Bheem Ne Haathi Par Chadkar Bhanumat Ko Hara Diya
Bheem ne zor se garjana ki aur talwar lekar Bhanumat ke vishal haathi par chadh gaye.

Haathi ke daanton ka sahara lekar woh uski peeth tak pahunch gaye.

Phir Bheem ne apni bhaari talwar se Bhanumat par vaar kiya.

Bhanumat wahi maara gaya.

Iske baad Bheem ne us vishal haathi ki gardan par bhi talwar se vaar kiya.

Haathi ka sir alag ho gaya aur woh ek bade pahaad ki tarah zameen par gir pada.

Bheem turant haathi se neeche utar aaye.

Ab woh talwar lekar paidal hi Kalinga sena ke beech ghus gaye.
Bheem Ka Bhayankar Yudh
Bheem itni tezi se lad rahe the ki dushman yoddha unki movements samajh hi nahi paa rahe the.

Kabhi woh aage badhte, kabhi uchhal kar hamla karte aur kabhi ek taraf se doosri taraf pahunch jaate.

Woh apni talwar se ghodon, haathiyon aur rathon par hamla kar rahe the.

Kai yoddha unke dar se bhaagne lage.

Bheem ki speed aur strength dekhkar aisa lag raha tha jaise koi jalta hua aag ka gola poori sena ke beech ghoom raha ho.

Unki garjana se dushmanon ke hosh ud rahe the.

Kai haathi ghaayal hokar apni hi sena ke yoddhaon ko kuchalne lage.

Kalinga sena mein har taraf afra-tafri mach gayi.
Kalinga Ke Raja Aur Bheem Ka Saamna
Ab Kalinga ke raja Shrutayush ne khud Bheem ka saamna karne ka faisla kiya.

Unhone Bheem ke seene par nau arrows chala diye.

Arrows lagne se Bheem ko bahut gussa aaya.

Tabhi Ashok naam ke ek kushal saarathi ne sone se saja hua ek naya rath Bheem ke paas laaya.

Bheem us rath par chadh gaye aur Shrutayush ki taraf badhte hue bole:

"Rukiye! Ab mera saamna kijiye!"

Shrutayush ne bhi Bheem par kai sharp arrows chalaye.

Lekin Bheem ne apna dhanush uthaya aur poori taakat se saat lohe ke arrows chalaye.

Un arrows se Kalinga ke raja Shrutayush ki mrityu ho gayi.

Iske baad Bheem ne Kalinga ke rath ke dono protectors ko bhi maar diya.

Unhone Satyadev, Satya aur Nishad rajkumar Ketumat ko bhi yudh mein hara diya.

Ab Kalinga sena ke kai bade-bade yoddha maare ja chuke the.
Bheem Ne Kalinga Sena Ko Hila Diya
Apne raja aur bade yoddhaon ko khone ke baad Kalinga sena aur bhi gusse mein aa gayi.

Hazaaron Kalinga yoddha Bheem ko chaaron taraf se gherkar un par arrows, gada, talwar aur bhale se hamla karne lage.

Bheem ne apni gada uthayi aur rath se neeche kood pade.

Ab woh paidal hi dushmanon ka saamna karne lage.

Unhone 700 yoddhaon ko maar giraya. Iske alawa 2,000 Kalinga yoddha bhi unke haathon maare gaye.

Unki taakat dekhkar sabhi hairaan reh gaye.

Bheem ne apna shankh bajaya. Uski tez awaaz sunkar Kalinga sena ke yoddha kaanpne lage.

Kisi ko samajh nahi aa raha tha ki Bheem ko kaise roka jaaye.

Aakhirkar Kalinga sena ke yoddha darr ke maare alag-alag dishaon mein bhaagne lage.
Pandav Sena Bheem Ki Madad Ke Liye Aayi
Jab Kalinga sena dobara ikatthi hui, tab Pandav sena ke commander Dhrishtadyumna ne apne yoddhaon ko order diya:

"Veer yoddhao! Aage badho aur yudh karo!"

Shikhandi aur kai bade Pandav yoddha apni sena lekar Bheem ki madad ke liye pahunch gaye.

Raja Yudhishthir bhi haathiyon ki ek badi sena ke saath wahan aa gaye.

Dhrishtadyumna ne apne yoddhaon ke saath Bheem ke ek taraf ki suraksha sambhaal li.

Dhrishtadyumna Bheem ko bahut pasand karte the. Unke liye Bheem aur Satyaki apni jaan se bhi zyada pyaare the.

Bheem ne Dhrishtadyumna ke laal flag wale sone se saje rath ko dekha toh unhe bahut rahat mili.

Ab unke saath aur bhi veer yoddha aa chuke the.
Satyaki Bhi Yudh Mein Shamil Hue
Dhrishtadyumna aur Bheem ne Satyaki ko door se aate dekha.

Satyaki bhi apne rath ke saath Kalinga sena par toot pade.

Ab Bheem, Dhrishtadyumna aur Satyaki teenon milkar Kalinga sena ka saamna karne lage.

Teenon ki taakat se Kalinga sena ko bahut nuksan hua.

Bheem ke hamlon se poora maidan khoon se bhar gaya.

Kalinga sena ke yoddha darr kar kehne lage:

"Yeh Bheem nahi, balki khud Mrityu hain jo hamare saamne yudh kar rahe hain!"
Bhishma Pitamah Bheem Ko Rokne Aaye
Kalinga sena ki haalat dekhkar Bhishma Pitamah ko bhi yudh ke maidan mein aana pada.

Woh apni sena ke saath Bheem ki taraf badhe.

Bheem, Satyaki aur Dhrishtadyumna ne milkar Bhishma Pitamah ke rath par teen-teen arrows chalaye.

Lekin Bhishma Pitamah ne bhi jawab mein teeno yoddhaon par teen-teen arrows chalaye.

Phir Bhishma Pitamah ne hazaaron arrows barsakar Bheem ke rath ke ghodon ko maar diya.

Bheem ne gusse mein ek bhaari lohe ka bhala uthaya aur Bhishma ke rath ki taraf phenk diya.

Lekin Bhishma Pitamah ne us bhale ko hawa mein hi do tukdon mein kaat diya.

Ab Bheem apne rath se neeche utar aaye.

Dhrishtadyumna ne turant Bheem ko apne rath par bitha liya.

Dusri taraf Satyaki ne Bhishma Pitamah ke saarathi par arrow chala diya.

Saarathi ke girte hi Bhishma Pitamah ka rath bina control ke ghodon ke saath yudh ke maidan se door chala gaya.
Bheem Ki Jeet
Bhishma Pitamah ke maidan se door jaate hi Bheem aur bhi zyada josh mein aa gaye.

Unhone Kalinga sena par dobara hamla kar diya.

Ab Kalinga sena ka koi bhi yoddha unka saamna karne ki himmat nahi kar pa raha tha.

Pandav aur Matsya sena ke yoddha Bheem ki bahaduri se bahut khush hue.

Bheem ne Dhrishtadyumna ko gale lagaya aur phir Satyaki ke paas gaye.

Satyaki ne khushi se Bheem se kaha:

"Bahut achha hua Bheem! Aapne akele hi Kalinga ke raja, Ketumat, Sakradev aur unki poori sena ko hara diya.

Aapki taakat aur bahaduri ke saamne koi nahi tik saka. Aapne haathiyon, ghodon aur rathon se bhari itni badi sena ko hara diya. Yeh sach mein bahut badi jeet hai!"

Yeh sunkar Bheem bahut khush hue.

Satyaki ne Bheem ko gale lagaya aur phir apne rath par baithkar Kaurav sena par dobara hamla karne chale gaye.

Is tarah Bheem ne apni bahaduri aur taakat se Kalinga ki vishal sena ko hara diya. Kurukshetra ke maidan mein unka naam ek mahaan yoddha ke roop mein goonjne laga! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.43
        with st.expander("Section 6.3.43  Section LV"):
            text1 = """ Mahabharat – Section 55: Abhimanyu Aur Arjun Ka Bhayankar Yudh
Dhrishtadyumna Aur Kaurav Yoddhaon Ka Sangharsh
Sanjaya ne Dhritarashtra se kaha:

"Hey Maharaj! Din ka pehla hissa beet chuka tha. Kurukshetra ke maidan mein yudh lagataar chal raha tha. Kai rath, haathi, ghode aur paidal yoddha maare ja chuke the.

Isi dauraan Panchal ke rajkumar Dhrishtadyumna ka saamna Dronacharya ke bete Ashwatthama, Shalya aur Kripacharya se hua. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.43.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dhrishtadyumna ne apne arrows se Ashwatthama ke ghodon ko maar giraya.

Ab Ashwatthama ke paas rath nahi tha. Isliye woh Shalya ke rath par chadh gaye aur wahan se Dhrishtadyumna par arrows barsane lage.

Yeh dekhkar Abhimanyu turant apne rath ke saath Dhrishtadyumna ki madad ke liye pahunch gaye.
Abhimanyu Ka Teen Maha-Yoddhaon Se Muqabla
Abhimanyu ne aate hi Shalya par 25 arrows, Kripacharya par 9 arrows aur Ashwatthama par 8 arrows chala diye.

Lekin Ashwatthama, Shalya aur Kripacharya ne bhi Abhimanyu par palatkar hamla kiya.

Tabhi Duryodhan ka beta Lakshman wahan aa gaya.

Apne pita ke dushmanon ko saamne dekhkar Lakshman ko bahut gussa aaya. Usne Abhimanyu par sharp arrows chalane shuru kar diye.

Ab dono yuva rajkumaron ke beech bhayankar yudh shuru ho gaya.

Abhimanyu ne apni tezi aur skill dikhate hue Lakshman par 500 arrows chala diye.

Lekin Lakshman ne bhi mauka dekhkar Abhimanyu ka dhanush beech se kaat diya.

Yeh dekhkar Kaurav sena ke yoddha khushi se chillane lage.

Par Abhimanyu ne haar nahi maani. Unhone turant apna doosra aur bhi powerful dhanush utha liya.

Dono rajkumar ek-doosre par lagataar arrows chalane lage.
Duryodhan Apne Bete Ki Madad Ke Liye Aaya
Duryodhan ne jab dekha ki uska beta Lakshman Abhimanyu ke saamne mushkil mein hai, toh woh khud uski madad ke liye aage badha.

Duryodhan ko aata dekh Kaurav sena ke kai raja apne-apne rathon ke saath Abhimanyu ko chaaron taraf se gherne lage.

Lekin Abhimanyu bilkul nahi ghabraye.

Woh Shri Krishna aur Arjun ki tarah bahadur aur powerful yoddha the.

Itne saare yoddhaon se ghire hone ke baad bhi woh poori himmat se ladte rahe.
Arjun Apne Bete Ki Madad Ke Liye Aaye
Jab Arjun ne dekha ki Abhimanyu ko Kaurav sena ne chaaron taraf se gher liya hai, toh unhe bahut gussa aaya.

Unhone Shri Krishna se kaha ki woh turant Abhimanyu ki madad ke liye chalein.

Shri Krishna ne apna divya rath Kaurav sena ki taraf badha diya.

Lekin Arjun ko aage badhte dekh Bhishma Pitamah, Dronacharya aur kai Kaurav raja apni sena ke saath unhe rokne ke liye aa gaye.

Ab Arjun ke saamne bhi Kaurav sena ki ek bahut badi fauj khadi thi.
Arjun Ka Bhayankar Hamla
Arjun ne apna Gandiva dhanush uthaya aur Kaurav sena par arrows ki baarish shuru kar di.

Unke arrows itni tezi se chal rahe the ki aasman mein dhool aur arrows ke kaaran andhera chha gaya.

Haathi, ghode aur rathon ki ek badi sena Arjun ke saamne aage nahi badh paa rahi thi.

Arjun ke arrows se kai haathiyon ke upar lage flags gir gaye. Kai rath apne ghodon se alag ho gaye.

Kuch yoddha apne rath chhodkar bhaagne lage. Haathiyon aur ghodon par baithe sainik darr ke maare neeche utarkar idhar-udhar bhaagne lage.

Arjun apne arrows se dushmanon ke weapons aur shields ko todte ja rahe the.

Kisi ke haath se talwar gir rahi thi, toh kisi ka dhanush toot raha tha.

Kai yoddha apne rath aur ghode chhodkar jaan bachane ke liye bhaagne lage.

Kaurav sena mein koi bhi Arjun ka saamna karne ki himmat nahi kar paa raha tha.

Jo bhi unke saamne aata, Arjun ke arrows se ghaayal hokar yudh ke maidan mein gir jaata.
Arjun Aur Shri Krishna Ka Shankhnaad
Aakhirkar Kaurav sena ke yoddha darr ke maare peeche hatne lage.

Apni sena ko bhaagte dekh Arjun aur Shri Krishna ne apne divya shankh bajaye.

Unki awaaz poore Kurukshetra mein goonj uthi.
Bhishma Pitamah Ne Dronacharya Ko Kya Kaha?
Bhishma Pitamah ne apni sena ko bhaagte hue dekha.

Unhone Dronacharya se kaha:

"Hey Acharya! Dekhiye, Arjun aur Shri Krishna milkar hamari poori sena ko hara rahe hain.

Aaj Arjun ko yudh mein harana namumkin lag raha hai. Woh is samay aise lad rahe hain jaise duniya ke ant mein khud Mahakaal saamne aa gaye hon.

Hamari sena ab thak chuki hai aur yoddha darr ke maare bhaag rahe hain.

Suraj bhi ab dhalne wala hai. Isliye mujhe lagta hai ki ab yudh rok dena chahiye.

Aaj hamare yoddha bahut thak chuke hain. Ab unmein dobara ladne ki himmat nahi bachi hai."
Pehle Din Ka Yudh Samaapt
Bhishma Pitamah ne Dronacharya se baat karne ke baad Kaurav sena ko wapas lautne ka order diya.

Suraj dheere-dheere dhalne laga.

Dono taraf ke yoddha apne-apne camps ki taraf lautne lage.

Is tarah Kurukshetra ke yudh ka pehla din samaapt hua.

Arjun ne apne bete Abhimanyu ki raksha ki aur Kaurav sena ko peeche hatne par majboor kar diya.

Lekin yeh toh sirf shuruaat thi. Kurukshetra ka mahaan yudh abhi kai aur bhayankar dinon tak chalne wala tha! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.44
        with st.expander("Section 6.3.44  Section LVI"):
            text1 = """ Mahabharat – Section 56: Garuda Vyuha Aur Ardh-Chandra Vyuha
Yudh Ke Doosre Din Ki Shuruaat
Sanjaya ne Dhritarashtra se kaha:

"Hey Maharaj! Raat beet gayi aur subah ho gayi. Bhishma Pitamah ne Kaurav sena ko dobara yudh ke liye taiyaar hone ka order diya.

Is din Bhishma Pitamah ne apni sena ko ek khaas formation mein sajaya, jise Garuda Vyuha kaha jaata tha.

Garuda ek vishal pakshi hai. Is formation mein sena ko Garuda ke shape mein khada kiya gaya tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.44.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Kaurav Sena Ka Garuda Vyuha
Garuda Vyuha mein har yoddha ko ek khaas jagah di gayi thi.
- Chonch par: Khud Bhishma Pitamah khade the.
- Dono aankhon par: Dronacharya aur Kritavarma the.
- Sir ke paas: Ashwatthama aur Kripacharya apni sena ke saath khade the.
- Gardan par: Bhurishrava, Shalya, Bhagadatta, Jayadratha aur kai doosre raja the.
- Peeth par: Duryodhan apne saathiyon ke saath tha.
- Poonch par: Avanti ke raja Vinda aur Anuvinda, Kamboj, Shak aur Shurasen ke yoddha the.
- Daaye pankh par: Magadh, Kalinga aur Daseraka ke sainik the.
- Baaye pankh par: Karusha, Vikunja, Munda aur doosre yoddha khade the.
Is tarah Bhishma Pitamah ne Kaurav sena ko ek bade Garuda ke roop mein taiyaar kar diya.
Pandav Sena Ka Ardh-Chandra Vyuha
Arjun ne jab Kaurav sena ka Garuda Vyuha dekha, toh unhone Dhrishtadyumna ki madad se apni sena ko bhi ek powerful formation mein sajaya.

Pandav sena ne Ardh-Chandra Vyuha banaya.

Iska shape aadhe chaand jaisa tha.

Is formation mein bhi har bade yoddha ko ek khaas jagah di gayi thi.
- Daaye hisse par: Bhimsen kai deshon ke rajaon ke saath khade the.
- Bhim ke paas: Raja Virat aur Drupad the.
- Unke aage: Nila apne khaas hathiyaaron ke saath khade the.
- Nila ke paas: Dhrishtaketu Chedi, Kashi aur doosre yoddhaon ke saath the.
- Beech mein: Dhrishtadyumna, Shikhandi aur Panchal ke yoddha khade the.
- Madhya mein: Raja Yudhishthir apni haathi sena ke saath maujood the.
- Yudhishthir ke paas: Satyaki aur Draupadi ke paanch bete the.
- Unke aage: Iravan khade the.
- Iravan ke paas: Ghatotkach aur Kekaya ke bahadur yoddha the.
- Baaye hisse par: Arjun khade the, jinke saath khud Shri Krishna saarathi ke roop mein maujood the.
Is tarah Pandavon ne bhi apni sena ko yudh ke liye taiyaar kar diya.
Doosre Din Ka Bhayankar Yudh Shuru
Dono senaon ke formation taiyaar hote hi yudh shuru ho gaya.

Haathi aur rath ek-doosre ki taraf tezi se badhne lage.

Har taraf talwaron aur hathiyaaron ki awaazein goonjne lagi.

Rathon ke pahiyon ki awaaz, haathiyon ki garjana aur yoddhaon ke yudh ke naare aasman tak pahunch rahe the.

Dono taraf ke sainik ek-doosre par hamla kar rahe the.

Kurukshetra ka maidan ek baar phir bhayankar yudh ka gawah ban gaya.

Ab dono senaon ke beech doosre din ka sangharsh shuru ho chuka tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.45
        with st.expander("Section 6.3.45  Section LVII"):
            text1 = """ Mahabharat – Section 57: Arjun Ka Bhayankar Yudh
Arjun Ka Kaurav Sena Par Hamla
Sanjaya ne Dhritarashtra ko bataya:

"Hey Maharaj! Dono senaon ke apne-apne formations mein khade hone ke baad bhayankar yudh shuru ho gaya.

Mahaan dhanurdhar Arjun ne apne teeron se Kaurav sena ke kai bade yoddhaon aur rathiyon ko haraana shuru kar diya. Unke teeron se Kaurav sena mein afra-tafri mach gayi.

Kaurav yoddha bahut nuksaan uthane ke baad bhi haar maanne ko taiyaar nahi the. Woh poori himmat ke saath Pandav sena par hamla karte rahe.

Dono taraf ke yoddha jeetne ke liye lad rahe the. Koi bhi peeche hatne ko taiyaar nahi tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.45.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dhool Se Dhak Gaya Kurukshetra
Yudh itna bhayankar ho gaya ki dono senaon ke sainik apni jagah chhodkar idhar-udhar bhaagne lage.

Rathon aur ghodon ke tez daudne se zameen par bahut saari dhool udne lagi. Dhool itni zyada thi ki Suraj tak dikhna band ho gaya.

Kisi ko pata nahi chal raha tha ki woh kis direction mein hai ya saamne apni sena ka sainik hai ya dushman ka.

Yoddha apne saathiyon ko pehchanne ke liye unke jhande, kapde, naam aur awaazon ka sahara lene lage.

Lekin ek baat khaas thi.

Dronacharya ki protection mein Kaurav sena ka Garuda Vyuha abhi bhi majboot khada tha. Use todna aasaan nahi tha.

Dusri taraf Arjun aur Bhim ki protection mein Pandavon ka Ardh-Chandra Vyuha bhi majboot bana hua tha.
Har Taraf Bhayankar Ladai
Ab yudh mein har tarah ke sainik ek-doosre se lad rahe the.
- Ghudsawar apni talwaron aur bhaalon se doosre ghudsawaron par hamla kar rahe the.
- Rath par baithe yoddha apne teeron se doosre rathiyon ko nishana bana rahe the.
- Haathiyon par baithe mahavat aur yoddha ek-doosre ke haathiyon se takra rahe the.
- Paidal sainik apni talwaron, teeron aur kulhaadiyon se lad rahe the.
Kabhi rath par savaar yoddha haathi par baithe sainik ko hara deta, toh kabhi haathi par savaar yoddha rath ko gira deta.

Ghudsawar bhi rathiyon par hamla karte aur kabhi paidal sainik ghudsawaron ko rok dete.

Yudh ka haal itna ajeeb aur bhayankar tha ki koi bhi kisi ko aasani se hara nahi paa raha tha.

Dheere-dheere poora maidan toote hue rathon, jhandon, dhanushon aur hathiyaaron se bhar gaya.

Zameen par khoon aur dhool phail gayi thi. Har taraf yudh ki bhayankar tasveer dikhai de rahi thi.
Bhishma Aur Dronacharya Ka Hamla
Isi beech Kaurav sena ke bade-bade yoddha dobara Pandav sena par toot pade.

Bhishma Pitamah, Dronacharya, Jayadratha, Purumitra, Vikarna aur Shakuni ne milkar Pandav sena ke formation ko todna shuru kar diya.

Ye sabhi yoddha yudh mein bahut kushal aur shaktishaali the.

Lekin Pandav bhi peeche hatne wale nahi the.

Bhimsen, Ghatotkach, Satyaki, Chekitana aur Draupadi ke paanchon beton ne milkar Kaurav sena par zor-daar hamla kiya.

Unhone Kaurav sainikon ko peeche dhakelna shuru kar diya.

Dono taraf ke bade-bade yoddha khoon se lathpath hokar bhi poori himmat se lad rahe the.
Duryodhan Ka Yudh Mein Aana
Jab Duryodhan ne dekha ki Pandav sena Kaurav sena par bhaari pad rahi hai, toh woh khud yudh mein utar aaya.

Uske saath lagbhag 1,000 rath the.

Duryodhan apni sena ke saath Pandavon aur Ghatotkach par hamla karne laga.

Dusri taraf Pandavon ne bhi milkar Bhishma Pitamah aur Dronacharya ka saamna karne ke liye apni sena aage badha di.

Arjun bhi bahut gusse mein apna rath lekar bade-bade rajaon ki taraf badhe.

Wahin Arjun ke bete Abhimanyu aur Satyaki ne Shakuni ki sena par hamla kar diya.
Yudh Aur Bhi Bhayankar Ho Gaya
Ab Kurukshetra mein ek baar phir bhayankar yudh shuru ho gaya.

Ek taraf Bhishma aur Dronacharya jaise mahaan yoddha the, toh doosri taraf Arjun, Bhim, Abhimanyu, Ghatotkach aur Satyaki jaise veer lad rahe the.

Dono senaon ka ek hi lakshya tha — apne dushman ko haraana aur yudh jeetna.

Is tarah Kurukshetra ka yudh aur bhi bhayankar hota chala gaya. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.46
        with st.expander("Section 6.3.46  Section LVIII"):
            text1 = """ Mahabharat – Section 58: Bhim Ka Duryodhan Par Prahar
Arjun Ko Kaurav Sena Ne Gher Liya
Sanjaya ne Dhritarashtra se kaha:

"Hey Maharaj! Jab Arjun yudh mein bahaduri se lad rahe the, tab Kaurav sena ke kai rajaon ne milkar unhe chaaron taraf se gher liya.

Hazaaron rathiyon ne Arjun par teeron ki baarish shuru kar di. Unhone bhaley, gada, talwarein aur kai tarah ke hathiyaar bhi Arjun ke rath ki taraf phenke.

Lekin Arjun bilkul nahi ghabraye. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.46.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Unhone apne sunehre teeron se hawa mein hi dushmanon ke saare hathiyaaron ko rok diya. Arjun ke haath itni tezi se chal rahe the ki unhe dekhkar Devta, Gandharva, Danav aur doosre divya prani bhi hairaan reh gaye.

Sabne Arjun ki tareef karte hue kaha — 

'Bahut khoob! Bahut khoob!'
Abhimanyu Ne Satyaki Ki Madad Ki
Dusri taraf Shakuni apni sena ke saath Abhimanyu aur Satyaki ko gher chuka tha.

Kaurav yoddhaon ne milkar Satyaki ke rath ko tod diya.

Satyaki ke paas ab apna rath nahi bacha tha. Tab unhone bina der kiye Abhimanyu ke rath par chadhkar yudh jaari rakha.

Ab dono veer ek hi rath par khade hokar Shakuni ki sena par teeron ki baarish karne lage.

Dono ne milkar Shakuni ki sena ko bhaari nuksaan pahunchaya.
Yudhishthir Aur Nakul-Sahdev Ka Prakram
Udhar Bhishma Pitamah aur Dronacharya ne milkar Yudhishthir ki sena par hamla kar diya.

Lekin Yudhishthir bhi peeche hatne wale nahi the.

Unke saath Madri ke dono bete, Nakul aur Sahdev, bhi yudh mein utar aaye.

Teeno bhaiyon ne milkar Dronacharya ki sena ka saamna kiya aur use peeche dhakelna shuru kar diya.

Kurukshetra mein yudh aur bhi bhayankar hota ja raha tha.
Bhim Aur Ghatotkach Ka Shandaar Yudh
Is beech Bhimsen aur unke bete Ghatotkach ne apni bahaduri dikhayi.

Ghatotkach ne apni shakti se aisa yudh kiya ki log hairaan reh gaye. Uska parakram dekhkar lag raha tha ki woh apne pita Bhimsen se bhi aage nikal raha hai.

Tabhi Duryodhan un dono ka saamna karne aa gaya.

Bhimsen ko Duryodhan par bahut gussa tha. Unhone apna dhanush uthaya aur ek teer seedha Duryodhan ke seene par chala diya.

Teer lagte hi Duryodhan buri tarah ghayal ho gaya aur apne rath mein hi behosh hokar gir pada.

Uska saarathi turant use yudh ke maidan se door le gaya.
Kaurav Sena Mein Bhagdad
Duryodhan ko behosh dekhkar uski sena ghabra gayi.

Kaurav sainik apni jagah chhodkar bhaagne lage.

Bhimsen ne unka peecha kiya aur teeron se unhe rokne lage.

Dusri taraf Dhrishtadyumna aur Raja Yudhishthir ne bhi Kaurav sena par hamla jaari rakha.

Bhishma Pitamah aur Dronacharya ne apni sena ko rokne ki bahut koshish ki, lekin us samay Kaurav sainik itne ghabraye hue the ki unki baat bhi nahi maan rahe the.
Abhimanyu Aur Satyaki Ka Ek Saath Yudh
Jab Kaurav sena ke hazaaron rathi idhar-udhar bhaagne lage, tab Abhimanyu aur Satyaki ne ek hi rath par khade hokar Shakuni ki sena par hamla kar diya.

Dono ki jodi bahut shandaar lag rahi thi.

Unka tej dekhkar aisa lag raha tha jaise aasman mein ek saath Suraj aur Chandrama chamak rahe hon.

Udhar Arjun ne bhi Kaurav sena par teeron ki zabardast baarish shuru kar di.

Unke teer baarish ki boondon ki tarah lagataar gir rahe the.

Kaurav sena mein ek baar phir bhagdad mach gayi.
Duryodhan Ne Apni Sena Ko Roka
Bhishma Pitamah aur Dronacharya ne jab apni sena ko bhaagte dekha, toh unhone use rokne ki koshish ki.

Tabhi Duryodhan bhi yudh ke maidan mein wapas aa gaya.

Usne apne sainikon ko himmat di aur unhe dobara ladne ke liye kaha.

Duryodhan ko saamne dekhkar bade-bade Kaurav yoddha ruk gaye.

Unhe rukta dekhkar baaki sainikon ne bhi bhaagna band kar diya.

Dheere-dheere poori Kaurav sena dobara yudh ke liye taiyaar ho gayi.
Duryodhan Ne Bhishma Pitamah Par Lagaya Aarop
Apni sena ko dobara taiyaar dekhkar Duryodhan seedha Bhishma Pitamah ke paas gaya.

Woh bahut gusse mein tha.

Usne Bhishma Pitamah se kaha:

"Pitamah! Jab aap, Dronacharya, Ashwatthama aur Kripacharya jaise mahaan yoddha hamari sena mein hain, toh phir hamari sena yudh se bhaag kaise sakti hai?

Mujhe nahi lagta ki Pandav aap logon ke saamne tik sakte hain.

Mujhe lagta hai ki aap jaan-boojhkar Pandavon ke saath naram vyavhaar kar rahe hain. Aap unhe poori shakti se nahi hara rahe.

Agar aap pehle hi bata dete ki aap Pandavon ke khilaaf poori shakti se nahi ladenge, toh main Karna ke saath milkar koi doosra raasta soch leta.

Lekin agar aap sach mein hamari taraf se lad rahe hain, toh ab apni poori shakti laga dijiye!"
Bhishma Pitamah Ka Jawab
Duryodhan ki baatein sunkar Bhishma Pitamah ko gussa aa gaya.

Woh muskuraaye aur bole:

"Duryodhan! Maine tumhe kai baar samjhaya hai ki Pandavon se dushmani karna tumhare liye achha nahi hai.

Pandav itne shaktishaali hain ki Devta bhi, Indra ke saath milkar, unhe aasani se nahi hara sakte.

Phir bhi main apni poori shakti se tumhari taraf se yudh karunga.

Aaj tum apni aankhon se dekhna. Main khud Pandav sena ko rokne ki poori koshish karunga."

Bhishma Pitamah ki baat sunkar Duryodhan bahut khush hua.

Usne turant apni sena ko shankh bajane aur nagade peetne ka order diya.

Dusri taraf Pandavon ne bhi shankh bajakar jawab diya.

Dono taraf se shankhon aur nagadon ki awaaz poore Kurukshetra mein goonjne lagi.

Ab Bhishma Pitamah ne khud Pandav sena ko rokne ki kasam jaisi chunauti de di thi. Yudh ka agla pal aur bhi romanchak hone wala tha! """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.47
        with st.expander("Section 6.3.47  Section LIX"):
            text1 = """ Mahabharat – Section 59: Shri Krishna Ka Sudarshan Chakra Uthana
Dhritarashtra Ne Sanjaya Se Sawal Kiya
Dhritarashtra ne Sanjaya se poocha:

"Sanjaya! Jab Duryodhan ki baaton se gussa hokar Bhishma Pitamah ne Pandavon ko haraane ka vachan diya tha, toh uske baad kya hua? Bhishma Pitamah ne Pandav sena ke saath kya kiya? Aur Pandavon ne unka saamna kaise kiya? Mujhe poori baat batao."

Sanjaya ne jawab diya:

"Hey Maharaj! Dopahar beet chuki thi aur Suraj dheere-dheere pashchim ki taraf badh raha tha. Pandav sena pehle kuch jagahon par jeet haasil kar chuki thi.

Lekin Bhishma Pitamah ne apna vachan yaad kiya aur apne rath par savaar hokar Pandav sena ki taraf badhne lage. Unke saath Kaurav sena ke kai bade yoddha bhi the.

Ab Kurukshetra mein ek baar phir bhayankar yudh shuru ho gaya." """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.47.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhishma Pitamah Ka Bhayankar Hamla
Bhishma Pitamah ne apna dhanush uthaya aur Pandav sena par teeron ki baarish shuru kar di.

Dono taraf se teeron ki awaaz, rathon ke pahiyon ki garaj aur yoddhaon ke yudh ke naare sunai dene lage.

Har taraf ek hi awaaz goonj rahi thi:

"Ruko! Yahin saamna karo!"

"Main tumhara intezaar kar raha hoon!"

"Aage badho aur yudh karo!"

Yudh itna bhayankar tha ki maidan mein har taraf hathiyaar aur toote hue rath bikhre pade the.

Kai yoddha apne parivaar aur doston ko awaaz laga rahe the. Kuch ghayal sainik madad ke liye pukaar rahe the, toh kuch apne saathiyon ko himmat de rahe the.
Bhishma Pitamah Ka Aisa Parakram Jaise Hazaar Yoddha Lad Rahe Hon
Bhishma Pitamah ne apna dhanush lagataar kheenchkar teer chalaane shuru kar diye.

Unke teer itni tezi se nikal rahe the ki Pandav yoddha samajh hi nahi paa rahe the ki unka agla hamla kis taraf se aayega.

Kabhi Bhishma purab mein dikhte, toh agle hi pal pashchim mein nazar aate.

Kabhi uttar mein, toh kabhi dakshin mein.

Aisa lag raha tha jaise ek nahi, balki hazaar Bhishma Pitamah yudh kar rahe hon!

Unke saamne aane wale bade-bade Pandav yoddha bhi unke teeron ka saamna nahi kar paa rahe the.

Bhishma Pitamah ke lagbhag har teer ka nishana sahi lag raha tha.

Unhone haathiyon, ghodon aur rathon ko bhi apne teeron se rokna shuru kar diya.

Unka yudh dekhkar Pandav sena mein dar phail gaya.
Pandav Sena Mein Bhagdad
Bhishma Pitamah ke lagataar hamlon se Raja Yudhishthir ki sena tootne lagi.

Pandav sainik alag-alag dishaon mein bhaagne lage.

Koi apna dhanush chhod raha tha, toh koi apna kavach utaarkar jaan bachaane ki koshish kar raha tha.

Yahan tak ki kai bade rathiyon ke liye bhi Bhishma Pitamah ko rokna mushkil ho gaya.

Shri Krishna aur Arjun ke saamne bhi Pandav sena buri tarah bikhar rahi thi.

Tab Shri Krishna ne Arjun se kaha:

"Hey Parth! Ab samay aa gaya hai ki tum Bhishma Pitamah ka saamna karo.

Tumne sabhi rajaon ke saamne vachan diya tha ki tum Bhishma, Dronacharya aur Duryodhan ki taraf se ladne wale sabhi yoddhaon ko haraoge.

Ab apna vachan poora karo!

Dekho, tumhari sena bhaag rahi hai. Yudhishthir ke saathi Bhishma ke dar se maidan chhod rahe hain.

Agar tumne abhi Bhishma ko nahi roka, toh Pandav sena ko bachaana mushkil ho jayega."

Arjun ne Shri Krishna ki baat sunkar kaha:

"Madhav! Aap mera rath seedha Bhishma Pitamah ke paas le chaliye. Main unka saamna karunga aur apni poori shakti lagaunga."
Arjun Aur Bhishma Pitamah Ka Maha-Yudh
Shri Krishna ne apne safed ghodon ko tezi se daudaya aur Arjun ka rath Bhishma Pitamah ke saamne le aaye.

Bhishma Pitamah ne Arjun ko aate dekha aur zor se garajkar unke rath par teeron ki baarish kar di.

Kuch hi palon mein Arjun ka rath, uska jhanda aur Shri Krishna tak teeron se dhak gaye.

Lekin Shri Krishna ne himmat nahi haari. Woh ghayal ghodon ko sambhalte hue rath chalaate rahe.

Arjun ne apna divya dhanush Gandiva uthaya aur ek teer se Bhishma Pitamah ka dhanush kaat diya.

Bhishma ne turant doosra dhanush uthaya.

Lekin Arjun ne woh bhi apne teer se kaat diya.

Bhishma Pitamah Arjun ki tezi dekhkar bahut prasann hue. Unhone kaha:

"Bahut khoob, Parth! Tum sach mein ek mahaan dhanurdhar ho. Aisa parakram tumhare jaise veer ko hi shobha deta hai.

Main tumse prasann hoon. Ab poori shakti se yudh karo!"

Itna kehkar Bhishma Pitamah ne ek aur dhanush uthaya aur Arjun par teer chalaane lage.
Bhishma Ke Teeron Se Krishna Aur Arjun Ghayal
Bhishma Pitamah ne apne teeron se Arjun aur Shri Krishna dono ko nishana banaya.

Shri Krishna apne rath ko tezi se ghumakar kai teeron se bachate rahe.

Lekin Bhishma ke teer lagataar un dono tak pahunch rahe the.

Arjun bhi poori shakti se yudh kar rahe the, lekin Bhishma Pitamah ke prati unke mann mein bahut samman tha. Isi wajah se woh unke khilaaf apni poori shakti lagaane mein hichkichaa rahe the.

Shri Krishna ne dekha ki Bhishma Pitamah apne teeron se Pandav sena ko lagataar nuksaan pahunchaa rahe hain.

Unhe laga ki agar aisa hi chalta raha, toh Pandav sena ka bachna mushkil ho jayega.

Tab Shri Krishna ke mann mein ek faisla aaya.
Shri Krishna Ne Uthaya Sudarshan Chakra
Shri Krishna ne dekha ki Arjun abhi bhi Bhishma Pitamah ke khilaaf poori taakat se nahi lad rahe.

Woh apne bhakt Arjun aur Pandav sena ki haalat dekhkar bahut gusse mein aa gaye.

Unhone socha:

"Bhishma aaj akela hi poori Pandav sena ko hara sakte hain. Agar maine abhi kuch nahi kiya, toh bahut bada nuksaan ho jayega.

Arjun Bhishma Pitamah ke prati samman ke kaaran dheere lad rahe hain. Isliye ab mujhe khud yudh mein utarna hoga."

Itna sochkar Shri Krishna ne rath ki lagaam chhod di.

Woh apne rath se neeche utare aur apne haath mein Sudarshan Chakra utha liya.

Unka roop bahut divya aur tej se bhara hua tha. Unke peele vastra hawa mein lehra rahe the aur haath mein chamakta hua Sudarshan Chakra Suraj ki tarah dikh raha tha.

Shri Krishna gusse mein seedhe Bhishma Pitamah ki taraf daud pade.

Aisa lag raha tha jaise koi sher ek bade haathi par hamla karne ja raha ho.
Bhishma Pitamah Ne Krishna Ka Swagat Kiya
Shri Krishna ko Sudarshan Chakra lekar apni taraf aate dekhkar Bhishma Pitamah bilkul nahi dare.

Woh bahut prasann hue aur bole:

"Aaiye, aaiye Prabhu Krishna!

Aap poore sansaar ke rakshak hain. Agar aapke haathon meri mrityu hoti hai, toh mere liye isse bada saubhagya aur kya ho sakta hai?

Aapke haathon yudh mein maara jaana mere liye samman ki baat hogi.

Aaj poore sansaar ko pata chalega ki aapne apne bhakt ko kitna bada samman diya hai."

Bhishma Pitamah Shri Krishna ko apne saamne dekhkar khush the. Unhe Bhagwan ke haathon mrityu bhi sweekar thi.
Arjun Ne Krishna Ko Rok Liya
Shri Krishna bahut tezi se Bhishma Pitamah ki taraf badh rahe the.

Tabhi Arjun apne rath se neeche utare aur unke peeche daud pade.

Arjun ne Shri Krishna ko dono haathon se pakad liya aur rokne ki koshish karne lage.

Lekin Krishna itne gusse mein the ki Arjun unhe aasani se rok nahi paa rahe the.

Arjun ne unke pair pakadkar bahut mushkil se unhe roka.

Phir Arjun ne haath jodkar kaha:

"Madhav! Kripya apna gussa shaant kijiye.

Aap hi Pandavon ke sabse bade rakshak hain.

Main aapko vachan deta hoon ki main apni poori shakti se Kaurav sena ka saamna karunga.

Main apna vachan zaroor poora karunga. Aapko dobara yudh mein hathiyaar uthaane ki zaroorat nahi padegi."

Arjun ki kasam sunkar Shri Krishna ka gussa shaant ho gaya.

Unhone Sudarshan Chakra sambhala aur wapas apne rath par chadh gaye.

Phir unhone apna shankh Panchajanya bajaya.

Uski awaaz poore Kurukshetra mein goonj uthi.

Arjun ne bhi apna Gandiva uthaya aur yudh ke liye taiyaar ho gaye.
Arjun Ka Divya Astra Aur Kaurav Sena Par Hamla
Shri Krishna ko dobara rath chalaate dekhkar Arjun ne apna Gandiva zor se kheenchkar teer chalaane shuru kar diye.

Ab Arjun ne apni poori shakti laga di.

Duryodhan, Bhishma, Bhurishrava aur Shalya jaise bade yoddha Arjun par alag-alag hathiyaaron se hamla karne lage.

Bhurishrava ne Arjun par saat bhaley phenke.

Duryodhan ne ek tez bhaala chalaya.

Shalya ne gada phenki aur Bhishma Pitamah ne bhi ek divya astra se hamla kiya.

Lekin Arjun ne apne teeron se un sabhi hathiyaaron ko hawa mein hi kaat diya.

Iske baad Arjun ne apna divya Mahendra Astra chala diya.

Is astra se hazaaron teer nikalne lage. Aisa lag raha tha jaise aasman se aag ki baarish ho rahi ho.

Kaurav sena ke rath, jhande, dhanush aur hathiyaar tootne lage.

Haathi aur ghode bhi Arjun ke teeron se bach nahi paa rahe the.

Gandiva ki awaaz itni tez thi ki shankh aur nagadon ki awaaz bhi uske saamne dab gayi.
Kaurav Sena Mein Dar Phail Gaya
Arjun ke is divya astr ne Kaurav sena ko buri tarah hila diya.

Raja Virat, Raja Drupad aur Pandav sena ke doosre yoddha Gandiva ki awaaz sunkar Arjun ki madad ke liye aage badhe.

Dusri taraf Kaurav yoddha Arjun ke paas jaane se bhi darne lage.

Arjun ke teeron ne Kaurav sena ke kai bade yoddhaon ko hara diya.

Unki sena mein bhaari bhagdad mach gayi.

Pandav yoddhaon ne yeh sab dekha toh woh bahut khush hue aur zor-zor se vijay ke naare lagaane lage.

Shri Krishna aur Arjun ne bhi zor se garjana ki.
Yudh Ka Ant Aur Arjun Ki Jeet
Shaam hone lagi thi. Suraj dheere-dheere laal hone laga.

Bhishma Pitamah, Dronacharya, Duryodhan aur doosre Kaurav yoddha Arjun ke divya astr ke saamne bahut nuksaan utha chuke the.

Aakhirkaar Kaurav sena ko raat ke liye yudh rokna pada.

Arjun ne us din apne parakram se Kaurav sena ko bhaari nuksaan pahunchaya tha.

Sanjaya ne bataya ki us din Arjun ne lagbhag 10,000 rathiyon aur 700 haathiyon ko yudh mein hara diya tha. Kaurav sena ke kai bade yoddha bhi unke saamne tik nahi paaye.

Kaurav sainik apne tents mein lautkar Arjun ki bahaduri ki baatein karne lage.

Woh keh rahe the:

"Aaj Arjun ne jo parakram dikhaya hai, woh koi aam yoddha nahi kar sakta.

Unhone akele hi hamari sena ke bade-bade yoddhaon ko hara diya. Unke saamne tikna bahut mushkil hai."

Dusri taraf Arjun bhi apne bhaiyon ke saath Pandav camp mein laut aaye.

Is tarah yudh ke is din ka ant hua.

Is din Shri Krishna ne apne bhakt Arjun ke liye apna vachan todne tak ka faisla kar liya tha, lekin Arjun ne unhe rok kar apna vachan nibhane ka promise kiya. Aur phir Gandiva ke parakram se Kaurav sena ko peeche hatne par majboor kar diya. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.48
        with st.expander("Section 6.3.48  Section LX"):
            text1 = """ Mahabharat – Section 60: Bhishma Aur Arjuna Ka Bhayankar Yudh
Raat beet chuki thi aur subah hote hi Kurukshetra ke maidan mein yudh dobara shuru ho gaya.

Is baar Bhishma Pitamah bahut gusse mein the. Unhone Kaurava sena ko apne saath lekar Pandavon ki taraf aage badhna shuru kiya.

Unke saath Dronacharya, Duryodhana, Jayadratha, Kripacharya, Shalya aur kai bade-bade yoddha bhi the. Bhishma Pitamah ke aas-paas hazaaron rath, ghode aur haathi the. Unki sena aasman mein chhaye kaale baadalon jaisi lag rahi thi.

Dusri taraf Arjuna bhi apne rath par taiyaar the. Unke rath par Hanuman ji ka dhwaj lehra raha tha aur Bhagwan Krishna unka saarathi bane hue the.

Dono senaon ne shankh bajaye. Nagade aur dhol zor-zor se bajne lage. Poora Kurukshetra yudh ke shor se goonj utha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.48.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Yudh ka bhayankar roop
Dono taraf ke yoddha ek-doosre par toot pade.

Rathiyon ka rathiyon se, haathiyon ka haathiyon se aur ghudsawaron ka ghudsawaron se yudh hone laga. Talwaarein, teer aur bhalon ki awaaz har taraf sunai de rahi thi.

Kai rath toot gaye, ghode girne lage aur haathiyon ke beech bhayankar takkar hone lagi. Dhool itni zyada udne lagi ki aasman tak dhundhla dikhne laga.

Dono senaon ke yoddha apni poori taakat laga rahe the.
Bhishma Pitamah Aur Arjuna Aamne-Saamne
Thodi der baad Bhishma Pitamah ki nazar Arjuna par padi.

Woh apna rath lekar seedhe Arjuna ki taraf badhe. Unke saath Dronacharya, Kripacharya, Shalya aur Duryodhana jaise bade yoddha bhi the.

Tabhi Arjuna ke bete Abhimanyu ne bhi apna rath lekar Kaurava yoddhaon ko rokne ke liye aage badhna shuru kiya.

Abhimanyu ne apne shandaar yudh kaushal se kai yoddhaon ke hamlon ko rok diya. Woh ek jalti hui aag ki tarah dushmanon ke beech lad rahe the.

Lekin Bhishma Pitamah ne Abhimanyu ko chhodkar seedha Arjuna ko apna nishana banaya.

Ab Arjuna aur Bhishma Pitamah ke beech ek mahaan yudh shuru ho gaya.
Gandiva Aur Bhishma Ke Teeron Ki Takkar
Arjuna ne apna divya dhanush Gandiva uthaya. Unhone tezi se teeron ki baarish kar di.

Bhishma Pitamah ne bhi apne dhanush se hazaaron teer chhode. Dono taraf se teeron ki baarish hone lagi.

Arjuna ke teer Bhishma ke teeron ko hawa mein hi kaat rahe the. Bhishma bhi Arjuna ke har vaar ka zabardast jawab de rahe the.

Dono mahaan dhanurdhar ek-doosre ke saamne apni poori shakti dikha rahe the.

Kabhi Arjuna ke teer Bhishma ke teeron ko rok dete, toh kabhi Bhishma apne teeron se Arjuna ke hamlon ko nakaam kar dete.

Yeh yudh dekhkar Kaurava aur Pandava dono sena ke log hairaan reh gaye.
Abhimanyu Ka Shaurya
Arjuna aur Bhishma ke yudh ke beech Abhimanyu bhi Kaurava sena ke kai bade yoddhaon ka saamna kar rahe the.

Unhone apne teeron se dushmanon ke hamlon ko roka aur apni veerta ka pradarshan kiya.

Unki himmat dekhkar Pandava sena ke yoddhaon ka hausla badhne laga.
Yudh Ka Sabse Bada Muqabla
Bhishma Pitamah aur Arjuna ka yudh lagataar chalta raha.

Dono ke dhanushon ki awaaz bijli ki garaj jaisi thi. Unke teer itni tezi se chal rahe the ki dekhne wale samajh hi nahi paa rahe the ki kaun kis par vaar kar raha hai.

Bhishma Pitamah apne anubhav aur shakti se lad rahe the, jabki Arjuna apne divya astron aur dhanush chalane ki kala se unka saamna kar rahe the.

Dono senaon ke yoddha is mahaan yudh ko dekh rahe the.

Kurukshetra ka maidan ek baar phir bhayankar sangharsh ka gawah ban gaya.

Is tarah Section 60 mein Bhishma Pitamah aur Arjuna ke beech ek zabardast yudh shuru hua, jismein dono mahaan dhanurdharon ne apni-apni shakti aur yudh kala ka pradarshan kiya. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.49
        with st.expander("Section 6.3.49  Section LXI"):
            text1 = """ Section LXI – Abhimanyu Aur Dhrishtadyumna Ki Veerta
Kurukshetra mein battle bahut intense ho chuki thi. Ek taraf Arjuna Bhishma se lad raha tha, aur doosri taraf uska beta Abhimanyu apni bravery dikha raha tha.

Drona ka beta, Bhurisravas, Chitrasena aur kai powerful warriors ne milkar Abhimanyu ko gher liya. Lekin Abhimanyu bilkul nahi dara. Woh akela paanch bade warriors ka saamna kar raha tha, bilkul ek young lion ki tarah jo paanch elephants se lad raha ho.

Uski archery itni accurate thi ki koi bhi uske saamne tik nahi paa raha tha. Arjuna ne apne bete ki bravery dekhi toh khushi se zor se roar kiya.

Abhimanyu ne apne arrows se Drona ke bete aur Shalya ko injured kar diya. Usne Samyamani ke bete ka flag gira diya aur Somadatta ke bete ke powerful weapon ko hawa mein hi destroy kar diya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.49.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Shalya ne Abhimanyu par hundreds of arrows chalaye, lekin Abhimanyu ne un sabko dodge kar diya aur Shalya ke chaaron horses ko maar giraya. Abhimanyu ke saamne Bhurisravas, Shalya aur baaki warriors bhi tik nahi paaye.

Yeh dekhkar Duryodhana ne 25,000 powerful soldiers ko Arjuna aur Abhimanyu ko gherne ke liye bhej diya. Unmein Trigarta, Madra aur Kekaya ke warriors bhi shamil the.

Jab Panchala ke commander Dhrishtadyumna ne dekha ki Arjuna aur Abhimanyu ko enemies ne chaaron taraf se gher liya hai, toh woh apni huge army lekar unki help ke liye aage badha.

Dhrishtadyumna ne enemy warriors par powerful attack kiya. Usne kai soldiers ko defeat kiya aur Kritavarman ke rear guard ko bhi hara diya.

Phir Samyamani ke bete ne Dhrishtadyumna par arrows se attack kiya. Dhrishtadyumna ne bhi jawab diya aur apne sharp arrow se uska bow kaat diya. Uske baad usne 25 arrows se enemy ko badly injure kiya aur uske horses ko bhi maar giraya.

Ab Samyamani ka beta chariot se neeche aa gaya. Usne ek sharp sword aur shield uthayi aur paidal hi Dhrishtadyumna ki taraf badhne laga.

Woh sword ghumate hue ek dangerous warrior ki tarah aage aa raha tha. Lekin Dhrishtadyumna bhi peeche hatne wala nahi tha.

Jaise hi enemy uske chariot ke paas aaya, Dhrishtadyumna ne apni heavy mace uthayi aur uske head par zor se attack kiya.

Ek hi powerful blow mein Samyamani ka beta zameen par gir gaya aur uski death ho gayi.

Panchala ke prince Dhrishtadyumna ki bravery dekhkar Pandava army mein excitement phail gayi, jabki Kaurava army mein sadness aur fear chha gaya.

Apne bete ki death dekhkar Samyamani gusse se bhar gaya. Woh khud Dhrishtadyumna se fight karne ke liye aage aaya.

Dono armies ke warriors dekhne lage ki ab in do powerful warriors ke beech kya hoga.

Samyamani ne Dhrishtadyumna par teen arrows chalaye. Shalya ne bhi uske chest par attack kiya.

Aur is tarah battlefield mein ek aur fierce battle shuru ho gayi...

Section LXI yahin end hota hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.50
        with st.expander("Section 6.3.50  Section LXII"):
            text1 = """ Section LXII – Bhima Ka Elephant Army Par Bhayankar Attack
Dhritarashtra Sanjaya se bahut dukhi hokar kehte hain:

"Hey Sanjaya, mujhe lagta hai ki destiny, hard work se bhi zyada powerful hai. Meri army continuously Pandavas se haar rahi hai. Tum roz mujhe batate ho ki mere soldiers mar rahe hain aur Pandavas jeet rahe hain.

Mere bete Duryodhana ki wajah se mujhe itna dukh mil raha hai. Mujhe samajh nahi aa raha ki Pandavas ko kaise haraya jaaye aur mere bete victory kaise hasil karein."

Sanjaya ne jawab diya:

"Rajan, is bade disaster ki responsibility aapki aur aapke bete Duryodhana ki galat decisions ki wajah se hai. Ab main aapko battlefield ka haal batata hoon." """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.50.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dhrishtadyumna Aur Shalya Ka Yudh
Battlefield mein Dhrishtadyumna aur Shalya ke beech fierce fight chal rahi thi.

Shalya ne Dhrishtadyumna ke bow ko kaat diya aur us par arrows ki baarish kar di. Lekin Dhrishtadyumna ne bhi himmat nahi haari aur Shalya ko powerful arrows se jawab diya.

Jab Abhimanyu ne dekha ki Dhrishtadyumna danger mein hai, toh woh turant Shalya ke chariot ki taraf badha.

Abhimanyu ne Shalya par teen sharp arrows se attack kiya. Yeh dekhkar Kaurava army ke kai warriors Shalya ki protection ke liye aa gaye.

Duryodhana, Dushasana, Vikarna, Chitrasena aur uske kai brothers ne milkar Abhimanyu ko gher liya.
10 Pandavas Warriors vs 10 Kaurava Warriors
Ab Pandava side se Bhima, Dhrishtadyumna, Abhimanyu, Draupadi ke paanch bete aur Nakula-Sahadeva battlefield mein saamne aaye.

Ek taraf 10 Pandava warriors the, aur doosri taraf Duryodhana ke 10 warriors.

Dono taraf ke warriors ek doosre par arrows aur powerful weapons se attack karne lage.

Duryodhana ne Dhrishtadyumna par arrows chalaye. Dushasana, Durmarshana, Chitrasena aur baaki Kaurava warriors ne bhi us par attack kiya.

Lekin Dhrishtadyumna ne sabhi ko zabardast jawab diya. Usne har enemy warrior par 25 arrows chalaye.

Abhimanyu ne Satyavrata aur Purumitra ko bhi arrows se injured kar diya.

Nakula aur Sahadeva ne apne maternal uncle Shalya par attack kiya. Shalya ne bhi apne nephews ko arrows se rokne ki koshish ki, lekin dono bhai himmat se ladte rahe.
Bhima Ka Gussa Aur Duryodhana Ka Dar
Tabhi Bhima ki nazar Duryodhana par padi.

Bhima ne apni powerful mace uthayi aur Duryodhana ki taraf badha. Uska gussa dekhkar Kaurava warriors dar gaye aur peeche hatne lage.

Lekin Duryodhana ne haar nahi maani. Usne apni army ka ek special division bulaya, jisme 10,000 powerful elephants the.

Duryodhana khud Magadha ke king ke saath us elephant army ko lekar Bhima ki taraf badha.

Bhima ne itni badi elephant army ko apni taraf aate dekha toh woh apne chariot se jump karke neeche aa gaya.

Usne zor se lion ki tarah roar kiya aur apni heavy mace lekar elephants par attack kar diya.
Bhima Ne Akela 10,000 Elephants Ko Challenge Kiya
Bhima ek ke baad ek elephants par apni mace se attack karne laga. Uski strength itni powerful thi ki elephants uske saamne tik nahi paa rahe the.

Uski loud roar sunkar elephants bhi panic mein aa gaye.

Bhima ke peeche Abhimanyu, Draupadi ke paanch bete, Nakula, Sahadeva aur Dhrishtadyumna uski protection kar rahe the. Woh arrows se enemy elephant riders aur soldiers ko rok rahe the.

Phir Magadha ka king apne giant elephant par baithkar Abhimanyu ki taraf aaya. Uska elephant Airavata jaisa powerful tha.

Lekin Abhimanyu ne ek hi arrow se us giant elephant ko gira diya!

Uske baad Abhimanyu ne ek sharp arrow se Magadha ke king ka head bhi kaat diya.

Doosri taraf Bhima apni mace se elephants ko destroy karta ja raha tha. Ek-ek blow mein bade-bade elephants zameen par gir rahe the.
Kaurava Army Mein Macha Hahakaar
Bhima ka attack itna dangerous tha ki elephants dar kar idhar-udhar bhaagne lage. Bhaagte hue elephants apni hi Kaurava army ke chariots aur soldiers ko kuchalne lage.

Bhima battlefield mein apni mace lekar aage badhta raha. Uska roop dekhkar enemy soldiers aur elephants sabhi dar gaye.

Aakhirkaar Bhima ne elephant army ko battlefield se peeche hatne par majboor kar diya.

Sanjaya ne Dhritarashtra ko bataya ki us din Bhima battlefield mein destruction ke devta jaisa lag raha tha.

Is battle mein Abhimanyu ki archery aur Bhima ki incredible strength ne Pandava army ko ek badi victory dilayi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.51
        with st.expander("Section 6.3.51  Section LXIII"):
            text1 = """ Section LXIII – Bhima Ka Kaurava Army Par Mahavinashak Attack
Sanjaya ne Dhritarashtra ko battlefield ka haal batana continue kiya.
Duryodhana Ki Poori Army Bhima Par Toot Padi
Jab Bhima ne Magadha ki elephant army ko destroy kar diya, toh Duryodhana bahut gusse mein aa gaya.

Usne apni poori army ko order diya:

"Sabhi warriors ek saath Bhima par attack karo aur use maar girao!"

Duryodhana ka order milte hi Kaurava army ke hazaaron warriors Bhima ki taraf badhne lage. Unke paas chariots, elephants, horses aur countless soldiers the.

Unki army itni badi thi jaise samundar ki ek vishal lehar Bhima ki taraf aa rahi ho.

Lekin Bhima bilkul nahi dara. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.51.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Woh apni heavy iron mace lekar wahin khada raha aur enemy army ka saamna karne laga. Jaise ek mountain samundar ki powerful waves ko rok deta hai, waise hi Bhima ne Kaurava army ko rok diya.

Bhima ke saath uske bhai, Dhrishtadyumna, Abhimanyu, Draupadi ke paanch bete aur Shikhandi bhi lad rahe the. Kisi ne bhi Bhima ka saath nahi chhoda.
Bhima Ka Mace Attack
Bhima ne apni massive mace uthayi aur Kaurava warriors par toot pada.

Woh apni mace se enemy chariots, horses aur elephants ko destroy karne laga. Jo soldiers uske saamne aaye, unhe bhi usne apni incredible strength se defeat kar diya.

Kabhi woh chariot par baithe warriors ko neeche gira deta, toh kabhi ground par lad rahe soldiers ko apni mace se hara deta.

Uska attack itna powerful tha ki Kaurava army mein panic phail gaya.

Bhima battlefield mein aise move kar raha tha jaise duniya ke end par destruction karne wala koi powerful force aa gaya ho.

Jis direction mein Bhima apni mace lekar dekhta, us taraf ke warriors dar kar peeche hatne lagte.

Kaurava soldiers ko lagne laga ki Bhima ko rokna almost impossible hai.
Bhishma Aur Bhima Aamne-Saamne
Bhima ke attack se Kaurava army ki halat kharab ho rahi thi.

Tabhi Bhishma apne powerful chariot par battlefield mein aage badhe. Unka chariot bahut fast tha aur woh arrows ki baarish karte hue aa rahe the.

Bhima ne Bhishma ko apni taraf aate dekha aur gusse mein unki taraf badhne laga.

Battlefield mein ab Bhishma aur Bhima ke beech ek bade encounter ka moment aa gaya tha.
Satyaki Ka Bhishma Par Attack
Isi waqt Yadava warrior Satyaki bhi apne chariot par Bhishma ki taraf badha.

Uske horses silver colour ke the aur uski archery bahut accurate thi.

Satyaki raste mein aane wale Kaurava warriors ko arrows se defeat karta hua aage badh raha tha.

Rakshasa warrior Alamvusha ne us par 10 arrows chalaye. Satyaki ne jawab mein 4 arrows se us par attack kiya aur bina ruke aage badhta raha.

Kaurava warriors ne milkar Satyaki par arrows ki baarish kar di, lekin woh kisi se nahi dara.

Woh battlefield mein aise lad raha tha jaise bright afternoon sun ko koi clouds chhupa nahi sakte.

Koi bhi warrior uska raasta nahi rok paa raha tha.
Bhurisravas Ne Satyaki Ko Challenge Kiya
Satyaki ko apni army ke warriors ko defeat karte dekhkar Somadatta ka beta Bhurisravas gusse se bhar gaya.

Usne dekha ki Satyaki Kaurava army ko continuously push back kar raha hai.

Bhurisravas ne apna powerful bow uthaya aur Satyaki ki taraf badha.

Ab dono powerful warriors ke beech ek naya yudh shuru hone wala tha...

Section LXIII yahin end hota hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.52
        with st.expander("Section 6.3.52  Section LXIV"):
            text1 = """ Section LXIV – Bhima Ne Duryodhana Ke 14 Bhaiyon Ko Hara Diya, Ghatotkacha Ka Bhayankar Attack
Sanjaya ne Dhritarashtra ko bataya ki pichhle battle mein Bhima ne Kaurava army ko buri tarah hila diya tha. Ab Duryodhana aur uske warriors Bhima ko rokne ke liye ek baar phir aage aaye.
Bhurisravas Aur Satyaki Ka Yudh
Bhurisravas aur Satyaki ke beech fierce battle shuru ho gayi.

Bhurisravas ne Satyaki par 9 arrows chalaye. Satyaki ne bhi turant jawab dete hue us par 9 arrows chala diye.

Duryodhana apne brothers ke saath Bhurisravas ki help ke liye aa gaya. Wahin Pandavas bhi Satyaki ko support karne ke liye uske aas-paas khade ho gaye.

Doosri taraf Bhima apni mace lekar Duryodhana aur uske brothers ka saamna kar raha tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.52.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhima Aur Duryodhana Ka Face-Off
Duryodhana ke bhai Nandaka ne Bhima par sharp arrows se attack kiya. Duryodhana ne bhi Bhima ke chest par 9 arrows maare.

Bhima apne chariot par wapas chadha aur apne charioteer Vishoka se bola:

"Ye Dhritarashtra ke bete mujhe maarna chahte hain. Aaj main in sabko tumhare saamne defeat karunga. Bas mera chariot carefully chalana!"

Yeh kehkar Bhima ne Duryodhana aur Nandaka par arrows chalaye.

Duryodhana ne Bhima ke bow ko kaat diya. Bhima ne doosra bow uthaya aur ek powerful arrow se Duryodhana ka bow bhi destroy kar diya.

Duryodhana ne turant ek aur bow uthaya aur ek dangerous arrow se Bhima ke chest par attack kiya.

Arrow lagte hi Bhima ko bahut zor ka shock laga. Woh apne chariot mein behosh hokar gir gaya.

Abhimanyu aur doosre Pandava warriors yeh dekhkar gusse mein aa gaye. Unhone Duryodhana ki army par arrows ki heavy baarish kar di.

Kuch der baad Bhima ko hosh aa gaya. Hosh mein aate hi usne Duryodhana par dobara attack kiya aur Shalya ko bhi 25 arrows se injured kar diya. Shalya ko battlefield se bahar le jaana pada.
Bhima Ne Duryodhana Ke 14 Bhaiyon Ko Maar Giraya
Ab Duryodhana ke 14 bhai ek saath Bhima ko gherkar attack karne lage.

Un sabki aankhein gusse se laal thi. Unhone Bhima par countless arrows chalaye.

Lekin Bhima bilkul nahi dara.

Usne apni mace aur arrows se unka saamna kiya. Phir ek-ek karke Kaurava warriors ko defeat karna shuru kar diya.

Bhima ne Senapati, Jalasandha, Sushena, Ugra, Virabahu, Bhima, Bhimaratha aur Sulocana samet kai bhaiyon ko maar gira diya.

Yeh sab kuch Duryodhana ki army ke saamne hua.

Apne brothers ko girte dekhkar baaki Kaurava warriors dar gaye aur battlefield se bhaagne lage.

Duryodhana ke liye yeh bahut bada shock tha. Uske apne bhai uski aankhon ke saamne maare ja rahe the.
Bhishma Ka Order – Sab Milkar Bhima Ko Roko!
Bhishma ne dekha ki Bhima akela hi Duryodhana ke powerful warriors ko destroy kar raha hai.

Unhone apni army ke sabhi warriors se kaha:

"Bhima bahut dangerous ho chuka hai. Woh Dhritarashtra ke powerful sons ko ek-ek karke maar raha hai. Tum sab ek saath attack karo aur Pandu ke bete ko roko!"

Bhishma ka order milte hi Kaurava army dobara Bhima ki taraf badhi.

Isi waqt Bhagadatta, jo Pragjyotisha ka king tha, apne giant elephant par baithkar Bhima ke saamne aa gaya.

Usne Bhima par itne arrows chalaye ki Bhima unke beech chhup gaya. Pandava warriors ne Bhagadatta aur uske elephant par arrows ki baarish shuru kar di.

Elephant ka poora body arrows se injured ho gaya, lekin Bhagadatta use aur zyada speed se aage badhane laga.

Phir Bhagadatta ne ek powerful arrow se Bhima ke chest par attack kiya.

Bhima ko zor ka jhatka laga aur woh apne chariot par behosh hokar gir gaya.
Ghatotkacha Ki Entry – Ab Shuru Hua Maya Yudh!
Jab Bhima ko behosh dekha, toh uska beta Ghatotkacha bahut gusse mein aa gaya.

Ghatotkacha ek powerful Rakshasa warrior tha aur uske paas magical powers thi.

Usne achanak apne aap ko sabki nazron se gayab kar diya.

Kuch hi pal baad woh ek bhayankar roop mein wapas aaya. Apni Maya se usne ek giant Airavata jaisa elephant create kiya aur us par khud sawar ho gaya.

Uske saath teen aur giant magical elephants bhi aaye:
- Anjana
- Vamana
- Mahapadma
In elephants par bhi powerful Rakshasa warriors sawar the.

Ghatotkacha ne apne magical elephants ke saath Bhagadatta ke elephant par attack kar diya.

Chaaron taraf se elephants ne Bhagadatta ke elephant ko apne tusks se hit karna shuru kar diya.

Pehle se injured elephant ab pain se zor-zor se chillane laga.
Bhishma Ko Ghatotkacha Se Dar Laga
Bhagadatta aur Ghatotkacha ka yudh dekhkar Bhishma ko samajh aa gaya ki situation dangerous ho rahi hai.

Unhone Drona, Duryodhana aur doosre kings se kaha:

"Ghatotkacha bahut powerful hai. Bhagadatta ab serious danger mein hai. Agar humne uski help nahi ki, toh uski jaan ja sakti hai. Chalo, sab milkar use bachate hain!"

Bhishma ki baat sunkar Kaurava warriors Bhagadatta ki help ke liye aage badhe.

Yeh dekhkar Yudhishthira ke leadership mein Pandava warriors bhi unke peeche badhne lage.

Ghatotkacha ne enemy army ko apni taraf aate dekha aur ek terrifying roar kiya.

Bhishma ne Ghatotkacha ka roop aur uski power dekhi. Unhone Drona se kaha:

"Main aaj Ghatotkacha se fight nahi karna chahta. Woh abhi bahut powerful hai aur uske paas Pandavas ka support bhi hai. Hamare soldiers aur animals already thak chuke hain. Pandavas se fresh battle karna ab sahi nahi hoga."

Phir Bhishma ne order diya:

"Aaj ke liye battle stop kar do. Kal hum dobara fight karenge."
Battle Ka End – Pandavas Ki Victory
Bhishma ka order sunkar Kaurava army ne retreat karna shuru kar diya.

Raat bhi ho chuki thi, isliye dono armies apne-apne camps ki taraf laut gayi.

Pandavas ne victory ke celebration mein conch shells aur trumpets bajaye. Unke warriors zor-zor se victory cries kar rahe the.

Bhima aur Ghatotkacha sabse aage chal rahe the.

Pandava warriors ne apne brave heroes ka welcome kiya. Unke bodies par battle ke wounds the, lekin unke chehron par victory ki khushi thi.

Doosri taraf Duryodhana apne camp mein bahut dukhi tha. Usne apne 14 brothers ko kho diya tha.

Woh chup-chaap baithkar unke baare mein sochta raha. Uski aankhon mein aansu the aur dil mein bahut sadness thi.

Us raat Kaurava camp mein celebration nahi, sirf grief aur silence tha.

Section LXIV yahin end hota hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.53
        with st.expander("Section 6.3.53  Section LXV"):
            text1 = """ Section LXV – Pandavas Ki Victory Ka Asli Reason: Shri Krishna
Is section mein Dhritarashtra apne bete Duryodhana ki haar se bahut pareshan hai. Woh Sanjaya se poochta hai ki aakhir Pandavas itne powerful kaise hain aur Kaurava army baar-baar unse kyun haar rahi hai.
Dhritarashtra Ka Dar
Dhritarashtra Sanjaya se kehta hai:

"Hey Sanjaya, Pandavas ke warriors aise amazing feats kar rahe hain jo shayad Gods bhi nahi kar sakte. Mere bete baar-baar battlefield mein haar rahe hain.

Bhima mere bete ko ek-ek karke maar raha hai. Mujhe koi aisa warrior nazar nahi aata jo mere beton ko protect kar sake.

Pandavas ke paas aisi kaunsi power hai? Kya unhone koi special tapasya ki hai? Kya unhe kisi God ka blessing mila hai?

Mujhe batao ki unhe harana itna difficult kyun ho raha hai. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.53.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Aur jab meri army battlefield se retreat kar rahi thi, tab Duryodhana, Bhishma, Drona, Kripacharya aur baaki warriors ne kya kiya?"
Sanjaya Ne Bataya Victory Ka Asli Reason
Sanjaya ne jawab diya:

"Rajan, Pandavas ki victory kisi magic ya illusion ki wajah se nahi hai. Woh apni strength, bravery aur righteousness ke dum par lad rahe hain.

Pandavas hamesha Dharma ke raaste par chalne ki koshish karte hain. Woh difficult situations mein bhi apne principles nahi chhodte.

Victory hamesha Dharma ke saath hoti hai.

Aapke bete cruel aur dishonest decisions lete rahe hain. Unhone Pandavas ke saath baar-baar injustice kiya.

Vidura, Bhishma, Drona aur maine bhi aapko kai baar samjhaya tha ki Pandavas ke saath peace kar lo. Lekin aapne humari advice nahi maani.

Ab aapke bete apne galat karmon ka result face kar rahe hain."
Duryodhana Ne Bhishma Se Poocha – Pandavas Ko Kaun Protect Kar Raha Hai?
Sanjaya ne phir bataya ki battle ke baad Duryodhana bahut dukhi tha.

Uske kai powerful brothers maare ja chuke the. Raat ko woh Bhishma ke paas gaya aur unse poocha:

"Pitamah, hamari army mein aap, Dronacharya, Shalya, Kripacharya, Ashwatthama, Kritavarma, Bhagadatta aur kai powerful warriors hain.

Hum sab weapons aur warfare mein experts hain. Hamari combined strength itni hai ki hum teenon worlds ki army ka bhi saamna kar sakte hain.

Phir bhi Pandavas baar-baar humein kaise hara rahe hain?

Aakhir woh kiski protection mein hain? Unki victory ka asli reason kya hai?"
Bhishma Ka Jawab – Shri Krishna Pandavas Ke Saath Hain
Bhishma ne Duryodhana ko samjhaya:

"Beta, maine tumhe pehle bhi kai baar advice di thi ki Pandavas ke saath peace kar lo.

Tum apne brothers ke saath kingdom enjoy kar sakte the. Sab khushi se reh sakte the.

Lekin tumne meri baat nahi maani. Tumne Pandavas ke saath injustice kiya. Aaj tumhe usi ka result mil raha hai.

Ab meri baat dhyan se suno.

Pandavas ko khud Shri Krishna protect kar rahe hain.

Jis army ke saath Shri Krishna khade hon, use duniya ki koi bhi power defeat nahi kar sakti.

Na past mein koi unhe hara saka, na present mein koi hara sakta hai aur na future mein koi hara payega."
Bhishma Ne Sunayi Shri Vishnu Ki Ek Divya Kahani
Duryodhana ko samjhane ke liye Bhishma ne ek ancient story sunayi.

Bahut purane samay ki baat hai. Ek baar sabhi Devas aur Rishis Gandhamadana mountain par Brahma ji ke paas gaye the.

Wahan achanak unhone sky mein ek extraordinary divine chariot dekha. Woh chariot bahut bright light se shine kar raha tha.

Brahma ji ne meditation karke samajh liya ki yeh koi ordinary being nahi, balki Supreme Divine Being hain.

Brahma ji aur sabhi Devas ne respect ke saath apne hands join kiye aur us Divine Being ko pranam kiya.

Woh Divine Being the – Shri Narayana, Shri Vishnu, yaani Vasudeva.
Brahma Ji Ne Shri Narayana Ki Stuti Ki
Brahma ji ne Shri Narayana ki praise karte hue kaha:

"Hey Narayana! Aap hi poore Universe ke Supreme Lord hain.

Aap past, present aur future sab kuch jaante hain.

Aap hi creation ke source hain aur aap hi poore Universe ko protect karte hain.

Aapke bina kuch bhi possible nahi hai.

Aap hi Vishnu hain, Vasudeva hain aur sabhi living beings ke protector hain.

Aapke paas unlimited power hai. Aap hi sabko life, strength aur protection dete hain.

Hum aapki actual power aur greatness ko kabhi completely understand nahi kar sakte."
Poora Universe Shri Vishnu Ka Hi Roop Hai
Brahma ji ne phir ek beautiful description diya:
- Earth, Shri Narayana ke feet ko represent karti hai.
- Sky unka head hai.
- Sun aur Moon unki eyes hain.
- Different directions unke arms hain.
- Fire unki energy hai.
- Wind unki breath hai.
- Rivers aur water unke divine existence se connected hain.
- Vedas unke knowledge ko represent karte hain.
Brahma ji keh rahe the ki poora Universe Shri Narayana ke divine form ka hi ek part hai.

Unhone kaha:

"Hey Lord, hum sab aapki grace se hi exist karte hain. Aap hi sabke protector aur guide hain.

Aapki protection se Earth fear se free rehti hai aur Devas bhi khush rehte hain."
Shri Vishnu Ka Shri Krishna Ke Roop Mein Janm
Brahma ji ne Shri Narayana se request ki:

"Hey Lord, Earth par jab bhi Adharma badhta hai aur evil forces powerful ho jaati hain, tab righteousness ko protect karna zaroori hota hai.

Isliye aap Yadu dynasty mein janm lijiye.

Aap human form mein aakar evil forces ka destruction kijiye, Dharma ko establish kijiye aur poore Universe ki protection kijiye."

Brahma ji ne Shri Narayana ke divine expansions ka bhi zikr kiya:
- Sankarshana
- Pradyumna
- Aniruddha
Is divine sequence ke through Brahma ji ne bataya ki creation bhi Shri Narayana ki divine power se hi hoti hai.

Aur isi tarah Shri Narayana ne duniya mein Dharma establish karne ke liye human form mein janm lene ka divine purpose accept kiya.
Is Kahani Ka Pandavas Se Connection
Bhishma ne Duryodhana ko yeh ancient story isliye sunayi kyunki woh samjhana chahte the ki Pandavas ke saath khud Shri Krishna hain.

Shri Krishna sirf Arjuna ke charioteer nahi hain. Woh Supreme Divine Being, Shri Narayana hain.

Pandavas Dharma ke liye lad rahe hain aur unke saath Shri Krishna khade hain.

Isi wajah se unhe defeat karna almost impossible hai.

Section LXV ka main message:

Duryodhana ke paas powerful army, Bhishma, Drona aur countless warriors hain. Lekin Pandavas ke paas Shri Krishna ka support aur Dharma ka saath hai.

Bhishma Duryodhana ko indirectly samjha rahe hain ki uski haar ka reason Pandavas ki koi magic power nahi, balki uske khud ke galat decisions aur Adharma hain. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.54
        with st.expander("Section 6.3.54  Section LXVI"):
            text1 = """ Section LXVI – Shri Krishna Hi Narayana Hain
Pichhle section mein Bhishma ne Duryodhana ko bataya tha ki Pandavas ko khud Shri Krishna protect kar rahe hain. Ab woh apni baat ko aage badhate hain aur samjhate hain ki Shri Krishna koi ordinary human nahi, balki poore Universe ke Supreme Lord hain.
Shri Narayana Ka Brahma Ji Ko Jawab
Bhishma ne bataya:

Bahut purane samay mein jab Brahma ji ne Shri Narayana se request ki thi ki woh Earth par janm lekar Adharma ka destruction karein, tab Shri Narayana ne ek soft aur powerful voice mein jawab diya:

"Brahma ji, mujhe aapki wish aur aapka purpose pata hai. Jo aap chahte hain, wahi hoga."

Itna kehkar Shri Narayana wahan se disappear ho gaye.

Yeh dekhkar sabhi Devas, Rishis aur Gandharvas bahut surprised ho gaye. Unhone Brahma ji se poocha:

"Hey Brahma ji, aapne itne powerful Divine Being ki itni devotion ke saath worship kyun ki? Woh kaun the?" """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.54.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Brahma Ji Ne Bataya – Woh Supreme Narayana Hain
Brahma ji ne jawab diya:

"Woh Supreme Being hain. Unka koi end nahi hai. Woh past, present aur future mein hamesha exist karte hain.

Wahi sabhi living beings ki Soul hain. Wahi poore Universe ke Supreme Master hain.

Maine unse request ki thi ki woh Vasudeva ke family mein human form lekar janm lein, taaki Earth par evil forces ka destruction kar sakein."

Brahma ji ne aage bataya ki purane samay mein kai powerful Asuras, Daityas aur Rakshasas ko battle mein defeat kiya gaya tha. Unmein se kuch ab human form mein Earth par janm le chuke hain.

Unka destruction karne ke liye Shri Narayana human form mein janm lenge.
Nara Aur Narayana Ka Connection
Brahma ji ne ek important baat batayi:

Shri Narayana Earth par Nara ke saath rahenge.

Nara aur Narayana dono ancient divine Rishis hain. Unki power itni extraordinary hai ki sabhi Devas milkar bhi unhe battle mein defeat nahi kar sakte.

Brahma ji ke according, ye dono jab human form mein Earth par aayenge, toh ordinary log unki real identity samajh nahi paayenge.

Is kahani mein Nara aur Narayana ka connection Pandavas aur Shri Krishna se hai:
- Nara ka sambandh Arjuna se hai.
- Narayana ka sambandh Shri Krishna se hai.
Yaani Shri Krishna aur Arjuna ka saath sirf ek friendship nahi, balki ek ancient divine connection hai.
Shri Krishna Ko Ordinary Human Samajhne Ki Galti Mat Karna
Brahma ji ne Devas ko warning di:

"Shri Vasudeva ko kabhi ordinary human mat samajhna.

Unke haathon mein Shankha, Chakra aur Gada hoti hai. Woh Supreme God hain.

Woh Eternal hain, Unchanging hain aur poore Universe ke protector hain.

Unhe samajhna aur unki greatness ko pehchanna bahut zaroori hai."

Brahma ji ne kaha ki jo log Shri Krishna ko sirf ek human samajhkar unki disrespect karte hain, woh ignorance mein jeete hain.

Shri Krishna hi woh Divine Being hain jinke chest par auspicious mark hai, jo Kaustubha gem aur crown dharan karte hain aur apne devotees ke fears ko door karte hain.

Unhe respect aur devotion ke saath worship karna chahiye.
Bhishma Ne Duryodhana Ko Samjhaya
Apni ancient story complete karne ke baad Bhishma ne Duryodhana se kaha:

"Yeh knowledge mujhe great Rishis se mili hai. Maine ise Parashurama, Markandeya, Ved Vyasa aur Narada jaise great sages se bhi suna hai.

Ab tum khud socho, jab Shri Krishna itne Supreme Divine Being hain, toh unki worship aur respect kyun nahi honi chahiye?

Tumhe pehle bhi warn kiya gaya tha ki Shri Krishna aur Pandavas ke against war mat karo.

Lekin tumne kisi ki advice nahi maani."

Bhishma ne Duryodhana ko strongly samjhaya ki Govinda (Shri Krishna) aur Dhananjaya (Arjuna) se nafrat karna uski sabse badi galti hai.
Jahan Shri Krishna Hain, Wahan Dharma Hai
Bhishma ne kaha:

"Shri Krishna Eternal hain. Woh poore Universe mein present hain. Wahi creation karte hain, protection karte hain aur Universe ko maintain karte hain.

Wahi sabhi living beings ke Supreme Master hain.

Jahan Shri Krishna hain, wahan Dharma hai. Aur jahan Dharma hai, wahan Victory zaroor hoti hai.

Pandavas ko Shri Krishna se hi wisdom, righteousness aur battlefield mein strength milti hai.

Wahi unhe dangers se protect karte hain aur difficult situations mein sahi direction dete hain.

Isliye Pandavas ki victory almost certain hai."
Shri Krishna Hi Har Yuga Ke Creator Hain
Bhishma ne aage bataya ki Shri Vasudeva hi har Yuga mein Gods aur human beings ki duniya ko create karte hain.

Wahi cities, kingdoms aur poori human civilization ke creator hain.

Different communities ke log apne-apne duties follow karte hue unki worship karte hain.

Dvapara Yuga ke end aur Kali Yuga ki beginning ke samay bhi devotees Shri Krishna aur Sankarshana ki devotion aur prayers karte hain.

Shri Krishna har Yuga mein Universe ko create aur maintain karne wale Supreme Lord hain.

Section LXVI Ka Main Message
Is section mein Bhishma Duryodhana ko ek final spiritual truth samjhate hain:
- Shri Krishna sirf Arjuna ke friend ya charioteer nahi hain.
- Shri Krishna hi Supreme Narayana hain.
- Arjuna aur Krishna ka connection Nara-Narayana ke ancient divine relationship se juda hai.
- Pandavas ko Shri Krishna ki guidance, protection aur blessings mil rahi hain.
- Jahan Shri Krishna aur Dharma hain, wahan victory hai.
Duryodhana ke paas Bhishma, Drona aur countless powerful warriors hain, lekin woh ek baat samajhne ko ready nahi hai: Pandavas ke against war karke woh sirf ek army se nahi, balki Dharma aur Shri Krishna ki divine power ke against khada hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.55
        with st.expander("Section 6.3.55  Section LXVII"):
            text1 = """ Section LXVII – Shri Krishna Ki Divine Powers Aur Creation Ki Kahani
Pichhle section mein Bhishma ne Duryodhana ko samjhaya tha ki Shri Krishna hi Supreme Narayana hain. Ab Duryodhana unse Shri Krishna ke origin aur unki divine powers ke baare mein aur detail mein poochta hai.
Duryodhana Ka Sawal
Duryodhana ne Bhishma se kaha:

"Pitamah, poore Universe mein Shri Vasudeva ko Supreme Being kaha jaata hai. Main unki greatness ke baare mein aur jaanna chahta hoon.

Mujhe bataiye ki Shri Vasudeva ka origin kya hai aur unki actual powers kitni hain?" """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.55.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhishma Ne Bataya – Shri Vasudeva Hi Supreme God Hain
Bhishma ne jawab diya:

"Beta, Shri Vasudeva sabhi Gods ke bhi God hain. Unse superior koi nahi hai.

Maharishi Markandeya bhi Shri Govinda ko Supreme Soul, Supreme Being aur poore Universe ka source maante hain.

Wahi sab kuch hain aur sabhi living beings ke andar unki divine presence hai."
Shri Narayana Ne Kaise Create Kiya Universe?
Bhishma ne ek ancient creation story sunayi.

Bahut purane samay mein jab kuch bhi exist nahi karta tha, tab Shri Narayana hi Supreme Divine Being ke roop mein present the.

Unhone sabse pehle Water, Air aur Fire ko create kiya. Phir unhone Earth aur baaki creation ko existence diya.

Uske baad Shri Narayana cosmic waters par Yoga Nidra mein rest karne lage.

Unki divine power se creation ka process aage badha:
- Unke mouth se Fire aur divine Speech originate hui.
- Unki breath se Wind create hui.
- Unhi se Vedas aur divine knowledge ka origin hua.
- Unhone Gods, Rishis aur different worlds ko create kiya.
- Unhone living beings ke liye birth, growth, old age aur death ka cycle bhi establish kiya.
Yaani creation ho, life ho ya time ka flow — sab Shri Narayana ki divine power se hi hai.
Sankarshana Aur Ananta Shesha Ka Creation
Shri Narayana ne Sankarshana ko create kiya, jo divine creation ke important forms mein se ek hain.

Unhone Ananta Shesha ko bhi create kiya. Ananta Shesha ek divine serpent hain, jinhe apne infinite form mein poori Earth aur mountains ko support karne wala bataya gaya hai.

Isi wajah se unka naam Ananta hai, yaani jinka koi end nahi.
Madhu Asura Ka Vadh – Isliye Shri Krishna Ka Naam Madhusudana Pada
Bhishma ne ek powerful incident bhi sunaya.

Ek samay Shri Narayana ke ear secretions se Madhu naam ka ek powerful Asura paida hua.

Madhu bahut dangerous tha. Uska intention Brahma ji ko destroy karna tha.

Lekin Shri Narayana ne uska saamna kiya aur uska vadh kar diya. Madhu ka destruction karne ke baad Gods, Rishis aur humans ne Shri Narayana ko Madhusudana, yaani Madhu Asura ka destroyer, kehna shuru kar diya.

Bhishma ne bataya ki Shri Narayana ke kai divine forms aur names hain:
- Varaha: Great divine Boar.
- Narasimha: Half-man, half-lion divine form.
- Trivikrama: Vamana Avatar ka विशाल form, jisme Bhagwan ne apne three steps se Universe ko cover kiya.
Ye sab Shri Vishnu ki divine power aur different manifestations ko represent karte hain.
Shri Narayana Sabhi Living Beings Ke Father Aur Mother Hain
Bhishma ne kaha:

"Shri Narayana hi sabhi living beings ke Father aur Mother hain. Unse superior koi nahi hai.

Unhone Universe mein different responsibilities aur social groups ko bhi create kiya."

Is ancient description mein chaar Varna ka origin unke divine body parts se bataya gaya hai:
- Brahmanas – Mouth se.
- Kshatriyas – Arms se.
- Vaishyas – Thighs se.
- Shudras – Feet se.
Yeh passage us samay ki traditional Varna-based creation explanation ko describe karta hai.
Shri Krishna Ke Devotees Ko Kya Milta Hai?
Bhishma ne Duryodhana ko bataya ki jo log devotion aur discipline ke saath Shri Kesava ki worship karte hain, unhe divine blessings milti hain.

Shri Krishna ko Hrishikesa bhi kaha jaata hai, jiska meaning hai – sabhi senses ke Lord.

Wahi sabke Preceptor, Father aur Master hain.

Bhishma ke according:
- Jo Shri Krishna ko sincerely worship karta hai, use divine blessings milti hain.
- Jo danger mein Shri Kesava ki protection maangta hai, Bhagwan uski raksha karte hain.
- Jo unki greatness ko devotion ke saath yaad karta hai, uske life mein happiness aur prosperity aati hai.
- Jo Shri Krishna ka shelter leta hai, woh difficult situations mein bhi unki protection paata hai.
Yudhishthira Ne Shri Krishna Ka Shelter Kyun Liya?
Bhishma ne end mein Duryodhana ko ek important baat samjhayi:

"Yudhishthira ne Shri Kesava ki greatness ko samajh liya hai.

Isi wajah se usne apne poore heart aur soul se Shri Krishna ka shelter liya hai.

Woh jaanta hai ki Shri Krishna hi Supreme Lord hain aur wahi Pandavas ko guidance aur protection dete hain."

Section LXVII Ka Main Message
Is section mein Bhishma Shri Krishna ke divine origin, Universe ki creation aur unke different forms ke baare mein batate hain.
1. Shri Narayana hi Universe ke creator aur protector hain.
2. Madhu Asura ka vadh karne ke baad unhe Madhusudana kaha gaya.
3. Varaha, Narasimha aur Vamana jaise divine forms bhi Shri Vishnu se connected hain.
4. Shri Krishna sabhi living beings ke Supreme Father aur Mother hain.
5. Yudhishthira ne isi divine truth ko samajhkar Shri Krishna ka shelter liya hai.
Bhishma Duryodhana ko baar-baar ek hi baat samjha rahe hain: Pandavas ki sabse badi strength unki army nahi, balki unka Shri Krishna par trust aur unka Dharma ke saath khade rehna hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.56
        with st.expander("Section 6.3.56  Section LXVIII"):
            text1 = """ Section LXVIII – Bhishma Ki Aakhri Warning: Pandavas Se Sandhi Kar Lo
Pichhle sections mein Bhishma ne Duryodhana ko Shri Krishna ki divine powers aur unke Supreme Narayana hone ke baare mein bataya tha.

Ab is section mein Bhishma Shri Krishna ki ek sacred prayer sunate hain aur Duryodhana ko ek baar phir Pandavas ke saath peace karne ki advice dete hain.
Brahma Ji Ki Shri Krishna Ke Liye Sacred Prayer
Bhishma ne Duryodhana se kaha:

"Beta, ab main tumhe woh sacred prayer sunata hoon jo khud Brahma ji ne Shri Narayana ki praise mein kahi thi. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.56.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Purane samay mein great Rishis aur Devas ne bhi is prayer ko Earth par logon tak pahunchaya tha."

Is prayer mein alag-alag Maharishis Shri Krishna ki greatness describe karte hain.
- Narada Rishi: Shri Krishna sabhi Gods ke God aur poore Universe ke Supreme Master hain.
- Markandeya Rishi: Shri Krishna hi Past, Present aur Future hain. Woh sabhi Yagya aur Tapasya ka Supreme Source hain.
- Bhrigu Rishi: Shri Krishna hi ancient Vishnu hain, jo sabhi Gods se superior hain.
- Ved Vyasa: Shri Krishna hi Vasudeva hain aur sabhi living beings ke Supreme Lord hain.
- Daksha: Shri Krishna hi creation ke Father hain.
- Angiras: Shri Krishna hi sabhi living beings ke Creator hain.
- Devala: Poora Universe Shri Krishna ke divine form ka part hai. Unmanifest aur manifest, dono unhi se connected hain.
Shri Krishna Ke Divine Form Mein Poora Universe Hai
Prayer mein bataya gaya hai ki poora Universe Shri Krishna ke divine body mein samaaya hua hai.
- Heavens unke head mein hain.
- Earth unki arms se supported hai.
- Teenon worlds unke stomach mein hain.
Woh Eternal Being hain. Har jagah unki presence hai.

Great Rishis aur Yogis meditation ke through unki divine reality ko experience karte hain.

Bhishma batate hain ki jo kings Dharma follow karte hain, generosity dikhate hain aur battle se kabhi peeche nahi hatte, unke liye bhi Shri Krishna hi ultimate refuge hain.

Sanatkumara aur doosre great Yogis bhi Shri Hari ki worship karte hain.

Prayer ke end mein Bhishma Duryodhana se kehte hain:

"Ab tumne Shri Kesava ki greatness ke baare mein sab kuch sun liya hai. Apne heart mein unke liye devotion aur respect jagao."
Duryodhana Par Is Kahani Ka Asar
Sanjaya Dhritarashtra ko batate hain ki sacred story sunkar Duryodhana ke mind mein Shri Krishna ke liye respect badhne laga.

Usne Pandavas ke powerful warriors ko bhi pehle se zyada seriously lena shuru kar diya.

Lekin Bhishma abhi bhi use ek final advice dena chahte the.
Bhishma Ki Final Warning
Bhishma ne Duryodhana se kaha:

"Beta, ab tumne Shri Krishna ki greatness samajh li hai.

Tumne Nara aur Narayana ke divine connection ke baare mein bhi sun liya hai.

Tumhe yeh bhi pata chal gaya hai ki Pandavas ko battle mein defeat karna itna difficult kyun hai.

Shri Krishna Pandavas se bahut prem karte hain. Woh unhe protect karte hain aur unhe right direction dete hain.

Isliye meri advice hai:

Pandavas ke saath peace kar lo.

Apne anger aur ego ko control karo. Apne brothers ke saath kingdom enjoy karo. Tum sab khushi se reh sakte ho.

Lekin agar tum Nara aur Narayana, yaani Arjuna aur Shri Krishna ki divine power ko ignore karoge, toh tumhara destruction certain hai."
Raat Ka Ant
Apni baat complete karne ke baad Bhishma silent ho gaye.

Unhone Duryodhana ko jaane ki permission di aur khud apne tent mein chale gaye.

Duryodhana ne bhi Bhishma ko respect ke saath pranam kiya aur apne tent mein laut gaya.

Us raat woh apne white bed par aaram karne ke liye let gaya.

Section LXVIII Ka Main Message
Is section mein Bhishma Duryodhana ko Shri Krishna ki greatness samjhane ke baad final warning dete hain.
1. Shri Krishna hi Universe ke Creator, Protector aur Supreme Lord hain.
2. Great Rishis aur Yogis bhi unki worship karte hain.
3. Shri Krishna Pandavas se prem karte hain aur unki protection karte hain.
4. Bhishma Duryodhana ko baar-baar peace ka option de rahe hain.
5. Agar Duryodhana apna ego aur anger control nahi karega, toh uska destruction ho sakta hai.
Sabse important baat: Bhishma jaante hain ki war ka result kya ho sakta hai. Phir bhi woh Duryodhana ko last moment tak samjha rahe hain ki apni zid chhodo, Pandavas se sandhi kar lo aur apne kingdom ko barbaadi se bachao. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.57
        with st.expander("Section 6.3.57  Section LXIX"):
            text1 = """ Section LXIX – War Ka Naya Din: Bhishma Aur Arjuna Ka Bhayankar Yudh
Pichhle sections mein Bhishma ne Duryodhana ko baar-baar samjhaya tha ki Pandavas ke saath peace kar lo. Lekin Duryodhana ne war rokne ka decision nahi liya.

Ab raat beet chuki thi aur subah ho gayi thi. Dono armies ek baar phir Kurukshetra ke battlefield mein saamne aa gayi.
Dono Armies Ne Banayi Powerful Battle Formation
Suraj nikalte hi Pandavas aur Kauravas apni-apni armies ke saath battlefield mein aage badhe.

Dono taraf ke warriors weapons aur armour ke saath ready the. Har kisi ke mind mein ek hi goal tha – enemy army ko defeat karna.

Kaurava army ke commander Bhishma ne apni army ko Makara Vyuha mein arrange kiya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.57.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Makara ek mythical aquatic creature hota hai, jo crocodile jaisa dikhta hai.

Dusri taraf Pandavas ne apni army ko ek powerful formation mein arrange kiya, jise Syena Vyuha kaha gaya. Syena ka meaning hota hai Hawk ya Eagle. Pandavas Ki Syena Vyuha Mein Kaun Kahan Tha?
Pandavas ne apne most powerful warriors ko formation ke different parts mein position diya tha.
- Beak (Chonch): Bhimasena – apni tremendous strength ke saath.
- Eyes (Aankhein): Shikhandi aur Dhrishtadyumna.
- Head (Sir): Satyaki.
- Neck (Gardan): Arjuna, apne powerful Gandiva bow ke saath.
- Left Wing: King Drupada aur unki army.
- Right Wing: Kekaya kingdom ke warriors.
- Back: Draupadi ke five sons aur Subhadra ke son Abhimanyu.
- Tail (Poonch): King Yudhishthira, Nakula aur Sahadeva ke saath.
Is tarah Pandavas ne apne important warriors ko strategically place kiya.
Bhima Ne Bhishma Ki Army Par Attack Kiya
Battle shuru hote hi Bhima ne Kauravas ki Makara Vyuha formation ke mouth ki taraf se attack kiya.

Woh seedha Bhishma ke paas pahunch gaya aur un par arrows ki baarish kar di.

Bhishma bhi chup rehne wale nahi the. Unhone apne powerful weapons se Pandava army par attack kiya.

Unke attacks se Pandava warriors ki formation disturb hone lagi.
Arjuna Ne Bhishma Ko Rok Diya
Jab Arjuna ne dekha ki Bhishma ke attacks se Pandava army trouble mein aa rahi hai, toh woh turant battlefield ke front par pahunch gaya.

Arjuna ne Bhishma par lagbhag 1,000 arrows chala diye.

Bhishma ke weapons ko counter karte hue Arjuna ne unka saamna kiya.

Ab battlefield mein dono legendary warriors aamne-saamne the: Ek taraf Bhishma the, jo Kaurava army ke commander the. Dusri taraf Arjuna tha, jiske saath Shri Krishna charioteer ke roop mein the.
Duryodhana Ne Dronacharya Se Help Maangi
Apni army ko battlefield mein suffer karte dekhkar Duryodhana bahut angry ho gaya.

Use pichhle din apne brothers ki death bhi yaad aa rahi thi.

Woh turant Dronacharya ke paas gaya aur bola:

"Acharyaji, aap hamesha mere well-wisher rahe hain.

Mujhe aap par aur Pitamah Bhishma par poora bharosa hai. Aap dono ke hote hue hum Gods ko bhi battle mein defeat kar sakte hain.

Phir Pandavas toh hamare saamne kuch bhi nahi hain.

Please, aisa kuch kijiye ki Pandavas ko battle mein destroy kiya ja sake."
Dronacharya Ne Pandava Army Mein Entry Ki
Duryodhana ki baat sunkar Dronacharya ne Pandavas ki formation ke andar attack kar diya.

Satyaki ne Drona ko aage badhte dekha aur unka raasta rok diya.

Ab dono powerful warriors ke beech fierce battle shuru ho gaya.

Drona ne apne arrows se Satyaki ke shoulder ke paas attack kiya aur unhe 10 arrows se hit kar diya.

Satyaki bhi Drona ka saamna karte rahe.
Bhima Ne Satyaki Ko Bachaya
Jab Bhima ne dekha ki Dronacharya Satyaki par attack kar rahe hain, toh woh turant unki help ke liye pahunch gaya.

Bhima ne Drona par multiple arrows chala diye, taaki Satyaki ko protection mil sake.

Lekin tab Bhishma aur Shalya bhi Drona ki help ke liye aa gaye.

Ab Bhima ko Drona, Bhishma aur Shalya – teeno powerful warriors ne apne arrows se target karna shuru kar diya.
Abhimanyu Aur Draupadi Ke Bete Bhi Battle Mein Utare
Bhima ko surrounded dekhkar Abhimanyu aur Draupadi ke five sons bhi battlefield mein aage aaye.

Unhone apne sharp arrows se Bhishma, Drona aur Shalya par attack kiya.

Battle aur bhi intense ho gayi. Dono sides ke warriors ek doosre ko rokne mein lage hue the.
Shikhandi Ne Bhishma Aur Drona Ko Challenge Kiya
Ab Shikhandi bhi apna powerful bow lekar Bhishma aur Drona ki taraf badhe.

Unke arrows itni speed se nikal rahe the ki battlefield mein sunlight tak cover hoti hui lag rahi thi.

Lekin jaise hi Bhishma ne Shikhandi ko apne saamne dekha, unhone unse fight karne se avoid kiya.

Iska reason tha ki Bhishma Shikhandi ko unke past aur unki feminine identity ke kaaran woman maante the. Bhishma ne pehle hi decide kiya hua tha ki woh Shikhandi ke against weapons nahi uthayenge.
Drona Ne Shikhandi Ka Raasta Roka
Duryodhana ke kehne par Dronacharya Bhishma ki protection ke liye aage aaye.

Shikhandi ne Drona ko apni taraf aate dekha, lekin woh unke saamne fight karne ke bajaye unse door ho gaye.

Drona ek extremely powerful warrior the aur unke saamne fight karna bahut dangerous tha.
Dono Armies Ke Beech Maha-Yudh
Ab Duryodhana apni large army ke saath Bhishma ki protection ke liye aage badha.

Dusri taraf Pandavas bhi apne warriors ke saath Bhishma ko challenge karne pahunch gaye.

Dono armies ke beech ek enormous battle shuru ho gaya.

Har warrior victory aur glory ke liye fight kar raha tha.

Sanjaya ke according, yeh battle itni fierce thi ki purane samay mein Devas aur Danavas ke beech hui war ki yaad dila rahi thi.

Section LXIX Ka Main Message
Is section mein war ka ek naya din shuru hota hai:
1. Kauravas ne Bhishma ke leadership mein Makara Vyuha banaya.
2. Pandavas ne Syena Vyuha, yaani Eagle Formation banayi.
3. Bhima ne Bhishma ki army par attack kiya.
4. Arjuna ne Bhishma ko 1,000 arrows se challenge kiya.
5. Dronacharya aur Satyaki ke beech fierce fight hui.
6. Bhima, Abhimanyu aur Draupadi ke bete Satyaki ki help ke liye aaye.
7. Shikhandi ne Bhishma ko challenge kiya, lekin Bhishma ne unse fight karne se avoid kiya.
Battle ab aur dangerous hoti ja rahi hai. Bhishma, Drona, Arjuna, Bhima aur Satyaki jaise legendary warriors ek hi battlefield mein apni full strength ke saath lad rahe hain. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.58
        with st.expander("Section 6.3.58  Section LXX"):
            text1 = """ Section LXX – Kurukshetra Ka Bhayankar Yudh: Khoon Ki Nadi Aur Warriors Ka Sangharsh
Pichhle section mein humne dekha ki Bhima, Arjuna, Satyaki, Drona aur Bhishma ke beech fierce battle shuru ho chuki thi.

Ab is section mein Sanjaya Dhritarashtra ko batate hain ki battlefield par yudh kitna bhayanak ho gaya tha.
Bhishma Ne Bhima Ke Khilaaf Yudh Tez Kar Diya
Bhishma samajh rahe the ki Bhima Kaurava army ke liye bahut bada danger ban chuka hai.

Isliye unhone apni army aur apne putron ko Bhima ke attack se protect karne ke liye poori strength ke saath fight karna shuru kar diya.

Ab Kauravas aur Pandavas ke beech ek massive battle chhid gayi.

Dono armies ke powerful warriors ek doosre ko defeat karne ke liye apne saare weapons use kar rahe the.  """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.58.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Battlefield Ka Shor Aasmaan Tak Pahunch Gaya
Kurukshetra ka battlefield kisi bhayanak storm jaisa lag raha tha.
- Elephants zor-zor se chinghaad rahe the.
- Horses ki neighing se poora maidan goonj raha tha.
- Warriors ke conch shells baj rahe the.
- Drums ki awaaz har taraf sunayi de rahi thi.
- Bows ki strings aur weapons ki takkar se bahut loud noise ho raha tha.
Warriors ek doosre ko challenge karte hue bulls ki tarah garaj rahe the.

Itna shor tha ki kisi ki awaaz samajhna bhi mushkil ho raha tha.
Battlefield Khoon Se Bhar Gaya
Dono armies ke warriors ek doosre par arrows ki baarish kar rahe the.

Bahut saare warriors battlefield mein maare ja rahe the. Unke helmets, golden ornaments, earrings aur weapons zameen par bikhar gaye the.

Elephants, horses aur soldiers ke bodies poore battlefield mein pade hue the.

Aasmaan mein warriors ke weapons lightning ki tarah chamak rahe the aur unke takrane ki awaaz thunder jaisi lag rahi thi.

Battlefield ki dhool itni zyada uth rahi thi ki aas-paas dekhna bhi mushkil ho gaya.

Sanjaya is scene ko describe karte hue kehte hain ki battlefield ek khoon ki nadi jaisa dikhne laga tha.
Warriors Ne Har Tarah Se Fight Kiya
Yudh ab sirf arrows aur bows tak limited nahi raha tha.

Warriors different weapons se ek doosre par attack kar rahe the:
- Gada (mace)
- Talwar (sword)
- Spear aur lance
- Arrows aur darts
Kuch warriors ke paas weapons nahi bache toh woh apne haathon se hi fight karne lage.

Koi punches maar raha tha, koi knees aur slaps se attack kar raha tha.

Kuch warriors apne chariots se neeche gir gaye, lekin unhone haar nahi maani. Woh swords lekar paidal hi enemy par attack karne lage.
Haathi Aur Ghode Control Se Bahar Ho Gaye
Arrows se injured elephants apne mahouts ko kho baithe aur battlefield mein idhar-udhar bhaagne lage.

Horses bhi apne riders se alag hokar uncontrolled ho gaye.

Kahin warriors elephants par attack kar rahe the, toh kahin horses aur chariots ke beech fierce fighting chal rahi thi.

Har taraf confusion aur destruction tha.
Bhima Aur Bhishma Ke Beech Bhayankar Fight
Bhima aur Bhishma ke beech bhi intense battle chal rahi thi.

Un dono ke aas-paas zameen par broken bows, maces, swords, arrows, ornaments aur fallen warriors ke bodies pade hue the.

Dono apni poori strength ke saath fight kar rahe the.

Kisi bhi taraf ke warriors peeche hatne ko ready nahi the.
Duryodhana Kalinga Army Ke Saath Aage Badha
Ab Duryodhana ne ek large division of Kalinga warriors ko apne saath liya.

Bhishma ko apne aage rakhkar woh Pandava army ki taraf attack karne ke liye badha.

Dusri taraf Pandava warriors bhi Bhima ko support karne ke liye aage aaye.

Unke horses aur chariots bahut fast the aur sabhi warriors Bhishma ki taraf gusse mein badh rahe the.

Ab ek baar phir dono armies ke beech ek massive clash hone wala tha.

Section LXX Ka Main Message
Is section mein Kurukshetra war ki brutality aur destruction ko describe kiya gaya hai.
1. Bhishma ne Bhima ke attacks ko rokne ke liye fierce fighting ki.
2. Dono armies ke beech massive battle hui.
3. Battlefield warriors, elephants aur horses ke bodies se bhar gaya.
4. Warriors ne arrows, swords, maces aur spears ke saath fight ki.
5. Kuch warriors weapons khatam hone ke baad bare hands se ladne lage.
6. Duryodhana Kalinga warriors ke saath Bhishma ko support karne aaya.
7. Pandava army Bhima ko support karte hue Bhishma ki taraf badhi.
Is section ka ek important point: Kurukshetra ka yudh ab apne sabse destructive phase mein enter kar raha tha. Dono taraf ke warriors victory ke liye lad rahe the, lekin us victory ki keemat hazaaron soldiers aur warriors ki jaan ban rahi thi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.59
        with st.expander("Section 6.3.59  Section LXXI"):
            text1 = """ Section LXXI – Arjuna Ka Mahayudh: Gandiva Ki Garaj Se Kaurava Sena Mein Dar
Pichhle section mein humne dekha ki Duryodhana Kalinga warriors ke saath Bhishma ki help ke liye aage badha tha. Dusri taraf Pandavas bhi Bhima ko support karne ke liye battlefield mein pahunch rahe the.

Ab is section mein Arjuna apni poori power ke saath battlefield mein utarta hai.
Arjuna Ne Bhishma Ki Taraf Kiya Attack
Jab Arjuna ne dekha ki uske brothers aur doosre Pandava kings Bhishma ke saath fight kar rahe hain, toh woh bhi apne weapons lekar Bhishma ki taraf badha.

Us samay Shri Krishna Arjuna ke charioteer the.

Krishna ne apna divine conch Panchajanya bajaya aur Arjuna ne apna legendary bow Gandiva uthaya.

Gandiva ki awaaz aur Panchajanya ke blast ko sunkar Kaurava army ke warriors ke dil mein dar baith gaya.

Arjuna ke chariot par laga flag bhi bahut magnificent tha. Us par lion's tail ka symbol tha. Woh flag aasman mein ek jalte hue mountain ya bright comet ki tarah chamak raha tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.59.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Gandiva Ki Garaj Se Kaurava Sena Ka Haal Bura Ho Gaya
Arjuna ne apne Gandiva bow se itni speed se arrows chalaye ki battlefield ke har direction mein arrows hi arrows dikhne lage.

Uski battle cries Indra ke roar jaisi lag rahi thi.

Arjuna apne haathon se zor-zor se clap karke bhi enemy warriors ko challenge kar raha tha.

Uske arrows ne Kaurava army ko har taraf se cover kar diya. Dhool, arrows aur battlefield ke shor ke beech Kaurava warriors ko samajhna mushkil ho gaya ki East kis taraf hai aur West kis taraf.

Unke horses thak chuke the, kai horses maare ja chuke the aur soldiers ka confidence tootne laga tha.

Aakhirkaar, Kaurava warriors aur Duryodhana ke brothers protection ke liye Bhishma ke paas jaane lage.
Bhishma Ne Kaurava Army Ko Protection Di
Kaurava warriors ko itna frightened dekhkar Bhishma unke protector bankar saamne aaye.

Gandiva ki thunder jaisi awaaz sunkar kai warriors apne chariots se neeche girne lage.

Cavalry soldiers apne horses se utar gaye aur infantry ke soldiers bhi dar ke maare zameen par girne lage.

Arjuna ke attacks ne Kaurava army ko buri tarah disturb kar diya tha.
Duryodhana Ne Arjuna Ko Gherne Ke Liye Badi Army Bheji
Duryodhana ne Arjuna ko rokne ke liye kai kingdoms ke warriors ko ek saath bheja.

Inmein shamil the:
- Kamboja ke fast horses aur horsemen.
- Hazaaron Gopa warriors.
- Madra, Sauvira, Gandhara aur Trigarta ke soldiers.
- Kalinga kingdom ke important warriors.
- King Jayadratha aur doosre kings.
- Dushasana ke leadership mein warriors.
- 14,000 powerful horsemen.
In sabhi forces ne milkar Suvala ke bete Shakuni ko support karne ke liye ghera.

Dusri taraf Pandavas bhi united hokar apne chariots aur animals par sawar hue aur Kaurava army par attack karne lage.
Bhishma Aur Arjuna Aamne-Saamne
Ab Bhishma ne elephants, horses aur chariots ki ek badi army ke saath Arjuna ka saamna kiya.

Unke warriors ke paas spears, sharp darts aur powerful arrows the.

Dono taraf se arrows ki baarish hone lagi. Battlefield Mein Alag-Alag Warriors Ke Beech Yudh
Is samay dono armies ke kai important warriors apne opponents ke saath fight kar rahe the.
Warrior	Opponent
Bhishma	Arjuna
Avanti ke king	Kashi ke king
Sindhu ke king	Bhima
Yudhishthira aur unke sons	Shalya
Vikarna	Sahadeva
Chitrasena	Shikhandi
Matsya warriors	Duryodhana aur Shakuni
Drupada aur Chekitana	Apne opponents ke saath battle
Satyaki	Dronacharya aur unke bete Ashwatthama
Kripacharya aur Kritavarma	Dhrishtadyumna

Is tarah battlefield ke alag-alag parts mein ek saath kai fierce battles chal rahi thi.
Battlefield Par Prakriti Bhi Bhayanak Roop Dikhane Lagi
Yudh itna intense ho gaya tha ki aasman aur zameen dono ajeeb dikhne lage.
- Aasman mein clouds nahi the, phir bhi lightning chamak rahi thi.
- Charon taraf dhool hi dhool thi.
- Achanak meteors girne lage aur thunder jaisi awaaz aayi.
- Tez hawa chalne lagi.
- Dhool ke kaaran suraj bhi chhup gaya.
Warriors dhool se poori tarah cover ho gaye the. Unhe aas-paas dekhna mushkil ho raha tha.

Weapons ki takkar aur arrows ki awaaz se poora battlefield goonj raha tha.
Chariots, Elephants Aur Horses Ka Bhayanak Nuksaan
Battlefield mein kai bade chariots destroy ho gaye.

Kisi chariot ka wheel toot gaya, kisi ka axle aur kisi ka poora structure damage ho gaya.

Kai charioteers aur horses maare gaye, jiske baad chariots apne riders ke bina idhar-udhar ghisatne lage.

Kuch elephants itne powerful the ki apni trunks se chariots ko tod rahe the.

Kai elephants apne upar baithe warriors aur standards ke saath zameen par gir rahe the.

Kuch elephants doosre elephants se takrakar gir gaye aur kuch apne trunks se chariots ko pakadkar ghaseetne lage.

Horses bhi arrows se injured hokar apne chariots ko ghaseette hue bhaag rahe the.

Aakhir mein poora battlefield fallen soldiers, elephants, horses, chariots aur broken flags se bhar gaya.

Section LXXI Ka Main Message
Is section mein Arjuna ki extraordinary fighting ability aur Kurukshetra war ke destruction ko dikhaya gaya hai.
1. Arjuna ne Panchajanya aur Gandiva ki awaaz ke saath Bhishma ki taraf attack kiya.
2. Uske arrows se Kaurava army mein panic phail gaya.
3. Bhishma ne frightened Kaurava warriors ko protection di.
4. Duryodhana ne kai kingdoms ki combined forces Arjuna ke khilaaf bheji.
5. Bhishma aur Arjuna ke beech direct battle hui.
6. Dono armies ke important warriors alag-alag battles mein engage ho gaye.
7. Battlefield mein elephants, horses aur chariots ka massive destruction hua.
Is section ka sabse powerful moment: Jab Arjuna ne Gandiva uthaya aur uski awaaz poore battlefield mein goonji, toh Kaurava army ke warriors tak dar gaye. Arjuna ko rokne ke liye Duryodhana ko kai kingdoms ki combined forces lagani padi.    """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.60
        with st.expander("Section 6.3.60  Section LXXII"):
            text1 = """ Section LXXII – Bhishma Ka Bhayankar Attack Aur Satyaki Ke Rath Ka Vinash
Pichhle section mein Arjuna ne Gandiva se Kaurava army mein dar paida kar diya tha. Duryodhana ne kai kingdoms ki armies ko Pandavas ke khilaaf bheja tha.

Ab battlefield mein har taraf alag-alag warriors ke beech fierce battles chal rahi thi. Is section mein Bhima, Bhishma aur Satyaki ke beech ka zabardast sangharsh dekhne ko milta hai.
Dono Armies Ke Warriors Ne Apne Opponents Chun Liye
Pandavas aur Kauravas ke warriors battlefield mein alag-alag directions mein aage badhe.

Pandava side ke important warriors ne apne opponents ke khilaaf battle shuru ki:
- Shikhandi aur King Virata: Bhishma ki taraf badhe.
- Arjuna: Dronacharya, Kripacharya, Vikarna aur Sindhu ke king ke saath kai powerful warriors se bhida.
- Bhima: Duryodhana aur Dussaha ke khilaaf aage badha.
- Sahadeva: Shakuni aur uske bete Uluka ke saamne gaya.
- Yudhishthira: Kaurava army ke elephant division par attack karne nikla.
- Nakula: Trigarta warriors ke saath fight karne laga.
- Satyaki, Chekitana aur Abhimanyu: Shalya aur Kaikeya warriors ki taraf badhe.
- Dhrishtaketu aur Ghatotkacha: Kaurava princes ki chariot army par attack karne gaye.
- Dhrishtadyumna: Dronacharya ke saamne aa gaya.
Ab battlefield ke har corner mein ek naya yudh shuru ho chuka tha. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.60.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dopahar Tak Battle Aur Bhi Dangerous Ho Gayi
Dheere-dheere suraj aasman ke beech pahunch gaya. Dopahar ka samay ho chuka tha.

Lekin battlefield mein fighting rukne ka naam nahi le rahi thi.

Dono armies ke decorated chariots, golden flags aur tiger-skin covers se saje hue rath battlefield mein tezi se move kar rahe the.

Warriors ki battle cries sher ki garaj jaisi sunayi de rahi thi.

Itne saare arrows ek saath chal rahe the ki aasman, suraj aur directions tak dikhna mushkil ho gaya.

Spears, swords, shields aur warriors ke golden ornaments suraj ki roshni mein chamak rahe the.

Poora battlefield ek ajeeb aur bhayanak scene ban gaya tha.
Bhishma Ne Bhima Par Powerful Attack Kiya
Battle ke beech Bhishma ne Bhima ko apne saamne dekha.

Bhishma gusse mein the aur unhone Bhima par golden wings wale, bahut sharp arrows ki baarish kar di.

Unke arrows Bhima ke body mein lagne lage.

Lekin Bhima bhi peeche hatne wala nahi tha.

Usne ek powerful dart (spear jaisa weapon) uthaya, jo ek gusse mein bhare saanp ki tarah Bhishma ki taraf gaya.

Bhishma ne apne sharp arrows se us dart ko hawa mein hi kaat diya.

Phir unhone ek aur sharp arrow chalaya aur Bhima ke bow ko do tukdon mein tod diya! Bhima ka bow toot chuka tha, lekin yudh abhi khatam nahi hua tha.
Satyaki Ne Bhishma Par Attack Kiya
Bhima aur Bhishma ke beech battle chal hi rahi thi ki Satyaki tezi se Bhishma ki taraf badha.

Satyaki ne apne bow ko kaan tak kheenchkar Bhishma par countless sharp arrows chala diye.

Bhishma ne bhi turant jawab diya.

Unhone ek extremely powerful arrow chalaya, jo seedha Satyaki ke charioteer ko laga.

Satyaki ka charioteer rath mein hi gir gaya aur uski death ho gayi.
Satyaki Ka Rath Control Se Bahar Ho Gaya
Charioteer ke maare jaane ke baad Satyaki ke horses control se bahar ho gaye.

Woh itni speed se bhaagne lage jaise unhe toofan ya hawa dhakka de rahi ho.

Satyaki ka rath battlefield mein idhar-udhar daudne laga.

Pandava army mein panic phail gaya.

Warriors zor-zor se chillane lage:
- "Jaldi jao!"
- "Horses ko pakdo!"
- "Unhe roko!"
- "Satyaki ki help karo!"
Poore battlefield mein Satyaki ke runaway chariot ko lekar afra-tafri mach gayi.
Bhishma Ne Pandava Army Par Qahar Barpa Diya
Is beech Bhishma ne Pandava army par apne attacks aur tez kar diye.

Sanjaya kehte hain ki Bhishma Pandava warriors ko is tarah maar rahe the jaise Indra Danavas ko destroy karte hain.

Bahut saare Panchala aur Somaka warriors Bhishma ke attacks mein maare gaye.

Lekin unhone himmat nahi haari.

Apni jaan ki parwah kiye bina woh dobara Bhishma ki taraf attack karne lage.

Dhrishtadyumna ke leadership mein Pandava warriors bhi Bhishma ko rokne ke liye aage badhe.

Dusri taraf Kaurava army ke warriors bhi Bhishma aur Drona ke saath milkar Pandavas par toot pade.

Aur is tarah battlefield mein ek aur massive battle shuru ho gayi.

Section LXXII Ka Main Message
1. Pandava warriors ne battlefield mein apne-apne opponents ke khilaaf attack kiya.
2. Bhishma ne Bhima par powerful arrows chalakar uska bow tod diya.
3. Bhima ka dart Bhishma ne hawa mein hi kaat diya.
4. Satyaki ne Bhishma par arrows ki baarish ki, lekin Bhishma ne uske charioteer ko maar diya.
5. Charioteer ke bina Satyaki ke horses control se bahar bhaag gaye.
6. Bhishma ne Panchala aur Somaka warriors par devastating attack kiya.
7. Dhrishtadyumna ke leadership mein Pandavas ne phir se Bhishma ko challenge kiya.
Is section ka sabse important moment: Bhishma ne ek hi battle mein Bhima ka bow tod diya aur Satyaki ke charioteer ko maar diya. Isse pata chalta hai ki Bhishma battlefield mein kitne powerful aur dangerous warrior the. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.61
        with st.expander("Section 6.3.61  Section LXXIII"):
            text1 = """ Section LXXIII – Arjuna vs Ashwatthama, Bhima vs Duryodhana Aur Abhimanyu Ki Veerta
Pichhle section mein Bhishma ne Pandava army par devastating attacks kiye the. Ab battlefield mein Arjuna, Ashwatthama, Bhima, Duryodhana aur Abhimanyu jaise powerful warriors ke beech zabardast yudh hone wala tha.

Sanjaya Dhritarashtra ko batate hain ki is din dono armies ke warriors ne apni poori strength laga di.
Arjuna Aur Ashwatthama Ke Beech Bhayankar Yudh
Sabse pehle King Virata ne Bhishma par teen arrows chalaye. Bhishma ne bhi jawab mein Virata ke horses ko teen arrows se hit kar diya.

Dusri taraf Dronacharya ke bete Ashwatthama ne Arjuna ko apne arrows se target kiya.

Ashwatthama ne Arjuna ke chest par chhe arrows maare.

Arjuna ko gussa aa gaya. Usne turant Ashwatthama ka bow tod diya aur uske body par paanch sharp arrows chala diye.

Lekin Ashwatthama bhi ek ordinary warrior nahi tha.

Usne turant doosra, aur bhi powerful bow uthaya aur Arjuna par 90 arrows chala diye. Usne Shri Krishna ko bhi 70 arrows se hit kiya! """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.61.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Ab Arjuna bahut angry ho gaya.

Usne apna Gandiva bow firmly pakda aur us par deadly arrows chadha diye. Arjuna ke arrows Ashwatthama ke armour ko penetrate karte hue uske body mein lage.

Lekin itne powerful attack ke baad bhi Ashwatthama peeche nahi hata.

Usne bhi Arjuna par powerful arrows se counterattack kiya.

Kaurava army ke warriors Ashwatthama ki bravery dekhkar impressed ho gaye. Unke liye yeh bahut badi baat thi ki Ashwatthama ek saath Arjuna aur Krishna dono ka saamna kar raha tha.
Arjuna Ne Ashwatthama Ko Zinda Chhod Diya
Arjuna Ashwatthama ko defeat kar sakta tha, lekin usne ek baat yaad rakhi.

Ashwatthama uske guru Dronacharya ka beta tha. Woh ek Brahmana bhi tha aur Arjuna uska respect karta tha.

Isliye Arjuna ne us par aur zyada deadly attack karne ke bajaye usse avoid kar diya.

Uske baad Arjuna ne apna dhyaan battlefield ke doosre Kaurava warriors par laga diya aur unki army ko destroy karne laga.
Bhima Aur Duryodhana Ke Beech Fight
Ab Duryodhana ne Bhima ko apne arrows se target kiya.

Usne Bhima par 10 golden arrows chalaye, jinke tips bahut sharp the.

Bhima ko gussa aa gaya.

Usne apna powerful bow uthaya aur 10 sharp arrows Duryodhana ki taraf chala diye.

Bhima ke arrows seedhe Duryodhana ke chest mein lage.

Duryodhana ke chest par ek beautiful jewel latak raha tha, jo golden threads se bandha hua tha. Bhima ke arrows uske aas-paas lage, toh woh jewel aisa chamakne laga jaise aasman mein suraj ke aas-paas planets chamakte hain.

Duryodhana ko yeh attack bilkul bardasht nahi hua.

Usne bhi Bhima par bahut saare sharp arrows chala diye.

Ab dono bhai ek doosre par continuously attacks kar rahe the.

Sanjaya ke according, dono warriors ki fight dekhkar aisa lag raha tha jaise do powerful celestial beings ek doosre se lad rahe hon. Abhimanyu Ne Kaurava Warriors Ko Challenge Kiya
Ab Subhadra ke bete Abhimanyu ne battlefield mein apni extraordinary bravery dikhani shuru ki.

Usne sabse pehle:
- Chitrasena par multiple sharp arrows chalaye.
- Purumitra par 7 arrows maare.
- Satyavrata par 70 arrows chalaye.
Abhimanyu itni speed se fight kar raha tha ki battlefield mein aisa lag raha tha jaise woh dance kar raha ho.

Lekin Kaurava warriors ne bhi jawab diya.

Chitrasena ne Abhimanyu par 10 arrows chalaye, Satyavrata ne 9 aur Purumitra ne 7 arrows se attack kiya.

Abhimanyu khud bhi injured ho gaya aur uske body par blood dikhne laga.

Lekin usne haar nahi maani.

Usne Chitrasena ka powerful bow tod diya aur uske armour ko penetrate karte hue uske chest mein arrow maar diya.
Kaurava Warriors Ne Abhimanyu Ko Gher Liya
Abhimanyu ki bravery aur fighting speed dekhkar Kaurava army ke kai princes gusse mein aa gaye.

Unhone milkar Abhimanyu ko surround kar liya aur us par sharp arrows ki baarish kar di.

Lekin Abhimanyu ne bhi un sabhi warriors ko apne arrows se counterattack kiya.

Sanjaya kehte hain ki Abhimanyu Kaurava army ke beech aise fight kar raha tha jaise garmi ke mausam mein jungle ki sookhi ghaas ko aag jala deti hai.

Woh jahan se guzarta, wahan Kaurava soldiers ko heavy losses hote.
Abhimanyu Aur Lakshmana Ka Yudh
Abhimanyu ki bravery dekhkar Duryodhana ka beta Lakshmana bhi usse fight karne ke liye aage aaya.

Dono young warriors ke beech direct battle shuru ho gayi.

Abhimanyu ne Lakshmana aur uske charioteer par chhe sharp arrows chalaye.

Lakshmana ne bhi Abhimanyu par multiple arrows se attack kiya.

Lekin Abhimanyu ne apni speed aur skill se Lakshmana ke chaaron horses ko maar diya. Usne Lakshmana ke charioteer ko bhi maar giraya.

Ab Lakshmana ka rath horses aur charioteer ke bina ruk gaya.

Gusse mein Lakshmana ne Abhimanyu ki taraf ek powerful dart pheka.

Lekin Abhimanyu ne apne sharp arrows se us dart ko hawa mein hi kaat diya! Kripacharya Ne Lakshmana Ki Jaan Bachayi
Lakshmana ab apne destroyed chariot par akela reh gaya tha.

Tab Kripacharya turant apne rath ke saath aaye.

Unhone Lakshmana ko apne chariot mein bithaya aur use battlefield se door le gaye.

Is tarah Lakshmana ki jaan bach gayi.
Battle Aur Bhi Zyada Destructive Ho Gayi
Ab dono armies ke warriors ek doosre par toot pade.

Kayi warriors ke bows toot chuke the, armour nikal chuka tha aur unke chariots destroy ho chuke the.

Lekin unhone fight karna nahi chhoda.

Kuch Srinjaya warriors apne weapons aur chariots kho dene ke baad bhi Kurus se apne haathon se fight karne lage.

Isi beech Bhishma ne apne celestial weapons ka use karke Pandava army par ek aur powerful attack kiya.

Unke attacks se bahut saare elephants, horses, chariots aur soldiers battlefield mein girne lage.

Poora maidan fallen warriors aur destroyed chariots se bhar gaya.

Section LXXIII Ka Main Message
1. Ashwatthama ne Arjuna aur Krishna dono par powerful attacks kiye.
2. Arjuna ne Ashwatthama ko seriously injure kiya, lekin guru-putra hone ke kaaran uske prati mercy dikhayi.
3. Bhima aur Duryodhana ke beech fierce archery battle hui.
4. Abhimanyu ne Chitrasena, Purumitra aur Satyavrata jaise warriors ko challenge kiya.
5. Kaurava princes ne Abhimanyu ko surround kiya, lekin woh sabka saamna karta raha.
6. Abhimanyu ne Duryodhana ke bete Lakshmana ke chaar horses aur charioteer ko maar diya.
7. Kripacharya Lakshmana ko apne chariot mein rescue karke le gaye.
8. Bhishma ne celestial weapons se Pandava army ko heavy damage pahunchaya.
Is section ka sabse powerful moment: Abhimanyu ne kai Kaurava warriors ka ek saath saamna kiya aur Lakshmana ka chariot destroy kar diya. Itni kam age mein uski bravery aur archery skills battlefield mein sabko hairaan kar rahi thi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.62
        with st.expander("Section 6.3.62  Section LXXIV"):
            text1 = """ Section LXXIV – Satyaki Aur Bhurisravas Ka Bhayankar Yudh
Pichhle section mein Abhimanyu ne apni bravery dikhayi thi. Ab battlefield mein ek aur powerful warrior, Satyaki, apne arrows se Kaurava army ko hila dene wala tha.

Sanjaya Dhritarashtra ko batate hain ki is din Satyaki aur Bhurisravas ke beech bahut hi dangerous fight hui.
Satyaki Ne 10,000 Chariots Ko Hara Diya
Satyaki ne apna powerful bow uthaya aur bahut tezi se arrows chalane laga.

Uske arrows itni speed se nikal rahe the jaise aasman mein kaale baadal zor se baarish kar rahe hon.

Woh ek ke baad ek arrows nikaalta, bowstring par lagata aur enemies par chala deta. Uski speed dekhkar lag raha tha jaise uske haath ruk hi nahi rahe.

Duryodhana ne Satyaki ki tabahi dekhi toh use rokne ke liye 10,000 chariots ki army bhej di.

Lekin Satyaki ne apne celestial weapons ka use karke un sabhi powerful warriors ko maar giraya.

Itni badi army ko akele defeat karne ke baad Satyaki seedha Bhurisravas ki taraf badha. Bhurisravas Ne Satyaki Ko Challenge Kiya
Bhurisravas ne dekha ki Satyaki ne Kaurava army ko bahut heavy damage pahunchaya hai.

Woh gusse mein apna powerful bow lekar Satyaki ke saamne aa gaya.

Usne bhi hazaaron deadly arrows chalaye. Uske arrows itne powerful the jaise bijli ke kadakne ki awaaz ke saath aasman se thunderbolts gir rahe hon.

Bhurisravas ke attacks itne dangerous the ki Satyaki ke saath aaye soldiers dar kar alag-alag directions mein bhaagne lage.

Satyaki ab battlefield mein akela reh gaya.
Satyaki Ke 10 Bete Bhurisravas Se Ladne Aaye
Apne pita Satyaki ko akela dekhkar uske 10 bahadur bete battlefield mein aa gaye.

Unhone Bhurisravas ko challenge diya:

"Hey Bhurisravas! Tum bahut powerful warrior ho. Agar tumhe apni strength par itna confidence hai, toh hum sabse ek saath ya ek-ek karke fight karo.

Agar tum humein hara doge toh tumhari fame aur badhegi. Aur agar hum tumhe hara denge toh humein bahut khushi hogi."

Bhurisravas ne unka challenge accept kar liya.

Usne kaha:

"Theek hai! Tum sab ek saath mujh par attack karo. Main tum sabko battlefield mein maar dunga."

Aur phir shuru hua ek bahut hi dangerous battle.
Bhurisravas Ne Satyaki Ke 10 Bete Maar Diye
Satyaki ke daso beton ne milkar Bhurisravas par arrows ki baarish kar di.

Unke arrows aise gir rahe the jaise monsoon ke clouds kisi mountain par heavy rain karte hain.

Lekin Bhurisravas ne apne extraordinary archery skills se unke saare arrows hawa mein hi kaat diye.

Phir usne ek-ek karke unke bows tod diye.

Aur uske baad apne sharp arrows se Satyaki ke daso beton ke sir kaat diye.

Woh sabhi warriors battlefield mein gir pade. Apne Beton Ki Maut Dekhkar Satyaki Gusse Se Bhar Gaya
Jab Satyaki ne apne daso beton ko mara hua dekha, toh woh bahut zyada gusse mein aa gaya.

Usne zor se roar kiya aur seedha Bhurisravas par attack karne ke liye badha.

Ab dono powerful warriors ek doosre ke saamne aa gaye.

Dono ne apne chariots se ek doosre par attack kiya aur fight karte-karte dono ke horses bhi maare gaye.

Ab dono warriors ke paas chariots nahi bache.

Dono apne-apne chariots se neeche utare aur bade swords aur shields lekar ek doosre se ladne lage.

Dono ki fight dekhne layak thi.

Tab Bhima ne Satyaki ko apne chariot par bitha liya.

Dusri taraf Duryodhana ke ek bete ne Bhurisravas ko apne chariot par rescue kar liya.

Is tarah dono warriors ki sword fight us waqt ruk gayi.
Arjuna Ne 25,000 Kaurava Warriors Ko Maar Giraya
Udhar Pandavas abhi bhi Bhishma ke saath fierce battle kar rahe the.

Suraj dheere-dheere laal hone laga tha.

Isi dauraan Arjuna ne apni full strength ke saath Kaurava army par attack kiya.

Sanjaya ke according, Arjuna ne 25,000 powerful chariot warriors ko maar giraya.

Ye sabhi warriors Duryodhana ke order par Arjuna ko maarne ke liye bheje gaye the.

Lekin Arjuna ke paas pahunchne se pehle hi woh sab uske arrows ka shikaar ban gaye.

Unki condition aisi ho gayi jaise jalti hui aag mein insects girkar khatam ho jaate hain. Suraj Doob Gaya Aur Yudh Ruk Gaya
Matsya aur Kekaya warriors Arjuna aur uske bete ko support dene ke liye unke aas-paas aa gaye.

Tabhi suraj doobne laga.

Battlefield mein twilight chha gayi aur warriors ko ek doosre ko dekhna mushkil hone laga.

Bhishma ke horses aur doosre animals bhi poore din ki fighting se thak chuke the.

Isliye Bhishma ne army ko battle rokne ka order diya.

Dono taraf ke warriors apne-apne camps ki taraf laut gaye.

Pandavas aur Srinjayas apne camp mein gaye, jabki Kaurava army bhi apne camp mein lautkar raat ke liye rest karne lagi.

Is tarah us din ka bhayankar yudh khatam hua.

Section LXXIV Ka Main Message
1. Satyaki ne akele 10,000 chariot warriors ko defeat kar diya.
2. Bhurisravas ne Satyaki ko challenge kiya aur uske 10 beton se ek saath fight ki.
3. Bhurisravas ne Satyaki ke sabhi 10 beton ko maar diya.
4. Apne beton ki maut dekhkar Satyaki ne Bhurisravas par attack kiya.
5. Dono ne chariot aur phir swords se fight ki, lekin Bhima aur Duryodhana ke bete ne unhe rescue kar liya.
6. Arjuna ne 25,000 Kaurava chariot warriors ko maar giraya.
7. Suraj doobne ke baad Bhishma ne battle rok di aur dono armies apne camps mein laut gayi.
Is section ka sabse emotional moment: Satyaki ne battlefield mein apne 10 beton ko ek saath khoya. Unki maut ka badla lene ke liye woh Bhurisravas par toot pada. दूसरी तरफ, Arjuna ne akele 25,000 warriors ko maar kar apni extraordinary power dikhayi. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.62.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.63
        with st.expander("Section 6.3.63  Section LXXV"):
            text1 = """ Section LXXV – Makara Vyuha Aur Drona Ka Bhayankar Attack
Pichhle din ka yudh khatam hone ke baad Pandavas aur Kauravas dono apne camps mein aaram kar rahe the. Lekin subah hote hi ek baar phir Kurukshetra ka maidan yudh ke liye taiyaar ho gaya.

Dono taraf ke warriors apne armour pehenne lage. Elephants ko battle ke liye sajaya gaya, horses aur chariots taiyaar hue. Conches aur drums ki awaaz se poora battlefield goonj utha.
Yudhishthira Ne Makara Vyuha Banane Ka Order Diya
Yudhishthira ne apne commander Dhrishtadyumna ko bulaya aur kaha:

"Apni army ko Makara Vyuha mein arrange karo. Yeh formation enemies ko destroy karne ke liye bahut powerful hai."

Makara ka matlab crocodile hota hai. Is formation mein army ko ek bade crocodile ke shape mein arrange kiya jaata tha.

Dhrishtadyumna ne sabhi warriors ko unki positions par laga diya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.63.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Pandava army ki Makara Vyuha formation:
- Head: King Drupada aur Arjuna.
- Eyes: Nakula aur Sahadeva.
- Beak: Bhima.
- Neck: Abhimanyu, Draupadi ke bete, Ghatotkacha, Satyaki aur Yudhishthira.
- Back: King Virata, Dhrishtadyumna aur unki army.
- Left Wing: Paanch Kekaya brothers.
- Right Wing: Dhrishtaketu aur Chekitana.
- Two Feet: Kuntibhoja aur Satanika.
- Tail: Shikhandi, Somaka warriors aur Iravat.
Is tarah Pandavas ne apni poori army ko ek bade crocodile ke shape mein arrange kar diya.
Bhishma Ne Crane Jaisi Formation Banayi
Jab Bhishma ne Pandava army ki formation dekhi, toh unhone bhi apni army ko ek special formation mein arrange kiya.

Unhone ek bade crane (saaras bird) jaisi formation banayi. Kaurava army ki formation:
- Beak: Dronacharya.
- Eyes: Ashwatthama aur Kripacharya.
- Head: Kritavarma, Kamboja ke king aur Valhika warriors.
- Neck: Duryodhana, Surasena aur unke saath kai kings.
- Breast: Pragjyotisha ke king, Madra, Sauvira aur Kekaya warriors.
- Left Wing: Susarman aur uski army.
- Right Wing: Tushara, Yavana, Saka aur Chulika warriors.
- Rear: Srutayush, Satyayush aur Somadatta ke bete.
Dono armies apni-apni formations mein taiyaar ho gayi.
Dono Armies Ke Beech Yudh Shuru
Suraj nikalte hi Pandavas ne Kauravas par attack kar diya.

Battlefield mein har taraf fight hone lagi:
- Elephants ka saamna elephants se hua.
- Horsemen doosre horsemen se ladne lage.
- Chariot warriors ek doosre par arrows barsane lage.
- Elephants par baithe warriors ka saamna horsemen aur chariot warriors se hua.
- Infantry soldiers bhi ek doosre se ladne lage.
Dono armies apni full strength ke saath battlefield mein utar chuki thi.

Sanjaya kehte hain ki Pandava army Bhima, Arjuna, Nakula aur Sahadeva ke protection mein aisi lag rahi thi jaise stars se bhara hua raat ka aasman.

Dusri taraf Kaurava army Bhishma, Drona, Kripacharya, Shalya aur Duryodhana ke saath chamak rahi thi.
Bhima Aur Dronacharya Ka Saamna
Bhima ne dekha ki Dronacharya apne chariot par Pandava army ki taraf badh rahe hain.

Woh turant Drona ki division par attack karne pahunch gaya.

Dronacharya ne Bhima ko dekhte hi apne powerful bow se uske vital body parts par nau iron arrows maare.

Bhima buri tarah injured ho gaya.

Lekin usne bhi jawab diya aur Dronacharya ke charioteer ko maar giraya.

Ab Drona ko apne horses ki control khud sambhalni padi.
Drona Ne Pandava Army Mein Tabahi Macha Di
Dronacharya ne apne horses ko control karte hue Pandava army par attack jaari rakha.

Unke arrows itni tezi se gir rahe the ki Pandava soldiers ki condition aisi ho gayi jaise aag cotton ke dher ko jalakar raakh kar deti hai.

Drona aur Bhishma dono milkar Pandava army ko heavy damage pahunchane lage.

Srinjaya aur Kekaya warriors unke attacks ko bardasht nahi kar paaye aur battlefield se bhaagne lage.

Lekin doosri taraf Bhima aur Arjuna bhi Kaurava army par attack kar rahe the.

Unke attacks se Kaurava soldiers bhi buri tarah disturb ho gaye.

Is battle mein dono armies ko bahut heavy losses hue.
Dono Taraf Ke Warriors Ne Peeche Hatne Se Mana Kar Diya
Battle itni dangerous ho chuki thi ki warriors apni jaan ki parwah kiye bina lad rahe the.

Pandavas aur Kauravas ek doosre ke weapons ko apne weapons se counter kar rahe the.

Koi bhi side easily haar maanne ko taiyaar nahi thi.

Kurukshetra ka maidan ek baar phir warriors, elephants, horses aur chariots ki destruction se bharne laga.

Section LXXV Ka Main Message
1. Yudhishthira ne Dhrishtadyumna ko Pandava army ki Makara Vyuha formation banane ka order diya.
2. Pandava army ko crocodile ke shape mein arrange kiya gaya.
3. Bhishma ne Kaurava army ko crane jaisi formation mein arrange kiya.
4. Suraj nikalte hi dono armies ke beech yudh shuru ho gaya.
5. Bhima aur Dronacharya ke beech fierce battle hui.
6. Dronacharya ne Pandava army par powerful attack karke Srinjaya aur Kekaya warriors ko peeche hatne par majboor kar diya.
7. Bhima aur Arjuna ne bhi Kaurava army ko heavy damage pahunchaya.
Is section ka main highlight: Dono armies ne apni military strategy aur formations ka use kiya. Lekin battlefield mein sabse bada danger Dronacharya aur Bhishma ke attacks se Pandava army ko hua. Yudh ab aur bhi destructive hota ja raha tha. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.64
        with st.expander("Section 6.3.64  Section LXXVI"):
            text1 = """ Section LXXVI – Dhritarashtra Ka Dukh Aur Kismat Par Vishwas
Pichhle section mein Drona aur Bhishma ne Pandava army ko bahut heavy damage pahunchaya tha. Lekin ab Dhritarashtra ko ek baat samajh nahi aa rahi thi.

Unki Kaurava army itni powerful thi, usmein duniya ke best warriors the, weapons the, elephants, horses aur chariots ki koi kami nahi thi. Phir bhi unki army yudh mein haar kyun rahi thi?

Sanjaya ko apni baat batate hue Dhritarashtra ne apni army ki strength ka description diya.
Dhritarashtra Ko Apni Army Par Bahut Garv Tha
Dhritarashtra ne kaha:

"Sanjaya! Hamari army mein bahut saari qualities hain. Yeh army military rules aur strategies ke according arrange ki gayi hai. Hamare soldiers loyal hain aur hamesha hamare orders follow karte hain.

Hamare soldiers na bahut buddhe hain aur na bahut young. Sabhi physically fit, strong aur healthy hain.

Unke paas proper armour aur powerful weapons hain. Woh har tarah ke weapons use karna jaante hain." """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.64.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dhritarashtra ne bataya ki unke soldiers:
- Swords, maces aur spears se fight kar sakte hain.
- Arrows, javelins aur darts chalane mein expert hain.
- Elephants aur horses par chadhna aur utarna jaante hain.
- Aage badhna, peeche hatna aur battlefield mein movement karna jaante hain.
- Chariot aur elephant warfare mein trained hain.
Yaani unki army sirf numbers mein badi nahi thi, balki training aur experience mein bhi bahut strong thi.
Soldiers Ko Sirf Rishton Ki Wajah Se Nahi Rakha Gaya Tha
Dhritarashtra ne ek aur important baat batayi.

Unhone kaha ki soldiers ko unki family background, caste, relationship ya kisi ki recommendation ke basis par army mein nahi rakha gaya tha.

Unki skills aur abilities ko properly test kiya gaya tha. Jo soldiers capable the, unhe salary dekar army mein recruit kiya gaya.

Dhritarashtra ke according, unhone soldiers aur unke families ke saath bhi achha behaviour kiya tha.

Isliye unki army ke soldiers unke prati loyal aur devoted the.
Kaurava Army Mein Duniya Ke Powerful Warriors The
Dhritarashtra ne kaha ki unki army ko duniya ke bahut saare famous aur powerful warriors protect kar rahe the.

Unmein shamil the:
- Bhishma Pitamah
- Dronacharya
- Kripacharya
- Kritavarma
- Dushasana
- Jayadratha
- Bhagadatta
- Vikarna
- Ashwatthama
- Shakuni
- Valhika
Inke alawa bhi bahut saare powerful kings apni armies ke saath Kauravas ki taraf se fight kar rahe the.

Dhritarashtra ko lagta tha ki itne powerful warriors ki protection mein unki army ko haraana almost impossible hona chahiye.
Kaurava Army Ek Vishal Samundar Jaisi Thi
Apni army ki strength samjhane ke liye Dhritarashtra ne ek bahut interesting example diya.

Unhone kaha:

"Hamari army ek bahut bade aur gehre samundar jaisi hai."

Unhone is comparison ko detail mein samjhaya:
- Elephants aur chariots us samundar ke powerful creatures jaise hain.
- Soldiers us samundar ka paani hain.
- Horses aur doosre animals uski dangerous waves hain.
- Swords, maces, arrows aur spears us samundar mein pade weapons jaise hain.
- Soldiers ke flags, golden ornaments aur decorated elephants us samundar ko aur bhi magnificent banate hain.
Aur is vishal army ko Bhishma, Drona, Kripacharya aur doosre great warriors protect kar rahe the.

Dhritarashtra ko yakeen tha ki aisi army ko defeat karna kisi ke liye bhi bahut mushkil hona chahiye. Phir Bhi Kaurava Army Haar Kyun Rahi Thi?
Apni army ki itni saari strengths batane ke baad Dhritarashtra dukhi ho gaye.

Unhone Sanjaya se kaha:

"Itni powerful army hone ke bawajood agar hamare soldiers battlefield mein maare ja rahe hain, toh iska reason sirf Destiny ya kismat hi ho sakti hai.

Maine kabhi nahi suna ki duniya mein pehle kabhi itni badi aur well-trained army yudh ke liye taiyaar hui ho.

Phir bhi hamari army destroy ho rahi hai. Yeh sab kuch unnatural lagta hai."

Dhritarashtra ko lagne laga ki shayad jo kuch ho raha hai, woh pehle se hi destiny mein likha hua tha.
Dhritarashtra Ko Vidura Ki Advice Yaad Aayi
Ab Dhritarashtra ko apne bhai Vidura ki baatein yaad aane lagi.

Vidura ne kai baar Duryodhana ko samjhaya tha ki Pandavas ke saath injustice mat karo. Unke saath peace bana kar rakho aur unka rightful kingdom unhe de do.

Lekin Duryodhana ne kabhi Vidura ki advice accept nahi ki.

Dhritarashtra ne Sanjaya se kaha:

"Vidura ek bahut wise aur knowledgeable person the. Unhone hamesha hamare benefit ke liye advice di thi.

Mujhe lagta hai unhone pehle hi samajh liya tha ki future mein kya hone wala hai. Shayad isi wajah se woh baar-baar humein sahi raasta dikhane ki koshish kar rahe the."
Sab Kuch Creator Ki Planning Ke According Hota Hai?
Aakhir mein Dhritarashtra ne kaha ki shayad yeh sab kuch pehle se hi Creator ke plan ka hissa tha.

Unke according, jo kuch Creator ne decide kar diya hai, woh hokar hi rahega. Use badla nahi ja sakta.

Is tarah Dhritarashtra apni army ki defeat ka reason destiny ko maanne lage.

Section LXXVI Ka Main Message
1. Dhritarashtra ko apni Kaurava army ki training, strength aur loyalty par bahut garv tha.
2. Unki army mein duniya ke bahut saare powerful warriors aur kings the.
3. Dhritarashtra ne apni army ko ek vishal aur powerful samundar se compare kiya.
4. Itni powerful army ke bawajood Kauravas ko losses ho rahe the.
5. Dhritarashtra ko Vidura ki purani advice yaad aayi, jise Duryodhana ne ignore kiya tha.
6. Aakhir mein Dhritarashtra ne apni army ki defeat ko Destiny aur Creator ki planning ka result maana.
Is section ka sabse important lesson: Kabhi-kabhi insaan ke paas power, resources aur capable log sab kuch hote hain, lekin galat decisions ka result phir bhi saamne aata hai. Dhritarashtra ko ab Vidura ki advice yaad aa rahi thi, lekin us waqt tak bahut der ho chuki thi. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.65
        with st.expander("Section 6.3.65  Section LXXVII"):
            text1 = """ Pasted markdown.md
Document
Section LXXVII – Bhima Ka Kaurava Army Mein Akela Pravesh Aur Dhrishtadyumna Ki Veerta
Is section mein battlefield ka yudh aur bhi dangerous ho jaata hai. Bhima akela Kaurava army ke beech ghus jaata hai. Duryodhana ke bhai use chaaron taraf se gher lete hain. Lekin Bhima bilkul nahi darta.

Dusri taraf Dhrishtadyumna apne dost Bhima ko bachane ke liye Drona aur Kaurava warriors se takra jaata hai.

Sanjaya Ne Dhritarashtra Ko Uski Galti Yaad Dilayi
Sanjaya ne Dhritarashtra se kaha:

"Rajan, aaj jo kuch aapke saath ho raha hai, uski zimmedari aapki apni galtiyon ki wajah se hai.

Aap jaante the ki Pandavas ke saath anyaay ho raha hai, lekin aapne use roka nahi.

Dyut Sabha mein dice game bhi aapki wajah se hua tha. Aur aaj Pandavas ke saath yeh bhayankar yudh bhi aapke decisions ka result hai.

Insaan ko apne karmon ka phal khud hi bhugatna padta hai. Isliye aapko bhi apne karmon ka result face karna hoga. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.65.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Ab shaant rahiye aur meri baat suniye. Main aapko battlefield ka haal batata hoon."
Bhima Akela Kaurava Army Ke Beech Ghusa
Bhima ne apne powerful arrows se Kaurava army ki formation ko tod diya aur Duryodhana ke chhote bhaiyon ki taraf badha.

Wahan usne Dushasana, Durvisaha, Dussaha, Durmada, Jaya, Jayasena, Vikarna, Chitrasena, Sudarshana, Charuchitra, Suvarman, Dushkarna aur Karna jaise warriors ko dekha.

Ye sabhi warriors Bhishma ki protection mein Kaurava army ke andar maujood the.

Bhima ko apne beech dekhkar Kaurava warriors ne kaha:

"Yeh hamare beech akela aa gaya hai. Aaj ise maar daalte hain!"

Unhone Bhima ko chaaron taraf se gher liya. Bhima Ne Hazaaron Warriors Ka Saamna Kiya
Bhima chaaron taraf se surrounded tha. Hazaaron chariot warriors us par arrows ki baarish karne lage.

Lekin Bhima ke dil mein bilkul darr nahi tha.

Sanjaya kehte hain ki Bhima us waqt aisa lag raha tha jaise pralaya ke samay Surya ko powerful planets ne gher liya ho.

Bhima ne apne aas-paas ke kai chariot warriors, elephant riders aur horsemen ko maar giraya.

Jab usne dekha ki Duryodhana ke bhai use jaan se maarne ke iraade se attack kar rahe hain, toh usne apna chariot chhod diya.

Usne apni powerful Gada (mace) uthayi aur Kaurava army ke beech tabahi machani shuru kar di.
Dhrishtadyumna Ko Bhima Ki Chinta Hui
Udhar Dhrishtadyumna Dronacharya ke saath fight kar raha tha.

Lekin jab woh Bhima ke chariot ke paas pahuncha, toh usne dekha ki chariot khaali hai. Sirf Bhima ka charioteer Vishoka wahan maujood tha.

Dhrishtadyumna yeh dekhkar bahut pareshan ho gaya.

Usne Vishoka se poocha:

"Mera dost Bhima kahan hai? Woh mere liye apni jaan se bhi zyada important hai!"

Vishoka ne jawab diya:

"Rajkumar, Bhima ne mujhe yahin horses ko rok kar wait karne ka order diya hai.

Woh akela hi Kaurava army ke beech ghus gaya hai. Usne kaha tha ki woh un warriors ko khatam karega jo uski jaan lene ke iraade se uske peeche aaye hain.

Jab Bhima apni Gada lekar dushman ki army mein ghusa, toh hamare soldiers bhi bahut khush aur excited ho gaye the."
Dhrishtadyumna Ne Bhima Ko Akela Chhodne Se Mana Kar Diya
Vishoka ki baat sunkar Dhrishtadyumna ne kaha:

"Bhima mera dost aur rishtedaar hai. Woh mujh par bharosa karta hai aur main bhi uske prati loyal hoon.

Agar main use battlefield mein akela chhodkar wapas chala gaya, toh duniya mere baare mein kya kahegi?

Ek Kshatriya ke liye apne dost ko danger mein chhod dena bahut bada apmaan hai.

Chahe mujhe apni jaan hi kyun na deni pade, main Bhima ko akela nahi chhodunga.

Main bhi uske paas jaunga aur enemies ka saamna karunga!"

Yeh kehkar Dhrishtadyumna Bhima ke peeche chal pada.
Bhima Aur Dhrishtadyumna Ne Milkar Kaurava Army Par Attack Kiya
Dhrishtadyumna Bhima ke banaye hue raaste se aage badha.

Raaste mein use toote hue chariots aur Gada ke attacks se kuchle hue elephants dikhai diye.

Aakhirkar usne Bhima ko dekh liya.

Bhima apni Gada lekar Kaurava soldiers ko aise maar raha tha jaise ek powerful storm pedon ki rows ko gira deta hai.

Kaurava soldiers ke beech cheekh-pukaar machi hui thi.

Lekin ab Kaurava warriors ne Bhima ko chaaron taraf se gher liya aur us par arrows barsane lage.

Bhima paidal khada tha, uske body par arrows lage hue the aur haath mein Gada thi.

Dhrishtadyumna turant uske paas pahuncha.

Usne Bhima ko apne chariot par bithaya, uske body se arrows nikale aur use gale laga kar himmat di. Duryodhana Ne Apne Bhaiyon Ko Dhrishtadyumna Par Attack Karne Bheja
Jab Duryodhana ne dekha ki Dhrishtadyumna Bhima ke saath aa gaya hai, toh usne apne bhaiyon se kaha:

"Dhrishtadyumna ab Bhima ke saath mil gaya hai. Tum sab milkar us par attack karo aur use maar daalo!"

Duryodhana ke bhai weapons lekar Dhrishtadyumna ki taraf badhe.

Unhone apne bows se itne arrows chalaye ki poora battlefield arrows se cover ho gaya.

Lekin Dhrishtadyumna bilkul nahi ghabraya.
Dhrishtadyumna Ne Pramohana Weapon Ka Use Kiya
Dhrishtadyumna ne dekha ki Duryodhana ke bhai use chaaron taraf se gher kar attack kar rahe hain.

Tab usne ek special celestial weapon ka use kiya, jiska naam tha Pramohana Astra.

Is weapon ka effect bahut extraordinary tha.

Jaise hi Dhrishtadyumna ne iska use kiya, Kaurava warriors apne hosh kho baithe.

Unki sochne-samajhne ki ability aur physical strength dono prabhavit ho gayi.

Kai warriors apne chariots, horses aur elephants ke saath battlefield se idhar-udhar bhaagne lage.

Kuch warriors behosh hokar gir pade.

Kaurava army mein confusion aur panic mach gaya.
Dronacharya Ne Drupada Ko Hara Diya
Isi beech Dronacharya ne King Drupada par teen powerful arrows chalaye.

Drupada buri tarah injured ho gaye aur battlefield chhodkar chale gaye.

Drona ne unhe defeat karne ke baad apna conch bajaya.

Uski awaaz sunkar Somaka warriors ke beech darr phail gaya.

Lekin jab Drona ko pata chala ki Dhrishtadyumna ne unke students aur Duryodhana ke bhaiyon par Pramohana Astra ka use kiya hai, toh woh turant unhe bachane ke liye pahunch gaye.
Dronacharya Ne Prajna Astra Se Pramohana Astra Ko Rok Diya
Drona ne dekha ki Duryodhana ke bete aur doosre Kaurava warriors behosh pade hain.

Tab unhone Prajna Astra ka use kiya.

Is weapon ne Dhrishtadyumna ke Pramohana Astra ke effect ko neutralize kar diya.

Dheere-dheere Kaurava warriors ko hosh aane laga.

Hosh mein aate hi woh dobara Bhima aur Dhrishtadyumna se fight karne lage. Yudhishthira Ne Abhimanyu Ko Rescue Mission Par Bheja
Udhar Yudhishthira ko Bhima aur Dhrishtadyumna ki safety ki bahut chinta ho rahi thi.

Unhone turant order diya:

"Subhadra ke bete Abhimanyu ke leadership mein 12 brave chariot warriors ko bhejo.

Unka kaam Bhima aur Dhrishtadyumna tak pahunchna aur unki situation ka pata lagana hai."

Abhimanyu ke saath Kaikeya warriors, Draupadi ke bete aur Dhrishtaketu bhi the.

In sabhi warriors ne Suchimukha Vyuha banaya.

Suchimukha ka matlab hota hai needle-shaped formation. Ismein army ka front bahut pointed hota hai, jo enemy formation ko penetrate karne ke kaam aata hai. Abhimanyu ki leadership mein ye warriors Kaurava army ko penetrate karte hue Bhima aur Dhrishtadyumna ko rescue karne ke liye aage badhe.

Kaurava soldiers pehle hi Bhima aur Dhrishtadyumna ke attacks se pareshan the. Isliye woh Abhimanyu ki army ko rok nahi paaye.

Abhimanyu aur uske saath aaye warriors tezi se aage badhe.

Unhe dekhkar Bhima aur Dhrishtadyumna ko bhi bahut relief mila.
Dhrishtadyumna Aur Drona Ke Beech Phir Se Yudh
Jab Dhrishtadyumna ne Dronacharya ko apni taraf aate dekha, toh usne Bhima ko Kaikeya king ke chariot par bhej diya.

Phir woh khud Drona ka saamna karne ke liye aage badha.

Drona ne sabse pehle ek powerful arrow se Dhrishtadyumna ka bow kaat diya.

Phir unhone us par hundreds of arrows chala diye.

Dhrishtadyumna ne turant doosra bow uthaya aur Drona par 70 sharp arrows chala diye.

Lekin Drona ne phir se uska bow kaat diya.

Iske baad Drona ne chaar arrows se Dhrishtadyumna ke chaaron horses ko maar diya aur ek broad-headed arrow se uske charioteer ko bhi maar giraya.

Ab Dhrishtadyumna ka chariot completely destroy ho chuka tha.

Usne turant Abhimanyu ke chariot par chadhkar apni jaan bachayi.
Drona Ne Pandava Army Mein Phir Tabahi Macha Di
Dhrishtadyumna aur Bhima ke saamne hi Dronacharya ne Pandava army par ek powerful attack shuru kar diya.

Unke arrows se elephants, horses aur chariots ke soldiers mein panic phail gaya.

Pandava army ki formation tootne lagi.

Soldiers idhar-udhar bhaagne lage. Unki condition aisi ho gayi jaise samundar mein bahut tez waves aane se paani idhar-udhar ghoomne lagta hai.

Kaurava army ke soldiers yeh sab dekhkar khush ho gaye.

Unhone Dronacharya ki bravery ki zor-zor se tareef ki.

Section LXXVII Ka Main Message
1. Sanjaya ne Dhritarashtra ko yaad dilaya ki Pandavas ke saath anyaay aur dice game ki zimmedari unki bhi thi.
2. Bhima akela Kaurava army ke beech ghus gaya aur apni Gada se warriors ko maarne laga.
3. Dhrishtadyumna ne apne dost Bhima ko danger mein akela chhodne se mana kar diya.
4. Dhrishtadyumna ne Pramohana Astra se Kaurava warriors ko behosh kar diya.
5. Dronacharya ne Prajna Astra se Pramohana Astra ka effect khatam kar diya.
6. Yudhishthira ne Abhimanyu ke leadership mein 12 warriors ko Bhima aur Dhrishtadyumna ki help ke liye bheja.
7. Drona aur Dhrishtadyumna ke beech dobara fierce battle hui.
8. Drona ne Dhrishtadyumna ka chariot destroy kar diya aur Pandava army ko heavy damage pahunchaya.
Is section ka sabse important moment: Dhrishtadyumna ne Bhima ko bachane ke liye apni jaan ki parwah nahi ki. Aur jab woh khud danger mein aa gaya, toh Yudhishthira ne Abhimanyu ko 12 warriors ke saath rescue mission par bheja.

Ek important lesson: Sacchi dosti ka matlab sirf achhe waqt mein saath rehna nahi, balki mushkil waqt mein bhi apne dost ko akela na chhodna hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.66
        with st.expander("Section 6.3.66  Section LXXVIII"):
            text1 = """ Section LXXVIII – Bhima Aur Duryodhana Ke Beech Bhayankar Yudh
Pichhle section mein Drona ne Pandava army ko buri tarah damage pahunchaya tha. Ab Duryodhana dobara hosh mein aakar Bhima ke saamne khada hota hai. Dono ke beech ek baar phir bhayankar fight shuru ho jaati hai.
Duryodhana Ne Bhima Par Dobara Attack Kiya
Duryodhana ne khud ko sambhala aur Bhima par arrows ki baarish karni shuru kar di.

Uske bhai bhi ek saath Bhima par attack karne lage.

Bhima ko bhi dobara apna chariot mil gaya. Woh us par chadha aur Duryodhana aur uske bhaiyon ka saamna karne pahunch gaya.

Usne ek powerful aur majboot bow uthaya, jo sone se saja hua tha. Phir usne apne arrows se Duryodhana ke bhaiyon ko nishana banana shuru kar diya. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.66.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Bhima Aur Duryodhana Ka Seedha Muqabla
Fight ke dauraan Duryodhana ne ek bahut tez aur sharp arrow Bhima ke vital body part par maara.

Bhima buri tarah injured hua, lekin uska gussa aur badh gaya.

Usne apna bow kheenchkar Duryodhana par teen powerful arrows chalaye:
- Ek attack uski dono arms par hua.
- Ek arrow uske chest par laga.
Duryodhana itne powerful attack ke baad bhi apni jagah se nahi hila. Woh ek bade pahaad ki tarah mazboot khada raha.

Dono warriors gusse mein ek-doosre par lagataar attacks kar rahe the. Duryodhana Ke Bhaiyon Ne Bhima Ko Gher Liya
Duryodhana ke chhote bhaiyon ko apni pehle se banayi hui planning yaad aa gayi.

Unka iraada tha ki sab milkar Bhima ko khatam kar denge.

Woh sab ek saath Bhima par toot pade.

Lekin Bhima bhi peeche hatne waalon mein se nahi tha.

Sanjaya ke according, Bhima un par aise toot pada jaise ek powerful elephant apne saamne aane wale doosre elephant par attack karta hai.

Bhima ne sabse pehle Chitrasena ko ek powerful arrow se buri tarah hit kiya.

Uske baad usne Duryodhana ke baaki bhaiyon par bhi alag-alag tarah ke golden arrows barsaye.
Yudhishthira Ne Abhimanyu Ke Saath 12 Warriors Bheje
Udhar Yudhishthira ne apni army ko sahi tarah arrange kiya aur Bhima ki help ke liye 12 powerful chariot warriors bheje.

In warriors mein Abhimanyu bhi shamil tha.

Ye sabhi warriors apne golden ornaments aur weapons ke saath battlefield mein bahut impressive dikh rahe the. Unki chamak Surya aur Agni jaisi batayi gayi hai.

Jab Duryodhana ke bhaiyon ne in powerful warriors ko apni taraf aate dekha, toh unhone Bhima ke saath chal rahi fight chhod di.

Lekin Pandava warriors ko yeh manzoor nahi tha ki Duryodhana ke bhai bina fight kiye wahan se chale jaayein.

Woh unhe zinda bachkar jaane dene ke liye taiyaar nahi the. Section LXXVIII Ka Main Message
1. Duryodhana ne hosh mein aakar dobara Bhima par attack kiya.
2. Bhima ne Duryodhana ke attack ka jawab teen powerful arrows se diya.
3. Duryodhana ke bhaiyon ne milkar Bhima ko maarne ki koshish ki.
4. Bhima ne Chitrasena aur doosre Kaurava warriors par powerful attacks kiye.
5. Yudhishthira ne Abhimanyu samet 12 chariot warriors ko Bhima ki help ke liye bheja.
6. Pandava warriors ko dekhkar Duryodhana ke bhaiyon ne Bhima ke saath fight chhod di.
Is section ka main highlight: Bhima akela Duryodhana aur uske bhaiyon ka saamna kar raha tha, lekin Yudhishthira ne Abhimanyu ke saath 12 powerful warriors bhejkar uski support ki.

Lesson: Mushkil waqt mein himmat ke saath-saath apne saathiyon ka support bhi bahut zaroori hota hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.67
        with st.expander("Section 6.3.67  Section LXXIX"):
            text1 = """ Section LXXIX – Abhimanyu Ka Shaurya Aur Kurukshetra Ka Bhayankar Yudh
Pichhle section mein Yudhishthira ne Abhimanyu ke saath 12 powerful warriors ko Bhima ki help ke liye bheja tha. Ab Abhimanyu, Bhima aur Dhrishtadyumna milkar Kaurava army par attack karte hain.

Dono taraf ke warriors ke beech itna bhayankar yudh hota hai ki poora Kurukshetra battlefield khoon se bhar jaata hai.
Abhimanyu Aur Bhima Ka Kaurava Warriors Par Attack
Abhimanyu, Bhima ke saath milkar Duryodhana ke bhaiyon aur Kaurava warriors ka peecha karne lagta hai.

Jab Duryodhana aur uski army ke doosre powerful warriors ne dekha ki Abhimanyu, Bhima aur Dhrishtadyumna ek saath unki army ke beech hain, toh unhone apne bows uthaye aur tezi se unki taraf badhe. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.67.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Dopahar ke baad battlefield mein ek bahut bhayankar fight shuru ho gayi.
Abhimanyu Ne Vikarna Ko Haraaya
Fight ke dauraan Abhimanyu ne Vikarna ke chariot par attack kiya.

Sabse pehle usne apne arrows se Vikarna ke horses ko maar giraya. Phir usne Vikarna par 25 arrows chala diye.

Vikarna ka chariot horses ke bina bekaar ho gaya, isliye use apna chariot chhodna pada.

Woh apne bhai Chitrasena ke chariot par chadh gaya.

Ab Vikarna aur Chitrasena ek hi chariot par khade hokar Abhimanyu ka saamna karne lage.

Dono bhaiyon ne milkar Abhimanyu par arrows ki baarish kar di.

Durjaya ne bhi Vikarna ke saath milkar Abhimanyu par paanch iron arrows chalaye.

Lekin Abhimanyu bilkul nahi hila. Woh Meru Parvat ki tarah mazboot khada raha aur lagataar unka saamna karta raha. Dushasana Aur Panch Kaikeya Bhaiyon Ka Yudh
Dusri taraf Dushasana ka saamna paanch Kaikeya brothers se hua.

Paanchon bhai milkar Dushasana par attack kar rahe the.

Yeh bhi battlefield ka ek intense confrontation tha.
Draupadi Ke Bete Duryodhana Se Bhid Gaye
Isi beech Draupadi ke paanchon beton ne gusse mein Duryodhana ko challenge kiya.

Har ek ne Duryodhana par teen arrows chalaye.

Duryodhana ne bhi haar nahi maani. Usne Draupadi ke har bete par sharp arrows se jawab diya.

Dono taraf se arrows lagne ke kaaran Duryodhana ka sharir khoon se bhar gaya. Sanjaya uski tulna ek aise pahaad se karte hain jis par laal rang mila hua paani beh raha ho.
Bhishma Ne Pandava Army Par Tabahi Macha Di
Jab battlefield ke ek taraf Abhimanyu aur Bhima Kaurava warriors se lad rahe the, tab doosri taraf Bhishma Pandava army par lagataar attack kar rahe the.

Bhishma apne arrows se Pandava soldiers ko buri tarah damage pahunchate rahe.

Woh apni army ke liye ek bahut powerful warrior sabit ho rahe the.

Udhar battlefield ke doosre hisse mein Arjuna bhi apne famous bow Gandiva se enemies ka saamna kar raha tha.

Uske Gandiva ki powerful twang poore battlefield mein sunai de rahi thi. Kurukshetra Ka Battlefield Khoon Ke Samundar Jaisa Ban Gaya
Sanjaya Dhritarashtra ko battlefield ka bahut bhayankar scene batate hain.

Dono armies ke hazaaron warriors maare ja chuke the. Kai soldiers ke sir unke dhad se alag ho gaye the.

Battlefield ka scene ek khoon ke samundar jaisa lag raha tha:
- Arrows us samundar ki tez lehron jaise dikh rahe the.
- Elephants us samundar ke beech islands jaise lag rahe the.
- Horses uski waves jaise the.
- Chariots boats ki tarah dikh rahe the, jin par warriors yudh kar rahe the.
Kai warriors ke arms cut chuke the. Kuch ke armour toot gaye the aur kai soldiers buri tarah injured hokar zameen par pade the.

Mare hue elephants ke bade-bade bodies battlefield mein aise dikh rahe the jaise wahan pahaad bikhre pade hon.

Yeh ek bahut hi terrifying scene tha. Dono Armies Ka Ek Bhi Warrior Peeche Hatne Ko Taiyaar Nahi Tha
Itni tabahi aur itne saare deaths ke bawajood Sanjaya ek extraordinary baat batate hain.

Unke according, na Kaurava army mein aur na hi Pandava army mein koi aisa warrior tha jo fight karne se bachna chahta ho.

Dono taraf ke warriors poori himmat ke saath lad rahe the.

Sabhi ke mann mein victory aur glory paane ki ichha thi.

Kisi ne bhi aasani se haar maanne ya battlefield chhodne ka iraada nahi dikhaya.

Section LXXIX Ka Main Message
1. Abhimanyu aur Bhima ne milkar Kaurava warriors par attack kiya.
2. Abhimanyu ne Vikarna ke horses maar diye aur use apna chariot chhodna pada.
3. Vikarna aur Chitrasena ne ek hi chariot se Abhimanyu ka saamna kiya, lekin Abhimanyu mazbooti se lada.
4. Dushasana ka saamna paanch Kaikeya brothers se hua.
5. Draupadi ke beton ne milkar Duryodhana par attack kiya.
6. Bhishma ne Pandava army ko heavy damage pahunchaya, jabki Arjuna Gandiva se doosri taraf yudh kar raha tha.
7. Battlefield ek khoon ke samundar jaisa ban gaya.
8. Dono armies ke warriors victory aur glory ke liye bina peeche hate ladte rahe.
Is section ka main highlight: Abhimanyu ne ek saath kai Kaurava warriors ka saamna kiya aur Vikarna jaise powerful warrior ko bhi apne chariot se utarne par majboor kar diya.

Ek important lesson: Himmat ka matlab sirf powerful hona nahi, balki mushkil situations mein bhi apne iraade par mazboot rehna hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.68
        with st.expander("Section 6.3.68  Section LXXX"):
            text1 = """ Section LXXX – Bhima Aur Duryodhana Ka Bhayankar Yudh
Kurukshetra mein shaam hone lagi thi. Suraj laal rang ka dikh raha tha. Tabhi Duryodhana ne Bhima ko dekha aur use maarne ke iraade se apne rath par seedha uski taraf badha.

Bhima ne Duryodhana ko apni taraf aate dekha. Woh bahut gusse mein tha. Usne kaha:

"Jis din ka main itne saalon se intezaar kar raha tha, woh aaj aa gaya hai! Duryodhana, agar tumne abhi yudh nahi chhoda, toh aaj main tumhara ant kar dunga.

Tumne pehle Kunti Mata aur Draupadi ko bahut dukh diya. Humein jungle mein exile ke dauran bhi bahut takleef di. Apne ghamand mein tumne Pandavon ka apmaan kiya tha.

Tumne Karna aur Shakuni ki baaton mein aakar humein hamesha neecha dikhaya. Shri Krishna ne bhi tumse shanti banaye rakhne ki request ki thi, lekin tumne unki baat nahi maani. """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.68.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ Ab tumhe apne har bure kaam ka jawab milega. Aaj main tumse apna saara badla loonga!"

Itna kehkar Bhima ne apna dhanush uthaya aur ek ke baad ek 36 powerful arrows Duryodhana ki taraf chala diye.

Bhima ke teeron ne Duryodhana ka dhanush tod diya. Uske saarathi ko bhi teer lage aur uske chaaron ghode gir gaye. Bhima ne Duryodhana ke rath ki chhatri aur uska sundar jhanda bhi kaat diya.

Duryodhana ka haathi ke nishaan wala chamakta hua jhanda rath se neeche gir gaya. Yeh dekhkar Bhima ne zor se garjana ki.

Phir Bhima ne Duryodhana par 10 aur teer chala diye. Duryodhana buri tarah ghayal ho gaya.

Yeh dekhkar Kripacharya ne Duryodhana ko apne rath par bitha liya. Duryodhana dard se pareshan tha aur rath mein baith gaya.

Lekin Jayadratha ne Bhima ko maarne ke liye apni hazaaron rathon ki sena se use chaaron taraf se gher liya.

Doosri taraf Dhrishtaketu, Abhimanyu, Kekaya ke paanch bhai aur Draupadi ke putra bhi Kaurav sena se lad rahe the.

Abhimanyu Ka Shandaar Yudh

Abhimanyu ne Kaurav yoddhaon par apne teeron ki baarish kar di. Usne har yoddha par paanch-paanch teer chalaye.

Kaurav yoddha gusse mein aa gaye. Un sabne milkar Abhimanyu par teeron ki baarish shuru kar di.

Lekin Abhimanyu bilkul nahi dara. Woh itni tezi se teer chala raha tha ki Kaurav yoddha uske hamlon se kaanpne lage.

Phir Abhimanyu ne Vikarna ko apna nishana banaya. Usne 14 khatarnak teer chalaye aur Vikarna ka jhanda kaat diya. Uske saarathi aur ghode bhi maare gaye.

Abhimanyu ne Vikarna par aur bhi teer barsaye. Vikarna buri tarah ghayal ho gaya.

Apne bhai Vikarna ki yeh haalat dekhkar uske doosre bhai bhi Abhimanyu par hamla karne aa gaye.

Yoddhaon Ke Beech Bhayankar Ladai

Ab Kaurav aur Pandav yoddhaon ke beech har taraf yudh hone laga.

Durmukha ne Srutakarman par teer chalaye. Uska jhanda kaat diya aur uske ghode aur saarathi ko bhi maar diya.

Lekin Srutakarman ne haar nahi maani. Usne gusse mein ek powerful bhala Durmukha ki taraf phenka. Woh bhala uske kavach ko paar karta hua zameen mein ja ghusa.

Tabhi Sutasoma ne Srutakarman ko apne rath par jagah di aur use bachaya.

Doosri taraf Srutakirti ne Jayatsena par hamla kiya. Lekin Jayatsena ne ek teer se uska dhanush kaat diya.

Yeh dekhkar Satanika apne bhai ki madad ke liye aa gaya. Usne Jayatsena par lagataar teer chalaye aur uske seene par bhi ek teer maara.

Tabhi Dushkarna apne bhai Jayatsena ki madad ke liye aa gaya. Usne Satanika ka dhanush aur teer kaat diya.

Lekin Satanika ne turant doosra dhanush uthaya aur Dushkarna ko lalkara.

Usne kaha, "Ruko! Ab tum mujhse bach nahi sakte!"

Phir Satanika ne Dushkarna par teeron ki baarish kar di. Usne uska dhanush kaat diya, saarathi ko maar diya aur uske saaton ghode bhi gira diye.

Aakhir mein Satanika ka ek powerful teer Dushkarna ke seene mein laga. Dushkarna bijli se gire ped ki tarah zameen par gir gaya.

Dushkarna ko girta dekh paanch Kaurav yoddhaon ne Satanika ko chaaron taraf se gher liya aur us par teer barsane lage.

Kekaya Bhaiyon Ka Hamla

Tabhi Kekaya ke paanch bahadur bhai Satanika ko bachane ke liye aa gaye.

Yeh dekhkar Duryodhana ke bhai Durmukha, Durjaya, Durmarshana, Satranjaya aur Satrusha bhi unse ladne aa gaye.

Dono taraf ke yoddha apne sundar rathon par sawar the. Unke ghode saje hue the aur rathon par rang-birange jhande lage the.

Dono senaon ke beech bahut bhayankar yudh shuru ho gaya. Teer chal rahe the, ghode daud rahe the aur haathi ek-doosre se takra rahe the.

Yeh ladai suraj dhalne tak chalti rahi. Battlefield par hazaaron yoddha aur ghode gir chuke the.

Bhishma Pitamah Ka Aakhri Hamla

Isi beech Bhishma Pitamah ne bhi Pandav sena par apne teeron se bhayankar hamla shuru kar diya.

Unhone apne powerful teeron se Pandav aur Panchal sena ke kai yoddhaon ko hara diya. Unke hamle se Pandav sena ki lines tootne lagi.

Aakhir mein Bhishma Pitamah ne apni sena ko wapas bulaya aur yudh rok kar apne camp ki taraf laut gaye.

Udhar Yudhishthira ne Bhima aur Dhrishtadyumna ko surakshit dekha toh woh bahut khush hue.

Unhone pyaar se dono ke sir ko chuma aur phir apne camp ki taraf laut gaye.

Is tarah Kurukshetra ke yudh ka ek aur din samaapt hua. Lekin dono taraf ke yoddha jaante the ki agle din phir ek naya aur bhayankar sangharsh unka intezaar kar raha hai. """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.69
        with st.expander("Section 6.3.69  Section LXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.69.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.70
        with st.expander("Section 6.3.70  Section LXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.70.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.71
        with st.expander("Section 6.3.71  Section LXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.71.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.72
        with st.expander("Section 6.3.72  Section LXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.72.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.73
        with st.expander("Section 6.3.73  Section LXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.73.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.74
        with st.expander("Section 6.3.74  Section LXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.74.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.75
        with st.expander("Section 6.3.75  Section LXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.75.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.76
        with st.expander("Section 6.3.76  Section LXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.76.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.77
        with st.expander("Section 6.3.77  Section LXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.77.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.78
        with st.expander("Section 6.3.78  Section XC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.78.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # Section 6.3.79
        with st.expander("Section 6.3.79  Section XCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.79.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.80
        with st.expander("Section 6.3.80  Section XCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.80.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.81
        with st.expander("Section 6.3.81  Section XCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.81.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.82
        with st.expander("Section 6.3.82  Section XCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.82.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.83
        with st.expander("Section 6.3.83  Section XCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.83.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.84
        with st.expander("Section 6.3.84  Section XCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.84.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.85
        with st.expander("Section 6.3.85  Section XCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.85.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.86
        with st.expander("Section 6.3.86  Section XCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.86.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.87
        with st.expander("Section 6.3.87  Section XCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.87.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.88
        with st.expander("Section 6.3.88  Section C"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.88.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.89
        with st.expander("Section 6.3.89  Section CI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.89.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.90
        with st.expander("Section 6.3.90  Section CII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.90.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.91
        with st.expander("Section 6.3.91  Section CIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.91.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.92
        with st.expander("Section 6.3.92  Section CIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.92.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.93
        with st.expander("Section 6.3.93  Section CV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.93.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.94
        with st.expander("Section 6.3.94  Section CVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.94.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.95
        with st.expander("Section 6.3.95  Section CVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.95.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.96
        with st.expander("Section 6.3.96  Section CVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.96.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.97
        with st.expander("Section 6.3.97  Section CIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.97.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.98
        with st.expander("Section 6.3.98  Section CX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.98.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.99
        with st.expander("Section 6.3.99  Section CXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.99.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.100
        with st.expander("Section 6.3.100  Section CXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.100.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.101
        with st.expander("Section 6.3.101  Section CXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.101.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.102
        with st.expander("Section 6.3.102  Section CXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.102.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.103
        with st.expander("Section 6.3.103  Section CXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.103.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.104
        with st.expander("Section 6.3.104  Section CXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.104.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.105
        with st.expander("Section 6.3.105  Section CXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.105.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.106
        with st.expander("Section 6.3.106  Section CXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.106.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.107
        with st.expander("Section 6.3.107  Section CXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.107.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.108
        with st.expander("Section 6.3.108  Section CXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.108.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # Section 6.3.109
        with st.expander("Section 6.3.109  Section CXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.109.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.110
        with st.expander("Section 6.3.110  Section CXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.110.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.111
        with st.expander("Section 6.3.111  Section CXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.111.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.112
        with st.expander("Section 6.3.112  Section CXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.112.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
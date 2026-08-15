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
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.32
        with st.expander("Section 6.3.32  Section XLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.33
        with st.expander("Section 6.3.33  Section XLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.34
        with st.expander("Section 6.3.34  Section XLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.35
        with st.expander("Section 6.3.35  Section XLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.36
        with st.expander("Section 6.3.36  Section XLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.37
        with st.expander("Section 6.3.37  Section XLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.38
        with st.expander("Section 6.3.38  Section L"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # Section 6.3.39
        with st.expander("Section 6.3.39  Section LI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.40
        with st.expander("Section 6.3.40  Section LII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.41
        with st.expander("Section 6.3.41  Section LIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.41.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.42
        with st.expander("Section 6.3.42  Section LIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.42.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.43
        with st.expander("Section 6.3.43  Section LV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.43.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.44
        with st.expander("Section 6.3.44  Section LVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.44.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.45
        with st.expander("Section 6.3.45  Section LVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.45.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.46
        with st.expander("Section 6.3.46  Section LVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.46.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.47
        with st.expander("Section 6.3.47  Section LIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.47.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.48
        with st.expander("Section 6.3.48  Section LX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.48.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.49
        with st.expander("Section 6.3.49  Section LXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.49.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.50
        with st.expander("Section 6.3.50  Section LXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.50.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.51
        with st.expander("Section 6.3.51  Section LXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.51.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.52
        with st.expander("Section 6.3.52  Section LXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.52.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.53
        with st.expander("Section 6.3.53  Section LXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.53.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.54
        with st.expander("Section 6.3.54  Section LXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.54.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.55
        with st.expander("Section 6.3.55  Section LXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.55.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.56
        with st.expander("Section 6.3.56  Section LXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.56.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.57
        with st.expander("Section 6.3.57  Section LXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.57.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.58
        with st.expander("Section 6.3.58  Section LXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.58.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.59
        with st.expander("Section 6.3.59  Section LXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.59.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.60
        with st.expander("Section 6.3.60  Section LXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.60.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.61
        with st.expander("Section 6.3.61  Section LXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.61.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.62
        with st.expander("Section 6.3.62  Section LXXIV"):
            text1 = """ """
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
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.63.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.64
        with st.expander("Section 6.3.64  Section LXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.64.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.65
        with st.expander("Section 6.3.65  Section LXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.65.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.66
        with st.expander("Section 6.3.66  Section LXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.66.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.67
        with st.expander("Section 6.3.67  Section LXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.67.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.68
        with st.expander("Section 6.3.68  Section LXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.68.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
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
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
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.20
        with st.expander("Section 6.3.20  Section XXXII (Bhagavad Gita Chapter VIII)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.21
        with st.expander("Section 6.3.21  Section XXXIII (Bhagavad Gita Chapter IX)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.22
        with st.expander("Section 6.3.22  Section XXXIV (Bhagavad Gita Chapter X)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.23
        with st.expander("Section 6.3.23  Section XXXV (Bhagavad Gita Chapter XI)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.24
        with st.expander("Section 6.3.24  Section XXXVI (Bhagavad Gita Chapter XII)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.25
        with st.expander("Section 6.3.25  Section XXXVII (Bhagavad Gita Chapter XIII)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.26
        with st.expander("Section 6.3.26  Section XXXVIII (Bhagavad Gita Chapter XIV)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.27
        with st.expander("Section 6.3.27  Section XXXIX (Bhagavad Gita Chapter XV)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.28
        with st.expander("Section 6.3.28  Section XL (Bhagavad Gita Chapter XVI)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )
        # Section 6.3.29
        with st.expander("Section 6.3.29  Section XLI (Bhagavad Gita Chapter XVII)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


        # Section 6.3.30
        with st.expander("Section 6.3.30  Section XLII (Bhagavad Gita Chapter XVIII)"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter6/6.3.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
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
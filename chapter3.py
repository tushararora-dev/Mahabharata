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
    create_image_text_layout("attached_assets/chapter3/chapter3.jpg", layout="full")
    create_image_text_layout("attached_assets/chapter3/banner3.jpg", layout="full")


    text0 = """
    <h2>Vana Parva / Aranyaka Parva (The Book of the Forest)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")
    
    with st.expander("Chapter 3.1  Aranyaka Parva (Forest Book)"):

        # --------------------------------------------------
        # Section 3.1.1
        # --------------------------------------------------
        with st.expander("Section 3.1.1  Section I"):
            text1 = """ 
            Om.
Pehle naman hai Narayana,
Nara,
aur Saraswati ko.
Phir kaha jaata hai— Jaya.

Janamejaya ne poocha—

“O mahan rishi,
jab Pandavas
ko Dhritarashtra ke putron ne
jua mein dhokhe se hara diya,
aur un par kathor shabd bole gaye,
tab mere poorvajon ne kya kiya?"""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Vanvaas ke un baarah saalon mein
woh jungle mein kaise rahe?
Kaun-kaun unke saath chala?
Woh kya khaate the,
kahaan rehte the?

Aur sabse zyada—
woh pavitra naari,
Draupadi,
jo sach bolne wali aur pativrata thi,
usne itna kasht kaise saha?

Mujhe sab kuch vistar se sunna hai.
Meri jigyasa bahut gehri hai.”

Vaisampayana bole—

“Jab Pandav jua mein haare,
toh woh Hastinapura se nikal pade.
Unke saath Draupadi thi.
Woh shehar ke
Vardhamana Dwar se nikle.

Indrasena aur kuch sevak,
apni patniyon ke saath,
unke peechhe chale.

Jab nagarvaasiyon ko pata chala,
toh unke mann toot gaye.
Sab rone lage.
Aur kehne lage—

‘Haay!
Agar Duryodhana raja ban gaya,
toh dharm ka vinaash ho jaayega.
Woh irshaalu hai,
cruel hai,
aur achaar se door hai.

Jahan Pandav ja rahe hain,
wahi hum jaayenge.
Kyunki achhon ke saath rehna
hi jeevan ka raksha-kavach hai.’”

Nagarvaasi Pandavon ke paas aaye.
Haath jod kar bole—

“Hey raja,
aap humein chhod kar kahaan ja rahe ho?
Hum bhi saath chalenge.

Burai ke saath rehkar
man aur buddhi dono bigad jaate hain.
Achhon ke saath rehne se
jeevan sudhar jaata hai.

Jaise phool ke paas rehkar
kapda bhi sugandhit ho jaata hai,
waise hi sajjanon ke saath rehkar
gun badhte hain.

Aap mein
dharm, shaurya aur daya—
sab gun hain.
Isliye hum
aapke saath rehna chahte hain.”

Tab Yudhishthira bole—

“Tum logon ka prem
hamare liye vardaan hai.
Par ek baat suno.

Hastinapura mein
hamare pitamah Bhishma,
raja Dhritarashtra,
Vidura
aur meri maa hain.

Agar tum hamara bhala chahte ho,
toh unka dhyaan rakho.
Unhe sambhalo.
Yahi mujhe sabse zyada sukh dega.

Ab tum laut jao.
Mujhe isi se shanti milegi.”

Yudhishthira ke shabd sun kar
log zor se ro pade.
Dil bhaari tha.
Par woh maan gaye.
Aur laut gaye.

Pandav aage badhe.
Ganga ke kinaare
Pramana naam ka bargad ka ped aaya.
Shaam ho chuki thi.

Wahan unhone
pavitra jal chhua.
Raat wahi bitaayi.
Us raat
sirf paani piya.
Koi bhojan nahi.

Kuch brahman,
jo prem se saath aaye the,
unke saath ruke.
Ved-mantron ka ucharan hua.
Aag jali.
Raat shaant aur gambhir thi.

Un brahmanon ke beech
Yudhishthira
tej se chamak rahe the.
Unke madhur swar
raja ko dhairya dete rahe.

✨ Moral (Sikh):
Sachcha raja
apne dukh mein bhi
dusron ka bhala sochta hai.
Aur jo achhon ka saath chunta hai,
uska jeevan
kabhi andhkaar mein nahi jaata."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.2
        # --------------------------------------------------
        with st.expander("Section 3.1.2  Section II"):
            text1 = """ 
            Subah hui.
Raat beet chuki thi.

Kuch Brahman,
jo bhiksha par jeevan jeete the,
Pandavas ke paas aaye.
Pandav van mein pravesh karne wale the.

Tab Yudhishthira bole—

“Hum sab kuch kho chuke hain.
Rajya bhi gaya.
Sampatti bhi."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Ab hum gehre jungle ja rahe hain.
Phal, mool aur shikar par jeeyenge.
Van khatron se bhara hai.
Jangli jaanwar hain.
Saanp hain.

Tum jaise Brahmanon ka
yahan kasht badhega.
Tumhara dukh
mere liye asahniya hoga.

Isliye main tumse kehta hoon—
kripya laut jao.
Jahan tumhara mann ho,
wahin jao.”

Brahman bole—

“Hey Raja,
humara marg wahi hai
jahan tum ja rahe ho.

Humein chhodna uchit nahi.
Hum tumhare bhakt hain.
Dharm par chalne wale hain.

Devta bhi
apne bhakton par daya karte hain.
Phir hum Brahman kyun nahi?”

Yudhishthira bole—

“Main Brahmanon ka
hamesha aadar karta hoon.

Par meri yeh daridrata
mere mann ko ghabra rahi hai.
Mere bhai
pehle hi dukh mein doobe hain.
Draupadi ka kasht
unhe tod raha hai.

Main unse
tumhare liye kathin kaam
kaise karwa sakta hoon?”

Brahman bole—

“Hey Raja,
is baat ki chinta mat karo.

Hum apna bhojan
khud kar lenge.
Tapasya aur jap se
tumhara kalyan karenge.

Mithri baaton se
tumhara mann halka rakhenge.”

Yudhishthira bole—

“Tumhari baat sach hai.
Mujhe tumhari sangat
priya hai.

Par meri haalat
mujhe lajjit karti hai.
Tum jaise log
sirf mere liye kasht sahein—
yeh soch kar
mera hriday jalta hai.

Dhritarashtra ke putron par
dhikkar hai!”

Yeh keh kar
Yudhishthira ro pade.
Aur dharti par baith gaye.

Tab ek vidwaan Brahman,
Saunaka,
jo gyaan aur yoga mein nipun the,
bole—

“Hey Raja,
dukh ke hazaar kaaran hote hain.
Bhay ke sau kaaran hote hain.

Par yeh sab
agnani ko hila dete hain.
Gyani ko nahi.

Tum jaise budhimaan
kabhi mohit nahi hote.
Tumhare andar
gyaan ke aath gun hain.

Main tumhe
Mithila ke raja Janaka ke
updesh sunata hoon.

Sharir ka dukh aata hai—
rog, parishram, abhav se.
Mann ka dukh aata hai—
chinta aur shok se.

Dawai sharir ka rog mitaati hai.
Gyaan mann ka rog mitaata hai.

Jaise garam loha
paani ko bhi garam kar deta hai,
waise hi mann ka dukh
sharir ko bhi jala deta hai.

Aur jaise paani
aag bujha deta hai,
waise hi gyaan
mann ki agni bujha deta hai.

Sab dukh ki jad hai—
aasakti.

Aasakti se hi
bhay, shok, sukh aur dukh
sab paida hote hain.

Thodi si bhi aasakti
guna aur laabh ko
jalaa deti hai,
jaise chhoti si aag
poora ped jala deti hai.

Sirf cheezon ko chhod dena
sanyas nahi hai.
Unke dosh ko dekh kar
mann se chhodna
hi sachcha sanyas hai.

Kamala patra jaise
paani se geela nahi hota,
waise hi gyani purush
aasakti se prabhavit nahi hota.

Dhan se bhay aata hai.
Chor ka bhay.
Raja ka bhay.
Aag aur paani ka bhay.
Yahan tak ki
apnon ka bhay.

Dhan ko paane mein dukh.
Dhan ko bachane mein dukh.
Dhan kharch karne mein bhi dukh.

Isliye gyaani
dhan ki lalasa nahi karta.
Santosha hi
sabse bada sukh hai.

Hey Yudhishthira,
kisi cheez ki laalsa mat karo.
Moksha chahte ho
toh ichchha chhod do.”

Yudhishthira bole—

“Hey Brahman,
mera dhan chahna
apne liye nahi hai.

Main Brahmanon ka
bharan-poshan karna chahta hoon.
Grihastha ka kartavya hai
apne ashriton ka palan.

Achhe ghar mein
chaar cheezein kabhi kam nahi hoti—
baithne ki jagah,
paani,
shabd ki madhurta,
aur aadar.

Atithi ka seva
yagya ke saman hai.
Usse bhojan dena
amrit dene jaisa hai.

Is baat par
aap kya kehte hain?”

Saunaka bole—

“Hey Raja,
tumne dharm ka saar kaha.

Par duniya vichitra hai.
Bure ko wahi accha lagta hai
jo sajjan ko sharminda kare.

Indriyon ke piche bhaagne wala
patang jaise
aag mein gir jaata hai.

Gyaan ke bina
jeev baar-baar janm leta hai.
Kabhi devta.
Kabhi pashu.
Kabhi tinka.

Isliye ved kehte hain—
karm karo,
par phal ki aasakti chhod do.

Yagya, daan, tapasya,
satya, kshama,
indriya-sanyam,
aur ichchha-tyaag—
yeh hi
sachcha marg hai.

Tumne pehle hi
apna kartavya poora kiya hai.
Ab tapasya se
sab kuch siddh karo.

Tapasvi
jo chahe
kar sakta hai.”

✨ Moral (Sikh):
Dukh ka mool bahar nahi,
mann ke andar hota hai.
Aasakti chhod do,
santosh apna lo—
tabhi jungle ho ya rajmahal,
mann shaant rahega."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.3
        # --------------------------------------------------
        with st.expander("Section 3.1.3  Section III"):
            text1 = """ 
            Vaisampayana bole—

Yudhishthira,
jo Kunti ke putra the,
Saunaka ke shabd sun kar
apne guru Dhaumya ke paas gaye.

Apne bhaiyon ke beech
Yudhishthira bole—

“Brahman mere saath
van ja rahe hain.
Main khud dukhi hoon.
Unka bharan-poshan
kar paana mushkil hai.

Main unhe chhod nahi sakta.
Aur unhe khila bhi nahi sakta.
Hey Gurudev,
ab main kya karoon?”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Dhaumya ne kuch pal
dhyaan kiya.
Yog-bal se vichaar kiya.
Phir shaant swar mein bole—

“Purane yug mein
sab jeev bhookh se peedit the.

Tab Surya ne
sab par daya ki.

Surya ne apni kirnon se
jal uthaya.
Chandrama ne
use megh bana diya.
Varsha hui.
Aur dharti par
anna uga.

Isliye bhojan ka mool
Surya hi hai.
Surya sab jeevon ke pita hain.

Hey Yudhishthira,
tum Surya ka
sharan lo.

Purane raja—
Kartavirya, Vainya, Nahusha—
sab ne tapasya se
apni praja ka uddhaar kiya.

Tum bhi tapasya karo.
Aur Brahmanon ka
dharm ke saath palan karo.”

Tab Janamejaya ne pucha—

“Hey Maharshi,
Yudhishthira ne
Surya ki pooja
kaise ki?”

Vaisampayana bole—

“Dhyaan se suno.
Man ko shaant rakho.

Dhaumya ne
Yudhishthira ko
Surya ke 108 naam bataye.

Un naamon ka
uchchaaran karke
Surya ki stuti ki jaati hai.

Jo vyakti
subah Surya-stotra
shraddha se padhta hai—
use putra, dhan,
smriti aur dhairya milta hai.

Van, aag, samudra,
ya dukh—
koi bhi bhay
use chhoo nahi sakta.”

Phir Yudhishthira
Ganga ke jal mein khade hue.
Indriyon ko niyantrit kiya.
Pranayama kiya.

Aur Surya ki stuti gaayi—

“Hey Surya,
aap sansar ke netra ho.
Aap sab jeevon ki atma ho.

Aap hi
dharm, gyaan aur tapasya ho.
Devta, Rishi, Siddh—
sab aapki pooja karte hain.

Jab aap nahi ugte,
toh duniya andhi ho jaati hai.

Aap hi Indra ho.
Aap hi Vishnu ho.
Aap hi Brahma ho.

Hey Annapati,
mujhe itna bhojan do
ki main apne atithiyon
ko samman se khila sakoon.”

Surya prasann hue.
Ve prakat hue.
Aur bole—

“Hey Yudhishthira,
tumhari ichchha poori hogi.

Yeh akshaya patra lo.
Jab tak Draupadi
is patra se pehle nahi khayegi,
tab tak bhojan
kabhi samapt nahi hoga.

Aur choudah varsh baad
tum apna rajya
wapis paoge.”

Yeh keh kar
Surya antardhaan ho gaye.

Yudhishthira ne
guru Dhaumya ke charan chhooye.
Bhaiyon ko gale lagaya.

Phir Draupadi ke saath
rasoi gaye.
Thoda sa bhojan pakaya.

Par woh bhojan
badhta hi gaya.
Kabhi khatam nahi hua.

Pehle Brahmanon ne khaya.
Phir bhaiyon ne.
Phir Yudhishthira ne.
Ant mein Draupadi ne.

Aur us din ke baad
har din bhojan
akshay raha.

Is tarah
Surya ke vardaan se
Pandavon ne
Brahmanon ka palan kiya.

Yagya kiye.
Shubh tithiyon ka paalan kiya.

Aur phir
Draupadi, Dhaumya
aur Brahmanon ke saath
Kamyaka van ki or
prasthan kiya.

✨ Moral (Sikh):
Jab insaan ka mann shuddh ho
aur uddeshya seva ka ho,
toh prakriti bhi
sahayak ban jaati hai.
Shraddha + Tapasya = Akshay Phal."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.4
        # --------------------------------------------------
        with st.expander("Section 3.1.4  Section IV"):
            text1 = """ 
            Vaisampayana bole—

Pandav jab van chale gaye,
tab Dhritarashtra ka mann
bahut dukhi ho gaya.

Woh apni jagah baith kar
buddhimaan Vidura se bole—

“Vidura,
tumhari buddhi shuddh hai.
Tum dharm ko achhi tarah jaante ho.

Ab jo ho chuka hai,
uske baad humein
kya karna chahiye?

Hum apni jadon se
kaise bachen?
Log humse nafrat na karein—
iska upaay batao.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Vidura shaant swar mein bole—

“Rajya ka mool
dharm hota hai.
Laabh, sukh aur moksha—
sab dharm par tikte hain.

Isliye, hey Raja,
tum apne putron
aur Pandavon—
dono ko nyay se rakho.

Jo paap hua hai—
jua mein dhokha—
woh galat tha.
Uska prayashchit yeh hai
ki Pandavon ko
unka adhikaar wapas do.

Ek raja ka
sabse bada dharm yeh hai—
jo apna hai,
usi mein santusht rahe.
Doosron ka
lobh na kare.

Aisa karne se
tumhara naam bachega.
Parivaar bhi bachega.
Aur vinash ruk jayega.

Agar tumne aisa nahi kiya,
toh yaad rakho—
Bhima aur Arjuna
krodh mein aaye
toh kisi ko nahi chhodenge.

Jinke paas Gandiva ho,
aur Bhima jaisa bal ho,
unke liye
kya asambhav hai?

Maine pehle bhi kaha tha—
Duryodhana ko
galat raah se roko.
Par tumne nahi suna.

Ab bhi mauka hai.
Duryodhana ko alag rakho.
Aur Yudhishthira
ko raja banao.

Duryodhana, Sakuni, Karna—
sab Pandavon se
maafi maangein.

Dussasana sabha mein
Bhima aur Draupadi se
kshama maange.

Yeh hi sahi raasta hai, Raja.”

Dhritarashtra gusse mein bole—

“Vidura!
Tum jo keh rahe ho
Pandavon ke hit mein hai,
mere hit mein nahi.

Main apne putra
Duryodhana ko
kaise chhod doon?
Woh mere sharir se janma hai.

Tumhari baatein
tedhi lagti hain.
Tum chaaho toh ruko,
ya chale jao.”

Yeh keh kar
Dhritarashtra
andar chale gaye.

Vidura ne
gehri saans li.
Aur bole—

“Yeh vansh
vinash ki or ja raha hai.”

Yeh keh kar
Vidura bhi
Pandavon ke paas
chale gaye.

✨ Moral (Sikh):
Jab raja apne moh mein
dharm ko chhod deta hai,
toh buddhi ki baat
kadvi lagne lagti hai.
Par dharm ko thukraane ka
ant hamesha
vinash hota hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.5
        # --------------------------------------------------
        with st.expander("Section 3.1.5  Section V"):
            text1 = """ 
            Vaisampayana bole—

Pandav van mein rehne ka
pakka nishchay kar chuke the.
Ganga ke kinaare se
woh aage badhe.

Kurukshetra pahuche.
Sarasvati, Drishadwati
aur Yamuna mein snaan kiya.
Phir ek van se
doosre van jaate gaye."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Aakhirkaar unhone
Kamyaka Van dekha.
Yeh rishiyon ka
priye sthal tha.
Sarasvati ke kinaare
shant aur sundar van.

Wahan pakshi the.
Hiran the.
Aur shanti thi.

Pandav wahi rehne lage.
Rishiyon ne unka
sneh se swagat kiya.
Unhe dhairya aur shanti di.

Udhar Vidura,
jo hamesha Pandavon ko
yaad karte the,
ek rath par baith kar
Kamyaka Van aaye.

Jab woh wahan pahuche,
toh dekha—
Yudhishthira
Draupadi ke saath baithe the.
Saath mein Bhai
aur Brahman bhi the.

Vidura ko door se aate dekh
Yudhishthira ne
Bhima se kaha—

“Bhima,
Vidura kis sandesh ke saath aaye hain?
Kahin Sakuni ne
phir se juye ka nyota
toh nahi bheja?

Kahin woh humare
hathiyaar bhi
jeetna toh nahi chahta?
Agar Gandiva chala gaya,
toh rajya bhi
chala jayega.”

Pandav uthe.
Vidura ka
adar se swagat kiya.
Unhe beech mein
baithaya.

Thoda vishram ke baad
Pandav bole—
“Vidura ji,
aap yahan kyun aaye?”

Vidura bole—

“O Ajatashatru,
Dhritarashtra ne mujhe
bulaya tha.
Unhone poocha
kya Pandavon
aur unke liye
achha hai.

Maine wahi kaha
jo sabke liye
hitkari tha.
Par unhe
meri baat
pasand nahi aayi.

Jaise bimar vyakti
kadvi dawa nahi leta,
waise hi Dhritarashtra
meri salah
nahi maan sake.

Maine poori koshish ki.
Par jaise kamal ke patte par
paani nahi tikta,
waise hi meri baatein
unke mann mein
nahi tik paayi.

Ant mein unhone kaha—
‘Jahan chaaho chale jao.
Ab mujhe tumhari
zarurat nahi.’

Isliye, hey Pandavon,
main aapke paas
aaya hoon.

Ab meri baat dhyaan se suno—

Jo vyakti
apmaan aur anyay
sah kar bhi
sahi samay ka
intzaar karta hai,
wahi aage chal kar
poori prithvi par
raj karta hai.

Jaise choti aag
dheere-dheere
badi ban jaati hai,
waise hi dhairya
sabse bada bal hai.

Jo apni khushi
apne logon ke saath
baantta hai,
woh musibat mein
akela nahi hota.

Isliye apne logon se
sach bolna.
Unke saath
prem se rehna.
Apna bhojan bhi
baantna.

Aur kabhi ghamand
mat karna.

Yahi raja ki
sachchi samriddhi hai.”

Yudhishthira bole—

“Vidura ji,
main aapki baat
poore mann se
maanunga.

Samay aur sthan ke
anusaar
jo bhi aap salah doge,
main usi raah par
chalunga.”

✨ Moral (Sikh):
Dhairya sabse bada shastra hai.
Jo apna dukh chupchaap
sah kar sahi waqt ka
intzaar karta hai,
wahi aakhirkaar
jeet paata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.6
        # --------------------------------------------------
        with st.expander("Section 3.1.6  Section VI"):
            text1 = """ 
            Vaisampayana bole—

Vidura ke jaane ke baad,
Dhritarashtra
ka mann badal gaya.
Unhe apni galti
mehsoos hui.

Vidura ki buddhi yaad aayi.
Yuddh aur shanti—
dono mein woh mahan the.
Pandavon ka bhavishya
yaad aaya."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yeh soch kar
Dhritarashtra ka dil
bohot dukh se bhar gaya.
Sabha ke dwar par
woh behosh ho kar
gir pade.

Thodi der baad
hosh aaya.
Unhone paas khade
Sanjaya se kaha—

“Vidura mera bhai hi nahi,
mera mitra hai.
Woh dharm ka
jeeta-jaagta roop hai.

Aaj unhe yaad karke
mera hriday jal raha hai.
Sanjaya,
turant jao.
Mere bhai ko
mere paas le aao.”

Raja rone lage.
Phir bole—

“Meri gusse bhari baaton se
maine unhe door kar diya.
Jaakar dekho
kya woh abhi bhi
jeevit hain.

Agar Vidura
wapis nahi aaye,
toh main
jeena chhod dunga.”

Sanjaya ne kaha—
“Jaise aap kahein.”
Aur woh turant
Kamyaka Van ki taraf
chal pade.

Van pahunch kar
unhone dekha—
Yudhishthira
hirna-charm pehne
baithe the.
Unke paas Vidura the.
Chaaron taraf
hazaaron Brahman the.
Saath mein Bhai—
Bhima,
Arjuna,
Nakula aur Sahadeva.

Yudhishthira ko dekh kar
Sanjaya ne
vinamr pranam kiya.
Pandavon ne bhi
adar se swagat kiya.

Baithne ke baad
Sanjaya bole—

“Vidura ji,
Dhritarashtra aapko
yaad kar rahe hain.
Woh aapke bina
jeevit nahi reh pa rahe.

Pandavon ki anumati se,
aap kripya
Hastinapur wapas chaliye.
Raja aapki
pratiksha kar rahe hain.”

Yudhishthira ki anumati se
Vidura wapas chale.
Hastinapur pahunchte hi
Dhritarashtra ne unhe dekha.

Raja ne Vidura ko
apni godi mein bithaya.
Unke sir ko
pyar se chuma.
Aur bole—

“Vidura,
tum aa gaye,
yeh mera
bhaagya hai.

Tumhare bina
main din-raat
so nahi paaya.
Mujhe maaf kar do
meri kadvi baaton ke liye.”

Vidura bole—

“Raja,
maine aapko maaf kar diya.
Aap mere bade ho.
Aadar ke yogya ho.

Mujhe dono—
aapke putra
aur Pandav—
barabar pyare hain.

Par jo dukh mein hota hai,
mera dil
uski taraf
apne aap jhuk jaata hai.
Yahi dharm hai.”

Dono bhai
ek-dusre se
vinamr shabdon mein
baat karte rahe.
Unka mann
shant ho gaya.
Aur unke beech
phir se
prem aur samadhan
aa gaya.

✨ Moral (Sikh):
Galti samajh kar
maafi maang lena
kamzori nahi hoti.
Aur jo dukh mein ho,
uske liye dil pighalna
hi sachcha dharm hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.7
        # --------------------------------------------------
        with st.expander("Section 3.1.7  Section VII"):
            text1 = """ 
            Vaisampayana bole—

Jab Duryodhana ne suna
ki Vidura
wapas aa gaye hain,
aur raja ne unhe
mana bhi liya hai,
toh uska mann
jalne laga.

Uski buddhi
gusse aur andhapan se
dhundhli ho gayi."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Usne turant
Sakuni,
Karna
aur Dussasana
ko bulaya.

Duryodhana bola—

“Vidura wapas aa gaye hain.
Woh hamesha Pandavon ka
bhala chahte hain.
Agar unhone pita ji ko
Pandav wapas bulane ke liye
mana liya,
toh mera jeena mushkil ho jayega.

Agar maine Pandavon ko
phir se shehar mein
samriddh dekha,
toh main na khana khaunga,
na paani piyunga.

Main ya toh zehar kha lunga,
ya aag mein kud jaunga,
ya apne hi hathiyaaron se
jaan de dunga.
Par main unhe
sukh mein kabhi
nahi dekh sakta.”

Tab Sakuni bola—

“Rajkumaar,
itni chinta kyun?
Pandav van gaye hain
ek vachan dekar.

Woh satya par chalne wale hain.
Woh pita ke kehne par bhi
apna vachan nahi todte.

Aur maan lo,
agar woh wapas aa bhi gaye,
toh hum upar se shant rahenge.
Andar hi andar
un par nazar rakhenge.
Chinta ki koi baat nahi.”

Dussasana bola—

“Mama,
aapki baat sahi hai.
Aap jo kehte ho,
mujhe hamesha
achhi lagti hai.”

Tab Karna bola—

“Duryodhana,
hum sab tumhare saath hain.
Is waqt hum sab
ek mann ke hain.

Pandav apna samay
poora kiye bina
wapas nahi aayenge.

Aur agar galti se
woh aa bhi gaye,
toh hum unhe
phir se juye mein
hara denge.”

Yeh sab sun kar
Duryodhana ka mann
aur bojhil ho gaya.
Usne chehra pher liya.

Tab Karna
gusse mein aage aaya.
Haath hila kar
zor se bola—

“Rajkumaaro,
meri baat suno!
Hum sab Duryodhana ke
sevakar hain.

Ab aur intezaar kyun?
Chalo, abhi ke abhi
hathiyaar uthao.
Rath par chadho.
Aur van jaakar
Pandavon ko
maar daalo.

Jab tak woh
dukhi hain,
nirbal hain,
aur madad se door hain—
tab tak hum
un par bhari hain.

Agar aaj unhe
khatam kar diya,
toh sabko shanti mil jayegi.
Yahi mera vichaar hai.”

Uski baat sun kar
sab ne taali bajayi.
“Bahut achha!”
aisa kaha.

Sab apne-apne rath par chadhe.
Aur Pandavon ko
maarne ke liye
nikal pade.

Par jaise hi woh chale,
apni divya drishti se
Krishna Dvaipayana
ne sab dekh liya.

Woh turant unke paas aaye.
Unhe roka.
Aur aadesh diya—
“Ruko!”

Unhe wapas bhej kar,
mahan rishi
seedhe raja ke paas
pahunche.
Aur raja se
bolne lage…

(Kahani aage chalti hai…)

✨ Moral (Sikh):
Jab gussa buddhi par
kabza kar leta hai,
toh galat vichaar
janm lete hain.
Par dharm aur gyaan
hamesha anyay ke
raaste ko rok dete hain."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.8
        # --------------------------------------------------
        with st.expander("Section 3.1.8  Section VIII"):
            text1 = """ 
            Vyasa bole—

“O Dhritarashtra,
meri baat dhyaan se suno.
Main woh keh raha hoon
jo sab Kauravon ke
bhale ke liye hai.

Mujhe yeh achha nahi laga
ki Pandavas
juye mein dhokhe se
hara kar van bhej diye gaye.

Yaad rakho,
jab unka terahvan saal
poora hoga,
toh apna dukh yaad karke
woh Kauravon par
zehre jaise hathiyaar
barsa sakte hain."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Tumhara paapi putra
Duryodhana,
jo hamesha gusse se bhara rehta hai,
Pandavon ko kyun
maarna chahta hai?

Us murkh ko roko.
Use shaant rehne do.
Agar usne van mein jaakar
Pandavon par hamla kiya,
toh apni hi
jaan gawa baithega.

Tum bhi utne hi gyaani ho
jitne Vidura,
Bhishma,
Drona
aur Kripa.

Apnon ke saath jhagda
kabhi dharm nahi hota.
Woh paap hai.
Aur vinaash ka raasta hai.

Isliye, raja,
aise kaamon se
turant ruko.
Agar tumne
beech mein hastakshep
nahi kiya,
toh Duryodhana ki
jalan sabko
nuksaan pahunchayegi.

Agar chaaho,
toh apne putra ko
akele van bhej do.
Pandavon ke saath
rehne do.

Shaayad sang rehkar
uska mann badal jaaye.
Shaayad prem paida ho.
Aur shaayad
tumhara bhagya
sudhhar jaaye.

Par sach yeh hai—
insaan ka swabhav
aksar maut tak
saath nahi chhodta.

Ab socho—
Bhishma kya chahte hain?
Drona kya sochte hain?
Vidura ki kya raay hai?
Aur tum khud
kya theek samajhte ho?

Jo hitkari hai,
use abhi kar lo.
Samay nikal gaya,
toh sab kuch
haath se nikal jaayega.

✨ Moral (Sikh):
Jalan aur gussa
apno ko bhi dushman
bana deta hai.
Samay par liya gaya
sahi nirnay
vinaash ko
rok sakta hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.9
        # --------------------------------------------------
        with st.expander("Section 3.1.9  Section IX"):
            text1 = """ 
            Dhritarashtra bole—

“O mahan rishi,
mujhe juye ka khel
kabhi pasand nahi tha.
Par lagta hai,
kismat mujhe
wahan kheench le gayi.

Bhishma,
Drona,
Vidura,
aur Gandhari—
kisi ko bhi
yeh juya achha nahi laga."""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yeh sab murkhta thi.
Phir bhi,
pita hone ke naate,
main apne putra
Duryodhana
ko chhod nahi paata.”

Tab Vyasa bole—

“O raja,
tum jo keh rahe ho,
woh sach hai.
Putra sabse pyara hota hai.
Putra se badhkar
kuch bhi nahi.

Main tumhe
ek chhoti si kahani
sunata hoon.”

“Swarg mein ek baar
Suravi
ro rahi thi.
Use dekh kar
Indra
ne poocha—

‘Mata,
tum kyun ro rahi ho?
Kya sab theek hai?’

Suravi boli—

‘Sab theek hai,
par mera beta
dukh mein hai.
Ek kisaan
mere kamzor putra ko
maar raha hai.
Us par bojh zyada hai.
Woh girne wala hai.’

Indra ne kaha—

‘Tumhare toh
hazaaron putra hain.
Phir ek ke liye
itna dukh kyun?’

Suravi boli—

‘Mere liye
sab barabar hain.
Par jo kamzor hai,
nirdosh hai,
uske liye
dil zyada pighalta hai.’”

Vyasa bole—

“Yeh sunkar
Indra ko samajh aaya—
putra jeevan se bhi
zyada pyara hota hai.
Usne baarish bhej kar
kisaan ko roka.

Isi tarah,
tum bhi apne sab putron se
prem karte ho.
Par jo kamzor hain,
jo kam hain,
unke liye
dil aur bhi
dayalu hona chahiye.”

“Tumhare
sau se zyada putra hain.
Par Pandavas
sirf paanch hain.
Aur woh aaj
dukh mein hain.
Van mein reh rahe hain.

Unka dard
mere mann ko
hila deta hai.

Agar tum chahte ho
ki sab Kaurav
zinda rahein,
toh apne putra
Duryodhana ko kaho—
Pandavon se
shanti kar le.”

✨ Moral (Sikh):
Putra sabse pyara hota hai,
par sachcha prem
sirf apnon tak simit
nahi hota.
Jo kamzor ho,
jo dukh mein ho,
uske liye daya rakhna
hi sachcha dharm hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.1.10
        # --------------------------------------------------
        with st.expander("Section 3.1.10  Section X"):
            text1 = """ 
            Dhritarashtra bole—

“O mahan rishi,
aap jo keh rahe ho,
woh bilkul sach hai.
Yahi baat
Vidura,
Bhishma,
aur Drona
mujhe pehle bhi samjha chuke hain.

Agar aap Kuruvansh par
kripa rakhte ho,
toh mere putra
Duryodhana
ko samjhaiye.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.1.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Tab Vyasa bole—

“O raja,
abhi Maitreya
yahan aane wale hain.
Woh Pandavon ko dekh kar
laut rahe hain.
Woh tumhare putra ko
Kuruvansh ke bhale ke liye
samjhayenge.

Par dhyan rakhna—
agar unki baat
nahi maani gayi,
toh krodh mein
veer rishi shraap bhi
de sakte hain.”

Thodi der mein
Rishi Maitreya aaye.
Raja ne unka
adar-satkar kiya.
Arghya diya.
Vinay se baithaya.

Dhritarashtra bole—

“Munivar,
kya aapki yatra
shubh rahi?
Kya Pandavas
van mein theek hain?
Kya ve apna
vanvaas poora karenge?”

Maitreya bole—

“Main teerth yatra par tha.
Wahan Kamyaka van mein
maine Yudhishthira
ko dekha.
Woh deer-skin pehne,
shaant aur dhairyavaan the.

Mujhe pata chala
ki juye ke kaaran
kitni badi galti hui.
Isi liye main
Kuruvansh ke bhale ke liye
yahan aaya hoon.

Jab tum aur Bhishma
jeevit ho,
toh bhaiyon mein
jhagda hona
bilkul theek nahi.”

Phir rishi ne
Duryodhana ki taraf dekha
aur shaant swar mein bole—

“O veer Duryodhana,
Pandavon se bair
mat rakho.
Shanti hi
sabke liye bhali hai.

Pandav mahaan yoddha hain.
Unmein Bhima jaisa
balshaali veer hai.
Usne Hidimba, Kirmira,
aur mahaan yoddha
Jarasandha
tak ko maara hai.

Socho,
aise veeron se
shatru-ta ka
kya parinaam hoga?”

Par Duryodhana
chup raha.
Usne jangha thoki.
Pair se zameen khurachi.
Yeh rishi ka
apmaan tha.

Yeh dekh kar
Rishi Maitreya ka
krodh badh gaya.

Unhone jal chhua
aur kaha—

“Tumne meri baat
nahi maani.
Is ghamand ka phal
tumhe milega.

Aane wale maha yuddh mein
Bhima
apni gada se
tumhari isi jangha ko
tod dega!”

Raja Dhritarashtra
ghabra gaye.
Unhone rishi ko
shaant karna chaha.

Maitreya bole—

“Agar tumhara putra
Pandavon se shanti kar le,
toh yeh shraap
nishphal ho sakta hai.
Warna jo kaha hai,
wahi hoga.”

Itna kehkar
Rishi Maitreya
chale gaye.
Duryodhana bhi
ashant mann se
wahan se nikal gaya.

✨ Moral (Sikh):
Ghamand aur zidd
buddhi ko andha kar dete hain.
Jo samay par
sahi salah maanta hai,
wahi vinash se
bach paata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.2  Kirmirabadha Parva (Slaying of Kirmira)"):

        # --------------------------------------------------
        # Section 3.2.1
        # --------------------------------------------------
        with st.expander("Section 3.2.1  Section XI"):
            text1 = """ 
            Dhritarashtra ne poocha

Dhritarashtra bole:
“O Vidura, mujhe batao—
Kirmira ka vinash kaise hua?
Bhima aur Rakshasa ka yuddh kaise hua?”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Vidura ne kahani shuru ki

Vidura bole:
“Raja, dhyaan se suno.
Yeh Bhima ki veerta ki kahani hai.”

Jungle ka bhay

Jua haarne ke baad
Pandav raat ke andhere mein
Kamyaka van pahunche.

Yeh raat Rakshason ki ghadi hoti hai.
Tapasvi aur gop sab jungle chhod dete hain.

Rakshasa ka aagman

Achanak aag ke shole jaisa
bhayanak Rakshasa aaya.
Aankhen jal rahi thi.
Daant bahar nikle hue.
Gurrata hua rasta rok liya.

Dar ke maare jungle kaanp utha.
Pashu–pakshi bhag gaye.

Draupadi dar se kaanp uthi.
Pandav usey gher kar khade ho gaye.

Dhaumya ka mantra

Rishi Dhaumya ne
mantron se Rakshasa ka moh tod diya.
Rakshasa aur bhi gusse mein aa gaya.

Yudhishthira ka prashn

Yudhishthira bole:
“Tum kaun ho?
Kya chahte ho humse?”

Kirmira ka parichay

Rakshasa hansa:
“Main Kirmira hoon.
Vaka ka bhai.

Bhima ne mere bhai ko mara.
Aaj main badla loonga.
Bhima ko yahin kha jaunga!”

Bhima aage badhe

Bhima ne
ek bada ped ukhaad liya 🌳
Arjuna ne Gandiva chadha diya,
par Bhima bole—
“Isse main hi nipatunga.”

Bhayankar yuddh

Ped aur pathar ude.
Aag ke shole pheinke gaye.
Jungle tootne laga.

Dono ek–dusre se
haath–paon se bhid gaye.
Do gusse wale saand jaise!

Bhima ka krodh

Bhima ko yaad aaya
Draupadi ka apmaan.
Unhone poori taakat jod li.

Rakshasa ko pakda.
Zameen par patka.
Ghuma–ghuma kar thaka diya.

Phir seene par ghutna rakha
aur gardan daba di.

Antim shabd

Bhima bole:
“Ab tu Yama ke lok jaa!”

Aur
Kirmira mar gaya.

Shanti ka samay

Jungle shant ho gaya 🌙
Pandav surakshit ho gaye.
Draupadi ne chain ki saans li.

Sab ne Bhima ki veerta ki prashansa ki.
Phir Pandav aage badh gaye,
Krishna ko aage rakh kar.

Moral 🌱

Anyay ka ant hota hai

Raksha ke liye shakti ka upyog dharm hai

Bhakti aur sahas saath ho
toh bhay tik nahi pata"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.3  Arjunabhigamana Parva (Arjunas Journey)"):

        # --------------------------------------------------
        # Section 3.3.1
        # --------------------------------------------------
        with st.expander("Section 3.3.1  Section XII"):
            text1 = """ 
            Pandav van mein

Jab Pandav vanvaas mein the,
unke apne log unse milne aaye.

Bhoj, Vrishni, Andhak,
Panchal ke rishte-daar,
aur Chedi ke raja bhi aaye.

Sabka ek hi sawaal tha:
“Ab anyay ka kya jawab hoga?”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Krishna ka krodh

Krishna bole:
“Duryodhana, Karna, Dushasana, Shakuni—
sab ka ant nishchit hai.

Dharm yahi kehta hai:
anyayi ka vinash zaroori hai.”

Krishna ka roop agni jaisa ho gaya.
Laga jaise sab kuch bhasm kar denge.

Arjuna ka shant stavan

Tab Arjuna aage aaye.
Unhone Krishna ki mahima gaayi.

“Tum hi Vishnu ho.
Tum hi srishti ke aarambh aur ant ho.

Tumne hazaron yugo mein
asuron ka vinash kiya.
Tum hi Narayana ho.”

Arjuna ke shabd sun kar
Krishna shaant ho gaye.

Krishna bole:
“Tum Nara ho,
aur main Narayana.
Hum alag nahi.”

Draupadi ka dard

Tab Draupadi aage aayi.
Aankhon mein aansu.
Dil mein agni.

“Krishna,
mujhe sabha mein ghasita gaya.
Sab ke saamne mera apmaan hua.

Mere pati chup rahe.
Mera vastra kheencha gaya.
Aur Duryodhana hansa.”

Uski awaaz kaanp rahi thi.
Yaadein phir zinda ho gayi.

Purane paap yaad aaye

Draupadi boli:
“Yahi Duryodhana hai
jisne Bhima ko zeher diya.
Jisne ghar jalwaya.

Fir bhi aaj zinda hai!”

Wo ro padi.
Haath se chehra dhak liya.

Krishna ka vachan

Krishna ne shant par dridh awaaz mein kaha:
“Draupadi, mat ro.

Jinke pati tumse bair rakhte hain,
unki patniyaan bhi royengi.

Main pratigya karta hoon:
Tum phir se rani banogi.

Aakash gir jaaye,
pahaad toot jaaye,
par mere vachan jhoothe nahi honge.”

Veeron ka sankalp

Arjuna bole:
“Krishna ka vachan atal hai.”

Dhrishtadyumna ne kaha:
“Drona marega.
Bhishma girega.
Duryodhana aur Karna ka ant hoga.”

Sab veer Krishna ki taraf dekhne lage.
Yuddh ka beej boyaa ja chuka tha.

Moral 🌱

Anyay chup rehne se badhta hai

Dharma ka saath dena hi veerta hai

Krishna ka vachan = satya + nyay"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.2
        # --------------------------------------------------
        with st.expander("Section 3.3.2  Section XIII"):
            text1 = """ 
            Krishna ka dukh

Krishna bole:
“Hey prithvi ke raja,
agar main us samay Dwarka mein hota,
to yeh anarth kabhi na hota.”

Unki awaaz mein pashchataap tha.
Dil bhara hua tha."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Jua hota hi nahi

Krishna bole:
“Chahe mujhe bulaya jaata ya nahi,
main sabha mein aa jata.

Main Dhritarashtra, Duryodhana,
aur sab Kauravon ko rokta.”

Bhishma, Drona, Kripa, Vahlika—
sab ko saath le leta.

Dice ke bhayanak parinaam

Krishna ne kaha:
“Jua ek din mein
sab kuch chheen leta hai.

Dhan, maryada, shanti—
sab nash kar deta hai.”

Wo bole:
“Shastra kehte hain—
chaar cheezein vinaash laati hain:

Jua

Stri ka andha moh

Shikar

Madira”

Jo inmein phans jaata hai,
wo apna hi dushman ban jaata hai.

Dhritarashtra ko chetavani

Krishna bole:
“Main Dhritarashtra se kehta:
‘Apne putron ko jua se door rakho.’

Ek galat khel
poore vansh ko jala deta hai.”

Agar wo baat maan lete,
to Kuru vansh bach jaata.
Aur dharma bhi surakshit rehta.

Zarurat padti to bal prayog

Krishna ne dridh swar mein kaha:
“Aur agar meri baat na maante,
to main bal se bhi rok deta.

Jo jhoothe mitra the,
jo jua badha rahe the—
un sab ko main wahi samaapt kar deta.”

Unki aankhon mein kshama nahi,
sirf nyay tha.

Der se mili khabar

Krishna bole:
“Mujhe Dwarka pahunch kar
Yuyudhana se sab pata chala.

Jab suna ki tum vanvaas mein ho,
mera hriday kaanp gaya.”

Isliye bina der kiye,
wo seedhe yahan aa gaye.

Pandavon ki dasha

Krishna ne dekha:
Yudhishthira,
Bhima, Arjuna, Nakul, Sahadev—
sab kasht mein the.

Krishna bole:
“Alas!
Pandavon par kitna bada dukh aa pada hai.”

Unki aankhon mein karuna thi.
Aur saath hi nyay ka sankalp.

Moral 🌱

Jua sirf khel nahi, vinaash hai

Galat nirnay poore vansh ko gira dete hain

Krishna ka shok = dharma ka dard"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.3
        # --------------------------------------------------
        with st.expander("Section 3.3.3  Section XIV"):
            text1 = """ 
            Yudhishthira ka sawaal

Yudhishthira bole:
“O Krishna,
aap us samay Dwarka mein kyun nahi the?
Aap kahan gaye the?
Aur kya kar rahe the?”

Unka sawal shaant tha,
par dil bhara hua tha."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Krishna ka uttar

Krishna bole:
“O Bharata-vansh ke shreshtha,
main Saubha nagar ke raja Salva ko samaapt karne gaya tha.”

Ye zaroori tha.
Dharma ke liye zaroori.

Shishupala ka badla

Krishna bole:
“Tumhare Rājasūya yajna mein
maine Shishupala ka vadh kiya tha.

Wo krodh mein andha ho gaya tha.
Mujhe pratham pooja milte dekh
wo apmaan se jal utha.”

Usi krodh ka badla tha Salva.

Dwarka par hamla

Krishna bole:
“Jab main yahan tha,
Salva ne khali Dwarka par aakraman kar diya.

Uska vimaan Saubha
sone–chandi se bana tha.
Aakash mein kahin bhi ja sakta tha.”

Usne Vrishni yuvaon se yuddh kiya.
Kai veer mare gaye.
Udyan aur nagar ujhad gaye.

Salva ka ghamand

Salva chillaya:
“Vasudeva kahan hai?
Kansa aur Kesi ke vadh ka ghamand karta hai!

Main usse maar kar hi lautunga.
Yahi meri pratigya hai!”

Wo baar-baar mera naam le kar
aakash mein ghoomta raha.

Krishna ka sankalp

Krishna bole:
“Jab mujhe ye sab pata chala,
mera hriday krodh se bhar gaya.

Anartta desh par atyachar,
mera apmaan,
aur uska ghamand—
sab kuch dekh kar
maine nishchay kar liya.”

Salva ka vinash hona hi tha.

Antim yuddh

Krishna bole:
“Main samudra ke beech
ek dweep par usse mila.

Maine apna Panchajanya shankh bajaya
aur yuddh ka ahvaan kiya.”

Kai Danav aaye.
Sab dhool chaat gaye.

Isi yuddh ke kaaran
main us samay tumhare paas
nahi aa saka.

Ant mein

Krishna bole:
“Jaise hi mujhe pata chala
ki Hastinapur mein jua hua,
aur tum vanvaas mein ho—
main turant yahan aa gaya.”

Unki awaaz mein spasht tha:
“Tumhara dukh mera dukh hai.”

Moral 🌿

Dharma ke liye kabhi-kabhi door jaana padta hai

Krishna ki anupasthiti laaparwahi nahi, kartavya thi

Ant mein Bhagwan bhakt ke paas zaroor aate hain"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.4
        # --------------------------------------------------
        with st.expander("Section 3.3.4  Section XV"):
            text1 = """ 
            Yudhishthira ka prashn

Yudhishthira bole:
“O balshali Vasudeva,
Saubha ke raja Salva ka ant kaise hua,
yeh vistaar se batao.

Abhi meri jigyāsa poori nahi hui.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Krishna bolna shuru karte hain

Krishna bole:
“O Pandu-putra,
jab maine Shishupala ka vadh kiya,
tab uska mitra Salva krodh se jal utha.

Badla lene ke liye
wo seedha Dwarka aa gaya.”

Dwarka ka gherav

Salva ne apni sena ko
charo taraf phaila diya.

Wo sirf zameen par nahi,
aakash se bhi yuddh kar raha tha.

Har disha se
teer, shastra aur agni barsne lage.

Yuddh shuru ho chuka tha.

Dwarka ki majboot taiyaari

Krishna bole:
“O Bharata-shreshtha,
Dwarka pehle se hi
shastra-vidya ke niyamon se bani hui nagari thi.”

Nagari mein tha:

unche prakar aur burj

majboot darwaaze

agni-fenkne wali yantra

pathron aur garam dravya ko phenknay wale upkaran

bhari shields, bhale, talwaren

sadkon par kaante aur lakdi ke avrodh

Har jagah taiyaari thi.

Veer rakshak

Nagari ki raksha kar rahe the:

Gada

Shamva

Uddhava

aur kai parikshit yoddha

Sab veer the.
Sab anubhavshali.

Rath, ghode aur hathi
sadkon par tayaar khade the.

Sanyam aur satarkta

Krishna bole:
“Ugrasena aur Uddhava ne
nagari mein ghoshna kar di—

❝Koi bhi madira ka sevan nahi karega❞”

Sab Vrishni aur Andhak jaante the:
agar laparwahi hui,
to Salva daya nahi karega.

Isliye:

sab sober rahe

sab satark rahe

Suraksha ke kathor niyam

Nagari se:

nritya, gaayan, tamasha band

nadiyon ke pul tod diye gaye

naav chalana mana

khayi ke neeche nokile baans lagaye gaye

Nagari ke aas-paas:

zameen ko khod kar
gaddhe aur jaal bichhaye gaye

aag lagane wale padarth chhupa diye gaye

Koi bina pehchaan ke
andar–bahar nahi ja sakta tha.

Dwarka – Indra ki nagari jaisi

Krishna bole:
“In sab taiyariyon ke kaaran
Dwarka aur bhi majboot ho gayi.

Wo Indrapuri jaisi lag rahi thi.”

Yoddhaon ko:

sona (gold)

bhojan

vastra

shastra

sab kuch mila.
Koi bhi aprasann nahi tha.

Ant mein

Krishna bole:
“Is tarah,
Ahuka (Ugrasena) ke netritva mein
Dwarka poori tarah surakshit thi.”

Salva ka ghamand
ab zyada der tak tikne wala nahi tha.

Moral 🌿

Dharma sirf shakti se nahi, sanyam se jeet ta hai

Sahi taiyaari bina ghabrahat ke raksha karti hai

Jahan anushasan hota hai, wahan adharma haar jata hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.5
        # --------------------------------------------------
        with st.expander("Section 3.3.5  Section XVI"):
            text1 = """ 
            Vasudeva bole—

“Hey rājā,
Saubha ka swami Śālva
bahut badi sena le kar
Dvārakā ki taraf aaya.

Paidal sainik.
Ghode.
Haathi.
Sab kuch tha uske paas.

Uski sena ne
paani ke paas wali
samatal bhoomi gher li."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Mandir, shamshān,
dev-vriksh,
aur pavitra sthaan
chhod kar
baaki sab jagah
unhone kabza kar liya.

Shehar ki sadkein band ho gayin.
Gupt raaste bhi rok diye gaye.

Garuḍ ki tarah
Śālva apni udti hui
Saubha-nagri par
tezi se aage badha.

Uski sena
achhi tarah poshit thi.
Achhe shastra the.
Jhande lehra rahe the.
Veer lag rahe the.

Yeh dekh kar
Vrishni vansh ke
yuvrajon ka khoon
garam ho gaya.

Unhone tay kiya—
‘Hum shehar se bahar nikal kar
samna karenge.’

Cārudeṣṇa, Sāmba aur Pradyumna
apne rathon par chadhe.

Kavach pehne.
Gehne sajaye.
Aur seedhe yuddh-bhoomi ki taraf badhe.

Sāmba ne sabse pehle
Śālva ke senapati
Kṣemavṛddhi par
baan barsaye.

Baan itne ghanay the
jaise Indra ki varsha.

Par Kṣemavṛddhi
Himālaya ki tarah
achal raha.

Usne māyā se bhare
teekhe baan chhode.

Sāmba ne bhi
chāl se kaam liya.
Us māyā ko
māyā se hi kaat diya.

Hazāron baan
senapati ke rath par bars gaye.

Ant mein
Kṣemavṛddhi
ghode ke sahare
yuddh-bhoomi chhod kar bhag gaya.

Tab ek bhayankar
Daitya Vegavān
Sāmba par toot pada.

Sāmba zara bhi nahi hila.

Usne ghoomti hui
gada uthai
aur zor se phenki.

Gada lagte hi
Vegavān dharti par gira—
jaise purana ped
jhad kar gir jata hai.

Sāmba bina dare
sena ke beech ghus gaya
aur sabse ladne laga.

Dusri taraf
ek aur Daitya Vivindhya
Cārudeṣṇa se bhid gaya.

Unka yuddh
sheron ki takkar jaisa tha.

Garaj.
Tez baan.
Koi peeche nahi hata.

Tab Rukmini ke putra
ne ek divya astra uthaya.

Mantron se jagaya.
Aankhon mein agni thi.

Us astra ke lagte hi
Vivindhya dharti par gir pada.
Nishchit.
Nishprāṇ.

Yeh dekh kar
Śālva phir aage badha.

Uski udti hui Saubha-nagri
dekh kar
Dvārakā ke yoddha
ek pal ke liye ghabra gaye.

Tab Pradyumna aage aaye.

Unki awaaz shaant thi
par hriday dridh.

Unhone kaha—

“Ghabrao mat.
Yahin ruko.
Mujhe ladne do.

Aaj main
is Saubha ko
aur Śālva ko
dono ko rokunga.

Mere baan
saanpon jaise honge.
Is sena ko
aaj yahin samaapt karunga.

Nidar raho.
Aaj Saubha ka ant hoga.”

Pradyumna ke shabdon se
Yādav sena ka mann
phir majboot ho gaya.

Sabke chehron par
hosla aa gaya.

Aur phir
yuddh dobara
poore bal ke saath
shuru ho gaya ⚔️

Is kahani ka bhāv 🌿

Jab apna ghar khatre mein ho,
to veer peeche nahi hat-te

Sachcha sahas
shant vaani se bhi dikhta hai

Ek dridh hriday
poori sena ko majboot bana deta hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.6
        # --------------------------------------------------
        with st.expander("Section 3.3.6  Section XVII"):
            text1 = """ 
            Vasudeva bole—

“Hey Bharata-vansh ke shreshṭh veer,
yeh keh kar
Rukmiṇī ka putra Pradyumna
apne sunehre rath par chadh gaya.

Uska rath
shreshṭh ghodon se jhuta tha.
Ghode kavach pehne hue the.

Rath par
Makara-dhvaja tha—
khula hua muh,
bhayanak,
jaise mrityu khud khadi ho."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Ghode
zamin par daud nahi rahe the,
jaise hawa mein ud rahe hon.

Pradyumna ne
tarakash sambhala.
Talvaar saath thi.
Ungliyon par chamda chadha tha.

Usne bijli jaise chamakte
dhanush ko zor se taana.

Kabhi daayein haath se,
kabhi baayein haath se—
jaise shatru ki
koi parvah hi na ho.

Danav aur Saubha ke yoddha
ghabra gaye.
Unki panktiyaan
tootne lagi.

Pradyumna lagataar
baan barsata raha.

Do baanon ke beech
ek pal ka bhi antar nahi.

Uske chehre ka rang
badla nahi.
Sharir zara bhi
kaanpa nahi.

Bas
uski garajti hui
sinh-naad
sunai deti rahi.

Makara-dhvaja
Salva ke sainikon ke
hriday mein
bhay bhar raha tha.

Phir Pradyumna
seedha Śālva ki taraf badha.

Is chunauti ko
Śālva sah nahi paaya.

Krodh se andha hokar
woh apne sundar rath se
neeche utar aaya.

Donon ka yuddh
aisa tha
jaise Indra aur Bali
saamne aa gaye hon.

Śālva ne
apne rath par chadh kar
teekhe baan chhode.

Pradyumna ne bhi
baanon ki baarish kar di.

Aakash bhar gaya.
Zameen kaanp uthi.

Śālva ne
agni jaise jalte astra chhode.
Par Pradyumna ne
sab ko kaat diya.

Tab Pradyumna ne
ek vishesh baan chhoda.

Woh baan
kavach ko cheerta hua
Śālva ke hriday mein ghus gaya.

Śālva
achanak behosh hokar
gir pada.

Yeh dekh kar
Danav sena bhag uthi.
Dharti unke bhaagti kadmon se
kampne lagi.

Har taraf se
“Haay! Alas!”
ki awaaz ghoonj uthi.

Par kuch hi palon baad
Śālva ne
hosh sambhala.

Usne phir se
baan chhodne shuru kiye.

Is baar
Pradyumna ke gale ke paas
gehra ghav laga.

Pradyumna
kamzor padne laga.

Śālva ne
sinh ki tarah garaj kar
poori prithvi ko
kaampa diya.

Aur bina ruke
aur bhi baan chhodta raha.

Ant mein—
baanon se chhinn-bhinn,
chetnā-rahit,
Pradyumna yuddh-bhoomi par
nishchal ho gaya.

Is drishya ka bhāv 🌑

Veerta ka matlab sirf jeetna nahi,
ant tak dat kar khade rehna bhi hota hai

Kabhi-kabhi sabse mahaan yoddha bhi
girta hai—
par uska sahas amar rehta hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.7
        # --------------------------------------------------
        with st.expander("Section 3.3.7  Section XVIII"):
            text1 = """ 
            Vasudeva bole—

“Hey rājā,
jab Śālva ke baanon se chhalni hokar
Pradyumna behosh ho gaya,
toh Vr̥ṣṇi yoddhāon ke mann toot gaye.

Har taraf se
‘Haay!’ ‘Alas!’
ki dhvani uthne lagi.

Dushman prasann ho gaye.

Tab Daruka ka putra,
jo Pradyumna ka sārathi tha,
usse turant
yuddh-bhoomi se
door le gaya."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Rath zyada door nahi gaya tha
ki Pradyumna ko chetnā laut aayi.

Usne dhanush uthaya
aur kathor svar mein bola—

“Hey Sūta-putra!
Yeh tumne kya kiya?
Yuddh-bhoomi chhod kar
rath kyun mod diya?

Kya Śālva ko dekh kar
tum ghabra gaye?
Ya tumhara mann toot gaya?
Sach-sach batao!”

Sārathi ne vinamrta se uttar diya—

“Hey Janārdan-putra,
na mujhe bhay hua,
na main bhramit hua.

Par mujhe laga
Śālva tumse bhi adhik balshāli hai.

Sārathi ka kartavya hai
jab veer behosh ho jaaye
toh uski rakṣā kare.

Tum akela ho,
aur Danav anek hain.
Isi liye
main tumhe bacha kar le ja raha hoon.”

Yeh sun kar
Makara-dhvaja-dhārī Pradyumna
tej se bola—

“Rath ghumao, Daruka-putra!
Aur yaad rakhna—
jab tak main jeevit hoon,
yuddh se kabhi peeth nahi pherni!

Vr̥ṣṇi-putra woh nahi
jo yuddh chhod de,
ya gir chuke shatru ko maare,
ya strī, balak, vriddh par vaar kare.

Tum Vr̥ṣṇi-riti jaante ho!
Phir yeh palayan kyun?”

Phir Pradyumna ke shabd
aur bhi kathor ho gaye—

“Mādhava kya kahenge
jab unhe pata chale
ki main peeth dikha kar bhaga?

Baladeva kya kahenge?
Sātyaki, Śāmba, Gada, Cārudeṣṇa
kya sochenge?

Aur Vr̥ṣṇi-veero ki patniyaan?

Kya woh nahi kahengi—
‘Yeh Pradyumna to kायर nikla!’

Lajja mere liye mrityu se bhi bhayankar hai!”

Pradyumna ki aankhon mein
aag thi,
par mann mein maryādā.

“Hari mujhe yahan chhod kar
Yudhiṣṭhira ke yajña mein gaye hain.

Main yahan chup kaise baith sakta hoon?

Kritavarman ko maine roka tha—
‘Tum ruko, Śālva se main ladunga.’

Ab yuddh chhod kar
main uska saamna kaise karunga?”

Uski aawaaz kampit thi,
par sankalp atal—

“Agar peeth par ghaav lekar
yahan se jeeta raha,
toh main jee hi nahi paunga!

Hey Daruka-putra,
rath ghumao!

Yuddh se bhaag kar jeevan
mere liye jeevan nahi.”

Is drishya ka saar ⚔️

Veer ke liye pratiṣṭhā prāṇ se bhi upar hoti hai

Yuddh sirf jeet-haar nahi,
maryādā aur aatma-samman ka parikshan hota hai

Pradyumna gir kar bhi veer hi raha,
kyunki usne bhay ko nahi,
dharma ko chuna"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.8
        # --------------------------------------------------
        with st.expander("Section 3.3.8  Section XIX"):
            text1 = """ 
            Vasudeva bole—

Pradyumna ke kathor shabd sun kar,
Daruka ke putra ne turant,
shaant par dridh svar mein kaha—

“Hey Rukmiṇī-putra,
main yuddh se nahi darta.

Vr̥ṣṇi-riti mujhe bhali-bhaanti aati hai.

Par sārathi ko sikhaya jata hai—
veer behosh ho jaaye,
toh pehle uski rakṣā!

Tum Śālva ke baanon se
bahut ghaayal ho chuke the.
Isliye main rath mod kar le gaya.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Phir usne gaurav se kaha—

“Ab tum poori tarah sachet ho.

Hey Keśava-putra,
ab meri sārathi-kala dekho!

Main Daruka ka putra hoon.
Mujhe poori shikṣā mili hai.

Ab main bina bhay
Śālva ke vyuh mein ghusunga!”

Yeh keh kar,
sārathi ne lagam kheench li.

Ghode bijli jaise daud pade.

Kabhi daayein,
kabhi baayein,
kabhi ghoomte hue,
kabhi seedhe—
aise lag raha tha
jaise zameen ko chhoo hi nahi rahe.

Daruka-putra ke haath
itne halke aur nishchit the
ki ghode bhi uski ichchha samajh gaye.

Pradyumna ne
Śālva ki sena ke chaaro taraf
rath ghumaya.

Yeh drishya dekh kar
sab yoddhā
vismit reh gaye.

Yeh dekh kar
Śālva kruddh ho utha.

Usne teen teekhe baan
sārathi par chhod diye.

Par Daruka-putra ne
unhe maano dekha hi nahi.

Rath apni gati mein bana raha.

Phir Śālva ne
Pradyumna par
har prakaar ke astra barsa diye.

Par Rukmiṇī-putra muskuraya.

Apni adbhut phurti se
usne sab astra
beech mein hi kaat diye.

Ab Śālva ne
Asur-māyā ka sahara liya.

Teer, teer, aur teer—
andhakaar sa chha gaya.

Tab Pradyumna ne
Brahmāstra ka prayog kiya.

Asuri astra
akash mein hi tukdon mein toot gaye.

Uske baad
Pradyumna ke baan
Śālva ke
sir, vaksh aur mukh mein lage.

Śālva behosh hokar
gir pada.

Sab taraf
“Haay! Alas!”
ki dhvani goonj uthi.

Pradyumna ne
ek aur bhayankar baan
dhanush par chadha diya.

Woh baan
aag jaisa chamak raha tha,
aur vishakt sarp jaise
mrityu lekar aa raha tha.

Tab Indra, Kubera
aur devtāon ne
Nārada aur Vāyu-dev ko bheja.

Unhone Pradyumna se kaha—

“Hey veer,
yeh baan wapas le lo.

Śālva tumhare haathon nahi marega.

Uska ant
Devakī-putra Śrī Kṛṣṇa ke haathon
likha hai.

Vidhi ko jhootha mat hone do.”

Yeh sun kar
Pradyumna prasann hua.

Usne shreshṭh baan
wapas tarkash mein rakh diya.

Ghaayal,
mann se toota hua Śālva
uth khada hua.

Apne chamakdar
Saubha-rath par chadha
aur aakash mein uḍ gaya.

Dvārikā se
bhaag nikla.

Is khand ka saar ⚔️

Sārathi aur veer ka rishta
kartavya aur vishvaas par tikta hai

Veer ka kaushal
jab maryādā se jud jaaye
toh vidhi bhi bol uthti hai

Pradyumna jeet sakta tha,
par vidhi ka aadesh maanne mein
bhi veerta hoti hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.9
        # --------------------------------------------------
        with st.expander("Section 3.3.9  Section XX"):
            text1 = """ 
            Vasudeva bole—

Jab Śālva Anartta-nagar chhod kar chala gaya,
tab, hey rājā,
tumhare Rājasūya yajña ke baad
main Dvārakā laut aaya.

Par jo dekha,
mera hriday bhar aaya।"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Nagar ki chamak bujh chuki thi.
Na Vedón ka swar,
na yajñón ki aahuti.

Sundar striyaan
abhooshan thi.
Udyān soone the.
Har chehre par chinta aur shok.

Main ghabra gaya.
Aur Hṛdik-putra Kritavarman se poocha—

“Hey veer,
Vr̥ṣṇi-nagar itna dukhi kyun hai?”

Usne mujhe
Śālva ka akraman
aur uski udaan
sab kuchh bata diya.

Sab sun kar
mera nishchay pakka ho gaya—

Śālva ka ant nishchit hai.

Main nagar ke veeron se bola—

“Hey Yādav-shreshṭho!
Tum nagar ki rakṣā karo.

Main Śālva ko maar kar hi lautunga.

Saubha-rath ke saath
uska vinaash karunga.

Dundubhi bajao—
shatru ke hriday kaanp jaaye!”

Sab veeron ne kaha—
“Jaao, vijay paao!”

Brāhmaṇon ke aashirvaad ke saath,
Śiva ko naman karke,
main apne rath par chadha.

Saivya aur Sugrīva
ghode jute hue the.

Main Pañcajanya shankh phoonka—
akash goonj utha.

Chaaron prakaar ki sena ke saath
main nikal pada.

Desh, parvat, nadiyaan
peeche chhoot ti gayi.

Ant mein
Mātrikāvarta pahucha.

Wahin suna—
Śālva apne chamakdar Saubha-rath par
samudra ke paas ghoom raha hai.

Main uske peeche gaya.

Samudra ke beech,
lahron ke upar,
uska rath akash mein tha.

Door se dekh kar
usne mujhe lalkaara.

Maine baan chhode—
par rath bahut door tha.

Mera krodh badha.

Śālva ne
hazaaron teer barsa diye.

Mere sainikon,
mere ghodon,
mere sārathi Daruka—
sab par teer.

Pal bhar ko
mujhe kuchh dikhai nahi diya.

Par maine dhairya nahi chhoda.

Mantron se bhare
hazaaron teer
maine bhi chhode.

Saubha-rath
itna upar tha
ki meri sena
sirf dekh sakti thi—

Par ve garaj kar utsaah badha rahe the.

Mere teer
Danavon ke sharir mein
keenon jaise ghus rahe the.

Ghaayal Danav
samudra mein gir rahe the.
Jal-jantu unhe nigal rahe the.

Tab maine
Pañcajanya zor se phoonka.

Shankh-naad ne
dishaon ko kaanpa diya.

Śālva ne dekha—
uski sena gir rahi hai.

Tab usne
Asuri māyā ka sahara liya.

Gada, hal, shakti,
talvaar, parshu,
aag jaise teer—
sab meri taraf.

Par main shaant raha.

Prati-māyā se
maine sab nasht kar diya.

Phir Śālva ne
parvat-shikhar phenkne shuru kiye.

Akash ajeeb ho gaya.

Kabhi andhera,
kabhi roshni.
Kabhi garmi,
kabhi thand.

Angaar, raakh,
astra—
sab baras rahe the.

Maine samajh liya—
yeh sab māyā hai.

Aur samay aane par
maine Prāgṇāstra chhoda.

Woh māyā
rooi ke reshon jaise
ud kar mit gayi.

Fir prakash lauta.

Yuddh fir se shuru hua.

Aur main
Śālva ke saamne
dridh aur sthir khada raha.

Is khand ka saar ⚔️

Bhagavān ka krodh bhi
niyantrit aur maryādit hota hai

Asuri māyā
divya buddhi ke aage tik nahi paati

Jab dharm yuddh ho,
tab akash, jal, aur agni
bhi sakshi ban jaate hain"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.10
        # --------------------------------------------------
        with st.expander("Section 3.3.10  Section XXI"):
            text1 = """ 
            Vasudeva bole—

Hey rājā,
jab Śālva mere saath yuddh karta hua
phir se akash mein utha,
toh us dusht ne
jeet ki lalasa mein
bhayankar astron ki baarish kar di."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Sataghnī,
bhari gadayen,
jalti hui shaktiyaan,
aur bhayanak mudgar—
sab akash se meri taraf aaye.

Par main shaant raha.

Mere tez baan
un sab ko
aane se pehle hi
do–teen tukdon mein kaat dete.

Aakash mein
bhayankar garjana hui.

Śālva ne
mere sārathi Daruka,
mere ghodon,
aur mere rath par
hundreds teer barsa diye.

Tab Daruka,
thartharate swar mein bola—

“Prabhu…
kartavya ke kaaran
main ab tak khada hoon…
par ab sharir
bilkul shaktihin ho gaya hai…”

Maine dekha—

Daruka ka sharir
teeron se bhara tha.
Sir, seena, haath—
kahin bhi ek jagah
khaali nahi thi.

Khoon beh raha tha.
Woh laal mitti ke pahad
jaise lag raha tha.

Us pal
maine use dhairya diya.

Tabhi achanak
Dvārakā ka ek vyakti
mere rath ke paas aaya.

Woh Ahuka ka sevak
lag raha tha.

Uski awaaz
dukh se bhari thi.

Usne kaha—

“Hey Keśava…
tumhare pitā ke mitra Ahuka ka sandesh hai…

Tumhari anupasthiti mein
Śālva ne Dvārakā par aakraman karke
Vasudeva ko maar diya hai!

Ab yuddh vyarth hai.
Janārdana, laut chalo.
Dvārakā ki rakṣā hi
tumhara mukhya kartavya hai…”

Yeh sunkar
mera hriday bhaari ho gaya.

Main samajh nahi paaya—
kya karoon,
kya na karoon.

Mera mann
Baladeva,
Sātyaki,
Pradyumna,
sab par chala gaya.

“Kya ve sab bhi…?”
“Kya pitā… sach mein…?”

Maine socha—

Jab Baladeva jaise veer jeevit ho,
toh Vasudeva ka vadh kaise?

Par phir mann ne kaha—
shayad sab nasht ho chuke hain.

Is soch ne
mujhe shok-sāgar mein daal diya.

Isi dukh ke saath
main phir Śālva ka saamna karne laga.

Tabhi, hey rājā—
maine dekha—

Mera pitā Vasudeva
Saubha-rath se
gir rahe hain!

Unka mukut bikhar gaya.
Vastra ast-vyast.
Sharir neeche ja raha tha—

Bilkul aisa
jaise Yayāti swarg se gir raha ho.

Yeh dekh kar
mere haath se Śārṅga dhanush
chhoot gaya.

Meri aankhon ke saamne
andhera chha gaya.

Main murchhit ho gaya.

Rath ke kinare
baith gaya.

Sena cheekh uthi—

“Haay! Haay!”

Pitā
pakshi jaise
neeche girte dikh rahe the.

Shatru veeron ne
un par astr chalaye.

Mera hriday kaanp gaya.

Par agle hi pal—

meri chetna lauti.

Maine dekha—

Na Saubha-rath.
Na Śālva.
Na pitā.

Tab mujhe spasht ho gaya—

👉 Yeh sab Māyā hai.
👉 Asuri bhram.

Main poori tarah
sambhal gaya.

Aur phir—

sau-sau teer
maine dobara chhode.

Iss baar
poore bodh ke saath.

Is khand ka saar 🌑➡️🌕

Asur yuddh mein bhavnatmak bhram bhi laate hain

Bhagavān bhi līlā mein mānush-bhaav dikhate hain

Par vivek jagte hi māyā toot jaati hai

Dharm-yoddhā ka bal
buddhi + sthirata se aata hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.11
        # --------------------------------------------------
        with st.expander("Section 3.3.11  Section XXII"):
            text1 = """ 
            Vasudeva bole—

Hey Bharata-shreshṭha,
phir maine Śārṅga dhanush uthaya
aur dev-shatru Dānavon ke
sir kaatne laga—
us sone-jaise uḍte rath (Saubha) se.

Mere baan
saap jaise tedhe,
bahut ūnchā jaane wale,
aur bhayanak shakti se bhare the."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Par achanak—
Saubha-rath gaayab ho gaya!
Sirf māyā.

Main vismit reh gaya.

Tab charon taraf se
Dānavon ki
bhayankar cheekh-pukaar gūnj uṭhi.

Maine ek aisa astr chuna
jo sirf dhvani (awaaz) ko pakad kar
shatru ko bhed deta tha.

Jaise hi maine chhoda—

🔇 Shor band.
☀️ Tez baan chamke.

Jo bhi chilaya—
aasmaan mein,
chhupe hue,
adrishya—
sab nasht ho gaye.

Har disha se phir shor—
aur har disha mein
meri pratighaati shakti.

Tab Saubha nagar
phir pragat hua—
is baar Prāgjyotiṣa ke paas.

Aur achanak—
pathron ki baarish!

Itni bhari
ki main,
mere ghode,
saarthi,
rath—
sab pahaad ke neeche dab gaye.

Main
deemak ke teele jaisa
dikhne laga.

Meri sena
ghabra kar bhag uthi.

Aakash, prithvi, antariksh—
sab jagah
“Haay! Haay!”

Mere mitr ro pade.
Shatru prasann ho gaye.

Par tab—
maine Indra ke vajra jaise astr se
saare pathar
choor-choor kar diye!

Mere ghode
lagbhag marne wale the,
kaamp rahe the.

Par jaise hi
main dikha—
sabke chehre par
surya uday jaisi khushi chha gayi.

Tab Daruka bola—

“Prabhu!
Woh raha Śālva—
ab komalta chhod do.

Yeh shatru
shaant upaayon se
jeetne layak nahi.

Isse abhi nasht karo!
Dvārakā ka vidhwansak
mitra nahi ho sakta!”

Main samajh gaya—
yeh satya hai.

Maine kaha—
“Daruka, zara rukna.”

Aur tab—

🔥 divya agni-astr
maine dhanush par chadhaaya.

Phir, krodh aur mantra ke saath—
maine chhoda
apna priya astr:

🟡 Sudarśana Chakra 🟡

Woh doosre surya jaisa
yug-anta ke samaan chamka.

Sudarśana ne
Saubha nagar ko
aise kaata
jaise aara
vriksh ko kaat de.

Tripura ke patan jaisa
Saubha do tukdon mein gira.

Chakra lauta—
maine phir kaha—

“Ab Śālva ke paas jao.”

⚔️ Śālva ka sharir do bhaagon mein kata.
🔥 Shatru jal utha.
😱 Dānav-striyan bhaag uṭhīn.

Maine śaṅkha bajaya—
mitron ke hriday khil uthe.

Saubha
Meru jaise uncha tha—
ab raakh tha.

Dvārakā lautkar
maine apnon ko
anand diya.

Aur isliye—
hey rājā,
main us samay
Hastināpura nahi aa saka.

Agar aata—
toh Suyodhana zinda na rehta,
ya dyūt-kreeda hoti hi nahi.

Par—
bandh toot jaaye,
toh paani kaise roka jaaye?

Antim drishya 🌅

Krishna ne
Pandavon ko pranam kiya.

Yudhiṣṭhira ne
aadar diya.
Bhīma ne
sir soongha.
Arjuna ne
baahon mein bhar liya.

Draupadī
aankhon se poojne lagi.

Subhadrā aur Abhimanyu ke saath
Krishna Dvārakā ke liye nikle.

Aur Kamyaka van mein
Pandav
apni yatra ke liye
tayyar hue.

Is adhyaay ka saar ✨

Māyā ka ant vivek + divya shakti se hota hai

Sudarśana = dharma ka nirṇayak astr

Jab samay nikal jaaye,
toh pachtawa reh jaata hai

Bhagavān bhi kehte hain:
“Ab kya… bandh toot chuka hai.”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.12
        # --------------------------------------------------
        with st.expander("Section 3.3.12  Section XXIII"):
            text1 = """ 
            Krishna ke jaane ke baad,
Yudhishthira, Bhīma, Arjuna,
aur Nakula–Sahadeva
mehngē rathon par chadhe.

Ghode shreshṭh the.
Chehre tej se chamak rahe the.
Par mann bhaari tha."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Chalte waqt,
Pandavon ne Brāhmaṇon ko
sona, vastra aur gaayein daan ki.
Yeh unka dharm tha.

Beech-beech mein
bees yoddhā
hathiyaaron ke saath chal rahe the.

Rajkumāri ke kapde,
gehne,
daaiyan aur sevikaayein—
sab saath thi.

Indrasena
tez rath par
peeche-peeche aaya.

Jab ve aage badhe,
Kurujāṅgala ke nagrik
unke paas aa gaye.

Brāhmaṇon ne
prem se aashirvaad diya.
Yudhishthira ne bhi
vinamr namaskar kiya.

Thodi der
vahaan ruke.

Rāja ne
logon ko aise dekha
jaise pita
apne bachchon ko dekhta hai.

Aur log—
unhe apna pita maan rahe the.

Tab logon ki aankhon mein
aansoo aa gaye.

Sab bole—

“Haay Prabhu!
Haay Dharm!”

“Tum hi hamare rāja ho.
Tum hi hamare rakshak ho.
Phir humein chhodkar
van kyon ja rahe ho?”

“Dhritarāshṭra ka beta nirdayi hai!
Suvala ka beta bhi durbuddhi hai!
Aur Karna—
un sab ka saath dene wala!”

Log bole—

“Tumne Indraprastha basaya.
Swarg jaisa nagar.
Māyā ka banaya hua
adbhut mahal.

Usse chhodkar
kahaan ja rahe ho,
hey Dharm ke putra?”

Unki awaaz
kamp rahi thi.
Dil bhar aaye the.

Tab Arjuna aage aaye.
Unki awaaz sthir thi.

Unhone kaha—

“Vanvaas mein rehkar
rāja
apne shatruon ka
jhootha maan todna chahte hain.

Aap sab—
rishiyon ke paas jaaiye.
Unse ashirvaad maangiye.
Yahi hamare
param hit ka raasta hai.”

Yeh sunkar,
Brāhmaṇ aur nagrik
Pandavon ke chaaron or ghoome.

Sabne namaskar kiya.
Aankhen bhaari thi.

Phir dheere-dheere
apne gharon ki taraf
laut gaye.

Dil bhaari tha.
Par vishvaas bhi tha.

Is drishya ka bhaav 🌿

Rāja sirf shāsak nahi, parivaar hota hai

Dharm ka raasta aksar tyaag maangta hai

Sachchai ke saath chalne wale
akela mehsoos hote hain

Par unke saath
logon ka aashirvaad hota hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.13
        # --------------------------------------------------
        with st.expander("Section 3.3.13  Section XXIV"):
            text1 = """ 
            Yudhishthira—
Kuntī ke dharm-putra,
apne vachan par atal,
bhaiyon se bole:

“Hamein baarah saal
is nirjan van mein rehna hai.
Isliye aisa sthaan dhundo
jo shubh ho, sundar ho—
jahan pakshi, hiran, phal, phool ho,
aur jahan rehna sukhdayak ho.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yeh sunkar Arjuna (Dhananjaya)
raja ko aise naman kiya
jaise guru ko kiya jaata hai,
aur bole:

“Aapne bade-bade rishiyon ki seva ki hai—
Dvaipāyana (Vyāsa), Nārada jaise
maha-yogiyon ke saath sampark raha hai.

Isliye jo aap nirṇay lenge,
wahi hamare liye shubh hoga.

Phir bhi, yahan paas hi
Dvaitavana naam ka pavitra jheel hai—
phoolon se bhara,
pakshiyon se gunjta hua.
Agar aap chahein,
hum yahin apna vanvaas bita sakte hain.”

Yudhishthira ne shant mann se kaha:

“Partha, tumhara vichaar
mujhe bhi uchit lagta hai.
Chalo, Dvaitavana chalte hain.”

🌿 Dvaitavana ka Divya Drishya
5

Pandav
anek Brāhmaṇon aur tapassviyon ke saath
us pavitra van mein pravesh karte hain.

Koi agnihotra karta hai,
koi ved-adhyayan,
koi bhiksha par jeevan,
aur koi vanaprastha jeevan mein sthit.

Van mein dikhta hai—

Śāla, Aam, Kadamba, Madhuka, Arjuna ke vriksh

Mor, Kokil, Chakora ki madhur dhwani

Hathi—parvat jaise,
mad-matt avastha mein

Sarasvatī (Bhogavatī) nadi ke kinare
jata-dhaari rishi, bark ke vastron mein

Yeh van jeevit lagta hai—
tap, shanti aur prakriti ka sangam.

Pandav rathon se utarte hain.
Yudhishthira aise lagte hain
jaise Indra swarg mein pravesh kar raha ho.

Siddh, Chāraṇ,
aur van-nivasi rishi
unke darshan ke liye aate hain.

Sab ek maha-vriksh ke neeche baithte hain—
phoolon aur latāon se jhukta hua.

Paanch maha-dhanurdhar
uske neeche vishraam karte hue
aise lagte hain
jaise paanch hathi parvat ke paas
shant ho kar khade ho.

🌸 Is adhyay ka saar

Vanvaas palayan nahi, saadhana hai

Raja dharm se alag nahi hota,
chahe singhāsan ho ya van

Prakriti bhi
satpurushon ka swaagat karti hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.14
        # --------------------------------------------------
        with st.expander("Section 3.3.14  Section XXV"):
            text1 = """ 
            Vanvaas ke dukh ke baad,
Pandavon ko Dvaitavana ke van mein
antatah ek sukhad nivaas mil gaya.

Yeh van—
Śāla vrikshon se bhara,
Sarasvatī ke jal se pavitra,
jahaan Pandav
Indra ke saman tejashvi lagte hue
shant roop se rehne lage."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            🌿 Yudhishthira ka Dharma

Raja Yudhishthira—
Kuru-vansh ke shreshṭh putra—
van ke Yatiyon, Muniyon aur Brāhmaṇon
ko phal aur kand-mool arpan karke
unhe santusht karne lage.

Unke purohit Dhaumya Ṛṣi,
pitā saman snehi hokar,
Ishti aur Paitreya yagya
niyamit roop se karte rahe.

Vanvaas ka jeevan
sirf kathin nahi,
dharm-may ban gaya.

🌸 Mārkaṇḍeya Ṛṣi ka Aagaman

Isi samay,
ek divya atithi aaye—
MahāṚṣi Mārkaṇḍeya,
jo devon aur manushya-rishiyon
dono dwara vandit the.

Yudhishthira ne
vinamr bhav se unka samman kiya.

Mārkaṇḍeya Ṛṣi ne
Draupadī, Bhīma, Arjuna aur Yudhishthira
ko tapasviyon ke beech dekha—
aur muskuraye.

Yeh dekhkar
Yudhishthira ne poocha:

“Sab rishi mujhe dekhkar dukhi hain,
par aap muskurā kyun rahe hain?”

🔥 Rāma ka Smaran

Mārkaṇḍeya bole:

“Putra, main anand se nahi muskuraya.
Tumhari dasha dekhkar
mujhe Rāma yaad aa gaye.”

Unhone kaha—

Rāma, jo Indra jaise shaktishali the

Jo Yama ke saman nyaypriya the

Jo Namuchi ke vināshak the

Phir bhi,
pitā ke vachan par
van mein rahe.

“Isliye, koi bhi yeh sochkar
adharm na kare—
‘Main shaktishali hoon’.”

📜 Dharm ke Udāharan

Mārkaṇḍeya ne kaha:

Nabhāga, Bhagiratha jaise rājā
satya ke bal par
swarg ko prapt hue

Kāśī–Karuṣa ke rājā
rajya tyag kar bhi
dharm ke maarg par chale

Saptarishi
Vedo ke niyam palan se
aakash mein prakashit hue

Bade-bade hathi bhi
srishti ke niyam ka ulanghan nahi karte

“Jab prakriti bhi niyam maanti hai,
to manushya ko
ghamand kyun?”

🌟 Yudhishthira ke liye Aashvasan

Ant mein Ṛṣi ne kaha:

“Satya, vinamrata aur sadachar mein
tum sab se aage ho.

Yeh vanvaas tumhara
dharm aur tej ko aur nikhaarega.

Samay aane par,
tum apni hi shakti se
Kauravon se apna rajya wapas loge.”

Yeh kehkar,
Mārkaṇḍeya Ṛṣi
Pandavon aur Dhaumya ko naman karke
uttar disha ki or chal pade.

🌼 Is adhyaay ka saar

Vanvaas pariksha hai, dand nahi

Shakti se bada dharm hota hai

Jo satya par tika rahta hai,
samay uska saathi ban jaata hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.15
        # --------------------------------------------------
        with st.expander("Section 3.3.15  Section XXVI"):
            text1 = """ 
            🌿 Section XXVI – Brahmana aur Kshatriya ka Sundar Milan

(Hinglish kahani • simple • moral story tone)

Vaisampayana bole:

Jab Pandu ke putra Yudhishthira Dvaita van mein reh rahe the,
toh woh jungle ek pavitra sthal ban gaya.

Har taraf Brahmanon ka vaas tha.
Van ke beech ka talaab
Vedic mantron ki dhvani se goonj raha tha.

Aisa lagta tha jaise
Brahma-lok ka doosra roop ho."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yajur, Rig aur Sama Ved ke swar
hawaa mein mithaas ghola karte the.
Aur un mantron ke beech
jab Pandav bhaiyon ke dhanush ki tankaar mil jaati,
toh ek adbhut drishya ban jaata.

Yeh tha
Brahmana ki shakti aur Kshatriya ke bal ka sundar sangam.

Ek shaam,
Rishi Vaka uth khade hue.
Yudhishthira Rishiyon ke beech baithe the.

Vaka bole:

“Hey Kuru-shreshtha,
dekho—havan ka samay aa gaya hai.

Tumhari raksha mein
yeh sab tapasvi Brahmana
agni ko prajwalit karke
dharma ke kaam kar rahe hain.”

“Bhrigu, Angiras, Vashishta, Kashyapa,
Agastya aur Atri ke vanshaj—
sab yahin ek saath hain.

Poore jagat ke shreshtha Brahmana
tumhare saath jud gaye hain.”

Phir Rishi Vaka ne gambhir swar mein kaha:

“Jaise tez hawa ke saath
aag poore jungle ko jala sakti hai,
waise hi jab
Brahmana ki tejas aur Kshatriya ka bal milta hai,
toh koi shatru tik nahi sakta.”

“Hey putra,
jo raja is lok aur parlok par vijay chahta hai,
use kabhi Brahmanon ke bina nahi rehna chahiye.”

“Brahmana raja ko
dharma aur neeti sikhata hai.
Aur raja us gyaan se
shatruon ka vinash karta hai.”

“Raja Bali ko hi dekh lo.
Usne Brahmanon ka aadar kiya.
Isliye uski sampatti kabhi khatam nahi hui.”

“Par jaise hi usne
Brahmanon ke saath anyaay kiya,
uska patan ho gaya.”

“Bina Brahmana ke raja
us haathi jaisa hai
jiske paas mahavat na ho.

Uska bal dheere-dheere khatam ho jaata hai.”

“Brahmana ki drishti adbhut hoti hai.
Kshatriya ka bal bhi anokha hota hai.

Jab dono ek saath hote hain,
toh poori dharti khud jhuk jaati hai.”

“Isliye, Yudhishthira,
jo tumhare paas nahi hai, use paane ke liye,
jo hai use badhaane ke liye,
aur jo hai use sahi jagah daan karne ke liye—

ek gyaani, anubhavī Brahmana
hamesha apne paas rakho.”

“Tum hamesha Brahmanon ka samman karte aaye ho.
Isi liye tumhara yash
teenon lokon mein fail raha hai.”

Vaisampayana aage bole:

Yeh sun kar
sabhi Brahmana prasann ho gaye.
Unhone Rishi Vaka ka bhi samman kiya
aur Yudhishthira par garv mehsoos kiya.

Vyasa, Narada, Jamadagni
aur anek maha-rishi
Yudhishthira ki pooja karne lage—

bilkul waise hi
jaise swarg mein Rishi
Indra ka vandan karte hain.

🌼 Kahani ka Saar (Moral):

Brahmana = gyaan aur drishti

Kshatriya = bal aur raksha

Dono alag ho jaayein toh shakti adhoori

Dono mil jaayein toh dharti bhi jhuk jaati hai

Sachcha raja wahi hai jo gyaan ka samman kare"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.16
        # --------------------------------------------------
        with st.expander("Section 3.3.16  Section XXVII"):
            text1 = """ 
            🌿 Section XXVII – Draupadī ka Dukh aur Yudhishthira ka Dhairya

(Hinglish kahani • short sentences • emotional • moral story tone)

Vaisampayana bole:

Vanvaas mein,
shaam ke samay,
Pandav bhai aur Draupadī
aag ke paas baithe the.

Sabke mann mein
dukh aur peeda bhari thi.
Hawa bhi udaas lag rahi thi."""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Tab Draupadī,
jo sabki priya thi,
jo samajhdaar aur hriday se prem karne wali thi,
Yudhishthira se boli.

“Hey Maharaj,”
Draupadī boli,
“Dhritarashtra ka beta Duryodhana
bilkul bhi sharminda nahi hai.

Us paapi ne
aap jaise dharmic bhai ko
aur mujhe
hiran ki khaal pehna kar
jungle bhej diya,
aur phir bhi uske mann mein
zara bhi dukh nahi!”

“Uska dil zaroor
lohe ka bana hoga,
jo apne bade bhai se
itni kathor baatein keh gaya.

Aap jo har sukh ke yogya the,
aaj is dukh mein ho,
aur woh apne mitron ke saath
khushiyan mana raha hai.”

“Jab aap van ke liye nikle the,
sirf chaar log nahi roye—
Duryodhana, Karna,
Shakuni aur Dushasana.

Baaki sab Kuruvanshi
aankhon se aansu baha rahe the.”

“Hey Rajan,”
Draupadī boli,
“main aapke rajmahal ka
woh ratno se saja singhasan yaad karti hoon,
aur aaj
yeh kusha ghaas ka asan dekh kar
mera mann toot jaata hai.”

“Pehle aap
reshmi vastron mein the,
chandan se sugandhit the.
Aaj
mitti aur dhool se bhare ho.”

“Pehle hazaron Brahmanon ko
sone ki thaliyon mein bhojan milta tha.
Aaj
aap aur aapke bhai
van ke phal-mool par jee rahe ho.”

“Hey Rajan,”
Draupadī boli,
“yeh dekh kar
kya aapka krodh nahi jagta?”

“Bhima,
jo hazaron haathiyon jitna balwan hai,
aaj jungle mein dukh seh raha hai.
Woh sab kuch sah raha hai
sirf isliye
kyunki woh aapke vachan ka maan rakhta hai.”

“Arjuna,
jo ek hi rath par
devta, daanav aur nagon ko hara chuka hai,
aaj chintit khada hai.

Kya use dekh kar bhi
aapka krodh nahi jaagta?”

“Nakula aur Sahadeva,
jo sundar, yuvak aur veer hain,
aaj dukh mein doobe hain.

Aur mujhe—
Drupad ki putri,
veeron ki patni—
van mein dekh kar bhi
aapka mann nahi hilta?”

“Kehta hai sansaar
ki bina krodh ke
koi Kshatriya hota hi nahi.

Par aaj,
aap us kahawat ko jhootha sabit kar rahe ho.”

Phir Draupadī ne shaant hokar kaha:

“Rajan,
jo Kshatriya
samay par apni shakti nahi dikhata,
use koi maan nahi deta.

Aur jo samay par kshama nahi karta,
woh bhi vinash ko paata hai.”

“Isliye,”
Draupadī boli,
“krodh aur kshama—
dono ka sahi samay hota hai.

Aapko
dono ka santulan
samajhna hoga.”

🌼 Kahani ka Saar (Moral):

Dukh mein krodh aana swabhavik hai

Par har samay krodh sahi nahi hota

Veer wahi hai jo krodh aur kshama ka santulan jaane

Yudhishthira ka bal talwar mein nahi, dhairya mein tha

Sachcha dharm sabr aur samay ki pehchaan se banta hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.17
        # --------------------------------------------------
        with st.expander("Section 3.3.17  Section XXVIII"):
            text1 = """ 
            🌿 Section XXVIII – Kshama aur Shakti ka Santulan

(Hinglish kahani • short sentences • simple • moral story tone)

Draupadī aage boli.
Uski awaaz shaant thi,
par shabdon mein aag thi.

“Hey Maharaj,”
Draupadī ne kaha,
“is baat par
ek purani kahani suni jaati hai.

Yeh kahani hai
Prahlāda aur
uske potey Vali,
jo Virochana ka beta tha.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Ek din Vali ne
apne dada Prahlāda se poocha.

“Hey pitāmaha,”
Vali bola,
“kya kshama zyada shreshth hai
ya shakti aur bal?

Main uljhan mein hoon.
Aap jo kahenge,
main wahi maanunga.”

Prahlāda muskuraye.
Woh dharm ke rahasya jaante the.
Unhone shant swar mein kaha:

“Sun, mere bachche.
Yeh yaad rakh.

Na hamesha shakti sahi hoti hai,
na hamesha kshama.”

“Jo vyakti
har baar maaf karta hai,
uska log upmaan karte hain.

Naukar, mehmaan,
aur shatru tak
uski izzat nahi karte.”

“Uske naukar
uska dhan chura lete hain.
Uske vastra,
gaadi, gehne,
sab apna samajhne lagte hain.”

“Woh na aadesh maante hain,
na sammaan dete hain.

Aur yaad rakh—
is duniya mein apmaan
mrityu se bhi bura hai.”

“Jo hamesha maaf karta hai,
us par log kathor shabd bolte hain.

Kabhi-kabhi
log uski patni tak par
galat nazar daalne lagte hain.”

“Isliye,”
Prahlāda bole,
“vidvaan log
hamesha kshama ki tareef
nahi karte.”

Phir Prahlāda bole:

“Ab sun,
hamesha krodhi rehne wale
ka kya hota hai.”

“Jo vyakti
andhe krodh mein
har kisi ko dand deta hai,
woh apno se door ho jaata hai.”

“Usse rishtedaar,
mitra,
sab nafrat karte hain.

Woh apni sampatti,
shanti
aur izzat sab kho deta hai.”

“Aisa vyakti
ghar mein ghuse
saanp jaisa hota hai.

Log mauka dekhte hi
use nuksaan pahunchate hain.”

“Toh yaad rakh,”
Prahlāda ne kaha,
“na ati-kshama sahi hai,
na ati-krodh.”

“Sahi samay par kshama,
aur sahi samay par shakti—
yeh hi raj-dharm hai.”

Phir Prahlāda ne niyam bataye:

“Jo vyakti pehle tumhara upkaar kare,
agar woh galti kare,
toh use maaf karo.”

“Jo agyaan se galti kare,
use bhi maaf kiya ja sakta hai.”

“Jo jaan-boojhkar galti kare
aur jhooth bole,
use dand milna chahiye.”

“Har vyakti ki pehli galti maaf honi chahiye.”

“Dusri galti par
dand avashyak hai.”

“Vinamrata
kabhi-kabhi bal se bhi shaktishaali hoti hai.

Par bina samay aur sthal dekhe
koi kaarya safal nahi hota.”

“Isliye,”
Prahlāda bole,
“samay, sthal
aur apni shakti ko dekh kar
nirnay lo.”

Draupadī ne kahani samapt karte hue kaha:

“Hey Maharaj,
aaj kshama ka samay nahi hai.

Dhritarashtra ke lalchi putra
baar-baar humein dukh dete aaye hain.

Aaj shakti dikhane ka samay hai.”

“Jo sirf maaf karta hai,
use log kuchal dete hain.
Jo sirf kathor hota hai,
woh naash paata hai.”

“Wahi sachcha raja hai
jo samay ke anusaar
kabhi kshama
aur kabhi shakti ka upyog kare.”

🌼 Kahani ka Saar (Moral):

Hamesha maaf karna kamzori ban jaata hai

Hamesha gussa rehna vinash laata hai

Samay pehchaan kar nirnay lena hi buddhi hai

Sachcha raj-dharm = kshama + shakti ka santulan

Aaj Draupadī ne kshatriya dharm yaad dilaya"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.18
        # --------------------------------------------------
        with st.expander("Section 3.3.18  Section XXIX"):
            text1 = """ 
            🌿 Section XXIX – Krodh vs Kshama (Yudhishthira ki Soch)

(Hinglish • short & simple lines • children / moral story tone)

Yudhishthira bole.
Unki awaaz shaant thi.
Par soch gehri thi.

“Draupadī,”
Yudhishthira ne kaha,
“gussa hi aadmi ka
naash bhi hai
aur unnati bhi.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Yeh yaad rakho.
Jo apna gussa
kaboo mein rakhta hai,
use safalta milti hai.”

“Jo har baat par
gussa karta hai,
use dukh aur vinaash milta hai.”

“Is duniya mein
gussa
har praani ke vinaash ka
kaarann bana hai.”

“Phir main kaise
aise gusse ko
apna loon
jo poori duniya ko jala deta hai?”

“Gusse mein aadmi
paap karta hai.
Gusse mein aadmi
apne guru tak ka
apmaan kar deta hai.”

“Gusse wala insaan
yeh nahi jaanta
kya bolna chahiye
aur kya nahi.”

“Uske liye
koi galat kaam
ya galat shabd
nahi hota.”

“Gusse mein aadmi
nirdosh ko maar sakta hai
aur doshi ko pooj sakta hai.”

“Gussa
aadmi ko
Yam ke dwar tak
le ja sakta hai.”

“Isliye vidvaan log
gusse ko
apne mann se
door rakhte hain.”

“Jo kisi gusse wale ko
palat kar gussa nahi dikhata,
woh do logon ko bacha leta hai—
khud ko
aur saamne wale ko.”

“Woh dono ka
vaidya hota hai.”

“Agar kamzor aadmi
taakatwar logon par
gussa kare,
toh woh
apni hi barbaadi likhta hai.”

“Isliye kaha gaya hai—
kamzor ko hamesha
gussa dabana chahiye.”

“Aur jo buddhimaan hai,
woh bhi
zulm sehkar
gussa nahi karta.”

“Woh shanti se
dusre ko nazarandaz karke
parlok mein sukh paata hai.”

“Isliye,”
Yudhishthira bole,
“chahe aadmi
mazboot ho ya kamzor,
kshama hi shreshth hai.”

“Sach
jhooth se behtar hai.
Komalta
nirdayata se behtar hai.”

“Phir main kaise
sirf Duryodhana ko maarne ke liye
itna bhayanak gussa apna loon?”

“Sachchi shakti
bahar ke gusse mein nahi,
andar ke niyantran mein hoti hai.”

“Jo apne uthe hue gusse ko
buddhi se daba le,
wahi sach mein shaktishaali hai.”

“Gusse wala aadmi
na daan kar paata hai,
na dhairya,
na garima,
na veerta.”

“Gussa chhodkar hi
sahi samay par
sahi shakti dikhayi ja sakti hai.”

“Moorkh log
gusse ko shakti samajhte hain.
Par asal mein
gussa duniya ko todne ke liye bana hai.”

“Agar har ghaav ka badla
ghaav se diya jaaye,
toh duniya ka ant ho jaaye.”

“Agar pita putra ko maare,
putra pita ko,
pati patni ko
aur patni pati ko—
toh janm hi kaise hoga?”

“Shanti se hi srishti chalti hai.”

“Agar raja bhi gusse mein rahe,
toh praja barbaad ho jaati hai.”

“Isliye duniya zinda hai
kyunki kuch log
dharti jaise kshamavaan hote hain.”

“Jo apmaan, peeda
aur zulm ke baad bhi
maaf kar deta hai,
wahi mahaan hai.”

“Jo apne gusse par vijay paata hai,
use dono lok milte hain.”

Phir Yudhishthira ne
Kashyapa Rishi ke shabd yaad kiye:

“Kshama hi dharm hai.
Kshama hi yagya hai.
Kshama hi Ved hai.
Kshama hi satya hai.”

“Kshama se
brahmand tika hai.
Kshama se hi
sab lok milte hain.”

“Jo sab kuch maaf kar sakta hai,
woh Brahma ko pa leta hai.”

“Aise log
is lok mein bhi samman paate hain
aur parlok mein bhi.”

Yudhishthira bole:

“Isliye Draupadī,
apne gusse ko shant karo.”

“Bheeshma,
Krishna,
Drona,
Vidura,
Kripa—
sab shanti ki baat karte hain.”

“Mujhe lagta hai
Dhritarashtra
humein rajya wapas de dega.”

“Agar usne lobh chuna,
toh vinaash uska hoga.”

“Suyodhana rajya ke yogya nahi,
isliye usme kshama nahi.”

“Main yogya hoon,
isliye kshama
mujhe apne paas rakhti hai.”

“Kshama aur komalta
aatma ki asli shakti hain.
Main inhi par chalunga.”

🌼 Moral (Seekh):

Gussa = vinaash

Kshama = srishti

Sachchi shakti = gusse par niyantran

Raja wahi mahaan hai jo shant rehkar faisla kare

Kshama sabse badi shakti hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.19
        # --------------------------------------------------
        with st.expander("Section 3.3.19  Section XXX"):
            text1 = """ 
            🌑 Section XXX – Draupadī ka Prashn (Bhagya, Karma aur Ishwar)

(Hinglish • emotional + philosophical • moral-story style)

Draupadī boli.
Is baar unki awaaz mein
sirf dukh nahi,
vidroh aur prashn tha.

“Yudhishthira,”
“main Dhatri aur Vidhatri ko pranam karti hoon
jinhe shayad tumhari buddhi par
parda daal diya hai!”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Tum apne pita–purkhon se
alag soch rahe ho.”

“Insaan ke karma
hi use jeevan ke alag-alag
haalaton mein daalte hain.”

“Karma ka phal
tala nahi ja sakta.”

“Par yeh maanna
ki mukti mil jaayegi
sirf bholaapan hai!”

“Agar sach mein
dharm, komalta, kshama,
sachchai aur saralta se
iss duniya mein sukh milta—
toh tum par
yeh bhayanak aapda
kabhi na aati!”

“Tum itne yogya ho,
tumhare bhai itne veer hain—
phir bhi yeh vinaash
tum par kyun aaya?”

“Tumne kabhi
dharm ko chhoda hi nahi!”

“Rajya bhi dharm ke liye,
jeevan bhi dharm ke liye—
yeh baat Brahman,
devta, sab jaante hain!”

“Bhima, Arjuna,
Nakula–Sahadeva,
mujhe—
sab chhod sakte ho,
par dharm ko kabhi nahi!”

“Kehta hai shastra—
raja dharm ki raksha karta hai,
aur dharm raja ki.”

“Par yahan kya dekh rahi hoon main?
Dharm tumhari raksha nahi kar raha!”

“Tumhara mann
chhaya ki tarah
hamesha dharm ke peeche chalta raha.”

“Tumne kabhi
na apnon ka apmaan kiya,
na chhote–badon ka.”

“Poora sansaar bhi mil jaata,
phir bhi tumhara ahankar
kabhi nahi badhta!”

“Tumne hamesha
Brahmano, devtaon, pitron ko
pooja.”

“Tumne Brahmano ki
har ichchha poori ki.”

“Yati, sannyasi,
vanaprasthi—
sab tumhare ghar
sona ki thaliyon mein
bhojan paate the!”

“Van mein rehne walon ko bhi
tumne daan diya.”

“Tumhare ghar mein
aisa kuch nahi tha
jo tum Brahman ko na de sako!”

“Pehle mehmaan,
phir sab praani,
aur ant mein tum khud—
yeh tumhara niyam tha!”

“Har prakaar ke yagya,
har prakaar ke karm—
tumhare ghar mein
nirantar hote rahe!”

“Yahan jungle mein bhi,
rajya chhin jaane ke baad bhi,
tumhara dharm
kam nahi hua!”

“Phir bhi…
us bhayanak pal mein
juye ke samay—
tum sab kuch haar gaye.”

“Rajya, dhan, shastra,
bhai…
aur mujhe bhi!”

“Tum itne saral,
itne sachche—
phir juye jaisa paap
tumhe kaise bha gaya?”

“Yeh dekhkar
mera mann hil gaya hai!”

“Ek purani kahani yaad aati hai—
insaan apni marzi ka nahi,
Bhagwan ki ichchha ka daas hota hai.”

“Bhagwan pehle hi
janm se pehle
sukh–dukh likh deta hai,
karma ko beej bana kar.”

“Jaise kathputli
dor se nachti hai,
waise hi praani
Ishwar ke ishaaron par chalte hain.”

“Jaise pakshi
dor se bandha ho,
waise hi hum sab
Bhagwan se bandhe hain.”

“Koi apna niyanta nahi.”

“Motiyon ki mala,
naak mein rassi se bandha bail,
ya nadi mein gira ped—
sab Bhagwan ke aadesh par chalte hain.”

“Ek pal bhi
insaan swatantra nahi.”

“Andhkaar mein lipte praani
khud apna bhagya nahi chunte.”

“Swarg ya narak—
sab Bhagwan ki prerana se.”

“Jaise halki tinke
tez hawa ke bas mein—
waise hi hum sab
Bhagwan ke adheen.”

“Yeh sharir sirf ek saadhan hai—
jisse Ishwar
paap–punya ka phal bhugatata hai.”

“Uski Māyā itni bhayanak hai
ki praani
ek dusre ko maar dete hain!”

“Muniyon ko sab kuch alag dikhta hai.
Aam log
sirf bahari roop dekhte hain.”

“Bhagwan khud hi
srishti karta hai,
aur khud hi naash—
jaise bachcha
mitti ke khilaune se khelta hai.”

“Par yeh dekhkar
mera hriday hil jaata hai—
achhe log dukh mein,
aur dusht log sukh mein!”

“Duryodhana jaise paapi ko
rajya aur sukh kyun?”

“Agar paap ka phal
karta hi bhugte—
toh phir Ishwar paap se kaise bache?”

“Aur agar paap ka phal
karta nahi bhugta—
toh shakti hi sab kuch hai!”

“Phir main un kamzoron ke liye roti hoon
jin ke paas shakti nahi!”

🌘 Is Section ki Gehri Seekh:

Draupadī bhagya vs dharm par prashn uthati hai

Woh Ishwar ki Māyā aur anyay par virodh karti hai

Yeh adhyay Manav Dukh ka Darshanik Sankat hai

Yahan Mahābhārata ka sabse kathin sawal uthta hai:
“Agar sab Bhagwan ke adheen hai, to nyay kahan hai?”"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.20
        # --------------------------------------------------
        with st.expander("Section 3.3.20  Section XXXI"):
            text1 = """ 
            🌗 Section XXXI – Yudhishthira ka Uttar (Shraddha, Dharma aur Kartavya)

(Hinglish • calm, deep, moral-story tone)

Yudhishthira bole.
Unki awaaz shaant thi,
par shabd bahut gehre.

“Yajñaseni,”
“tumhari baatein
meethi hain,
sundar hain,
aur shabdon se bhari hui hain.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Humne dhyaan se
sab suna.”

“Par jo tum keh rahi ho,
usme nāstikta ka rang hai.”

“Main kabhi bhi
karma ke phal ke liye
karm nahi karta.”

“Main daan karta hoon
kyunki daan karna mera kartavya hai.”

“Main yagya karta hoon
kyunki yagya karna mera dharm hai.”

“Grihastha ke roop mein
jo bhi karna chahiye,
main apni poori shakti se karta hoon—
yeh soche bina
ki phal milega ya nahi.”

“Main dharm isliye nahi karta
ki mujhe uska phal chahiye,
balki isliye
ki main Ved ke niyamon ka ullanghan na karoon
aur sajjanon ka aacharan dekhkar seekhoon.”

“Mera mann
swabhav se hi
dharm ki ore jhukta hai.”

“Jo vyakti dharm ka phal chah kar dharm karta hai,
woh dharm ka vyapari hai.”

“Uska svabhav chhota hota hai,
aur woh kabhi
sach mein dharmik nahi hota.”

“Na hi use
uske karm ka phal milta hai.”

“Aur jo vyakti
dharmik karma karke bhi
mann mein sandeh rakhta hai,
use bhi phal nahi milta.”

“Main Vedon ke aadhar par keh raha hoon—
dharm par kabhi sandeh mat karo.”

“Jo dharm par sandeh karta hai,
use pashu-yoni milti hai.”

“Jo vyakti kam buddhi ka ho
aur dharm, Ved aur Rishiyon par sandeh kare,
woh amar aur aanand ke lok se
vanjit ho jaata hai.”

“Jaise Shudra
Ved ke adhikar se vanchit hote hain.”

“Agar kisi achhi kul mein janma bachcha
Ved padhe
aur achha aacharan rakhe,
toh raja-rishi
use vriddh muni ke saman maante hain—
chahe woh yuva hi kyun na ho.”

“Par jo paapi
dharm par sandeh kare
aur shastron ka ullanghan kare,
woh lutere aur nich se bhi
neeche maana jaata hai.”

“Tumne khud dekha hai
Maharshi Markandeya ko.”

“Sirf dharm ke bal par hi
unhone sharir sahit amaratva paya.”

“Vyasa, Vashishtha, Maitreya,
Narada, Lomasa, Shuka—
yeh sab sirf dharm se
shuddh atma wale bane.”

“Tum unhe apni aankhon se dekhti ho—
devtaon se bhi shreshth,
shraap aur vardaan dene mein saksham.”

“Yeh Rishi
Ved mein likha hua
apni aankhon se dekhte hain.”

“Isliye, he priye,
tumhe Ishwar ya dharm par
sandeh nahi karna chahiye.”

“Jo murkh
sirf apni tark-shakti par ghamand karta hai,
aur Rishiyon ko paagal samajhta hai,
woh sirf bahari sukh dekhta hai.”

“Uski aankhein
antar-satya se andhi hoti hain.”

“Jo dharm par sandeh karta hai,
uske liye
koi praayashchit nahi hota.”

“Woh chinta se bhara rehta hai
aur swarg ke lok nahi paata.”

“Par jo shraddha ke saath
dharm ka palan karta hai,
use anant aanand milta hai.”

“Jo Rishiyon ke pramaan ko thukrata hai,
use na is jeevan mein
aur na agle jeevan mein
sukh milta hai.”

“Dharm hi ek naav hai,
jo swarg jaane walon ko
sansaar ke samundar se paar karati hai.”

“Agar dharm ka koi phal na hota,
toh yeh sansaar
andhkaar mein doob jaata.”

“Na koi moksha chaahta,
na gyaan,
na dhan.”

“Log pashuon ki tarah jeete.”

“Agar tapasya, brahmacharya, yagya,
Ved-adhyayan, daan, satya—
sab nishphal hote,
toh peedhi-dar-peedhi
log dharm kyun apnaate?”

“Rishi, devta, Gandharva, Rakshas—
sab dharm ka palan karte hain
kyunki Ishwar phal dene wala hai.”

“Tum apne janm ko yaad karo,
aur Dhrishtadyumna ke janm ko bhi.”

“Yeh sab
dharm ke phal ke pramaan hain.”

“Jo mann ko niyantran mein rakhte hain,
woh thode mein bhi santusht rehte hain.”

“Murkh log
zyada paakar bhi
khush nahi hote.”

“Karma ka phal
aur uska rahasya
devtaon ke liye bhi
gehra hai.”

“Isliye,
agar tumhe phal na dikhe,
toh bhi dharm par sandeh mat karo.”

“Yagya shraddha se karo,
daan vinamrata se.”

“Karma ka phal hota hai,
aur dharm shashvat hai.”

“Brahma ne yeh satya
apne putron ko bataya hai.”

“Isliye, he Krishna,
apna sandeh chhod do.”

“Ishwar ki ninda mat karo.”

“Unhe samjho,
unhe naman karo.”

“Us Supreme Being ko kabhi tuchchh mat samajhna,
jinki kripa se
manav
dharm ke dwara
amarata ko paata hai.”

🌱 Is Section ki Seekh (Simple Words mein):

Yudhishthira = Nishkaam Dharma (kartavya bina phal ke lobh ke)

Shraddha > Tark

Dharm ka phal turant dikhe ya na dikhe, phir bhi dharm satya hai

Sandeh se nahi, vishwas se jeevan chalata hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.21
        # --------------------------------------------------
        with st.expander("Section 3.3.21  Section XXXII"):
            text1 = """ 
            🌾 Section XXXII – Draupadi ka Vichaar (Karma, Prayās aur Umeed)

(Hinglish • short sentences • children’s / moral-story tone)

Draupadi boli.
Uski awaaz bhaari thi.
Dukh se bhari hui.

“Pritha ke putra,”
“main dharm ka apmaan kabhi nahi karti.”

“Bhagwan ko kaise ninda kar sakti hoon,
jo sab praniyon ke swami hain?”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Main sirf dukh se boli hoon.”
“Mujhe roti hui samajh lo.”

“Par meri baat dhyaan se suno.”

“Is duniya mein
har jeev ko kuch na kuch karna hi padta hai.”

“Sirf patthar aur ped
bina kuch kiye reh sakte hain.”

“Chalne-phirne wale prani
bina karma ke nahi jee sakte.”

“Bachcha janm lete hi
maa ka doodh peeta hai.”

“Mantra se murti ko dard hota hai.”

“Isse pata chalta hai
ki pichhle janm ke karm
is janm ko chalaate hain.”

“Sab prani
apne purva-janm ke karmon se
phal paate hain.”

“Yeh niyam
sab par lagu hota hai.”

“Par manushya alag hai.”

“Manushya
iss aur agle jeevan ko
apne karm se badalne ki koshish karta hai.”

“Isliye, O Bharata,”
“bina karma ke
jeevan chal hi nahi sakta.”

“Tumhe bhi karma karna chahiye.”
“Haath par haath rakhkar baithna
tumhe ninda ka paatra bana dega.”

“Karma ko
apna kavach bana lo.”

“Agar sirf kharch karte rahoge
aur kamane ki koshish nahi karoge,
toh Himavat jitna dhan bhi
khatm ho jaayega.”

“Agar karma na hota,
toh duniya ke sab prani
kab ke khatam ho jaate.”

“Kuch log kehte hain
sab kuch bhagya se hota hai.”

“Kuch kehte hain
sab kuch sanyog se hota hai.”

“Par jo log
sirf bhagya par bharosa karke
baithe rehte hain,
woh sabse kamzor hote hain.”

“Woh us kachche matke jaise hote hain
jo paani mein turant toot jaata hai.”

“Jo kehta hai
‘sab sanyog hai’
aur phir kuch nahi karta,
woh bhi zyada jee nahi paata.”

“Isliye jo log
karma ki shakti mein vishwas rakhte hain,
wahi prashansaniya hote hain.”

“Jo bina prayās ke dhan milta hai,
use log sanyog kehte hain.”

“Jo dharm se milta hai,
use bhagya kehte hain.”

“Par jo apni mehnat se milta hai,
woh apni yogyata ka pramaan hota hai.”

“Sach yeh hai ki
yeh sab bhi
pichhle janm ke karmon ka hi phal hai.”

“Bhagwan sabka hisaab rakhte hain.”
“Wahi phal baantte hain.”

“Yeh sharir
sirf ek upkaran hai.”

“Par phir bhi,”
“manushya sochta hai,
nirnay leta hai,
aur phir karma karta hai.”

“Isliye hum kehte hain
ki manushya apne karm ka kaaran khud hai.”

“Gaon, shehar, mahal—
sab manushya ke karm se bane hain.”

“Jo kaam jaankar kiya jaata hai,
woh achha hota hai.”

“Anjaane mein kiya kaam
kamzor hota hai.”

“Agar manushya
apne karm ka kaaran na hota,
toh yagya ka phal bhi na milta.”

“Na guru hota,
na shishya.”

“Safalta milti hai toh prashansa hoti hai.”
“Asafalta hoti hai toh ninda.”

“Yeh sab isliye hai
kyunki karta khud manushya hota hai.”

“Kuch cheezein bhagya se milti hain.”
“Kuch sanyog se.”
“Kuch mehnat se.”

“Iske alawa
koi chautha raasta nahi.”

“Yeh Manu ka bhi nishkarsh hai.”

“Jo karma nahi karta,
woh gir jaata hai.”

“Jo karma karta hai,
uske safal hone ki sambhavana hoti hai.”

“Agar safalta na mile,
toh bhi
us par dosh nahi aata.”

“Kisan kheti karta hai.”
“Beej daalta hai.”

“Phir baadal par chhod deta hai.”

“Agar baarish na ho,
toh bhi kisan kehta hai—
‘maine apna kartavya nibha diya.’”

“Isliye, O Bharata,”
“koshish karke bhi asafal hone par
nirash mat hona.”

“Safalta
kai cheezon ke milne se aati hai.”

“Par bina prayās ke
kuch bhi nahi milta.”

“Samay, sadhan, buddhi, shakti—
sab ko jodna padta hai.”

“In sab mein
parakram sabse mahatvapurn hai.”

“Agar shatru balwan ho,
toh saam, daam, bhed ka sahara lo.”

“Apne shatru ki kamzori dhundo.”

“Kabhi bhi
apne aap ko kamzor mat samjho.”

“Jo khud ko tuchchh samajhta hai,
woh kabhi upar nahi uthta.”

“Is duniya mein safalta
samay aur paristhiti ke anusaar
karma karne se milti hai.”

“Yeh baatein,”
“mere pita ke ghar
ek vidvaan Brahman ne mujhe sikhayi thi.”

“Unhone kaha tha—
‘Karma hi jeevan ka aadhaar hai.’”

🌼 Is Section ki Seekh (Simple Words):

Sirf bhagya ya sanyog par baithna galat hai

Karma karna zaroori hai, phal mile ya na mile

Safalta = prayās + samay + paristhiti

Mehnat kabhi vyarth nahi jaati

Asafalta bhi seekh hoti hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.22
        # --------------------------------------------------
        with st.expander("Section 3.3.22  Section XXXIII"):
            text1 = """ 
            🔥 Section XXXIII – Bhima ka Aag se Bhara Vichaar

(Hinglish • short & simple • moral-story tone)

Vaisampayana bole.
Draupadi ki baat sun kar,
Bhima ka dil bhar aaya.

Usne gehri saans li.
Aankhon mein gussa tha.
Pair tez ho gaye.

Aur woh seedha
Yudhishthira ke paas gaya.  """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Bhima bola,

“Rajaa,
tum purkhon ke raaste par chalo.”

“Yeh jungle ka jeevan
humein kya de raha hai?”

“Na rajya hai,
na sukh,
na bal.”

“Duryodhana ne rajya
na dharm se jeeta,
na shaurya se.”

“Usne dhokhe ke paashe se
sab chheen liya.”

“Woh us jackal jaisa hai
jo sher ka shikar chura leta hai.”

“Hum sher hain,
phir bhi chup baithe hain.”

“Sirf ek pratigya ke liye
itna bada dukh?”

“Woh dhan,
jo dharm aur sukh ka aadhaar hai,
tumne chhod diya.”

“Gandiva dhari Arjuna ke hote hue bhi
rajya humse chhin gaya.”

“Yeh humari kamzori nahi,
tumhari atyadhik shaanti ka phal hai.”

“Hum tumhari izzat mein
sab kuch seh rahe hain.”

“Isi ka faayda
hamare shatru utha rahe hain.”

“Jungle mein rehna
kisi kamzor ka kaam hai.”

“Koi bhi balwaan
aise nahi jeeta.”

“Na Krishna ko yeh pasand hai,”
“na Arjuna ko,”
“na mujhe,”
“na Madri ke putron ko.”

“Tum bas bolte ho—
‘Dharm, Dharm’.”

“Kya niraasha ne
tumhara veeratva chheen liya?”

“Jo apna rajya wapas nahi le sakta,
wahi niraash hota hai.”

“Humein kamzor samjha ja raha hai.”

“Yeh baat
mujhe yudh mein marne se bhi zyada chubhti hai.”

“Agar hum yudh mein mar jaayein,
toh swarg milega.”

“Par yeh vanvaas
zinda rehkar bhi maut jaisa hai.”

“Ya toh hum sabko maar kar
dharti ka rajya lein.”

“Yahi kshatriya ka kartavya hai.”

“Jo dharm
apno ko dukh de,
woh dharm nahi hota.”

“Kabhi-kabhi
dharm bhi kamzori ban jaata hai.”

“Sirf dharm ke liye jeene wala
aksar dukhi hi rehta hai.”

“Woh sooraj ko dekh na paane wale
andhe jaisa hota hai.”

“Na sirf dhan,
na sirf sukh,
na sirf dharm—”

“Teenon ka santulan zaroori hai.”

“Shaastra kehte hain—
subah dharm,
dopahar dhan,
shaam sukh.”

“Zindagi ke pehle hissa mein sukh,”
“beech mein dhan,”
“aur ant mein dharm.”

“Jo in teenon ke beech atka rehta hai,
woh dukhi jeevan jeeta hai.”

“Tum faisla karo—
paana hai ya chhodna hai.”

“Sirf daan, yagya, aur padhai
bina dhan ke sambhav nahi.”

“Rajya ke bina
mahadaan bhi nahi hota.”

“Kshatriya ke liye
bal aur parakram hi dharm hai.”

“Bhiksha ya kamzori
tumhe shobha nahi deti.”

“Arjuna aur main tumhare saath hain.”

“Dushman ko mita do.”

“Rajya paana hi tumhara dharm hai.”

“Yeh dharm
khud Ishwar ne
kshatriya ke liye banaya hai.”

“Bal se hi rajya milta hai.”

“Bina bal ke
sab kuch bekaar hai.”

“Dhan ko beej ki tarah kharch karo,
taaki aur dhan uge.”

“Par bina soch ke kharch
baad mein dukh deta hai.”

“Thoda dharm chhod kar
agar zyada dharm milta ho,
toh wahi buddhimani hai.”

“Shatru ke mitron ko alag karo.”

“Phir shatru kamzor ho jaata hai.”

“Kabhi kamzor bhi
mil kar balwaan ko hara dete hain.”

“Jaise madhumakkhiyan
bade daku ko maar deti hain.”

“Sooraj jaisa bano—
jo bachata bhi hai
aur jalaata bhi.”

“Kshatriya ke liye
yudh hi tapasya hai.”

“Yudh mein haar bhi
vanvaas se behtar hai.”

“Aaj duniya hairaan hai
tumhari yeh haalat dekh kar.”

“Sab tumhari sachchai ki tareef karte hain,
aur Duryodhana ki burai.”

“Log kehte hain—
jaise kutte ke chamde mein doodh,
waise hi Duryodhana ke haath mein rajya.”

“Bachche aur auratein bhi
yeh baat dohra rahe hain.”

“Isliye, O Raja,”
“aaj hi rath par chadho.”

“Brahmanon se aashirvaad lo.”

“Hastinapur ki ore chalo.”

“Hum sab tumhare saath hain.”

“Arjuna ke teer,”
“meri gada—”

“koi seh nahi paayega.”

“Indra jaise Asuron ko kuchla tha,”
“waise hi hum bhi jeetenge.”

“Phir kyun na jeetein hum apna rajya?”

🌟 Is Section ki Seekh (Simple Moral):

Sirf dharm par jeena bhi galat ho sakta hai

Dharm + Dhan + Shakti ka santulan zaroori hai

Kshatriya ke liye parakram bhi dharm hai

Kamzori ko log galat samajhte hain

Kabhi-kabhi nyay ke liye kathor hona padta hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.23
        # --------------------------------------------------
        with st.expander("Section 3.3.23  Section XXXIV"):
            text1 = """ 
            🌿 Section XXXIV – Yudhishthira ka Shaant Par Majboot Uttar

(Hinglish • short & simple • children’s / moral-story tone)

Vaisampayana bole.
Bhima ke kathor shabdon ko sun kar,
Ajatshatru Yudhishthira ne
thoda ruk kar
apni saans sambhaali.

Unke chehre par dard tha,
par mann shaant tha.

Phir woh bole—"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Yudhishthira ne kaha:

“Bhima,
jo tum keh rahe ho
galat nahi hai.”

“Tum mujhe chubhne wale shabd keh rahe ho,
par main tumhe dosh nahi deta.”

“Yeh sab meri hi galti se hua.”

“Main hi paashe khelne baitha.”

“Maine socha tha
Duryodhana se uska rajya chheen lunga.”

“Par maine yeh nahi socha
ki main is khel mein anjaan hoon.”

“Sakuni bahut chaalaak tha.”

“Woh paashe ka jaadu jaanta tha.”

“Sabke saamne
usne mujhe hara diya.”

“Main chah kar bhi
apna mann sambhaal nahi paaya.”

“Gussa aaya,
aur gussa buddhi chheen leta hai.”

“Garv, ahankaar aur ghamand
mann ko kamzor bana dete hain.”

“Isliye Bhima,
main tumhari baaton ka bura nahi maanta.”

“Jo kuch hua,
shayad pehle se likha tha.”

“Jab Duryodhana ne
humein das bana diya,
tab Draupadi ne hi
humein sambhaala.”

“Phir doosra khel hua.”

“Us din sabke saamne
Duryodhana ne shart rakhi.”

“12 saal vanvaas,
aur 13va saal gupt roop mein.”

“Agar pehchaan ho gayi,
toh phir se wahi saza.”

“Usne kaha—
agar tum yeh poora kar lo,
toh rajya tumhara.”

“Usne bhi wahi shart maani.”

“Maine sabke saamne kaha—
‘So be it.’”

“Phir hum haar gaye
aur vanvaas mila.”

“Isi pratigya ki wajah se
aaj hum junglon mein bhatak rahe hain.”

“Duryodhana phir bhi khush nahi hua.”

“Usne logon ko kaha
hamari museebat par hansne ko.”

“Par Bhima,”
“jo pratigya sabke saamne li ho,
use todna kaise theek ho sakta hai?”

“Mere liye,”
“galat tareeke se rajya paane se
toh maut bhi behtar hai.”

“Mujhe yaad hai Bhima,”
“tum us din gusse mein the.”

“Tum mere haath jala dena chahte the.”

“Arjuna ne tumhe roka.”

“Agar tab hum kuch kar paate,
shayad aaj yeh din na dekhna padta.”

“Par ab samay beet chuka hai.”

“Ab kadve shabd kehne ka
kya laabh?”

“Mera sabse bada dukh yeh hai,”
“ki us sabha mein
hum Draupadi ko bachha nahi paaye.”

“Mera dil aaj bhi jalta hai.”

“Par ek baar di hui pratigya
main tod nahi sakta.”

“Bhima,”
“achhe din phir aayenge.”

“Jaise kisan beej bo kar
fasal ka intezaar karta hai.”

“Jo pehle chot khata hai,”
“aur sahi samay par badla leta hai,”
“uski veerta amar hoti hai.”

“Aise veer ko—
duniya yaad rakhti hai.”

“Dushman jhukte hain,”
“aur dost saath aa jaate hain.”

“Par meri pratigya
kabhi jhoothi nahi ho sakti.”

“Mere liye,”
“satya jeevan se bhi bada hai.”

“Rajya,”
“putra,”
“yash,”
“dhan—”

“yeh sab mil kar bhi
satya ke solahve hissa ke barabar nahi.”

🌟 Is Section ki Seekh (Moral):

Gussa galat faisle karwata hai

Galti maan lena bhi mahaanta hai

Pratigya aur satya Yudhishthira ke liye sabse upar hain

Sahi samay ka intezaar bhi veerta hai

Galat tareeke se jeet, jeet nahi hoti"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.24
        # --------------------------------------------------
        with st.expander("Section 3.3.24  Section XXXV"):
            text1 = """ 
            🔥 Section XXXV – Bhima ka Aag-sa Bhara Virodh

(Hinglish • emotional • moral–philosophical tone)

Bhima ne kaha:

“O Raja,
insaan toh jhag (froth) jaisa hai—
na tikne wala,
har pal tootne wala.”

“Tum samay (time) ke saath samjhauta kaise kar sakte ho,
jab samay khud
anant, tez aur maut jaisa hai?”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Zindagi har pal ghat rahi hai—
jaise surma,
jisme se har baar sui se thoda nikal jaata hai.”

“Jo apni maut ka din jaanta ho,
sirf wahi intezaar kar sakta hai.”

“Hum kaise intezaar karein,
jab har pal
maut paas aa rahi hai?”

“13 saal rukna
matlab zindagi kam karna.”

“Isse pehle ki maut aaye,
humein apna rajya wapas lena chahiye.”

“Jo apne dushman ko dand nahi deta,
woh gandi cheez jaisa hai.”

“Woh dharti par bojh hai—
jaise kaam na kar paane wala bail.”

“Aisa aadmi bina yash ke mar jaata hai.”

“Raja,
tumhara haath sona barsa sakta hai.”

“Tumhara naam poori prithvi par faila hai.”

“Toh phir kyun na
shastra se rajya paao?”

“Agar kisi ne apne apmaan ka badla lekar
ussi din narak chala jaaye,
toh woh narak bhi
uske liye swarg ban jaata hai.”

“Gussa dabana
aag se bhi zyada jalata hai.”

“Main jal raha hoon,
din-raat neend nahi aati.”

“Arjuna bhi jal raha hai—
par sher ki tarah
apna gussa dabaye baitha hai.”

“Nakula, Sahadeva,
maa Kunti—
sab chup hain
sirf tumhe khush rakhne ke liye.”

“Main aur Draupadi hi
apna dard bol rahe hain.”

“Par sach yeh hai—
sab yudh chahte hain.”

“Isse bada dukh kya hoga Raja—
ki kamzor aur neech log
hamara rajya bhog rahe hain?”

“Tum pratigya todne mein
sharm mehsoos karte ho.”

“Par sach yeh hai—
is dukh ko koi sarah nahi raha.”

“Tumhari buddhi
sach nahi dekh rahi—
jaise koi Veda ratta ho
par arth na jaanta ho.”

“Tum Brahman jaise dayalu ho.”

“Par phir Kshatriya ghar mein
paida kaise hue?”

“Kshatriya dharm
seedha nahi,
tedha bhi hota hai.”

“Toh phir Duryodhan ko
maaf kyun kar rahe ho?”

“Tumhare paas
buddhi, shakti, shastra, janm—
sab kuch hai.”

“Toh phir kyun
hilte bhi nahi?”

“Tum toh aise lagte ho
jaise bada sa saanp
jo hila bhi nahi.”

“Tumhe chhupaana
Himalaaya ko ghaas se dhakne jaisa hai.”

“Suraj kabhi chhup nahi sakta.”

“Arjuna kaise chhupa rahega?”

“Nakula-Sahadeva
do yuva sher jaise hain—
kaise chhupenge?”

“Draupadi—
poori duniya jaanti hai use.”

“Main bhi bachpan se pehchana jaata hoon.”

“Toh gupt vaas kaise hoga?”

“Humne kai raja haraye the.”

“Woh sab ab Duryodhan ke saath milkar
hum par nazar rakhenge.”

“Agar ek bhi pehchaan ho gayi—
toh sab kuch phir se shuru.”

“Hum pehle hi
13 mahine jungle mein reh chuke hain.”

“Maana jaaye
jaise 13 saal.”

“Jaise Soma ke badle pot-herb.”

“Ya phir pratigya todne ka paap
daan se dhoya jaa sakta hai.”

“Isliye Raja—
nirnay lo.”

“Dushmanon ko maaro.”

“Yudh se bada koi dharm nahi
Kshatriya ke liye.”

🌟 Is Section ki Gehri Seekh:

Bhima karm, shakti aur turant action ka prateek hai

Woh maanta hai: intezaar = kamzori

Kshatriya dharm mein yudh bhi dharm hai

Sirf daya kabhi-kabhi anyay ban jaati hai

Samay kisi ka intezaar nahi karta"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.25
        # --------------------------------------------------
        with st.expander("Section 3.3.25  Section XXXVI"):
            text1 = """ 
            🌿 Section XXXVI – Yudhishthira ka Gambhir Nirnay

(Hinglish • simple • moral story tone)

Bhima ke teekhe shabdon ko sunkar
Yudhishthira gehri saans leta hai.
Woh chup ho jaata hai.
Uska mann bhaari ho jaata hai.

Woh dil mein sochta hai—

“Main raja ka dharm jaanta hoon.
Sab varno ke kartavya bhi jaanta hoon.
Par dharma bahut sookshma hota hai.
Use zabardasti kaise toda ja sakta hai?
Kya main Meru parvat ko pees sakta hoon?
Nahi.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Thodi der baad,
soch-vichaar karke,
Yudhishthira bolta hai—

“Bhima,
tum jo keh rahe ho, usme sach hai.
Par meri baat bhi suno.”

“Jo kaam sirf gusse aur himmat par kiya jaaye,
woh aksar dukh deta hai.”

“Par jo kaam
soch-samajh kar,
sahi taiyaari ke saath,
aur sahi samay par kiya jaaye—
woh safal hota hai.”

“Devgann bhi
aise kaamon mein saath dete hain.”

Phir Yudhishthira gehri baat kehta hai—

“Tum turant yudh chahte ho.
Par dekho hamare saamne kaun khade hain.”

“Bhishma, Drona, Kripa—
yeh sab mahaan yoddha hain.”

“Karna—
jo kabhi peeche nahi harta,
jo shastraon ka maharathi hai.”

“Duryodhana aur uske bhai—
sab taiyaar hain.”

“Woh raja bhi hamare khilaaf hain
jinhe humne pehle haraya tha.”

“Woh sab
Kauravon ke paksh mein hain.”

“Unke paas sena hai, dhan hai,
aur badla lene ki aag hai.”

“Bhishma aur Drona
humein bhi pyaar karte hain.”

“Par raj ka rin bhi hota hai.”

“Jo samman unhe mila hai,
uske liye
woh apni jaan bhi de sakte hain.”

“Bhima,
mujhe Karna ki chinta sone nahi deti.”

“Uska teer chalane ka hunar
sabse tez hai.”

“Jab tak hum
in sab ko nahi hara dete,
Duryodhana tak pahunchna
namumkin hai.”

Yeh sunkar
Bhima shaant ho jaata hai.
Woh kuch nahi bolta.

Tabhi
Maharshi Vyasa wahan aate hain.
Pandav unka samman karte hain.

Vyasa muskurate hain aur kehte hain—

“Yudhishthira,
main tumhare mann ka bojh jaanta hoon.”

“Tum Bhishma, Drona, Karna se darte ho.
Par main tumhara yeh dar door karunga.”

“Ek vidhi hai.
Use shant mann se suno.
Aur use apnao.”

Vyasa,
Yudhishthira ko alag le jaakar kehte hain—

“Ab tumhari unnati ka samay aane wala hai.”

“Arjuna
sab shatruon ko yudh mein haraayega.”

“Main tumhe
Pratismriti Vidya deta hoon.”

“Yeh gyaan
Arjuna ke kaam aayega.”

“Arjuna ko kaho—
woh devtaon ke paas jaaye.”

“Indra, Rudra, Varuna, Kubera, Yama—
sab se divya astra le.”

“Woh iske yogya hai.”

“Woh Narayana ka mitra hai.
Woh swayam ek mahaan rishi jaisa hai.”

“Tum log
is jungle ko chhod kar
kisi aur van mein jao.”

“Ek jagah zyada din rehna
na tumhare liye theek hai,
na tapasviyon ke liye.”

“Yahan ke hiran aur vanaspati
nuksaan mein aa jayenge.”

Yudhishthira shuddh hokar
woh gyaan grahan karta hai.

Vyasa ashirvaad dekar
antardhyaan ho jaate hain.

Yudhishthira
us gyaan ko mann mein basa leta hai.
Woh use sahi samay par
yaad karta rehta hai.

Phir Pandav
Dvaita van chhodkar
Kamyaka van ki taraf jaate hain,
Saraswati nadi ke kinaare.

Kai Brahman
unke saath jaate hain.

Wahan Pandav
kuch samay rehte hain.

Roz dhanush ka abhyas hota hai.
Ved mantron ki dhvani gunjti hai.

Woh shikar bhi karte hain,
aur devta, pitri,
aur Brahmanon ke liye
vidhi-poorvak karm karte hain.

🌟 Is Section ki Seekh:

Sirf gussa yudh jeetata nahi

Soch, samay aur taiyaari zaroori hai

Dharm kabhi jaldi mein nahi toda jaata

Sahi samay par kiya gaya karm hi safal hota hai

Guru ka margdarshan andhere mein roshni hota hai"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.26
        # --------------------------------------------------
        with st.expander("Section 3.3.26  Section XXXVII"):
            text1 = """ 
            🌿 Section XXXVII – Arjuna ka Kathor Tapasya Yatra

(Hinglish • short sentences • children/moral story tone)

Kuch samay baad,
Dharmaraj Yudhishthira
Maharshi Vyasa ke shabd yaad karta hai.

Woh Arjuna ko chupchaap bulata hai.
Pyaar se uske haath pakadta hai.
Chehre par halki si muskaan hoti hai.

Phir dheere se bolta hai—"""
            create_image_text_layout(
                "attached_assets/chapter3/3.3.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            “Arjuna,
Bhishma, Drona, Kripa, Karna,
aur Drona putra—
sab shastra-vidya ke maharathi hain.

Brahma astra, dev astra,
maanav aur vayu ke astra—
sab jaante hain.

Duryodhana unka bahut samman karta hai.
Unhe khush rakhta hai.
Isliye woh uske liye jaan tak de denge.”

“Poori prithvi aaj
Duryodhana ke adhikaar mein hai.
Gaon, sheher, jungle, samudra—sab.”

“Arjuna,
ab tum hi hamara ekmatra sahara ho.”

Yudhishthira gambhir ho jaata hai.

“Mainne Vyasa se
ek vidya paayi hai.
Aisi vidya jo
poore brahmand ko khol kar dikha de.”

“Main yeh vidya
tumhe deta hoon.”

“Par usse pehle—
tumhe kathor tapasya karni hogi.”

“Dhanush aur talwar ke saath,
kavach pehen kar,
uttar disha ki taraf jao.”

“Devtaon ke raja Indra ke paas jao.”

“Sab divya astra
Indra ke paas hain.”

“Isi din niklo, Arjuna.”

Yudhishthira vidhipoorvak
woh vidya Arjuna ko deta hai.
Mann, vachan, aur sharir—
sab shant rehte hain.

Arjuna agya maanta hai.

Arjuna Gandiva dhanush uthata hai.
Akshay tarqash saath leta hai.
Kavach aur angulitra pehenta hai.

Havan karta hai.
Brahmanon se aashirvaad leta hai.

Nikalte waqt,
aasmaan ki taraf dekhta hai—
mann mein ek hi sankalp—

“Dhritarashtra ke putron ka ant.”

Raste mein
Brahman, Siddh,
aur adrishya shaktiyaan bolti hain—

“Putra, tumhara kaam poora ho.”

“Vijay tumhari ho.”

Draupadi (Krishna)
bhari mann se kehti hai—

“Arjuna,
tumhare bina humein
sukh nahi milega.”

“Hamara jeevan,
hamari vijay—
sab tum par nirbhar hai.”

“Tumhara safar
mangalmay ho.”

“Lakshmi, Saraswati,
Shaktiyaan tumhari raksha karein.”

Arjuna sabko pranam karta hai.
Bhaiyon ke chakkar lagata hai.
Aur chal padta hai.

Prakriti bhi raasta chhod deti hai.
Pahad, jungle, nadi—
sab paar karta hai.

Himavat,
Gandhamadan,
aur kathin marg—
sab ek hi din mein.

Tapasya ka bal tha.

Aakhirkaar
woh Indrakila parvat pahunchta hai.

Tab aakash se awaaz aati hai—

“Ruko!”

Arjuna dekhta hai—
ek tapasvi brahman,
ped ke neeche baitha hai.

Jataayein,
tejas,
shaant chehra.

Brahman kehta hai—

“Putra,
yahaan shastra ki zarurat nahi.
Yeh shanti ka sthal hai.”

“Dhanush chhod do.”

Par Arjuna nahi hilta.
Uska sankalp atoot hai.

Tab tapasvi muskurata hai
aur kehta hai—

“Main Sakra (Indra) hoon.”

“Maango jo chaho.”

Arjuna vinamr ho kar bolta hai—

“Hey Indra,
mujhe swarg nahi chahiye.”

“Na bhog, na sukh.”

“Mujhe divya astra chahiye.”

“Bina shatru ko haraaye,
main chain se nahi reh sakta.”

Indra kehte hain—

“Pehle
tumhe Mahadev (Shiva) ke darshan karne honge.”

“Unke darshan ke baad
tumhe sab astra milenge.”

Yeh kehkar
Indra antardhyaan ho jaate hain.

Arjuna wahi ruk jaata hai.
Kathor tapasya shuru karta hai.

Shant mann.
Ek hi lakshya.

🌟 Is Section ki Seekh (Moral):

Sirf shakti kaafi nahi hoti

Tapasya + sankalp = asli bal

Sacha yoddha
pehle apne mann ko jeetta hai

Guru ki agya aur dhairya
vijay ka raasta dikhate hain"""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.4  Kairata Parva (Kirata Episode)"):

        # --------------------------------------------------
        # Section 3.4.1
        # --------------------------------------------------
        with st.expander("Section 3.4.1  Section XXXVIII"):
            text1 = """ 
            Section XXXVIII – Arjuna ki Tapasya ki Kahani (Hinglish Story Version)

Raja Janmejaya ne kaha,
“O mahāgyānī,
main Arjuna ki poori kahani sunna chahta hoon.

Bataiye,
Arjuna ne kaise astr–shastra haasil kiye?
Wo akela, bina dare, jungle mein kaise gaya?
Aur wahan reh kar usne kya-kya kiya?

Mujhe ye bhi jaan’na hai
ki kaise Bhagwān Shiv aur devon ke raja Indra
Arjuna se prasann hue.

Arjuna aur Shiv ji ke beech jo yuddh hua,
wo adbhut tha.
Us kahani ko sun kar
rom-rom khade ho jaate hain.

Isliye,
hey Brahmana,
mujhe sab kuch poori tarah bataiye.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            🌿 Arjuna ka vanvaas

Vaishampayana bole,
“O Kuruvansh ke shreshth,
main tumhe ye pavitra kahani sunata hoon.

Yudhishthira ke aadesh par,
Arjuna jungle ki taraf nikle.
Unka lakshya tha –
Indra aur Mahadev ka darshan.

Haath mein divya dhanush,
aur sone ki mooth wali talvaar thi.
Man bilkul shant tha.
Iraada atal tha.

Wo Himavat parvat ki taraf badhe.
Aur bina samay gawaye
tapasya mein lag gaye.

🌲 Bhayanak par sundar jungle

Arjuna akela
ghane jungle mein ghuse.
Wahan kaante the,
jangli jaanwar the,
aur anokhe pakshi the.

Par jungle sirf bhayanak nahi tha.
Wo sundar bhi tha.

Aasmaan se shankh aur nagade jaise shabd aaye.
Phoolon ki baarish hui.
Badal chha gaye.

Devta dekh rahe the.

🏔️ Himavat ka saundarya

Arjuna ne parvat ke neeche ka kshetra dekha.
Hari-bhari ghaatiyaan thi.
Nadiyaan beh rahi thi.

Hans, battakh, mor, kokil –
sab apni madhur awaaz mein ga rahe the.

Ye sab dekh kar
Arjuna ka mann prasann ho gaya.

🔥 Kathor tapasya

Usi pavitra sthal par
Arjuna ne tapasya shuru ki.

Ghaas ke kapde pehne.
Kala mrigcharm liya.
Haath mein danda rakha.

Pehle mahine –
teen din mein ek baar fal khaya.

Dusre mahine –
chhe din mein ek baar.

Teesre mahine –
pandrah din mein ek baar.

Chauthe mahine –
sirf saans par jeene lage.

Pairon ke anguthe par khade rahe.
Haath upar uthaye.
Kisi sahare ke bina.

Unke baal chamakne lage.
Bijli jaise.
Ya kamal jaise.

🌍 Rishiyon ki chinta

Arjuna ki tapasya se
dharti garam hone lagi.
Sab taraf dhuaan sa uthne laga.

Rishi ghabra gaye.
Wo sab Bhagwān Shiv ke paas gaye.

Bole,
“O Mahadev,
Arjuna ki tapasya bahut kathor hai.
Humein nahi pata wo kya chahte hain.
Kripya unhe rokiye.”

🕉️ Mahadev ka vachan

Mahadev shant muskaan ke saath bole,
“Chinta mat karo.

Main Arjuna ka mann jaanta hoon.
Wo na swarg chahte hain,
na dhan,
na lambi zindagi.

Jo wo chahte hain,
main aaj hi poora karunga.”

Ye sun kar
sab rishi prasann ho gaye.
Aur apne-apne sthal laut gaye.

✨ Moral (Seekh):

Sachchi tapasya shor nahi karti.
Wo itni gehri hoti hai
ki Bhagwān khud usse pehchaan lete hain.

Jo nishkāam bhav se mehnat karta hai,
uska marg khud hi khul jaata hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.2
        # --------------------------------------------------
        with st.expander("Section 3.4.2  Section XXXIX"):
            text1 = """ 
            Section XXXIX – Kirata aur Arjuna ka Mahāyuddh (Hinglish Story Version)

Vaishampayana bole:

Sab rishi wapas ja chuke the.
Tab Bhagwān Shiv ne ek naya roop liya.

Wo Kirata bane.
Sunehre ped jaise chamak rahe the.
Unka sharir Meru parvat jaisa bada tha.
Haath mein dhanush aur zahreeli saanp jaise teer the."""
            create_image_text_layout(
                "attached_assets/chapter3/3.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Unke saath Uma ji bhi thi.
Wo bhi Kirata stri ke roop mein thi.
Kai anokhe gan aur hazaaron Kirata striyan saath thi.

Unke aate hi jungle aur bhi sundar ho gaya.
Par achanak…
sab awaazein ruk gayin.
Nadi, pakshi, hawa — sab shant.

🐗 Muka ka aana

Tab Arjuna ne dekha,
ek bhayanak Rakshasa Muka,
suar ke roop mein,
usse maarne aa raha tha.

Arjuna ne turant Gāṇḍīva uthaya.
Teer chadhaaya.
Aur kaha,
“Main shant tapasya mein hoon.
Par agar tu mujhe maarne aaya hai,
toh main tujhe Yama ke paas bhej dunga.”

Jaise hi Arjuna ne teer chalaaya,
Kirata ne bhi teer chala diya.

Dono teer
ek hi pal mein
Muka ko lage.

Zordaar awaaz hui.
Aur Muka gir pada.
Rakshasa apna asli roop dikha kar
mar gaya.

⚔️ Vivad aur gussa

Arjuna ne Kirata ko dekha.
Aur kaha,
“Ye shikaar mera tha.
Tumne mere niyam tode hain.
Is jungle mein aise kaam galat hai.”

Kirata muskuraya aur bola,
“Ye jungle hamara ghar hai.
Aur Rakshasa ko maine pehle maara.”

Baat badh gayi.
Gussa badh gaya.

🏹 Teeron ka yuddh

Dono ne
teeron ki baarish kar di.
Arjuna ke teer
bijli jaise chamakte the.

Par Kirata
parvat ki tarah
hilta hi nahi tha.

Arjuna hairaan ho gaya.
“Ye kaun hai?
Sirf Rudra hi mere teeron ko jhel sakte hain.”

Teer khatam ho gaye.
Arjuna ne dhanush se hi vaar kiya.
Par Kirata ne Gāṇḍīva chheen liya.

Talvaar chali.
Par talvaar toot gayi.

Ped, patthar, mukke —
sab bekaar gaye.

Ant mein,
Kirata ne ek zor ka vaar kiya.
Arjuna gir pada.
Behosh ho gaya.

🙏 Bhakti ka pal

Thodi der baad Arjuna utha.
Khoon se bhara sharir tha.
Aankhon mein aansu the.

Usne mitti se Shiv ji ki moorti banayi.
Phool chadhaaye.
Dil se pooja ki.

Aur tab…
usne dekha –
jo phool usne moorti par chadhaaye the,
wo Kirata ke sir par the.

Arjuna samajh gaya.
Ye koi aur nahi…
Mahadev khud the.

Wo turant jhuk gaya.
Charno mein gir gaya.

🔱 Mahadev ka vardaan

Mahadev apne asli roop mein aaye.
Teesri aankh chamak rahi thi.
Uma ji saath thi.

Shiv ji bole,
“Arjuna,
tumhara sahas anokha hai.
Tumhari tapasya aur dhairya
mere barabar hai.

Main tumse prasann hoon.
Main tumhe apna divya astra doonga.
Tum apne sab shatruon par vijay paaoge.”

🌸 Arjuna ka stavan

Arjuna ne haath jod kar kaha,
“Hey Mahadev,
aap hi sab ka kaaran hain.
Aap hi Vishnu hain,
aur aap hi Shiv.

Mujhe maaf kar dijiye.
Agyanta mein jo yuddh hua,
wo mera aparadh tha.”

Mahadev muskuraye.
Arjuna ka haath pakda.
Aur gale laga liya.

✨ Moral (Seekh):

Ahankār se yuddh hota hai,
par bhakti se Bhagwān milte hain.

Jab shakti ke saath
vinamrata aa jaaye,
tab hi sachcha vardaan milta hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.3
        # --------------------------------------------------
        with st.expander("Section 3.4.3  Section XL"):
            text1 = """ 
            Section XL – Mahadev ka Vardaan (Hinglish Story Version)

Mahadev ne Arjuna se kaha:

“Arjuna,
tum pichhle janam mein Nara the.
Aur Nārāyaṇa tumhare mitra the.

Badari van mein
tum dono ne hazaaron saal
kathor tapasya ki thi.

Tum mein aur Vishnu mein
ek hi shakti basti hai.
Tum dono milkar
poore jagat ko sambhalte ho."""
            create_image_text_layout(
                "attached_assets/chapter3/3.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            Jab Indra ka rajyabhishek hua tha,
tab tum aur Krishna
is dhanush se
daityon ko shant kiya tha.

Ye Gāṇḍīva
pehle bhi tumhara hi tha.
Maine sirf
apni Māyā se
ise tumse chheen liya tha.

Tumhare akshay teer-daan
phir se akshay rahenge.
Tumhara sharir
rog aur peeda se mukt rahega.

Tumhari shakti
kabhi asafal nahi hogi.
Main tumse prasann hoon.

Ab bolo,
jo vardaan chahte ho,
wo maang lo.”

🙏 Arjuna ka var

Arjuna ne vinamr hokar kaha:

“O Mahadev,
mujhe aapka
sabse bhayankar divya astra chahiye.

Wo astra
jo yug ke ant mein
poori srishti ko mita sakta hai.

Us astra se
main aane wale mahayuddh mein
Bhishma, Drona, Kripa aur Karna
jaise veeron ka saamna kar saku.

Us astra se
main daityon, rakshason
aur bure shaktiyon ka vinash kar saku.

Hey Shiv,
mujhe wahi astra dijiye.”

🔱 Pāśupata Astra

Mahadev bole:

“Main tumhe
apna priya astra
Pāśupata deta hoon.

Is astra ko
na Indra jaanta hai,
na Yama,
na Varuna,
na Vayu.

Iski shakti
bahut bhayanak hai.

Isse bina kaaran
kabhi prayog mat karna.
Agar galat jagah chala,
toh poora jagat
nasht ho sakta hai.

Isse man se,
aankhon se,
shabd se
aur dhanush se
chalaaya ja sakta hai.”

🌍 Divya shiksha

Arjuna ne apne aap ko shuddh kiya.
Aur kaha,
“Prabhu,
mujhe sikhaiye.”

Mahadev ne
Pāśupata Astra ka
poora gyaan diya.
Chalaana bhi,
rokna bhi.

Wo astra
ab Arjuna ke saath
waise hi rehne laga
jaise Mahadev ke saath.

Jaise hi astra mila,
dharti kaanp uthi.
Pahad, van, nadi,
sab hil gaye.

Aakash mein
shankh aur nagade bajne lage.
Devta aur daitya
sab dekh rahe the.

Arjuna ke sharir se
sab dosh
mit gaye.

☁️ Swarg ka aadesh

Mahadev bole,
“Ab tum
swarg jao.”

Arjuna ne
sir jhuka kar pranam kiya.
Haath jod kar dekhta raha.

Mahadev,
Uma ji ke saath,
akash ki taraf badhe.
Him parvat
phir se shant ho gaya.

Aur Arjuna ke dil mein
sirf ek baat thi—
Bhagwān ki kripa.

✨ Moral (Seekh):

Jab shakti ke saath
vinamrata hoti hai,
tab Bhagwān
apni sabse badi shakti dete hain.

Divya gyaan
sirf usi ko milta hai
jo zimmedaari samajhta ho."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.4
        # --------------------------------------------------
        with st.expander("Section 3.4.4  Section XLI"):
            text1 = """ 
            Section XLI – Devtaon ka Vardaan aur Arjuna ka Gaurav (Hinglish Story Version)

Vaishampayana bole:

Mahadev
Arjuna ke saamne hi
soorya ke ast hone jaise
antar-dhyaan ho gaye.

Arjuna hairaan reh gaya.
Usne mann mein kaha,

“Kitna bhaagyashaali hoon main.
Maine Bhagwān Shiv ko dekha.
Unhe sparsh kiya.
Ab meri jeet nishchit hai.
Mere shatru pehle hi haar chuke hain.”"""
            create_image_text_layout(
                "attached_assets/chapter3/3.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ 
            🌊 Varuna ka aagaman

Tab achanak
Varuna dev aaye.
Neel mani jaise chamak rahe the.
Unke saath nadiyaan,
jal jeev,
naag aur anya dev the.

Poori disha
prakash se bhar gayi.

💰 Kuvera ka darshan

Phir Kuvera aaye.
Sone jaise tej se chamak rahe the.
Unke saath Yaksh the.
Aasmaan jagmaga utha.

⚖️ Yama ka aadesh

Phir Yama dev aaye.
Gambhir awaaz mein bole,

“Arjuna,
tum pehle janam mein Nara rishi the.
Brahma ji ke kehne par
tum manushya bane.

Tum yuddh mein
Bhishma, Drona ke sainikon
aur sab adharmi shaktiyon ko haraoge.

Tum Karna ko bhi parajit karoge.
Tumhari keerti
sada rahegi.

Tumne Mahadev ko prasann kiya hai.
Isliye,
ye lo mera gada astra.”

Arjuna ne vinamrta se
astra grahan kiya.

🌧️ Varuna ka vardaan

Varuna bole,

“Arjuna,
main jal ka swami hoon.
Mera paash astra
koi nahi tod sakta.

Isse tum
sab shatruon ko baandh sakte ho.
Ye astra tumhara ho.”

Arjuna ne
Varuna ka astra bhi grahan kiya.

🌟 Kuvera ka uphaar

Kuvera muskuraye aur bole,

“Arjuna,
tum mujhe Krishna jaise priya ho.

Main tumhe
Antardhyan astra deta hoon.
Isse shatru
nindra mein chale jaate hain.

Is astra se
tum bade kaam karoge.”

Arjuna ne
yeh astra bhi shraddha se liya.

☁️ Indra ka sandesh

Ant mein Indra dev bole,

“Arjuna,
tum pehle hi devta the.
Par abhi
devtaon ka kaam poora baaki hai.

Tumhe swarg aana hoga.
Mera rath
jaldi tumhe lene aayega.
Wahan main tumhe
aur divya astra dunga.”

🙏 Antim vandana

Arjuna ne
sab Lokapalon ko pranam kiya.
Jal, phal aur shabd se pooja ki.

Devta prasann hue.
Aur apne-apne lok
laut gaye.

Arjuna
shant mann se khada raha.
Uska dil
anand se bhara tha.

Usne socha,
“Ab mera jeevan
safal ho gaya.”

✨ Moral (Seekh):

Jab manushya
tapasya, dhairya aur vinamrata se
apna kartavya nibhata hai,
to prakriti aur devta khud sahayata karte hain.

Sachchi shakti
ahankār mein nahi,
seva aur dharma mein hoti hai."""
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.5  Indralokagamana Parva (Journey to Indras Heaven)"):

        # --------------------------------------------------
        # Section 3.5.1
        # --------------------------------------------------
        with st.expander("Section 3.5.1  Section XLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.2
        # --------------------------------------------------
        with st.expander("Section 3.5.2  Section XLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.3
        # --------------------------------------------------
        with st.expander("Section 3.5.3  Section XLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.4
        # --------------------------------------------------
        with st.expander("Section 3.5.4  Section XLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.5
        # --------------------------------------------------
        with st.expander("Section 3.5.5  Section XLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.6
        # --------------------------------------------------
        with st.expander("Section 3.5.6  Section XLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.7
        # --------------------------------------------------
        with st.expander("Section 3.5.7  Section XLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.8
        # --------------------------------------------------
        with st.expander("Section 3.5.8  Section XLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.9
        # --------------------------------------------------
        with st.expander("Section 3.5.9  Section L"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.5.10
        # --------------------------------------------------
        with st.expander("Section 3.5.10  Section LI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.5.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.6  Nalopakhyana Parva (Story of Nala)"):

        # --------------------------------------------------
        # Section 3.6.1
        # --------------------------------------------------
        with st.expander("Section 3.6.1  Section LII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.2
        # --------------------------------------------------
        with st.expander("Section 3.6.2  Section LIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.3
        # --------------------------------------------------
        with st.expander("Section 3.6.3  Section LIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.4
        # --------------------------------------------------
        with st.expander("Section 3.6.4  Section LV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.5
        # --------------------------------------------------
        with st.expander("Section 3.6.5  Section LVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.6
        # --------------------------------------------------
        with st.expander("Section 3.6.6  Section LVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.7
        # --------------------------------------------------
        with st.expander("Section 3.6.7  Section LVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.8
        # --------------------------------------------------
        with st.expander("Section 3.6.8  Section LIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.9
        # --------------------------------------------------
        with st.expander("Section 3.6.9  Section LX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.10
        # --------------------------------------------------
        with st.expander("Section 3.6.10  Section LXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.11
        # --------------------------------------------------
        with st.expander("Section 3.6.11  Section LXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.12
        # --------------------------------------------------
        with st.expander("Section 3.6.12  Section LXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.13
        # --------------------------------------------------
        with st.expander("Section 3.6.13  Section LXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.14
        # --------------------------------------------------
        with st.expander("Section 3.6.14  Section LXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.15
        # --------------------------------------------------
        with st.expander("Section 3.6.15  Section LXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.16
        # --------------------------------------------------
        with st.expander("Section 3.6.16  Section LXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.17
        # --------------------------------------------------
        with st.expander("Section 3.6.17  Section LXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.18
        # --------------------------------------------------
        with st.expander("Section 3.6.18  Section LXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.19
        # --------------------------------------------------
        with st.expander("Section 3.6.19  Section LXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.20
        # --------------------------------------------------
        with st.expander("Section 3.6.20  Section LXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.21
        # --------------------------------------------------
        with st.expander("Section 3.6.21  Section LXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.22
        # --------------------------------------------------
        with st.expander("Section 3.6.22  Section LXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.23
        # --------------------------------------------------
        with st.expander("Section 3.6.23  Section LXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.24
        # --------------------------------------------------
        with st.expander("Section 3.6.24  Section LXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.25
        # --------------------------------------------------
        with st.expander("Section 3.6.25  Section LXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.26
        # --------------------------------------------------
        with st.expander("Section 3.6.26  Section LXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.27
        # --------------------------------------------------
        with st.expander("Section 3.6.27  Section LXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.6.28
        # --------------------------------------------------
        with st.expander("Section 3.6.28  Section LXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.6.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.7  Tirtha-yatra Parva (Pilgrimage)"):

        # --------------------------------------------------
        # Section 3.7.1
        # --------------------------------------------------
        with st.expander("Section 3.7.1  Section LXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.2
        # --------------------------------------------------
        with st.expander("Section 3.7.2  Section LXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.3
        # --------------------------------------------------
        with st.expander("Section 3.7.3  Section LXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.4
        # --------------------------------------------------
        with st.expander("Section 3.7.4  Section LXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.5
        # --------------------------------------------------
        with st.expander("Section 3.7.5  Section LXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.6
        # --------------------------------------------------
        with st.expander("Section 3.7.6  Section LXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.7
        # --------------------------------------------------
        with st.expander("Section 3.7.7  Section LXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.8
        # --------------------------------------------------
        with st.expander("Section 3.7.8  Section LXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.9
        # --------------------------------------------------
        with st.expander("Section 3.7.9  Section LXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.10
        # --------------------------------------------------
        with st.expander("Section 3.7.10  Section LXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.11
        # --------------------------------------------------
        with st.expander("Section 3.7.11  Section XC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.12
        # --------------------------------------------------
        with st.expander("Section 3.7.12  Section XCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.13
        # --------------------------------------------------
        with st.expander("Section 3.7.13  Section XCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.14
        # --------------------------------------------------
        with st.expander("Section 3.7.14  Section XCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.15
        # --------------------------------------------------
        with st.expander("Section 3.7.15  Section XCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.16
        # --------------------------------------------------
        with st.expander("Section 3.7.16  Section XCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.17
        # --------------------------------------------------
        with st.expander("Section 3.7.17  Section XCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.18
        # --------------------------------------------------
        with st.expander("Section 3.7.18  Section XCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.19
        # --------------------------------------------------
        with st.expander("Section 3.7.19  Section XCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.20
        # --------------------------------------------------
        with st.expander("Section 3.7.20  Section XCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.21
        # --------------------------------------------------
        with st.expander("Section 3.7.21  Section C"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.22
        # --------------------------------------------------
        with st.expander("Section 3.7.22  Section CI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.23
        # --------------------------------------------------
        with st.expander("Section 3.7.23  Section CII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.24
        # --------------------------------------------------
        with st.expander("Section 3.7.24  Section CIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.25
        # --------------------------------------------------
        with st.expander("Section 3.7.25  Section CIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.26
        # --------------------------------------------------
        with st.expander("Section 3.7.26  Section CV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.27
        # --------------------------------------------------
        with st.expander("Section 3.7.27  Section CVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.28
        # --------------------------------------------------
        with st.expander("Section 3.7.28  Section CVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.29
        # --------------------------------------------------
        with st.expander("Section 3.7.29  Section CVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.30
        # --------------------------------------------------
        with st.expander("Section 3.7.30  Section CIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.31
        # --------------------------------------------------
        with st.expander("Section 3.7.31  Section CX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.32
        # --------------------------------------------------
        with st.expander("Section 3.7.32  Section CXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.33
        # --------------------------------------------------
        with st.expander("Section 3.7.33  Section CXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.34
        # --------------------------------------------------
        with st.expander("Section 3.7.34  Section CXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.35
        # --------------------------------------------------
        with st.expander("Section 3.7.35  Section CXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.36
        # --------------------------------------------------
        with st.expander("Section 3.7.36  Section CXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.37
        # --------------------------------------------------
        with st.expander("Section 3.7.37  Section CXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.38
        # --------------------------------------------------
        with st.expander("Section 3.7.38  Section CXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.39
        # --------------------------------------------------
        with st.expander("Section 3.7.39  Section CXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.40
        # --------------------------------------------------
        with st.expander("Section 3.7.40  Section CXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.41
        # --------------------------------------------------
        with st.expander("Section 3.7.41  Section CXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.41.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.42
        # --------------------------------------------------
        with st.expander("Section 3.7.42  Section CXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.42.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.43
        # --------------------------------------------------
        with st.expander("Section 3.7.43  Section CXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.43.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.44
        # --------------------------------------------------
        with st.expander("Section 3.7.44  Section CXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.44.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.45
        # --------------------------------------------------
        with st.expander("Section 3.7.45  Section CXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.45.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.46
        # --------------------------------------------------
        with st.expander("Section 3.7.46  Section CXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.46.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.47
        # --------------------------------------------------
        with st.expander("Section 3.7.47  Section CXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.47.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.48
        # --------------------------------------------------
        with st.expander("Section 3.7.48  Section CXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.48.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.49
        # --------------------------------------------------
        with st.expander("Section 3.7.49  Section CXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.49.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.50
        # --------------------------------------------------
        with st.expander("Section 3.7.50  Section CXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.50.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.51
        # --------------------------------------------------
        with st.expander("Section 3.7.51  Section CXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.51.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.52
        # --------------------------------------------------
        with st.expander("Section 3.7.52  Section CXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.52.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.53
        # --------------------------------------------------
        with st.expander("Section 3.7.53  Section CXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.53.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.54
        # --------------------------------------------------
        with st.expander("Section 3.7.54  Section CXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.54.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.55
        # --------------------------------------------------
        with st.expander("Section 3.7.55  Section CXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.55.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.56
        # --------------------------------------------------
        with st.expander("Section 3.7.56  Section CXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.56.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.57
        # --------------------------------------------------
        with st.expander("Section 3.7.57  Section CXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.57.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.58
        # --------------------------------------------------
        with st.expander("Section 3.7.58  Section CXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.58.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.59
        # --------------------------------------------------
        with st.expander("Section 3.7.59  Section CXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.59.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.60
        # --------------------------------------------------
        with st.expander("Section 3.7.60  Section CXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.60.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.61
        # --------------------------------------------------
        with st.expander("Section 3.7.61  Section CXL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.61.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.62
        # --------------------------------------------------
        with st.expander("Section 3.7.62  Section CXLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.62.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.63
        # --------------------------------------------------
        with st.expander("Section 3.7.63  Section CXLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.63.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.64
        # --------------------------------------------------
        with st.expander("Section 3.7.64  Section CXLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.64.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.65
        # --------------------------------------------------
        with st.expander("Section 3.7.65  Section CXLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.65.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.66
        # --------------------------------------------------
        with st.expander("Section 3.7.66  Section CXLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.66.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.67
        # --------------------------------------------------
        with st.expander("Section 3.7.67  Section CXLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.67.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.68
        # --------------------------------------------------
        with st.expander("Section 3.7.68  Section CXLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.68.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.69
        # --------------------------------------------------
        with st.expander("Section 3.7.69  Section CXLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.69.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.70
        # --------------------------------------------------
        with st.expander("Section 3.7.70  Section CXLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.70.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.71
        # --------------------------------------------------
        with st.expander("Section 3.7.71  Section CL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.71.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.72
        # --------------------------------------------------
        with st.expander("Section 3.7.72  Section CLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.72.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.73
        # --------------------------------------------------
        with st.expander("Section 3.7.73  Section CLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.73.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.74
        # --------------------------------------------------
        with st.expander("Section 3.7.74  Section CLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.74.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.75
        # --------------------------------------------------
        with st.expander("Section 3.7.75  Section CLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.75.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.76
        # --------------------------------------------------
        with st.expander("Section 3.7.76  Section CLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.76.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.77
        # --------------------------------------------------
        with st.expander("Section 3.7.77  Section CLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.77.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.78
        # --------------------------------------------------
        with st.expander("Section 3.7.78  Section CLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.78.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.79
        # --------------------------------------------------
        with st.expander("Section 3.7.79  Section CLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.79.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.80
        # --------------------------------------------------
        with st.expander("Section 3.7.80  Section CLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.80.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.81
        # --------------------------------------------------
        with st.expander("Section 3.7.81  Section CLX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.81.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.82
        # --------------------------------------------------
        with st.expander("Section 3.7.82  Section CLXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.82.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.83
        # --------------------------------------------------
        with st.expander("Section 3.7.83  Section CLXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.83.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.84
        # --------------------------------------------------
        with st.expander("Section 3.7.84  Section CLXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.84.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.85
        # --------------------------------------------------
        with st.expander("Section 3.7.85  Section CLXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.85.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.86
        # --------------------------------------------------
        with st.expander("Section 3.7.86  Section CLXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.86.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.87
        # --------------------------------------------------
        with st.expander("Section 3.7.87  Section CLXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.87.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.88
        # --------------------------------------------------
        with st.expander("Section 3.7.88  Section CLXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.88.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.89
        # --------------------------------------------------
        with st.expander("Section 3.7.89  Section CLXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.89.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.90
        # --------------------------------------------------
        with st.expander("Section 3.7.90  Section CLXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.90.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.91
        # --------------------------------------------------
        with st.expander("Section 3.7.91  Section CLXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.91.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.92
        # --------------------------------------------------
        with st.expander("Section 3.7.92  Section CLXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.92.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.93
        # --------------------------------------------------
        with st.expander("Section 3.7.93  Section CLXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.93.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.94
        # --------------------------------------------------
        with st.expander("Section 3.7.94  Section CLXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.94.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.95
        # --------------------------------------------------
        with st.expander("Section 3.7.95  Section CLXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.95.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.96
        # --------------------------------------------------
        with st.expander("Section 3.7.96  Section CLXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.96.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.97
        # --------------------------------------------------
        with st.expander("Section 3.7.97  Section CLXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.97.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.98
        # --------------------------------------------------
        with st.expander("Section 3.7.98  Section CLXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.98.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.99
        # --------------------------------------------------
        with st.expander("Section 3.7.99  Section CLXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.99.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.100
        # --------------------------------------------------
        with st.expander("Section 3.7.100  Section CLXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.100.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.7.101
        # --------------------------------------------------
        with st.expander("Section 3.7.101  Section CLXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.7.101.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.8  Markandeya-Samasya Parva (Markandeya Dialogues)"):

        # --------------------------------------------------
        # Section 3.8.1
        # --------------------------------------------------
        with st.expander("Section 3.8.1  Section CLXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.2
        # --------------------------------------------------
        with st.expander("Section 3.8.2  Section CLXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.3
        # --------------------------------------------------
        with st.expander("Section 3.8.3  Section CLXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.4
        # --------------------------------------------------
        with st.expander("Section 3.8.4  Section CLXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.5
        # --------------------------------------------------
        with st.expander("Section 3.8.5  Section CLXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.6
        # --------------------------------------------------
        with st.expander("Section 3.8.6  Section CLXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.7
        # --------------------------------------------------
        with st.expander("Section 3.8.7  Section CLXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.8
        # --------------------------------------------------
        with st.expander("Section 3.8.8  Section CLXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.9
        # --------------------------------------------------
        with st.expander("Section 3.8.9  Section CLXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.10
        # --------------------------------------------------
        with st.expander("Section 3.8.10  Section CXC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.11
        # --------------------------------------------------
        with st.expander("Section 3.8.11  Section CXCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.12
        # --------------------------------------------------
        with st.expander("Section 3.8.12  Section CXCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.13
        # --------------------------------------------------
        with st.expander("Section 3.8.13  Section CXCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.14
        # --------------------------------------------------
        with st.expander("Section 3.8.14  Section CXCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.15
        # --------------------------------------------------
        with st.expander("Section 3.8.15  Section CXCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.16
        # --------------------------------------------------
        with st.expander("Section 3.8.16  Section CXCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.17
        # --------------------------------------------------
        with st.expander("Section 3.8.17  Section CXCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.18
        # --------------------------------------------------
        with st.expander("Section 3.8.18  Section CXCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.19
        # --------------------------------------------------
        with st.expander("Section 3.8.19  Section CXCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.20
        # --------------------------------------------------
        with st.expander("Section 3.8.20  Section CC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.21
        # --------------------------------------------------
        with st.expander("Section 3.8.21  Section CCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.22
        # --------------------------------------------------
        with st.expander("Section 3.8.22  Section CCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.23
        # --------------------------------------------------
        with st.expander("Section 3.8.23  Section CCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.24
        # --------------------------------------------------
        with st.expander("Section 3.8.24  Section CCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.25
        # --------------------------------------------------
        with st.expander("Section 3.8.25  Section CCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.26
        # --------------------------------------------------
        with st.expander("Section 3.8.26  Section CCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.27
        # --------------------------------------------------
        with st.expander("Section 3.8.27  Section CCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.28
        # --------------------------------------------------
        with st.expander("Section 3.8.28  Section CCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.29
        # --------------------------------------------------
        with st.expander("Section 3.8.29  Section CCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.30
        # --------------------------------------------------
        with st.expander("Section 3.8.30  Section CCX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.31
        # --------------------------------------------------
        with st.expander("Section 3.8.31  Section CCXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.31.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.32
        # --------------------------------------------------
        with st.expander("Section 3.8.32  Section CCXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.32.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.33
        # --------------------------------------------------
        with st.expander("Section 3.8.33  Section CCXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.33.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.34
        # --------------------------------------------------
        with st.expander("Section 3.8.34  Section CCXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.34.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.35
        # --------------------------------------------------
        with st.expander("Section 3.8.35  Section CCXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.35.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.36
        # --------------------------------------------------
        with st.expander("Section 3.8.36  Section CCXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.36.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.37
        # --------------------------------------------------
        with st.expander("Section 3.8.37  Section CCXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.37.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.38
        # --------------------------------------------------
        with st.expander("Section 3.8.38  Section CCXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.38.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.39
        # --------------------------------------------------
        with st.expander("Section 3.8.39  Section CCXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.39.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.40
        # --------------------------------------------------
        with st.expander("Section 3.8.40  Section CCXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.40.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.41
        # --------------------------------------------------
        with st.expander("Section 3.8.41  Section CCXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.41.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.42
        # --------------------------------------------------
        with st.expander("Section 3.8.42  Section CCXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.42.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.43
        # --------------------------------------------------
        with st.expander("Section 3.8.43  Section CCXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.43.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.44
        # --------------------------------------------------
        with st.expander("Section 3.8.44  Section CCXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.44.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.45
        # --------------------------------------------------
        with st.expander("Section 3.8.45  Section CCXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.45.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.46
        # --------------------------------------------------
        with st.expander("Section 3.8.46  Section CCXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.46.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.47
        # --------------------------------------------------
        with st.expander("Section 3.8.47  Section CCXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.47.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.48
        # --------------------------------------------------
        with st.expander("Section 3.8.48  Section CCXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.48.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.49
        # --------------------------------------------------
        with st.expander("Section 3.8.49  Section CCXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.49.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.8.50
        # --------------------------------------------------
        with st.expander("Section 3.8.50  Section CCXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.8.50.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.9  Draupadi-Satyabhama Samvada (Dialogue of Draupadi & Satyabhama)"):

        # --------------------------------------------------
        # Section 3.9.1
        # --------------------------------------------------
        with st.expander("Section 3.9.1  Section CCXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.9.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.9.2
        # --------------------------------------------------
        with st.expander("Section 3.9.2  Section CCXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.9.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.9.3
        # --------------------------------------------------
        with st.expander("Section 3.9.3  Section CCXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.9.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.10  Ghosha-yatra Parva (Cattle Expedition)"):

        # --------------------------------------------------
        # Section 3.10.1
        # --------------------------------------------------
        with st.expander("Section 3.10.1  Section CCXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.2
        # --------------------------------------------------
        with st.expander("Section 3.10.2  Section CCXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.3
        # --------------------------------------------------
        with st.expander("Section 3.10.3  Section CCXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.4
        # --------------------------------------------------
        with st.expander("Section 3.10.4  Section CCXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.5
        # --------------------------------------------------
        with st.expander("Section 3.10.5  Section CCXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.6
        # --------------------------------------------------
        with st.expander("Section 3.10.6  Section CCXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.7
        # --------------------------------------------------
        with st.expander("Section 3.10.7  Section CCXL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.8
        # --------------------------------------------------
        with st.expander("Section 3.10.8  Section CCXLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.9
        # --------------------------------------------------
        with st.expander("Section 3.10.9  Section CCXLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.10
        # --------------------------------------------------
        with st.expander("Section 3.10.10  Section CCXLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.11
        # --------------------------------------------------
        with st.expander("Section 3.10.11  Section CCXLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.12
        # --------------------------------------------------
        with st.expander("Section 3.10.12  Section CCXLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.13
        # --------------------------------------------------
        with st.expander("Section 3.10.13  Section CCXLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.14
        # --------------------------------------------------
        with st.expander("Section 3.10.14  Section CCXLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.15
        # --------------------------------------------------
        with st.expander("Section 3.10.15  Section CCXLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.16
        # --------------------------------------------------
        with st.expander("Section 3.10.16  Section CCXLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.17
        # --------------------------------------------------
        with st.expander("Section 3.10.17  Section CCL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.18
        # --------------------------------------------------
        with st.expander("Section 3.10.18  Section CCLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.19
        # --------------------------------------------------
        with st.expander("Section 3.10.19  Section CCLII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.20
        # --------------------------------------------------
        with st.expander("Section 3.10.20  Section CCLIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.21
        # --------------------------------------------------
        with st.expander("Section 3.10.21  Section CCLIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.22
        # --------------------------------------------------
        with st.expander("Section 3.10.22  Section CCLV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.23
        # --------------------------------------------------
        with st.expander("Section 3.10.23  Section CCLVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.24
        # --------------------------------------------------
        with st.expander("Section 3.10.24  Section CCLVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.25
        # --------------------------------------------------
        with st.expander("Section 3.10.25  Section CCLVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.26
        # --------------------------------------------------
        with st.expander("Section 3.10.26  Section CCLIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.10.27
        # --------------------------------------------------
        with st.expander("Section 3.10.27  Section CCLX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.10.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.11  Draupadi-harana Parva (Abduction of Draupadi)"):

        # --------------------------------------------------
        # Section 3.11.1
        # --------------------------------------------------
        with st.expander("Section 3.11.1  Section CCLXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.2
        # --------------------------------------------------
        with st.expander("Section 3.11.2  Section CCLXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.3
        # --------------------------------------------------
        with st.expander("Section 3.11.3  Section CCLXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.4
        # --------------------------------------------------
        with st.expander("Section 3.11.4  Section CCLXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.5
        # --------------------------------------------------
        with st.expander("Section 3.11.5  Section CCLXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.6
        # --------------------------------------------------
        with st.expander("Section 3.11.6  Section CCLXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.7
        # --------------------------------------------------
        with st.expander("Section 3.11.7  Section CCLXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.8
        # --------------------------------------------------
        with st.expander("Section 3.11.8  Section CCLXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.9
        # --------------------------------------------------
        with st.expander("Section 3.11.9  Section CCLXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.10
        # --------------------------------------------------
        with st.expander("Section 3.11.10  Section CCLXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.11
        # --------------------------------------------------
        with st.expander("Section 3.11.11  Section CCLXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.12
        # --------------------------------------------------
        with st.expander("Section 3.11.12  Section CCLXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.13
        # --------------------------------------------------
        with st.expander("Section 3.11.13  Section CCLXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.14
        # --------------------------------------------------
        with st.expander("Section 3.11.14  Section CCLXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.15
        # --------------------------------------------------
        with st.expander("Section 3.11.15  Section CCLXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.16
        # --------------------------------------------------
        with st.expander("Section 3.11.16  Section CCLXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.17
        # --------------------------------------------------
        with st.expander("Section 3.11.17  Section CCLXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.18
        # --------------------------------------------------
        with st.expander("Section 3.11.18  Section CCLXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.19
        # --------------------------------------------------
        with st.expander("Section 3.11.19  Section CCLXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.20
        # --------------------------------------------------
        with st.expander("Section 3.11.20  Section CCLXXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.21
        # --------------------------------------------------
        with st.expander("Section 3.11.21  Section CCLXXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.22
        # --------------------------------------------------
        with st.expander("Section 3.11.22  Section CCLXXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.23
        # --------------------------------------------------
        with st.expander("Section 3.11.23  Section CCLXXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.24
        # --------------------------------------------------
        with st.expander("Section 3.11.24  Section CCLXXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.25
        # --------------------------------------------------
        with st.expander("Section 3.11.25  Section CCLXXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.26
        # --------------------------------------------------
        with st.expander("Section 3.11.26  Section CCLXXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.27
        # --------------------------------------------------
        with st.expander("Section 3.11.27  Section CCLXXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.27.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.28
        # --------------------------------------------------
        with st.expander("Section 3.11.28  Section CCLXXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.28.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.29
        # --------------------------------------------------
        with st.expander("Section 3.11.29  Section CCLXXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.29.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.11.30
        # --------------------------------------------------
        with st.expander("Section 3.11.30  Section CCXC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.11.30.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.12  Pativrata-mahatmya Parva (Glory of Chaste Wives)"):

        # --------------------------------------------------
        # Section 3.12.1
        # --------------------------------------------------
        with st.expander("Section 3.12.1  Section CCXCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.2
        # --------------------------------------------------
        with st.expander("Section 3.12.2  Section CCXCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.3
        # --------------------------------------------------
        with st.expander("Section 3.12.3  Section CCXCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.4
        # --------------------------------------------------
        with st.expander("Section 3.12.4  Section CCXCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.5
        # --------------------------------------------------
        with st.expander("Section 3.12.5  Section CCXCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.6
        # --------------------------------------------------
        with st.expander("Section 3.12.6  Section CCXCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.7
        # --------------------------------------------------
        with st.expander("Section 3.12.7  Section CCXCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.8
        # --------------------------------------------------
        with st.expander("Section 3.12.8  Section CCXCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.9
        # --------------------------------------------------
        with st.expander("Section 3.12.9  Section CCXCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.10
        # --------------------------------------------------
        with st.expander("Section 3.12.10  Section CCC"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.11
        # --------------------------------------------------
        with st.expander("Section 3.12.11  Section CCCI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.12
        # --------------------------------------------------
        with st.expander("Section 3.12.12  Section CCCII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.13
        # --------------------------------------------------
        with st.expander("Section 3.12.13  Section CCCIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.14
        # --------------------------------------------------
        with st.expander("Section 3.12.14  Section CCCIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.15
        # --------------------------------------------------
        with st.expander("Section 3.12.15  Section CCCV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.16
        # --------------------------------------------------
        with st.expander("Section 3.12.16  Section CCCVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.17
        # --------------------------------------------------
        with st.expander("Section 3.12.17  Section CCCVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.12.18
        # --------------------------------------------------
        with st.expander("Section 3.12.18  Section CCCVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.12.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.13  Aranya Parva (Forest Life Continued)"):

        # --------------------------------------------------
        # Section 3.13.1
        # --------------------------------------------------
        with st.expander("Section 3.13.1  Section CCCIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.13.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.13.2
        # --------------------------------------------------
        with st.expander("Section 3.13.2  Section CCCX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.13.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.13.3
        # --------------------------------------------------
        with st.expander("Section 3.13.3  Section CCCXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.13.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.13.4
        # --------------------------------------------------
        with st.expander("Section 3.13.4  Section CCCXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.13.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.13.5
        # --------------------------------------------------
        with st.expander("Section 3.13.5  Section CCCXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.13.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )


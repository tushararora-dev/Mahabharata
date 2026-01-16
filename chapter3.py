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
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.2.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.3  Arjunabhigamana Parva (Arjunas Journey)"):

        # --------------------------------------------------
        # Section 3.3.1
        # --------------------------------------------------
        with st.expander("Section 3.3.1  Section XII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.2
        # --------------------------------------------------
        with st.expander("Section 3.3.2  Section XIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.3
        # --------------------------------------------------
        with st.expander("Section 3.3.3  Section XIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.4
        # --------------------------------------------------
        with st.expander("Section 3.3.4  Section XV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.5
        # --------------------------------------------------
        with st.expander("Section 3.3.5  Section XVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.5.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.6
        # --------------------------------------------------
        with st.expander("Section 3.3.6  Section XVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.6.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.7
        # --------------------------------------------------
        with st.expander("Section 3.3.7  Section XVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.7.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.8
        # --------------------------------------------------
        with st.expander("Section 3.3.8  Section XIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.8.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.9
        # --------------------------------------------------
        with st.expander("Section 3.3.9  Section XX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.9.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.10
        # --------------------------------------------------
        with st.expander("Section 3.3.10  Section XXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.10.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.11
        # --------------------------------------------------
        with st.expander("Section 3.3.11  Section XXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.11.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.12
        # --------------------------------------------------
        with st.expander("Section 3.3.12  Section XXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.12.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.13
        # --------------------------------------------------
        with st.expander("Section 3.3.13  Section XXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.13.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.14
        # --------------------------------------------------
        with st.expander("Section 3.3.14  Section XXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.14.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.15
        # --------------------------------------------------
        with st.expander("Section 3.3.15  Section XXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.15.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.16
        # --------------------------------------------------
        with st.expander("Section 3.3.16  Section XXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.16.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.17
        # --------------------------------------------------
        with st.expander("Section 3.3.17  Section XXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.17.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.18
        # --------------------------------------------------
        with st.expander("Section 3.3.18  Section XXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.18.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.19
        # --------------------------------------------------
        with st.expander("Section 3.3.19  Section XXX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.19.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.20
        # --------------------------------------------------
        with st.expander("Section 3.3.20  Section XXXI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.20.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.21
        # --------------------------------------------------
        with st.expander("Section 3.3.21  Section XXXII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.21.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.22
        # --------------------------------------------------
        with st.expander("Section 3.3.22  Section XXXIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.22.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.23
        # --------------------------------------------------
        with st.expander("Section 3.3.23  Section XXXIV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.23.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.24
        # --------------------------------------------------
        with st.expander("Section 3.3.24  Section XXXV"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.24.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.25
        # --------------------------------------------------
        with st.expander("Section 3.3.25  Section XXXVI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.25.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.3.26
        # --------------------------------------------------
        with st.expander("Section 3.3.26  Section XXXVII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.3.26.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

    with st.expander("Chapter 3.4  Kairata Parva (Kirata Episode)"):

        # --------------------------------------------------
        # Section 3.4.1
        # --------------------------------------------------
        with st.expander("Section 3.4.1  Section XXXVIII"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.4.1.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.2
        # --------------------------------------------------
        with st.expander("Section 3.4.2  Section XXXIX"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.4.2.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.3
        # --------------------------------------------------
        with st.expander("Section 3.4.3  Section XL"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.4.3.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
            create_image_text_layout(
                text_content=text2,
                layout="full"
            )

        # --------------------------------------------------
        # Section 3.4.4
        # --------------------------------------------------
        with st.expander("Section 3.4.4  Section XLI"):
            text1 = """ """
            create_image_text_layout(
                "attached_assets/chapter3/3.4.4.jpg",
                text1,
                layout="side",
                image_position="left"
            )

            text2 = """ """
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


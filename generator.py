def roman(num):
    vals = [
        (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
        (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
        (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")
    ]
    result = ""
    for v, s in vals:
        while num >= v:
            result += s
            num -= v
    return result


parvas = [
    ("3.1", "Aranyaka Parva", "Forest Book", 1, 10),
    ("3.2", "Kirmirabadha Parva", "Slaying of Kirmira", 11, 11),
    ("3.3", "Arjunabhigamana Parva", "Arjuna’s Journey", 12, 37),
    ("3.4", "Kairata Parva", "Kirata Episode", 38, 41),
    ("3.5", "Indralokagamana Parva", "Journey to Indra’s Heaven", 42, 51),
    ("3.6", "Nalopakhyana Parva", "Story of Nala", 52, 79),
    ("3.7", "Tirtha-yatra Parva", "Pilgrimage", 80, 180),
    ("3.8", "Markandeya-Samasya Parva", "Markandeya Dialogues", 181, 230),
    ("3.9", "Draupadi-Satyabhama Samvada", "Dialogue of Draupadi & Satyabhama", 231, 233),
    ("3.10", "Ghosha-yatra Parva", "Cattle Expedition", 234, 260),
    ("3.11", "Draupadi-harana Parva", "Abduction of Draupadi", 261, 290),
    ("3.12", "Pativrata-mahatmya Parva", "Glory of Chaste Wives", 291, 308),
    ("3.13", "Aranya Parva", "Forest Life Continued", 309, 313),
]

for ch, title, eng, start, end in parvas:
    print(f'with st.expander("Chapter {ch} – {title} ({eng})"):\n')

    idx = 1
    for sec in range(start, end + 1):
        sec_no = f"{ch}.{idx}"
        sec_roman = roman(sec)

        print("    # --------------------------------------------------")
        print(f"    # Section {sec_no}")
        print("    # --------------------------------------------------")
        print(f'    with st.expander("Section {sec_no} – Section {sec_roman}"):')
        print('        text1 = """ """')
        print("        create_image_text_layout(")
        print(f'            "attached_assets/chapter3/{sec_no}.jpg",')
        print("            text1,")
        print('            layout="side",')
        print('            image_position="left"')
        print("        )\n")
        print('        text2 = """ """')
        print("        create_image_text_layout(")
        print("            text_content=text2,")
        print('            layout="full"')
        print("        )\n")

        idx += 1

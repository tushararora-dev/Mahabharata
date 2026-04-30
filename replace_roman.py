import re

user_text = """
. Section CLXL
. Section CLXLI
. Section CLXLII
. Section CLXLIII
. Section CLXLIV
. Section CLXLV
. Section CLXLVI
. Section CLXLVII
. Section CLXLVIII
. Section CLXLIX
. Section CC
. Section CCI
. Section CCII
. Section CCIII
. Section CCIV
. Section CCV
. Section CCVI
. Section CCVII
. Section CCVIII
. Section CCIX
. Section CCX
. Section CCXI
. Section CCXII
. Section CCXIII
. Section CCXIV
. Section CCXV
. Section CCXVI
. Section CCXVII
. Section CCXVIII
. Section CCXIX
. Section CCXX
. Section CCXXI
. Section CCXXII
. Section CCXXIII
. Section CCXXIV
. Section CCXXV
. Section CCXXVI
. Section CCXXVII
. Section CCXXVIII
. Section CCXXIX
. Section CCXXX
+ Draupadi-Satyabhama Samvada
. Section CCXXXI
. Section CCXXXII
. Section CCXXXIII
+ Ghosha-yatra Parva
. Section CCXXXIV
. Section CCXXXV
. Section CCXXXVI
. Section CCXXXVII
. Section CCXXXVIII
. Section CCXXXIX
. Section CCXL
. Section CCXLI
. Section CCXLII
. Section CCXLIII
. Section CCXLIV
. Section CCXLV
. Section CCXLVI
. Section CCXLVII
. Section CCXLVIII
. Section CCXLIX
. Section CCL
. Section CCLI
. Section CCLII
. Section CCLIII
. Section CCLIV
. Section CCLV
. Section CCLVI
. Section CCLVII
. Section CCLVIII
. Section CCLIX
. Section CCLX
+ Draupadi-harana Parva
. Section CCLXI
. Section CCLXII
. Section CCLXIII
. Section CCLXIV
. Section CCLXV
. Section CCLXVI
. Section CCLXVII
. Section CCLXVIII
. Section CCLXIX
. Section CCLXX
. Section CCLXXI
. Section CCLXXII
. Section CCLXXIII
. Section CCLXXIV
. Section CCLXXV
. Section CCLXXVI
. Section CCLXXVII
. Section CCLXXVIII
. Section CCLXXIX
. Section CCLXXX
. Section CCLXXXI
. Section CCLXXXII
. Section CCLXXXIII
. Section CCLXXXIV
. Section CCLXXXV
. Section CCLXXXVI
. Section CCLXXXVII
. Section CCLXXXVIII
. Section CCLXXXIX
. Section CCLXL
+ Pativrata-mahatmya Parva
. Section CCLXLI
. Section CCLXLII
. Section CCLXLIII
. Section CCLXLIV
. Section CCLXLV
. Section CCLXLVI
. Section CCLXLVIII
. Section CCLXLIX
. Section CCC
. Section CCCI
. Section CCCII
. Section CCCIII
. Section CCCIV
. Section CCCV
. Section CCCVI
. Section CCCVII
. Section CCCVIII
+ Aranya Parva
. Section CCCIX
. Section CCCX
. Section CCCXI
. Section CCCXII
. Section CCCXIII
"""

roman_list = []
for line in user_text.split('\n'):
    if line.startswith('. Section '):
        roman_list.append(line.replace('. Section ', '').strip())

with open('chapter3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
roman_idx = 0
start_replacing = False

for i, line in enumerate(lines):
    if 'with st.expander("Section 3.8.11' in line:
        start_replacing = True
        
    if start_replacing and 'with st.expander("Section' in line and 'Chapter' not in line:
        if roman_idx < len(roman_list):
            match = re.search(r'(with st\.expander\("Section \d+\.\d+\.\d+\s+Section ).*?("\):)', line)
            if match:
                line = match.group(1) + roman_list[roman_idx] + match.group(2) + "\n"
                roman_idx += 1
                
    new_lines.append(line)

with open('chapter3.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Replaced {roman_idx} roman numerals.")

import re

with open('chapter3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith('with st.expander("Section 3.'):
        line = '        ' + line
    new_lines.append(line)

with open('chapter3.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

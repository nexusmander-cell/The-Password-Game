import re

Pattern1 = r'\b[A-ZÀ-Ỹ][a-zà-ỹ]*\b'

text = "Hôm nay trời Đẹp. Tôi sẽ Đi học Python ở Aptech."

match = re.findall(Pattern1, text)

print(match)
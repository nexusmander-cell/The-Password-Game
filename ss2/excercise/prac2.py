import re

emails = ["hung.ngo@gmail.com", "teacher@fpt.edu.vn", "user123@yahoo.com"]

pattern = r'@([\w\.-]+)'

for i in emails:
    match = re.search(pattern, i)
    if match:
        print(match)
    else:
        print("No match")


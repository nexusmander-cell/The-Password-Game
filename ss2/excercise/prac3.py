import re

sample = "Hôm nay học #Python, mai học #Regex và #MachineLearning"

pattern = r'#\w+'

match = re.findall(pattern, sample)

print(match)
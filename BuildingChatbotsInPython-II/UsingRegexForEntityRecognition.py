import re

pattern = re.compile('[A-Z]{1}[a-z]*')
message = """Mary is a friend of mine, she studied at Oxford and now works at Google"""
print(pattern.findall(message))
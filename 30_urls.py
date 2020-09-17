import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# group 0 is entire thing, group 1,2,3 references ()
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

# previous line creates a pattern. Below is using that pattern
# to substitute out group 2 and 3 for all matches in url
subbed_urls = pattern.sub(r"\2\3", urls)

print(subbed_urls)

matches = pattern.finditer(urls)

# for match in matches:
# print(match.group(3))

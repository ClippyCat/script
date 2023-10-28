import requests

TOKEN = "DF5A4A7E6CB90704"
DOMAINS = [
  "villagevote.clippycat.ca",
]
USERNAME = "taithoyem"

# NO LONGER CONFIG

TLD = DOMAINS[0].split(".")[-1] # can only update one TLD at a time
URL = f"https://{USERNAME}:{TOKEN}@api.cp.easydns.com/dyn/generic.php"

for domain in DOMAINS:
  resp = requests.get(URL, {"hostname": domain, "TLD": TLD})
  code = resp.status_code
  content = str(resp.content)
  print(f"CODE: {code}:\n{content}")

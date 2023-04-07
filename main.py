import json
import requests

# --- Enroll Test --- #
myenroll = {"username": "ffwatcharin", "refcode": "HARD001"}
print(myenroll)
x = requests.post("http://localhost:8000/addcart", data=json.dumps(myenroll))
print(x)
y = requests.get("http://localhost:8000/cart")
print(y)

import requests

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY4OTA2NjI4MywiaWF0IjoxNjg5MDYyNjgzLCJqdGkiOiIwN2ZhNmMwOS0xOGQ0LTQyNjQtYTlhYi1mOTY3YWYyMDFjOWMiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.Po6vgDeL1JLL2BM_MhOhfQfU5N8pYqNHiJsJRoAe1IvtODdOVNvyVkgLgz8T1II-QlpREV5ee0w6o5nbw1a3FLTN0PhKvZFJ_O16A611sNGIHHQYcYFB-jivsSmmLC5pJMcPeiIA4ZGfrmjZwxRDXvy7rh_QH1iJI9i1vE07nmpO0weI-QrkgI5FK3yelcJwgR_3llUaUVRI-WoBAGUgzyO0-iXz03FnLsS-xYnAQz1caIUh6PNM36mMbkkkHzP1BKmcbCudrToMJ0eWZpzf7XZaaJMHZM5nrhKem2bVlWJ7XkrUseVGEluWkn6ZcjYqpD2TdomsEINeY77NOaO0Tg'
}

response = requests.request("GET", url,verify = False, headers=headers, data=payload)

raw_data = json.loads(response.text)
devices = raw_data["response"]

for device in devices:
  print("Hostname: {}".format(device["hostname"]))
  print("Family: {}".format(device["family"]))
  print("Manajemen Ip Addres: {}".format(device["managementIpAddress"]))
  print("Type: {}".format(device["type"]))
  print("MacAddres: {}".format(device["macAddress"]))
  print("platformId: {}".format(device["platformId"]))


import requests

url = "http://192.168.12.110:4040/portal/scrapper/sisben/afiliados-sisben"
response = requests.get(url)
if response.status_code == 200:
    print ("Success!")
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
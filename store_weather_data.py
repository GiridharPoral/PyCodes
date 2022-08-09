import http.client
import json # import JSON module

conn = http.client.HTTPSConnection("api.openweathermap.org")
payload = ''
headers = {}
# URL is requested
conn.request("GET", "/data/2.5/weather?q=Bengaluru&appid=8b673d823b7d2fc9fe8b1858b3e5694d", payload, headers)
res = conn.getresponse()
data = res.read()
weather_data = json.loads(data.decode("utf-8"))


with open("weather_report.txt","w") as f: # create a new text file
    f.write(f"""The weather details of {weather_data["name"]} are:\n""")

with open("weather_report.txt","a") as fb: # write the data to the existing text file
    fb.write(f"""the co-ordinates of {weather_data["name"]} are:\n""")
    # Longitude & Latitude of the place
    fb.write(f"""\t{weather_data["coord"]["lon"]} longitude & {weather_data["coord"]["lon"]} latitude""")
    # Temperature of the place
    fb.write(f"""\n\nTemperature of {weather_data["name"]} is """)
    fb.write(str(round(weather_data["main"]["temp"]-273,2)))
    # Humidity of the place
    fb.write(f"""\n\nHumidity of {weather_data["name"]} is """)
    fb.write(str(weather_data["main"]["humidity"]))

with open("weather_report.txt","r") as f: # read the contents of the file in iDLE Shell
    data_read = f.read()
    print(f"""the weather report present in file for {weather_data["name"]} is \n\n{data_read}""")

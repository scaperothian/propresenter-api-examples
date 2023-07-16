import requests
import time

hostname = "localhost"
port = "1025"

if __name__ == "__main__":
    pause_time = 0.5
    while True:
        for s in [0,1,2,3]:
            # try to cycle through the presentation from slide 1 to 4 pausing for 0.1 seconds
            # v1/doc/index.html#/Presentation/presentationActiveCueTrigger
            url = "http://"+hostname+":"+port+"/v1/presentation/active/"+str(s)+"/trigger"

            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for any 4XX or 5XX status codes
            except requests.exceptions.RequestException as e:
                print("Error:", e)

            time.sleep(pause_time)
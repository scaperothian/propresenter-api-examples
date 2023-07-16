import requests
import time

# takes a playlist and if PP7 is not actively on that presentation,
# then the API will be used to bring it into 'focus.'


hostname = "localhost"
port = "1025"
playlist_to_be_found = "Service"

if __name__ == "__main__":
    # try to cycle through the presentation from slide 1 to 4 pausing for 0.1 seconds
    # v1/doc/index.html#/Playlist/playlistGetAll
    url = "http://"+hostname+":"+port+"/v1/playlists?chunked=false"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any 4XX or 5XX status codes
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

    print(data)
    playlist_id = ''
    for item in data:
        if item['id']['name']==playlist_to_be_found:
            playlist_id = item['id']['uuid']
    print(f"playlist id = {playlist_id}\n")

    # focus on the specific playlist on the UI
    url = "http://"+hostname+":"+port+"/v1/playlist/"+playlist_id+"/focus"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any 4XX or 5XX status codes
    except requests.exceptions.RequestException as e:
        print("Error:", e)

    # find all items in specific playlist
    url = "http://"+hostname+":"+port+"/v1/playlist/"+playlist_id

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any 4XX or 5XX status codes
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    print(data)

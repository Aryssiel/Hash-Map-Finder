import urllib.request
import time
import json
import webbrowser
word = ' - '
def findIt(linea):
    URL = urllib.request.urlopen("https://osu.ppy.sh/api/get_beatmaps?k=//Your API key here//&h="+linea).read().decode('utf-8')
    res = json.loads(URL)
    b_id = res[0]['beatmapset_id']
    d_id = res[0]['beatmap_id']
    webbrowser.open("https://osu.ppy.sh/beatmapsets/"+b_id+"#fruits/"+d_id)
    return
with open(r'//Directory where the .txt file is//', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if word in line:
            linea = line.split(word, 1)[1]
            findIt(linea)
            input("Press anything to continue.")

import requests
from bs4 import BeautifulSoup
import re
import googletrans

translator = googletrans.Translator()

def get_ecomonicdata():
    url = 'https://rili.jin10.com/day/'
    headers = {'user-agent': 'Mozilla/5.0'}
    r= requests.get(url,headers=headers).text

    soup = BeautifulSoup(r,'html.parser')

    incident_data = soup.find_all(class_='jin-table-row')
    time=[]
    name=[]
    important=[]
    former_value=[]
    perdictive_value=[]
    published_value=[]
    for i in incident_data:
        if(i.find(class_="data-name-text")==None):
            break
        t =  i.find(class_="cell").text
        t = re.sub("[\n\t\s ]","",t)
        time.append(t)
        n = i.find(class_="data-name-text").text
        n = re.sub("[\n\t\s ]","",n)

        name.append(n)
        im = i.find(class_="cell important is-important")
        if(im==None):
            important.append(False)
        else:
            important.append(True)
        value = i.find_all(style="text-align:right;")
        for j in range(len(value)):
            s = value[j].text
            s = re.sub("[\n \t\s]","",s)
            if j == 0:
                former_value.append(s)
            elif j==1:
                perdictive_value.append(s)
            else:
                published_value.append(s)
    for i in range(len(time)):
        if(time[i]==""):
            time[i] = time[i-1]
    data_string =""

    for i in range(len(time)):
        if(important[i]==False):
            continue
        beauty_name=translator.translate(name[i],dest='zh-tw').text
        data_string = data_string +"**" +time[i] +"**"+" "+beauty_name +"\n"+"=========="+"\n"
    return data_string
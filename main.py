import requests



def main():

    apiKey="Paste ur api key here"
    bassUrl="http://api.openweathermap.org/data/2.5/weather?"
    city=input("Enter A city Name:")
    url=bassUrl +"appid=" + apiKey + "&q=" + city
    response=requests.get(url).json()
    if len(response)==2:
        print(response['message'])
    temp=response['main']['temp']
    feels_like=response['main']['feels_like']
    desc=response['weather'][0]['description']
    print("Temprature: "+str(temp)+" Feels Like:"+str(feels_like)+" Weather Description: "+desc)




if __name__=="__main__":
    main()

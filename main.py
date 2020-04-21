import speech_recognition as sr
from googlesearch import search
import webbrowser

r = sr.Recognizer()

wordCap = 'Look up'
wordLow = 'look up'

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)
    
    try:    
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        if((wordCap in '{}'.format(text)) or (wordLow in '{}'.format(text))):
            ind = ('{}'.format(text)).find(wordCap) + 8
            ind = ('{}'.format(text)).find(wordLow) + 8
            sent = ('{}'.format(text))[ind:len(('{}'.format(text)))]
            print(sent)
            # for j in search(sent, tld="co.in", num=10, stop=5, pause=2): 
            #     print(j)
            webbrowser.open_new_tab("http://google.com/?#q=" + sent)
    except:
        print('Bitch speak English')
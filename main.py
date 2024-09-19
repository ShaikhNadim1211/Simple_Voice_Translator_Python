import googletrans
import speech_recognition
import gtts
import playsound
import os
import win32com.client
import time
languages = {'ar': 'Arabic',
             'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian',
             'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish','fr': 'French',
             'gu': 'Gujarati', 'hi': 'Hindi','id': 'Indonesian',
             'it': 'Italian','ja': 'Japanese','kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin',
             'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
             'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian',
             'sq': 'Albanian', 'sr': 'Serbian','ta': 'Tamil', 'te': 'Telugu',
             'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
             'zh-tw': 'Chinese'}
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takecommand(ln):
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        voice = recognizer.listen(source)
        try:
            text=recognizer.recognize_google(voice,language=ln)
            print(text)
            return text
        except Exception as e:
            return "Not identify Please Say Again"
def takecommand1():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        voice = recognizer.listen(source)
        try:
            text=recognizer.recognize_google(voice,language="en")
            return text
        except Exception as e:
            return "Not identify Please Start Again"

if __name__ == '__main__':
    try:
        start_time=time.time()
        firstlanguage = ""
        secondlanguage=""
        start = googletrans.Translator()
        startt = start.translate("Please say the first language", dest="hi")
        print(startt.text)
        converted_message = gtts.gTTS(startt.text, lang="hi")
        converted_message.save("message.mp3")
        playsound.playsound("message.mp3")
        os.remove("message.mp3")
        t = takecommand1()
        print(t)
        if (t == "Not identify Please Start Again"):
            startt = start.translate("Language Not Available", dest="en")
            print(startt.text)
            converted_message = gtts.gTTS(startt.text, lang="en")
            converted_message.save("message.mp3")
            playsound.playsound("message.mp3")
            os.remove("message.mp3")
            print("___________________________________________________________________________________________________________________________________________")
            exit()
        else:
            for i, j in languages.items():
                if j.lower() in t.lower():
                    firstlanguage = i
            if(firstlanguage==""):
                startt = start.translate("Language Not Available", dest=firstlanguage)
                print(startt.text)
                converted_message = gtts.gTTS(startt.text, lang=firstlanguage)
                converted_message.save("message.mp3")
                playsound.playsound("message.mp3")
                os.remove("message.mp3")
                print("___________________________________________________________________________________________________________________________________________")
                exit()

            start = googletrans.Translator()
            startt = start.translate("Please say the second language", dest="en")
            print(startt.text)
            converted_message = gtts.gTTS(startt.text, lang="en")
            converted_message.save("message.mp3")
            playsound.playsound("message.mp3")
            os.remove("message.mp3")
            t = takecommand1()
            print(t)
            if (t == "Not identify Please Start Again"):
                startt = start.translate("Please Start Again", dest="en")
                print(startt.text)
                converted_message = gtts.gTTS(startt.text, lang="en")
                converted_message.save("message.mp3")
                playsound.playsound("message.mp3")
                os.remove("message.mp3")
                print("___________________________________________________________________________________________________________________________________________")
                exit()
            else:
                for i, j in languages.items():
                    if j.lower() in t.lower():
                        secondlanguage = i
                if (secondlanguage == ""):
                    startt = start.translate("Please Start Again", dest=firstlanguage)
                    print(startt.text)
                    converted_message = gtts.gTTS(startt.text, lang=firstlanguage)
                    converted_message.save("message.mp3")
                    playsound.playsound("message.mp3")
                    os.remove("message.mp3")
                    print("___________________________________________________________________________________________________________________________________________")
                    exit()
        while True:
            startt = start.translate("Sentence is Listening", dest=firstlanguage)
            print(startt.text)
            converted_message = gtts.gTTS(startt.text, lang=firstlanguage)
            converted_message.save("message.mp3")
            playsound.playsound("message.mp3")
            os.remove("message.mp3")
            t2 = takecommand(firstlanguage)
            if(t2=="Not identify Please Say Again"):
                startt=start.translate("Please Say Again",dest=firstlanguage)
                print(startt.text)
                converted_message=gtts.gTTS(startt.text,lang=firstlanguage)
                converted_message.save("message.mp3")
                playsound.playsound("message.mp3")
                os.remove("message.mp3")
                print("___________________________________________________________________________________________________________________________________________")
            else:
                translator = googletrans.Translator()
                translation = translator.translate(t2, dest=secondlanguage)
                print(translation.text)
                converted_audio = gtts.gTTS(translation.text, lang=secondlanguage)
                converted_audio.save("voice.mp3")
                end_time = time.time()
                print(end_time - start_time)
                playsound.playsound("voice.mp3")
                os.remove("voice.mp3")
    except Exception as ex:
        networkissue = str(ex)
        if ("[Errno 11001] getaddrinfo failed" in networkissue):
            print("Network Issue Occur")
        else:
            print("Error Occured "+ex.__str__())

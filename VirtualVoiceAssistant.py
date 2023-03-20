import pyttsx3
import speech_recognition as sr
import openai

openai.api_key = "Your API Key"    # Enter your API key from your OpenAI account

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"User said: {query}\n ")

        except Exception as e:
            print(e)
            print("say that again please...")
            return "NULL"
        return query
    
    
def chatgpt(query):
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Virtual Assistant "},
            {"role": "user", "content": query },
                 ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content
    
            print(result)
            speak(result)


while(1):
    query = takecommand().lower()  #comment this line and
    #query = " hi I am Jack"       # Uncomment this if you want to give written instructions
    if 'hello' in query:
        query = query.replace("hello", "")
        chatgpt(query)
    elif 'hi' in query:
        query = query.replace("jarvis", "")
        chatgpt(query)
        






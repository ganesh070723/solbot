from django.shortcuts import render
import openai
import speech_recognition as sr
import json
import pyttsx3
openai.api_key = "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"
# Create your views here.
def index(request):
    arr=[]
    if request.method == 'POST':
        if request.POST.get('search') != '':
          name = request.POST.get('search')
          def generate_response(prompt):
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5
            )
            return response.choices[0].text
          
        user_input = name
        # user_input = 0
        # r = sr.Recognizer()
        #
        # with sr.Microphone() as source:
        #     print("Please say something: ")
        #     audio = r.listen(source)
        # try:
        #     text = r.recognize_google(audio)
        #     user_input = text
        #     # print("You said: ", text)
        # except:
        #     pass
        prompt = f"User: {user_input} Bot: "
        bot_response = generate_response(prompt)

        # engine = pyttsx3.init()
        #
        # # Set the voice and rate
        # engine.setProperty('voice', 'en-us')
        # engine.setProperty('rate', 150)
        #
        # # Speak the text
       
        arr.append(bot_response)
        print("GPT: " + bot_response)
        # engine.say(bot_response)
        # engine.runAndWait()
        context ={
            'results': arr,
            'question': name,
        }
    if len(arr)>0:
        return render(request,'index.html',context)
    else:
       return render(request,'index.html')
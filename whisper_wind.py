import pyttsx3
engine = pyttsx3.init()
print("Welcome to Whisper Wind")
while True:
   message = input("Enter what do you want to speak: ")
   if (message == "q"):
     engine.say("Bye and take care of yourself")
     engine.runAndWait()
     break
   engine.say(message)
   engine.runAndWait()

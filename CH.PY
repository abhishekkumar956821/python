#question:answer
import time
now = time.ctime()
qna = {
    "hii":"hey! how can i help you?",
    "how are you?":"I am fine",
    "what is your name?":"my name is Chatbot",
    "how old are you?":"Maybe enough to answer your questions",
    "do you have emotions?":"no, i am a robot,I don't have emotions",
    "what do you want to eat?":"I am a robot i can't eat,but thankyou for asking",
    "what is the time now?":now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
      print(qna[qs])
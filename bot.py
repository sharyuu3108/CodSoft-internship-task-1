import random
from datetime import datetime

class DoraBot:
    def __init__(self):
        self.name = ""
    def greet(self):
        self.name = input("Hi!What is your name? How can I assist you today?")
        print(f"Hi {self.name}, I'm DoraBot!")
    def get_day(self):
        # Gets the current day of the week
        now = datetime.now()
        return now.strftime("%A")
    def get_flute_info(self):
        # Provides general information about the flute
        return (
            "The flute is a popular woodwind instrument known for its sweet,gentle sound. \n Unlike other woodwind instruments, the flute does not have a reed. "
            "It produces sound by directing air across an opening. \n A musician who plays flute is called a flautist or flutist.\n"
           "The flute is used in various genres including classical,jazz,folk,pop,rock.Do you have any specific question about flute?"
        )
    def get_flute_types(self):
        # Provides information about different types of flutes
        return (
            "There are several types of flutes, including:\n"
            "Western concert flute\n"
            "Piccolo\n"
            "Alto flute\n"
            "Bass flute\n"
            "Bamboo flute\n"
        )
    def get_flute_playing_tips(self):
        # Provides tips for playing the flute
        return (
            "Here are some tips for playing the flute:\n "
            "Posture: Sit or stand up straight with your shoulders relaxed.\n"
            "Breathing: Use your diaphragm to control the airflow. Practice long, steady notes to improve breath support.\n "
            "Embouchure: The position of your lips is crucial for producing a good sound. Practice your embouchure regularly.\n"
            "Practice: Regular practice is key to improving your technique and tone.\n"
            "Finger exercises: Develope finger independence and strength for easy playing.\n"
            "Seek guidanace: Take lessons from a flute teacher to improve yourself.\n"
        
        )
    def get_flute_famous_flutists(self):
        # Provides names of famous flutist
        return(
            "Here are some famous flutists in India:\n"
            "1.Hariprasad Chaurasiya: A renowned classical flutist and composer,known for his soulful performances.\n"
            "2.Pandit Ronu Majumdar: A leading flutist in Indian Classical Music,recongnised for his technical mastery and emotional depth.\n"
            "3.Vijay Raghav Rao: A flutist and composer known for his work in Indian classical,folk,and fusion music.\n"
            "4.Rakesh Chaurasiya: A flutist known for his innovative and fusion style flute playing.\n"
            "5.Shashank Subramanyam: A carnatic flutist and composer celebrated for his technical virtuosity and musicality.\n"
            "These musicians have contributed significantly to the world of Indian classical music and helped to popularize the flute globally.\n"
        )
    def get_flute_notes(self):
        #if user asks for flute notes for a song
        return(
            "I'm unable to provide you with flute notes for any particular song as I don't have access to that specific information.However I can suggest some alternatives to help you find flute notes:\n"
            "1.Check online music sheets or explore websites such as Musicnotes,MuseScore.\n"
            "2.Look for flute tutorials on YouTube or other platforms.\n"
            "3.Reach out a music teacher or a proffesional flutist who can help you with the notes.\n"
            "4.Try using music notation software or apps such as Sibelius or Finale to create or find the notes.\n"
            "Do you have more questions about flute?\n"
        )
    def chat(self):
        while True:
            user_input = input("You: ").strip().lower()  # Strip whitespace and convert to lowercase
            if user_input in ["quit", "exit", "bye","goodbye","farewell"]:
                print("Goodbye! It was nice chatting with you.Have a great day!")
                break
            elif user_input in ["hello", "hi","hey"]:
                print("Hi! How are you?")
            elif user_input in ["i'm good","i am good","i am fine","i am doing well","great"]:
                print("That's great to hear!")
            elif user_input in ["how are you?", "how are you doing"]:
                print("I'm good, thanks! How about you? How can I help you with?")
            elif user_input in ["what's your name", "who are you"]:
                print(f"I'm DoraBot, your virtual friend! Do you have anything to share with me or do you want to know about anything?")
            elif "day" in user_input:
                day_of_week = self.get_day()
                print(f"Today is {day_of_week}.")
            elif user_input in ["can you help me?","i need some help"]:
                print("I can help you with requied information. Try asking me something about flute!")
            elif user_input in ["thanks", "thank you"]:
                print("You're welcome!")
            elif user_input == "ok":
                print("Got it! If you need anything to help with, just let me know.")
            elif "flute" in user_input:
                if "what is a flute" in user_input or "describe the flute" in user_input or "tell me about flute" in user_input or "information of flute" in user_input:
                    print(self.get_flute_info())
                elif "what are types of flutes?" in user_input or "types of flutes" in user_input or "different flutes" in user_input:
                    print(self.get_flute_types())
                elif "how to play the flute?" in user_input or "flute playing tips" in user_input:
                    print(self.get_flute_playing_tips())
                elif "who are famous flutists in india?" in user_input or "famous flute players" in user_input or "famous flutists of india" in user_input:
                    print(self.get_flute_famous_flutists())
                elif "Suggest some songs with flute notes" in user_input or "Give me flute notes of Happy Birthday song." in user_input or "flute notes" in user_input:
                    print(self.get_flute_notes())
                else:
                    print("I can tell you about the flute, its types, or how to play it. What would you like to know?")
            else:
                responses = [
                    "I didn't understand that.",
                    "Sorry! I am unable to understand that.",
                    "Do you me to help you with something?"
                ]
                print(random.choice(responses))

bot= DoraBot()
bot.greet()
bot.chat()

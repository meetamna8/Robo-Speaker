import os
import pyttsx3

if __name__ == '__main__':
    while True:
        print("Welcome to the RoboSpeaker 1.1. Created by Amna")
        text = input("Enter What You Want Me To Speak: ")
        if text == 'q':
            break

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Speak the entered text
        engine.say(text)

        # Wait for the speech to complete
        engine.runAndWait()
        






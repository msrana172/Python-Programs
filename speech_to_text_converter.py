import pyaudio
import speech_recognition as sr
import pickle
def main():
    # initialize the recognizer
    r = sr.Recognizer()

    # Reading the data from the default microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something you want: ")
        audio_data = r.listen(source)
        print("Recognizing Now .... ")
        
        # recognize speech using google
        text = r.recognize_google(audio_data)
        try:
            print("You have said \n" + text)
            print("Audio Recorded Successfully.\n ")


        except Exception as e:
            print("Error, Please try again : " + str(e))

        # write audio

        with open("C:\\MyData\\Python_Data\\Python_Projects\\recorded.wav", "wb") as f:
            f.write(audio_data.get_wav_data())

        # with open('C:\\MyData\\Python_Data\\Python_Projects\\model.pkl', 'wb') as f:
        #     pickle.dump(text, f)

if __name__ == "__main__":
    main()
    

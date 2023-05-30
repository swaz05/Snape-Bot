import speech_recognition as sr #speech recognition module 
import pyttsx3 #text-to-speech module 
import pywhatkit #module to perform actions like playing music on youtube 
import datetime #module to get current date and time
import wikipedia #module to search informations on wikipedia
import pyjokes #module to generat ejokes
import webbrowser #module to open web browser for google search

listener = sr.Recognizer() # Creating recognizer object
engine = pyttsx3.init()  # Creating text-to-speech object
voices = engine.getProperty('voices') #getting the list of available voices
engine.setProperty('voice', voices[1].id) # Setting female voice as default
     
# Function for text-to-speech conversion     
def talk(text):
    engine.say(text) #say method to convert text to speech
    engine.runAndWait() #launching the speech engine and playing the output in speech
    
# Function for taking user command using microphone input
def take_command():
    try:
        with sr.Microphone() as source: #microphone as the input source of audio
            print('listening...')
            voice = listener.listen(source) #using the listen method of the Recognizer class to capture audio
            command = listener.recognize_google(voice) #using the Google Web Speech API to recognize the speech input
            command = command.lower()
            if 'snape' in command:
                command = command.replace('snape', '')
                print(command)
    except:
        pass
    return command

# Function for processing user commands and generating responses

def run_snape(): #defining the function that contains the commands to be executed by snape
    command = take_command() #calling the take_command function 
    print(command)

#checking if the command is to play a song on YouTube
    if 'play' in command: 
        song = command.replace('play', '') #extracting the name of the song to be played
        talk('playing ' + song) 
        pywhatkit.playonyt(song) #using the playonyt method to play the song on YouTube

    # If user wants to know current time
    elif 'time' in command:  
        time = datetime.datetime.now().strftime('%I:%M %p') #using strftime method to get the time in a particular format
        print(time)
        talk('Current time is ' + time) #converting the text to speech and saying the time

# If user wants to know current date
    elif 'date' in command: 
        date = datetime.datetime.now().strftime('%d /%m /%Y') 
        print(date)
        talk("Today’s date " + date) #converting the text to speech and saying the date
    
# If user wants to search for a person on Wikipedia
    elif 'who is' in command: 
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1) #getting a summary of the person's information from Wikipedia
        print(info) 
        talk(info)
    
# If user wants to search on Google
    elif 'search' in command: 
        query = command.replace('search', '')
        talk('searching for ' + query) # Using pywhatkit to search the query on Google
        pywhatkit.search(query)

 # If user wants to open Google Maps
    elif 'open google map' in command:
        talk('Opening Google Map')
        webbrowser.open(f'https://www.google.com/maps/') # Using webbrowser to open Google Maps

# If user asks how is the assistant doing
    elif 'how are you' in command: 
         print('I am fine, how about you')
         talk('I am fine, how about you')
        
# If user asks assistant's name
    elif 'what is your name' in command:  
        print('I am Snape, What can I do for you?')
        talk('I am Snape, What can I do for you?')

# If user wants a joke
    elif 'joke' in command: 
        talk(pyjokes.get_joke()) #pyjokes library to get a joke
        
# If user wants to open netflix
    elif 'open netflix' in command:
        webbrowser.open('https://www.netflix.com/')
        talk('Opening Netflix')
        
    elif 'search movie on netflix' in command: 
        movie = command.replace('search movie','') #extracts the movie name from the command
        search_url = f'https://www.netflix.com/search?q={movie}' #creates the URL for Netflix search
        webbrowser.open(search_url) #opens the URL in default browser
    
#prompts user to repeat the command if none of the predefined commands are detected
    else:
        talk('Please say the command again.')
#keeps the program running continuously to listen for user input
while True:
    run_snape()
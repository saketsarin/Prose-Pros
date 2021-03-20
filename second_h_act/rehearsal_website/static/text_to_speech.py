import pyttsx3
#In case there are three roles
# role_choosen  = role user has selected
# role_1 and role_2 will the other two roles 
role_1 = pyttsx3.init()
role_2 = pyttsx3.init()

role_1.setProperty('rate', 300)
role_2.setProperty('rate', 300)

role_1.setProperty('volume', 1.0)
role_2.setProperty('volume', 1.0)

role_1.setProperty('voice', voices[0].id) #male voice
role_2.setProperty('voice', voices[1].id) #female voice

## play -> list of scenes  
#### each scene is seperated with ---------
## scene -> {'mood' : '---', 'time' : '--:--','roles':[] ##list of roles,'script' : [,,,]list of dialogues }
## dialogue -> character : dialogue_character ###

scene_selected = input("enter scene number : ")
character_selected = input("enter character ")
other_characters = [i for i in scene['roles'] if i!=character_selected ]

#role_1 --> other_character[0]
#role_2 --> other_character[1]
#map_voice [other_character[0]: role_1, other_character[1] : role_2]

scene_selected_script = scene['script']
for dialogue in scene_selected_script:
    speaker, rest = dialogue.split(":")
    if speaker == other_character[0]:
        role_1.say(rest)
        role_1.runAndWait()
        role_1.stop()
    elif speaker == other_character[1]:
        role_2.say(rest)
        role_2.runAndWait()
        role_2.stop()

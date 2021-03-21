import pyttsx3
import time
filename = "script.txt"
characterList = []
eachLine = []
currentScene = ""
currentSetting = ""

with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    if "+" in line:
        genderMatch = line.split("+")
        for i in range(len(genderMatch)):
            genderMatch[i] = genderMatch[i].strip()
        characterList.append(genderMatch)
    if "#" in line:
        sceneSplit = line.split("#")
        for i in range(len(sceneSplit)):
            sceneSplit[i] = sceneSplit[i].strip()
        currentScene = sceneSplit[0]
        currentSetting = sceneSplit[1]
    if "*" in line:
        charAndLine = line.split("*")
        for x in range(len(charAndLine)):
            charAndLine[x] = charAndLine[x].strip()
        charAndLine.append(currentScene)
        charAndLine.append(currentSetting)
        eachLine.append(charAndLine)

# print(characterList)
# [['Sir Chancelot', 'm'], ['Squire', 'f'], ['Dragon', 'f']
# print(eachLine[0])
#['Sir Chancelot', 'Ha! I will slay this dragon now, for the sake of the people!', 'Scene 1', 'day']


# the lists in characterList are [character name, voice gender] for each character
# the lists in eachLine are [character name, the line, and scene number] for every line
play = {}  # dict of scenes
# scene -> {'mood' : '---', 'time' : '--','roles':[] ##list of roles,'script' : [,,,]list of dialogues }
## dialogue -> character : dialogue_character ###
for line in eachLine:
    dialogue = {}
    dialogue['charname'] = line[0]
    dialogue['line'] = line[1]
    curr_scene = str(line[-2])
    if curr_scene not in play:
        scene = {}
        scene['time'] = line[-1]
        scene['roles'] = [line[0]]
        scene['name'] = line[-2]
        scene['dialogue_list'] = [dialogue]
        play[line[-2]] = scene

    else:

        play[line[-2]]['roles'].append(line[0])
        play[line[-2]]['dialogue_list'] .append(dialogue)

#print(play['Scene 6'])

scene_selected = input("enter scene: ")
scene_selected_play = play[scene_selected]
character_selected = input("enter character: ")
other_characters = [i for i in scene['roles'] if i != character_selected]

if(len(other_characters) == 2):

    role_1 = pyttsx3.init()
    role_2 = pyttsx3.init()

    role_1.setProperty('rate', 150)
    role_2.setProperty('rate', 150)

    role_1.setProperty('volume', 1.0)
    role_2.setProperty('volume', 1.0)
    voices = role_1.getProperty('voices')
    role_1.setProperty('voice', voices[0].id)  # male voice
    role_2.setProperty('voice', voices[1].id)  # female voice

    scene_selected_script = scene_selected_play['dialogue_list']
    for dialogue in scene_selected_script:
        speaker = dialogue['charname']
        rest = dialogue['line']
        if speaker == other_characters[0]:
            role_1.say(rest)
            role_1.runAndWait()
            role_1.stop()
        elif speaker == other_characters[1]:
            role_2.say(rest)
            role_2.runAndWait()
            role_2.stop()
        else:
            time.sleep(10)

else:
    role_1 = pyttsx3.init()
    role_1.setProperty('rate', 150)
    role_1.setProperty('volume', 1.0)
    voices = role_1.getProperty('voices')
    role_1.setProperty('voice', voices[0].id)
    scene_selected_script = scene_selected_play['dialogue_list']
    for dialogue in scene_selected_script:
        speaker = dialogue['charname']
        rest = dialogue['line']
        if speaker == other_characters[0]:
            role_1.say(rest)
            role_1.runAndWait()
            role_1.stop()
        else:
            time.sleep(10)

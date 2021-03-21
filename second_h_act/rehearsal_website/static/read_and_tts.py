import pyttsx3
import time
from second_h_act.settings import BASE_DIR
import os

#filename = "script.txt"
characterList = []
eachLine = []
currentScene = ""
currentSetting = ""

def saveAudio(filepath, sceneNum, characterNum):
    with open(filepath) as f_obj:
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

    #print(characterList)
    #[['Sir Chancelot', 'm'], ['Squire', 'f'], ['Dragon', 'f']
    #print(eachLine[0])
    #['Sir Chancelot', 'Ha! I will slay this dragon now, for the sake of the people!', 'Scene 1', 'day']


    # the lists in characterList are [character name, voice gender] for each character
    # the lists in eachLine are [character name, the line, and scene number] for every line
    play = {} # dict of scenes
    ### scene -> {'mood' : '---', 'time' : '--','roles':[] ##list of roles,'script' : [,,,]list of dialogues }
    ## dialogue -> character : dialogue_character ###
    for line in eachLine:
        dialogue = {}
        dialogue['charname'] = line[0]
        dialogue['line']= line[1]
        curr_scene = str(line[-2])
        if curr_scene not in play:
            scene ={}
            scene['time'] = line[-1]
            scene['roles'] = [line[0]]
            scene['name'] = line[-2]
            scene['dialogue_list'] = [dialogue]
            play[line[-2]] = scene

        else:
            
            play[line[-2]]['roles'].append(line[0])
            play[line[-2]]['dialogue_list'] .append(dialogue)
        
    #print(play['Scene 6'])

    scene_selected = 'Scene ' + str(sceneNum) #input("enter scene: ")
    scene_selected_play = play[scene_selected]
    character_selected = characterList[characterNum][0] #input("enter character: ")
    other_characters = [i for i in scene['roles'] if i!=character_selected ]
    audioPath = os.path.join(BASE_DIR, 'rehearsal_website\static\scriptAudio')
    audioNum = 0
    
    if(len(other_characters) == 2):

        role_1 = pyttsx3.init()
        role_2 = pyttsx3.init()

        role_1.setProperty('rate', 150)
        role_2.setProperty('rate', 150)

        role_1.setProperty('volume', 1.0)
        role_2.setProperty('volume', 1.0)
        voices = role_1.getProperty('voices')
        role_1.setProperty('voice', voices[0].id) #male voice
        role_2.setProperty('voice', voices[1].id) #female voice

        scene_selected_script = scene_selected_play['dialogue_list']
        for dialogue in scene_selected_script:
            speaker = dialogue['charname']
            rest = dialogue['line']
            linePath = os.path.join(audioPath, str(sceneNum) + '_' + str(audioNum) + '.mp3')
            audioNum += 1
            if speaker == other_characters[0]:
                role_1.save_to_file(rest, linePath)
                role_1.runAndWait()
                role_1.stop()
            elif speaker == other_characters[1]:
                role_2.save_to_file(rest, linePath)
                role_2.runAndWait()
                role_2.stop()
            #else: 
                #time.sleep(30) #delay must be moved to html, but audioNum still increments regardless
        

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
            linePath = os.path.join(audioPath, str(sceneNum) + '_' + str(audioNum) + '.mp3')
            audioNum += 1
            if speaker == other_characters[0]:
                role_1.save_to_file(rest, linePath)
                role_1.runAndWait()
                role_1.stop()
            #else: 
                #time.sleep(30) #delay must be moved to html, but audioNum still increments regardless

    return audioNum

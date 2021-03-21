from django.shortcuts import render
from rehearsal_website.forms import RehearsalForm
from rehearsal_website.static import read_and_tts
from second_h_act.settings import BASE_DIR
import os

def mainPage(request):
    return render(request, 'index.html', {})


def submit(request):
    sceneNum = 0
    character = 0

    if request.method == "POST":
        print(request.POST)
        myForm = RehearsalForm(request.POST)

        if myForm.is_valid():
            print(myForm.cleaned_data)
            sceneNum = myForm.cleaned_data['sceneNum']
            character = myForm.cleaned_data['character']
            scriptPath = os.path.join(BASE_DIR, 'rehearsal_website\static\script.txt')
            maxNumAudio = read_and_tts.saveAudio(scriptPath, sceneNum, character)

            return render(request, 'play.html', {"sceneNum": sceneNum, "character": character, "maxAudio":maxNumAudio, "scriptPath":scriptPath})
        else:
            print('error: invalid form')

    else:
        myForm = RehearsalForm()

    return render(request, 'index.html', {})

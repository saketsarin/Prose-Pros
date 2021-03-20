from django.shortcuts import render
from rehearsal_website.forms import RehearsalForm


def mainPage(request):
    return render(request, 'index.html', {})


def submit(request):
    sceneNum = 0

    if request.method == "POST":
        print(request.POST)
        myForm = RehearsalForm(request.POST)

        if myForm.is_valid():
            #print(myForm.cleaned_data)
            sceneNum = myForm.cleaned_data['sceneNum']
            #character = myForm.cleaned_data['character']
        else:
            print('error: invalid form')

    else:
        myForm = RehearsalForm()

    return render(request, 'play.html', {"sceneNum": sceneNum, "character": 'test'})#character})

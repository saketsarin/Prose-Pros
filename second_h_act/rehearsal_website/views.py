from django.shortcuts import render
from rehearsal_website.forms import form


def mainPage(request):
    return render(request, 'index.html', {})


def submit(request):
    sceneNum = 0

    if request.method == "POST":
        myForm = form(request.POST)

        if myForm.is_valid():
            sceneNum = myForm.cleaned_data['sceneNum']
            character = myForm.cleaned_data['character']

    else:
        myForm = form()

    return render(request, 'play.html', {"sceneNum": sceneNum, "character": character})

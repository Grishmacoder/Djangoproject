from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def page1(request):
    djtext = request.POST.get('Text', 'default')
    captext = request.POST.get('check1', 'off')
    chkpunc = request.POST.get('check2', 'off')
    rmvnwline = request.POST.get('check3', 'off')

    if captext == 'on':
        result = ""
        for char in djtext:
            result = result + char.upper()

        params = {'page1txt': 'capitalized Text', 'aftertxt': result}
        djtext = result

    if chkpunc == "on":
        punc = "!,?:""-_()[]{}."
        result = ""
        for char in djtext:
            if char not in punc:
                result = result + char
        params = {'page1txt': 'Removed Punchuation', 'aftertxt': result}
        djtext = result

    if rmvnwline == 'on':
        result = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                result = result + char
        params = {'page1txt': 'removed new line', 'aftertxt': result}
        djtext = result

    if (rmvnwline != 'on' and captext != 'on' and chkpunc != 'on'):
        return HttpResponse('Error')

    return render(request, 'page1.html', params)




   # return HttpResponse("page 1 <a href = '/'>Back Home</a>")
"""def page2(request):
    return HttpResponse("page2")
def page3(request):
    return HttpResponse("page3")
def about(request):
    return HttpResponse("About Hello World")
"""
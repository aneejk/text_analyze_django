from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def analyze(request):
    user_text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    removextspace = request.GET.get('removextspace', 'off')
    countwords = request.GET.get('countwords', 'off')
    # analyze the text
    if removepunc == "on":
        punc = '''!"#$%&()*+,-'./:;?@]\[^_`{|}~'''
        analyzed_text = ""
        for i in user_text:
            if i not in punc:
               analyzed_text = analyzed_text + i
        analyze_text = {'analage': analyzed_text}
        return render(request,'analyze.html', analyze_text)
    elif fullcaps == 'on':
        analyzed_text = user_text.upper()
        analyze_text = {'analage': analyzed_text}
        return render(request, 'analyze.html', analyze_text)
    elif removextspace == 'on':
        analyzed_text = ""
        for index,char in enumerate(user_text):
            if not (user_text[index] == " " and user_text[index+1]) == " ":
                analyzed_text = analyzed_text + char
                analyze_text = {'analage' : analyzed_text}
        return render(request, 'analyze.html', analyze_text)
    elif countwords == 'on':
        wordcount = {}
        user_text1 = user_text.lower().split(' ')
        for char in user_text1:
            if char in wordcount:
                wordcount[char] += 1
            else:
                wordcount[char] = 1
        analyze_text = {'analage' : wordcount}
        return render(request, 'analyze.html', analyze_text)
    else:
        return HttpResponse("error")


#def capfirstletter(request):
#    return HttpResponse("capletter")
#def countwords(request):
#    return HttpResponse("countwords")

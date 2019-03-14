
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    alltext = request.GET['fulltext']
    wordlist = alltext.split()
    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            # increase COUNT
            worddictionary[word] +=1
        else:
            # add word to the Dictionary
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':alltext, 'count':len(wordlist),'sortedwords':sortedwords})

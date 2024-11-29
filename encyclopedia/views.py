from django.shortcuts import render, redirect
from django.http import Http404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    content = util.get_entry(name) 
    if content:
        return render(request, "encyclopedia/article.html",{
            "title": name,
            "content": content
        })
    else:
        return render(request, "encyclopedia/error.html") 

def search(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        content = util.get_entry(query)
        if content:
            return redirect("wiki_search", q = query)

def wiki_search(request, q):
    content = util.get_entry(q)
    return render(request, "encyclopedia/article.html",{
            "title": name,
            "content": content})
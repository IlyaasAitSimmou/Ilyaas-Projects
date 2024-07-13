from django.shortcuts import render
import markdown2
from encyclopedia.forms import SearchBar, NewPage, EditPage
from . import util
from random import choice
import re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchBar()
    })

def getTitle(request, title):
    page = util.get_entry(title.capitalize())
    if page == None:
        return render(request, "encyclopedia/error.html", {
        "entries": util.list_entries(),
        "form": SearchBar()
    }) # for now - will be changed
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": md_to_html(page),
        "form": SearchBar(),
        "current_page": title
    })
    
def md_to_html(page):
    markdowner = markdown2.Markdown()
    return markdowner.convert(page)

def Search(request):
    if request.method == "GET":
        searchquery = SearchBar(request.GET)
        if searchquery.is_valid():
            SearchInput = searchquery.cleaned_data["SearchInput"]
    if SearchInput in util.list_entries():
        return render(request, "encyclopedia/title.html", {
        "title": SearchInput,
        "content": md_to_html(util.get_entry(SearchInput.capitalize())),
        "form": SearchBar()
    })
    else:
        SearchResults = []
        for i in util.list_entries():
            if i.lower().count(str(SearchInput).lower()) > 0:
                SearchResults.append(i)
        return render(request, "encyclopedia/searchresults.html", {
                "SearchResults":SearchResults,
                "form": SearchBar()
            })

def page_creator(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
            "form": SearchBar(),
            "form2": NewPage()
        })
    elif request.method == "POST":
        new_page = NewPage(request.POST)
        if new_page.is_valid():
            title = new_page.cleaned_data["Title"]
            content = new_page.cleaned_data["textarea"]
            for filename in util.list_entries():
                if filename.lower() == str(title).lower():
                    print(False)
                    new_page = NewPage()
                    return render(request, "encyclopedia/error.html", {
                        "entries": util.list_entries(),
                        "form": SearchBar()
                    })     
            util.save_entry(title, content)
            return getTitle(request, title)
        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": SearchBar(),
                "form2": NewPage()
            })
        

def edit_page(request, title):
    if request.method == "GET":
        editpath = title
        # editpath2 = re.search(r"entries/(.*)/\.md", editpath)[1]
        print(util.get_entry(editpath))
        return render(request, "encyclopedia/editpage.html", {
            "form": SearchBar(),
            "form2": EditPage(initial={"textarea": util.get_entry(editpath)}),
            "edit_page": title
        })

def save_page(request, title):
    if request.method == "POST":
        save_page = EditPage(request.POST)
        if save_page.is_valid():
            content = save_page.cleaned_data["textarea"]  
            util.save_entry(title, content)
            return getTitle(request, title)
    


def random(request):
    randPage = choice(util.list_entries())
    return getTitle(request, randPage)
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Form configuration class
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# 1. View to display all tasks
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# 2. View to add a new task
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            new_task_string = form.cleaned_data["task"]
            
            # FIX: Ensure session list exists, then append to it
            if "tasks" not in request.session:
                request.session["tasks"] = []
            
            # We must assign the list to a local variable or mutate it directly
            current_tasks = request.session["tasks"]
            current_tasks.append(new_task_string)
            print(current_tasks)
            
            # FIX: Tell Django the session data has changed so it saves!
            request.session.modified = True
            
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
            
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

# 3. View to delete a task matching the index from index.html
def delete(request):
    if request.method == "POST":
        task_index = int(request.POST.get("task_index"))
        
        # FIX: Grab the tasks list from the session
        current_tasks = request.session.get("tasks", [])
        
        # Guard check using the actual session list length
        if 0 <= task_index < len(current_tasks):
            current_tasks.pop(task_index)  
            
            # FIX: Tell Django to save the deletion change
            request.session.modified = True
            
    return HttpResponseRedirect(reverse("tasks:index"))
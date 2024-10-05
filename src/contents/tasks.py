from pprint import pprint
import requests
# from contentapi.celery import app
from celery import shared_task
import environ
from contents.models import Content

env = environ.Env()
header = {'x-api-key': env('X_API_KEY')}
header = {'x-api-key': 'a327ec58sk_f42csk_43e9sk_9aabsk_faaf700a456e1728099608'}


@shared_task
def pull_and_store_content():
    # TODO: The design of this celery task is very weird. It's posting the response to localhost:3000.
    #  which is not ideal

    url = "https://hackapi.hellozelf.com/api/v1/contents/"
    api_url = "http://localhost:3000/api/contents/"
    res = requests.get(url).json()['data']
    for item in res:
        res = requests.post(api_url, json={**item})


@shared_task
def pull_AIGeneratedComment():
    # as content is orderd as latest fisrt, we will pull the first item
    _content = Content.objects.first()
    url = "https://hackapi.hellozelf.com/api/v1/ai_comment/"
    api_url = "http://localhost:3000/api/contents/"
    data = {
        "content_id": _content.id,
        "title": _content.title,
        "url": _content.url,
        "author_username": _content.author.username
    }

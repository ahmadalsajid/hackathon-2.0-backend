from pprint import pprint
import requests
# from contentapi.celery import app
from celery import shared_task
import environ
from rest_framework.templatetags.rest_framework import items

env = environ.Env()
header = {'x-api-key' : env('X_API_KEY')}
header = {'x-api-key' : 'a327ec58sk_f42csk_43e9sk_9aabsk_faaf700a456e1728099608'}
@shared_task
def pull_and_store_content():
    # TODO: The design of this celery task is very weird. It's posting the response to localhost:3000.
    #  which is not ideal
    # print("clerey running")

    url = "https://hackapi.hellozelf.com/api/v1/contents/"
    api_url = "http://localhost:3000/api/contents/"
    res = requests.get(url).json()['data']
    for item in res:
        res = requests.post(api_url, json={**item})

from locust import HttpUser, User, TaskSet, task, web, between
from random import randint
import random
import logging
import re
import os
import csv

logger = logging.getLogger(__name__)

HOST = ''

# List of user agents to test with, n.b. they are all identified by "LocustIO"
# so they can be uniquely identified in logs, by CDN, etc
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19 (LocustIO)",
    "Android 4.0.3;AppleWebKit/534.30;Build/IML74K;GT-I9220 Build/IML74K (LocustIO)",
    "KWC-S4000/ UP.Browser/7.2.6.1.794 (GUI) MMP/2.0 (LocustIO)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) (LocustIO)",
    "Googlebot-Image/1.0 (LocustIO)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0 (LocustIO)",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52 (LocustIO)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
]

# Loading from inline definition
URLS = ['']
# Loading from urls.csv:
# try:
#     path = '/mnt/locust/urls.csv'
#     print(os.listdir())
#     with open(path, 'r') as f:
#         reader = csv.reader(f)
#         URLS = list(reader)
# except FileNotFoundError:
#     raise Exception(f'Missing {path}')

class WebsiteUser(HttpUser):
    host = HOST  # e.g. https://example.org
    wait_time = between(1, 2)

    @task
    class UserBehavior(TaskSet):

        def on_start(self):
            """on_start is called when a Locust start before any task is scheduled"""
            self.headers = {
                "User-Agent": USER_AGENTS[random.randint(0,len(USER_AGENTS)-1)],
                "Authorization": "token mytokenhere"
            }
            self.client.headers = self.headers

        @task(90)
        def action_foo(self):
            """Request one of these urls 90% of the time"""
            url = random.choice(URLS)
            self.client.get(url, name='optional-name-to-identify-these-in-ui')

        @task(10)
        def action_bar(self):
            """Request one of these urls 10% of the time"""
            urls = ['']
            url = random.choice(urls)
            self.client.get(url, name='bar')

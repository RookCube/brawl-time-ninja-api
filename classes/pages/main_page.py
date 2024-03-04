import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from classes.etc import Event, StateEvents, DataEvents


class MainPage(object):
    url = "https://brawltime.ninja/"

    def __init__(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        self.data = json.loads(soup.find("script", id="vike_pageContext").text)['vueQueryState']['queries']
        data_stateMainBrawler = self.data[1]
        current_events = [
            Event(id=int(event_json['id']),
                  map=event_json['map'],
                  mode=event_json['mode'],
                  start=datetime.fromisoformat(event_json['start']),
                  end=datetime.fromisoformat(event_json['end']))
            for event_json in data_stateMainBrawler['state']['data']['current']
        ]
        upcoming_events = [
            Event(id=int(event_json['id']),
                  map=event_json['map'],
                  mode=event_json['mode'],
                  start=datetime.fromisoformat(event_json['start']),
                  end=datetime.fromisoformat(event_json['end']))
            for event_json in data_stateMainBrawler['state']['data']['upcoming']
        ]
        self.stateMainBrawler = StateEvents(
            data=DataEvents(
                current=current_events,
                upcoming=upcoming_events),
            dataUpdateCount=data_stateMainBrawler['state']['dataUpdateCount'],
            dateUpdatedAt=data_stateMainBrawler['state']['dataUpdatedAt'])

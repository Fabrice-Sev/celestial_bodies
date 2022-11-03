# create the register instance by initializing it with the Library instance.
from django import template
import requests
import datetime as dt


register = template.Library()

# An upper function that capitalizes word passed to it. We then register the filter using a suitable name.
@register.simple_tag(name="get_next_approach_date")
def get_next_approach_date(link):
  close_approach_dates=[]
  r = requests.get(link)
  asteroid = r.json()
  for data in asteroid['close_approach_data']:
    close_approach_dates.append(data['close_approach_date'])
    pass
  # ls:str=''
  for date in close_approach_dates:
    splitted_date = date.split('-')
    if dt.date(int(splitted_date[0]),int(splitted_date[1]),int(splitted_date[2])) >= dt.date.today():
      return date
    pass
  return 'No expected future approach for this asteroid'

@register.simple_tag(name="get_close_approach_data_in_km")
def get_close_approach_data_in_km(close_approach_data):
  return round(float(close_approach_data[0]['miss_distance']['kilometers']),2)

@register.simple_tag(name="get_close_approach_data_in_mi")
def get_close_approach_data_in_mi(close_approach_data):
  return round(float(close_approach_data[0]['miss_distance']['miles']),2)

# @register.simple_tag(name="session_classes")
# def session_subject(session:Session):
#   if session.classes.all().count() > 1:
#     return str(session.classes.all()[0]) + "," + str(session.classes.all()[1])
#   elif session.classes.all().count() == 1:
#     return str(session.classes.all()[0])
#   else:
#     return "None"
  
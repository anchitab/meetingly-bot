import os, ssl 
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
  ssl._create_default_https_context = ssl._create_unverified_context
import schedule
import time
import logging
from slack.web.client import WebClient
from slack.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  
    # makes a POST request through the slackclient
    # checks if the request works
  try:
    slack_client.chat_postMessage(
      channel='#bottest',
      text=msg
    )
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  #Sends reminder on Mondays
  reminder = "Happy Monday Team 🌤! We have a meeting this Friday from 5pm"
  schedule.every().monday.at("12:30").do(lambda: sendMessage(slack_client, reminder))

  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(2) 


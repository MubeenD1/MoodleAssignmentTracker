from flask import Flask, render_template, flash
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests

app = Flask(__name__)
app.secret_key = os.getenv('KEY')
token = os.getenv('API_TOKEN')
url = 'https://courses.ms.wits.ac.za/moodle/webservice/rest/server.php?moodlewsrestformat=json'

@app.route("/")
def home():

    params_calendar = {
    'wstoken' : token,
    'wsfunction' : 'core_calendar_get_calendar_upcoming_view'
    }

    response = requests.get(url, params=params_calendar)
    calendar = response.json()


    for event in calendar['events']:
            if event['popupname']:
                formatted_time = event['formattedtime']
                soup = BeautifulSoup(formatted_time, 'html.parser')
                time = soup.get_text()

                flash("<b>" + event['popupname'] + "</b>" + "<br>" + time)
            flash("<br>")

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.getennviron.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
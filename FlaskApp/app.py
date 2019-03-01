import os
from threading import Thread, Event

from flask import Flask, render_template
from flask_socketio import SocketIO


thread = Thread()
thread_stop_event = Event()
import pymongo
from pymongo import DESCENDING
from geopy.geocoders import Nominatim

DB_URI = 'mongodb+srv://fyp_admin:fyp_pwd@cluster0-oov30.mongodb.net/test?retryWrites=true'

def getLocationCoord(loc):
	geolocator = Nominatim()
	location = geolocator.geocode(loc + " ,Mauritius")
	print((location.latitude, location.longitude))
	long = location.longitude
	lat = location.latitude
	return (long, lat)

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()
    def getRecent(self):
        client = pymongo.MongoClient(DB_URI)
        db = client.test
        with db.watch() as stream:
            for document in stream:
                print(document)
                doc = document['fullDocument']
                try:
                    loc = doc['location']
                    print(loc)
                    if loc != "Not found":
                        long, lat = getLocationCoord(loc)
                    else:
                        print("Failed to get location coordinates due to no location text")
                except:
                    lat = doc['latitude']
                    long = doc['longitude']

                disease = doc['diseasetype']
                time = doc['date']


                socketio.emit('newdata', {'lat': lat, 'lng': long, 'dis': disease, 'time': time}, namespace='/test')


    def run(self):
        self.getRecent()

test_data = {
'lat': '-20.2233014','lng': '57.5382649'
}
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

#app = Flask(__name__)
app = Flask(__name__,
    template_folder=os.path.join(PROJECT_PATH, 'templates'),
    static_folder=os.path.join(PROJECT_PATH, 'static')
)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map_realtime")
def map_realtime():
    return render_template('map.html')

@app.route("/predict")
def predict():
    return render_template('predict.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')
    #socketio.emit('newdata', {'lat': '-20.2233014','lng': '57.5382649'}, namespace='/test')
    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()
'''@socketio.on('my_event', namespace='/test')
def test_message():
    socketio.emit('newdata', {'lat': '-20.2233014','lng': '57.5382649'}, namespace='/test')'''

if __name__ == "__main__":
    socketio.run(app)
    #app.run()

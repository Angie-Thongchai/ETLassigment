import datetime,json,requests
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# DATABASE integrate

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.app_context().push()

# Crate database

class Myapp(db.Model):
    city = db.Column(db.String(20),primary_key = True)
    date = db.Column(db.Integer)
    temperature = db.Column(db.integer)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    description = db.Column(db.String(20))

class MyappSchema(ma.Schema):
    fields = ('city', 'date', 'temperature', 'pressure', 'humidity','description')

my_app_schema = MyappSchema(many=True)

#Get order

@app.route('/')
def get():
    entries = Myapp.query.all()
    result = my_app_schema.dump(entries)
    return jsonify(result)

# Post order

@app.route('/', methods = ["POST"])
def post(city):
    api_key = "8c28834273d1c5b639e0f53eef0da3a2"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    # use JSON to get data
    response = requests.get(complete_url)
    x = response.json()
    # use datetime to indentify local date
    time = datetime.datetime.now()
    t = time.strftime("%x")
    y = x["main"]
    # get temperature and convert from kelvin to celsius
    temp = y["temp"] - 273.15
    # float must be 2 decimal numbers
    current_temperature = '%.2f' % temp
    # air pressure
    current_pressure = y["pressure"]
    # air humility
    current_humidity = y["humidity"]
    z = x["weather"]
    # weather detail
    weather_description = z[0]["description"]
    new_entry = Myapp(city = city, date = t, temperature = current_temperature , pressure = current_pressure, humidity = current_humidity, description = weather_description )

    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for("get"))

post("Stockholm")
post("London")
post("Madrid")
post("Rom")
post("Cairo")

# Delete order

@app.route('/<order_id>', methods = ["DELETE"])
def delete_order(order_id):
    entry = Myapp.query.get_or_404(order_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("get"))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
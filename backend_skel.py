#Backend for Extractive Metallurgy Simulation Website
#Core Developer - Ankit Kumar, Proneet Verma

from flask import Flask, render_template, request, session, redirect, url_for, flash 
from flask.ext.script import Manager
from flask.ext.wtf import Form 
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectMultipleField, BooleanField, RadioField, SubmitField
from wtforms.validators import Required, NumberRange, AnyOf

app = Flask(__name__)
manager = Manager(app)
# Application instance created 


@app.route('/', methods = ['GET'])
def index():
	return render_template('home.html')


@app.route('/simulation' , methods = ['POST', 'GET'] )
def simulation():
	return render_template('simulation.html')


@app.route('/documentation_wiki',  methods = ['GET'])
def wiki():
	return render_template('documentation_wiki.html')



if __name__ == '__main__':
    manager.run()

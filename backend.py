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


@app.route("/")
def index():
	return render_template("home.html")




"""  
	
	Main Content, Magic Sauce, All the simulation python functions
	come down here in a single page which hosts webform for retrieving 
	data about process selection and input parameters

"""

#Leave this as well for now (below). Does no harm plus i haven't thought clearly about what to do with these webforms
class ProcessForm(Form): 
	process = SelectField(u'Choose a Process', choices = [ (1,'Mineral Processing'), (2,'Hydrometallurgy'), (3,'Pyrometallurgy')], validators = [ Required() ], coerce = int)
	unit_operation = SelectField(u'Choose a unit operation' ,validators = [ Required() ] )
	submit = SubmitField('Submit')


#class InputParameters(Form):
#	submit = SubmitField('Submit')

###Customize the class variables/form fields of InputParameters class depending on unit operations chosen in previous form ie ProcessForm instance data
#"""
#	if form1.unit_operation.data == 'Crushing':
	####           Customised form fields for Crushing Input Parameters
#	elif form1.unit_operation.data == 'Some_other_unit_operation':   
	####           Some different set of form fields

	 ### | (above)	 Similar elif branches for each unit operation to generate custom forms corresponding to each operations input requirements with 
	 ### |   		 corresponding validators

#"""



### HTML Rendering of Forms created above to be done below here :

@app.route('/simulation' , methods = ['POST', 'GET'] )
def simulation():
	output = "Some Operation"
	sample_output = '007'

### Customising Response page with output (below)
	if request.method == 'POST':
		if request.form['unit_operation'] == 'Crushing':
			output =  'Crushing' #Put Crushing Function here, Crushing Function returns tuple, multiple assignment
			sample_output = '007'

		elif request.form['unit_operation'] == 'Calorific Value':
			output = "Calorific"  # Put Calorific Function here , Return tuple with output parameters, multiple assignment

		### Similarly Multiple elifs, one for each unit_operation
		return render_template('simulation.html', sample_output = sample_output, output = output) # Use control Structure to customize rendered variables according to unit_operation
	
	return render_template('simulation_home.html')

#LEAVE THIS ABHI BAAD MEIN DEKHTE HAIN WHAT TO DO ABOUT THIS PIECE OF CODE  (WEBFORMS CODE) (below)
"""
	unit_operation_by_process = {

    1: [('Crushing', 'Crushing'), ('second_unit_operation_mineral', 'second_unit_operation_mineral')],
    2: [('first_unit_operation_hydro', 'first_unit_operation_hydro')],
    3: [('first_unit_operation_pyro', 'first_unit_operation_pyro')]
	}
 	#####        (above) Enter the Unit Operation in the (value, label) form in the list above for every unit operation of each process

	form1 = ProcessForm({ 'process' :request.form['process'], 'unit_operation' :request.form['unit_operation']})    
     # (above) some doubt about this !!  request.form returns a MultiDict with class variable/field name as keys and data as its value 
     # (above) I am sure its correct but just check !!

	form1.unit_operation.choices = unit_operation_by_process.get(form1.process.data)

	 # (above) Dynamic SelectField implementation by defining choices after instantiation 
	 # http://stackoverflow.com/questions/18737255/dynamic-fields-depending-of-previous-fields-with-wtforms
	 # http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object
	 # http://stackoverflow.com/questions/17752301/dynamic-form-fields-in-flask-request-form

	unit_operation = form.unit_operation.data

"""



"""
	Magic Ends HERE !!!

"""



@app.route('/documentation_wiki')
def wiki():
	return render_template("documentation_wiki.html")

if __name__ == '__main__':
    manager.run()


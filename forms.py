from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

# Form for setting Elemental Live IP address
class IPForm(FlaskForm):
	ipaddress = StringField('Elemental IP Adress', validators=[DataRequired()] )
	submit = SubmitField('Set')

# Form for setting Elemental streamID to an GPIO input
class GPItoID(FlaskForm):	
	streamid = IntegerField('Stream ID:', validators=[DataRequired()] )
	setbut = SubmitField('Set')


# Buttons for manual Testing of GPI signal, activating or logging GPI inputs
class GPIctrl(FlaskForm):
	active = BooleanField('Active')
	testbut = SubmitField('Test')
	logbut = SubmitField('Log')
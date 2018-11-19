from flask import Flask, render_template, request
from config import Config
import liveapi
import forms

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/command_center')
def index():
	numGPI = 5
	fields_gpiToID = forms.GPItoID()
	fields_gpiCtrl = forms.GPIctrl()
	
	return render_template('command_center.html', f_gpiID = fields_gpiToID, 
									f_gpiCtrl = fields_gpiCtrl, numGPI = numGPI)
	
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



from flask import Flask, render_template, request, jsonify
from config import Config
import liveapi
import forms

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/command_center', methods = ['GET', 'POST'])
def index():
	gpiNum = 5									# Specify number of GPI inputs
	fields_gpiToID = forms.GPItoID()
	fields_gpiCtrl = forms.GPIctrl()
	
	if request.method == 'GET':					# When the page loads for first time
		return render_template('command_center.html', f_gpiID = fields_gpiToID, 
									f_gpiCtrl = fields_gpiCtrl, numGPI = gpiNum)
		
		
@app.route('/gpiSetID', methods = ['POST'])
def gpiSetID():
	gpiIdForm = forms.GPItoID()
	
	if gpiIdForm.validate_on_submit():
		return jsonify(data={'message': 'hello {}'.format(gpiIdForm.streamid.data)})
		
	

@app.route('/gpiCtrl')	
def gpiCtrl():
		return 'Perkele!'
	
	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_assets import Bundle, Environment
from config import Config
import liveapi
import forms


app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect()
csrf.init_app(app)

jsfiles = Bundle('form_ajax.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', jsfiles)

class Stream:
	ID = 0;

def init_forms_list(num_forms):
	forms_list = list()
	for num in range(0, num_forms):
		forms_list.append(forms.GPIctrl(prefix = str(num) + '_'))
	return forms_list
	
@app.route('/')
@app.route('/command_center', methods = ['GET', 'POST'])
def index():
	gpiNum = 5									# Specify number of GPI inputs
	forms_list = init_forms_list(gpiNum)
	fields_gpiCtrl = forms.GPIctrl()
	
	if request.method == 'GET':					# When the page loads for first time
		return render_template('command_center.html', forms = forms_list)
		#return render_template('command_center.html',f_gpiCtrl = fields_gpiCtrl,
		#														numGPI = gpiNum)
		#return 'Perkele'

		
def gpiSetID(gpiCtrl):
	stream1 = Stream()
	stream1.ID = gpiCtrl.gpi_id.stream_id.data
	return jsonify(data={'message': 'hello {}'.format(stream1.ID)})

@app.route('/gpiCtrl', methods = ['POST'])	
def gpiCtrl():
	gpiCtrl = forms.GPIctrl()
	
	if request.form['which-form'] == 'form_0':
		return 'PERKELE'
	
	if gpiCtrl.validate_on_submit():
		if gpiCtrl.gpi_id.setbut:
			gpiCtrl.gpi_id.setbut = False
			return gpiSetID(gpiCtrl)
		else:
			return 'Nice'
		
	else:
		return 'Perkele!'
	
	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



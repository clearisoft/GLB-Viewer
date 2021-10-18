from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__, template_folder='.', static_folder='./', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>.glb')
def show_module(name):
    return render_template('index.html', name=name, 
        ini_xyz=request.args.get('ini_xyz', '1,1,1'),
        obj_xyz=request.args.get('obj_xyz', '0,0,0'),
        ratio_xyz=request.args.get('ratio_xyz', '1,1,1'),
        ratio_ypr=request.args.get('ratio_ypr', '1,1,1'),
        )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

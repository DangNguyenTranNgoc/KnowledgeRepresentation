from flask import jsonify
from flask import request

from TriangleProblem import app
from ..models import TriangleSemantic

@app.route("/triangle_calculator", methods=['POST'])
def triangle_calculator():
    alpha = request.form.get('alpha', -1, float)
    beta = request.form.get('beta', -1, float)
    delta = request.form.get('delta', -1, float)
    a = request.form.get('a', -1, float)
    b = request.form.get('b', -1, float)
    c = request.form.get('c', -1, float)
    s = request.form.get('s', -1, float)
    height_c = request.form.get('h_c', -1, float)
    p = request.form.get('p', -1, float)

    return jsonify({'p':(a+b+c)/2, 'angle':(alpha+beta+delta)})


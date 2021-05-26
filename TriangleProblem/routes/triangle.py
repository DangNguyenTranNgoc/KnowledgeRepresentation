from flask.wrappers import Response
from TriangleProblem.models import triangle_semantic
from flask import jsonify
from flask import request

from ..utils.response_status import STATUS, get_status
from TriangleProblem import app
from ..models import TriangleSemantic

@app.route("/triangle_calculator", methods=['POST'])
def triangle_calculator():
    alpha = request.form.get('alpha', None, float)
    beta = request.form.get('beta', None, float)
    delta = request.form.get('delta', None, float)
    a = request.form.get('a', None, float)
    b = request.form.get('b', None, float)
    c = request.form.get('c', None, float)
    s = request.form.get('s', None, float)
    height_c = request.form.get('h_c', None, float)
    p = request.form.get('p', None, float)

    # Validate params
    is_valid = validate_param(alpha, beta, delta, a, b, c, s, height_c, p)
    if not is_valid:
        return jsonify({'status':400, 'message':'Bad Request','data':{}})
    
    triangle_semantic = create_triangle_semantic(a, b, c, alpha, beta, delta, height_c, s, p)
    response_data = {
        'alpha': triangle_semantic.alpha,
        'beta': triangle_semantic.beta,
        'delta': triangle_semantic.delta,
        'a': triangle_semantic.a,
        'b': triangle_semantic.b,
        'c': triangle_semantic.c,
        's': triangle_semantic.square,
        'height_c': triangle_semantic.height_c,
        'p': triangle_semantic.p
    }

    return jsonify({'status':200, 'message':'OK','data':response_data})

def validate_param(alpha:int=None, beta:int=None, delta:int=None,
                    a:int=None, b:int=None, c:int=None,
                    s:int=None, h_c:int=None, p:int=None) -> bool:
    '''
    Validate params
        - All param if exist need greater than 0
        - update later
        ...
    '''
    if alpha and alpha <= 0:
        return False
    
    if beta and beta <= 0:
        return False
    
    if delta and delta <= 0:
        return False
    
    if a and a <= 0:
        return False
    
    if b and b <= 0:
        return False
    
    if c and c <= 0:
        return False
    
    if s and s <= 0:
        return False
    
    if h_c and h_c <= 0:
        return False
    
    if p and p <= 0:
        return False

    return True

def create_triangle_semantic(a: int=None, b: int=None, c: int=None, 
                            alpha: int=None, beta: int=None, delta: int=None, 
                            height_c: int=None, square: int=None, p: int=None):
    triangle_semantic = TriangleSemantic()

    if alpha and alpha > 0:
        triangle_semantic.alpha = alpha

    if beta and beta > 0:
        triangle_semantic.beta = beta

    if delta and delta > 0:
        triangle_semantic.delta = delta

    if a and a > 0:
        triangle_semantic.a = a

    if b and b > 0:
        triangle_semantic.b = b

    if c and c > 0:
        triangle_semantic.c = c

    if square and square > 0:
        triangle_semantic.square = square

    if height_c and height_c > 0:
        triangle_semantic.height_c = height_c

    if p and p > 0:
        triangle_semantic.p = p
    
    return triangle_semantic

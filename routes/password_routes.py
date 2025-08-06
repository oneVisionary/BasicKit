from flask import Blueprint, render_template,request,jsonify
import string
import random
password_bp = Blueprint('password_mod',__name__)

@password_bp.route('/password')
def password():
    return render_template('password-generator.html')


@password_bp.route('/pwd_generate',methods=['POST'] )
def pwd_generate():
    data = request.get_json()
    suggested_name = data.get('suggested_name')
    length= data.get('length')
    includeUppercase= data.get('includeUppercase')
    includeLowercase= data.get('includeLowercase')
    includeNumbers= data.get('includeNumbers')
    includeSymbols= data.get('includeSymbols')
    output = data.get('sugges_name')
    
    char_pool = ''
    if includeUppercase:
        char_pool += string.ascii_uppercase
    if includeLowercase:
        char_pool += string.ascii_lowercase
    if includeNumbers:
        char_pool += string.digits
    if includeSymbols:
        char_pool +='!@#$%^&*()_+[]{}|;:,.<>?'
    
    sugg_length = len(suggested_name)
    remaining_length = length - sugg_length 
    if remaining_length < 0:
        return jsonify({'error': 'Password length must be greater than the length of the suggested name.'}), 400
    print(char_pool )
    random_chars =random.choices(char_pool, k=remaining_length)
    print(random_chars  )
    rand_pwd=''.join(random_chars)
    final_password = ''
    if output=='first':
        final_password = suggested_name + rand_pwd
    elif output=='last':
        final_password = rand_pwd + suggested_name  
    elif output == 'middle':
        mid_index = len(rand_pwd) // 2
        final_password = rand_pwd[:mid_index] + suggested_name + rand_pwd[mid_index:]
    
    return jsonify({'password': final_password})
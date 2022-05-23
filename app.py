from flask import *

def get_posts():
    sample = [{
        'post_name': 'sample_posts',
        
        
        }]

    return 


app = Flask(__name__)

app.errorhandler(404)
def file_not_found():
    return jsonify({'status_code':200, 'message':'file not found'}), 404

@app.route('/health', methods=['GET', 'POST', 'PUT', 'DELETE'])
def health():
    return jsonify({
        'status_code':200,
        'request_method':request.method,
        'message':'server status is up'
        }), 200

@app.route('/posts', methods=['GET', 'POST', 'PUT', 'DELETE'])
def posts():
    if request.method == 'GET':
        pass
        

    

@app.route('/community/<string:subject>')
def community_subject(subject):
    pass

app.run(host='0.0.0.0', port=8080)

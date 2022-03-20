
from flask import Flask, jsonify, request
import face_rec 
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'obito' : ['omda', 'emad']})


@app.route('/addimg', methods = ['POST'])
def addimg():
    img = request.json['img']
    
    faces = face_rec.classify_face(img)
    
    return jsonify({'faces' : faces})

if __name__ == '__main__':
    app.run(debug=True)
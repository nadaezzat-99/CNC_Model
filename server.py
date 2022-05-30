from flask import Flask , request
from flask_cors import CORS
from flask import jsonify

# Create flask & cors instance 
app = Flask(__name__)
cors = CORS()
cors.init_app(app)

selected_shape = ["circle"]

# Upadating srequired shape 
@app.route("/shape",methods=["POST"])
def save_shape():
    shapes = request.get_json()
    selected_shape[0] =shapes["shape"]

    return ("Drawing a " + selected_shape[0])
    
# Send required  shape 
@app.route('/draw_shape',methods=['GET'])
def draw_shape():
        response = jsonify(shape = selected_shape[0])
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090,debug=True)

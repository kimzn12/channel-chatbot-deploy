from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test",methods = ["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list = ["abc","def"]
    )
    return data

def skill():
    data = {
        "version" : "2.0",
        "template" : {
            "outputs": [
                {
                    "simpleText" : {
                        "Text": "간단한 텍스트"
                    }
                }
            ]
        }
    }

if __name__ == "__main__":
    app.run(host='localhost', debug = True)
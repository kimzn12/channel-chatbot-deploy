from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods =["GET"])
def main():
    return "Hi! If you wanna get response about Skill server, Go to /skill"


@app.route("/test", methods =["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list=[
            "abc",
            "def"
        ]
    )
    return data

@app.route("/skill", methods =["POST"])
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://www.wikihow.com/images_en/9/9b/Get-the-URL-for-Pictures-Step-2-Version-4.jpg",
                        "altText": "로고"
                    }
                }
            ]
        }
    }
    return jsonify(data)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
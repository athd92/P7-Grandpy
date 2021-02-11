from flask import Flask, render_template, make_response , request, jsonify
from datetime import date
import json
from wordlist import stopWords
from controler.parser import Parser
from controler.wiki import Wikipedia
from controler.googleMaps import GoogleMaps

app = Flask(__name__) # modif  annulee apres commit

@app.route("/", methods=['GET', 'POST'])
def homepage():

    error = ""
    if request.method == 'POST':
        question = request.form['question']
    return render_template("main.html", error=error)


@app.route('/entry', methods=['POST'])  # FONCTION QUI VA RECUPERER LE JSON
def createEntry():

    message = json.loads(request.data)   # get message from ajax request
    questionJson = Parser(message)
    questionString = questionJson.to_lower_string()
    questionLessWords = questionJson.after_deleted_words()
    questionRegexWords = questionJson.extract_question()
    finalQuery = questionJson.extract_question()
    geocodingQuery = GoogleMaps(finalQuery)
    geo = geocodingQuery.get_geocode()
    if geo == []:
        return jsonify({"data": "no result",
                        'localisation': 'no localisation possible'})
    else:
        city = geo[0]
        try:
            address = geo[1]
        except:
            address = "C'est ici mon petit..."

        if city == []:
            return jsonify({"data": "no result",
                            'localisation': 'no localisation possible'})

        else:
            try:
                localisation = city['geometry']['location']  # coordonates
                cityName = city['address_components'][0]['long_name']  # name
            except:
                localisation = city[0]['geometry']['location']
                cityName = city[0]['address_components'][0]['long_name']

            grandpyStory = Wikipedia(finalQuery)  # keep only city name
            story = grandpyStory.get_request()  # request story
            return jsonify({"data": story,
                            'localisation': localisation,
                            'address': address})


@app.errorhandler(404)
def page_not_found(e):
    """Function returns the lost page"""

    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

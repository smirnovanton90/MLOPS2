from flask import Flask, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello from Flask!")

@app.route("/predict/<int:G>/<int:NR>/<int:PG>/<int:PG_13>/<int:R>")
def predict(G, NR, PG, PG_13, R):
    with open("/home/prod-srv-admin/Titanic/models/model.pkl", "rb") as fd:
        clf = pickle.load(fd)
    prediction = int(clf.predict([[G, NR, PG, PG_13, R]])[0])
    return(jsonify({"rating": prediction}))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=55555)
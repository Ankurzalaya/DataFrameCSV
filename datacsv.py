from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("/home/developer/Downloads/annual.csv")
    df = df.head(100)
    df = df.to_html()

    df = [df]

    return render_template("data.html", tables=df, titles=[""])


@app.route("/Search_data", methods=["GET", "POST"])
def Search_data():
    if request.method == "GET":
        return render_template("searchdata.html")

    elif request.method == "POST":
        cv = request.form["filterdata"]
        df = pd.read_csv("/home/developer/Downloads/annual.csv")
        # data = pd.DataFrame(df)
        df = df.head(100)
        search = df[
            df.apply(
                lambda row: row.astype(str).str.contains(cv, case=False).any(), axis=1
            )
        ]

        # search = data.loc[data['Variable_code'] == cv]
        return render_template("searchdata.html", tables=[search.to_html()])


@app.route("/Filter_data", methods=["GET", "POST"])
def Filter_data():
    if request.method == "GET":
        return render_template("filterdata.html")
    elif request.method == "POST":
        df = pd.read_csv("/home/developer/Downloads/annual.csv")
        cv = str(request.form["data"])
        t = cv.split(",")
        data = df.filter(t)
        return render_template("filterdata.html", tables=[data.to_html()])


if __name__ == "__main__":
    app.run(debug=True)

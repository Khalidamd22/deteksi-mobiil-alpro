from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Baca file CSV menggunakan Pandas
    df = pd.read_csv('mmm.csv')
    # Convert dataframe to HTML table
    data_html = df.to_html(classes='table table-striped', index=False)
    return render_template('index.html', table=data_html)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/data/')
def data():
    # Verbindung zur SQLite-Datenbank mit dem vollständigen Pfad
    conn = sqlite3.connect('data/dog_breeds.db')
    # Daten abfragen
    df = pd.read_sql_query('SELECT * FROM cleaned_data', conn)
    # Verbindung schließen
    conn.close()
    # Daten an das Template senden (HTML-Tabelle erstellen oder ähnliches)
    return render_template('data.html', tables=[df.to_html(classes='data', escape=False)], titles=df.columns.values)
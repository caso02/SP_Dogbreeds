from flask import Flask, request, render_template, jsonify
import sqlite3
import pandas as pd
import re

app = Flask(__name__)
DB_PATH = 'data/dog_breeds.db'

# Route um alle Hunderassen zu bekommen
@app.route('/get_all_breeds', methods=['GET'])
def get_all_breeds():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT breed FROM cleaned_data")
    breeds = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(breeds)

@app.route('/', methods=['GET', 'POST'])
def hello():
    result = None
    if request.method == 'POST' and 'breed_search' in request.form:
        breed = request.form['breed_search'].lower()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cleaned_data WHERE LOWER(breed) LIKE ?", ('%' + breed + '%',))
        result = cursor.fetchall()
        conn.close()
    return render_template('index.html', result=result)


# Route für die Suche nach Charaktereigenschaften
def get_unique_traits_from_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT [Character Traits] FROM cleaned_data")
    all_traits = set()
    
    for row in cursor.fetchall():
        traits = row[0].lower() if row[0] else ''
        traits_list = re.split(r',\s*', traits)
        all_traits.update(traits_list)
    
    conn.close()
    return sorted(all_traits)

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    breeds = None
    all_traits = get_unique_traits_from_db()
    
    if request.method == 'POST':
        traits = request.form.getlist('traits')
        if traits:
            trait_conditions = ' AND '.join([f"LOWER([Character Traits]) LIKE '%{trait.lower()}%'" for trait in traits])
            query = f"SELECT * FROM cleaned_data WHERE {trait_conditions}"
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(query)
            breeds = cursor.fetchall()
            conn.close()
    return render_template('filter.html', breeds=breeds, traits=all_traits)


# Route für anzeigen aller Daten
@app.route('/data/')
def data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query('SELECT * FROM cleaned_data', conn)
    conn.close()
    return render_template('data.html', tables=[df.to_html(classes='data', escape=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)

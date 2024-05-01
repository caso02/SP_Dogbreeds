from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Diagramm erstellen
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])  # Beispiel-Daten
    ax.set_title("Beispiel Diagramm")
    # Diagramm in HTML einbinden
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

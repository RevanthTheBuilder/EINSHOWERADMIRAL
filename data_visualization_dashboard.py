
# Project: Data Visualization Dashboard
# Language: Python
# Libraries: Flask, Matplotlib, Seaborn, Pandas, NumPy

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = {'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'],
            'Cases': [500000, 200000, 300000, 150000, 100000]}
    df = pd.DataFrame(data)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Country', y='Cases', data=df)
    plt.title('COVID-19 Cases by Country')
    plt.savefig('static/covid_cases.png')
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

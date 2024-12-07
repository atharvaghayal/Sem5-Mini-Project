# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

# Database connection
def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route - shows dashboard with all expenses
@app.route('/')
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    expenses = cur.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Route to add a new expense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = float(request.form['amount'])
        
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                    (date, category, description, amount))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

# Machine Learning Insights route
@app.route('/insights')
def insights():
    # Load data and ML model
    conn = connect_db()
    expenses_df = pd.read_sql_query("SELECT amount FROM expenses", conn)
    model = joblib.load("expense_predictor_model.pkl")
    prediction = model.predict(expenses_df)  # Just an example; fine-tune as needed
    conn.close()
    return render_template('insights.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "count_count"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/addcount', methods=['POST'])
def refresh():
    if request.form['addcount'] == 'plus':
        session['count'] += 1
    if request.form['addcount'] == 'reset':
        session['count'] = 0
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
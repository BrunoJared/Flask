from flask import Flask, render_template

app = Flask(__name__)

@app.route('/interview')
def interview():
    # Simple professional experiences
    experiences = [
        "Software Engineer at Company IBM (2022-present)",
        "Software QA Engineer at Company Qintess (2021-2022)",
        "Software QA Engineer Wipro(2021-2021)"
    ]
    return render_template('interview.html', experiences=experiences)

if __name__ == '__main__':
    app.run(host='8080', port=5050)

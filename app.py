from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Abuja',
  'salary': 'N 7,680,000'
}, {
  'id': 2,
  'title': 'Business Analyst',
  'location': 'Lagos'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Remote',
  'salary': 'N 7,500,000'
}, {
  'id': 4,
  'title': 'Backend Developer',
  'location': 'Leeds',
  'salary': '£ 120,000'
}, {
  'id': 5,
  'title': 'Full stack Developer.',
  'location': 'Abuja',
  'salary': '£ 150,000',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Bhucee')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

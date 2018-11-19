from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    q = request.args.get('q')
    if q == "Ping":
      return "OK"
    if q == "Name":
      return "Cole Knowlden"
    if q == "Degree":
      return "B.S. Computer Science - University of Chicago"
    if q == "Resume":
      return "Resume - http://ec2-3-16-128-77.us-east-2.compute.amazonaws.com:5005/resume \n Cover - http://ec2-3-16-128-77.us-east-2.compute.amazonaws.com:5005/cover"
    if q == "Puzzle":
      return ''' ABCD
A=<><
B>=><
C<<=<
D>>>='''
    if q == "Email Address":
      return "coknowlden@gmail.com"
    if q == "Position":
      return "Sr. Full Stack Engineer"
    if q == "Phone":
      return "425-315-5647"
    if q == "Years":
      return "5"
    if q == "Source":
      return "https://github.com/seasonics/emxtest"
    if q == "Referrer":
      return "Angel List"
    if q == "Status":
      return "Yes"
    return "OK"

@app.route('/resume')
def resume():
  return send_from_directory('static','resume.pdf')

@app.route('/cover'):
def cover():
  return send_from_directory('static','emx_cover.pdf')

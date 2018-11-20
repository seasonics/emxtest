from flask import Flask, request, Response, send_from_directory

app = Flask(__name__)


def puzzle_solve(arr):
  opp = {'=':'=', '<':'>','>':'<'}
  # apply identitiy and transative
  for i, item in enumerate(arr):
    for j, val in enumerate(arr[i]):
      if i == j:
        arr[i][j] = "="
      elif val != '-':
        arr[-i-1][-j-1] = opp[val]
        arr[j][i] = opp[val]

  # not entirely sure how to proceed with assigning the remain carrots
  # examples given have rows of entitely < or > so I'll add a row of < or >
  safe = ['=','-']
  for i,row in enumerate(arr):
    val = ''
    for item in row:
      if item not in safe and val== '':
        val = item
      elif item not in safe and val !=item:
        val = ''
        break
    if val:
      new_row = [val if item !="=" else '=' for item in row]
      break
  arr[i] = new_row

  # apply identitiy and transative again
  for i, item in enumerate(arr):
    for j, val in enumerate(arr[i]):
      if i == j:
        arr[i][j] = "="
      elif val != '-':
        arr[-i-1][-j-1] = opp[val]
        arr[j][i] = opp[val]     
  return arr

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
      puzzle = request.args.get('d')
      sp = puzzle.split('Please solve this puzzle:\n ABCD\n')[1].split()
      arr=[(list(sp[i][1:])) for i in range(4)]
      arr = puzzle_solve(arr)
      return '''ABCD
A%s
B%s
C%s
D%s
''' % (''.join(arr[0]),''.join(arr[1]),''.join(arr[2]),''.join(arr[3]))
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

@app.route('/cover')
def cover():
  return send_from_directory('static','emx_cover.pdf')

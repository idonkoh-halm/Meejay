import flask

myapp=flask.Flask('Hello')

@myapp.route('/',methods=['POST','GET'])
def getm3u():
    if flask.request.method=='GET':
        html=file ('UI.html','r').read()
        return html
    else:
        #If it is post
        return str(flask.request.form)
myapp.run(debug=True)

@myapp('/USER_select_genre',methods=['POST'])
def genre_get():
    request.form['genre']
    genre=request.form['genre']
    if flask.request.method=='POST':
        form = file('linkcreator.py','r').read()

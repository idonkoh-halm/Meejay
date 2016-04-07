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

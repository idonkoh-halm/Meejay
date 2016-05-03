import flask
import linkcreator as lc
myapp=flask.Flask('Hello')

@myapp.route('/',methods=['POST','GET'])
def getm3u():
    if flask.request.method=='GET':
        html=file ('UI.html','r').read()
        return html
    else:
        #If it is post
        return str(flask.request.form)

@myapp.route('/USER_select_genre',methods=['POST'])
def genre_get():
    genre1=flask.request.form['genre1']
    genre2=flask.request.form['genre2']
    lc.generate_m3us_for_genres_samples('html_jazz+rock',[genre1,genre2],2)


myapp.run(debug=True)
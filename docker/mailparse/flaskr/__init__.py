import os,sys,logging

from flask import Flask, redirect, url_for, request, render_template

# create and configure the app
app = Flask(__name__, instance_relative_config=True)


#Primary parse function. Takes a block of text and produes a parsed dict
def parseemail(rawtext):
    maildict = dict()
    maillines = rawtext.splitlines()
    for i in maillines:
        x = str(i)
        if x.find("To:") == 2 or x.find("From:") == 2 or x.find("Date:") == 2 or x.find("Subject:") == 2 or x.find("Message-ID:") == 2:
            y = x.split (':',1) 
            maildict[y[0][2:]] = y[1][1:-1]
    return maildict






# Return some instructions if they hit the URL with a GET method. Else do the thing. 
@app.route('/post',methods = ['POST', 'GET'] )
def post():
    if request.method == 'GET':
        out = request.args.get('text')
        return render_template("post.html")
    else:
        out = request.get_data()
        jsonemail = parseemail(out)
        return jsonemail

app.add_url_rule('/', 'post', post)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 ,debug = True)
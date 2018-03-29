from flask import Flask, render_template, request, make_response
import base64
import json
import os

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    result=request.form
    newresult={}
    for k,v in result.iteritems():
        newresult[k]=v
    test(**newresult)
    return "SimplCi Template Generated Successfully"

def test(**result):
    with open('output/simpleci.conf','w') as f:
        f.write(render_template("simpleci.conf.template",
            ggithubURL=str(result.get('ggithubURL')),
            glibraryName=str(result.get('glibraryName')),
            gversion=str(result.get('gversion')),
            bproject=str(result.get('bProject')),
            bserverUrl=str(result.get('bServerUrl')),
            busername=str(result.get('bUsername')),
            bpassword=base64.b64encode(str(result.get('bPassword'))),
            atype=str(result.get('atype')),
            ausername=str(result.get('aUsername')),
            acredentialsId=str(result.get('acredentialsId')),
            adescription=str(result.get('adescription')),
            apath=str(result.get('apath')),
            apassword=base64.b64encode(str(result.get('aPassword')))
            ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
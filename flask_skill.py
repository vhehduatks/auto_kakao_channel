
from flask import request
from flask import Flask
from flask import jsonify

import requests

def GET_Link(file_name):
    try:
        with open(file_name,'r') as f:
            img_link=f.read()

        return img_link    
    except Exception as e:
            print(e)


<<<<<<< HEAD
=======

def CLOSE_DRIVER():
    driver.quit()
    exit()


>>>>>>> 271a40be20d6499ac6c986bc55858abac44b1b85
app=Flask(__name__)


@app.route('/')
def testmain():
    return "Hello_world"

@app.route('/testskill01',methods=['POST'])

def func01():
    

    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
<<<<<<< HEAD
                        "imageUrl": GET_Link('link txt file name'),
                        "altText": "alt"
=======
                        "imageUrl": GET_Link('CCTV.txt'),
                        "altText": "1번 채널 사진입니다."
>>>>>>> 271a40be20d6499ac6c986bc55858abac44b1b85
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route('/testskill02',methods=['POST'])

def func02():
    

    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
<<<<<<< HEAD
                        "imageUrl": GET_Link('link txt file name'),
                        "altText": "alt"
=======
                        "imageUrl": GET_Link('Hourly.txt'),
                        "altText": "2번 채널 사진입니다."
>>>>>>> 271a40be20d6499ac6c986bc55858abac44b1b85
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route('/testskill03',methods=['POST'])

def func03():
    

    content = request.get_json()
    content = content['userRequest']
    Client_Message = content['utterance']
    print(Client_Message)
    res={   
        "version": "2.0",
        "template": 
        {
            "outputs": 
            [
                {
                    "simpleImage": 
                    {
<<<<<<< HEAD
                        "imageUrl": GET_Link('link txt file name'),
                        "altText": "alt"
=======
                        "imageUrl": GET_Link('daily.txt'),
                        "altText": "18시 30분 현장 사진입니다."
>>>>>>> 271a40be20d6499ac6c986bc55858abac44b1b85
                    }
                }
            ]
        }
    }
    return jsonify(res)


if __name__=="__main__":
    app.run(host='0.0.0.0',port='8080')
<<<<<<< HEAD
=======

# 168.131.70.215
#노트북 168.131.70.50
>>>>>>> 271a40be20d6499ac6c986bc55858abac44b1b85

from flask import Flask, render_template, request,url_for
import random, os
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
        'sqlite:///'+os.path.join(basedir,'database.db')

db=SQLAlchemy(app)

class result(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    com_rsp=db.Column(db.String, nullable=False)
    user_rsp=db.Column(db.String, nullable=False)
    resulting=db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    #input 받은 값을 flask에서 사용하는 부분(NONE값이 처음 들어갈때 생기는 오류를 방지하기 위해)
    if(request.args.get('user_rsp') is None):
        user_rsp='✊'
    else:
        user_rsp=request.args.get('user_rsp')
    #컴퓨터 랜덤 가위바위보 정하기
    random_com=random.randint(1,3)
    if(random_com==1):
        com_rsp='✊'
    elif(random_com==2):
        com_rsp='✌'
    elif(random_com==3):
        com_rsp='✋'

    #승패무 결정하는 곳
    if(com_rsp==user_rsp):#무
        c_res='무'
    elif((com_rsp=='✊'and user_rsp=='✋') or (com_rsp=='✌'and user_rsp=='✊') or (com_rsp=='✋' and user_rsp=='✌')):#승리
        c_res='승'
    else: #패
        c_res='패'

    #DB에 결과 저장하는 곳
    res=result(com_rsp=com_rsp,user_rsp=user_rsp,resulting=c_res)
    db.session.add(res)
    db.session.commit()

    #승패무 카운트 하는 곳 + html에서 나타내기 위한 데이터 만드는 곳
    history_game=result.query.all()
    cnt_d=result.query.filter_by(resulting='무').count()
    cnt_w=result.query.filter_by(resulting='승').count()
    cnt_l=result.query.filter_by(resulting='패').count()
    context=[history_game,cnt_d,cnt_l,cnt_w,user_rsp,com_rsp,c_res]
    return render_template('index.html',data=context)

#DB에서 제거해서 새게임 하게 만드는 곳
@app.route('/cleanup', methods=['POST'])
def cleanup():
    b=result.query.all()
    for d in b:
        db.session.delete(d)

    db.session.commit()
    context={

    }
    return render_template('index.html',data=context) 

if __name__=='__main__':
    app.run(debug=True)
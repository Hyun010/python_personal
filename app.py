from flask import Flask, render_template, request,url_for
import random, os
from flask_sqlalchemy import SQLAlchemy
import sqlite3

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
    user_rsp=request.args.get('user_rsp')
    random_com=random.randint(1,3)
    if(random_com==1):
        com_rsp='✊'
    elif(random_com==2):
        com_rsp='✌'
    elif(random_com==3):
        com_rsp='✋'

    if(com_rsp==user_rsp):#무
        c_res='무'
    elif((com_rsp=='✊'and user_rsp=='✋') or (com_rsp=='✌'and user_rsp=='✊') or (com_rsp=='✋' and user_rsp=='✌')):#승리
        c_res='승'
    else: #패
        c_res='패'

    res=result(com_rsp=com_rsp,user_rsp=user_rsp,resulting=c_res)
    db.session.add(res)
    db.session.commit()

    history_game=result.query.all()
    cnt_d=result.query.filter_by(resulting='무').count()
    cnt_w=result.query.filter_by(resulting='승').count()
    cnt_l=result.query.filter_by(resulting='패').count()
    context=[history_game,cnt_d,cnt_l,cnt_w,user_rsp,com_rsp,c_res]
    return render_template('index.html',data=context)

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
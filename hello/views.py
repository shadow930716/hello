from flask import flash,redirect,url_for,render_template

from hello import app,db
from hello.forms import HelloForm
from hello.models import Message

@app.route('/',methods=['GET','POST'])
def index():
    form=HelloForm()
    if form.validate_on_submit():
        name=form.name.data
        body=form.body.data
        age=form.age.data
        score=form.score.data
        message=Message(body=body,name=name,age=age,score=score)  
        db.session.add(message)
        db.session.commit()
        flash('your message have been sent to the world')
        return redirect(url_for('index'))
        
    messages=Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html',form=form,messages=messages)

    
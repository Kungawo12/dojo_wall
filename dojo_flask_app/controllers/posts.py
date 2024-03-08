from flask import render_template,request, redirect,session,flash
from dojo_flask_app import app
from dojo_flask_app.models.post import Post

@app.route("/post/message", methods=['POST'])
def create():

    data={
        "user_id": request.form["user_id"],
        "content": request.form["content"]
    }
    Post.save(data)
    
    return redirect('/dashboard')

@app.route('/post/delete/<int:id>')
def deleter(id):
    data={
        "id": id
    }
    Post.delete(data)
    return redirect('/dashboard')
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import BlogPost
from myapp.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

# to create a blog post
@blogposts.route('/create', methods=['GET', 'POST'])
# protects this controller/ route
@login_required
def create_post():
  form = BlogPostForm()
  if form.validate_on_submit():
    blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
    # add blog post to the database
    db.session.add(blog_post)
    db.session.commit()
    flash('Blog Post Created')
    print('Blog post was created')
    # go to the core page after a post is created
    return redirect(url_for('core.index'))
  # else, return form to create a post ?
  return render_template('create_post.html', form=form)

  
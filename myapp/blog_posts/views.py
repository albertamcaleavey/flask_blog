from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import BlogPost
from myapp.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

# create controller
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

# show controller
# variable for dynamic routing we will pass
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
  # query for blog post
  # get the post, or throw 404
  blog_post = BlogPost.query.get_or_404(blog_post_id)
  return render_template('blog_post.html', title=blog_post.title, date=blog_post.date, post=blog_post)
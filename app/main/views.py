from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import CourseForm
from .. import db
from ..models import Course

@main.route('/adder',methods = ["GET","POST"])
def adder():
    form = CourseForm()
    if form.validate_on_submit():
        crs = Course(courseName = form.name.data, courseType = form.courseType.data, courseId = form.courseId.data, courseLink = form.link.data, courseSlot = form.slot.data)
        db.session.add(crs)
        return redirect(url_for('.adder'))

    return render_template("form.html",form = form, name = session.get('name'))# current_time = datetime.utcnow()

@main.route('/')
def index():
    data = Course.query.all()
    return render_template("index.html",data = data)
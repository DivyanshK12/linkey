from datetime import datetime
from flask import render_template, session, redirect, url_for, flash

from . import main
from .forms import CourseForm
from .. import db
from ..models import Course
from .utils import *

@main.route('/adder',methods = ["GET","POST"])
def adder():
    form = CourseForm()
    if form.validate_on_submit():
        if not is_valid_link(form.link.data):
            flash("Invalid meeting link entered")
            return redirect(url_for('.adder'))
        
        form_inp = Course.query.filter_by(courseName = form.name.data,courseType = form.courseType.data, courseId = form.courseId.data, courseSlot = form.slot.data).first()
        crs = Course(courseName = form.name.data, courseType = form.courseType.data, courseId = form.courseId.data, courseLink = form.link.data, courseSlot = form.slot.data)
        if form_inp is not None:
            db.session.delete(form_inp)
            db.session.commit()

        db.session.add(crs)
        db.session.commit()
        return redirect(url_for('.adder'))

    return render_template("form.html",form = form, name = session.get('name'))# current_time = datetime.utcnow()

@main.route('/')
def index():
    time_obj = datetime.now()
    slot = get_slot(time_obj)
    data = Course.query.filter_by(courseSlot = slot).all()
    return render_template("index.html",data = data,page = "Home")

@main.route('/all')
def aller():
    data = Course.query.all()
    return render_template("index.html",data = data,page = "All Courses")
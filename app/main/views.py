from datetime import datetime
from flask import render_template, session, redirect, url_for, flash

from . import main
from .forms import CourseForm, RemoverForm
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

    return render_template("form.html",form = form)# current_time = datetime.utcnow()

@main.route('/')
def index():
    slot = get_slot()
    if slot is not None :
        data = Course.query.filter_by(courseSlot = slot).all()
        return render_template("index.html",data = data, active = len(data))
    else:
        return render_template("empty.html")

@main.route('/all')
def aller():
    data = dict()
    for slot in "ABCDEFGPQRS":
        data[slot] = Course.query.filter_by(courseSlot = slot).all()
    return render_template("all_courses.html",data = data)

@main.route('/empty')
def empty():
    return render_template("empty.html")

@main.route('/sloter')
def slots():
    return render_template("slot_timetable.html")

@main.route('/remover',methods = ["GET","POST"])
def remover():
    form = RemoverForm()
    if form.validate_on_submit():
        if form.Password.data == "Ragnarok":
            form_inp = Course.query.filter_by(courseType = form.courseType.data, courseId = form.courseId.data, courseSlot = form.slot.data).first()
            if form_inp is not None :
                db.session.delete(form_inp)
                db.session.commit()
            else:
                flash("Course Doesn't exist")
        else:
            flash("Invalid Password Entered")
        return redirect(url_for('.remover'))

    return render_template("form_rm.html",form = form)# current_time = datetime.utcnow()


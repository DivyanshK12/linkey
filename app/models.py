from . import db

#Database Basic
class Course(db.Model):
    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key = True)
    courseName = db.Column(db.String(64))
    courseType = db.Column(db.String(64))
    courseId = db.Column(db.Integer)
    courseLink = db.Column(db.String(128))
    courseSlot = db.Column(db.String(64))
    # segment_id = db.Column(db.Integer, db.ForeignKey('segment.id'))

# class Segment(db.model):
#     __tablename__ = 'segment'
#     id = db.Column(db.Integer, primary_key = True)
#     courses = db.relationship('Course', backref='segment')
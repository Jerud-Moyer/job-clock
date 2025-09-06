from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class TimeEntry(db.Model):
    __tablename__ = 'time_entries'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    # duration = db.Column(db.Interval, nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    currently_open = db.Column(db.Boolean, default=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('time_entries', lazy=True))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    job = db.relationship('Job', backref=db.backref('time_entries', lazy=True))

    @property
    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return None

    def __repr__(self):
        return f'<TimeEntry {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'duration': str(self.duration),
            'notes': self.notes
        }

    # def save(self, session):
    #     #need to move this stuff to controller!
    #         if not self.end_time:
    #             self.end_time = self.start_time
    #         client_id = session.query(Job).filter(Job.id == self.job_id).first().client_id
    #         self.client_id = client_id
    #         session.add(self)
    #         session.commit()

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    # may be first and last fields? And a company name field?
    # name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    # maybe separate address fied out?
    # address = db.Column(db.String(255), nullable=True)
    street_address = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    current_rate = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f'<Client {self.name}>'#need to fix
        

    @hybrid_property
    def client_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'client_name': self.client_name,
            'email': self.email,
            'phone': self.phone,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'current_rate': self.current_rate
        }

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('jobs', lazy=True))
    last_clocked = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Job {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'client': self.client.to_dict(),
            'client_id': self.client_id,
            'last_clocked': self.last_clocked
        }
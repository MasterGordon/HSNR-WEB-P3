# coding: utf-8
import cherrypy
from .db.database import Database
from .view import View

class Application:
    def __init__(
            self, 
            employees: Database, 
            trainings: Database, 
            certificates: Database, 
            qualifications: Database, 
            granted_qualifications: Database, 
            owned_certificates: Database, 
            owned_qualifications: Database):
        self.employees = employees
        self.trainings = trainings
        self.certificates = certificates
        self.qualifications = qualifications

    @cherrypy.expose
    def index(self):
        return View().index(
                {
                    "employees": self.employees.count(),
                    "trainings": self.trainings.count(),
                    "participations": 5
                }
            )

    @cherrypy.expose
    def default(self):
        raise cherrypy.HTTPError(404)
    default.expose = True

    @cherrypy.expose
    def edit_employees(self):
        return View().editEmployees(
                {
                    "employees": self.employees.get_all()
                }
            )

    @cherrypy.expose
    def add_training(self):
        return View().addTraining(
                {
                    "certificates": self.certificates.get_all()
                }
            )

    @cherrypy.expose
    def edit_trainings(self):
        return View().editTrainings(
                {
                    "trainings": self.trainings.get_all()
                }
            )
    @cherrypy.expose
    def edit_training(self, index):
        training = self.trainings.get_by_index(int(index))
        certificate = self.certificates.get_by_index(int(training["certificate_id"]))
        qualifications = self.qualifications.query(
        '''
            SELECT id, title, desc
            FROM qualification q
            JOIN training_grants_qualification t
              ON q.id = t.qualification_id
            WHERE t.training_id = ?
        ''', [training.id])
        qualifications = self.qualifications.deserialize_result(qualifications)
        return View().editTraining(
                {
                    "training": training,
                    "certificate": certificate,
                    "all_qualifications": self.qualifications.get_all(),
                    "qualifications": qualifications
                }
            )


    @cherrypy.expose
    def edit_certificates(self):
        return View().editCertificates(
                {
                    "certificates": self.certificates.get_all()
                }
            )

    @cherrypy.expose
    def edit_qualifications(self):
        return View().editQualifications(
                {
                    "qualifications": self.qualifications.get_all()
                }
            )

    @cherrypy.expose
    def participation_employees(self):
        return

    @cherrypy.expose
    def participation_trainings(self):
        return

    @cherrypy.expose
    def report_employees(self):
        return

    @cherrypy.expose
    def report_trainings(self):
        return

    @cherrypy.expose
    def report_certificates(self):
        return

# EOF

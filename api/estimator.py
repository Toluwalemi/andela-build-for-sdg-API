from datetime import datetime

LANGUAGES_CHOICES = ('Days', 'Weeks', 'Months',)


class Estimator(object):
    def __init__(self, time_to_elapse, reported_cases, population, total_hospital_beds,
                 period_type=LANGUAGES_CHOICES):
        self.period_type = period_type
        self.time_to_elapse = time_to_elapse
        self.reported_cases = reported_cases
        self.population = population
        self.total_hospital_beds = total_hospital_beds

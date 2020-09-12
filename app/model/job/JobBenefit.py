class JobBenefit:
    def __init__(self):
        self.job_id = 0
        self.benefit = ''

    def serialize(self):
        return {
            "jobId": self.job_id,
            "benefit": self.benefit
        }

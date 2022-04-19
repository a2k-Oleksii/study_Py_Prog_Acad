class ElevenStudentAddGroupException(Exception):
    
    def __init__(self):
        super().__init__()
        self.message = "Add eleven student! The group must contain no more than ten students!"

    def __str__(self):
        return self.message

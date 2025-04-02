from django.contrib import admin # type: ignore
from .models import Exam, ExamParticipant, ProctoringSession, ProctoringEvent, Question, UserResponse, UserScore

admin.site.register(Exam)
admin.site.register(ProctoringSession)
admin.site.register(ProctoringEvent)
admin.site.register(Question)
admin.site.register(UserResponse)
admin.site.register(UserScore)
admin.site.register(ExamParticipant)

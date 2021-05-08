from django.contrib import admin
from voting.models import *


class CandidateAdminView(admin.ModelAdmin):
    list_display = ["name", "constituency", "no_votes"]

class VotersAdminView(admin.ModelAdmin):
    list_display = ["user", "constituency", "is_voted"]

admin.site.register(Constituency)
admin.site.register(Candidate, CandidateAdminView)
admin.site.register(Voter, VotersAdminView)
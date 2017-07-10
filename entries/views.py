from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):
	"""Show all entries."""
	entries = Entry.objects.all()
	return render(request, 'entries/index.html', {'entries': entries})
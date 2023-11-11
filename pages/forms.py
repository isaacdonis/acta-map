from django import forms

class FeedbackForm(forms.Form):
    station_name = forms.CharField(label="What is the name of the station you'd like to submit feedback about?", max_length=500)
    feedback_text = forms.CharField(label="What advice would you like to give others who use wheelchairs?", widget=forms.Textarea)
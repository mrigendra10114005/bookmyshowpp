from django.urls import path
from django.conf.urls import url

from . import views

from .views import HometemplateView

urlpatterns=[ path('', views.index, name='index'),
			#url('add/',views.Audienceadd,name="Audience"),
			 # ex: /bookmyshow/Movie
			 url(r'^Movie/', views.movieView, name='Movie'),
			 # ex: /bookmyshow/Audience
			 url(r'^Audience/', views.audienceView, name='Audience'),
			 # ex: /bookmyshow/Theater
			 url(r'^Theatre/', views.theatreView, name='Theatre'),
			 #ex:/bookmyshow/Review
			 url(r'^Review/', views.reviewView, name='Review'),
			 #ex:/bookmyshow/Screen
			 url(r'^Screen/', views.screenView, name='Screen'),
			 #ex:/bookmyshow/Seatbooking
			 url(r'^Seatbooking/', views.seatbookingView, name='Seatbooking'),
			 #ex:/bookmyshow/Add/Audience
			 url(r'^Employee/',views.employeeview,name='Employeeview'),
			 #ex:del/ete through id
			 url(r'^Employeedelete/(?P<question_id>\d+)/',views.employeedelete,name='Employeedelete'),
			 #to update the data
			 url(r'^Employeeupdateclass/(?P<question_id>\d+)/',views.employeeUpdateView.as_view(),name='Employeeupdate'),
			 #

			 url(r'^Employeedeleteclass/(?P<question_id>\d+)/',views.employeeUpdateView.as_view(),name='Employeeupdate'),

			 url(r'^Employeefetchclass/',views.employeeUpdateViews.as_view(),name='Employeeupdate'),

			 url(r'^Employeeupdate/(?P<question_id>\d+)/',views.employeeupdate,name='Employeeupdate'),

			 url(r'^home/', HometemplateView.as_view(), name='home'),
]
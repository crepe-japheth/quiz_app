from django.urls import path
from .views import (
    QuizListView, 
    quiz_view, 
    index, 
    about,
    contact,
    appointment,
    courses,
    feature,
    team,
    not_found,
    testimonial,
    save_quiz_view,
    result,
    login_view,
    signup_view,
    )


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("courses/", courses, name="courses"),
    path("contact/", contact, name="contact"),
    path("appointment/", appointment, name="appointment"),
    path("contact/", contact, name="contact"),
    path("feature/", feature, name="feature"),
    path("team/", team, name="team"),
    path("testimonial/", testimonial, name="testimonial"),
    path("404/", not_found, name="not_found"),
    path("quiz/<pk>/", quiz_view, name="quiz"),
    path("quiz/<pk>/save", save_quiz_view, name="save_quiz"),
    path("quizes", QuizListView.as_view(), name="quizes"),
    path("result", result, name="result"),
    path("login", login_view, name="login"),
    path("signup", signup_view, name="signup"),
]

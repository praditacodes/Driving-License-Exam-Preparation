# from django.contrib import admin
# from django.urls import path
# from accounts import views as accounts_views
# from Quiz import views as quiz_views
# from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
# from django.conf import settings
# from Quiz import views

# urlpatterns = [
#     # Admin panel
#     path("admin/", admin.site.urls),
    
#     # Home page (Quiz Dashboard)
#     path("", quiz_views.home, name='home'),
#     path('profile/', quiz_views.profile, name='profile'), 
#     path('add-question/', quiz_views.add_question, name='add_question'),  # Corrected import

#     # Quiz-related URLs
#     path("quiz/", quiz_views.quiz_list, name='quiz_list'),
#     path("quiz/<int:pk>/", quiz_views.quiz_detail, name='quiz_detail'),
#     path("quiz/<int:pk>/start/", quiz_views.start_quiz, name='start_quiz'),
#     path("quiz/<int:pk>/submit/", quiz_views.submit_quiz, name='submit_quiz'),
#     path("quiz/results/", quiz_views.quiz_results, name='quiz_results'),
#     path("quiz/leaderboard/", quiz_views.leaderboard, name='leaderboard'),
#     path('edit-profile/', quiz_views.edit_profile, name='edit_profile'),
#     path('start_quiz/<int:pk>/', views.start_quiz, name='quiz_start'),  

#     # User Authentication (Signup, Login, Logout)
#     path("signup/", accounts_views.signup, name='signup'),  # Ensure this function exists in accounts/views.py
#     path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path("logout/", auth_views.LogoutView.as_view(), name='logout'),

#     # Password Reset
#     path("password_reset/", auth_views.PasswordResetView.as_view(
#         template_name='password_reset.html',
#         email_template_name='password_reset_email.html',
#         subject_template_name='password_reset_subject.txt'
#     ), name='password_reset'),
    
#     path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
#         template_name='password_reset_done.html'
#     ), name='password_reset_done'),
    
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
#         template_name="password_reset_confirm.html"
#     ), name="password_reset_confirm"),
    
#     path("reset/complete/", auth_views.PasswordResetCompleteView.as_view(
#         template_name='password_reset_complete.html'
#     ), name='password_reset_complete'),

#     # Password Change
#     path("settings/password/", auth_views.PasswordChangeView.as_view(
#         template_name='password_change.html'
#     ), name='password_change'),
    
#     path("settings/password/done/", auth_views.PasswordChangeDoneView.as_view(
#         template_name='password_change_done.html'
#     ), name='password_change_done'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from Quiz import views as quiz_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from Quiz import views

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # Home page (Quiz Dashboard)
    path("", quiz_views.home, name='home'),
    path('random-questions/', views.random_questions_view, name='random_questions'),
    
    # Profile and Edit Profile
    path('profile/', accounts_views.profile, name='profile'),  # Assuming profile is in accounts/views.py
    path('edit-profile/', accounts_views.edit_profile, name='edit_profile'),  # Assuming edit_profile is in accounts/views.py

    # Add Question (for admins)
    path('add-question/', quiz_views.add_question, name='add_question'),

    # Quiz-related URLs
    path("quiz/", quiz_views.quiz_list, name='quiz_list'),
    path("quiz/<int:pk>/", quiz_views.quiz_detail, name='quiz_detail'),
    path("quiz/<int:pk>/start/", quiz_views.start_quiz, name='start_quiz'),
    path("quiz/<int:pk>/submit/", quiz_views.submit_quiz, name='submit_quiz'),
    path("quiz/results/", quiz_views.quiz_results, name='quiz_results'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # User Authentication (Signup, Login, Logout)
    path("signup/", accounts_views.signup, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),

    # Password Reset
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='password_reset'),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

    # Password Change
    path("settings/password/", auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'
    ), name='password_change'),

    path("settings/password/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


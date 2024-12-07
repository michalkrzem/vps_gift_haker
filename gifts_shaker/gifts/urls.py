from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("all_gifts", views.gifts, name="all_gifts"),
    path("all_shakers", views.shakers, name="all_shakers"),
    path("new_shaker", views.create_shaker, name="new_shaker"),
    path("delete_shaker/<str:pk>/", views.delete_shaker, name="delete_shaker"),
    path(
        "new_shaker/add_person/<str:pk>/",
        views.add_person_to_shaker,
        name="add_person",
    ),
    path("new_shaker/shake/<str:pk>/", views.shake, name="shake"),
    path(
        "new_shaker/gifts_of_shaked_user/<str:pk>/",
        views.gifts_of_shaked_users,
        name="gifts_of_shaked_users",
    ),
    path("new_gift", views.create_gift, name="new_gift"),
    path("invite", views.create_invitation, name="invite"),
    path("all_invitations", views.invitations, name="all_invitations"),
    path(
        "all_invitations/invitation/delete/<str:pk>/",
        views.delete_invitation,
        name="delete_invitation",
    ),
    path(
        "all_gifts/gift/delete/<str:pk>/",
        views.delete_gift,
        name="delete_gift",
    ),
    path(
        "all_gifts/gift/update/<str:pk>/",
        views.update_gift,
        name="update_gift",
    ),
]

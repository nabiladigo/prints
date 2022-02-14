from django.urls import path 
from . import views

urlpatterns = [
    path('prints/', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('', views.PrintList.as_view(), name ="print_list"),
    path('prints/new/',  views.PrintCreate.as_view(), name="print_create"),
    path('prints/<int:pk>/', views.PrintDetail.as_view(), name="print_detail"),
    path('prints/<int:pk>/update',views.PrintUpdate.as_view(), name="print_update"),
    path('prints/<int:pk>/delete',views.PrintDelete.as_view(), name="print_delete"), 
    path('prints/<int:pk>/cards/new/', views.CardCreate.as_view(), name="card_create"),
    path('prints/<int:pk>/mugs/new/', views.MugCreate.as_view(), name="mug_create"),
    path('prints/<int:pk>/photos/new/', views.PhotoCreate.as_view(), name="photo_create"),
    path('prints/<int:pk>/puzzles/new/', views.PuzzleCreate.as_view(), name="puzzle_create"),
    path('giftset/<int:pk>/cards/<int:cards_pk>/', views.GiftSetCardAssoc.as_view(), name="giftset_card_assoc"),
    path('giftset/<int:pk>/cards/<int:cards_pk>/', views.GiftSetMugAssoc.as_view(), name="giftset_mug_assoc"),
    path('giftset/<int:pk>/cards/<int:cards_pk>/', views.GiftSetPhotoAssoc.as_view(), name="giftset_photo_assoc"),
    path('giftset/<int:pk>/cards/<int:cards_pk>/', views.GiftSetPuzzleAssoc.as_view(), name="giftset_puzzle_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # path('giftsets/<int:pk>/', views.GiftSetDetail.as_view(), name="giftset_detail"),
]
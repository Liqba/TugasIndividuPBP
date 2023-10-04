from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, show_detail, register, login_user, logout_user, edit_item, delete_item
from main.views import increase_item, decrease_item


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('show-detail', show_detail, name='show_detail'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
    path('increase_item/<int:id>/', increase_item, name='increase_item'),
    path('decrease_item/<int:id>/', decrease_item, name='decrease_item'),
]
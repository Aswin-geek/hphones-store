from django.urls import path
from hps_adm.views import *

urlpatterns = [
    path('adm_index',adm_index,name='adm_index'),
    path('adm_login',adm_login,name='adm_login'),
    path('view_cat',view_cat,name='view_cat'),
    path('view_brd',view_brd,name='view_brd'),
    path('view_prd',view_prd,name='view_prd'),
    path('add_cat',add_cat,name='add_cat'),
    path('up_cat<int:cid>',up_cat,name='up_cat'),
    path('up_brd<int:bid>',up_brd,name='up_brd'),
    path('up_prd<int:pid>',up_prd,name='up_prd'),
    path('up_var<int:pid>',up_var,name='up_var'),
    path('adm_logout',adm_logout,name='adm_logout'),
    path('add_brd',add_brd,name='add_brd'),    
    path('add_prd',add_prd,name='add_prd'),
    path('add_var',add_var,name='add_var'), 
    path('variant',variant,name='variant'),
    path('reports',reports,name='reports'),
    path('date_report',date_report,name='date_report'),
    path('week_report',week_report,name='week_report'),
    path('year_report',year_report,name='year_report'),
    path('veiw_report<int:order_id>',veiw_report,name='veiw_report'),
    path('add_ban',add_ban,name='add_ban'),
    path('banner',banner,name='banner'),
    path('up_ban<int:ban_id>',up_ban,name='up_ban'),
    path('ban_mgmt',ban_mgmt,name='ban_mgmt'),
]


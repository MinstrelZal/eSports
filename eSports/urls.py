"""eSports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from backend import views as backend_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    # user_info
    url(r'^user/register_login/$', backend_views.Register_Login, name='Register_Login'),
    url(r'^user/logout/$', backend_views.Logout, name='Logout'),
    url(r'^user/list/$', backend_views.User_List, name='User_List'),
    url(r'^user/add/$', backend_views.Add_User, name='Add_User'),
    url(r'^user/delete/$', backend_views.Delete_User, name='Delete_User'),
    url(r'^user/search/$', backend_views.Search_User, name='Search_User'),
    url(r'^user/alter/$', backend_views.Alter_User, name='Alter_User'),

    # esport_info
    url(r'^esport/list/$', backend_views.ESport_List, name='ESport_List'),
    url(r'^esport/add/$', backend_views.Add_ESport, name='Add_ESport'),
    url(r'^esport/delete/$', backend_views.Delete_ESport, name='Delete_ESport'),
    url(r'^esport/search/$', backend_views.Search_ESport, name='Search_ESport'),
    url(r'^esport/alter/$', backend_views.Alter_ESport, name='Alter_ESport'),

    # league_info & league_result
    url(r'^league/list/$', backend_views.League_List, name='League_List'),
    url(r'^league/add/$', backend_views.Add_League, name='Add_League'),
    url(r'^league/delete/$', backend_views.Delete_League, name='Delete_League'),
    url(r'^league/search/$', backend_views.Search_League, name='Search_League'),
    url(r'^league/alter/$', backend_views.Alter_League, name='Alter_League'),
    url(r'^league/result/list/$', backend_views.League_Result_List, name='League_Result_List'),
    url(r'^league/result/add/$', backend_views.Add_League_Result, name='Add_League_Result'),
    url(r'^league/result/delete/$', backend_views.Delete_League_Result, name='Delete_League_Result'),
    url(r'^league/result/search/$', backend_views.Search_League_Result, name='Search_League_Result'),
    url(r'^league/result/alter/$', backend_views.Alter_League_Result, name='Alter_League_Result'),

    # game_info
    url(r'^game/list/$', backend_views.Game_List, name='Game_List'),
    url(r'^game/add/$', backend_views.Add_Game, name='Add_Game'),
    url(r'^game/delete/$', backend_views.Delete_Game, name='Delete_Game'),
    url(r'^game/search/$', backend_views.Search_Game, name='Search_Game'),
    url(r'^game/alter/$', backend_views.Alter_Game, name='Alter_Game'),

    # club_info
    url(r'^club/list/$', backend_views.Club_List, name='Club_List'),
    url(r'^club/add/$', backend_views.Add_Club, name='Add_Club'),
    url(r'^club/delete/$', backend_views.Delete_Club, name='Delete_Club'),
    url(r'^club/search/$', backend_views.Search_Club, name='Search_Club'),
    url(r'^club/alter/$', backend_views.Alter_Club, name='Alter_Club'),

    # team_info
    url(r'^team/list/$', backend_views.Team_List, name='Team_List'),
    url(r'^team/add/$', backend_views.Add_Team, name='Add_Team'),
    url(r'^team/delete/$', backend_views.Delete_Team, name='Delete_Team'),
    url(r'^team/search/$', backend_views.Search_Team, name='Search_Team'),
    url(r'^team/alter/$', backend_views.Alter_Team, name='Alter_Team'),
]

from django.urls import path
#from django.conf.urls import url
#from django.views.generic.base import TemplateView

from . import views

app_name = "varasto"
urlpatterns = [
    # /varasto/ - etusivu
    path("", views.index, name="index"), 

    # /varasto/profiili - # TODO: Tee profiilisivu
    # path("profiili/<str:username>/", views.profiili, name="profiili"),

    # varasto/kirjaudu_ulos/
    path("kirjaudu_ulos/", views.kirjauduUlos, name="kirjauduUlos"),

    # Yksittäisten lainausten tiedot:
    # varasto/lainaus.html
    path("lainaus/<int:pk>/", views.lainaus, name="lainaus"),
    # varasto/lisatty_lainaus.html
    path("lisatty_lainaus/<int:pk>/", views.lisattyLainaus, name="lisattyLainaus"),

    # varasto/raportit.html
    path("raportit/", views.raportit, name="raportit"),
    
    # varasto/uusi_lainaus.html
    path("uusi_lainaus/", views.uusiLainaus, name="uusiLainaus"),

    # varasto/lainauksen_palautus.html
    path("lainauksen_palautus/", views.lainauksenPalautus, name="lainauksenPalautus"),
    # varasto/lisaa_muokkaa.html
    path("lisaa_muokkaa/", views.lisaaMuokkaa, name="lisaaMuokkaa"),
]
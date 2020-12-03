from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Login',views.Login,name='Login'),
    path('Registrar',views.Registrar,name='Registrar'),
    path('Precios',views.Precios,name='Precios'),
    path('Compra',views.Compra,name='Compra'),
    path('Guitarras',views.Guitarras,name='Guitarras'),
    path('Bajos',views.Bajos,name='Bajos'),
    path('Formulario',views.Formulario,name='Formulario'),
    path('instrumento/<str:pk>', views.InstrumentoDetailView.as_view(), name='instrumento-detail'),
    path('instrumentos/', views.InstrumentoListView.as_view(),name='instrumentos'),
    path('producto/<str:pk>', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/', views.ProductoListView.as_view(),name='productos'),


]

urlpatterns += [
    path('instrumento/create/', views.InstrumentoCreate.as_view(), name='instrumento_create'),
    path('instrumento/<str:pk>/update/', views.InstrumentoUpdate.as_view(), name='instrumento_update'),
    path('instrumento/<str:pk>/delete/', views.InstrumentoDelete.as_view(), name='instrumento_delete'),
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/<str:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/<str:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
] 
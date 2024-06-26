from django.urls import path
from .views import sensor_data_detail, servo_motor_state_detail,login_user,configuracion_detail,TransaccionesList,kilos_list_create,TransaccionDetail,KiloDetail,update_user,UserList,UserDetail,register, login, ProveedorList, ClienteList, ProductoList, canjear_puntos, consultar_puntos, register_proveedor, proveedor_profile, ProveedorDetail, ClienteDetail, ProductoDetail

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('loginuser/', login_user),
    path('proveedores/', ProveedorList.as_view(), name='proveedores-list'),
    path('usuarios/', UserList.as_view(), name='user-list'),
    path('usuarios/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
    path('clientes/', ClienteList.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('productos/', ProductoList.as_view(), name='productos-list'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='productos-detail'),
    path('canjear_puntos/', canjear_puntos, name='canjear-puntos'),
    path('consultar_puntos/<int:proveedor_id>/', consultar_puntos, name='consultar-puntos'),
    path('register_proveedor/', register_proveedor, name='register-prove'),
    path('profile_proveedor/', proveedor_profile, name='proveedor-profile'),
    path('kilos/', kilos_list_create, name='kilos-list'),
    path('kilos/<int:pk>/', KiloDetail.as_view() , name='kilo-detail'),
    path('transacciones/', TransaccionesList.as_view(), name='transaccion-list'),
    path('transacciones/<int:pk>/', TransaccionDetail.as_view(), name='transaccion-detail'),
    path('update-user/<int:pk>/', update_user, name='update-user'),
    path('configuracion/', configuracion_detail, name='configuracion'),
    path('sensor_data/', sensor_data_detail, name='sensor_data_detail'),
    path('servo_motor_state/', servo_motor_state_detail, name='servo_motor_state_detail'),
]

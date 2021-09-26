from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用 include() 将 users 应用的 urls 模块包含进来
    path('users/', include('users.urls'))
]

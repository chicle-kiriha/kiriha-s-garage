from django.shortcuts import render
from page.models import douban,jingdong,tianqiyubao

def dbindex(request):
    db_list=douban.objects.all()
    return render(request,'douban.html',{'db_list':db_list})
def jdindex(request):
    jd_list=jingdong.objects.all()
    return render(request,'jingdong.html',{'jd_list':jd_list})
def tqybindex(request):
    tqyb_list=tianqiyubao.objects.all()
    return render(request,'tianqiyubao.html',{'tqyb_list':tqyb_list})
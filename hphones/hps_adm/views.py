from django.shortcuts import render,redirect
from django.contrib import messages
from hps.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Count,Sum
from django.db.models.functions import ExtractMonth,ExtractYear
# Create your views here.

def adm_index(request):
    if request.user.is_superuser:
        item_count=OrderItem.objects.filter(status='Order Placed').count()
        total_revenue=OrderItem.objects.filter(status='Order Placed').aggregate(order_sum=Sum('sub_tot'))['order_sum'] or 0
        print(total_revenue)
        active_customers=User.objects.filter(is_active=True).count()
        order_counts = Order.objects.annotate(month=ExtractMonth('created_at')).annotate(year=ExtractYear('created_at')).values('year', 'month').annotate(count=Count('id'))
        month_counts = [0] * 12
        for entry in order_counts:
            month = entry['month']
            count = entry['count']
            month_counts[month - 1] = count
        context={'month_counts':month_counts,'item_count':item_count,'total_revenue':total_revenue,'active_customers':active_customers}
        return render(request,"adm/adm_index.html",context)
    else:
        return redirect(adm_login)
    

def adm_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        upass=request.POST.get("password")
        myuser=authenticate(username=uname,password=upass)
        if myuser is not None and myuser.is_superuser:
            login(request,myuser)
            # messages.success(request,"Login Success")
            return redirect(adm_index)
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/adm_login')
    return render(request,"adm/adm_login.html")

def view_cat(request):
    if request.user.is_superuser:
        cat=Category.objects.all()
        context={'cat':cat}
        return render(request,"adm/view_cat.html",context)
    else:
        return redirect(adm_login)

def view_brd(request):
    if request.user.is_superuser:
        brd=Brand.objects.all()
        context={'brd':brd}
        return render(request,"adm/view_brd.html",context)
    else:
        return redirect(adm_login)
    
def view_prd(request):
    if request.user.is_superuser:
        prd=Product.objects.all().select_related('brd_id','cat_id')
        context={'prd':prd}
        return render(request,"adm/view_prd.html",context)
    else:
        return redirect(adm_login)


def add_cat(request):
    if request.user.is_superuser:
        if request.method == "POST":
            cname=request.POST['name']
            cdesc=request.POST['desc']
            cimg=request.FILES['img']
            if Category.objects.filter(cat_name__iexact=cname).exists():
                messages.info(request,'Category already exists.')
            else:
                cat=Category(cat_name=cname,cat_desc=cdesc,cat_img=cimg,cat_status='True')
                cat.save()
                return redirect(view_cat)
        return render(request,"adm/add_cat.html")
    else:
        return redirect(adm_login)
    
def add_brd(request):
    if request.user.is_superuser:
        if request.method == "POST":
            bname=request.POST['name']
            bdesc=request.POST['desc']
            bimg=request.FILES['img']
            if Brand.objects.filter(brd_name__iexact=bname).exists():
                messages.info(request,'Brand already exists.')
            else:
                brd=Brand(brd_name=bname,brd_desc=bdesc,brd_img=bimg,brd_status='True')
                brd.save()
                return redirect(view_brd)
        return render(request,"adm/add_brd.html")
    else:
        return redirect(adm_login)

def adm_logout(request):
    logout(request)
    # messages.info(request,"Logout Success")
    return redirect(adm_login)

def up_cat(request,cid):
    cat=Category.objects.get(id=cid)
    if request.method =='POST':
        cname=request.POST['name']
        cimg=request.FILES.get('img')
        cat1=Category.objects.filter(cat_name__iexact=cname).exclude(id=cid)
        if cat1.exists():
            messages.info(request,'Category already exists.')
        elif cimg is None:
            cat.cat_name=request.POST['name']
            cat.cat_desc=request.POST['desc']
            cat.cat_status=request.POST['status']
            cat.save()
            return redirect(view_cat)
        else:
            cat.cat_name=request.POST['name']
            cat.cat_desc=request.POST['desc']
            cat.cat_img=request.FILES['img']
            cat.cat_status=request.POST['status']
            cat.save()
            return redirect(view_cat)
    return render(request,"adm/up_cat.html",{'cat':cat})

def up_brd(request,bid):
    brd=Brand.objects.get(id=bid)
    if request.method =='POST':
        bname=request.POST['name']
        bimg=request.FILES.get('img')
        brd1=Brand.objects.filter(brd_name__iexact=bname).exclude(id=bid)
        if brd1.exists():
            messages.info(request,'Brand already exists.')
        elif bimg is None:
            brd.brd_name=request.POST['name']
            brd.brd_desc=request.POST['desc']
            brd.brd_status=request.POST['status']
            brd.save()
            return redirect(view_brd)
        else:
            brd.brd_name=request.POST['name']
            brd.brd_desc=request.POST['desc']
            brd.brd_img=request.FILES['img']
            brd.brd_status=request.POST['status']
            brd.save()
            return redirect(view_cat)
    return render(request,"adm/up_brd.html",{'brd':brd})

def add_prd(request):
    cat=Category.objects.filter(cat_status=True)
    brd=Brand.objects.filter(brd_status=True)
    context={'cat':cat,'brd':brd}
    if request.user.is_superuser:
        if request.method == "POST":
            pname=request.POST['name']
            categ=request.POST['categ']
            brand=request.POST['brand']
            pdesc=request.POST['desc']
            war=request.POST['war']
            if Product.objects.filter(prd_name__iexact=pname).exists():
                messages.info(request,'Product already exists.')
            else:
                prd=Product(prd_name=pname,cat_id_id=categ,brd_id_id=brand,desc=pdesc,warr=war)
                prd.save()
                return redirect(view_prd)
        return render(request,"adm/add_prd.html",context)
    else:
        return redirect(adm_login)
    
    
def up_prd(request,pid):
    print(pid)
    prd=Product.objects.filter(id=pid).select_related('brd_id','cat_id')[0]
    cat=Category.objects.filter(cat_status=True)
    brd=Brand.objects.filter(brd_status=True)
    context={'cat':cat,'brd':brd,'prd':prd}
    if request.method =='POST':
        pname=request.POST['name']
        prd1=Product.objects.filter(prd_name__iexact=pname).exclude(id=pid)
        if prd1.exists():
            messages.info(request,'Product already exists.')
        else:
            prd.prd_name=request.POST['name']
            prd.brd_id_id=request.POST['brand']
            prd.cat_id_id=request.POST['categ']
            prd.warr=request.POST['war']
            prd.desc=request.POST['desc']
            prd.save()
            return redirect(view_prd)
    return render(request,"adm/up_prd.html",context)

def variant(request):
    if request.user.is_superuser:
        prd=PrdVariation.objects.all().select_related('prd_id')
        context={'prd':prd}
        return render(request,"adm/variation.html",context)
    else:
        return redirect(adm_login)
    
def add_var(request):
    prd=Product.objects.all()
    context={'prd':prd}
    if request.user.is_superuser:
        if request.method == "POST":
            prdt=request.POST['prdt']
            color=request.POST['color']
            stock=request.POST['stock']
            cprice=request.POST['cprice']
            mprice=request.POST['mprice']
            img1=request.FILES['img1']
            img2=request.FILES['img2']
            img3=request.FILES['img3']
            if PrdVariation.objects.filter(color__iexact=color,prd_id=prdt).exists():
                messages.info(request,'Variant already exists.')
            else:
                prd=PrdVariation(prd_id_id=prdt,color=color,stock=stock,cur_price=cprice,max_price=mprice,p1_img=img1,p2_img=img2,p3_img=img3,prd_status=True)
                prd.save()
                return redirect(variant)
        return render(request,"adm/add_var.html",context)
    else:
        return redirect(adm_login)
    
def up_var(request,pid):
    prdt=Product.objects.all()
    prd=PrdVariation.objects.filter(id=pid).select_related('prd_id')[0]
    print(prd)
    context={'prd':prd,'prdt':prdt}
    if request.user.is_superuser:
        if request.method == "POST":
            prd.prd_id_id=request.POST['prdt']
            prd.color=request.POST['color']
            prd.stock=request.POST['stock']
            prd.cur_price=request.POST['cprice']
            prd.max_price=request.POST['mprice']
            img1=request.FILES.get('img1')
            img2=request.FILES.get('img2')
            img3=request.FILES.get('img3')
            if img1:
                prd.p1_img=img1
            if img2:
                prd.p2_img=img2
            if img3:
                prd.p3_img=img3
            prd1=PrdVariation.objects.filter(color__iexact=prd.color,prd_id_id=prd.prd_id_id).exclude(id=pid)
            if prd1.exists():    
                messages.info(request,'Variant already exists.')
            else:
                prd.save()
                return redirect(variant)
        return render(request,"adm/up_var.html",context)
    else:
        return redirect(adm_login)
    

def reports(request):
    all_report=Order.objects.all().select_related('user')
    context={'all_report':all_report}
    return render(request,"adm/reports.html",context)

# def view_order(request,order_id):
#     selected_order=Or

def date_report(request):
    if request.method == "POST":
        selected_date=request.POST['selected_date']
        all_report=Order.objects.filter(created_at=selected_date)
        context={'all_report':all_report,'selected_date':selected_date}
        return render(request,"adm/date_report.html",context)
    return render(request,"adm/date_report.html")
    
def week_report(request):
    if request.method == "POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        all_report=Order.objects.filter(created_at__range=(start_date, end_date))
        context={'all_report':all_report,'start_date':start_date,'end_date':end_date}
        return render(request,"adm/week_report.html",context)
    return render(request,"adm/week_report.html")

def year_report(request):
    if request.method == "POST":
        selected_year=request.POST['selected_year']
        all_report=Order.objects.filter(created_at__year=selected_year)
        context={'all_report':all_report,'selected_year':selected_year}
        return render(request,"adm/year_report.html",context)
    return render(request,"adm/year_report.html")

def veiw_report(request,order_id):
    order_details=Order.objects.get(id=order_id)
    order_items=Order.objects.get(id=order_id).new_order.all().select_related('item')
    addrress=Address.objects.get(id=order_details.del_add_id)
    context={'order_details':order_details,'order_items':order_items,'addrress':addrress}
    if request.method == "POST":
        order_details.status=request.POST['status']
        order_details.save()
        return redirect(reports)
    return render(request,"adm/view_report.html",context)

def add_ban(request):
    if request.method == "POST":
        banner_name=request.POST['name']
        banner_image=request.FILES['img']
        new_banner=Banner(name=banner_name,ban_img=banner_image,status=False)
        new_banner.save()
    return render(request,"adm/add_ban.html")

def banner(request):
    ban=Banner.objects.all()
    return render(request,"adm/banner.html",{'ban':ban})

def up_ban(request,ban_id):
    ban=Banner.objects.get(id=ban_id)
    if request.method == "POST":
        banner_image=request.FILES.get('img')
        if banner_image:
            ban.name=request.POST['name']
            ban.ban_img=request.FILES.get('img')
            ban.status=request.POST['status']
            ban.save()
            return redirect(banner)
        else:
            ban.name=request.POST['name']
            ban.status=request.POST['status']
            ban.save()
            return redirect(banner)
    return render(request,"adm/up_ban.html",{'ban':ban})

def ban_mgmt(request):
    ban=Banner.objects.all()
    return render(request,"adm/ban_mgmt.html",{'ban':ban})
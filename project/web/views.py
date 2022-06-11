from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
import re
from django.contrib import messages
from .forms import Supplier, Spareparts
from django.http import HttpResponseRedirect
from django.urls import reverse
import math



def home(request):

    date_today = datetime.today()
    wait = import_wait.objects.all
    part = sparepart.objects.all
    submit = request.POST.get('submit')
    reset = request.POST.get('reset')
    test = request.POST.get('test')
    price_order = 0
    id_bill = 0
    get_sup = 0
    date_t = 0

    print(test,submit,reset)

    if submit:
        for i in range(10):
            for wi in wait():
                idim = wi.id_import

                if idim == submit:
                    import_part.objects.create(
                        id_import=wi.id_import,
                        sparepart=wi.sparepart,
                        quantity=wi.quantity,
                        price=wi.price,
                        DateTime=wi.DateTime,
                    )

                    quantity = sparepart.objects.get(id_code=wi.sparepart.id_code).quantity
                    quan_nu = quantity + wi.quantity

                    sparepart.objects.filter(id_code=wi.sparepart.id_code).update(
                        quantity=quan_nu,
                    )

                    price_order = price_order + wi.price
                    id_bill = wi.id_import
                    get_sup = wi.supplier
                    date_t = wi.DateTime

                    wi.delete()

            if i == 9:
                if price_order:
                    sparepart_order.objects.create(
                        id_import=id_bill,
                        supplier=get_sup,
                        price=price_order,
                        DateTime=date_t,
                    )

    elif reset:
        for wi in wait():
            idim = wi.id_import
            if idim == reset:
                print('98888888888888888888')
                wi.delete()

    zip_keep = []
    text_tall = []
    alert_all = []
    reorder_point = []
    sum_all = []
    text_all = []
    part_a = []
    keep = []
    store_all = []
    ex_mall = 0
    test = 0
    k = 0

    for w in wait():
        h = w.id_import
        store = w.supplier

        if k == h:
            print('-------------------------')
        else:
            k = h
            keep.append(k)
            store_all.append(store)
            zip_keep = zip(keep,store_all)
    import_id = request.GET.get('importid')

    if import_id:
        imp = import_wait.objects.filter(id_import=import_id)
        return render(request, 'import.html', {
            'imp': imp,
        })

    if part:
        for p in part():
            ex_qall = 0
            reorder = 0
            export_modate = export_part.objects.filter(sparepart=p)

            if export_modate:
                for exmp in export_modate:
                    price_im = p.Price_Per_Unit_Imp
                    ex_mp = exmp.price
                    ex_mall = ex_mall + ex_mp
                    ex_qp = exmp.quantity
                    ex_qall = ex_qall + ex_qp
                    EOQ_D = ex_qall * 12
                    EOQ_S = price_im
                    EOQ_H = 5
                    sum_EOQ = round(math.sqrt(2 * EOQ_D * EOQ_S / EOQ_H))
                    reorder = reorder + (ex_qall / 30 * 7)

                    reorder_p = math.ceil(reorder)
                    print('++++++++++++++++++++++', p)
                    if p.quantity <= reorder_p:
                        print('333333333333333333', p)
                        text = 'กรูณาสั่งสินค้าโดยด่วน'
                        test = 1
                        part_a.append(p)
                        text_all.append(text)
                        sum_all.append(sum_EOQ)
                        reorder_point.append(reorder_p)

            else:
                reorder_p = 1
                print('----------------',p)
                if p.quantity <= reorder_p:
                    print('333333333333333333',p)
                    text = 'กรูณาสั่งสินค้าโดยด่วน'
                    test = 1
                    part_a.append(p)
                    text_all.append(text)
                    sum_all.append(sum_EOQ)
                    reorder_point.append(reorder_p)

            zip_f = zip(part_a, sum_all, text_all)

        for wi in wait():
            for p in part_a:
                p_wi = wi.sparepart.id_code
                p_id = p.id_code
                if p_wi == p_id:
                    print(p_wi ,'+++++++++++', p_id)
                    text_t = 'อยู่ในรายการสั่งซื้อ'
                    alert_all.append(p)
                    text_tall.append(text_t)
            zip_a = zip(alert_all,text_tall)
            print(zip_a)

        return render(request, 'home.html', {
            'test': test,
            'zip': zip_f,
            'wait': zip_keep,
            'alert': zip_a,
        })

def dashboard(request):
    parts = sparepart.objects.all

    part_id = request.GET.get('partid')
    if part_id:
        part = sparepart.objects.filter(id_code=part_id)
        return render(request, 'part.html', {
         'part': part,
    })

    return render(request, 'dashboard.html', {
        'part': parts,
    })

def inventory(request):
    parts = sparepart.objects.all
    supplier_im =supplier.objects.all
    ex_part = import_part.objects.latest('id_import')

    now = request.POST.get('date')
    im_sup = request.POST.get('im_sup')
    id_bill = request.POST.get('id_bill')

    i = {9, 8, 7, 6, 5, 4, 3, 2, 1}
    date_today = datetime.today()
    date_t = date_today.strftime("%Y-%m-%d %H:%M:%S")
    date_now = date_today.strftime("%Y-%m-%d")
    price_all = 0

    part_s = []
    quan_s = []
    price_s = []

    exx = re.findall(r'\d+', ex_part.id_import)

    for num_ex in exx:
        for j in range(9999):
            number = str(j).zfill(4)
            if number == num_ex:
                j = j+1
                number2 = str(j).zfill(4)
                print(number2)
                ex_part2 = 'BM'+ number2
                print(ex_part2)
                break

    im = 'im_'
    quan = 'quan_'
    num = ['p' + str(num) * bool(num) for num in range(1,10)]

    for n in num:
        im_num = im + n
        quan_num = quan + n
        im_num = request.POST.get(im_num)
        quan_num = request.POST.get(quan_num)


        if im_num:
            if quan_num:
                if im_sup:
                    pp = sparepart.objects.get(id_code=im_num)
                    quantity = sparepart.objects.get(id_code=im_num).quantity
                    price = sparepart.objects.get(id_code=im_num).Price_Per_Unit_Imp
                    suppli = supplier.objects.get(name=im_sup)

                    quan_n = int(quan_num)
                    quan_nu = quantity + quan_n

                    price_ex = price * quan_n
                    price_all = price_all + price_ex

                    import_wait.objects.create(
                        id_import=ex_part2,
                        sparepart=pp,
                        supplier=suppli,
                        quantity=quan_num,
                        price=price_ex,
                        DateTime=now,
                    )

                    part_s.append(pp)
                    quan_s.append(quan_num)
                    price_s.append(price_ex)
                    zip_f = zip(part_s, quan_s,price_s)

                else:
                    messages.info(request, 'กรุณาใส่ supplier')
                    break

            else:
                messages.info(request, 'กรุณาใส่จำนวน')
                break

    if part_s:
        return render(request, 'paperim.html', {
            'supplier': suppli,
            'spare': part_s,
            'ex_part2': ex_part2,
            'zip': zip_f,
            'price_total': price_all,
        })

    return render(request,'inventory.html',{
        'date_now': date_now,
        'part': parts,
        'supplier_im': supplier_im,
        'ex_part': ex_part2,
        'i': i,
    })

def product(request):
    parts = sparepart.objects.all
    ex_part = export_part.objects.latest('id_bill')
    car = customer_car.objects.order_by('license')


    now = request.POST.get('date')
    license_ex = request.POST.get('license')
    name_ex = request.POST.get('name')
    phone = request.POST.get('phone')
    charges = request.POST.get('charge')


    exx = re.findall(r'\d+', ex_part.id_bill)

    date_today = datetime.today()
    date_t = date_today.strftime("%Y-%m-%d %H:%M:%S")
    date_now = date_today.strftime("%Y-%m-%d")
    price_all = 0

    for num_ex in exx:
        for i in range(9999):
            number = str(i).zfill(4)
            if number == num_ex:
                i = i+1
                number2 = str(i).zfill(4)
                print(number2)
                ex_part2 = 'BE'+ number2
                print(ex_part2)
                break

    ex = ['ex_']
    quan = ['quan_']
    num = ['p'+ str(num)*bool(num) for num in range(10)]

    for n in num:
        for e in ex:
            for q in quan:
                ex_num = e+n
                quan_num = q+n
                ex_num = request.POST.get(ex_num)
                quan_num = request.POST.get(quan_num)

                if ex_num:
                    if quan_num:
                        if license_ex:

                            pp = sparepart.objects.get(id_code=ex_num)
                            quantity = sparepart.objects.get(id_code=ex_num).quantity
                            price = sparepart.objects.get(id_code=ex_num).Price_Per_Unit

                            quan_n = int(quan_num)
                            quan_nu = quantity-quan_n

                            price_ex = price*quan_n

                            price_all = price_all+price_ex

                            sparepart.objects.filter(id_code=ex_num).update(
                                quantity=quan_nu
                            )

                            spare = export_part.objects.create(
                                id_bill=ex_part2,
                                sparepart=pp,
                                quantity=quan_num,
                                price=price_ex,
                                DateTime=now,
                            )

                            bill_b = export_bill.objects.create(
                                id_bill=ex_part2,
                                part_all=spare,
                            )

                            for c in car:
                                print(c)
                                str_c = str(c)
                                if license_ex == str_c:
                                    messages.success(request, 'success')

                                else:
                                    if name_ex:
                                        customer_car.objects.update_or_create(
                                            license=license_ex,
                                            name=name_ex,
                                            number=phone,
                                        )
                                        messages.success(request, 'success')

                                    else:
                                        name_ex = 'บิลเงินสด'
                                        phone = '0'
                                        customer_car.objects.update_or_create(
                                            license=license_ex,
                                            name=name_ex,
                                            number=phone,
                                        )
                                        messages.success(request, 'success')

                        else:
                            messages.info(request, 'กรุณาใส่เลขทะเบียน')
                            break
                    else:
                        messages.info(request,'กรุณาระบุจำนวน')
                        break

    p9 = 'p9'
    if n == p9:
        if price_all:
            customers = customer_car.objects.get(license=license_ex)
            float_c = float(charges)
            price_total = price_all + float_c

            bill.objects.create(
                id_bill=bill_b,
                customer_Car=customers,
                fixing_Charge=charges,
                sparepart_price=price_all,
                total_Charge=price_total,
                DateTime=date_t,
            )

            part_s = export_part.objects.filter(id_bill=ex_part2)
            return render(request, 'paper.html', {
                'charges': charges,
                'customer': customers,
                'spare': part_s,
                'ex_part2': ex_part2,
                'price_total': price_total,
            })

    i = {9,8,7,6,5,4,3,2,1}
    return render(request,'product.html',{
        'car': car,
        'date_now': date_now,
        'part': parts,
        'ex_part': ex_part2,
        'i' : i,
    })

def analysis(request):
    date_today = datetime.today()
    date_now = date_today.strftime("%Y-%m-%d")

    import_date = import_part.objects.filter(DateTime=date_now)
    export_date = export_part.objects.filter(DateTime=date_now)

    im_all = 0
    for imp in import_date:
        im_p = imp.price
        im_all = im_all + im_p

    ex_all = 0
    for exp in export_date:
        ex_p = exp.price
        ex_all = ex_all + ex_p

    part = sparepart.objects.all

    reorder_point = []
    sum_all =[]
    text_all = []
    part_a = []
    ex_mall = 0

    print(part)

    if part:
        for i in range(30):
            date_mo = date_today - timedelta(days=i)

            for p in part():
                ex_qall = 0
                reorder = 0
                export_modate = export_part.objects.filter(sparepart=p)

                if export_modate:
                    for exmp in export_modate:
                        price_im = p.Price_Per_Unit_Imp
                        ex_mp = exmp.price
                        ex_mall = ex_mall + ex_mp
                        ex_qp = exmp.quantity
                        ex_qall = ex_qall + ex_qp
                        EOQ_D = ex_qall*12
                        EOQ_S = price_im
                        EOQ_H = 5
                        sum_EOQ = round(math.sqrt(2*EOQ_D*EOQ_S/EOQ_H))
                        reorder = reorder + (ex_qall/30*7)

                        reorder_p = math.ceil(reorder)
                        if p.quantity <= reorder_p:
                            text = 'กรูณาสั่งสินค้าโดยด่วน'
                        elif reorder_p + 5 > p.quantity > reorder_p:
                            text = 'สินค้าใกล้หมด'
                        else:
                            text = 'ปกติ'

                else:
                    reorder_p = 1
                    if p.quantity <= reorder_p:
                        text = 'กรูณาสั่งสินค้าโดยด่วน'
                    elif reorder_p + 5 > p.quantity > reorder_p:
                        text = 'สินค้าใกล้หมด'
                    else:
                        text = 'ปกติ'

                part_a.append(p)
                text_all.append(text)
                sum_all.append(sum_EOQ)
                reorder_point.append(reorder_p)

                zip_f = zip(part_a,reorder_point,sum_all,text_all)

            return render(request, 'analysis.html', {
                'zip_f' : zip_f,
                'im_all': im_all,
                'ex_all': ex_all,
                'ex_mall': ex_mall,
            })

def add_supplier(request):
    form = Supplier()
    if request.method == 'POST':
        form = Supplier(request.POST, request.FILES)
        if form.is_valid():
            sup = form.save(commit=False)
            sup.save()
            form.save()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('inventory', kwargs={}))
        messages.error(request, 'Save failed')

    return render(request,'paper2.html',{
        'form': form,
    })

def add_sparepart(request):
    form = Spareparts()
    if request.method == 'POST':
        form = Spareparts(request.POST, request.FILES)
        if form.is_valid():
            sup = form.save(commit=False)
            sup.save()
            form.save()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('product', kwargs={}))
        messages.error(request, 'Save failed')

    return render(request,'add_sparepart.html',{
        'form': form,
    })

# Create your views here.

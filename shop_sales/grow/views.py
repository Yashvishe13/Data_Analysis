from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from unicodedata import category
import pandas as pd

def convert_to_csv(products):
    dataset = pd.DataFrame(columns=['date', 'product_name', 'category', 'quantity', 'selling_price', 'cost_price', 'customer_name', 'customer_age', 'customer_gender', 'total', 'revenue', 'total_rev'])
    
    for product in products.iterator():
        date = product.date
        product_name = product.product_name
        category = product.category
        quantity = product.quantity
        selling_price = product.selling_price
        cost_price = product.cost_price
        customer_name = product.customer_name
        customer_age = product.customer_age
        customer_gender = product.customer_gender
        total = selling_price * quantity
        revenue = selling_price - cost_price
        total_rev = revenue * quantity
        
        dataset = dataset.append({'date': date, 'product_name': product_name, 'category': category, 'quantity': quantity, 'selling_price': selling_price, 'cost_price': cost_price, 'customer_name': customer_name,'customer_age': customer_age, 'customer_gender': customer_gender, 'total': total, 'revenue': revenue, 'total_rev': total_rev}, ignore_index=True)
        
        dataset.to_csv('grow/data/dataset.csv', index=False)
        
def sales_per_month():
    df = pd.read_csv("grow/data/dataset.csv")
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
    df = df.groupby(pd.Grouper(key='date', freq='m')).sum()
    df.to_csv('df.csv')
    return df
    
def sales_per_year():
    df = pd.read_csv("grow/data/dataset.csv")
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
    df = df.groupby(pd.Grouper(key='date', freq='Y')).sum()
    df.to_csv('df_Y.csv')
    return df

def recent_transactions():
    df = pd.read_csv("grow/data/dataset.csv")
    return df

def gender_wise_sales():
    df = pd.read_csv("grow/data/dataset.csv")
    gws = df.groupby(['customer_gender']).sum()
    gender_sales = gws.total
    return gender_sales 
    
def category_wise_sales():
    df = pd.read_csv("grow/data/dataset.csv")
    cws = df.groupby(['category']).sum()
    category_sales = cws.total
    return category_sales

def age_groups_sales():
    df = pd.read_csv("grow/data/dataset.csv")
    age_groups = pd.cut(df['customer_age'], bins=[8,12,16,20,25,30,40,65,100])
    aws = df.groupby(age_groups)['total'].sum()
    return aws

def total_revenue():
    df = pd.read_csv("grow/data/dataset.csv")
    df['revenue'] = df.selling_price - df.cost_price
    return df.revenue.sum()

def total_sales():
    df = pd.read_csv("grow/data/dataset.csv")
    return df.selling_price.sum()
    
def data_entry(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grow:dashboard')
    else:
        form = ProductForm()

    context = {
        "form": form,
    }

    return render(request, 'grow/data_entry.html', context)


def grow_about(request):
    return render(request, 'grow/grow_about.html')


@login_required
def dashboard(request):
    products = Product.objects.all()

    form = ProductForm(request.POST)

    convert_to_csv(products)
    df = sales_per_month()
    
    values = df.total
    u_months = list(values.index)
    months = []
    prices = []
    u_prices = list(values.values)
    for i in range(0, len(u_months)):
        if str(u_months[i]).split()[0].split('-')[0] == '2022':
            months.append(str(u_months[i]).split()[0])
            prices.append(int(u_prices[i]))
    print(months)
    print(prices)
    
    df = sales_per_year()
    values = df.total
    u_months = list(values.index)
    y_months = []
    for i in range(0, len(u_months)):
            y_months.append(str(u_months[i]).split()[0])
    costs = list(values.values)
    y_prices = []
    for cost in costs:
        y_prices.append(int(cost))

    df = recent_transactions()
    recent = []
    for i  in range(len(df) - 1, len(df) - 6, -1):
        recent.append({ 'date': df.date[i], 'product_name': df.product_name[i], 'category': df.category[i], 'quantity': df.quantity[i],  'customer_name': df.customer_name[i], })

    gws = gender_wise_sales()
    gender = list(gws.index)
    g_sales = list(gws.values)
    
    cws = category_wise_sales()
    category = list(cws.index)
    c_sales = list(cws.values)
    
    aws = age_groups_sales()
    age_categories = []
    c = list(aws.index)
    for i in range(0, len(aws.index)):
        age_categories.append(str(aws.index[i]))
    age_sales = list(aws.values)
    print(age_sales)
    print(age_categories)
    
    
    context = {
        "months": months,
        "prices": prices,
        "y_months": y_months,
        "y_prices": y_prices,
        "form": form,
        "recents": recent,
        "gender": gender,
        "gws" : g_sales,
        "category": category,
        "cws": c_sales,
        "age_categories": age_categories,
        "age_sales": age_sales,
        "total_revenue": total_revenue,
        "total_sales": total_sales,
    }

    return render(request, 'grow/index.html', context)




def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'grow/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'grow/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'grow/edit.html', context=context)
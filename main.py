from entities.my_model_s import My_model_s
from entities.my_semi import My_semi
from entities.stock import Stock
from entities.purchasingAdvices import PurchasingAdvices
from helpers.calculatePurchasingAdvices import CalculatePurchasingAdvices
from helpers.dbHelper import DbHelper

from flask import Flask,render_template,request,url_for,redirect


from dotenv import load_dotenv
import os


app=Flask(__name__,template_folder='templates')



@app.route("/")
def home():
    sales_orders=dbHelper.readSalesOrders()
    stock_info=dbHelper.readStock()
    stock=Stock()
    purchasing_advices=PurchasingAdvices()
    
    for item in stock_info:
        setattr(stock, item[1], float(item[2]))

    for order in sales_orders:
        count=int(order[2])-int(order[3])
        calculate_advices=CalculatePurchasingAdvices(order[1], count, stock, purchasing_advices)
        calculate_advices.calculateWheelQuantity()
        calculate_advices.calculateSteeringWheelQuantity()
        calculate_advices.calculateSeatQuantity()
        calculate_advices.calculateMirrorQuantity()
        calculate_advices.calculateLcdMonitor()
        
    datas=calculate_advices.getData()
    return render_template("index.html",datas=datas)

@app.route("/stock")
def stockPage():
    # datas = db.session.execute(db.select(Stock))
    # datas=Stock.query.filter_by().all()
    
    datas=dbHelper.readStock()

    return render_template("stock.html", datas=datas)

@app.route("/sales_orders")
def salesOrders():
    datas=dbHelper.readSalesOrders()

    return render_template("sales_orders.html",datas=datas)

@app.route("/new_sales_order",methods=['POST','GET'])
def addNewSalesOrder():
    if request.method=="POST":
        # Get the data from the form

        code = request.form['code']
        total = request.form['total']
        shipped = request.form['shipped']
        orderNo = request.form['orderNo']
        dbHelper.insertNewSalesOrder(code, total, shipped, orderNo)
        # Redirect to the home page
        return redirect(url_for("salesOrders"))
    else:
        sales_orders=dbHelper.readSalesOrders()
        return render_template("new_sales_order.html")

@app.route("/edit_sales_order",methods=['POST','GET'])
def editSalesOrdder():
    if request.method=="POST":
        # Get the data from the form

        code = request.form['code']
        total = request.form['total']
        shipped = request.form['shipped']
        orderNo = request.form['orderNo']
        dbHelper.updateSalesOrders(code, total, shipped, orderNo)
        # Redirect to the home page
        return redirect(url_for("salesOrders"))
    else:
        sales_orders=dbHelper.readSalesOrders()
        datas=dbHelper.readSalesOrders()
        return render_template("edit_sales_order.html",datas=datas)

@app.route("/edit_stock",methods=['POST','GET'])
def editStock():
    if request.method=="POST":
        stock_info=dbHelper.readStock()
        # Get the data from the form
        for item in stock_info:
            quantity = request.form[item[1]]
            dbHelper.updateStock(item[1], quantity)
        # Redirect to the home page
        return redirect(url_for("stockPage"))
    else:
        sales_orders=dbHelper.readSalesOrders()
        stock_info=dbHelper.readStock()
        
        return render_template("edit_stock.html",stock_info=stock_info)

if __name__=="__main__":
    dbHelper=DbHelper()
    app.run(debug=True)
    dbHelper.closeConnection()

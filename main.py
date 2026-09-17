from pyscript import document, display

def create_order(e):
       document.getElementById("output2").innerHTML ="" #clears previous result

       prod1 = document.getElementById("item1")
       prod2 = document.getElementById("item2")
       prod3 = document.getElementById("item3")
       prod4 = document.getElementById("item4")
       prod5 = document.getElementById("item5")
       #Calculate
       size = document.getElementById("extra")
       price = float(size.value) 
       
       subtotal = (float(prod1.value) * prod1.checked +float(prod2.value) * prod2.checked +float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked +float(prod5.value) * prod5.checked)
       taxrate = 0.12
       tax=subtotal * taxrate  #the product of subtotal and taxrate
       grandtotal = subtotal + tax + price
       display(grandtotal, target="output2")


       

       
       

def place_order(e):
       document.getElementById("output3").innerHTML ="" #clears previous result
       initial_order = document.getElementById("output2")
       initial_price = float(initial_order.innerHTML.replace("<div>", "").replace("</div>", "")) #get the initial price
       display(initial_price, target="output3") #display price

def show_order(e):
       document.getElementById("output4").innerHTML = "" # clears previous result
       prod1=document.getElementById("item1") #get item 1 id
       subtotal= float(prod1.value) * prod1.checked
       size = document.getElementById("extra")
       price = float(size.value)
       grandtotal = subtotal + price
       order = document.getElementById("output3")
       final_order_price = float(order.innerHTML.replace("<div>", "").replace("</div>", "")) #get the final price
       final_order = round(grandtotal + final_order_price, 2)
       display(f'Your total is  ₱{final_order}, come again! ', target="output4")
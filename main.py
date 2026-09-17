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
       display(f"|Subtotal: ₱{subtotal} |Tax: ₱{tax} |Grand Total: ₱{grandtotal}", target="output2")


       

       
       

def place_order(e):
       document.getElementById("output3").innerHTML ="" #clears previous result

       display(f"Order placed successfully!", target="output3") #display initial price

def show_order(e):
       document.getElementById("output4").innerHTML = "" # clears previous result

       prod1 = document.getElementById("item1")
       prod2 = document.getElementById("item2")
       prod3 = document.getElementById("item3")
       prod4 = document.getElementById("item4")
       prod5 = document.getElementById("item5")

       size = document.getElementById("extra")
       price = float(size.value)

       subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)

       tax = subtotal * 0.12

       grandtotal = subtotal + tax + price

       display(f"Your total is ₱{grandtotal}. Thank you for your purchase!", target="output4")
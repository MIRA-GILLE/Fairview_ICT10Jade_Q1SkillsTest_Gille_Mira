from pyscript import document, display

def add_num(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 + num2
        display(result, target="output1") #display result


def create_order(e):
       document.getElementById("output2").innerHTML ="" #clears previous result

       prod1=document.getElementById("item1") #get item 1 id
       #Calculate
       subtotal=float(prod1.value) * prod1.checked 
       size = document.querySelector("input[name='size']:checked")
       price = float(size.value) 
       grandtotal = subtotal + price
       display(grandtotal, target="output2")

       subtotal = (float(prod1.value) * prod1.checked +                        float(prod2.value) * prod2.checked +        #continue here)Create  a variable for tax rateCreate a variable that gets the product of subtotal and taxrateCreate a variable for the grandtotal
       

def place_order(e):
       document.getElementById("output3").innerHTML ="" #clears previous result
       coffee = document.getElementById("coffee")
       coffee_price = float(coffee.value)
       display(coffee_price, target="output3") #display coffee price

def show_order(e):
       document.getElementById("output4").innerHTML = "" # clears previous result
       prod1=document.getElementById("item1") #get item 1 id
       subtotal= float(prod1.value) * prod1.checked
       size = document.querySelector("input[name='size']:checked")
       price = float(size.value)
       grandtotal = subtotal + price
       coffee = document.getElementById("coffee")
       coffee_price = float(coffee.value)
       final_order = grandtotal + coffee_price
       display(f'You have to pay a total of {final_order}', target="output4")
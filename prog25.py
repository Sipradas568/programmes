res= [{"testcase": "Logintest", "status":"Pass"},
      {"testcase": "Orderpage", "status":"Fail"},
      {"testcase": "Cartpage", "status":"Fail"},
    {"testcase": "PaymentPage", "status":"Pass"},
    {"testcase": "Confirmationpage", "status":"Fail"}
      ]
lst2= []
ctr=0
ctr2= 0
for i in res:
    if i["status"]=="Fail":
        ctr= ctr+1
        lst2.append(i["testcase"])
    else:
        ctr2= ctr2+1
print("No of test cases failed", ctr)
print("No of test cases Passed", ctr2)
print(lst2)

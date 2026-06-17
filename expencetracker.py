print("""===========================================
          PERSONAL EXPENCE TRACKER
 ===========================================
         1.Add New Expense
         2.View All Expense
         3.Category Summary
         4.Set/Check Budget
         5.Search Expense
         6.Exit
  ===========================================""")
expences=[]
categories=["food","transport","entertainment","shopping","bills","others"]
while True:
  choice=int(input("Enter your choice (1-6):"))

  if choice==1:
    print("Add New Expense")
    temp=','.join(categories)
    print(f"enter categories:{temp}")
    category=input("Enter Category:").lower()
    amount=float(input("Enter Amount:"))
    description=input("Enter Description:")
    expence={}
    expence["category"]=category
    expence["amount"]=amount
    expence["description"]=description
    expences.append(expence)
    print("Expense added successfully")
    print("your expence as follow")
    for i in expences:
      print(i["category"],i["amount"],i["description"])
  elif choice==2:
    print("="*20)
    print("View All Expences".center(20))
    print("="*20)

    num=1
    sum=0
    for i in expences:
      print(f"#{num} {i['category']} | {i['amount']} | {i['description']}")
      num=num+1
      sum = sum + i['amount']
    print("="*20)
    print(f"The total amount is {sum}")
  elif choice==3:
    summary_cat={}
    for i in categories:
      summary_cat[i]=0
    print("category summary")
    categories_sum=0
    for i in expences:
        item=i["category"].lower()
        amount=i["amount"]
        summary_cat[item]=summary_cat[item]+amount
    for i,j  in summary_cat.items():
      if j!=0:
        print(f"{i} : {j}")
        categories_sum=categories_sum + j
    print('='*20)
    print(f"total amount is {categories_sum}")

  elif choice==4:
    print("Set/Check Budget")
  elif choice==5:
    print("Search Expense")
  elif choice==6:
    print("Exit")
    break
  else:
    print("invalid choice, Please try again")
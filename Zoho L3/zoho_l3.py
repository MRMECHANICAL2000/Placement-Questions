#class to store user Data
class User:
	#Default User Details
	defautlDetail={"admin":["admin",True],"vignesh":["Admin@123",False],"akash":["password",False]}

	def __init__(self):
		print("[Message] : User class constructor")
		self.userData={}
		for i in User.defautlDetail.keys():
			self.userData[i]={"password":hash(User.defautlDetail[i][0]),"TotalBalance":1000,"FreeCred":300,"isAdmin":User.defautlDetail[i][1]}
		print()
		User.info()

	def userInfo(self):
		print("Details of User:")
		print("user : password")
		for key,val in self.userData.items():
			print("{} : {}".format(key,val))
		print()		

	@staticmethod
	def info():
		print("Details of User:")
		print("user : password")
		for key,val in User.defautlDetail.items():
			print("{} : {}".format(key,val))
		print()

#class to store food Data
class Food(User):

	#To store default items
	defaultData={}
	defaultItemName=["Dosa","Idli","Masala_Dosa","Vada","Pongal"]
	defaultItemCount=[5,15,3,10,8]
	defaultPricePerUnit=[30,10,50,10,25]
	defaultUnitPerUser=["Unlimited","Unlimited","1","2","Unlimited"]


	def __init__(self):
		super().__init__()
		print("[Message] : Food class constructor")
		self.foodData={}
		Food.InitiateDefault()
		temp=self.RestoreDefault()
		for i in temp.keys():
			self.foodData[i]={"item":i,"availableCount":temp[i][0],"pricePerUnit":temp[i][1],"unitsPerUser":temp[i][2]}
		print()
		Food.info()


	def foodInfo(self):
		print("Details of Food:")
		print()
		for key,val in self.foodData.items():
			print("{} {} ".format(key, val))
		print()

	@classmethod
	def InitiateDefault(cls):
		for idx,val in enumerate(Food.defaultItemName):
			Food.defaultData[val]=[Food.defaultItemCount[idx],Food.defaultPricePerUnit[idx],Food.defaultUnitPerUser[idx]]

	
	def RestoreDefault(self):
		return(Food.defaultData)

	@staticmethod
	def info():
		print("Details of Food:")
		print()
		for key,val in Food.defaultData.items():
			print("{}  {}  {}  {}".format(key, val[0],val[1],val[2]))
		print()


#class to do operation on data
class Task(Food):
	def __init__(self):
		super().__init__()

	def validateUser(self,user,password):
		try:
			self.userData[user]
			if self.userData[user]["password"]==hash(password):
				print("Welcome {}".format(user))
				return (self.userData[user]["isAdmin"])
			else:
				password=input("Please Retype the password :")
				return(self.validateUser(user,password))

		except:
			print("Invalid User Details")
			return(None)



	def addUser(self,user,password):
		try:
			self.userData[user]={"password":hash(password),"TotalBalance":0,"FreeCred":0,"isAdmin":False}
			print("User {} Added successfully".format(user))
			print()			
		except:
			print("Invalid Detail entered to Add User")
			print()			

	def addFoodItem(self):
		try:
			item=input("Enter the Item Name : ")
			availableCount=input("Enter Available Count : ")
			pricePerUnit=input("Enter Price Per Unit : ")
			unitsPerUser=input("Enter the Max Units Per User : ")
			self.foodData[item]={"item":item,"availableCount":int(availableCount),"pricePerUnit":int(pricePerUnit),"unitsPerUser":unitsPerUser}
			print("Item {} Added successfully".format(item))
			print()						
		except:
			print("Invalid Detail entered to Add Food Item")
			print()			

	def modifyFoodItem(self):
		try:
			item=input("Enter the Item Name : ")
			print("What would you like to Modify")
			print("Press 1 to Modify Available Count ")
			print("Press 2 to Modify Price Per Unit")
			print("Press 3 to Modify Units Per User")
			toModify=int(input())

			if toModify==1:
				self.foodData[item]["availableCount"]=int(input("Enter the Value : "))
			elif toModify==2:
				self.foodData[item]["pricePerUnit"]=int(input("Enter the Value : "))
			elif toModify==3:
				self.foodData[item]["unitsPerUser"]=input("Enter the Value : ")
			print("Item {} Modify successfully".format(item))
			print()			
		except:
			print("Invalid Details Entered to Modify items")
			print()			

	def deleteFoodItem(self):
		try:
			item=input("Enter the Item Name : ")
			self.foodData[item]
			print("Item {} has been deleted from library successfully".format(item))
			print()			
		except:
			print("Invalid Details Entered to Delete items")			
			print()			


	def addMoneyToUser(self):
		try:
			userName=input("Enter an User Name: ")
			Balance=int(input("Enter the Amount"))
			self.userData[userName]["TotalBalance"]+=Balance
			print("Balance Amount of Rs.{} added to {} Account successfully".format(Balance,userName))
			print()			
		except:
			print("Invalid Details Entered to Add Balance to User")
			print()			

	def viewBalance(self,userName):
		try:
			print("Balane {} in {}".format(self.userData[userName]["TotalBalance"],userName))
		except:
			print("Invalid Details Entered to check Balance")

	def orderFood(self,userName,token,TodayOrder):
		orderList=[]
		idVal=1
		temp=0
		while True:
			try:
				item=input("Please Enter an Food Name : ")
				count=int(input("Please Enter the count of food to buy :"))

				if self.foodData[item]["unitsPerUser"]!="Unlimited":
					if count>int(self.foodData[item]["unitsPerUser"]):
						print("You can't buy {} more than {}".format(item,self.foodData[item]["unitsPerUser"]))
						continue

				if self.userData[userName]["TotalBalance"]<count*self.foodData[item]["pricePerUnit"]:
					print("You did not have enough balance to buy {} , {} times".format(item,count))
					continue

				if self.foodData[item]["availableCount"]>=count:
					self.foodData[item]["availableCount"]-=count
					self.userData[userName]["TotalBalance"]-=count*self.foodData[item]["pricePerUnit"]
					self.userData[userName]["FreeCred"]=max(0,self.userData[userName]["FreeCred"]-count*self.foodData[item]["pricePerUnit"])				 	
				else:
					print("The Available count is {} less that required Count {}".format(self.foodData[item]["availableCount"],count))
					continue
				orderList.append([idVal,item,count*self.foodData[item]["pricePerUnit"]])	
				idVal+=1

			except:
				print("Invalid Details Entered to Order Food")
			try:
				temp=int(input("Press 1 to stop Purchase and Show Bill : \nPress 2 to continue Purchase : "))			
			except:
				pass
			if temp==1:
				break


		print("Token No: {}".format(token))
		for i in orderList:
			print("id: {}  item: {} cost: {}".format(i[0],i[1],i[2]))
		TodayOrder.append(orderList)




	def info(self):
		self.userInfo()
		self.foodInfo()


#Main Function

task=Task()
token=1
TodayOrder=[]

while True:
	print("Welcome to Zoho Canteen:")
	user=input("User Name :")
	password=input("password :")

	isAdmin=task.validateUser(user,password)
	if isAdmin==None:
		try:
			x=int(input(" Press 1. Would you like to signIn with this Detail  \n Press 2 to login Again :\n"))
			if x==1:
				task.addUser(user,password)
			else:
				continue
		except:
			print("Invalid No entered !!!!")

	elif isAdmin:
		print("Perform Any following operations for Admin: ")
		while True:
			print()			
			print("Press 1 to add Food Item")
			print("Press 2 to Modify Food Item")
			print("Press 3 to delete Food Item :")
			print("Press 4 Add money to users account")
			print("Press 5 to Logout :")
			print()			
			temp=int(input())
			if temp==1:
				task.addFoodItem()
			elif temp==2:
				task.modifyFoodItem()
			elif temp==3:
				task.deleteFoodItem()
			elif temp==4:
				task.addMoneyToUser()
			elif temp==5:
				break
			else:
				print("Please Enter an Valid Number!!!!!")
	else:
		print("What do you want to do?: ")
		while True:
			print()			
			print("Press 1 to View Balance")
			print("Press 2 to Order Food")
			print("Press 3 to Logout :")
			print()			
			temp=int(input())
			if temp==1:
				task.viewBalance(user)
			elif temp==2:
				task.orderFood(user,token,TodayOrder)
				token+=1

			elif temp==3:
				break
			else:
				print("Please Enter an Valid Number!!!!!")
	task.info()
	if int(input(("Pless 1 to close Canteen and show bill and Update Default:")))==1:
		print(TodayOrder)
		task.__init__()
		task.info()
		break
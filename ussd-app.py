from flask import Flask, request
import africastalking
import os

app = Flask(__name__)

username = "sandbox"
api_key = "acf6afa94b14298fcb067238ca5f99b8ecbc3d8df64f925ad9cf348663f3b84a"

africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods = ['POST', 'GET'] )
def ussd_callback():
	global response
	session_id = request.values.get("sessionId", None)
	service_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phoneNumber", None)
	text = request.values.get("text", "default")
	sms_phone_number = []
	sms_phone_number.append(phone_number)


	#USSD logic
	if text == "":
		#print main menu
		response = "CON What would you like to do?\n"
		response += "1. Buy farm produce\n"
		response += "2. Sell farm produce\n"
		response += "3. Learn professional farming\n"
		response += "4. Seek agricultural/extension services\n"

	elif text == "1":
		#print sub-menu 1
		response = "CON What would you like to buy?\n"
		response += "1. Grains\n"
		response += "2. Fruits\n"
		response += "3. Vegetables\n"
		response += "4. Poultry products\n"
		response += "5. Dairy products\n"

	elif text == "2": 
		#print sub-menu 1
		response = "CON What would you like to sell?\n"
		response += "1. Grains\n"
		response += "2. Fruits\n"
		response += "3. Vegetables\n"
		response += "4. Poultry products\n"
		response += "5. Dairy products\n"

	elif text == "3": 
		#print sub-menu 1
		response = "CON What would you like to learn?\n"
		response += "1. How to cultivate Beans\n"
		response += "2. How to cultivate Maize\n"
		response += "3. How to cultivate Wheat"
		response += "4. How to cultivate Tomatoes\n"
		response += "5. How to cultivate Vegetables\n"
		response += "6. How to cultivate Bananas\n"
		response += "7. How to cultivate Avocado\n"
		response += "8. How to cultivate Mangoes\n"
		response += "9. How to cultivate Macademia nuts\n"
		response += "10. How to cultivate Groundnuts\n"
		response += "11. Poultry keeping\n"
		response += "12. Dairy farming\n"
		response += "13. Bee keeping\n"
		response += "14. Pig farming"

	elif text == "4":
		try:

			#send sms with the number to call for extension service
			#send sms to extension officer from farmer seeking services
			sms_response_farmer = sms.send("Call this number: {}".format(phone_number) + "Thank you for using this service.", sms_phone_number)
			sms_response_extension_officer = sms.send("Farmer seek your services: {}".format(phone_number) + "Thank you for using this service.", sms_phone_number)
			print(sms_response_farmer)
			print(sms_response_extension_officer)

		except Exception as e:
			#print error
			print(f"Oops! we have a problem: {e}")
			
	elif text == "1*1":
		#sub-menu 1 sub-menu 1 -> buy grains
		## 1 -> 1
		seller_phone_number = "+254721234567"
		selling_price_wheat = "ksh5000.00 per 90kg bag"
		selling_price_beans = "ksh6000.00 per 90kg bag"
		selling_price_maize = "ksh3000.00 per 90kg bag"
		selling_price_millet = "ksh11000.00 per 90kg bag"
		selling_price_sorgham = "ksh5500.00 per 90kg bag"

		response = "CON Choose Grains to buy:\n"
		response += "1. Wheat @ {}".format(selling_price_wheat) + "\n"
		response += "2. Beans @ {}".format(selling_price_beans) + "\n"
		response += "3. Maize @ {}".format(selling_price_maize) + "\n"
		response += "4. Millet @ {}".format(selling_price_millet) + "\n"
		response += "5. Sorgham @ {}".format(selling_price_sorgham) + "\n"

	elif text == "1*2":
		#sub-menu 1 sub-menu 2 -> buy fruits
		## 1 -> 2
		seller_phone_number = "+254721234567"
		selling_price_bananas = "ksh500.00 - bunch"
		selling_price_oranges = "ksh1000.00 - 90kg bag"
		selling_price_mangoes = "ksh2000.00 - 90kg bag"
		selling_price_watermelon = "ksh600.00 - half dozen(six pieces)"
		selling_price_avocado = "ksh200.00 - dozen"

		response = "CON Choose Fruits to buy:\n"
		response += "1. Bananas @ {}".format(selling_price_bananas) + "\n"
		response += "2. Oranges @ {}".format(selling_price_oranges) + "\n"
		response += "3. Mangoes @ {}".format(selling_price_mangoes) + "\n"
		response += "4. Watermelon @ {}".format(selling_price_watermelon) + "\n"
		response += "5. Avocado @ {}".format(selling_price_avocado) + "\n"

	elif text == "1*3":
		#sub-menu 1 sub-menu 3 -> buy vegetables
		## 1 -> 3
		seller_phone_number = "+254721234567"
		selling_price_spinach = "ksh500.00 - 90kg bag"
		selling_price_kales = "ks400.00 - 90kg bag"
		selling_price_tomatoes = "ksh1800.00 - crate"
		selling_price_cabbages = "ksh200.00 - half dozen(six pieces)"
		selling_price_bulb_onions = "ksh1200.00 - crate"

		response = "CON Choose Vegetables to buy:\n"
		response += "1. Spinach @ {}".format(selling_price_spinach) + "\n"
		response += "2. Kales @ {}".format(selling_price_kales) + "\n"
		response += "3. Tomatoes @ {}".format(selling_price_tomatoes) + "\n"
		response += "4. Cabbages @ {}".format(selling_price_cabbages) + "\n"
		response += "5. Bulb Onions @ {}".format(selling_price_bulb_onions) + "\n"

	elif text == "1*4":
		#sub-menu 1 sub-menu 4 -> buy poultry products
		## 1 -> 4
		seller_phone_number = "+254721234567"
		selling_price_eggs = "ksh300.00 - crate"
		selling_price_broilers = "ksh500.00 - 1 chicken"

		response = "CON Choose chicken product to buy:\n"
		response += "1. Eggs @ {}".format(selling_price_eggs) + "\n"
		response += "2. Broillers @ {}".format(selling_price_broilers) + "\n"

	elif text == "1*5":
		#sub-menu 1 sub-menu 5 -> buy dairy products
		## 1 -> 5
		seller_phone_number = "+254721234567"
		selling_price_cow_milk = "ksh40.00 - litre"
		selling_price_goat_milk = "ksh40.00 - litre"

		response = "CON Choose Dairy product to buy:\n"
		response += "1. Cow Milk @ {}".format(selling_price_cow_milk) + "\n"
		response += "2. Goat Milk @ {}".format(selling_price_goat_milk) + "\n"



	else:
		response = "END Invalid input. Try again."

	return response

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.environ.get("PORT"))


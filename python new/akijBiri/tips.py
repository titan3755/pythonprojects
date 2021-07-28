import math

print(f"""
Welcome to tips calculator! Enter the amount in this form: $99.99 . The tips for 18%, 20%, 25% shall be displayed.
        """)
input_bill = input("What's the total bill for today? \n\n> ")
def calculate(value):
        output = str(value).replace('$', '')
        if float(output):
                output_flt = float(output)
                result_18_tip = round(output_flt * 18/100)
                result_20_tip = round(output_flt * 20/100)
                result_25_tip = round(output_flt * 25/100)
                print(f"The tips for 18% is ${result_18_tip}, totaling to ${round(result_18_tip + output_flt)}\nThe tips for 20% is ${result_20_tip}, totaling to ${round(result_20_tip + output_flt)}\nThe tips for 25% is ${result_25_tip}, totaling to ${round(result_25_tip + output_flt)}")
        else:
                print('Invalid Values!')
calculate(input_bill)
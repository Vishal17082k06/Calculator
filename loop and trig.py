import math
print("Hello!")
print("Supported operations(+,-,/,,*,//,%,(),|,&,^,>>,<<)")
print("Trig functions: sin(x), cos(x), tan(x) (x in radians)")
print("Logarithmic functions: log(x) (base 10), log2(x), log10(x), ln(x) (natural log)")
print("Type 'END' to exit the calculator.")
while True:
    e=input("Enter your calculation: ").strip()
    if e.upper() == "END":
        print("Exited")
        break
    try:
         print(eval(e,math.__dict__))
    except:
        print("Unexpected format/character recognised please try again")


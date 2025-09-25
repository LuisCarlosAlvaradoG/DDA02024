print("Enter values, fin to stop:")  # (Ejemplo demostrativo)
acc = 0.0
count = 0
val = input("Value (or fin): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or fin): ")
if count == 0:
    print("No numbers entered")
else:
    print("Sum:", acc, "| Avg:", acc / count)

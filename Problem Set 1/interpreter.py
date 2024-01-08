x,y,z = input("Expression: ").split(" ")
match y:
    case "+":
        e = float(x) + float(z)
        print(f"${e:.1f}")
    case "-":
        e = float(x) - float(z)
        print(f"${e:.1f}")
    case "*":
        e = float(x) * float(z)
        print(f"${e:.1f}")
    case "/":
        if(z != 0):
            e = float(x) / float(z)
            print(f"${e:.1f}")

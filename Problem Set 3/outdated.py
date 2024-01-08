def main():
    m = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
        ]
    while True:
        try:
            d = input("Date: ").title()
            if('/' in d):
                month,day,year = d.split('/')
                month,day,year = int(month),int(day),int(year)
                if((month>12) or (day>31) or year>2023):
                    continue
            else:
                month,day,year= d.split(" ")
                year = int(year)
                if(day.endswith(',')):
                    day=int(day.removesuffix(','))
                    if(day>31):
                        continue
                else:
                    continue

                for i in range(len(m)):
                    if(m[i]==month):
                        month = i+1
                    else:
                        continue

            print(f"{year:4}"+"-"+f"{month:02}"+"-"+f"{day:02}")
            break
        except ValueError:
            continue

main()

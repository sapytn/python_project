skl = int(input("СКОЛЬКА ПРОЦЕНТАВ?:"))
if skl % 10 == 1 and skl != 11:
    print(f"{skl} процент")
elif 1 < (skl % 10) < 5 and (skl < 5 or skl > 20):
    print(f"{skl} процента")
else:
    print(f"{skl} процентов")

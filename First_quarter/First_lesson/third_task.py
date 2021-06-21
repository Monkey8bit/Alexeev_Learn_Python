for percent in range(1, 21):
    ending = ""
    if percent < 2:
        ending = "процент"
        print(percent, ending)
    elif 2 <= percent < 5:
        ending = "процента"
        print(percent, ending)
    else:
        ending = "процентов"
        print(percent, ending)

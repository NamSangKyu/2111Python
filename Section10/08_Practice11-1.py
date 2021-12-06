def vendin_machine(money):
    count = 0
    while money >= 0:
        print(f'음료수 = {count}, 잔돈 = {money}')
        money -= 700
        count += 1

vendin_machine(3000)

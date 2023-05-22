def solve(meal, tip, tax):
    print(round(meal * (100+tip+tax)/100))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)
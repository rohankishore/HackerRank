def bonAppetit(bill, anna_didnot_eat, b):
    bill.remove(bill[anna_didnot_eat])
    bill_sum = sum(bill)
    b_actual = bill_sum//2   # cost_per_person
    overcharged = b - b_actual
    
    if b != b_actual:
        print(overcharged)
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    anna_didnot_eat = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, anna_didnot_eat, b)

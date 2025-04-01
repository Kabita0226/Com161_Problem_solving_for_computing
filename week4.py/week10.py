def sum_even_number():
    num=int(input("Enter Even Number: "))
    if num % 2 !=0:
        print("that's not an even number.")
        return
    even_sum = sum(range(2, num +1, 2))
    print(f"The sum of all even numbers up to {num} is: {even_sum}")
sum_even_number()
a = 1
while(a):
    def is_perfect_number(n):
        divisors = []
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i < n // i:
                    divisors.append(n // i)
        divisors.sort()
        divisors.remove(n)
        
        divisor_sum = sum(divisors)
        if divisor_sum == n:
            return divisors

    number = int(input())
    if (number != -1):
    
        perfect_divisors = is_perfect_number(number)

        if perfect_divisors:
            divisors_str = " + ".join(map(str, perfect_divisors))
            print(f"{number} = {divisors_str}")
        else:
            print(f"{number} is NOT perfect.")
    else:
        a = 0
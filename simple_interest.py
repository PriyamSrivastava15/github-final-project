def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate, and time."""
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (% per annum): "))
    t = float(input("Enter time period (years): "))
    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest: {si}")

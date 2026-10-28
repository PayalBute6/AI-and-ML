"""
Assignment 3 (Set B - Q1)
Title: Cryptarithmetic Problem Solver using CSP Approach
Description: Solves the classic verbal arithmetic puzzle 'SEND + MORE = MONEY' using 
             Constraint Satisfaction Problem (CSP) backtracking with all-different and 
             arithmetic constraints.
"""

def solve_cryptarithmetic():
    print("=" * 60)
    print("CRYPTARITHMETIC CSP SOLVER: SEND + MORE = MONEY")
    print("=" * 60)

    # All unique letters in the puzzle
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    digits = list(range(10))

    # Assigned mapping: {letter: digit}
    assignment = {}
    used_digits = set()

    def is_consistent():
        """Evaluates arithmetic equation once all letters are assigned."""
        s = assignment['S']
        e = assignment['E']
        n = assignment['N']
        d = assignment['D']
        m = assignment['M']
        o = assignment['O']
        r = assignment['R']
        y = assignment['Y']

        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

        return send + more == money

    def backtrack(index=0):
        # Base case: All letters assigned
        if index == len(letters):
            if is_consistent():
                return True
            return False

        current_letter = letters[index]

        for digit in digits:
            # Leading letter constraint: S and M cannot be 0
            if current_letter in ('S', 'M') and digit == 0:
                continue

            # All-Different constraint
            if digit in used_digits:
                continue

            # Assign
            assignment[current_letter] = digit
            used_digits.add(digit)

            # Early pruning check: In SEND + MORE = MONEY, M must be 1 since S+M <= 9+1=10
            if 'M' in assignment and assignment['M'] != 1:
                del assignment[current_letter]
                used_digits.remove(digit)
                continue

            if backtrack(index + 1):
                return True

            # Undo assignment (Backtrack)
            del assignment[current_letter]
            used_digits.remove(digit)

        return False

    if backtrack(0):
        print("SOLUTION FOUND!")
        print("-" * 60)
        for letter in letters:
            print(f"  Letter '{letter}' = {assignment[letter]}")
        print("-" * 60)

        s = assignment['S']
        e = assignment['E']
        n = assignment['N']
        d = assignment['D']
        m = assignment['M']
        o = assignment['O']
        r = assignment['R']
        y = assignment['Y']

        send_val = s * 1000 + e * 100 + n * 10 + d
        more_val = m * 1000 + o * 100 + r * 10 + e
        money_val = m * 10000 + o * 1000 + n * 100 + e * 10 + y

        print(f"  Mathematical Proof:")
        print(f"    SEND   :  {send_val}")
        print(f"  + MORE   : +{more_val}")
        print(f"  ---------------------")
        print(f"    MONEY  : {money_val}")
        print(f"\nVerification: {send_val} + {more_val} == {money_val} -> {send_val + more_val == money_val}")
    else:
        print("No valid solution found!")
    print("=" * 60)

if __name__ == "__main__":
    solve_cryptarithmetic()

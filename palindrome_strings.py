words = input().split()
palindrome = input()

palindromes = [word for word in words if word == word[::-1]]
found_palindrome = palindromes.count(palindrome)

print(f"{palindromes}\n"
      f"Found palindrome {found_palindrome} times")
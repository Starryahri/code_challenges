Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
    - Separate name string into first name string and last name string to manipulate
        - We can use the split() method: returns a list of the separated 
            - "Ahria Nicholas".split(" ")
- Find the vowel and consonant count for each name
    - For first name find vowel and consonant count
    - For second name find vowel and constant count
    - Possibly can do this by comparing each letter to a list of vowels and if it doesn't equal one of them then its a consonant. Increase consonant count else increase vowel count.
        - For loop comparing to a tuple of vowels
            - first name cosonant count, vowel count
            - last name constonatn count, vowel count
            - vowels = ("a", "e", "i", "o", "u")
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
    - Compare the vowel and consonant counts between the names, use which ever is smaller. Multiply by the length of the smallest name.
        - Compare which first name vowel count to last name vowel count
        - EX: "Ahria" Vowels = 3, Consonants = 2, Length = 5
                "Nicholas" Vowels = 3, Consonants = 5, Length = 8
                small_v_mult_c = 6
                small_name = 5
                total=30
        - EX: "John" Vowels = 1, Consonants = 3, Length = 4
                "Doe" Vowels = 2, Consonants = 1, Length = 3
                small_v_mult_c = 1
                small_name = 3
                total = 3
- Do the same for the two larger counts and the larger name
    - Same thing with the largest vowel and consonant counts and then multiply by the length of the larger name.
    - Ahria
        - big_v_mult_c = 15
        - big_name = 8
        - total = 120
    - John
        - big_v_mult_c = 6
        - big_name = 4
        - total = 24
- Subtract the smaller value from the larger one to get their lucky number
    - Subtract smaller value from larger value to get lucky number
        - Ahria
            - 120-30 = 90
        - John
            - 24-3 = 1
    - if final lucky number is actually 0 return instead 13. (heh lucky number 13)
If the final value is zero (`0`), return `13`.

Chloe Perez

chloe - v=2, c=3, len=5
perez - v=2, c=3, len=5
small_v_mult_c=6
big_v_mult_c=6
# Assignment 1 
Write a program that takes some data as string input. Then it tries to find a positive number **x** such that when x is appended to the end of the string, the **SHA256** hash of this new string is less than the **target**, which is **0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF**.
Also print the **time** it takes to get this nonce value. 


I have **start** variable as the reference for start time. I set the **target** variable as **0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF**, took input string in the variable **inp**, and starting from **x**=1 appended x at the end of inp and checked it's hash value then incremented x by 1 till I got the first positive integer that satisfies the condition of having SHA256 hash value of the string produced less than target.

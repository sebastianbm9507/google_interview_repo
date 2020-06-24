0x07 - Google interview
Mock interviews are multi-purpose:
It helps you and the staff understand where you stand in terms of general knowledge
It helps you and the staff understand where you stand in terms of technical skills
It is a training for interviews
Mock interviews - How-to

Before starting the mock interview, please read these instructions. Don't share this page with the candidate
When you are done, please click on "I'm ready!" and let's start the mock interview.
Whiteboarding
Find a pair of numbers which sum equals to a another number
We are going to give you a collection of numbers numbers. You have to find a pair of those numbers which sum equals to another given number sum.
What you don’t tell the candidate, but answer her/him when she/he asks for clarification:
Numbers in the collection are sorted, all integers, and can be either negative or positive.
You should return True (there is a pair) or False (there is no pair)
Example 1:
numbers: [1, 2, 3, 9] sum: 8 -> there isn’t a pair of number which sum is equal to 8. Return False
Example 2
numbers: [1, 2, 4, 4] sum: 8 -> there is a pair of number which sum is equal to 8: 4, and 4. Return True
Instructions:
Level 1
0.0 Naive brute force - 10%
Going through all possible combinations.
For each n in numbers:
   For each m in numbers:
      Test if n + m = `sum`

OR
For each n in numbers:
   For each m in numbers after n:
      Test if n + m = `sum`

Follow-up question:
What is the time complexity of this algorithm? => O(n^2)
This is not fast enough. Can you find a faster solution?
-> if the candidate can not find anything, give him an advice on how to do better. See 0.1
0.1 loop + binary search - 20%
Since it’s sorted you can look for the “complement” number to the current number you are looking at in the collection with a binary search.
For each n in numbers:
   Find the complement in the rest of the array with binary search

Follow-up question:
What is the time complexity of this algorithm? => O(nlogn)
This is not fast enough. Can you find a faster solution?
-> if the candidate can not find anything, give him an advice on how to do better. See 0.2
0.2 using two indexes - 50%
If the candidate hasn’t found anything better than O(nlogn). Ask her/him: "What if you had two pointers or indexes, one starting from the beginning and the other one starting from the end. Could you find a better solution using this?"
It is possible to move the two indexes to get to the sum faster.
The idea is you start with the first and last. You do the sum, and:
If the sum is smaller than the sum you are looking for, then you move the lower index to the right (++)
If the sum is greater than the sum you are looking for, then you move the higher index to the left (--)
If sum == sum then you have found it
You stop the loop when high index <= low index
Follow-up question:
What is the time complexity of this algorithm? => O(n)
Level 2
If the candidate can find the best solution in Level 1 you can move on to this question. Otherwise stop.
Ask the candidate: What if the array is not sorted?
0.3 sort and do the same as 0.2 - 60%
Follow-up question:
What is the time complexity of this algorithm? => O(nlogn)
0.4 using a hash table of hash set - 100%
As we go through the collection, we can store the numbers we went through, and look into them to see if we have seen the right number to get the required sum when added to the current number we are looking at. We want to store to a hash table or a hash set because they are supposed to have an constant time of insertion and lookup (we do not want to use an array or list or anything that has a O(n) complexity for insertion or lookup).
Example: [1, 2, 3, 6, 4, 7, 5, 9], sum = 10
Step 1
Hash set = []
Number = 1
-> can’t find a 9 in the hash set
Strore 1 to the hash set
Step 2
Hash set = [1]
Number = 2
-> Can’t find a 8 in the hash set
Store 2 in the hash set
Step 3
Hash set = [1, 2]
Number = 3
-> Can’t find a 7 in the hash set
Store 3 in the hash set
Step 3
Hash set = [1, 2, 3]
Number = 6
-> Can’t find a 4 in the hash set
Store 6 in the hash set
Step 4
Hash set = [1, 2, 3, 6]
Number = 4
-> Found a 6 in the hash set
Note that you can also store the “complement” to sum in the hash set and look for the current number in the hash set.
Follow-up question:
What is the time complexity of this algorithm? => O(n)
What is the space complexity of this algorithm? => Θ(n)
# google_interview_repo

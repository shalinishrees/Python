"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains . The second line contains an array of integers each separated by a space.
Constraints
Output Format
Print the runner-up score."""

n = int(input())
    arr =list(map(int, input().split()))
    largest_number=-100
    second_largest=-100

    for x in arr:
        if x>largest_number:
            second_largest=largest_number
            largest_number=x
        elif x==largest_number:
            pass
        elif x>second_largest:
            second_largest=x
    print(second_largest)

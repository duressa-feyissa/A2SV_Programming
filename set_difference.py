# Enter your code here. Read input from STDIN. Print output to STDOUT
NO_ENGLISH = int(input())
eng_list = list(map(int, input().split()))
NO_FRENCH = int(input())
fre_list = list(map(int, input().split()))

eng_set = set(eng_list)
fre_set = list(fre_list)

intersection = len(eng_set.intersection(fre_set))
number = len(eng_set) - intersection
print(number)

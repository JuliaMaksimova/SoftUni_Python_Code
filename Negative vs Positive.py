def compare(positive_list,negative_list):
    sum_of_positive = sum(positive_list)
    sum_of_negative = sum(negative_list)
    print(f"{sum_of_positive}\n{sum_of_negative}")
    if sum_of_positive>abs(sum_of_negative):
        return "The positive are stronger than the negative"
    return "The negatives are stronger than the positives"


numbers = [int(num) for num in input().split()]

negative = []
positive = []

for num in numbers:
    if num<0:
        negative.append(num)
    elif num>0:
        positive.append(num)

print(compare(positive,negative))



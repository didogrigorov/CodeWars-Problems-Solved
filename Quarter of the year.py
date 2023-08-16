def quarter_of(month):
    # your code here
    quarters = {
        "first_quarter": [1,2,3],
        "second_quarter": [4,5,6],
        "third_quarter": [7,8,9],
        "fourth_quarter": [10,11,12]
    }
    result = [i for i in quarters if month in quarters[i]]
    return result

print(quarter_of(5))
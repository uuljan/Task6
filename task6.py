"""
@Makers
Write a function bigger_guy that takes in wo numbers and returns the bigger one.
Ex: bigger_guy(10, 20) # --> 20
"""
def bigger_guy(one, two):
    return max(one, two)
#write your code here ...
#DO NOT remove lines below here, this is designed to test your code.
def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20

    assert bigger_guy(10, 10) == 10
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_bigger_guy()
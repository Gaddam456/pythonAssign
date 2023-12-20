# # filter(function, sequence)
# list_a = [1, 3, -4, 6, 5]
# def is_positive(n):
#     return n > 0
# filter_obj = filter(is_positive, list_a)
# print(list(filter_obj))
# print(list(filter(lambda n: n%2==0 and n>0, list_a)))
list_b = ['sai', 'ravi', 'raju', 'ramu', 'sita', 'lakshman', 'hanuman']
print(list(filter(lambda n: len(n)==4 and n.startswith('r') and n.endswith('u'), list_b)))
# map(function, sequence)
def cube_num(n):
    return n ** 3
# ['1', '2', '3', '4', '5', '6']
int_input = list(map(int, input().split())) #[1,2,3,4,5,6]
map_obj = map(cube_num, int_input)
print(list(map_obj))
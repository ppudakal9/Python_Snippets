def rotateImage(a):
    row = len(a)
    rotate_layers = int(row / 2)
    col = len(a[0])

    for cell in range(0, rotate_layers):
        start_loc = cell
        end_loc = col - cell - 1

        # traverse each layer from left to right, top to bottom and then move to the next layer
        for current in range(start_loc, end_loc):
            diff = current - start_loc
            # fetch all 4 corners of the current layer
            top_left = a[start_loc][current]
            top_right = a[current][end_loc]
            bottom_left = a[end_loc - diff][start_loc]
            bottom_right = a[end_loc][end_loc - diff]

            print(top_left, " ", top_right)
            print(bottom_left, " ", bottom_right)

            # swap the elements with the ones on their right
            a[start_loc][current] = bottom_left
            a[current][end_loc] = top_left
            a[end_loc - diff][start_loc] = bottom_right
            a[end_loc][end_loc - diff] = top_right

    return a


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(rotateImage(a))
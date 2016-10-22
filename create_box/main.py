"""This is the entry point of the program."""


def create_box(height, width, character):

# return character * width
# return character * height
    
    if height > 1 and width > 1:
        for i in range(0, width):
            print (character * height)
    
            
    else:
        return "box is too small"

        


if __name__ == '__main__':
    create_box(3, 4, '*')

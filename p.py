def draw_tree(height):
    # Draw the leaves of the tree
    for i in range(height):
        # Calculate spaces to center the stars
        print(' ' * (height - i - 1) + '#' * (2 * i + 1))
    
    # Draw the trunk (centered)
    for t in range(2):
        print(' ' * (height - 1) + '||')

# Set how tall you want your tree to be
draw_tree(10)
draw_tree(3*2)

# Function to draw the mirrored right-angled triangle
def mirrored_right_triangle(n):
    for i in range(1, n+1):
        # Print leading spaces
        for j in range(n-i):
            print(" ", end="")
        # Print stars for the right-angle triangle part
        for j in range(i):
            print("*", end="")
        # Move to the next line
        print()

# Input from Radhika
n = int(input("Enter the height of the mirrored right-angled triangle: "))

# Call the function to draw the triangle
mirrored_right_triangle(n)

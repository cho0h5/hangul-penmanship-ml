import cv2

img = cv2.imread("pre-image.png")
print("image size:", img.shape)
print("input: x y width height x_count y_count item_square_size")
n = input().split(" ")

x = int(n[0])
y = int(n[1])
width = int(n[2])
height = int(n[3])
x_count = int(n[4])
y_count = int(n[5])
item_square_size = int(n[6])

# Draw main rectangle
cv2.rectangle(img, (x, y), (x+width, y+height), (200, 0, 0), 2)

# Draw items rectangle
for 



cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

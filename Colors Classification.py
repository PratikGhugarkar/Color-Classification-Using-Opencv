# importing required modules
import cv2
import pandas as pd

# Reading the image with opencv
img = cv2.imread('Sample.png')

# resize img
img = cv2.resize(img, (550, 350))

# declaring global variables (are used later on)
Clicked = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global b, g, r, xpos, ypos, clicked
        Clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', drawFunction)

while 1:

    cv2.imshow("image", img)
    if Clicked:

        cv2.rectangle(img, (20, 20), (500, 60), (b, g, r), -1)

        text = getColorName(r, g, b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

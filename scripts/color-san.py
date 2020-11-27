import cv2
import numpy as np 
import pickle
import os

def emptyFun():
    pass

def detect_color_contour_centers(frame, x, y):
    if frame[x][y] == 0:
        return True
    else:
        return False
    

def check_whether_lit(frame, x, y):
    if frame[x][y]==0:
        return True
    else:
        return False
    

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    w = "sasa"
    cv2.namedWindow(w)
    cv2.createTrackbar("h", w, 0,179,emptyFun)
    cv2.createTrackbar("s", w, 0,255,emptyFun)
    cv2.createTrackbar("v", w, 0,255,emptyFun)
    cv2.createTrackbar("H", w, 0,179,emptyFun)
    cv2.createTrackbar("S", w, 0,255,emptyFun)
    cv2.createTrackbar("V", w, 0,255,emptyFun)
    cords_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rect_info.pkl")
    with open(cords_path, mode='rb') as file:
        kords = pickle.load(file)
    print("File loaded successfully")


    lower_reed = np.array([0,10,10], dtype=np.uint8)
    higher_reed = np.array([10,255,255], dtype=np.uint8)

    lower_red = np.array([160,10,10], dtype=np.uint8)
    higher_red = np.array([179,255,255], dtype=np.uint8)

    #[59,62,14],[75,255,255]
    lower_green = np.array([59,62,14], dtype=np.uint8)
    higher_green = np.array([75,255,255], dtype=np.uint8)
    #[105,123,82], [118,255,255]
    lower_blue = np.array([105,123,82], dtype=np.uint8)
    higher_blue = np.array([118,255,255], dtype=np.uint8)

    #[30,23,200], [48,255,255]
    

    while(1):
        h = cv2.getTrackbarPos("h", w)
        s = cv2.getTrackbarPos("s", w)
        v = cv2.getTrackbarPos("v", w)
        H = cv2.getTrackbarPos("H", w)
        S = cv2.getTrackbarPos("S", w)
        V = cv2.getTrackbarPos("V", w)
        ret, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        red0 = cv2.inRange(hsv_frame, lower_reed, higher_reed)
        red1 = cv2.inRange(hsv_frame, lower_red, higher_red)

        red = cv2.bitwise_or(red0, red1)
        

        green = cv2.inRange(hsv_frame, lower_green, higher_green)
        blue = cv2.inRange(hsv_frame, lower_blue, higher_blue)



        _ = cv2.bitwise_or(red, green)
        mask = cv2.bitwise_or(_, blue)
        
    

        for i in sorted(kords.keys()):
            x, y = (int(kords[i][0][0][0])+int(kords[i][2][0][0]))//2, (int(kords[i][0][0][1])+int(kords[i][2][0][1]))//2 
            #print(center_x, center_y, sep=' ')
            if detect_color_contour_centers(mask, x, y):
                print('''location: "''', i, '''"''')
                if check_whether_lit(red, x, y):
                    print('''info: "RESCUE"''')
                elif check_whether_lit(blue, x, y):
                    print('''info: "MEDICINE"''')
                elif check_whether_lit(green, x, y):
                    print('''info: "FOOD"''')
       

        cv2.imshow("FUCKA", mask)
        cv2.imshow("FUCKAA", red)
        if cv2.waitKey(5) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
       
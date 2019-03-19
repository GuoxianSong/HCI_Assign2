import numpy as np
import cv2
from cv2 import aruco
import glob

def Run():
    mtx = np.load("calibration/mtx.npy")
    dist = np.load("calibration/dist.npy")
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    cam = cv2.VideoCapture(0)
    cout=0
    while True:
        ret_val, img = cam.read()
        if ret_val:
            #img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
            if(len(corners)==0):
                continue
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
            for i in range(0, ids.size):
                aruco.drawAxis(img, mtx, dist, rvec[i], tvec[i], 0.1)  # Draw Axis
            aruco.drawDetectedMarkers(img, corners)  # Draw A square around the markers
            gray = aruco.drawDetectedMarkers(img.copy(), corners, ids)
            cv2.imshow('my webcam', gray)
        # if(cv2.waitKey(1)==ord('a')):
        #     cv2.imwrite("calibration/"+str(cout)+".jpg",img)
        #     cout+=1

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


def Calibration():
    images = glob.glob('calibration/*.jpg')
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.
    objp = np.zeros((7 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:7].T.reshape(-1, 2)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (9, 7), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (9, 7), corners2, ret)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

Run()
import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
from time import time
import demo
import os


def match_images(img_path1, img_path2=None):
  img1 = cv2.imread(img_path1)
  if img_path2 is None:
    height, width, channel = img1.shape
    m = cv2.getRotationMatrix2D((width/2, height/2), 15, 1)
    img2 = cv2.warpAffine(img1, m, (width, height))
  else:
    img2 = cv2.imread(img_path2)

  gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  start = time()
  # SIFT 생성
  detector = cv2.ORB_create()

  # 각 영상에 대해 키 포인트와 서술자 추출 ---②
  kp1, desc1 = detector.detectAndCompute(gray1, None)
  kp2, desc2 = detector.detectAndCompute(gray2, None)

  # BFMatcher 생성
  matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

  # 매칭 계산
  matches = matcher.match(desc1, desc2)
  matches = sorted(matches, key = lambda x:x.distance)
  top100_matches = matches[:100]

  # 거리 계산
  distances = [m.distance for m in top100_matches]
  val = sum(distances)/len(distances)
  #print(f'mean distance : {sum(distances)/len(distances)}')
  #print(f'time {time() - start}s')
  # 매칭 결과 그리기
  #res = cv2.drawMatches(img1, kp1, img2, kp2, top100_matches, None, \
#                      flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

  #cv2_imshow(res)
  cv2.waitKey()
  cv2.destroyAllWindows()
  return val


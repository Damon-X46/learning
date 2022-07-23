
import numpy as np


def py_nms(dets, threshold):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]
    keep = []
    while len(order) > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        inter = h * w
        union = areas[i] + areas[order[1:]] - inter
        iou = inter / union
        inds = np.where(iou <= threshold)[0]
        order = order[inds + 1]
    return keep


def main():
    dets = np.array([[30, 20, 230, 200, 1], 
                    [50, 50, 260, 220, 0.9], 
                    [210, 30, 420, 5, 0.8], 
                    [430, 280, 460, 360, 0.7]])
    
    threshold = 0.35
    keeo_dets = py_nms(dets, threshold)     # 返回的是框的下标编号
    print(keeo_dets)
    print(dets[keeo_dets])


if __name__ == '__main__':
    main()
from tool.imageTool import *


def nearestInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    newImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    for i in range(newHeight):
        x = int((i + 0.5) * hScale - 0.5)
        for j in range(newWidth):
            y = int((j + 0.5) * wScale - 0.5)
            newImage[i, j] = image[x, y]
    return newImage


if __name__ == "__main__":
    image = imageLoad()
    newImage = nearestInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage, "flower_nearest.jpg")

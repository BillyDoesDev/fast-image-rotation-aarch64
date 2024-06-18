#include <iostream>
#include <stdio.h>
#include <cmath>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    Mat img = imread("../assets/fish.png");
    if (!img.data) {
        printf("No image data \n");
        return -1;
    }

    // Rotation angle in degrees
    float rot_angle = 30;
    // Center of the image
    Point2f center(img.cols / 2.0, img.rows / 2.0);

    // Calculate the rotation matrix
    Mat rotation_mat = getRotationMatrix2D(center, rot_angle, 1.0);

    // Calculate the size of the bounding box for the rotated image
    Rect2f bbox = RotatedRect(Point2f(), img.size(), rot_angle).boundingRect2f();

    // Adjust the transformation matrix
    rotation_mat.at<double>(0, 2) += bbox.width / 2.0 - img.cols / 2.0;
    rotation_mat.at<double>(1, 2) += bbox.height / 2.0 - img.rows / 2.0;

    // Perform the affine transformation (rotation) with bilinear interpolation
    Mat rotated;
    warpAffine(img, rotated, rotation_mat, bbox.size());


    if (imwrite("../outputs/opencv_warpAffine_builtin.png", rotated)) {
        // cout << "Rotated image saved to " << output_image_path << endl;
    } else {
        cerr << "Error saving image" << endl;
        return 1;
    }
    return 0;
}
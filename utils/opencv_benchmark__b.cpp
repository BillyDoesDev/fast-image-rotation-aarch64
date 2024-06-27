#include <iostream>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Usage: program input_path output_path angle\n");
        return -1;
    }

    Mat image = imread(argv[1]);
    double angle = std::stod(argv[3]);

    // get the center coordinates of the image to create the 2D rotation matrix
    Point2f center((image.cols - 1) / 2.0, (image.rows - 1) / 2.0);

    Mat rotation_matix = getRotationMatrix2D(center, angle, 1.0);
    Mat rotated_image;
    // rotate the image using warpAffine
    warpAffine(image, rotated_image, rotation_matix, image.size());
    imwrite(argv[2], rotated_image);

    return 0;
}
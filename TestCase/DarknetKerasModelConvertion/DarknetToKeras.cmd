cd %~dp0

set file_path=C:\Users\Ivan Lee\Documents\Software project\Machine learning\AI\CPOS\AI-TrainData-PscalVOC-and-Yolo-LicensePlateRecognition\
echo %file_path%
python ../../yolov3_darknet_to_keras.py -cfg_path "%file_path%lpr.cfg" -weights_path "%file_path%backup\yolov4-tiny-custom_60000.weights" -output_path ocr_yolo.h5

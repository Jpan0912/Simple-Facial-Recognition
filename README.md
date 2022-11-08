# Simple-Facial-Recognition
Facial Recognition Application built using OpenCV and Machine Learning

TRAINING MODEL

1. Install OpenCV on your machine.

2. Insert photos to train and validate of your choice into the train folder. The train folder format must match list provided in the face_train.py file. For example, 
    ![image](https://user-images.githubusercontent.com/74218391/200461797-fb4c344a-a126-49e1-8361-e43c78bdfe35.png)
    ![image](https://user-images.githubusercontent.com/74218391/200461874-b4fc95f4-72b3-4195-a01e-99f50be01e0c.png)


3. Provide the correct path for the train folder in face_train.py

4. Run face_train.py, if successful 'Training done -----------' should be seen on the terminal and 'features.npy' and 'labels.npy' should be created.

RECOGNITION

1. Insert photos to validate into the val folder. The val folder format must match list provided in the face_recognition.py file. For example, 
    ![image](https://user-images.githubusercontent.com/74218391/200462033-102b340d-36d2-44b3-8439-440b5a68b45c.png)
    ![image](https://user-images.githubusercontent.com/74218391/200462071-8df0c4a4-2073-44de-9f08-2021fefc5e8e.png)


2. Provide the correct path for the val folder in face_recognition.py

3. Run face_recognition.pym if successful it should recognise the face and provide a boundry box with a classification.
![image](https://user-images.githubusercontent.com/74218391/200461477-23558c40-5700-4ae8-976f-9cfb21ea5095.png)
![image](https://user-images.githubusercontent.com/74218391/200461507-fcf5bf38-3a7c-4db3-8032-4f2b8e68bb0f.png)


# auto-photo-organizer
Organizes photos on local, Azure Blob or AWS S3 by using face recognition

## References 
https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/ 


## Setup 

### Work environment
Check: https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html
```shell
python3 -m venv .env
source .env/bin/activate
```



### install OpenCV 
Ref: https://www.pyimagesearch.com/opencv-tutorials-resources-guides/

- Install OpenCV on Ubuntu
  ```bash
  pip install opencv-contrib-python
  ```

## Run:
```shell
python main.py abc.JPG haarcascade_frontalface_alt2.xml
```


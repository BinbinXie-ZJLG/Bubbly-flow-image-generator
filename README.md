Bubbly-flow-image-generator
=====


### The environment is

Python 3.5.2
Keras 2.2.5
tensorflow 1.14.0
CUDA 10.0 toolkit and cuDNN 7.5.

## Generator

### Download Generator'weight file
```python
https://drive.google.com/drive/folders/1pf8xs7YfFcBtIA2gkDX2IY4PfXV0QEKA?usp=sharing
```

### Generate images
  -different seeds can change noise z
  -label(0~9) can change superficial gas velocity
  -truncation-psi can change truncation value

```python
python run_generator.py generate-images  --seeds=6600-6609 --truncation-psi=1.0 --label=0 --network=xxx/xxxx
```


## Detector

### Download Detector'weight file
```python
https://drive.google.com/drive/folders/1pf8xs7YfFcBtIA2gkDX2IY4PfXV0QEKA?usp=sharing
```

### detect images
##### Don't forget to put the weight file into the “model_data” folder
```python
python yolo_video.py
```




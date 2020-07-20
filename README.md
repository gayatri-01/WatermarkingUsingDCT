# `Watermarking Using DCT`

[![made-with-python](https://img.shields.io/badge/Made%20With-Python-red?style=for-the-badge&logo=Python)](https://www.python.org/)
![made-with-django](https://img.shields.io/badge/Made%20With-Django-blue?style=for-the-badge&logo=Django)

Digital watermarking is a technology using which one can ensure copyright protection of
digital media, data authentications and security. It is the act of hiding a message related to
a signal into the signal itself. This process is a little similar to steganography.
Watermarking tries to hide a message related to the actual content of the digital signal,
while in steganography the digital signal has no relation to the message, and it is merely
used as a cover to hide its existence. 

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image1.jpeg">

-----------------------------------------------
## How it Works

### Haar Transform
A 1D, 1-level Haar transform is performed on a signal,
 f = (f1, f2, f3, f4,..., fN-1, fN)
f-> a^1 | d^1
[-] a^1 is called the trend or running average, and d^1 is called fluctuation or running difference.
[-] This process can be repeated until there ceases to be an even number of averages.
[-] Performing an inverse transform only to the trend sub-signal would allow an
approximation of the original signal.


### Watermarking using DCT
The discrete cosine transform (DCT) helps separate the image into parts (or spectral subbands) of differing importance (with respect to the image's visual quality). 
The DCT is similar to the discrete Fourier transform: it transforms a signal or image from the spatial domain to the frequency domain

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image2.jpeg">

The general equation for a 1D (N data items) DCT is defined by the following equation:

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image3.jpeg">

The corresponding inverse 1D DCT transform is simple F^-1(u), i.e.: where

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image4.jpeg">

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image 5.jpeg">

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image 6.jpeg">

-----------------------------------------------

## Demo

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/image 7.jpeg">

<img src="https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/images/demo.gif">

-----------------------------------------------

## Getting Started

### Prerequisites

* Django Framework
* Haar Transform
* Discrete Cosine Transform


### Setup
```
$ virtualenv venv
$ venv/scripts/activate
$ pip install -r https://github.com/gayatri-01/WatermarkingUsingDCT/blob/master/requirements.txt


$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver

```
-----------------------------------------------
## Built With

* [Django](https://www.djangoproject.com)

-----------------------------------------------

## Contributions

 We're are open to `enhancements` & `bug-fixes`

 ----------------------------------------------- 

## Contributors
* [Gayatri Srinivasan](https://github.com/gayatri-01)
* [Amisha Waghela](https://github.com/amisha-w)
* [Girish Thatte](https://github.com/girishgr8)


-----------------------------------------------

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

-----------------------------------------------







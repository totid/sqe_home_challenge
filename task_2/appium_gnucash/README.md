# GnuCash Android

## Description:
Test automation of test cases according to the test plan using __https://github.com/codinguser/gnucash-android__ app.

Used Page Object Pattern implementation. 

### Tests were implemented and run on:
* System: macOS Mojave 10.14.3
* Selenium WebDriver: 3.141.0
* Python version : 3.7.2.final.0
* Conda version : 4.6.7
* Conda-build version : 3.17.8
* PyCharm: 2018.3.5 (Community Edition)

### environment.yml:
```
name: appium_gnucash
channels:
  - conda-forge
  - defaults
dependencies:
  - asn1crypto=0.24.0=py37_1003
  - ca-certificates=2018.11.29=ha4d7672_0
  - certifi=2018.11.29=py37_1000
  - cffi=1.12.2=py37h342bebf_0
  - cryptography=2.5=py37hc2b1221_1
  - idna=2.8=py37_1000
  - libcxx=4.0.1=hcfea43d_1
  - libcxxabi=4.0.1=hcfea43d_1
  - libedit=3.1.20181209=hb402a30_0
  - libffi=3.2.1=h475c297_4
  - ncurses=6.1=h0a44026_1
  - openssl=1.1.1b=h1de35cc_0
  - pip=19.0.3=py37_0
  - pycparser=2.19=py_0
  - pyopenssl=19.0.0=py37_0
  - pysocks=1.6.8=py37_1002
  - python=3.7.2=haf84260_0
  - readline=7.0=h1de35cc_5
  - setuptools=40.8.0=py37_0
  - six=1.12.0=py37_1000
  - sqlite=3.26.0=ha441bb4_0
  - tk=8.6.8=ha441bb4_0
  - wheel=0.33.1=py37_0
  - xz=5.2.4=h1de35cc_4
  - zlib=1.2.11=h1de35cc_3
  - pip:
    - appium-python-client==0.39
    - selenium==3.141.0
    - urllib3==1.24.1
prefix: /Users/salvatore/anaconda3/envs/appium_gnucash
```

### Creating an envirment with existing .yml:
```
$ conda env create -f path/to/environment.yml
```
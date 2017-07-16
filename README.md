# Introduction

Randomized Prim Algorithm for Object Proposals on Python3

Forked form https://github.com/prlz77/pyrp

# pyrp
Ctypes Python wrapper for S. Manen, M. Guillaumin, L. Van Gool's Random Prim's Algorithm for Object Proposals.

Visit: https://github.com/smanenfr/rp to get the original code.

# Quick Start

#### 1. Change config.py and Save configruation
Change configuration at config.py or you can use default configuration.

Check https://github.com/smanenfr/rp to know the details about configuration

Save configuration
```
python3 config.py #rp.npy is the default saved configuration filename
```
### 2. compile
```
make
```
### 3. Run demo
```
python3 demo.py [image=image_path] [savefile=(save_file.npy | save_file.mat)]
```

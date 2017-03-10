# dataset_sim_001_km_320x160

First dataset recorded by Karol Majek using Sim (20170306) set to output **320x160** images.

10726 images.

## CSV

Raw CSV output from simulator was modified:

- global path replaced with local
- add 2 empty columns (left/right cam)


CSV includes: (all **8** laps)

- filename for one center camera only
- steering
- throttle
- brakes
- speed
- position
- rotation

### Example

First row of csv:

| filename | empty | empty | steering | throttle | brakes | speed | Position | Rotation|
|----------|-------|-------|----------|----------|--------|-------|----------------|----------------|
| IMG/center_2017_03_07_07_21_19_755.jpg | | | 0.0 | 0.681 | 0.0 | 32.178 | 1238.048:750.667: 29.766 | 356.186:177.798:359.968 |

Position and rotation are split while loading.

Min/Max values for columns:

|   | steering | throttle | brakes | speed | Pos X | Pos Y | Pos Z | Rot X | Rot Y | Rot Z |
|----------|-------|-------|----------|----------|--------|-------|
| Min values | -0.821 | 0.000 | 0.000 | 25.161 | 1179.530 | 491.830 | 2.764 | -0.006 | 0.010 | -0.005 |
| Max values | 1.000 | 0.976 | 1.000 | 100.146 | 1580.281 | 1325.112 | 42.436 | 359.994 | 359.992 | 359.993 |

## Images

Image size: **320x160**

![Example image](IMG/center_2017_03_07_07_21_19_755.jpg)

## Plot

First 5000 rows:

![First 5000 rows](first5000.png)

Full plot:

![Full plot](full.png)

## Video

[![Self-Racing Cars - Udacity Soulless - Dataset 001](https://img.youtube.com/vi/xC7O5KCY1lk/0.jpg)](https://www.youtube.com/watch?v=xC7O5KCY1lk)

# dataset_sim_002_km_320x160_recovery

Dataset recorded by Karol Majek using Sim (20170306) set to output **320x160** images.

3787 images.

## CSV

Raw CSV output from simulator was modified:

- global path replaced with local
- add 2 empty columns (left/right cam)


CSV includes: (recovery data)

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
| IMG/center_2017_03_10_22_45_11_191.jpg | | | -0.29040129999999997 | 0.810 | 0.0 | 54.644 | 1259.469:652.974:32.614 | 356.482:135.336:0.550 |

Position and rotation are split while loading.

Min/Max values for columns:

|   | steering | throttle | brakes | speed | Pos X | Pos Y | Pos Z | Rot X | Rot Y | Rot Z |
|----------|-------|-------|----------|----------|--------|-------|
| Min values | -1.000 | 0.000 | 0.000 | 28.396 | 1186.863 | 488.610 | 2.823 | -0.005 | 0.056 | 0.008 |
| Max values | 0.890 | 0.912 | 1.000 | 96.883 | 1583.007 | 1322.493 | 42.659 | 359.993 | 359.936 | 359.990 |

## Images

Image size: **320x160**

![Example image](IMG/center_2017_03_10_22_45_11_191.jpg)

## Plot

First 5000 rows:

![First 5000 rows](first5000.png)

Full plot:

![Full plot](full.png)

## Video

[![Self-Racing Cars - Udacity Soulless - Dataset 002](https://img.youtube.com/vi/ZdCt0mk-s6E/0.jpg)](https://www.youtube.com/watch?v=ZdCt0mk-s6E)

# dataset_sim_000_km_few_laps

First dataset recorded by Karol Majek using Sim (20170306) set to output **1920x600** images.

7684 images.

## CSV

Raw CSV output from simulator was modified:

- global path replaced with local
- add 2 empty columns (left/right cam)


CSV includes: (all **5** laps)

- filename for one center camera only
- steering
- throttle
- brakes
- speed
- acceleration x
- acceleration y

### Example

First row of csv:

| filename | empty | empty | steering | throttle | brakes | speed | Position | Rotation|
|----------|-------|-------|----------|----------|--------|-------|----------------|----------------|
| IMG/center_2017_03_06_21_15_27_656.jpg | | | 0.07247914 | 0.7352967 | 0 | 0.6671922 | 1239.393:754.3097:29.65825 | 356.0383:175.2307:0.3258028 |

Position and rotation are split while loading.

Min/Max values for columns:

|   | steering | throttle | brakes | speed | Pos X | Pos Y | Pos Z | Rot X | Rot Y | Rot Z |
|----------|-------|-------|----------|----------|--------|-------|
| Min values | -0.800 | 0.000 | 0.000 | 0.667 | 1180.007 | 489.573 | 2.901 | -0.006 | 0.012 | -0.005 |
| Max values | 1.000 | 0.867 | 1.000 | 86.655 | 1579.938 | 1325.674 | 42.685 | 359.994 | 359.909 | 359.994 |


## Images

Image size: **1920x600**
![Example image](IMG/center_2017_03_06_21_15_27_656.jpg)

## Plot

First 5000 rows:

![First 5000 rows](first5000.png)

Full plot:

![Full plot](full.png)

## Video

[![Self-Racing Cars - Udacity Soulless - Dataset 000](https://img.youtube.com/vi/0DRl_zYuX_8/0.jpg)](https://www.youtube.com/watch?v=0DRl_zYuX_8)

# Audeze Sine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 5.9; 22 5.9; 23 5.9; 25 5.9; 26 5.9; 28 5.7; 30 5.6; 32 5.6; 35 5.6; 37 5.6; 40 5.5; 42 5.4; 45 5.2; 49 5.0; 52 4.8; 56 4.5; 59 4.3; 64 4.0; 68 3.7; 73 3.5; 78 3.3; 83 3.2; 89 2.8; 95 2.4; 102 2.0; 109 1.8; 117 1.5; 125 1.3; 134 1.1; 143 1.0; 153 0.8; 164 0.7; 175 0.7; 188 0.9; 201 1.1; 215 0.9; 230 0.6; 246 0.4; 263 0.3; 282 0.1; 301 0.1; 323 0.2; 345 0.3; 369 0.4; 395 0.4; 423 0.3; 452 0.0; 484 -0.0; 518 0.0; 554 0.1; 593 0.2; 635 0.4; 679 0.5; 726 0.6; 777 0.5; 832 0.5; 890 0.4; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.4; 1248 -0.5; 1336 -0.6; 1429 -0.5; 1529 -0.2; 1636 -0.1; 1751 -0.1; 1873 -0.4; 2004 -0.5; 2145 -0.3; 2295 0.1; 2455 0.8; 2627 0.6; 2811 0.5; 3008 0.2; 3219 0.0; 3444 0.1; 3685 0.3; 3943 1.6; 4219 3.3; 4514 4.4; 4830 4.7; 5168 4.7; 5530 5.4; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.0; 10167 -3.1; 10879 -5.5; 11640 -5.7; 12455 -6.4; 13327 -9.7; 14260 -14.9; 15258 -20.1; 16326 -23.5; 17469 -24.2; 18692 -22.3; 20000 -18.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0482186183443645dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.66 | 4.5 dB   |
| Peaking | 45 Hz    | 0.63 | 3.8 dB   |
| Peaking | 82 Hz    | 3.26 | 0.4 dB   |
| Peaking | 7156 Hz  | 0.74 | 10.2 dB  |
| Peaking | 17475 Hz | 0.61 | -26.9 dB |
| Peaking | 3730 Hz  | 1.01 | -4.0 dB  |
| Peaking | 5052 Hz  | 1.02 | 4.7 dB   |
| Peaking | 7545 Hz  | 4.38 | -4.4 dB  |
| Peaking | 12712 Hz | 4.52 | 3.3 dB   |
| Peaking | 15405 Hz | 4.29 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine/Audeze%20Sine.png)
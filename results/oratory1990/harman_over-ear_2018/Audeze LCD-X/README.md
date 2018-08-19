# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.4; 30 5.0; 32 4.5; 35 4.0; 37 3.7; 40 3.3; 42 3.1; 45 3.0; 49 2.9; 52 2.8; 56 2.7; 59 2.7; 64 2.6; 68 2.5; 73 2.3; 78 2.1; 83 1.9; 89 1.6; 95 1.3; 102 1.0; 109 0.8; 117 0.5; 125 0.2; 134 -0.0; 143 -0.2; 153 -0.4; 164 -0.6; 175 -0.7; 188 -0.9; 201 -1.0; 215 -1.1; 230 -1.1; 246 -1.1; 263 -1.1; 282 -1.1; 301 -0.9; 323 -0.8; 345 -0.7; 369 -0.5; 395 -0.4; 423 -0.4; 452 -0.4; 484 -0.5; 518 -0.5; 554 -0.3; 593 -0.3; 635 -0.3; 679 -0.3; 726 -0.3; 777 -0.3; 832 -0.3; 890 -0.2; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.4; 1248 0.5; 1336 0.4; 1429 0.4; 1529 0.6; 1636 1.0; 1751 1.3; 1873 1.3; 2004 1.2; 2145 1.3; 2295 1.5; 2455 1.8; 2627 2.4; 2811 2.6; 3008 2.6; 3219 2.7; 3444 2.8; 3685 2.6; 3943 2.8; 4219 3.7; 4514 3.7; 4830 3.7; 5168 4.1; 5530 4.4; 5917 4.3; 6331 3.6; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.2; 12455 -2.0; 13327 -2.9; 14260 -2.7; 15258 -3.3; 16326 -5.5; 17469 -8.9; 18692 -13.4; 20000 -19.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.91 | 5.9 dB   |
| Peaking | 70 Hz    | 0.93 | 1.9 dB   |
| Peaking | 211 Hz   | 0.7  | -1.4 dB  |
| Peaking | 3169 Hz  | 1.21 | 2.6 dB   |
| Peaking | 5546 Hz  | 2.67 | 4.0 dB   |
| Peaking | 807 Hz   | 4.23 | -0.3 dB  |
| Peaking | 1738 Hz  | 6.18 | 0.5 dB   |
| Peaking | 12922 Hz | 0.51 | 1.3 dB   |
| Peaking | 19713 Hz | 0.99 | -18.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-X/Audeze%20LCD-X.png)
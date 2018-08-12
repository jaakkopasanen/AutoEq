# Campfire Audio Vega (Foam Eartips)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.0; 22 -7.1; 23 -7.1; 25 -7.2; 26 -7.3; 28 -7.3; 30 -7.3; 32 -7.3; 35 -7.3; 37 -7.3; 40 -7.3; 42 -7.3; 45 -7.3; 49 -7.4; 52 -7.4; 56 -7.5; 59 -7.5; 64 -7.6; 68 -7.7; 73 -7.9; 78 -8.0; 83 -8.1; 89 -8.2; 95 -8.3; 102 -8.4; 109 -8.4; 117 -8.5; 125 -8.5; 134 -8.4; 143 -8.3; 153 -8.2; 164 -8.0; 175 -7.8; 188 -7.6; 201 -7.3; 215 -7.0; 230 -6.7; 246 -6.4; 263 -6.1; 282 -5.7; 301 -5.3; 323 -4.8; 345 -4.3; 369 -3.9; 395 -3.5; 423 -3.1; 452 -2.7; 484 -2.3; 518 -1.9; 554 -1.5; 593 -1.1; 635 -0.8; 679 -0.4; 726 -0.1; 777 0.1; 832 0.3; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.3; 1429 -0.1; 1529 0.1; 1636 0.4; 1751 0.8; 1873 1.5; 2004 2.6; 2145 3.9; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.6; 4830 3.8; 5168 2.0; 5530 0.7; 5917 -0.1; 6331 -0.7; 6775 -0.8; 7249 -1.2; 7756 -3.2; 8299 -5.5; 8880 -6.9; 9502 -7.3; 10167 -7.4; 10879 -6.3; 11640 -3.4; 12455 -0.7; 13327 -2.0; 14260 -7.6; 15258 -12.9; 16326 -13.6; 17469 -9.5; 18692 -3.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.26 | -7.0 dB  |
| Peaking | 139 Hz   | 0.82 | -5.0 dB  |
| Peaking | 276 Hz   | 1.36 | -3.0 dB  |
| Peaking | 16050 Hz | 1.62 | -14.3 dB |
| Peaking | 1548 Hz  | 1.44 | -3.4 dB  |
| Peaking | 3200 Hz  | 0.68 | 8.0 dB   |
| Peaking | 10002 Hz | 1.07 | -8.9 dB  |
| Peaking | 12554 Hz | 2.83 | 9.2 dB   |
| Peaking | 19644 Hz | 3.23 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)
# Samsung EO-IG955 (AKG)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -3.9; 22 -4.3; 23 -4.4; 25 -4.7; 26 -4.8; 28 -5.0; 30 -5.2; 32 -5.4; 35 -5.6; 37 -5.8; 40 -5.9; 42 -6.0; 45 -6.2; 49 -6.4; 52 -6.5; 56 -6.7; 59 -6.8; 64 -7.0; 68 -7.1; 73 -7.3; 78 -7.4; 83 -7.5; 89 -7.7; 95 -7.8; 102 -7.9; 109 -8.0; 117 -8.0; 125 -8.0; 134 -7.9; 143 -7.9; 153 -7.7; 164 -7.5; 175 -7.2; 188 -6.6; 201 -6.6; 215 -6.9; 230 -6.6; 246 -6.3; 263 -5.9; 282 -5.6; 301 -5.1; 323 -4.7; 345 -4.2; 369 -3.8; 395 -3.4; 423 -3.1; 452 -2.7; 484 -2.3; 518 -1.9; 554 -1.5; 593 -1.1; 635 -0.8; 679 -0.5; 726 -0.2; 777 0.1; 832 0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.7; 1336 -0.7; 1429 -0.7; 1529 -0.7; 1636 -0.6; 1751 -0.6; 1873 -0.5; 2004 -0.4; 2145 -0.2; 2295 -0.0; 2455 0.0; 2627 0.0; 2811 -0.1; 3008 -0.5; 3219 -0.9; 3444 -1.2; 3685 -1.3; 3943 -1.2; 4219 -0.9; 4514 -0.9; 4830 -1.6; 5168 -2.4; 5530 -2.0; 5917 -0.0; 6331 1.9; 6775 2.6; 7249 0.5; 7756 -2.7; 8299 -5.1; 8880 -6.6; 9502 -7.9; 10167 -9.0; 10879 -8.6; 11640 -7.5; 12455 -9.0; 13327 -15.4; 14260 -24.2; 15258 -30.7; 16326 -32.2; 17469 -29.2; 18692 -22.7; 20000 -13.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.36 | -5.3 dB  |
| Peaking | 132 Hz   | 0.76 | -4.5 dB  |
| Peaking | 275 Hz   | 1.2  | -3.1 dB  |
| Peaking | 15576 Hz | 2.05 | -21.9 dB |
| Peaking | 17800 Hz | 1.17 | -21.1 dB |
| Peaking | 823 Hz   | 4.27 | 1.1 dB   |
| Peaking | 5343 Hz  | 4.23 | -2.1 dB  |
| Peaking | 6672 Hz  | 3.78 | 6.0 dB   |
| Peaking | 9129 Hz  | 3.8  | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)
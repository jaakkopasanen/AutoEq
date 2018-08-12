# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 1.0; 22 0.5; 23 0.3; 25 -0.0; 26 -0.2; 28 -0.5; 30 -0.7; 32 -0.9; 35 -1.2; 37 -1.4; 40 -1.6; 42 -1.7; 45 -1.9; 49 -2.1; 52 -2.2; 56 -2.4; 59 -2.6; 64 -2.8; 68 -3.0; 73 -3.2; 78 -3.5; 83 -3.7; 89 -3.9; 95 -4.2; 102 -4.4; 109 -4.6; 117 -4.7; 125 -4.8; 134 -4.9; 143 -5.1; 153 -5.3; 164 -5.5; 175 -5.7; 188 -5.9; 201 -6.1; 215 -6.3; 230 -6.4; 246 -6.4; 263 -6.4; 282 -6.3; 301 -6.1; 323 -6.0; 345 -5.8; 369 -5.6; 395 -5.5; 423 -5.4; 452 -5.2; 484 -5.0; 518 -4.7; 554 -4.4; 593 -3.8; 635 -3.4; 679 -3.0; 726 -2.7; 777 -2.2; 832 -1.7; 890 -1.2; 952 -0.6; 1019 0.3; 1090 1.2; 1167 2.1; 1248 2.9; 1336 2.9; 1429 1.9; 1529 1.1; 1636 0.1; 1751 -0.6; 1873 -1.2; 2004 -2.2; 2145 -2.9; 2295 -2.9; 2455 -1.3; 2627 0.8; 2811 2.3; 3008 2.6; 3219 1.9; 3444 1.5; 3685 0.6; 3943 -0.5; 4219 -1.6; 4514 -2.1; 4830 -2.9; 5168 -4.8; 5530 -6.1; 5917 -6.0; 6331 -3.9; 6775 -3.4; 7249 -4.2; 7756 -3.8; 8299 -1.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.3; 11640 -3.2; 12455 -4.2; 13327 -2.2; 14260 -0.1; 15258 -1.1; 16326 -4.7; 17469 -8.1; 18692 -9.4; 20000 -8.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 344 Hz   | 0.25 | -7.2 dB  |
| Peaking | 1996 Hz  | 0.5  | 10.0 dB  |
| Peaking | 2112 Hz  | 2.03 | -10.3 dB |
| Peaking | 5551 Hz  | 1.49 | -8.6 dB  |
| Peaking | 21 Hz    | 2.04 | 1.2 dB   |
| Peaking | 1250 Hz  | 8.22 | 1.4 dB   |
| Peaking | 4036 Hz  | 7.86 | -0.7 dB  |
| Peaking | 19920 Hz | 1.85 | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712/AKG%20K712.png)
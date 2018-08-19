# Sennheiser IE 80 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -10.7; 22 -10.7; 23 -10.8; 25 -10.8; 26 -10.8; 28 -10.8; 30 -10.8; 32 -10.9; 35 -10.9; 37 -10.9; 40 -11.0; 42 -11.0; 45 -11.0; 49 -11.1; 52 -11.2; 56 -11.2; 59 -11.3; 64 -11.4; 68 -11.5; 73 -11.6; 78 -11.7; 83 -11.9; 89 -12.0; 95 -12.1; 102 -12.2; 109 -12.2; 117 -12.2; 125 -12.2; 134 -12.2; 143 -12.1; 153 -12.0; 164 -11.8; 175 -11.6; 188 -11.3; 201 -11.0; 215 -10.7; 230 -10.4; 246 -10.0; 263 -9.7; 282 -9.2; 301 -8.8; 323 -8.2; 345 -7.7; 369 -7.2; 395 -6.7; 423 -6.2; 452 -5.7; 484 -5.1; 518 -4.6; 554 -4.0; 593 -3.5; 635 -3.0; 679 -2.4; 726 -1.9; 777 -1.3; 832 -0.9; 890 -0.5; 952 -0.2; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.3; 1336 0.5; 1429 0.5; 1529 0.5; 1636 0.4; 1751 0.4; 1873 0.6; 2004 0.9; 2145 1.3; 2295 1.6; 2455 1.7; 2627 1.6; 2811 1.3; 3008 0.9; 3219 0.4; 3444 -0.1; 3685 -0.8; 3943 -1.6; 4219 -2.9; 4514 -4.8; 4830 -6.9; 5168 -7.1; 5530 -4.3; 5917 -0.9; 6331 1.6; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.0; 11640 -0.9; 12455 -3.4; 13327 -7.7; 14260 -12.1; 15258 -14.9; 16326 -16.2; 17469 -16.1; 18692 -14.7; 20000 -11.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1610927172499768dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.2  | -10.4 dB |
| Peaking | 157 Hz   | 0.68 | -6.4 dB  |
| Peaking | 340 Hz   | 1.19 | -3.6 dB  |
| Peaking | 4945 Hz  | 6.71 | -7.8 dB  |
| Peaking | 17399 Hz | 1.24 | -18.6 dB |
| Peaking | 1118 Hz  | 1.16 | 2.5 dB   |
| Peaking | 2666 Hz  | 0.87 | 6.7 dB   |
| Peaking | 5511 Hz  | 0.19 | -6.1 dB  |
| Peaking | 6829 Hz  | 2.56 | 7.2 dB   |
| Peaking | 10727 Hz | 1.8  | 8.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)
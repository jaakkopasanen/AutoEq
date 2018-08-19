# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 0.9; 22 1.0; 23 1.1; 25 1.2; 26 1.3; 28 1.4; 30 1.6; 32 1.7; 35 1.9; 37 2.1; 40 2.5; 42 2.8; 45 3.1; 49 3.0; 52 2.4; 56 1.6; 59 1.2; 64 0.7; 68 0.1; 73 -0.7; 78 -1.2; 83 -1.5; 89 -2.0; 95 -2.5; 102 -3.1; 109 -3.4; 117 -3.7; 125 -3.8; 134 -3.8; 143 -3.9; 153 -3.8; 164 -3.5; 175 -3.1; 188 -2.7; 201 -2.3; 215 -1.9; 230 -1.2; 246 -0.5; 263 0.1; 282 0.8; 301 1.4; 323 1.8; 345 2.2; 369 2.3; 395 2.1; 423 1.8; 452 1.7; 484 1.3; 518 0.8; 554 0.5; 593 0.4; 635 0.3; 679 0.3; 726 0.3; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.6; 1167 -1.3; 1248 -1.7; 1336 -1.8; 1429 -1.8; 1529 -2.0; 1636 -2.3; 1751 -2.6; 1873 -2.8; 2004 -2.4; 2145 -2.0; 2295 -2.1; 2455 -2.4; 2627 -2.7; 2811 -2.0; 3008 -1.7; 3219 -1.7; 3444 -1.1; 3685 -0.2; 3943 0.2; 4219 -0.3; 4514 -0.4; 4830 0.3; 5168 1.2; 5530 0.8; 5917 -1.6; 6331 -4.8; 6775 -4.4; 7249 -2.9; 7756 -3.6; 8299 -4.3; 8880 -2.1; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.3; 12455 -4.1; 13327 -4.9; 14260 -1.8; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.238296814350431dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 1.61 | 3.4 dB  |
| Peaking | 130 Hz   | 1.52 | -4.6 dB |
| Peaking | 1978 Hz  | 1.51 | -2.8 dB |
| Peaking | 7230 Hz  | 2.89 | -4.2 dB |
| Peaking | 13141 Hz | 5.81 | -5.6 dB |
| Peaking | 203 Hz   | 2.37 | -1.5 dB |
| Peaking | 359 Hz   | 1.54 | 2.8 dB  |
| Peaking | 2760 Hz  | 5.05 | -0.9 dB |
| Peaking | 5243 Hz  | 8.06 | 2.5 dB  |
| Peaking | 10587 Hz | 5.87 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Oppo%20PM3/Oppo%20PM3.png)
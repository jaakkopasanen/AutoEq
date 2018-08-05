# Westone 4R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.4; 22 0.9; 23 0.7; 25 0.3; 26 0.1; 28 -0.2; 30 -0.5; 32 -0.7; 35 -1.0; 37 -1.2; 40 -1.4; 42 -1.5; 45 -1.7; 49 -1.9; 52 -2.1; 56 -2.2; 59 -2.3; 64 -2.6; 68 -2.6; 73 -2.8; 78 -3.1; 83 -3.3; 89 -3.6; 95 -4.0; 102 -4.5; 109 -5.0; 117 -5.5; 125 -6.1; 134 -6.6; 143 -6.9; 153 -7.2; 164 -7.4; 175 -7.4; 188 -7.4; 201 -7.3; 215 -7.3; 230 -7.0; 246 -7.0; 263 -6.8; 282 -6.6; 301 -6.3; 323 -6.0; 345 -5.7; 369 -5.4; 395 -5.0; 423 -4.6; 452 -4.3; 484 -4.0; 518 -3.7; 554 -3.0; 593 -2.4; 635 -1.9; 679 -1.5; 726 -1.0; 777 -0.3; 832 -0.0; 890 0.1; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.3; 1529 -1.3; 1636 -1.2; 1751 -0.9; 1873 -0.2; 2004 0.5; 2145 1.3; 2295 2.1; 2455 3.0; 2627 3.5; 2811 4.2; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -3.8; 9502 -7.1; 10167 -8.6; 10879 -6.4; 11640 -1.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 2.18 | 1.5 dB   |
| Peaking | 143 Hz   | 2.3  | -0.7 dB  |
| Peaking | 206 Hz   | 0.51 | -7.3 dB  |
| Peaking | 4637 Hz  | 0.89 | 7.2 dB   |
| Peaking | 9945 Hz  | 3.29 | -11.0 dB |
| Peaking | 13 Hz    | 2.09 | 1.4 dB   |
| Peaking | 869 Hz   | 2.64 | 1.6 dB   |
| Peaking | 1598 Hz  | 2.29 | -2.2 dB  |
| Peaking | 3056 Hz  | 4.65 | 1.8 dB   |
| Peaking | 24000 Hz | 1.67 | -0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%204R/Westone%204R.png)
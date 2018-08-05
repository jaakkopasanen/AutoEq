# Sennheiser HD 218

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.8; 83 5.7; 89 5.0; 95 4.1; 102 3.1; 109 2.4; 117 1.6; 125 0.6; 134 -0.1; 143 -0.7; 153 -1.2; 164 -1.1; 175 -0.7; 188 -1.2; 201 -1.9; 215 -2.4; 230 -2.7; 246 -3.1; 263 -3.5; 282 -3.7; 301 -3.9; 323 -4.2; 345 -4.6; 369 -5.0; 395 -4.2; 423 -2.8; 452 -2.4; 484 -2.3; 518 -2.4; 554 -1.7; 593 -0.3; 635 0.2; 679 0.3; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 0.1; 1248 0.4; 1336 0.7; 1429 1.1; 1529 1.4; 1636 0.8; 1751 0.2; 1873 0.6; 2004 1.0; 2145 1.7; 2295 2.5; 2455 3.4; 2627 3.8; 2811 3.7; 3008 3.9; 3219 4.2; 3444 4.6; 3685 5.7; 3943 6.0; 4219 4.3; 4514 0.1; 4830 -2.7; 5168 -2.2; 5530 -1.1; 5917 -0.3; 6331 1.2; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.6; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -2.7; 17469 -5.4; 18692 -6.9; 20000 -7.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.43 | 6.9 dB  |
| Peaking | 281 Hz   | 0.91 | -5.0 dB |
| Peaking | 3252 Hz  | 1.74 | 5.3 dB  |
| Peaking | 19077 Hz | 0.6  | -8.2 dB |
| Peaking | 14586 Hz | 1.27 | 4.5 dB  |
| Peaking | 17 Hz    | 2.03 | 1.4 dB  |
| Peaking | 140 Hz   | 5.47 | -1.6 dB |
| Peaking | 4072 Hz  | 5.87 | 5.2 dB  |
| Peaking | 4831 Hz  | 3.14 | -5.1 dB |
| Peaking | 6759 Hz  | 7.64 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)
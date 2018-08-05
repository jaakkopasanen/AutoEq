# UBSound Fighter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.6; 23 -5.8; 25 -6.1; 26 -6.2; 28 -6.5; 30 -6.6; 32 -6.8; 35 -7.1; 37 -7.2; 40 -7.3; 42 -7.3; 45 -7.4; 49 -7.5; 52 -7.5; 56 -7.6; 59 -7.6; 64 -7.5; 68 -7.5; 73 -7.6; 78 -7.6; 83 -7.7; 89 -7.9; 95 -8.2; 102 -8.5; 109 -8.8; 117 -9.0; 125 -9.3; 134 -9.5; 143 -9.6; 153 -9.5; 164 -9.3; 175 -9.0; 188 -8.7; 201 -8.3; 215 -7.9; 230 -7.4; 246 -7.0; 263 -6.6; 282 -6.1; 301 -5.6; 323 -5.1; 345 -4.6; 369 -4.2; 395 -3.6; 423 -3.0; 452 -2.5; 484 -2.2; 518 -1.8; 554 -1.1; 593 -0.3; 635 0.1; 679 0.4; 726 1.3; 777 1.9; 832 0.5; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.2; 1336 -0.9; 1429 -1.4; 1529 -1.9; 1636 -2.3; 1751 -2.5; 1873 -2.3; 2004 -1.6; 2145 -0.4; 2295 1.4; 2455 3.6; 2627 5.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.3; 5917 1.5; 6331 -3.1; 6775 -1.1; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UBSound Fighter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 5 Hz    | 1.68 | -4.6 dB |
| Peaking | 44 Hz   | 0.3  | -6.6 dB |
| Peaking | 178 Hz  | 0.78 | -6.5 dB |
| Peaking | 1844 Hz | 2.47 | -5.5 dB |
| Peaking | 3306 Hz | 1.06 | 7.5 dB  |
| Peaking | 727 Hz  | 2.18 | 3.3 dB  |
| Peaking | 654 Hz  | 0.72 | -1.2 dB |
| Peaking | 5422 Hz | 3.37 | 4.5 dB  |
| Peaking | 6326 Hz | 5.35 | -7.0 dB |
| Peaking | 3478 Hz | 6.21 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UBSound%20Fighter/UBSound%20Fighter.png)
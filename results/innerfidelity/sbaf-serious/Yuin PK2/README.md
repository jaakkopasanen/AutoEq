# Yuin PK2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 5.7; 175 5.5; 188 5.3; 201 5.3; 215 5.1; 230 5.1; 246 4.8; 263 5.0; 282 5.1; 301 4.9; 323 4.9; 345 4.7; 369 4.6; 395 4.3; 423 2.7; 452 3.1; 484 3.6; 518 3.0; 554 2.4; 593 2.4; 635 2.2; 679 1.9; 726 1.7; 777 1.4; 832 1.1; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.8; 1336 -2.3; 1429 -3.4; 1529 -4.4; 1636 -5.7; 1751 -6.3; 1873 -7.0; 2004 -7.0; 2145 -7.7; 2295 -8.5; 2455 -7.9; 2627 -6.5; 2811 -5.1; 3008 -3.3; 3219 -1.5; 3444 -0.3; 3685 -0.7; 3943 -0.9; 4219 -2.7; 4514 -4.0; 4830 -4.1; 5168 -4.0; 5530 -5.0; 5917 -6.4; 6331 -8.6; 6775 -7.9; 7249 -7.3; 7756 -6.2; 8299 -5.6; 8880 -5.8; 9502 -6.3; 10167 -6.2; 10879 -4.1; 11640 -0.8; 12455 0.0; 13327 -0.8; 14260 -4.3; 15258 -6.2; 16326 -5.1; 17469 -2.5; 18692 -0.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.11 | 5.9 dB  |
| Peaking | 244 Hz   | 0.4  | 4.1 dB  |
| Peaking | 2045 Hz  | 1.65 | -8.4 dB |
| Peaking | 7243 Hz  | 1.37 | -7.6 dB |
| Peaking | 32191 Hz | 3.02 | -6.2 dB |
| Peaking | 2555 Hz  | 5.9  | -2.1 dB |
| Peaking | 3529 Hz  | 3.78 | 3.4 dB  |
| Peaking | 8125 Hz  | 2.9  | 5.3 dB  |
| Peaking | 9757 Hz  | 1.09 | -5.4 dB |
| Peaking | 12182 Hz | 3.06 | 5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)
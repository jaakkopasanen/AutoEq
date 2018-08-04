# Acoustic Research AR H1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.0; 22 3.8; 23 3.8; 25 3.6; 26 3.6; 28 3.5; 30 3.4; 32 3.3; 35 3.3; 37 3.3; 40 3.2; 42 3.2; 45 3.2; 49 3.2; 52 3.1; 56 3.1; 59 3.1; 64 3.1; 68 3.0; 73 2.9; 78 2.8; 83 2.6; 89 2.3; 95 1.8; 102 1.3; 109 1.0; 117 0.5; 125 -0.1; 134 -0.6; 143 -0.8; 153 -1.1; 164 -1.2; 175 -1.4; 188 -1.5; 201 -1.3; 215 -0.7; 230 -0.1; 246 -0.0; 263 -0.3; 282 -0.6; 301 -0.8; 323 -1.1; 345 -1.5; 369 -1.9; 395 -1.8; 423 -1.3; 452 -0.1; 484 0.6; 518 -0.4; 554 -0.9; 593 -1.4; 635 -2.2; 679 -2.2; 726 1.8; 777 2.8; 832 1.2; 890 0.1; 952 -0.2; 1019 0.1; 1090 -0.1; 1167 0.0; 1248 0.0; 1336 0.1; 1429 0.7; 1529 1.2; 1636 0.6; 1751 -1.8; 1873 -0.9; 2004 -0.3; 2145 0.3; 2295 0.8; 2455 1.6; 2627 2.6; 2811 3.4; 3008 4.9; 3219 5.9; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.7; 4514 1.0; 4830 0.4; 5168 2.2; 5530 3.5; 5917 4.2; 6331 4.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -3.3; 9502 -3.2; 10167 -1.8; 10879 -0.6; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustic Research AR H1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.89 | 3.8 dB  |
| Peaking | 68 Hz   | 2.08 | 2.6 dB  |
| Peaking | 3451 Hz | 2.74 | 6.7 dB  |
| Peaking | 6304 Hz | 3.58 | 4.4 dB  |
| Peaking | 9184 Hz | 4.05 | -4.2 dB |
| Peaking | 172 Hz  | 2.72 | -1.8 dB |
| Peaking | 371 Hz  | 4.57 | -2.0 dB |
| Peaking | 672 Hz  | 5.02 | -4.1 dB |
| Peaking | 748 Hz  | 6.6  | 5.1 dB  |
| Peaking | 1805 Hz | 8.68 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Acoustic%20Research%20AR%20H1/Acoustic%20Research%20AR%20H1.png)
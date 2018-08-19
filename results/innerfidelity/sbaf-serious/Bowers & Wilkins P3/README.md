# Bowers & Wilkins P3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.5; 22 0.8; 23 0.4; 25 -0.1; 26 -0.4; 28 -0.8; 30 -1.2; 32 -1.6; 35 -2.1; 37 -2.5; 40 -2.9; 42 -3.1; 45 -3.5; 49 -3.9; 52 -4.2; 56 -4.5; 59 -4.8; 64 -5.2; 68 -5.5; 73 -5.9; 78 -6.2; 83 -6.5; 89 -6.9; 95 -7.3; 102 -7.6; 109 -7.7; 117 -7.9; 125 -8.1; 134 -8.2; 143 -8.4; 153 -8.7; 164 -8.9; 175 -8.7; 188 -8.9; 201 -9.2; 215 -9.2; 230 -9.3; 246 -9.5; 263 -9.5; 282 -9.5; 301 -9.4; 323 -9.3; 345 -9.0; 369 -8.7; 395 -8.3; 423 -7.7; 452 -7.2; 484 -6.8; 518 -6.4; 554 -5.9; 593 -5.1; 635 -4.3; 679 -3.6; 726 -2.8; 777 -1.9; 832 -1.2; 890 -0.7; 952 -0.3; 1019 0.1; 1090 0.8; 1167 1.8; 1248 2.3; 1336 1.8; 1429 1.6; 1529 2.0; 1636 2.2; 1751 2.6; 1873 3.3; 2004 3.7; 2145 3.9; 2295 3.9; 2455 4.0; 2627 3.7; 2811 2.8; 3008 1.8; 3219 0.7; 3444 0.2; 3685 0.1; 3943 0.6; 4219 2.3; 4514 5.2; 4830 6.0; 5168 4.3; 5530 1.9; 5917 2.7; 6331 3.2; 6775 2.1; 7249 -0.2; 7756 -2.2; 8299 -3.4; 8880 -3.1; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.5; 18692 -3.8; 20000 -5.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0998568309251455dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.55 | -5.4 dB |
| Peaking | 330 Hz  | 0.58 | -8.0 dB |
| Peaking | 1684 Hz | 0.71 | 4.1 dB  |
| Peaking | 4874 Hz | 5.11 | 5.6 dB  |
| Peaking | 8504 Hz | 5.48 | -4.3 dB |
| Peaking | 20 Hz   | 2.23 | 2.0 dB  |
| Peaking | 1635 Hz | 3.03 | -2.1 dB |
| Peaking | 2287 Hz | 1.06 | 1.8 dB  |
| Peaking | 3499 Hz | 3.2  | -2.8 dB |
| Peaking | 6401 Hz | 8.78 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P3/Bowers%20&%20Wilkins%20P3.png)
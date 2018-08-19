# Beyerdynamic T50p sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.5; 40 5.1; 42 4.9; 45 4.6; 49 4.2; 52 4.0; 56 3.6; 59 3.3; 64 2.9; 68 2.6; 73 2.4; 78 2.2; 83 2.0; 89 1.6; 95 1.3; 102 1.9; 109 2.6; 117 2.8; 125 2.5; 134 2.3; 143 2.6; 153 3.0; 164 3.5; 175 3.1; 188 1.7; 201 0.5; 215 -0.4; 230 -1.1; 246 -1.7; 263 -1.8; 282 -1.8; 301 -1.8; 323 -2.2; 345 -2.5; 369 -2.4; 395 -2.3; 423 -2.1; 452 -2.1; 484 -2.1; 518 -2.0; 554 -1.8; 593 -1.5; 635 -1.4; 679 -0.7; 726 -0.0; 777 -0.1; 832 -0.2; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.2; 1336 1.5; 1429 1.8; 1529 2.3; 1636 3.0; 1751 4.0; 1873 5.4; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.58 | 5.1 dB  |
| Peaking | 54 Hz   | 0.28 | 1.5 dB  |
| Peaking | 161 Hz  | 1.71 | 4.9 dB  |
| Peaking | 282 Hz  | 0.44 | -3.7 dB |
| Peaking | 3196 Hz | 0.64 | 7.0 dB  |
| Peaking | 86 Hz   | 5.1  | -0.3 dB |
| Peaking | 2021 Hz | 2.77 | 3.1 dB  |
| Peaking | 2254 Hz | 0.95 | -1.7 dB |
| Peaking | 6277 Hz | 2.07 | 5.7 dB  |
| Peaking | 7352 Hz | 1.41 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20B/Beyerdynamic%20T50p%20sample%20B.png)
# Bowers & Wilkins P5 Test 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.7; 23 -1.8; 25 -1.9; 26 -2.0; 28 -2.1; 30 -2.2; 32 -2.2; 35 -2.3; 37 -2.4; 40 -2.5; 42 -2.5; 45 -2.7; 49 -2.9; 52 -3.1; 56 -3.3; 59 -3.5; 64 -3.8; 68 -4.0; 73 -4.2; 78 -4.4; 83 -4.7; 89 -5.0; 95 -5.2; 102 -5.4; 109 -5.6; 117 -5.8; 125 -5.9; 134 -5.9; 143 -6.1; 153 -6.4; 164 -6.2; 175 -6.0; 188 -6.1; 201 -5.8; 215 -5.5; 230 -5.0; 246 -4.5; 263 -3.9; 282 -3.4; 301 -3.5; 323 -3.5; 345 -3.0; 369 -2.4; 395 -1.8; 423 -1.0; 452 -0.6; 484 -0.5; 518 -0.4; 554 -0.2; 593 0.1; 635 -0.0; 679 -0.2; 726 -0.1; 777 0.0; 832 -0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 -0.1; 1248 -0.2; 1336 -0.5; 1429 -0.9; 1529 -1.4; 1636 -1.8; 1751 -2.3; 1873 -2.5; 2004 -2.7; 2145 -3.1; 2295 -4.0; 2455 -3.9; 2627 -3.4; 2811 -3.1; 3008 -2.8; 3219 -2.1; 3444 -1.1; 3685 -0.9; 3943 0.3; 4219 0.4; 4514 0.4; 4830 0.4; 5168 -0.2; 5530 -1.7; 5917 -2.1; 6331 0.3; 6775 2.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.010499289367878dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Test 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.41 | -1.4 dB |
| Peaking | 104 Hz  | 0.64 | -2.8 dB |
| Peaking | 195 Hz  | 0.71 | -4.8 dB |
| Peaking | 1128 Hz | 0.16 | 1.3 dB  |
| Peaking | 2343 Hz | 1.27 | -5.0 dB |
| Peaking | 345 Hz  | 3.77 | -2.0 dB |
| Peaking | 353 Hz  | 1.89 | 1.3 dB  |
| Peaking | 4856 Hz | 2.36 | 3.0 dB  |
| Peaking | 5908 Hz | 2.16 | -5.3 dB |
| Peaking | 6738 Hz | 5.14 | 5.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Test%202/Bowers%20&%20Wilkins%20P5%20Test%202.png)
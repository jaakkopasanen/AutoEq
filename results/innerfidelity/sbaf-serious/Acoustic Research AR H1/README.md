# Acoustic Research AR H1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.0; 22 3.8; 23 3.8; 25 3.6; 26 3.5; 28 3.4; 30 3.3; 32 3.3; 35 3.2; 37 3.2; 40 3.1; 42 3.1; 45 3.1; 49 3.0; 52 2.9; 56 2.8; 59 2.7; 64 2.5; 68 2.4; 73 2.2; 78 2.0; 83 1.8; 89 1.5; 95 1.1; 102 0.8; 109 0.6; 117 0.3; 125 -0.1; 134 -0.4; 143 -0.6; 153 -0.9; 164 -1.0; 175 -1.1; 188 -1.3; 201 -1.1; 215 -0.5; 230 0.0; 246 0.1; 263 -0.3; 282 -0.5; 301 -0.8; 323 -1.1; 345 -1.4; 369 -1.9; 395 -1.8; 423 -1.3; 452 -0.1; 484 0.6; 518 -0.4; 554 -0.9; 593 -1.4; 635 -2.2; 679 -2.2; 726 1.8; 777 2.8; 832 1.2; 890 0.1; 952 -0.2; 1019 0.1; 1090 -0.1; 1167 0.0; 1248 0.0; 1336 0.1; 1429 0.7; 1529 1.2; 1636 0.6; 1751 -1.8; 1873 -0.9; 2004 -0.3; 2145 0.3; 2295 0.8; 2455 1.6; 2627 2.6; 2811 3.4; 3008 4.9; 3219 5.9; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.7; 4514 1.0; 4830 0.4; 5168 2.2; 5530 3.5; 5917 4.2; 6331 4.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -3.3; 9502 -3.2; 10167 -1.8; 10879 -0.6; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999993210627dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustic Research AR H1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.96 | 3.7 dB  |
| Peaking | 59 Hz   | 1.82 | 2.2 dB  |
| Peaking | 3451 Hz | 2.74 | 6.7 dB  |
| Peaking | 6304 Hz | 3.57 | 4.4 dB  |
| Peaking | 9177 Hz | 4.02 | -4.2 dB |
| Peaking | 174 Hz  | 2.86 | -1.4 dB |
| Peaking | 370 Hz  | 4.65 | -2.0 dB |
| Peaking | 672 Hz  | 5.05 | -4.2 dB |
| Peaking | 747 Hz  | 6.45 | 5.0 dB  |
| Peaking | 1818 Hz | 8.18 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Acoustic%20Research%20AR%20H1/Acoustic%20Research%20AR%20H1.png)
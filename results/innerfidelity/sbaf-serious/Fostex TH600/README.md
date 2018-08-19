# Fostex TH600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.4; 23 -3.5; 25 -3.8; 26 -3.9; 28 -4.1; 30 -4.3; 32 -4.4; 35 -4.6; 37 -4.7; 40 -4.8; 42 -4.9; 45 -4.9; 49 -4.9; 52 -4.8; 56 -4.6; 59 -4.4; 64 -4.6; 68 -4.9; 73 -5.2; 78 -5.4; 83 -5.5; 89 -5.5; 95 -5.7; 102 -5.7; 109 -5.6; 117 -5.5; 125 -5.5; 134 -5.5; 143 -5.4; 153 -5.3; 164 -4.9; 175 -4.5; 188 -4.4; 201 -4.2; 215 -3.7; 230 -3.3; 246 -3.0; 263 -2.6; 282 -2.1; 301 -1.6; 323 -1.0; 345 -0.3; 369 0.4; 395 1.3; 423 2.4; 452 3.3; 484 3.7; 518 3.7; 554 3.5; 593 3.1; 635 2.3; 679 1.5; 726 0.8; 777 1.1; 832 1.6; 890 0.6; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.7; 1429 0.6; 1529 0.6; 1636 0.5; 1751 0.6; 1873 0.7; 2004 1.0; 2145 1.5; 2295 3.1; 2455 5.1; 2627 4.2; 2811 4.0; 3008 5.8; 3219 5.8; 3444 4.9; 3685 5.0; 3943 4.6; 4219 1.9; 4514 -0.1; 4830 -1.5; 5168 -1.1; 5530 -1.5; 5917 -2.4; 6331 -2.1; 6775 -2.1; 7249 -1.7; 7756 -0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.5; 18692 -3.9; 20000 -6.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999028093dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.74 | -3.1 dB |
| Peaking | 124 Hz  | 0.47 | -5.4 dB |
| Peaking | 496 Hz  | 1.68 | 5.2 dB  |
| Peaking | 3065 Hz | 2.4  | 6.3 dB  |
| Peaking | 2470 Hz | 7.7  | 3.7 dB  |
| Peaking | 2678 Hz | 4.53 | -1.8 dB |
| Peaking | 3863 Hz | 6.59 | 3.4 dB  |
| Peaking | 5663 Hz | 1.77 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)
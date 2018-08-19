# Fostex TH900mk2 TH610Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 -0.4; 22 -1.0; 23 -1.3; 25 -1.8; 26 -2.0; 28 -2.4; 30 -2.7; 32 -2.9; 35 -3.1; 37 -3.2; 40 -3.4; 42 -3.4; 45 -3.5; 49 -3.5; 52 -3.6; 56 -3.7; 59 -3.8; 64 -3.9; 68 -3.9; 73 -4.0; 78 -4.2; 83 -4.4; 89 -4.6; 95 -4.7; 102 -4.8; 109 -4.9; 117 -4.9; 125 -5.1; 134 -5.2; 143 -5.3; 153 -5.3; 164 -5.1; 175 -4.9; 188 -5.0; 201 -5.0; 215 -4.9; 230 -4.7; 246 -4.5; 263 -4.4; 282 -4.1; 301 -3.8; 323 -3.5; 345 -3.2; 369 -2.9; 395 -2.6; 423 -2.2; 452 -1.7; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.7; 635 -0.6; 679 -0.9; 726 -0.4; 777 0.9; 832 0.4; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.3; 1167 0.6; 1248 0.6; 1336 0.5; 1429 0.2; 1529 -0.1; 1636 -0.2; 1751 -0.1; 1873 0.4; 2004 1.0; 2145 1.4; 2295 1.9; 2455 3.1; 2627 3.9; 2811 3.9; 3008 3.5; 3219 2.8; 3444 2.3; 3685 2.5; 3943 2.9; 4219 3.1; 4514 3.0; 4830 3.5; 5168 4.6; 5530 4.7; 5917 3.4; 6331 1.9; 6775 1.5; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.991772684877764dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 TH610Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 72 Hz   | 1.33 | 1.8 dB  |
| Peaking | 82 Hz   | 0.46 | -5.6 dB |
| Peaking | 245 Hz  | 0.99 | -2.6 dB |
| Peaking | 2796 Hz | 2.33 | 3.7 dB  |
| Peaking | 5253 Hz | 2.65 | 4.4 dB  |
| Peaking | 795 Hz  | 9.61 | 1.4 dB  |
| Peaking | 1218 Hz | 4.19 | 0.7 dB  |
| Peaking | 1671 Hz | 4.33 | -0.8 dB |
| Peaking | 4009 Hz | 8.84 | 0.8 dB  |
| Peaking | 8669 Hz | 2.76 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2%20TH610Pads/Fostex%20TH900mk2%20TH610Pads.png)
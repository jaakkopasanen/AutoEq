# Fostex TH900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -4.5; 22 -4.8; 23 -4.9; 25 -5.0; 26 -5.1; 28 -5.2; 30 -5.2; 32 -5.3; 35 -5.3; 37 -5.3; 40 -5.3; 42 -5.3; 45 -5.1; 49 -4.6; 52 -4.1; 56 -4.4; 59 -5.1; 64 -5.7; 68 -5.9; 73 -5.9; 78 -5.9; 83 -5.9; 89 -5.8; 95 -5.9; 102 -6.0; 109 -5.9; 117 -5.9; 125 -6.0; 134 -6.0; 143 -6.0; 153 -5.8; 164 -5.4; 175 -5.3; 188 -5.1; 201 -4.8; 215 -4.6; 230 -4.3; 246 -4.0; 263 -3.7; 282 -3.3; 301 -2.9; 323 -2.4; 345 -1.8; 369 -1.2; 395 -0.5; 423 0.2; 452 1.3; 484 2.5; 518 3.9; 554 5.0; 593 4.9; 635 3.6; 679 2.3; 726 2.4; 777 2.3; 832 1.1; 890 0.4; 952 0.2; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.2; 1336 0.4; 1429 0.3; 1529 -0.2; 1636 -0.7; 1751 -1.0; 1873 -0.6; 2004 1.1; 2145 3.1; 2295 3.5; 2455 2.5; 2627 2.5; 2811 1.7; 3008 1.2; 3219 1.4; 3444 1.9; 3685 2.2; 3943 2.2; 4219 0.8; 4514 -0.8; 4830 -1.6; 5168 -1.9; 5530 -2.7; 5917 -3.3; 6331 -2.3; 6775 -2.1; 7249 -2.2; 7756 -1.8; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -1.2; 11640 -1.6; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 -1.0; 16326 -2.4; 17469 -2.3; 18692 -3.8; 20000 -9.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2822839440985dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.88 | -3.7 dB |
| Peaking | 122 Hz   | 0.38 | -5.9 dB |
| Peaking | 561 Hz   | 2.21 | 6.6 dB  |
| Peaking | 3493 Hz  | 1.08 | 3.5 dB  |
| Peaking | 5600 Hz  | 1.43 | -4.3 dB |
| Peaking | 1828 Hz  | 3.71 | -2.8 dB |
| Peaking | 2186 Hz  | 3.93 | 3.2 dB  |
| Peaking | 3028 Hz  | 7.08 | -1.4 dB |
| Peaking | 8937 Hz  | 5.87 | 1.1 dB  |
| Peaking | 20272 Hz | 1.46 | -9.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH900/Fostex%20TH900.png)
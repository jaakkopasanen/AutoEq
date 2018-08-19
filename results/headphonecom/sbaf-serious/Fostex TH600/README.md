# Fostex TH600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.8; 23 -2.0; 25 -2.4; 26 -2.6; 28 -3.0; 30 -3.3; 32 -3.5; 35 -3.8; 37 -3.9; 40 -4.1; 42 -4.1; 45 -4.1; 49 -4.2; 52 -4.4; 56 -4.8; 59 -4.9; 64 -4.8; 68 -4.4; 73 -4.5; 78 -5.0; 83 -5.2; 89 -5.5; 95 -5.5; 102 -5.5; 109 -5.4; 117 -5.4; 125 -5.4; 134 -5.3; 143 -5.2; 153 -5.1; 164 -4.7; 175 -4.5; 188 -4.3; 201 -3.9; 215 -3.6; 230 -3.2; 246 -2.8; 263 -2.3; 282 -1.8; 301 -1.1; 323 -0.2; 345 0.6; 369 1.4; 395 1.9; 423 2.3; 452 2.7; 484 3.0; 518 3.2; 554 3.2; 593 2.8; 635 2.2; 679 1.7; 726 1.0; 777 0.6; 832 1.8; 890 0.8; 952 0.2; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.2; 1429 0.0; 1529 -0.2; 1636 -0.3; 1751 0.1; 1873 0.2; 2004 0.4; 2145 1.1; 2295 2.2; 2455 4.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.6; 3685 5.0; 3943 3.1; 4219 0.6; 4514 -1.1; 4830 -2.2; 5168 -2.6; 5530 -2.7; 5917 -3.4; 6331 -3.3; 6775 -3.0; 7249 -3.0; 7756 -2.0; 8299 -0.1; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.2; 18692 -4.4; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999991164dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 1.02 | -1.7 dB |
| Peaking | 122 Hz   | 0.39 | -5.5 dB |
| Peaking | 468 Hz   | 1.32 | 5.0 dB  |
| Peaking | 3147 Hz  | 2.07 | 7.7 dB  |
| Peaking | 5705 Hz  | 1.64 | -4.5 dB |
| Peaking | 1907 Hz  | 1.63 | -1.2 dB |
| Peaking | 2558 Hz  | 8.57 | 2.7 dB  |
| Peaking | 8991 Hz  | 5.22 | 1.1 dB  |
| Peaking | 16121 Hz | 1.12 | 2.4 dB  |
| Peaking | 19463 Hz | 0.91 | -6.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)
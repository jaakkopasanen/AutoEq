# Philips ActionFit SHQ5200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.7; 26 5.5; 28 4.9; 30 4.2; 32 3.6; 35 2.7; 37 2.2; 40 1.5; 42 1.0; 45 0.4; 49 -0.2; 52 -0.7; 56 -1.2; 59 -1.5; 64 -2.1; 68 -2.4; 73 -2.8; 78 -3.1; 83 -3.4; 89 -3.7; 95 -3.9; 102 -4.0; 109 -4.0; 117 -4.2; 125 -4.3; 134 -4.3; 143 -4.4; 153 -4.4; 164 -4.3; 175 -4.1; 188 -4.0; 201 -4.0; 215 -3.8; 230 -3.5; 246 -3.3; 263 -3.0; 282 -2.7; 301 -2.5; 323 -1.9; 345 -1.2; 369 -0.3; 395 -0.3; 423 -2.2; 452 -2.5; 484 -2.1; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.7; 726 -0.5; 777 -0.2; 832 0.0; 890 0.0; 952 0.0; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.4; 1336 0.4; 1429 0.6; 1529 0.9; 1636 1.1; 1751 1.6; 1873 2.6; 2004 2.9; 2145 2.8; 2295 3.9; 2455 2.7; 2627 3.0; 2811 3.0; 3008 4.3; 3219 5.5; 3444 6.0; 3685 6.0; 3943 5.4; 4219 3.2; 4514 2.5; 4830 2.9; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ActionFit SHQ5200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.75 | 7.0 dB  |
| Peaking | 125 Hz  | 0.37 | -4.8 dB |
| Peaking | 364 Hz  | 4.51 | 1.9 dB  |
| Peaking | 3278 Hz | 1.17 | 5.1 dB  |
| Peaking | 5918 Hz | 4.18 | 5.2 dB  |
| Peaking | 450 Hz  | 8.78 | -1.3 dB |
| Peaking | 2649 Hz | 1.75 | 2.3 dB  |
| Peaking | 2725 Hz | 4.19 | -3.8 dB |
| Peaking | 7985 Hz | 6.62 | -1.1 dB |
| Peaking | 9816 Hz | 2.27 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ActionFit%20SHQ5200/Philips%20ActionFit%20SHQ5200.png)
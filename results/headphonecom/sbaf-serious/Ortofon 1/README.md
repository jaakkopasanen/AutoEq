# Ortofon 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 4.6; 369 2.1; 395 0.1; 423 -1.1; 452 -1.7; 484 -2.1; 518 -2.2; 554 -1.7; 593 -1.0; 635 0.8; 679 1.1; 726 0.8; 777 0.7; 832 0.3; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 0.7; 1248 0.9; 1336 1.2; 1429 -0.1; 1529 -0.7; 1636 -0.6; 1751 0.3; 1873 3.2; 2004 5.6; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.7; 3943 2.5; 4219 0.2; 4514 2.7; 4830 -0.1; 5168 -1.5; 5530 1.7; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.1; 8299 -1.5; 8880 -2.6; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.8; 16326 -1.3; 17469 -0.9; 18692 -2.6; 20000 -7.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 83 Hz    |  0.14 | 6.6 dB  |
| Peaking | 488 Hz   |  2.71 | -6.2 dB |
| Peaking | 2786 Hz  |  1.47 | 8.4 dB  |
| Peaking | 6289 Hz  |  5.35 | 7.1 dB  |
| Peaking | 12707 Hz |  0.03 | -1.7 dB |
| Peaking | 304 Hz   |  4.87 | 2.2 dB  |
| Peaking | 1715 Hz  |  2.99 | -3.2 dB |
| Peaking | 2006 Hz  |  5.19 | 4.4 dB  |
| Peaking | 5110 Hz  | 13.24 | -3.3 dB |
| Peaking | 13012 Hz |  2.13 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%201/Ortofon%201.png)
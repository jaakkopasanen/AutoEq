# Audeze LCD-XC sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.3; 59 4.4; 64 3.0; 68 2.6; 73 2.5; 78 2.4; 83 2.2; 89 2.0; 95 1.9; 102 1.9; 109 2.0; 117 1.7; 125 1.6; 134 1.6; 143 1.6; 153 1.7; 164 1.8; 175 1.3; 188 1.5; 201 1.6; 215 1.7; 230 1.9; 246 2.1; 263 2.2; 282 2.3; 301 2.4; 323 2.5; 345 2.5; 369 2.4; 395 2.3; 423 2.4; 452 2.2; 484 1.8; 518 1.7; 554 2.0; 593 2.2; 635 2.1; 679 1.8; 726 1.4; 777 1.1; 832 0.7; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.7; 1336 -2.3; 1429 -3.0; 1529 -3.7; 1636 -4.2; 1751 -4.3; 1873 -4.0; 2004 -3.2; 2145 -2.1; 2295 -1.0; 2455 0.6; 2627 1.7; 2811 2.1; 3008 3.1; 3219 3.7; 3444 4.4; 3685 4.4; 3943 2.8; 4219 -0.0; 4514 -2.8; 4830 -3.3; 5168 1.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -0.4; 16326 -0.6; 17469 -1.4; 18692 -2.8; 20000 -4.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.62 | 6.6 dB  |
| Peaking | 410 Hz  | 0.61 | 2.4 dB  |
| Peaking | 1677 Hz | 1.79 | -5.0 dB |
| Peaking | 3254 Hz | 3.32 | 5.0 dB  |
| Peaking | 6067 Hz | 5.33 | 6.8 dB  |
| Peaking | 74 Hz   | 4.43 | -0.6 dB |
| Peaking | 2563 Hz | 9.57 | 1.5 dB  |
| Peaking | 3833 Hz | 7.54 | 3.0 dB  |
| Peaking | 4796 Hz | 4.16 | -6.0 dB |
| Peaking | 5422 Hz | 8.45 | 5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC%20sample%202/Audeze%20LCD-XC%20sample%202.png)
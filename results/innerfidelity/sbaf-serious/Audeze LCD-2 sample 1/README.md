# Audeze LCD-2 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.4; 22 6.0; 23 5.8; 25 5.5; 26 5.4; 28 5.2; 30 5.1; 32 5.1; 35 5.1; 37 5.1; 40 5.0; 42 5.0; 45 5.0; 49 4.8; 52 4.7; 56 4.4; 59 4.2; 64 3.6; 68 3.2; 73 3.0; 78 2.9; 83 2.8; 89 2.6; 95 2.5; 102 2.3; 109 2.2; 117 2.0; 125 1.8; 134 1.7; 143 1.6; 153 1.4; 164 1.3; 175 1.2; 188 1.1; 201 1.0; 215 1.0; 230 1.0; 246 0.8; 263 0.7; 282 0.7; 301 0.7; 323 0.6; 345 0.5; 369 0.4; 395 0.4; 423 0.4; 452 0.3; 484 0.3; 518 0.6; 554 0.7; 593 0.6; 635 0.2; 679 -0.1; 726 -0.2; 777 -0.3; 832 -0.6; 890 -0.7; 952 -0.5; 1019 0.2; 1090 1.9; 1167 3.2; 1248 3.6; 1336 3.9; 1429 3.5; 1529 3.3; 1636 4.2; 1751 5.3; 1873 6.0; 2004 6.0; 2145 5.6; 2295 4.5; 2455 4.6; 2627 4.6; 2811 4.6; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.534684091410098dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.16 | 5.6 dB  |
| Peaking | 32 Hz   | 0.35 | 4.6 dB  |
| Peaking | 1864 Hz | 1.58 | 4.9 dB  |
| Peaking | 3750 Hz | 1.54 | 5.3 dB  |
| Peaking | 5757 Hz | 3.17 | 4.6 dB  |
| Peaking | 956 Hz  | 2.25 | -2.8 dB |
| Peaking | 1138 Hz | 0.15 | 0.2 dB  |
| Peaking | 1190 Hz | 2.88 | 2.9 dB  |
| Peaking | 1558 Hz | 5.66 | -1.4 dB |
| Peaking | 8406 Hz | 3.29 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sample%201/Audeze%20LCD-2%20sample%201.png)
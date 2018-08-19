# HiFiMAN HE400S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.5; 52 5.2; 56 4.9; 59 4.6; 64 4.1; 68 3.7; 73 3.3; 78 2.9; 83 2.6; 89 2.2; 95 1.8; 102 1.7; 109 1.5; 117 1.3; 125 1.1; 134 0.9; 143 0.8; 153 0.7; 164 0.6; 175 0.6; 188 0.5; 201 0.5; 215 0.6; 230 0.7; 246 0.7; 263 0.6; 282 0.6; 301 0.4; 323 0.3; 345 0.2; 369 0.2; 395 -0.0; 423 0.5; 452 0.7; 484 1.0; 518 1.3; 554 1.2; 593 1.1; 635 1.1; 679 1.0; 726 0.8; 777 0.6; 832 0.3; 890 0.1; 952 -0.1; 1019 -0.1; 1090 -0.1; 1167 0.7; 1248 0.5; 1336 0.1; 1429 -0.2; 1529 0.1; 1636 0.2; 1751 0.6; 1873 1.2; 2004 1.6; 2145 1.6; 2295 2.2; 2455 2.6; 2627 2.9; 2811 2.2; 3008 2.1; 3219 2.4; 3444 2.4; 3685 2.4; 3943 2.2; 4219 0.5; 4514 -0.3; 4830 1.9; 5168 5.2; 5530 6.0; 5917 3.9; 6331 1.7; 6775 1.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.139846745254403dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE400S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  0.44 | 5.5 dB  |
| Peaking | 49 Hz   |  1.12 | 2.3 dB  |
| Peaking | 567 Hz  |  2.57 | 1.3 dB  |
| Peaking | 2749 Hz |  1.73 | 2.7 dB  |
| Peaking | 5514 Hz |  5.46 | 6.1 dB  |
| Peaking | 1464 Hz |  6.24 | -0.6 dB |
| Peaking | 3809 Hz |  6.13 | 1.2 dB  |
| Peaking | 4475 Hz |  9.94 | -2.3 dB |
| Peaking | 6938 Hz | 13.11 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE400S/HiFiMAN%20HE400S.png)
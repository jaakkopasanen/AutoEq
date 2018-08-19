# Yamaha HPH MT220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.2; 23 2.0; 25 1.5; 26 1.3; 28 1.0; 30 0.8; 32 0.6; 35 0.5; 37 0.4; 40 0.3; 42 0.3; 45 0.3; 49 0.3; 52 0.3; 56 0.4; 59 0.4; 64 0.3; 68 0.3; 73 0.3; 78 0.4; 83 0.4; 89 0.3; 95 0.3; 102 0.6; 109 1.0; 117 1.5; 125 2.0; 134 2.2; 143 1.7; 153 1.0; 164 1.9; 175 2.8; 188 2.0; 201 1.9; 215 2.1; 230 2.4; 246 2.8; 263 3.2; 282 3.8; 301 4.0; 323 3.8; 345 3.8; 369 3.9; 395 3.9; 423 3.8; 452 3.4; 484 2.8; 518 2.3; 554 2.0; 593 1.7; 635 1.3; 679 0.8; 726 0.4; 777 0.3; 832 0.1; 890 -0.0; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.6; 1248 1.0; 1336 0.9; 1429 0.8; 1529 1.2; 1636 1.8; 1751 2.9; 1873 4.1; 2004 5.4; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.5; 4514 4.1; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999964dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH MT220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.77 | 2.7 dB  |
| Peaking | 160 Hz  | 1.17 | 1.5 dB  |
| Peaking | 353 Hz  | 1.46 | 4.0 dB  |
| Peaking | 2764 Hz | 1.27 | 6.5 dB  |
| Peaking | 5590 Hz | 2.68 | 5.3 dB  |
| Peaking | 1117 Hz | 1.38 | -1.0 dB |
| Peaking | 2066 Hz | 5.37 | 2.0 dB  |
| Peaking | 2770 Hz | 4.31 | -1.0 dB |
| Peaking | 3722 Hz | 7.59 | 1.5 dB  |
| Peaking | 8376 Hz | 3.84 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HPH%20MT220/Yamaha%20HPH%20MT220.png)
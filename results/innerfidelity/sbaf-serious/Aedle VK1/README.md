# Aedle VK1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.6; 42 5.1; 45 4.0; 49 2.8; 52 1.9; 56 0.8; 59 0.0; 64 -1.1; 68 -2.0; 73 -2.9; 78 -3.7; 83 -4.3; 89 -4.8; 95 -5.1; 102 -5.2; 109 -5.1; 117 -4.9; 125 -4.8; 134 -4.6; 143 -4.4; 153 -4.2; 164 -3.9; 175 -3.6; 188 -3.4; 201 -3.2; 215 -2.9; 230 -2.6; 246 -2.4; 263 -2.2; 282 -1.8; 301 -1.4; 323 -1.0; 345 -1.0; 369 -1.1; 395 -0.8; 423 -0.4; 452 -0.1; 484 0.2; 518 0.5; 554 1.0; 593 -0.4; 635 -0.6; 679 0.9; 726 1.7; 777 2.1; 832 2.0; 890 1.4; 952 0.6; 1019 -0.2; 1090 -1.0; 1167 -1.9; 1248 -2.9; 1336 -3.9; 1429 -4.9; 1529 -5.6; 1636 -5.9; 1751 -5.0; 1873 -4.2; 2004 -4.0; 2145 -3.3; 2295 -2.4; 2455 -1.2; 2627 0.1; 2811 1.4; 3008 2.9; 3219 3.9; 3444 4.5; 3685 5.7; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.2; 6331 4.3; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aedle VK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.53 | 9.7 dB  |
| Peaking | 88 Hz   | 0.59 | -9.2 dB |
| Peaking | 849 Hz  | 1.57 | 3.6 dB  |
| Peaking | 1645 Hz | 1.22 | -7.1 dB |
| Peaking | 4267 Hz | 1.22 | 7.6 dB  |
| Peaking | 578 Hz  | 3.19 | 1.7 dB  |
| Peaking | 611 Hz  | 7.75 | -3.0 dB |
| Peaking | 4488 Hz | 4.41 | -1.7 dB |
| Peaking | 6205 Hz | 1.56 | 3.7 dB  |
| Peaking | 7704 Hz | 1.55 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aedle%20VK1/Aedle%20VK1.png)
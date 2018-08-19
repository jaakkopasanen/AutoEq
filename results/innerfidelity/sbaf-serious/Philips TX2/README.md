# Philips TX2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -6.5; 22 -6.5; 23 -6.5; 25 -6.5; 26 -6.5; 28 -6.5; 30 -6.5; 32 -6.4; 35 -6.4; 37 -6.4; 40 -6.4; 42 -6.4; 45 -6.4; 49 -6.4; 52 -6.4; 56 -6.4; 59 -6.5; 64 -6.5; 68 -6.6; 73 -6.6; 78 -6.7; 83 -6.8; 89 -6.8; 95 -6.9; 102 -6.9; 109 -6.7; 117 -6.6; 125 -6.6; 134 -6.5; 143 -6.4; 153 -6.2; 164 -6.0; 175 -5.7; 188 -5.5; 201 -5.2; 215 -5.0; 230 -4.6; 246 -4.3; 263 -4.0; 282 -3.6; 301 -3.2; 323 -2.9; 345 -2.5; 369 -2.2; 395 -1.9; 423 -1.5; 452 -1.1; 484 -0.4; 518 -0.5; 554 -0.1; 593 0.4; 635 0.6; 679 0.6; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -2.1; 1529 -2.6; 1636 -3.2; 1751 -3.6; 1873 -3.8; 2004 -4.1; 2145 -4.3; 2295 -4.0; 2455 -3.0; 2627 -1.8; 2811 -0.5; 3008 1.2; 3219 2.5; 3444 3.5; 3685 3.4; 3943 2.6; 4219 0.6; 4514 -1.2; 4830 -2.4; 5168 -3.3; 5530 -3.7; 5917 -4.0; 6331 -3.6; 6775 -2.0; 7249 -1.0; 7756 -0.8; 8299 -1.3; 8880 -1.6; 9502 -1.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.666901724392512dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.25 | -7.2 dB |
| Peaking | 2093 Hz | 2.04 | -5.0 dB |
| Peaking | 3547 Hz | 2.73 | 5.4 dB  |
| Peaking | 5554 Hz | 2.29 | -4.6 dB |
| Peaking | 8986 Hz | 6.65 | -1.1 dB |
| Peaking | 18 Hz   | 1.1  | -1.9 dB |
| Peaking | 54 Hz   | 0.85 | 1.2 dB  |
| Peaking | 177 Hz  | 0.65 | -1.0 dB |
| Peaking | 685 Hz  | 1.11 | 1.9 dB  |
| Peaking | 1499 Hz | 3.37 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX2/Philips%20TX2.png)
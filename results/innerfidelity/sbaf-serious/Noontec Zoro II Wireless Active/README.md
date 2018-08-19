# Noontec Zoro II Wireless Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 0.6; 22 -0.0; 23 -0.3; 25 -0.7; 26 -0.9; 28 -1.3; 30 -1.5; 32 -1.8; 35 -2.1; 37 -2.3; 40 -2.5; 42 -2.6; 45 -2.8; 49 -2.9; 52 -3.1; 56 -3.3; 59 -3.4; 64 -3.4; 68 -3.5; 73 -3.7; 78 -4.1; 83 -4.5; 89 -5.0; 95 -5.2; 102 -5.4; 109 -5.7; 117 -5.9; 125 -6.1; 134 -6.2; 143 -6.6; 153 -6.7; 164 -6.5; 175 -6.5; 188 -6.7; 201 -6.6; 215 -6.4; 230 -6.2; 246 -6.0; 263 -5.7; 282 -5.1; 301 -4.8; 323 -4.7; 345 -4.4; 369 -4.1; 395 -4.1; 423 -3.9; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.5; 593 -1.9; 635 -1.5; 679 -1.2; 726 -0.7; 777 -0.3; 832 -0.1; 890 -0.0; 952 0.0; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -1.9; 1751 -1.9; 1873 -1.5; 2004 -1.0; 2145 -0.3; 2295 0.3; 2455 1.0; 2627 1.5; 2811 1.8; 3008 2.0; 3219 1.8; 3444 1.9; 3685 2.9; 3943 5.0; 4219 4.9; 4514 3.9; 4830 2.8; 5168 1.5; 5530 1.7; 5917 2.1; 6331 0.4; 6775 -0.1; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.385123120014757dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 0.42 | -2.7 dB |
| Peaking | 206 Hz  | 0.59 | -4.9 dB |
| Peaking | 1704 Hz | 4.19 | -2.2 dB |
| Peaking | 4112 Hz | 2.18 | 4.7 dB  |
| Peaking | 72 Hz   | 4.97 | 0.4 dB  |
| Peaking | 481 Hz  | 3.21 | -1.0 dB |
| Peaking | 875 Hz  | 1.8  | 1.1 dB  |
| Peaking | 2507 Hz | 0.99 | -0.8 dB |
| Peaking | 2658 Hz | 3.53 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Active/Noontec%20Zoro%20II%20Wireless%20Active.png)
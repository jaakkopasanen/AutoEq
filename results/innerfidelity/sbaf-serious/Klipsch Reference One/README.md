# Klipsch Reference ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.9; 22 -4.1; 23 -4.2; 25 -4.4; 26 -4.5; 28 -4.6; 30 -4.8; 32 -4.9; 35 -5.0; 37 -5.1; 40 -5.3; 42 -5.3; 45 -5.5; 49 -5.6; 52 -5.7; 56 -5.9; 59 -6.0; 64 -6.2; 68 -6.4; 73 -6.6; 78 -6.8; 83 -6.9; 89 -7.0; 95 -7.1; 102 -7.1; 109 -7.0; 117 -7.1; 125 -7.4; 134 -7.7; 143 -7.5; 153 -7.7; 164 -7.3; 175 -7.1; 188 -6.9; 201 -6.7; 215 -6.6; 230 -6.5; 246 -6.0; 263 -5.4; 282 -4.6; 301 -4.2; 323 -3.9; 345 -3.6; 369 -3.0; 395 -2.2; 423 -1.1; 452 -0.3; 484 -0.0; 518 0.6; 554 1.4; 593 2.3; 635 2.8; 679 2.8; 726 2.7; 777 2.5; 832 1.8; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.5; 1167 -0.3; 1248 -0.3; 1336 -1.5; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.0; 1873 -3.0; 2004 -3.0; 2145 -3.1; 2295 -3.4; 2455 -3.3; 2627 -3.3; 2811 -3.3; 3008 -2.7; 3219 -2.1; 3444 -0.8; 3685 1.0; 3943 2.7; 4219 4.0; 4514 5.4; 4830 5.6; 5168 3.6; 5530 2.5; 5917 2.6; 6331 1.8; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9766913502514605dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.45 | -5.5 dB |
| Peaking | 141 Hz  | 1.15 | -4.7 dB |
| Peaking | 242 Hz  | 2.05 | -3.6 dB |
| Peaking | 4730 Hz | 4.41 | 6.3 dB  |
| Peaking | 14 Hz   | 1.87 | -0.9 dB |
| Peaking | 357 Hz  | 3.68 | -1.7 dB |
| Peaking | 685 Hz  | 1.66 | 4.0 dB  |
| Peaking | 2761 Hz | 0.79 | -7.0 dB |
| Peaking | 3940 Hz | 0.89 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)
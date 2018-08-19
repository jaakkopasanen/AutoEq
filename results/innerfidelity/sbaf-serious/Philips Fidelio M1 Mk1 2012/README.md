# Philips Fidelio M1 Mk1 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.6; 22 0.4; 23 0.3; 25 0.1; 26 0.1; 28 -0.0; 30 -0.1; 32 -0.1; 35 -0.1; 37 -0.1; 40 -0.1; 42 -0.1; 45 -0.1; 49 -0.1; 52 -0.0; 56 0.0; 59 0.1; 64 0.2; 68 0.2; 73 0.2; 78 0.1; 83 -0.1; 89 -0.3; 95 -0.3; 102 -0.2; 109 0.0; 117 0.2; 125 0.4; 134 0.5; 143 0.5; 153 0.8; 164 1.2; 175 1.7; 188 1.9; 201 2.0; 215 2.2; 230 2.3; 246 2.4; 263 2.5; 282 2.7; 301 2.8; 323 2.7; 345 2.3; 369 1.9; 395 1.6; 423 1.1; 452 0.5; 484 -0.0; 518 -0.3; 554 -0.2; 593 -0.2; 635 -0.4; 679 -0.5; 726 -0.3; 777 -0.1; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.5; 1429 0.5; 1529 0.4; 1636 0.4; 1751 0.7; 1873 1.1; 2004 1.7; 2145 2.4; 2295 3.1; 2455 4.0; 2627 4.8; 2811 5.3; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999999703621dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 Mk1 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 280 Hz  | 0.86 | 5.6 dB  |
| Peaking | 331 Hz  | 0.44 | -2.8 dB |
| Peaking | 3343 Hz | 1.31 | 6.1 dB  |
| Peaking | 5665 Hz | 2.75 | 4.7 dB  |
| Peaking | 251 Hz  | 8.31 | -0.4 dB |
| Peaking | 1735 Hz | 2.55 | -1.7 dB |
| Peaking | 1742 Hz | 1.17 | 1.1 dB  |
| Peaking | 6507 Hz | 7.22 | 2.1 dB  |
| Peaking | 7851 Hz | 2.18 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1%20Mk1%202012/Philips%20Fidelio%20M1%20Mk1%202012.png)
# Echobox Finder X1 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 10 -84; 20 -10.7; 22 -10.7; 23 -10.7; 25 -10.7; 26 -10.6; 28 -10.6; 30 -10.5; 32 -10.4; 35 -10.3; 37 -10.2; 40 -10.1; 42 -10.0; 45 -9.9; 49 -9.8; 52 -9.7; 56 -9.5; 59 -9.5; 64 -9.3; 68 -9.3; 73 -9.2; 78 -9.1; 83 -9.0; 89 -9.0; 95 -8.9; 102 -8.7; 109 -8.4; 117 -8.2; 125 -8.1; 134 -7.8; 143 -7.6; 153 -7.4; 164 -7.1; 175 -6.8; 188 -6.5; 201 -6.1; 215 -5.7; 230 -5.4; 246 -5.0; 263 -4.7; 282 -4.2; 301 -3.9; 323 -3.4; 345 -3.0; 369 -2.7; 395 -2.3; 423 -1.8; 452 -1.5; 484 -1.2; 518 -0.9; 554 -0.5; 593 -0.0; 635 0.2; 679 0.3; 726 0.4; 777 0.7; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.0; 1873 -3.1; 2004 -3.2; 2145 -3.3; 2295 -3.5; 2455 -3.4; 2627 -3.7; 2811 -4.4; 3008 -4.8; 3219 -5.2; 3444 -5.4; 3685 -5.6; 3943 -6.0; 4219 -7.2; 4514 -8.4; 4830 -9.1; 5168 -9.6; 5530 -10.6; 5917 -11.3; 6331 -11.5; 6775 -9.5; 7249 -7.9; 7756 -7.2; 8299 -7.6; 8880 -8.9; 9502 -9.9; 10167 -9.0; 10879 -5.2; 11640 -0.7; 12455 0.0; 13327 -0.9; 14260 -4.0; 15258 -4.2; 16326 -0.9; 17469 0.0; 18692 0.0; 20000 -0.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7915812653542692dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.21 | -10.5 dB |
| Peaking | 162 Hz   | 0.77 | -3.5 dB  |
| Peaking | 5666 Hz  | 0.84 | -10.4 dB |
| Peaking | 9673 Hz  | 5.23 | -5.9 dB  |
| Peaking | 24000 Hz | 2.01 | -1.4 dB  |
| Peaking | 801 Hz   | 1.78 | 1.7 dB   |
| Peaking | 1797 Hz  | 1.73 | -1.5 dB  |
| Peaking | 3931 Hz  | 5.69 | 1.2 dB   |
| Peaking | 12398 Hz | 4.99 | 3.7 dB   |
| Peaking | 14915 Hz | 4.97 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Black%20Filter/Echobox%20Finder%20X1%20Black%20Filter.png)
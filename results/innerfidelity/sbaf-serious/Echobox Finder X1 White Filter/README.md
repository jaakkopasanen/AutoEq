# Echobox Finder X1 White Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -10.5; 22 -10.4; 23 -10.4; 25 -10.3; 26 -10.3; 28 -10.3; 30 -10.2; 32 -10.1; 35 -10.0; 37 -9.9; 40 -9.8; 42 -9.7; 45 -9.6; 49 -9.5; 52 -9.4; 56 -9.3; 59 -9.2; 64 -9.1; 68 -9.0; 73 -8.9; 78 -8.8; 83 -8.7; 89 -8.7; 95 -8.6; 102 -8.4; 109 -8.2; 117 -7.9; 125 -7.8; 134 -7.6; 143 -7.3; 153 -7.1; 164 -6.8; 175 -6.5; 188 -6.2; 201 -5.9; 215 -5.5; 230 -5.1; 246 -4.8; 263 -4.4; 282 -4.0; 301 -3.6; 323 -3.2; 345 -2.9; 369 -2.5; 395 -2.1; 423 -1.6; 452 -1.3; 484 -1.0; 518 -0.7; 554 -0.3; 593 0.1; 635 0.4; 679 0.4; 726 0.7; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.3; 1636 -2.7; 1751 -3.0; 1873 -3.0; 2004 -2.9; 2145 -3.0; 2295 -3.0; 2455 -2.8; 2627 -2.9; 2811 -3.2; 3008 -3.4; 3219 -3.7; 3444 -4.1; 3685 -4.6; 3943 -5.2; 4219 -6.6; 4514 -7.6; 4830 -7.9; 5168 -7.8; 5530 -8.3; 5917 -8.2; 6331 -8.7; 6775 -7.4; 7249 -5.9; 7756 -4.6; 8299 -3.7; 8880 -3.5; 9502 -4.5; 10167 -6.4; 10879 -7.2; 11640 -5.4; 12455 -2.7; 13327 -1.9; 14260 -3.4; 15258 -3.9; 16326 -1.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9216460278331491dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.22 | -10.2 dB |
| Peaking | 159 Hz   | 0.8  | -3.4 dB  |
| Peaking | 1869 Hz  | 2.51 | -2.2 dB  |
| Peaking | 5423 Hz  | 1.09 | -8.4 dB  |
| Peaking | 10991 Hz | 3.12 | -5.5 dB  |
| Peaking | 308 Hz   | 1.88 | -0.7 dB  |
| Peaking | 749 Hz   | 1.51 | 1.6 dB   |
| Peaking | 1472 Hz  | 3.5  | -0.7 dB  |
| Peaking | 8512 Hz  | 7.11 | 1.2 dB   |
| Peaking | 15007 Hz | 5.33 | -3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20White%20Filter/Echobox%20Finder%20X1%20White%20Filter.png)
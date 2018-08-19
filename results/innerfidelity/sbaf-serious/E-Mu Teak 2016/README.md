# E-Mu Teak 2016

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -1.5; 22 -2.0; 23 -2.2; 25 -2.6; 26 -2.8; 28 -3.1; 30 -3.3; 32 -3.4; 35 -3.5; 37 -3.6; 40 -3.7; 42 -3.7; 45 -3.8; 49 -3.8; 52 -3.9; 56 -3.8; 59 -3.8; 64 -3.7; 68 -3.6; 73 -3.5; 78 -3.7; 83 -4.0; 89 -4.2; 95 -4.2; 102 -4.3; 109 -4.3; 117 -4.3; 125 -4.4; 134 -4.4; 143 -4.4; 153 -4.3; 164 -4.0; 175 -3.9; 188 -3.9; 201 -3.8; 215 -3.5; 230 -3.1; 246 -2.8; 263 -2.4; 282 -2.1; 301 -1.9; 323 -1.7; 345 -1.5; 369 -1.3; 395 -1.0; 423 -0.6; 452 -0.4; 484 -0.3; 518 -0.2; 554 0.1; 593 0.3; 635 0.2; 679 -0.1; 726 -0.2; 777 -0.2; 832 -0.2; 890 0.3; 952 0.2; 1019 -0.0; 1090 0.1; 1167 0.3; 1248 0.4; 1336 0.5; 1429 0.3; 1529 0.2; 1636 0.3; 1751 0.6; 1873 0.9; 2004 1.4; 2145 1.8; 2295 2.2; 2455 2.8; 2627 3.2; 2811 3.2; 3008 3.7; 3219 3.8; 3444 3.0; 3685 2.7; 3943 2.5; 4219 2.4; 4514 1.7; 4830 0.9; 5168 0.7; 5530 1.1; 5917 1.3; 6331 1.9; 6775 2.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -0.9; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.028158869660874dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak 2016 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.48 | -3.3 dB |
| Peaking | 157 Hz  | 0.83 | -3.5 dB |
| Peaking | 3047 Hz | 1.51 | 3.8 dB  |
| Peaking | 6684 Hz | 6.76 | 2.4 dB  |
| Peaking | 590 Hz  | 3.12 | 0.7 dB  |
| Peaking | 727 Hz  | 4.93 | -0.3 dB |
| Peaking | 9847 Hz | 6.5  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%202016/E-Mu%20Teak%202016.png)
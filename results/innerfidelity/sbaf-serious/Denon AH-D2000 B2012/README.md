# Denon AH-D2000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 2.2; 22 1.4; 23 1.1; 25 0.5; 26 0.2; 28 -0.1; 30 -0.4; 32 -0.5; 35 -0.7; 37 -0.7; 40 -0.8; 42 -0.8; 45 -0.7; 49 -0.5; 52 -0.4; 56 -0.4; 59 -0.5; 64 -0.5; 68 -0.5; 73 -0.6; 78 -0.8; 83 -1.0; 89 -1.2; 95 -1.5; 102 -1.6; 109 -1.7; 117 -1.8; 125 -2.0; 134 -2.2; 143 -2.3; 153 -2.2; 164 -2.1; 175 -2.2; 188 -2.2; 201 -2.3; 215 -2.2; 230 -2.1; 246 -2.0; 263 -1.9; 282 -1.8; 301 -1.7; 323 -1.6; 345 -1.5; 369 -1.3; 395 -1.1; 423 -0.9; 452 -0.8; 484 -1.0; 518 -1.2; 554 -1.3; 593 -1.2; 635 -1.4; 679 -0.4; 726 1.4; 777 0.8; 832 -0.0; 890 -0.3; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.7; 1248 1.0; 1336 1.1; 1429 1.0; 1529 0.8; 1636 0.6; 1751 0.9; 1873 1.1; 2004 1.4; 2145 1.5; 2295 1.5; 2455 1.7; 2627 1.6; 2811 3.2; 3008 5.4; 3219 4.7; 3444 2.6; 3685 1.4; 3943 1.2; 4219 1.3; 4514 2.2; 4830 3.2; 5168 2.6; 5530 2.9; 5917 1.9; 6331 1.2; 6775 0.7; 7249 0.2; 7756 0.2; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -1.4; 10879 -1.3; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.649255918213073dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.54 | -2.3 dB |
| Peaking | 1767 Hz  | 0.88 | 1.0 dB  |
| Peaking | 3072 Hz  | 5.59 | 5.0 dB  |
| Peaking | 5188 Hz  | 3.03 | 2.9 dB  |
| Peaking | 10492 Hz | 5.03 | -1.6 dB |
| Peaking | 14 Hz    | 0.71 | 3.0 dB  |
| Peaking | 31 Hz    | 1.53 | -1.6 dB |
| Peaking | 655 Hz   | 4.22 | -2.0 dB |
| Peaking | 720 Hz   | 5.51 | 2.8 dB  |
| Peaking | 895 Hz   | 5.25 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000%20B2012/Denon%20AH-D2000%20B2012.png)
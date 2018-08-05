# Denon AH-D5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.7; 26 5.4; 28 4.6; 30 3.8; 32 3.0; 35 2.1; 37 1.7; 40 1.3; 42 1.1; 45 0.9; 49 0.7; 52 0.6; 56 0.8; 59 0.9; 64 1.1; 68 1.0; 73 1.0; 78 1.0; 83 1.0; 89 1.1; 95 1.0; 102 0.8; 109 0.7; 117 0.5; 125 0.2; 134 -0.0; 143 -0.1; 153 -0.2; 164 -0.1; 175 0.1; 188 0.1; 201 0.2; 215 0.4; 230 0.6; 246 0.7; 263 0.9; 282 1.2; 301 1.3; 323 1.5; 345 1.8; 369 2.0; 395 2.1; 423 2.4; 452 2.5; 484 2.3; 518 1.9; 554 1.5; 593 0.8; 635 -0.1; 679 -1.0; 726 -1.7; 777 -2.3; 832 -2.9; 890 -3.0; 952 -0.8; 1019 -0.4; 1090 -1.4; 1167 -1.1; 1248 -0.7; 1336 -0.3; 1429 -0.1; 1529 0.0; 1636 0.4; 1751 0.9; 1873 1.4; 2004 1.9; 2145 2.2; 2295 2.5; 2455 2.0; 2627 1.2; 2811 0.4; 3008 -0.4; 3219 -0.8; 3444 -1.3; 3685 -1.1; 3943 -0.4; 4219 -0.0; 4514 0.8; 4830 1.8; 5168 2.8; 5530 2.3; 5917 1.1; 6331 0.7; 6775 0.5; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -3.0; 10167 -3.2; 10879 -2.2; 11640 -2.0; 12455 -1.5; 13327 -0.1; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.9; 20000 -1.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.2  | 6.2 dB  |
| Peaking | 456 Hz   | 1.31 | 2.9 dB  |
| Peaking | 808 Hz   | 2.18 | -3.6 dB |
| Peaking | 2195 Hz  | 3.53 | 2.7 dB  |
| Peaking | 10222 Hz | 4.21 | -3.5 dB |
| Peaking | 85 Hz    | 2.95 | 0.8 dB  |
| Peaking | 1167 Hz  | 9.53 | -0.7 dB |
| Peaking | 3539 Hz  | 3.98 | -1.9 dB |
| Peaking | 5270 Hz  | 3.16 | 2.8 dB  |
| Peaking | 12051 Hz | 7.74 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)
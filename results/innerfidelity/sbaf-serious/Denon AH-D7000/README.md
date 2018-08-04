# Denon AH-D7000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.4; 32 4.8; 35 3.8; 37 3.3; 40 2.8; 42 2.6; 45 2.4; 49 2.2; 52 2.0; 56 2.0; 59 2.0; 64 2.1; 68 2.1; 73 2.1; 78 2.1; 83 2.1; 89 2.1; 95 2.0; 102 2.0; 109 1.9; 117 1.8; 125 1.6; 134 1.4; 143 1.4; 153 1.4; 164 1.6; 175 1.8; 188 1.9; 201 2.0; 215 2.4; 230 2.8; 246 3.1; 263 3.4; 282 3.8; 301 4.1; 323 4.4; 345 4.8; 369 4.9; 395 4.7; 423 4.4; 452 3.9; 484 2.7; 518 1.7; 554 1.0; 593 0.4; 635 0.1; 679 -0.4; 726 -0.7; 777 -0.7; 832 0.3; 890 0.7; 952 0.3; 1019 -0.2; 1090 0.2; 1167 0.6; 1248 1.0; 1336 1.1; 1429 1.2; 1529 1.3; 1636 1.5; 1751 2.0; 1873 2.3; 2004 2.5; 2145 2.7; 2295 3.2; 2455 3.8; 2627 4.4; 2811 4.6; 3008 4.8; 3219 4.6; 3444 4.1; 3685 3.2; 3943 2.5; 4219 0.2; 4514 -0.3; 4830 0.9; 5168 1.7; 5530 1.7; 5917 0.4; 6331 -0.0; 6775 -0.1; 7249 0.1; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -1.4; 10879 -2.0; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.18 | 6.1 dB  |
| Peaking | 97 Hz    | 0.55 | 1.5 dB  |
| Peaking | 350 Hz   | 1.76 | 4.8 dB  |
| Peaking | 3012 Hz  | 2.24 | 4.7 dB  |
| Peaking | 2022 Hz  | 2.14 | 1.6 dB  |
| Peaking | 447 Hz   | 7.39 | 1.3 dB  |
| Peaking | 699 Hz   | 3.34 | -1.6 dB |
| Peaking | 4449 Hz  | 6.75 | -3.8 dB |
| Peaking | 4593 Hz  | 2.76 | 2.0 dB  |
| Peaking | 10752 Hz | 6.48 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)
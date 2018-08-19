# HiFiMAN Edition X V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 4.8; 22 4.4; 23 4.2; 25 3.9; 26 3.8; 28 3.6; 30 3.4; 32 3.3; 35 3.2; 37 3.1; 40 3.1; 42 3.1; 45 3.2; 49 3.2; 52 3.1; 56 2.6; 59 2.1; 64 1.5; 68 1.3; 73 1.1; 78 1.0; 83 0.9; 89 0.7; 95 0.5; 102 0.3; 109 0.3; 117 0.0; 125 -0.2; 134 -0.2; 143 -0.4; 153 -0.5; 164 -0.7; 175 -0.8; 188 -0.9; 201 -1.0; 215 -1.1; 230 -1.2; 246 -1.4; 263 -1.7; 282 -2.0; 301 -1.6; 323 0.1; 345 -1.3; 369 0.5; 395 0.2; 423 -0.3; 452 -0.9; 484 -1.6; 518 -2.5; 554 -1.6; 593 0.5; 635 -1.6; 679 -0.6; 726 1.8; 777 0.6; 832 1.7; 890 1.1; 952 -0.1; 1019 1.8; 1090 4.7; 1167 3.4; 1248 3.2; 1336 3.6; 1429 5.8; 1529 4.5; 1636 5.2; 1751 4.7; 1873 4.5; 2004 3.5; 2145 3.2; 2295 2.2; 2455 1.6; 2627 1.1; 2811 0.5; 3008 1.1; 3219 1.0; 3444 1.3; 3685 1.8; 3943 1.7; 4219 0.7; 4514 0.7; 4830 1.1; 5168 2.1; 5530 4.0; 5917 3.5; 6331 0.4; 6775 -0.4; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -2.9; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.940979568056768dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.8  | 4.9 dB  |
| Peaking | 48 Hz   | 1.1  | 2.3 dB  |
| Peaking | 359 Hz  | 0.39 | -1.4 dB |
| Peaking | 1516 Hz | 1.22 | 5.5 dB  |
| Peaking | 5632 Hz | 6.98 | 4.3 dB  |
| Peaking | 392 Hz  | 3.26 | 3.6 dB  |
| Peaking | 435 Hz  | 1.46 | -2.3 dB |
| Peaking | 734 Hz  | 7.76 | 1.7 dB  |
| Peaking | 3337 Hz | 1.83 | -0.9 dB |
| Peaking | 3730 Hz | 4.58 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X%20V2/HiFiMAN%20Edition%20X%20V2.png)
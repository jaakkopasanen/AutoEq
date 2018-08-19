# Shure SRH750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.5; 40 5.0; 42 4.6; 45 4.2; 49 3.7; 52 3.5; 56 3.2; 59 2.9; 64 2.4; 68 1.9; 73 1.4; 78 0.9; 83 0.6; 89 0.4; 95 0.4; 102 0.7; 109 0.9; 117 0.7; 125 0.2; 134 -0.3; 143 -0.8; 153 -1.1; 164 -1.0; 175 -0.6; 188 -0.9; 201 -1.2; 215 -1.1; 230 -1.2; 246 -2.3; 263 -2.7; 282 -2.5; 301 -2.2; 323 -1.8; 345 -1.6; 369 -1.5; 395 -1.6; 423 -1.8; 452 -1.9; 484 -2.1; 518 -2.1; 554 -1.9; 593 -1.6; 635 -1.4; 679 -1.2; 726 -0.7; 777 -0.2; 832 0.1; 890 0.4; 952 0.4; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 -0.0; 1336 -0.3; 1429 -1.1; 1529 -2.0; 1636 -2.9; 1751 -4.4; 1873 -5.8; 2004 -7.0; 2145 -7.8; 2295 -7.6; 2455 -6.0; 2627 -4.6; 2811 -2.4; 3008 -0.6; 3219 0.6; 3444 2.0; 3685 2.4; 3943 2.0; 4219 -0.2; 4514 -0.9; 4830 2.2; 5168 4.7; 5530 4.9; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -3.3; 8880 -6.0; 9502 -5.0; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.71 | 6.4 dB  |
| Peaking | 303 Hz  | 0.79 | -2.3 dB |
| Peaking | 2160 Hz | 2.93 | -8.7 dB |
| Peaking | 6004 Hz | 2.13 | 6.5 dB  |
| Peaking | 8921 Hz | 4.47 | -7.8 dB |
| Peaking | 563 Hz  | 3.38 | -1.0 dB |
| Peaking | 922 Hz  | 2.58 | 1.1 dB  |
| Peaking | 2618 Hz | 5.34 | -1.8 dB |
| Peaking | 3656 Hz | 2.53 | 2.8 dB  |
| Peaking | 4403 Hz | 7.84 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)
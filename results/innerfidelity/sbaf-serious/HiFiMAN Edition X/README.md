# HiFiMAN Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.2; 32 4.8; 35 4.5; 37 4.3; 40 4.1; 42 4.0; 45 3.9; 49 3.8; 52 3.7; 56 3.6; 59 3.5; 64 3.4; 68 3.3; 73 3.2; 78 3.0; 83 2.6; 89 2.2; 95 1.9; 102 1.8; 109 1.7; 117 1.6; 125 1.5; 134 1.4; 143 1.4; 153 1.4; 164 1.2; 175 1.2; 188 1.1; 201 1.1; 215 1.0; 230 0.9; 246 0.8; 263 0.7; 282 0.7; 301 0.5; 323 0.6; 345 1.2; 369 1.5; 395 1.7; 423 1.5; 452 1.1; 484 0.6; 518 0.3; 554 0.1; 593 0.5; 635 0.2; 679 0.3; 726 1.1; 777 2.7; 832 2.4; 890 1.1; 952 0.4; 1019 0.8; 1090 2.7; 1167 3.9; 1248 3.8; 1336 2.2; 1429 2.9; 1529 2.8; 1636 2.5; 1751 1.6; 1873 2.1; 2004 2.4; 2145 2.0; 2295 2.1; 2455 2.2; 2627 2.0; 2811 1.8; 3008 1.5; 3219 1.8; 3444 2.8; 3685 2.6; 3943 2.1; 4219 0.7; 4514 0.1; 4830 1.2; 5168 3.3; 5530 4.5; 5917 4.0; 6331 2.2; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 -5.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.22 | 5.6 dB  |
| Peaking | 53 Hz   | 0.05 | 0.6 dB  |
| Peaking | 1203 Hz | 5.32 | 2.6 dB  |
| Peaking | 2194 Hz | 0.69 | 2.1 dB  |
| Peaking | 5728 Hz | 4.83 | 4.2 dB  |
| Peaking | 402 Hz  | 5.58 | 1.2 dB  |
| Peaking | 761 Hz  | 1.75 | -1.5 dB |
| Peaking | 789 Hz  | 6.84 | 3.5 dB  |
| Peaking | 3671 Hz | 6.32 | 1.5 dB  |
| Peaking | 4462 Hz | 9.14 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X/HiFiMAN%20Edition%20X.png)
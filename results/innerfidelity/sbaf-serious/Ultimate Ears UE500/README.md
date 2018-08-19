# Ultimate Ears UE500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -8.7; 22 -8.7; 23 -8.6; 25 -8.6; 26 -8.6; 28 -8.5; 30 -8.4; 32 -8.3; 35 -8.2; 37 -8.1; 40 -7.9; 42 -7.9; 45 -7.7; 49 -7.6; 52 -7.5; 56 -7.5; 59 -7.4; 64 -7.3; 68 -7.3; 73 -7.2; 78 -7.2; 83 -7.2; 89 -7.2; 95 -7.1; 102 -7.0; 109 -6.8; 117 -6.7; 125 -6.6; 134 -6.5; 143 -6.3; 153 -6.1; 164 -5.9; 175 -5.7; 188 -5.4; 201 -5.2; 215 -4.8; 230 -4.6; 246 -4.3; 263 -4.0; 282 -3.6; 301 -3.3; 323 -3.0; 345 -2.6; 369 -2.3; 395 -1.9; 423 -1.5; 452 -1.2; 484 -0.9; 518 -0.7; 554 -0.3; 593 0.2; 635 0.4; 679 0.4; 726 0.6; 777 0.8; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.1; 1336 -1.3; 1429 -1.3; 1529 -1.5; 1636 -2.0; 1751 -2.5; 1873 -2.7; 2004 -3.1; 2145 -3.5; 2295 -3.4; 2455 -2.9; 2627 -1.7; 2811 0.2; 3008 2.8; 3219 5.1; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.4; 6775 2.5; 7249 0.1; 7756 -0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999979483249dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.46 | -7.6 dB |
| Peaking | 119 Hz  | 0.4  | -5.7 dB |
| Peaking | 693 Hz  | 1.42 | 1.8 dB  |
| Peaking | 2270 Hz | 1.45 | -6.8 dB |
| Peaking | 3911 Hz | 1.11 | 8.7 dB  |
| Peaking | 1257 Hz | 6.92 | -0.6 dB |
| Peaking | 3297 Hz | 7.32 | 2.0 dB  |
| Peaking | 3996 Hz | 2.69 | -1.3 dB |
| Peaking | 6172 Hz | 2.89 | 5.6 dB  |
| Peaking | 7163 Hz | 1.97 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)
# Ultimate Ears UE600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.4; 22 3.3; 23 3.3; 25 3.2; 26 3.2; 28 3.1; 30 3.1; 32 3.1; 35 3.1; 37 3.0; 40 2.9; 42 2.9; 45 2.9; 49 2.9; 52 2.9; 56 2.8; 59 2.8; 64 2.7; 68 2.6; 73 2.4; 78 2.2; 83 2.0; 89 1.5; 95 1.0; 102 0.4; 109 0.1; 117 -0.4; 125 -1.0; 134 -1.5; 143 -1.9; 153 -2.1; 164 -2.3; 175 -2.4; 188 -2.4; 201 -2.5; 215 -2.4; 230 -2.3; 246 -2.3; 263 -2.3; 282 -2.0; 301 -2.0; 323 -1.9; 345 -1.7; 369 -1.7; 395 -1.5; 423 -1.2; 452 -1.2; 484 -1.1; 518 -1.0; 554 -0.6; 593 -0.1; 635 0.1; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.5; 1636 -0.4; 1751 -0.0; 1873 0.6; 2004 1.4; 2145 2.0; 2295 2.9; 2455 4.0; 2627 4.8; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 4.0; 4514 3.1; 4830 3.6; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -0.6; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.32 | 3.2 dB  |
| Peaking | 78 Hz   | 0.91 | 2.9 dB  |
| Peaking | 166 Hz  | 0.58 | -3.6 dB |
| Peaking | 3225 Hz | 1.81 | 6.5 dB  |
| Peaking | 5827 Hz | 3.48 | 5.7 dB  |
| Peaking | 762 Hz  | 2.92 | 0.8 dB  |
| Peaking | 1577 Hz | 2.45 | -1.2 dB |
| Peaking | 2480 Hz | 5.34 | 1.1 dB  |
| Peaking | 6647 Hz | 9.04 | 1.8 dB  |
| Peaking | 8225 Hz | 2.38 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE600/Ultimate%20Ears%20UE600.png)
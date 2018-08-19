# HiFiMAN HE-400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.8; 64 5.7; 68 5.6; 73 5.5; 78 5.3; 83 5.1; 89 5.0; 95 4.6; 102 4.4; 109 4.3; 117 4.2; 125 4.0; 134 3.8; 143 3.6; 153 3.3; 164 3.1; 175 3.2; 188 4.8; 201 5.0; 215 4.2; 230 3.8; 246 3.6; 263 3.4; 282 3.5; 301 3.5; 323 3.4; 345 3.1; 369 2.4; 395 2.6; 423 4.0; 452 6.2; 484 5.7; 518 5.4; 554 4.5; 593 3.8; 635 3.4; 679 2.9; 726 1.9; 777 1.4; 832 0.9; 890 1.4; 952 0.9; 1019 0.3; 1090 0.9; 1167 1.9; 1248 2.3; 1336 3.5; 1429 4.5; 1529 5.2; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -2.4; 9502 -2.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.340260157302463dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.34 | 5.5 dB  |
| Peaking | 76 Hz   | 0.69 | 2.8 dB  |
| Peaking | 224 Hz  | 1.42 | 2.9 dB  |
| Peaking | 490 Hz  | 2.98 | 5.0 dB  |
| Peaking | 2996 Hz | 0.63 | 6.9 dB  |
| Peaking | 1036 Hz | 3.72 | -2.1 dB |
| Peaking | 1642 Hz | 2.9  | 2.0 dB  |
| Peaking | 2974 Hz | 2.15 | -1.2 dB |
| Peaking | 5921 Hz | 2.5  | 3.3 dB  |
| Peaking | 8842 Hz | 2.57 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)
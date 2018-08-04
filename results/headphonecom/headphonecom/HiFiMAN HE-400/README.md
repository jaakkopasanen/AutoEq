# HiFiMAN HE-400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 1.5; 22 1.5; 23 1.5; 25 1.5; 26 1.5; 28 1.5; 30 1.5; 32 1.5; 35 1.5; 37 1.5; 40 1.5; 42 1.6; 45 1.7; 49 1.7; 52 1.7; 56 1.7; 59 1.7; 64 1.7; 68 1.7; 73 1.8; 78 1.8; 83 1.7; 89 1.8; 95 1.6; 102 1.5; 109 1.6; 117 1.6; 125 1.6; 134 1.6; 143 1.6; 153 1.4; 164 1.3; 175 1.5; 188 3.1; 201 3.4; 215 2.7; 230 2.3; 246 2.1; 263 1.9; 282 2.1; 301 2.1; 323 2.0; 345 1.6; 369 1.0; 395 1.3; 423 2.9; 452 5.3; 484 4.9; 518 4.8; 554 4.0; 593 3.4; 635 3.2; 679 2.8; 726 1.9; 777 1.3; 832 0.8; 890 1.3; 952 0.8; 1019 0.3; 1090 1.0; 1167 2.2; 1248 3.0; 1336 4.9; 1429 6.0; 1529 6.0; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.37 | 1.4 dB  |
| Peaking | 83 Hz   | 0.94 | 1.0 dB  |
| Peaking | 212 Hz  | 2.18 | 2.4 dB  |
| Peaking | 495 Hz  | 3.27 | 4.6 dB  |
| Peaking | 2921 Hz | 0.56 | 6.8 dB  |
| Peaking | 1048 Hz | 3.3  | -2.6 dB |
| Peaking | 1472 Hz | 2.69 | 2.5 dB  |
| Peaking | 2918 Hz | 2.01 | -1.1 dB |
| Peaking | 6261 Hz | 1.86 | 6.2 dB  |
| Peaking | 7494 Hz | 1.4  | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)
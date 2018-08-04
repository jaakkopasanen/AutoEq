# HiFiMAN HE-400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 2.0; 22 2.0; 23 2.0; 25 2.0; 26 2.0; 28 2.0; 30 2.0; 32 2.1; 35 2.1; 37 2.1; 40 2.1; 42 2.2; 45 2.3; 49 2.3; 52 2.3; 56 2.3; 59 2.3; 64 2.3; 68 2.3; 73 2.4; 78 2.5; 83 2.5; 89 2.6; 95 2.5; 102 2.5; 109 2.7; 117 2.8; 125 2.8; 134 2.9; 143 2.9; 153 2.7; 164 2.6; 175 2.8; 188 4.5; 201 4.7; 215 4.0; 230 3.7; 246 3.5; 263 3.3; 282 3.5; 301 3.5; 323 3.3; 345 3.1; 369 2.4; 395 2.5; 423 4.1; 452 5.9; 484 5.6; 518 5.3; 554 4.5; 593 3.9; 635 3.5; 679 2.8; 726 1.9; 777 1.4; 832 0.9; 890 1.3; 952 0.9; 1019 0.3; 1090 0.9; 1167 1.9; 1248 2.3; 1336 3.5; 1429 4.5; 1529 5.3; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.5; 9502 -2.1; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 25 Hz   | 0.57 | 1.7 dB  |
| Peaking | 89 Hz   | 0.65 | 1.8 dB  |
| Peaking | 222 Hz  | 1.37 | 3.1 dB  |
| Peaking | 491 Hz  | 2.92 | 4.9 dB  |
| Peaking | 2996 Hz | 0.63 | 6.9 dB  |
| Peaking | 1036 Hz | 3.65 | -2.1 dB |
| Peaking | 1641 Hz | 2.91 | 2.0 dB  |
| Peaking | 2977 Hz | 2.14 | -1.2 dB |
| Peaking | 5931 Hz | 2.46 | 3.3 dB  |
| Peaking | 8798 Hz | 2.6  | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)
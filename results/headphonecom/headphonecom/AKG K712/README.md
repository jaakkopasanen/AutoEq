# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.4; 23 -4.7; 25 -5.0; 26 -5.2; 28 -5.5; 30 -5.7; 32 -6.0; 35 -6.3; 37 -6.5; 40 -6.7; 42 -6.8; 45 -7.0; 49 -7.1; 52 -7.2; 56 -7.4; 59 -7.4; 64 -7.4; 68 -7.4; 73 -7.4; 78 -7.4; 83 -7.4; 89 -7.4; 95 -7.7; 102 -7.8; 109 -7.8; 117 -7.6; 125 -7.6; 134 -7.8; 143 -7.7; 153 -7.7; 164 -7.6; 175 -7.3; 188 -7.6; 201 -7.6; 215 -7.7; 230 -7.8; 246 -7.7; 263 -7.6; 282 -7.6; 301 -7.5; 323 -7.3; 345 -7.0; 369 -6.8; 395 -6.6; 423 -6.4; 452 -6.0; 484 -5.6; 518 -5.1; 554 -4.1; 593 -4.0; 635 -3.9; 679 -3.5; 726 -2.8; 777 -2.3; 832 -1.8; 890 -1.1; 952 -0.5; 1019 0.2; 1090 1.3; 1167 1.9; 1248 2.3; 1336 2.7; 1429 2.6; 1529 2.5; 1636 1.6; 1751 0.8; 1873 -0.8; 2004 -2.5; 2145 -2.8; 2295 -0.9; 2455 1.2; 2627 4.0; 2811 5.9; 3008 6.0; 3219 5.3; 3444 3.7; 3685 2.9; 3943 2.2; 4219 1.3; 4514 1.6; 4830 3.4; 5168 2.9; 5530 1.9; 5917 0.1; 6331 -1.9; 6775 -5.1; 7249 -6.2; 7756 -5.4; 8299 -3.8; 8880 -2.1; 9502 -0.6; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 0.27 | -7.5 dB |
| Peaking | 342 Hz   | 0.94 | -4.4 dB |
| Peaking | 3011 Hz  | 3.87 | 6.7 dB  |
| Peaking | 5172 Hz  | 2.88 | 3.9 dB  |
| Peaking | 7266 Hz  | 3.2  | -7.3 dB |
| Peaking | 704 Hz   | 1.64 | -1.4 dB |
| Peaking | 1369 Hz  | 1.5  | 3.9 dB  |
| Peaking | 2086 Hz  | 3.74 | -4.9 dB |
| Peaking | 2653 Hz  | 9.21 | 1.8 dB  |
| Peaking | 10336 Hz | 5.83 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/AKG%20K712/AKG%20K712.png)
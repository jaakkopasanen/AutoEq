# AKG K240 MK II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.6; 22 0.8; 23 0.4; 25 -0.3; 26 -0.6; 28 -1.2; 30 -1.7; 32 -2.2; 35 -2.9; 37 -3.3; 40 -3.8; 42 -4.0; 45 -4.3; 49 -4.6; 52 -5.0; 56 -5.2; 59 -5.0; 64 -4.9; 68 -5.5; 73 -6.6; 78 -7.2; 83 -7.7; 89 -8.0; 95 -8.4; 102 -8.7; 109 -8.7; 117 -8.9; 125 -8.9; 134 -8.9; 143 -8.8; 153 -8.4; 164 -8.0; 175 -7.9; 188 -7.5; 201 -7.3; 215 -7.0; 230 -6.6; 246 -6.2; 263 -6.0; 282 -6.0; 301 -5.9; 323 -5.8; 345 -5.4; 369 -5.2; 395 -4.8; 423 -4.6; 452 -4.4; 484 -4.2; 518 -1.6; 554 -0.7; 593 -1.4; 635 -1.4; 679 -1.1; 726 -0.9; 777 -0.8; 832 -0.6; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.8; 1248 1.2; 1336 1.5; 1429 1.7; 1529 1.7; 1636 1.6; 1751 0.7; 1873 0.0; 2004 0.0; 2145 -0.9; 2295 -0.7; 2455 -0.4; 2627 0.9; 2811 1.6; 3008 2.3; 3219 3.4; 3444 3.8; 3685 3.7; 3943 3.1; 4219 3.3; 4514 3.8; 4830 4.8; 5168 6.0; 5530 6.0; 5917 4.7; 6331 2.1; 6775 -0.4; 7249 -1.9; 7756 -4.4; 8299 -6.9; 8880 -8.0; 9502 -6.3; 10167 -2.3; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MK II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 120 Hz   | 0.56 | -9.0 dB |
| Peaking | 351 Hz   | 1.79 | -2.7 dB |
| Peaking | 3470 Hz  | 3.01 | 3.3 dB  |
| Peaking | 5383 Hz  | 2.84 | 6.7 dB  |
| Peaking | 8646 Hz  | 3.38 | -9.2 dB |
| Peaking | 14 Hz    | 0.92 | 3.5 dB  |
| Peaking | 38 Hz    | 2.04 | -1.5 dB |
| Peaking | 1434 Hz  | 2    | 2.1 dB  |
| Peaking | 2213 Hz  | 4.08 | -1.8 dB |
| Peaking | 11002 Hz | 6.84 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/AKG%20K240%20MK%20II/AKG%20K240%20MK%20II.png)
# Philips Fidelio M1 Mk1 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.6; 22 0.4; 23 0.3; 25 0.1; 26 0.1; 28 0.0; 30 -0.0; 32 -0.0; 35 -0.0; 37 -0.0; 40 -0.0; 42 0.0; 45 0.1; 49 0.2; 52 0.3; 56 0.4; 59 0.5; 64 0.7; 68 0.8; 73 0.9; 78 0.8; 83 0.7; 89 0.5; 95 0.4; 102 0.4; 109 0.4; 117 0.4; 125 0.4; 134 0.4; 143 0.3; 153 0.5; 164 1.0; 175 1.5; 188 1.7; 201 1.8; 215 2.1; 230 2.2; 246 2.3; 263 2.4; 282 2.7; 301 2.8; 323 2.7; 345 2.3; 369 1.9; 395 1.6; 423 1.0; 452 0.5; 484 -0.0; 518 -0.3; 554 -0.2; 593 -0.2; 635 -0.4; 679 -0.5; 726 -0.3; 777 -0.1; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.5; 1429 0.5; 1529 0.4; 1636 0.4; 1751 0.7; 1873 1.1; 2004 1.7; 2145 2.4; 2295 3.1; 2455 4.0; 2627 4.8; 2811 5.3; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 Mk1 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 1.75 | 0.2 dB  |
| Peaking | 72 Hz   | 2.46 | 0.8 dB  |
| Peaking | 272 Hz  | 1.62 | 2.9 dB  |
| Peaking | 5527 Hz | 2.5  | 5.1 dB  |
| Peaking | 3317 Hz | 1.51 | 5.9 dB  |
| Peaking | 18 Hz   | 1.88 | 0.8 dB  |
| Peaking | 661 Hz  | 1.35 | -1.2 dB |
| Peaking | 1660 Hz | 3.45 | -1.0 dB |
| Peaking | 1132 Hz | 0.2  | 0.4 dB  |
| Peaking | 8420 Hz | 3.32 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1%20Mk1%202012/Philips%20Fidelio%20M1%20Mk1%202012.png)
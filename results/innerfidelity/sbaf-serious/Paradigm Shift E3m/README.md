# Paradigm Shift E3m

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.5; 22 -7.5; 23 -7.5; 25 -7.5; 26 -7.5; 28 -7.6; 30 -7.6; 32 -7.6; 35 -7.6; 37 -7.6; 40 -7.6; 42 -7.7; 45 -7.7; 49 -7.8; 52 -7.8; 56 -7.8; 59 -7.8; 64 -7.8; 68 -7.9; 73 -8.0; 78 -8.2; 83 -8.4; 89 -8.8; 95 -9.2; 102 -9.7; 109 -10.2; 117 -10.7; 125 -11.3; 134 -11.7; 143 -12.0; 153 -12.1; 164 -12.2; 175 -12.1; 188 -12.0; 201 -12.0; 215 -11.8; 230 -11.5; 246 -11.3; 263 -11.1; 282 -10.7; 301 -10.4; 323 -10.0; 345 -9.6; 369 -9.1; 395 -8.7; 423 -8.0; 452 -7.5; 484 -6.9; 518 -6.3; 554 -5.5; 593 -4.6; 635 -3.9; 679 -3.3; 726 -2.5; 777 -1.7; 832 -1.2; 890 -0.7; 952 -0.3; 1019 0.2; 1090 0.6; 1167 0.7; 1248 0.8; 1336 0.6; 1429 0.0; 1529 -0.5; 1636 0.5; 1751 1.5; 1873 1.1; 2004 1.8; 2145 2.9; 2295 4.3; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.8; 4830 3.8; 5168 3.4; 5530 2.5; 5917 1.6; 6331 1.7; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E3m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 6 Hz    | 0.53 | -7.0 dB |
| Peaking | 42 Hz   | 0.13 | -6.0 dB |
| Peaking | 227 Hz  | 0.57 | -8.0 dB |
| Peaking | 2495 Hz | 6.2  | 2.1 dB  |
| Peaking | 3406 Hz | 1.07 | 6.4 dB  |
| Peaking | 136 Hz  | 5.46 | -0.8 dB |
| Peaking | 486 Hz  | 2.42 | -1.3 dB |
| Peaking | 1216 Hz | 1.17 | 3.1 dB  |
| Peaking | 1520 Hz | 1.78 | -2.9 dB |
| Peaking | 8998 Hz | 2.64 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E3m/Paradigm%20Shift%20E3m.png)
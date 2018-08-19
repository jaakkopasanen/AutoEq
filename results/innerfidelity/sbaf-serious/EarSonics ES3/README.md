# EarSonics ES3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.8; 22 -3.0; 23 -3.0; 25 -3.2; 26 -3.2; 28 -3.3; 30 -3.4; 32 -3.4; 35 -3.5; 37 -3.5; 40 -3.5; 42 -3.5; 45 -3.5; 49 -3.5; 52 -3.5; 56 -3.5; 59 -3.5; 64 -3.4; 68 -3.4; 73 -3.3; 78 -3.3; 83 -3.2; 89 -3.1; 95 -2.9; 102 -2.6; 109 -2.3; 117 -1.9; 125 -1.5; 134 -1.0; 143 -0.6; 153 -0.0; 164 0.5; 175 1.1; 188 1.6; 201 2.0; 215 2.5; 230 2.8; 246 2.9; 263 2.9; 282 3.1; 301 2.9; 323 2.7; 345 2.5; 369 2.4; 395 2.1; 423 2.0; 452 1.9; 484 1.7; 518 1.6; 554 1.7; 593 1.7; 635 1.7; 679 1.5; 726 1.4; 777 1.4; 832 1.1; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.3; 1429 -3.1; 1529 -3.8; 1636 -4.3; 1751 -4.3; 1873 -3.6; 2004 -1.9; 2145 0.3; 2295 2.1; 2455 3.6; 2627 5.0; 2811 5.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.8; 5530 6.0; 5917 5.9; 6331 4.0; 6775 0.3; 7249 -0.2; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999814357dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `EarSonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.32 | -3.6 dB |
| Peaking | 116 Hz  | 0.78 | -3.5 dB |
| Peaking | 203 Hz  | 0.5  | 5.1 dB  |
| Peaking | 1695 Hz | 1.91 | -7.6 dB |
| Peaking | 3428 Hz | 0.88 | 7.6 dB  |
| Peaking | 1192 Hz | 5.7  | -0.4 dB |
| Peaking | 2690 Hz | 4.98 | 1.1 dB  |
| Peaking | 3534 Hz | 3.55 | -1.1 dB |
| Peaking | 5972 Hz | 2.8  | 6.5 dB  |
| Peaking | 6738 Hz | 1.93 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/EarSonics%20ES3/EarSonics%20ES3.png)
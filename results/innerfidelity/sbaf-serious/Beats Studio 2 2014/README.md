# Beats Studio 2 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 5.2; 23 4.7; 25 3.7; 26 3.2; 28 2.2; 30 1.5; 32 1.0; 35 0.6; 37 0.5; 40 0.5; 42 0.5; 45 0.5; 49 0.5; 52 0.5; 56 0.6; 59 0.6; 64 0.7; 68 0.6; 73 0.7; 78 0.6; 83 0.5; 89 0.3; 95 0.1; 102 -0.1; 109 -0.0; 117 -0.0; 125 -0.1; 134 -0.0; 143 0.1; 153 0.2; 164 0.5; 175 0.8; 188 1.1; 201 1.4; 215 1.8; 230 2.3; 246 2.7; 263 3.2; 282 3.9; 301 4.6; 323 5.5; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.5; 635 3.3; 679 1.0; 726 -0.5; 777 -1.2; 832 -1.5; 890 -0.9; 952 -0.2; 1019 -0.1; 1090 0.2; 1167 0.1; 1248 -0.3; 1336 -0.0; 1429 0.6; 1529 1.0; 1636 1.1; 1751 2.2; 1873 3.0; 2004 3.8; 2145 4.4; 2295 4.8; 2455 5.2; 2627 5.2; 2811 4.5; 3008 3.3; 3219 1.2; 3444 0.9; 3685 1.8; 3943 3.4; 4219 4.7; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -1.5; 10167 -1.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.14 | 5.9 dB  |
| Peaking | 468 Hz  | 0.98 | 7.6 dB  |
| Peaking | 802 Hz  | 2.02 | -4.9 dB |
| Peaking | 2386 Hz | 2.59 | 5.0 dB  |
| Peaking | 5270 Hz | 2.22 | 6.7 dB  |
| Peaking | 321 Hz  | 6.24 | 1.1 dB  |
| Peaking | 140 Hz  | 2.01 | -0.9 dB |
| Peaking | 3402 Hz | 8.17 | -2.3 dB |
| Peaking | 6751 Hz | 0.66 | 0.9 dB  |
| Peaking | 9300 Hz | 2.08 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%202014/Beats%20Studio%202%202014.png)
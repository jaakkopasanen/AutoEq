# Grado RS1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 4.8; 52 4.0; 56 3.1; 59 2.4; 64 1.5; 68 0.7; 73 -0.1; 78 -0.9; 83 -1.5; 89 -2.2; 95 -2.7; 102 -3.1; 109 -3.2; 117 -3.3; 125 -3.4; 134 -3.3; 143 -3.2; 153 -3.1; 164 -2.9; 175 -2.7; 188 -2.5; 201 -2.3; 215 -1.9; 230 -1.5; 246 -1.7; 263 -1.8; 282 -1.5; 301 -1.3; 323 -1.1; 345 -0.7; 369 -0.7; 395 -0.9; 423 -0.6; 452 -0.5; 484 -0.5; 518 -0.4; 554 -0.2; 593 0.0; 635 0.2; 679 0.1; 726 0.0; 777 0.4; 832 0.3; 890 0.2; 952 0.0; 1019 -0.0; 1090 0.0; 1167 -0.3; 1248 -0.8; 1336 -1.5; 1429 -2.7; 1529 -3.8; 1636 -4.7; 1751 -6.6; 1873 -10.3; 2004 -8.7; 2145 -7.7; 2295 -6.5; 2455 -5.5; 2627 -4.7; 2811 -3.0; 3008 -1.7; 3219 -0.8; 3444 0.6; 3685 0.9; 3943 -2.0; 4219 -7.7; 4514 -10.6; 4830 -7.5; 5168 -5.5; 5530 -5.1; 5917 -5.6; 6331 -8.1; 6775 -10.5; 7249 -9.6; 7756 -7.9; 8299 -8.0; 8880 -9.5; 9502 -8.4; 10167 -2.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -4.2; 17469 -7.5; 18692 -5.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.51 | 7.4 dB  |
| Peaking | 1960 Hz  | 2.95 | -9.5 dB |
| Peaking | 7010 Hz  | 1.29 | -9.7 dB |
| Peaking | 17782 Hz | 3.36 | -8.4 dB |
| Peaking | 24000 Hz | 2.2  | -7.7 dB |
| Peaking | 50 Hz    | 2.02 | 3.6 dB  |
| Peaking | 123 Hz   | 0.81 | -3.9 dB |
| Peaking | 3641 Hz  | 5.23 | 4.9 dB  |
| Peaking | 4434 Hz  | 7.9  | -8.2 dB |
| Peaking | 11969 Hz | 3.4  | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1/Grado%20RS1.png)
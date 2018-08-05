# Ivery IS-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.8; 22 -10.9; 23 -10.9; 25 -11.0; 26 -11.0; 28 -11.0; 30 -11.0; 32 -11.0; 35 -11.0; 37 -11.0; 40 -11.0; 42 -11.0; 45 -11.0; 49 -11.0; 52 -10.9; 56 -10.9; 59 -10.9; 64 -10.9; 68 -10.8; 73 -10.9; 78 -11.0; 83 -11.1; 89 -11.3; 95 -11.6; 102 -12.1; 109 -12.4; 117 -12.7; 125 -13.1; 134 -13.3; 143 -13.4; 153 -13.4; 164 -13.4; 175 -13.1; 188 -12.9; 201 -12.5; 215 -12.1; 230 -11.7; 246 -11.4; 263 -10.9; 282 -10.4; 301 -10.0; 323 -9.5; 345 -8.9; 369 -8.4; 395 -7.9; 423 -7.1; 452 -6.6; 484 -6.1; 518 -5.5; 554 -4.8; 593 -4.0; 635 -3.5; 679 -2.9; 726 -2.1; 777 -1.2; 832 -1.1; 890 -0.9; 952 -0.6; 1019 0.5; 1090 1.4; 1167 1.4; 1248 1.5; 1336 1.6; 1429 1.8; 1529 2.2; 1636 2.6; 1751 3.3; 1873 4.1; 2004 5.3; 2145 6.0; 2295 6.0; 2455 6.0; 2627 5.8; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.5; 4219 3.5; 4514 2.1; 4830 1.9; 5168 2.2; 5530 2.3; 5917 1.7; 6331 -0.6; 6775 -4.2; 7249 -8.0; 7756 -8.3; 8299 -5.6; 8880 -1.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.0; 13327 -2.1; 14260 -0.6; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ivery IS-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.47 | -9.3 dB  |
| Peaking | 172 Hz   | 0.39 | -12.4 dB |
| Peaking | 2784 Hz  | 0.78 | 6.8 dB   |
| Peaking | 934 Hz   | 1.32 | 1.4 dB   |
| Peaking | 7545 Hz  | 4.17 | -10.9 dB |
| Peaking | 3850 Hz  | 7.7  | 1.3 dB   |
| Peaking | 4549 Hz  | 8.15 | -1.7 dB  |
| Peaking | 9488 Hz  | 8.48 | 1.1 dB   |
| Peaking | 12098 Hz | 2.64 | 0.7 dB   |
| Peaking | 13207 Hz | 4.78 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ivery%20IS-1/Ivery%20IS-1.png)
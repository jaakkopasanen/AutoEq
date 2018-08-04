# AKG K1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 4.9; 68 3.8; 73 2.6; 78 1.6; 83 0.7; 89 -0.1; 95 -0.7; 102 -1.1; 109 -1.3; 117 -1.6; 125 -1.9; 134 -1.6; 143 -1.4; 153 -1.4; 164 -1.1; 175 -0.9; 188 -0.8; 201 -0.7; 215 -0.5; 230 -0.3; 246 -0.2; 263 -0.0; 282 0.2; 301 0.2; 323 0.3; 345 0.4; 369 0.5; 395 0.5; 423 0.7; 452 0.8; 484 0.7; 518 0.6; 554 0.8; 593 0.9; 635 0.9; 679 0.8; 726 0.7; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.9; 1248 -1.9; 1336 -3.1; 1429 -4.2; 1529 -4.6; 1636 -4.6; 1751 -5.4; 1873 -7.1; 2004 -6.9; 2145 -5.9; 2295 -5.1; 2455 -2.9; 2627 -0.8; 2811 0.8; 3008 2.6; 3219 2.7; 3444 2.1; 3685 0.5; 3943 -1.7; 4219 -2.8; 4514 -2.6; 4830 -2.8; 5168 -2.8; 5530 -3.3; 5917 -5.0; 6331 -5.3; 6775 -4.2; 7249 -4.0; 7756 -4.2; 8299 -4.6; 8880 -4.6; 9502 -3.5; 10167 -1.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.6; 18692 -1.6; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 77 Hz    | 0.25 | 14.5 dB  |
| Peaking | 117 Hz   | 0.5  | -15.3 dB |
| Peaking | 1948 Hz  | 1.78 | -7.5 dB  |
| Peaking | 3110 Hz  | 3.26 | 6.0 dB   |
| Peaking | 6684 Hz  | 1.13 | -4.9 dB  |
| Peaking | 90 Hz    | 5.7  | -0.7 dB  |
| Peaking | 939 Hz   | 1.91 | 0.8 dB   |
| Peaking | 1403 Hz  | 7.11 | -1.6 dB  |
| Peaking | 9142 Hz  | 4.12 | -3.0 dB  |
| Peaking | 10603 Hz | 1.69 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K1000/AKG%20K1000.png)
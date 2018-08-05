# Read Heath Acoustics MA750

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -5.8; 22 -5.8; 23 -5.8; 25 -5.8; 26 -5.8; 28 -5.8; 30 -5.7; 32 -5.7; 35 -5.7; 37 -5.6; 40 -5.5; 42 -5.4; 45 -5.3; 49 -5.2; 52 -5.1; 56 -4.9; 59 -4.9; 64 -4.7; 68 -4.7; 73 -4.6; 78 -4.6; 83 -4.7; 89 -4.9; 95 -5.2; 102 -5.5; 109 -5.8; 117 -6.2; 125 -6.6; 134 -6.9; 143 -7.1; 153 -7.1; 164 -7.1; 175 -7.0; 188 -6.8; 201 -6.7; 215 -6.4; 230 -6.2; 246 -6.0; 263 -5.8; 282 -5.5; 301 -5.2; 323 -4.9; 345 -4.6; 369 -4.3; 395 -4.0; 423 -3.5; 452 -3.2; 484 -3.0; 518 -2.7; 554 -2.2; 593 -1.6; 635 -1.3; 679 -1.1; 726 -0.7; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.3; 1248 0.3; 1336 0.3; 1429 0.1; 1529 -0.1; 1636 -0.1; 1751 0.0; 1873 0.3; 2004 0.6; 2145 0.8; 2295 1.1; 2455 1.4; 2627 1.3; 2811 1.0; 3008 0.7; 3219 0.0; 3444 -0.8; 3685 -1.8; 3943 -3.1; 4219 -5.4; 4514 -7.7; 4830 -7.8; 5168 -5.3; 5530 -1.3; 5917 2.1; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -3.2; 15258 -4.4; 16326 -1.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Acoustics MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.47 | -5.6 dB |
| Peaking | 185 Hz   | 0.61 | -6.7 dB |
| Peaking | 4708 Hz  | 4.19 | -9.4 dB |
| Peaking | 6395 Hz  | 4.74 | 6.1 dB  |
| Peaking | 32875 Hz | 4.68 | -5.1 dB |
| Peaking | 219 Hz   | 2.12 | 0.9 dB  |
| Peaking | 531 Hz   | 0.52 | -1.3 dB |
| Peaking | 844 Hz   | 0.97 | 1.8 dB  |
| Peaking | 2598 Hz  | 2.29 | 1.8 dB  |
| Peaking | 4074 Hz  | 4.84 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Acoustics%20MA750/Read%20Heath%20Acoustics%20MA750.png)
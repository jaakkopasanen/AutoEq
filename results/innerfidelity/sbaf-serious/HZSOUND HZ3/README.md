# HZSOUND HZ3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 0.9; 22 0.6; 23 0.5; 25 0.2; 26 0.1; 28 -0.1; 30 -0.2; 32 -0.3; 35 -0.4; 37 -0.5; 40 -0.6; 42 -0.7; 45 -0.7; 49 -0.8; 52 -0.9; 56 -0.9; 59 -1.0; 64 -1.1; 68 -1.1; 73 -1.3; 78 -1.5; 83 -1.7; 89 -2.1; 95 -2.5; 102 -3.0; 109 -3.4; 117 -4.0; 125 -4.5; 134 -5.0; 143 -5.2; 153 -5.4; 164 -5.5; 175 -5.5; 188 -5.4; 201 -5.4; 215 -5.2; 230 -5.1; 246 -4.9; 263 -4.8; 282 -4.6; 301 -4.4; 323 -4.2; 345 -4.0; 369 -3.7; 395 -3.5; 423 -3.2; 452 -2.9; 484 -2.7; 518 -2.5; 554 -2.2; 593 -1.7; 635 -1.5; 679 -1.3; 726 -1.1; 777 -0.8; 832 -0.8; 890 -0.8; 952 0.5; 1019 -0.2; 1090 -0.6; 1167 -0.8; 1248 -0.4; 1336 0.5; 1429 -0.3; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -0.7; 2004 -0.5; 2145 -0.4; 2295 -0.2; 2455 0.1; 2627 0.5; 2811 0.8; 3008 1.4; 3219 2.0; 3444 2.3; 3685 1.3; 3943 1.2; 4219 1.5; 4514 -2.4; 4830 -5.2; 5168 -7.9; 5530 -8.1; 5917 -4.0; 6331 -0.6; 6775 1.8; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -1.2; 9502 -1.4; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.9dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 147 Hz  |  1.16 | -3.4 dB  |
| Peaking | 278 Hz  |  0.7  | -3.7 dB  |
| Peaking | 3977 Hz |  1.97 | 4.6 dB   |
| Peaking | 5298 Hz |  2.71 | -11.2 dB |
| Peaking | 6693 Hz |  4.3  | 5.0 dB   |
| Peaking | 17 Hz   |  1.82 | 1.0 dB   |
| Peaking | 1452 Hz |  1.44 | 1.0 dB   |
| Peaking | 1709 Hz |  2.02 | -1.6 dB  |
| Peaking | 3213 Hz |  8.52 | 0.9 dB   |
| Peaking | 9222 Hz | 10.36 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ3/HZSOUND%20HZ3.png)
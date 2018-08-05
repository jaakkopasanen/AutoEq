# RHA T10i Treble Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.6; 22 -9.6; 23 -9.6; 25 -9.7; 26 -9.8; 28 -10.0; 30 -10.2; 32 -10.3; 35 -10.4; 37 -10.3; 40 -10.3; 42 -10.3; 45 -10.3; 49 -10.2; 52 -10.2; 56 -10.1; 59 -10.0; 64 -9.9; 68 -9.8; 73 -9.7; 78 -9.7; 83 -9.7; 89 -9.8; 95 -10.1; 102 -10.3; 109 -10.5; 117 -10.7; 125 -11.0; 134 -11.2; 143 -11.2; 153 -11.0; 164 -10.8; 175 -10.5; 188 -10.1; 201 -9.8; 215 -9.3; 230 -8.8; 246 -8.4; 263 -8.0; 282 -7.4; 301 -6.9; 323 -6.4; 345 -5.9; 369 -5.4; 395 -4.9; 423 -4.3; 452 -3.8; 484 -3.5; 518 -3.0; 554 -2.5; 593 -1.8; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.0; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.5; 1636 -3.2; 1751 -3.8; 1873 -4.3; 2004 -5.0; 2145 -5.9; 2295 -6.8; 2455 -7.0; 2627 -6.4; 2811 -5.3; 3008 -3.7; 3219 -2.4; 3444 -1.7; 3685 -1.6; 3943 -0.2; 4219 1.1; 4514 3.7; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -2.3; 8299 -9.6; 8880 -13.0; 9502 -13.2; 10167 -10.5; 10879 -4.4; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 6 Hz    | 1.51 | -9.0 dB  |
| Peaking | 30 Hz   | 0.25 | -9.4 dB  |
| Peaking | 184 Hz  | 0.65 | -7.5 dB  |
| Peaking | 2339 Hz | 2.8  | -7.6 dB  |
| Peaking | 9340 Hz | 5.32 | -15.6 dB |
| Peaking | 924 Hz  | 2.7  | 1.4 dB   |
| Peaking | 1672 Hz | 4.13 | -1.8 dB  |
| Peaking | 3522 Hz | 1.76 | -3.6 dB  |
| Peaking | 5545 Hz | 1.4  | 8.7 dB   |
| Peaking | 8423 Hz | 5.47 | -7.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Treble%20Filter/RHA%20T10i%20Treble%20Filter.png)
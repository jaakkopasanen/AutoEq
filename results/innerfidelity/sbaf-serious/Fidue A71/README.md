# Fidue A71

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.9; 23 -2.1; 25 -2.4; 26 -2.5; 28 -2.8; 30 -2.9; 32 -3.1; 35 -3.3; 37 -3.4; 40 -3.5; 42 -3.6; 45 -3.7; 49 -3.8; 52 -3.8; 56 -3.9; 59 -4.0; 64 -4.0; 68 -4.1; 73 -4.2; 78 -4.3; 83 -4.5; 89 -4.8; 95 -5.3; 102 -5.7; 109 -6.1; 117 -6.5; 125 -7.0; 134 -7.3; 143 -7.5; 153 -7.6; 164 -7.6; 175 -7.4; 188 -7.2; 201 -7.0; 215 -6.7; 230 -6.4; 246 -6.1; 263 -5.8; 282 -5.4; 301 -5.0; 323 -4.6; 345 -4.2; 369 -3.8; 395 -3.6; 423 -3.1; 452 -2.0; 484 -1.6; 518 -1.4; 554 -0.9; 593 -0.3; 635 0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.6; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.4; 1336 -2.2; 1429 -3.2; 1529 -4.1; 1636 -4.9; 1751 -5.2; 1873 -4.9; 2004 -4.0; 2145 -2.8; 2295 -1.6; 2455 -0.1; 2627 1.8; 2811 3.9; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 2.5; 6775 -1.3; 7249 -2.0; 7756 -1.2; 8299 -0.8; 8880 -1.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.23 | -2.6 dB  |
| Peaking | 187 Hz   | 0.66 | -5.9 dB  |
| Peaking | 1875 Hz  | 1.18 | -14.7 dB |
| Peaking | 3166 Hz  | 0.39 | 11.9 dB  |
| Peaking | 7992 Hz  | 1.34 | -7.2 dB  |
| Peaking | 4101 Hz  | 5.28 | -0.8 dB  |
| Peaking | 5980 Hz  | 4.53 | 3.8 dB   |
| Peaking | 6809 Hz  | 4.29 | -4.6 dB  |
| Peaking | 8107 Hz  | 2.27 | 1.8 dB   |
| Peaking | 13858 Hz | 0.94 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A71/Fidue%20A71.png)
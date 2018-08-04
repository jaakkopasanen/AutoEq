# Pioneer Monitor 10 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.3; 22 -4.4; 23 -4.4; 25 -4.4; 26 -4.5; 28 -4.5; 30 -4.5; 32 -4.5; 35 -4.5; 37 -4.5; 40 -4.5; 42 -4.5; 45 -4.5; 49 -4.6; 52 -4.6; 56 -4.5; 59 -4.4; 64 -4.4; 68 -4.3; 73 -4.2; 78 -4.1; 83 -3.9; 89 -3.8; 95 -3.9; 102 -4.3; 109 -4.7; 117 -4.7; 125 -4.1; 134 -3.4; 143 -3.3; 153 -6.2; 164 -5.8; 175 -3.5; 188 -4.7; 201 -5.6; 215 -6.1; 230 -6.2; 246 -6.4; 263 -6.6; 282 -6.2; 301 -5.7; 323 -5.8; 345 -5.0; 369 -4.3; 395 -3.4; 423 -2.3; 452 -1.4; 484 -0.6; 518 0.4; 554 1.6; 593 2.9; 635 3.7; 679 4.0; 726 4.1; 777 3.3; 832 2.1; 890 1.1; 952 0.1; 1019 0.2; 1090 0.4; 1167 -0.3; 1248 -1.1; 1336 -2.9; 1429 -5.3; 1529 -7.5; 1636 -8.9; 1751 -9.0; 1873 -6.9; 2004 -4.3; 2145 -2.0; 2295 0.1; 2455 0.3; 2627 -0.3; 2811 0.5; 3008 2.6; 3219 3.6; 3444 3.2; 3685 3.8; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.36 | -4.7 dB  |
| Peaking | 175 Hz  | 1.42 | -3.1 dB  |
| Peaking | 284 Hz  | 2.4  | -5.3 dB  |
| Peaking | 1698 Hz | 3.73 | -10.8 dB |
| Peaking | 4649 Hz | 1.31 | 6.6 dB   |
| Peaking | 383 Hz  | 3.43 | -1.8 dB  |
| Peaking | 640 Hz  | 2.8  | 4.0 dB   |
| Peaking | 760 Hz  | 4.4  | 2.3 dB   |
| Peaking | 6381 Hz | 3.92 | 4.6 dB   |
| Peaking | 7165 Hz | 1.49 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)
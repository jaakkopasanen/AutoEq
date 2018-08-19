# Shure SE112

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.2; 23 -3.3; 25 -3.3; 26 -3.4; 28 -3.4; 30 -3.5; 32 -3.6; 35 -3.7; 37 -3.7; 40 -3.8; 42 -3.9; 45 -4.0; 49 -4.1; 52 -4.2; 56 -4.4; 59 -4.5; 64 -4.7; 68 -4.9; 73 -5.1; 78 -5.3; 83 -5.5; 89 -5.7; 95 -6.0; 102 -6.2; 109 -6.4; 117 -6.5; 125 -6.7; 134 -6.8; 143 -6.8; 153 -6.9; 164 -6.8; 175 -6.8; 188 -6.7; 201 -6.6; 215 -6.4; 230 -6.2; 246 -6.0; 263 -5.8; 282 -5.5; 301 -5.2; 323 -4.8; 345 -4.4; 369 -4.0; 395 -3.7; 423 -3.3; 452 -3.0; 484 -2.6; 518 -2.2; 554 -1.8; 593 -1.4; 635 -1.0; 679 -0.7; 726 -0.3; 777 -0.0; 832 0.2; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.4; 1248 -0.5; 1336 -0.6; 1429 -0.5; 1529 -0.4; 1636 -0.4; 1751 -0.4; 1873 -0.4; 2004 -0.2; 2145 0.2; 2295 0.9; 2455 2.0; 2627 3.2; 2811 4.3; 3008 5.0; 3219 5.3; 3444 5.1; 3685 4.1; 3943 2.3; 4219 -0.8; 4514 -3.6; 4830 -1.9; 5168 3.0; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.2; 14260 -4.2; 15258 -4.2; 16326 -1.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.084225018767812dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.25 | -3.1 dB |
| Peaking | 146 Hz   | 0.71 | -4.4 dB |
| Peaking | 292 Hz   | 1.08 | -2.7 dB |
| Peaking | 3127 Hz  | 3.66 | 6.0 dB  |
| Peaking | 6024 Hz  | 5.06 | 6.8 dB  |
| Peaking | 831 Hz   | 4.43 | 1.0 dB  |
| Peaking | 3769 Hz  | 5.85 | 2.6 dB  |
| Peaking | 4602 Hz  | 5.15 | -6.0 dB |
| Peaking | 5366 Hz  | 8.17 | 4.0 dB  |
| Peaking | 14817 Hz | 3.95 | -5.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE112/Shure%20SE112.png)
# Brainwavz S5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 10 -84; 20 -9.0; 22 -9.1; 23 -9.2; 25 -9.3; 26 -9.3; 28 -9.4; 30 -9.4; 32 -9.4; 35 -9.4; 37 -9.4; 40 -9.4; 42 -9.3; 45 -9.3; 49 -9.2; 52 -9.2; 56 -9.1; 59 -9.0; 64 -9.0; 68 -8.9; 73 -8.9; 78 -8.9; 83 -9.0; 89 -9.1; 95 -9.4; 102 -9.7; 109 -9.9; 117 -10.2; 125 -10.5; 134 -10.7; 143 -10.7; 153 -10.6; 164 -10.5; 175 -10.1; 188 -9.8; 201 -9.5; 215 -9.0; 230 -8.6; 246 -8.1; 263 -7.7; 282 -7.2; 301 -6.8; 323 -6.3; 345 -5.7; 369 -5.3; 395 -4.8; 423 -4.2; 452 -3.8; 484 -3.4; 518 -2.9; 554 -2.3; 593 -1.6; 635 -1.2; 679 -0.9; 726 -0.5; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.2; 1167 0.3; 1248 0.4; 1336 -0.0; 1429 -0.2; 1529 -0.1; 1636 -0.1; 1751 0.0; 1873 0.5; 2004 0.8; 2145 1.2; 2295 1.5; 2455 2.1; 2627 2.1; 2811 1.8; 3008 1.5; 3219 0.9; 3444 -0.4; 3685 -2.3; 3943 -4.0; 4219 -6.3; 4514 -7.9; 4830 -9.2; 5168 -10.9; 5530 -11.9; 5917 -9.5; 6331 -6.8; 6775 -4.4; 7249 -3.4; 7756 -4.4; 8299 -6.9; 8880 -9.0; 9502 -8.0; 10167 -3.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -0.5; 14260 -4.6; 15258 -6.1; 16326 -4.3; 17469 -2.6; 18692 -2.5; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.8dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.15 | -9.0 dB  |
| Peaking | 188 Hz   | 0.72 | -6.9 dB  |
| Peaking | 5449 Hz  | 2.26 | -11.7 dB |
| Peaking | 32530 Hz | 2.98 | -4.6 dB  |
| Peaking | 23347 Hz | 0.08 | -3.0 dB  |
| Peaking | 3005 Hz  | 1.24 | 3.8 dB   |
| Peaking | 4228 Hz  | 2.86 | -3.5 dB  |
| Peaking | 7149 Hz  | 3.42 | 3.0 dB   |
| Peaking | 9127 Hz  | 2.82 | -9.9 dB  |
| Peaking | 11051 Hz | 2.29 | 4.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S5/Brainwavz%20S5.png)
# Grado SR125i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.6; 35 4.9; 37 4.3; 40 3.6; 42 3.2; 45 2.5; 49 1.8; 52 1.4; 56 1.0; 59 0.7; 64 0.2; 68 -0.1; 73 -0.4; 78 -0.6; 83 -0.9; 89 -1.2; 95 -1.5; 102 -1.7; 109 -1.9; 117 -2.1; 125 -2.4; 134 -2.5; 143 -2.6; 153 -2.5; 164 -2.4; 175 -2.3; 188 -2.1; 201 -1.9; 215 -1.6; 230 -1.3; 246 -1.1; 263 -0.9; 282 -0.5; 301 -0.2; 323 -0.6; 345 -0.8; 369 -0.7; 395 -0.8; 423 -0.6; 452 -0.4; 484 -0.3; 518 -0.3; 554 -0.1; 593 0.3; 635 0.3; 679 0.2; 726 0.2; 777 0.4; 832 0.3; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.0; 1167 -0.1; 1248 -0.5; 1336 -1.1; 1429 -1.9; 1529 -2.9; 1636 -3.4; 1751 -4.0; 1873 -6.8; 2004 -9.9; 2145 -9.8; 2295 -8.0; 2455 -5.9; 2627 -4.5; 2811 -2.7; 3008 -1.8; 3219 -0.4; 3444 -1.1; 3685 -1.8; 3943 -1.6; 4219 -0.2; 4514 0.1; 4830 -0.1; 5168 -0.7; 5530 -0.6; 5917 1.7; 6331 1.5; 6775 -0.9; 7249 -3.0; 7756 -3.7; 8299 -4.1; 8880 -4.3; 9502 -3.0; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.96 | 6.6 dB   |
| Peaking | 133 Hz   | 0.93 | -2.9 dB  |
| Peaking | 2109 Hz  | 3.09 | -10.5 dB |
| Peaking | 8456 Hz  | 3.98 | -4.9 dB  |
| Peaking | 24000 Hz | 2.14 | -2.7 dB  |
| Peaking | 894 Hz   | 0.95 | 1.9 dB   |
| Peaking | 980 Hz   | 0.6  | -1.2 dB  |
| Peaking | 6182 Hz  | 7.52 | 3.1 dB   |
| Peaking | 7249 Hz  | 7.85 | -1.9 dB  |
| Peaking | 10713 Hz | 6.61 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)
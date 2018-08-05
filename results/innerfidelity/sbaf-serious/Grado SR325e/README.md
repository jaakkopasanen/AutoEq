# Grado SR325e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.7; 42 5.3; 45 4.6; 49 3.9; 52 3.5; 56 2.9; 59 2.6; 64 2.0; 68 1.6; 73 1.3; 78 0.9; 83 0.6; 89 0.3; 95 0.0; 102 -0.3; 109 -0.4; 117 -0.7; 125 -0.9; 134 -1.1; 143 -1.2; 153 -1.2; 164 -1.1; 175 -1.0; 188 -0.9; 201 -0.8; 215 -0.6; 230 -0.4; 246 -0.3; 263 -0.2; 282 -0.3; 301 -0.2; 323 0.0; 345 0.4; 369 0.5; 395 0.8; 423 0.3; 452 0.1; 484 0.2; 518 0.2; 554 0.5; 593 0.7; 635 0.8; 679 0.6; 726 0.6; 777 0.8; 832 0.6; 890 0.4; 952 0.3; 1019 0.1; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -1.2; 1429 -1.8; 1529 -2.8; 1636 -3.2; 1751 -5.0; 1873 -8.1; 2004 -8.7; 2145 -7.7; 2295 -6.0; 2455 -4.0; 2627 -2.1; 2811 -0.3; 3008 1.6; 3219 2.7; 3444 2.7; 3685 0.1; 3943 -0.8; 4219 0.6; 4514 0.1; 4830 2.7; 5168 5.5; 5530 2.2; 5917 2.9; 6331 1.6; 6775 1.5; 7249 0.5; 7756 -1.4; 8299 -4.5; 8880 -7.5; 9502 -8.5; 10167 -6.4; 10879 -1.9; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.07 | 6.9 dB   |
| Peaking | 2011 Hz | 2.49 | -11.1 dB |
| Peaking | 4151 Hz | 0.28 | 2.5 dB   |
| Peaking | 5227 Hz | 6.94 | 3.2 dB   |
| Peaking | 9354 Hz | 3.35 | -11.1 dB |
| Peaking | 50 Hz   | 2.34 | 1.1 dB   |
| Peaking | 144 Hz  | 1.42 | -1.6 dB  |
| Peaking | 3306 Hz | 4.81 | 4.9 dB   |
| Peaking | 3778 Hz | 2.73 | -3.6 dB  |
| Peaking | 6298 Hz | 3.4  | 1.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325e/Grado%20SR325e.png)
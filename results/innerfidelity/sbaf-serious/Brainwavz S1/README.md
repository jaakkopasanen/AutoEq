# Brainwavz S1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 10 -84; 20 -8.9; 22 -9.0; 23 -9.1; 25 -9.1; 26 -9.2; 28 -9.2; 30 -9.2; 32 -9.2; 35 -9.2; 37 -9.2; 40 -9.2; 42 -9.2; 45 -9.2; 49 -9.1; 52 -9.1; 56 -9.0; 59 -9.0; 64 -9.0; 68 -9.0; 73 -9.0; 78 -9.0; 83 -9.1; 89 -9.4; 95 -9.7; 102 -10.0; 109 -10.3; 117 -10.6; 125 -11.0; 134 -11.2; 143 -11.2; 153 -11.2; 164 -11.1; 175 -10.8; 188 -10.5; 201 -10.2; 215 -9.7; 230 -9.3; 246 -9.0; 263 -8.5; 282 -8.0; 301 -7.5; 323 -7.1; 345 -6.5; 369 -6.0; 395 -5.6; 423 -4.9; 452 -4.4; 484 -4.0; 518 -3.5; 554 -2.9; 593 -2.2; 635 -1.7; 679 -1.5; 726 -1.0; 777 -0.5; 832 -0.3; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.4; 1429 -0.1; 1529 -1.1; 1636 -2.4; 1751 -2.9; 1873 -2.9; 2004 -2.6; 2145 -2.5; 2295 -2.4; 2455 -2.1; 2627 -2.0; 2811 -2.1; 3008 -2.1; 3219 -2.3; 3444 -2.5; 3685 -3.1; 3943 -4.2; 4219 -6.3; 4514 -8.4; 4830 -9.0; 5168 -9.4; 5530 -7.9; 5917 -4.2; 6331 -1.7; 6775 0.3; 7249 1.0; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -2.0; 10167 -4.9; 10879 -5.4; 11640 -2.9; 12455 -0.8; 13327 -2.6; 14260 -5.9; 15258 -5.9; 16326 -1.8; 17469 0.0; 18692 -0.2; 20000 -6.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.6dB` and instead set Global volume in the UI for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.16 | -8.7 dB |
| Peaking | 187 Hz   | 0.61 | -8.4 dB |
| Peaking | 4827 Hz  | 2.61 | -9.8 dB |
| Peaking | 14646 Hz | 2.55 | -6.2 dB |
| Peaking | 20019 Hz | 5.23 | -5.9 dB |
| Peaking | 1340 Hz  | 1.28 | 4.9 dB  |
| Peaking | 1693 Hz  | 1.18 | -5.4 dB |
| Peaking | 5493 Hz  | 7.01 | -3.7 dB |
| Peaking | 8560 Hz  | 0.75 | 3.4 dB  |
| Peaking | 10483 Hz | 3.58 | -7.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S1/Brainwavz%20S1.png)
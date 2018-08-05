# Beyerdynamic T1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.4; 22 4.8; 23 4.6; 25 4.1; 26 3.9; 28 3.6; 30 3.3; 32 3.0; 35 2.7; 37 2.6; 40 2.3; 42 2.2; 45 2.0; 49 1.8; 52 1.8; 56 2.1; 59 2.4; 64 2.2; 68 1.7; 73 1.1; 78 0.7; 83 0.5; 89 0.1; 95 -0.3; 102 -0.7; 109 -1.1; 117 -1.4; 125 -1.8; 134 -2.2; 143 -2.4; 153 -2.5; 164 -2.7; 175 -2.7; 188 -2.7; 201 -2.8; 215 -2.7; 230 -2.6; 246 -2.6; 263 -2.5; 282 -2.4; 301 -2.4; 323 -2.2; 345 -2.1; 369 -2.0; 395 -1.8; 423 -1.6; 452 -1.5; 484 -1.3; 518 -1.2; 554 -1.1; 593 -0.8; 635 -0.5; 679 -0.4; 726 -0.3; 777 -0.0; 832 -0.2; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.7; 1248 0.5; 1336 0.2; 1429 0.3; 1529 -0.2; 1636 -0.8; 1751 -1.3; 1873 -1.5; 2004 -0.7; 2145 0.2; 2295 -0.4; 2455 -1.0; 2627 -0.6; 2811 -0.8; 3008 0.2; 3219 0.9; 3444 1.0; 3685 0.4; 3943 -0.1; 4219 -0.8; 4514 -0.8; 4830 2.3; 5168 5.9; 5530 2.0; 5917 -3.7; 6331 -5.2; 6775 -0.6; 7249 -2.5; 7756 -6.5; 8299 -9.8; 8880 -10.2; 9502 -7.3; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 16 Hz    |  0.65 | 5.9 dB   |
| Peaking | 65 Hz    |  1.66 | 1.9 dB   |
| Peaking | 196 Hz   |  0.61 | -3.1 dB  |
| Peaking | 5162 Hz  | 11.52 | 7.5 dB   |
| Peaking | 8602 Hz  |  3.61 | -11.3 dB |
| Peaking | 1816 Hz  |  3.27 | -3.5 dB  |
| Peaking | 2536 Hz  |  3.83 | -2.3 dB  |
| Peaking | 2043 Hz  |  1.1  | 2.5 dB   |
| Peaking | 6150 Hz  | 12.98 | -5.3 dB  |
| Peaking | 11216 Hz |  5.31 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)
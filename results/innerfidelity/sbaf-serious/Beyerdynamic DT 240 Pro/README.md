# Beyerdynamic DT 240 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.2; 23 -1.4; 25 -1.8; 26 -2.0; 28 -2.3; 30 -2.6; 32 -2.9; 35 -3.2; 37 -3.3; 40 -3.5; 42 -3.6; 45 -3.7; 49 -3.8; 52 -3.9; 56 -3.9; 59 -3.9; 64 -3.8; 68 -3.8; 73 -3.7; 78 -3.3; 83 -2.6; 89 -2.4; 95 -3.4; 102 -4.7; 109 -5.3; 117 -5.4; 125 -5.0; 134 -4.7; 143 -5.0; 153 -5.4; 164 -4.8; 175 -5.2; 188 -5.1; 201 -4.9; 215 -4.3; 230 -3.7; 246 -3.3; 263 -2.8; 282 -2.1; 301 -1.4; 323 -0.7; 345 -0.0; 369 -0.1; 395 -0.7; 423 -0.8; 452 -0.8; 484 -0.9; 518 -0.7; 554 -0.4; 593 -0.1; 635 -0.2; 679 -0.4; 726 -0.4; 777 -0.4; 832 -0.4; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.4; 1529 -2.0; 1636 -2.5; 1751 -2.8; 1873 -2.9; 2004 -2.9; 2145 -2.6; 2295 -2.1; 2455 -1.0; 2627 0.2; 2811 0.6; 3008 2.0; 3219 3.0; 3444 4.7; 3685 5.5; 3943 2.4; 4219 1.3; 4514 3.0; 4830 5.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 240 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.8  | -3.4 dB |
| Peaking | 156 Hz  | 1.03 | -5.1 dB |
| Peaking | 1915 Hz | 2.26 | -3.5 dB |
| Peaking | 3505 Hz | 4.71 | 4.9 dB  |
| Peaking | 5588 Hz | 2.8  | 6.8 dB  |
| Peaking | 113 Hz  | 1.76 | 2.0 dB  |
| Peaking | 112 Hz  | 4.15 | -3.2 dB |
| Peaking | 219 Hz  | 2.7  | -0.8 dB |
| Peaking | 348 Hz  | 5.9  | 1.5 dB  |
| Peaking | 9056 Hz | 4.75 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20240%20Pro/Beyerdynamic%20DT%20240%20Pro.png)
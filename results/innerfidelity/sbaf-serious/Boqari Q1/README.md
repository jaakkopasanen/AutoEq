# Boqari Q1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.5; 83 5.2; 89 4.6; 95 4.0; 102 3.3; 109 2.7; 117 2.0; 125 1.1; 134 0.5; 143 0.0; 153 -0.4; 164 -0.8; 175 -1.0; 188 -1.3; 201 -1.6; 215 -1.8; 230 -1.9; 246 -2.2; 263 -2.4; 282 -2.5; 301 -2.8; 323 -3.0; 345 -3.1; 369 -3.2; 395 -3.3; 423 -3.2; 452 -3.1; 484 -2.8; 518 -2.8; 554 -2.3; 593 -2.0; 635 -1.8; 679 -1.5; 726 -1.2; 777 -0.8; 832 -0.5; 890 0.0; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.3; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.0; 1636 -0.9; 1751 -0.4; 1873 0.2; 2004 1.0; 2145 1.9; 2295 2.7; 2455 3.8; 2627 4.9; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.1; 4514 0.3; 4830 -2.2; 5168 -2.2; 5530 0.8; 5917 4.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Boqari Q1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.3  | 7.9 dB  |
| Peaking | 224 Hz  | 0.43 | -5.8 dB |
| Peaking | 3343 Hz | 1.66 | 7.2 dB  |
| Peaking | 4983 Hz | 4.63 | -6.1 dB |
| Peaking | 6215 Hz | 5.43 | 6.1 dB  |
| Peaking | 18 Hz   | 2.09 | 0.9 dB  |
| Peaking | 79 Hz   | 4.51 | 0.8 dB  |
| Peaking | 924 Hz  | 3.38 | 1.3 dB  |
| Peaking | 1605 Hz | 2.61 | -1.5 dB |
| Peaking | 2556 Hz | 5.37 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Boqari%20Q1/Boqari%20Q1.png)
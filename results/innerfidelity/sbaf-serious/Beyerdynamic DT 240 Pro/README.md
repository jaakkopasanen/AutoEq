# Beyerdynamic DT 240 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.2; 23 -1.5; 25 -1.9; 26 -2.0; 28 -2.4; 30 -2.7; 32 -2.9; 35 -3.2; 37 -3.4; 40 -3.6; 42 -3.7; 45 -3.9; 49 -4.0; 52 -4.2; 56 -4.3; 59 -4.3; 64 -4.3; 68 -4.4; 73 -4.3; 78 -4.0; 83 -3.4; 89 -3.2; 95 -4.1; 102 -5.3; 109 -5.7; 117 -5.6; 125 -5.0; 134 -4.6; 143 -4.8; 153 -5.2; 164 -4.6; 175 -4.9; 188 -4.9; 201 -4.7; 215 -4.2; 230 -3.6; 246 -3.2; 263 -2.7; 282 -2.0; 301 -1.4; 323 -0.7; 345 0.0; 369 -0.1; 395 -0.6; 423 -0.7; 452 -0.8; 484 -0.9; 518 -0.7; 554 -0.4; 593 -0.1; 635 -0.2; 679 -0.4; 726 -0.4; 777 -0.4; 832 -0.4; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.4; 1529 -2.0; 1636 -2.5; 1751 -2.8; 1873 -2.9; 2004 -2.9; 2145 -2.6; 2295 -2.1; 2455 -1.0; 2627 0.2; 2811 0.6; 3008 2.0; 3219 3.0; 3444 4.7; 3685 5.5; 3943 2.4; 4219 1.3; 4514 3.0; 4830 5.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.1; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099245613600242dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 240 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.71 | -3.5 dB |
| Peaking | 152 Hz  | 0.91 | -4.6 dB |
| Peaking | 3541 Hz | 6.8  | 5.1 dB  |
| Peaking | 5593 Hz | 2.96 | 6.9 dB  |
| Peaking | 155 Hz  | 2.71 | 1.8 dB  |
| Peaking | 172 Hz  | 1.32 | -1.4 dB |
| Peaking | 345 Hz  | 4.52 | 1.6 dB  |
| Peaking | 1881 Hz | 2.68 | -3.5 dB |
| Peaking | 9096 Hz | 5.31 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20240%20Pro/Beyerdynamic%20DT%20240%20Pro.png)
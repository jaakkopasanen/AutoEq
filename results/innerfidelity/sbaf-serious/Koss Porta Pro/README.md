# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.3; 32 4.7; 35 3.7; 37 3.1; 40 2.3; 42 1.8; 45 1.1; 49 0.3; 52 -0.4; 56 -1.1; 59 -1.6; 64 -2.3; 68 -2.8; 73 -3.4; 78 -3.8; 83 -4.3; 89 -4.7; 95 -5.1; 102 -5.4; 109 -5.5; 117 -5.5; 125 -5.7; 134 -5.7; 143 -5.6; 153 -5.6; 164 -5.5; 175 -5.3; 188 -5.0; 201 -4.8; 215 -4.5; 230 -4.2; 246 -4.0; 263 -3.7; 282 -3.4; 301 -3.2; 323 -2.9; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.6; 452 -1.3; 484 -1.1; 518 -1.0; 554 -0.6; 593 -0.3; 635 -0.2; 679 -0.1; 726 0.0; 777 0.2; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -3.2; 1751 -3.7; 1873 -3.9; 2004 -3.6; 2145 -2.8; 2295 -1.6; 2455 0.1; 2627 2.0; 2811 3.6; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.4; 4514 1.8; 4830 1.7; 5168 3.7; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.86 | 7.1 dB  |
| Peaking | 125 Hz  | 0.55 | -6.3 dB |
| Peaking | 1926 Hz | 2.37 | -5.3 dB |
| Peaking | 3369 Hz | 2.03 | 7.1 dB  |
| Peaking | 6009 Hz | 4.35 | 5.8 dB  |
| Peaking | 806 Hz  | 1.69 | 0.8 dB  |
| Peaking | 1545 Hz | 6.24 | -0.7 dB |
| Peaking | 4617 Hz | 2.85 | 2.0 dB  |
| Peaking | 4668 Hz | 7.58 | -4.0 dB |
| Peaking | 8284 Hz | 3.5  | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)
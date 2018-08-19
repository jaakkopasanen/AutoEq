# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.5; 35 4.7; 37 4.2; 40 3.4; 42 2.8; 45 1.8; 49 0.5; 52 -0.3; 56 -1.3; 59 -2.1; 64 -3.2; 68 -4.0; 73 -4.8; 78 -5.6; 83 -6.2; 89 -6.8; 95 -7.3; 102 -7.5; 109 -7.4; 117 -7.2; 125 -6.9; 134 -6.5; 143 -6.2; 153 -5.8; 164 -5.3; 175 -4.8; 188 -4.3; 201 -4.0; 215 -3.5; 230 -3.0; 246 -2.7; 263 -2.2; 282 -1.9; 301 -1.9; 323 -2.0; 345 -1.9; 369 -1.6; 395 -1.4; 423 -1.0; 452 -0.8; 484 -0.7; 518 -0.7; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.2; 726 -0.2; 777 0.1; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.6; 1336 -1.1; 1429 -1.4; 1529 -1.7; 1636 -0.8; 1751 -1.7; 1873 -1.7; 2004 -1.6; 2145 -1.4; 2295 -1.3; 2455 -1.2; 2627 -1.4; 2811 -1.4; 3008 -1.1; 3219 -0.8; 3444 -2.0; 3685 -2.7; 3943 -5.0; 4219 -9.3; 4514 -9.5; 4830 -6.5; 5168 -7.7; 5530 -9.7; 5917 -11.0; 6331 -11.4; 6775 -9.9; 7249 -7.8; 7756 -5.8; 8299 -6.0; 8880 -8.6; 9502 -10.8; 10167 -10.0; 10879 -6.8; 11640 -3.6; 12455 -2.2; 13327 -1.9; 14260 -0.9; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.63 | 7.9 dB   |
| Peaking | 98 Hz    | 0.67 | -9.0 dB  |
| Peaking | 261 Hz   | 2.42 | 0.2 dB   |
| Peaking | 5837 Hz  | 1.37 | -10.5 dB |
| Peaking | 9873 Hz  | 3.78 | -8.7 dB  |
| Peaking | 884 Hz   | 0.94 | 1.9 dB   |
| Peaking | 2231 Hz  | 0.32 | -2.3 dB  |
| Peaking | 3887 Hz  | 1.14 | 4.8 dB   |
| Peaking | 4267 Hz  | 6.86 | -7.2 dB  |
| Peaking | 15689 Hz | 2.57 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)
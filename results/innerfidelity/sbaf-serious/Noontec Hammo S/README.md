# Noontec Hammo S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.9; 22 0.7; 23 0.6; 25 0.4; 26 0.3; 28 0.2; 30 0.1; 32 -0.0; 35 -0.2; 37 -0.2; 40 -0.3; 42 -0.3; 45 -0.4; 49 -0.5; 52 -0.6; 56 -0.7; 59 -0.7; 64 -0.8; 68 -0.9; 73 -0.9; 78 -1.0; 83 -1.1; 89 -1.1; 95 -1.0; 102 -0.7; 109 -0.5; 117 -0.5; 125 -1.1; 134 -1.9; 143 -2.6; 153 -3.1; 164 -2.3; 175 -2.1; 188 -2.9; 201 -2.8; 215 -2.7; 230 -2.4; 246 -2.0; 263 -1.6; 282 -1.1; 301 -0.7; 323 -0.2; 345 0.5; 369 0.9; 395 1.4; 423 1.9; 452 1.9; 484 2.1; 518 2.1; 554 2.1; 593 1.8; 635 1.2; 679 0.6; 726 0.5; 777 0.8; 832 1.0; 890 0.8; 952 0.7; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.7; 1336 -2.0; 1429 -2.4; 1529 -2.6; 1636 -2.6; 1751 -2.5; 1873 -2.2; 2004 -1.5; 2145 -0.8; 2295 -0.0; 2455 1.3; 2627 2.2; 2811 2.8; 3008 3.4; 3219 3.0; 3444 1.0; 3685 -0.5; 3943 1.2; 4219 0.4; 4514 0.8; 4830 3.5; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -1.0; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.094765865819561dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 224 Hz  | 0.81 | -4.3 dB |
| Peaking | 426 Hz  | 0.8  | 3.7 dB  |
| Peaking | 1599 Hz | 1.52 | -3.3 dB |
| Peaking | 2863 Hz | 3.71 | 3.8 dB  |
| Peaking | 5758 Hz | 3.33 | 6.9 dB  |
| Peaking | 113 Hz  | 7.79 | 0.9 dB  |
| Peaking | 2483 Hz | 3.94 | 0.3 dB  |
| Peaking | 3583 Hz | 7.39 | -0.9 dB |
| Peaking | 9325 Hz | 4.42 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S/Noontec%20Hammo%20S.png)
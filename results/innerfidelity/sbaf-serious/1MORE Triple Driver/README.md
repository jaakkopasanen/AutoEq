# 1MORE Triple Driver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.4; 23 -1.6; 25 -2.0; 26 -2.2; 28 -2.6; 30 -2.9; 32 -3.1; 35 -3.5; 37 -3.7; 40 -3.9; 42 -4.1; 45 -4.3; 49 -4.6; 52 -4.8; 56 -5.0; 59 -5.1; 64 -5.4; 68 -5.6; 73 -5.8; 78 -6.0; 83 -6.3; 89 -6.5; 95 -6.7; 102 -6.8; 109 -6.8; 117 -6.8; 125 -6.9; 134 -6.9; 143 -6.8; 153 -6.7; 164 -6.7; 175 -6.5; 188 -6.3; 201 -6.1; 215 -5.8; 230 -5.5; 246 -5.2; 263 -4.9; 282 -4.5; 301 -4.2; 323 -3.9; 345 -3.4; 369 -3.1; 395 -2.7; 423 -2.2; 452 -1.8; 484 -1.5; 518 -1.2; 554 -0.7; 593 -0.2; 635 0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.4; 1336 -1.0; 1429 -1.6; 1529 -2.2; 1636 -2.9; 1751 -3.3; 1873 -3.6; 2004 -3.9; 2145 -4.3; 2295 -4.7; 2455 -4.5; 2627 -4.3; 2811 -3.6; 3008 -2.2; 3219 -1.0; 3444 -0.3; 3685 -1.0; 3943 -2.9; 4219 -5.1; 4514 -5.2; 4830 -2.2; 5168 2.8; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.3; 9502 -3.7; 10167 -3.8; 10879 -1.7; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 -0.9; 15258 -3.8; 16326 -4.8; 17469 -3.5; 18692 -1.6; 20000 -0.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0725486821010906dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.49 | -5.7 dB |
| Peaking | 205 Hz   | 0.96 | -3.4 dB |
| Peaking | 2252 Hz  | 1.94 | -4.9 dB |
| Peaking | 4437 Hz  | 5.46 | -6.8 dB |
| Peaking | 5810 Hz  | 3.77 | 7.9 dB  |
| Peaking | 800 Hz   | 2.08 | 1.4 dB  |
| Peaking | 1630 Hz  | 5.5  | -1.1 dB |
| Peaking | 9904 Hz  | 3.25 | -6.1 dB |
| Peaking | 12447 Hz | 0.78 | 3.1 dB  |
| Peaking | 16234 Hz | 1.56 | -6.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)
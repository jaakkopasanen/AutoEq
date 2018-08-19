# Philips Fidelio S1 Early 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.4; 23 -1.4; 25 -1.4; 26 -1.4; 28 -1.4; 30 -1.4; 32 -1.4; 35 -1.5; 37 -1.5; 40 -1.5; 42 -1.5; 45 -1.5; 49 -1.6; 52 -1.7; 56 -1.8; 59 -1.8; 64 -1.9; 68 -2.1; 73 -2.2; 78 -2.3; 83 -2.5; 89 -2.6; 95 -2.7; 102 -2.8; 109 -2.8; 117 -2.8; 125 -2.8; 134 -2.8; 143 -2.8; 153 -2.7; 164 -2.7; 175 -2.5; 188 -2.4; 201 -2.3; 215 -2.1; 230 -1.9; 246 -1.7; 263 -1.6; 282 -1.3; 301 -1.1; 323 -0.9; 345 -0.7; 369 -0.5; 395 -0.4; 423 -0.1; 452 0.2; 484 0.9; 518 0.6; 554 0.6; 593 1.0; 635 1.1; 679 1.0; 726 1.1; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.2; 1336 -1.7; 1429 -2.3; 1529 -2.8; 1636 -3.2; 1751 -3.4; 1873 -3.4; 2004 -3.2; 2145 -3.0; 2295 -2.6; 2455 -1.6; 2627 -0.8; 2811 0.0; 3008 1.1; 3219 1.8; 3444 2.3; 3685 1.8; 3943 0.4; 4219 -2.1; 4514 -4.1; 4830 -4.8; 5168 -3.3; 5530 -0.9; 5917 1.8; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.309585089716281dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S1 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 107 Hz  | 0.6  | -3.0 dB |
| Peaking | 1889 Hz | 2.05 | -3.9 dB |
| Peaking | 3520 Hz | 2.81 | 4.0 dB  |
| Peaking | 4730 Hz | 3.25 | -6.2 dB |
| Peaking | 6435 Hz | 4.63 | 5.2 dB  |
| Peaking | 23 Hz   | 1.48 | -1.1 dB |
| Peaking | 236 Hz  | 1.61 | -0.6 dB |
| Peaking | 702 Hz  | 1.1  | 1.6 dB  |
| Peaking | 1216 Hz | 2.12 | -0.6 dB |
| Peaking | 1481 Hz | 5.69 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S1%20Early%202013/Philips%20Fidelio%20S1%20Early%202013.png)
# Philips O'Neil Bend

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.0; 22 3.0; 23 2.6; 25 2.0; 26 1.8; 28 1.4; 30 1.1; 32 0.8; 35 0.2; 37 -0.1; 40 -0.4; 42 -0.6; 45 -0.9; 49 -1.3; 52 -1.6; 56 -1.8; 59 -2.0; 64 -2.3; 68 -2.5; 73 -2.8; 78 -3.1; 83 -3.3; 89 -3.7; 95 -3.9; 102 -4.1; 109 -4.1; 117 -4.2; 125 -4.2; 134 -4.4; 143 -4.6; 153 -4.9; 164 -4.5; 175 -4.2; 188 -4.3; 201 -4.2; 215 -4.0; 230 -3.6; 246 -3.3; 263 -3.0; 282 -2.4; 301 -2.0; 323 -1.6; 345 -1.2; 369 -0.9; 395 -0.7; 423 -0.5; 452 -0.4; 484 -0.3; 518 -0.4; 554 -0.4; 593 -0.2; 635 -0.1; 679 -0.3; 726 -0.3; 777 -0.2; 832 -0.3; 890 -0.4; 952 -0.2; 1019 -0.1; 1090 0.3; 1167 0.8; 1248 1.3; 1336 1.6; 1429 1.9; 1529 2.4; 1636 2.8; 1751 3.4; 1873 4.2; 2004 4.9; 2145 5.8; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.9; 4514 4.6; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999816dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips O'Neil Bend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.18 | 4.4 dB  |
| Peaking | 98 Hz   | 0.67 | -3.0 dB |
| Peaking | 188 Hz  | 0.99 | -2.9 dB |
| Peaking | 2802 Hz | 1.03 | 6.5 dB  |
| Peaking | 5650 Hz | 2.9  | 4.8 dB  |
| Peaking | 951 Hz  | 2.98 | -1.0 dB |
| Peaking | 2150 Hz | 2.99 | 1.2 dB  |
| Peaking | 2771 Hz | 2.68 | -1.1 dB |
| Peaking | 3894 Hz | 4.48 | 1.1 dB  |
| Peaking | 8443 Hz | 3.4  | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20O'Neil%20Bend/Philips%20O'Neil%20Bend.png)
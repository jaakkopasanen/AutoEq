# Phiaton MS 100 BA

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.3; 22 1.1; 23 1.0; 25 0.9; 26 0.8; 28 0.7; 30 0.6; 32 0.4; 35 0.3; 37 0.2; 40 -0.0; 42 -0.1; 45 -0.3; 49 -0.5; 52 -0.6; 56 -0.8; 59 -1.1; 64 -1.4; 68 -1.6; 73 -1.9; 78 -2.1; 83 -2.4; 89 -2.7; 95 -3.0; 102 -3.3; 109 -3.4; 117 -3.6; 125 -3.8; 134 -4.0; 143 -4.2; 153 -4.3; 164 -4.4; 175 -4.4; 188 -4.4; 201 -4.5; 215 -4.4; 230 -4.4; 246 -4.3; 263 -4.2; 282 -4.0; 301 -3.9; 323 -3.7; 345 -3.5; 369 -3.3; 395 -3.0; 423 -2.6; 452 -2.3; 484 -2.1; 518 -1.8; 554 -1.4; 593 -0.9; 635 -0.5; 679 -0.4; 726 -0.1; 777 0.2; 832 0.2; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.5; 2004 -1.2; 2145 -0.7; 2295 0.2; 2455 1.9; 2627 3.2; 2811 4.0; 3008 4.8; 3219 5.2; 3444 5.5; 3685 5.7; 3943 5.9; 4219 5.5; 4514 5.3; 4830 5.8; 5168 6.0; 5530 5.9; 5917 4.4; 6331 1.2; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099245613600242dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 100 BA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.68 | 1.4 dB  |
| Peaking | 150 Hz  | 0.67 | -4.0 dB |
| Peaking | 317 Hz  | 1.27 | -2.1 dB |
| Peaking | 1858 Hz | 2.28 | -3.3 dB |
| Peaking | 3896 Hz | 1.11 | 6.6 dB  |
| Peaking | 820 Hz  | 3.11 | 0.8 dB  |
| Peaking | 2870 Hz | 3.43 | 1.4 dB  |
| Peaking | 5427 Hz | 0.57 | -1.3 dB |
| Peaking | 5524 Hz | 3.89 | 4.7 dB  |
| Peaking | 6089 Hz | 2.41 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20100%20BA/Phiaton%20MS%20100%20BA.png)
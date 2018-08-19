# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.6; 42 5.2; 45 4.5; 49 3.9; 52 3.5; 56 3.1; 59 2.8; 64 2.4; 68 2.3; 73 2.3; 78 2.3; 83 1.8; 89 1.5; 95 1.4; 102 1.2; 109 1.0; 117 1.1; 125 0.9; 134 0.8; 143 0.9; 153 0.7; 164 0.7; 175 0.8; 188 0.9; 201 1.0; 215 1.4; 230 1.9; 246 1.5; 263 1.3; 282 1.3; 301 1.2; 323 1.0; 345 1.1; 369 1.0; 395 1.3; 423 1.5; 452 1.3; 484 1.5; 518 2.1; 554 2.9; 593 3.9; 635 4.6; 679 4.5; 726 4.1; 777 3.6; 832 2.7; 890 1.7; 952 0.8; 1019 -0.3; 1090 -1.3; 1167 -2.1; 1248 -2.7; 1336 -2.9; 1429 -3.3; 1529 -2.9; 1636 -2.2; 1751 -1.8; 1873 -1.6; 2004 -0.6; 2145 0.7; 2295 2.5; 2455 4.6; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.64 | 6.4 dB  |
| Peaking | 240 Hz  | 2.57 | 1.2 dB  |
| Peaking | 692 Hz  | 1.74 | 5.3 dB  |
| Peaking | 1518 Hz | 1.16 | -6.5 dB |
| Peaking | 3418 Hz | 0.77 | 8.0 dB  |
| Peaking | 2074 Hz | 5.5  | -1.1 dB |
| Peaking | 2581 Hz | 4.83 | 1.9 dB  |
| Peaking | 3586 Hz | 2.85 | -1.2 dB |
| Peaking | 6286 Hz | 2.24 | 5.5 dB  |
| Peaking | 7363 Hz | 1.48 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)
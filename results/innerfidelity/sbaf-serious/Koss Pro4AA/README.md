# Koss Pro4AA

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 1.6; 22 1.0; 23 0.7; 25 0.2; 26 -0.1; 28 -0.5; 30 -0.9; 32 -1.2; 35 -1.6; 37 -1.9; 40 -2.3; 42 -2.5; 45 -2.7; 49 -3.1; 52 -3.3; 56 -3.7; 59 -3.9; 64 -4.2; 68 -4.4; 73 -4.6; 78 -4.9; 83 -5.4; 89 -6.4; 95 -6.9; 102 -7.0; 109 -7.0; 117 -7.6; 125 -8.4; 134 -8.8; 143 -9.0; 153 -9.2; 164 -9.0; 175 -9.4; 188 -9.6; 201 -9.6; 215 -9.5; 230 -9.3; 246 -8.9; 263 -8.4; 282 -7.7; 301 -7.6; 323 -7.8; 345 -7.7; 369 -7.2; 395 -6.5; 423 -5.8; 452 -5.1; 484 -4.7; 518 -4.0; 554 -3.3; 593 -2.5; 635 -1.9; 679 -1.6; 726 -1.3; 777 -1.0; 832 -0.8; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.6; 1248 0.8; 1336 0.6; 1429 0.2; 1529 -0.2; 1636 -0.6; 1751 -1.2; 1873 -1.6; 2004 -2.2; 2145 -3.1; 2295 -4.2; 2455 -4.7; 2627 -4.9; 2811 -5.5; 3008 -5.3; 3219 -3.6; 3444 -1.6; 3685 -0.3; 3943 1.1; 4219 0.2; 4514 -0.7; 4830 3.7; 5168 5.9; 5530 3.8; 5917 1.4; 6331 -0.3; 6775 2.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.034992534975409dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.63 | 1.8 dB  |
| Peaking | 155 Hz  | 0.6  | -9.0 dB |
| Peaking | 341 Hz  | 1.53 | -3.4 dB |
| Peaking | 2711 Hz | 2.73 | -5.9 dB |
| Peaking | 5187 Hz | 5.63 | 6.5 dB  |
| Peaking | 16 Hz   | 2.25 | 1.0 dB  |
| Peaking | 485 Hz  | 5    | -0.7 dB |
| Peaking | 1151 Hz | 2.3  | 1.6 dB  |
| Peaking | 6394 Hz | 6.98 | -2.2 dB |
| Peaking | 6796 Hz | 8.59 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA/Koss%20Pro4AA.png)
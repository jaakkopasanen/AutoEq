# Master Dynamic MH30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.2; 23 -4.2; 25 -4.3; 26 -4.3; 28 -4.4; 30 -4.4; 32 -4.4; 35 -4.4; 37 -4.3; 40 -4.3; 42 -4.3; 45 -4.2; 49 -4.3; 52 -4.3; 56 -4.4; 59 -4.4; 64 -4.4; 68 -4.4; 73 -4.4; 78 -4.5; 83 -4.5; 89 -4.5; 95 -4.5; 102 -4.6; 109 -4.7; 117 -4.7; 125 -4.8; 134 -4.7; 143 -4.8; 153 -4.9; 164 -4.4; 175 -4.3; 188 -4.4; 201 -4.2; 215 -3.8; 230 -3.3; 246 -2.8; 263 -2.2; 282 -1.7; 301 -1.6; 323 -1.6; 345 -1.6; 369 -1.7; 395 -1.8; 423 -1.9; 452 -2.0; 484 -2.2; 518 -2.3; 554 -2.1; 593 -1.9; 635 -1.9; 679 -2.0; 726 -1.8; 777 -1.5; 832 -1.3; 890 -0.9; 952 -0.4; 1019 0.2; 1090 0.9; 1167 1.5; 1248 2.0; 1336 2.3; 1429 2.4; 1529 2.6; 1636 2.7; 1751 2.7; 1873 2.9; 2004 3.0; 2145 2.7; 2295 2.5; 2455 2.6; 2627 3.0; 2811 3.0; 3008 3.2; 3219 3.4; 3444 4.3; 3685 5.7; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999994318308834dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.25 | -4.3 dB |
| Peaking | 156 Hz  | 1.03 | -2.8 dB |
| Peaking | 735 Hz  | 0.93 | -3.2 dB |
| Peaking | 1446 Hz | 0.74 | 3.4 dB  |
| Peaking | 4772 Hz | 1.45 | 6.4 dB  |
| Peaking | 208 Hz  | 7.23 | -0.5 dB |
| Peaking | 3813 Hz | 5.53 | 1.6 dB  |
| Peaking | 4645 Hz | 2.41 | -1.0 dB |
| Peaking | 6360 Hz | 3.27 | 4.4 dB  |
| Peaking | 7351 Hz | 1.7  | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH30/Master%20Dynamic%20MH30.png)
# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.8; 22 1.7; 23 1.6; 25 1.6; 26 1.6; 28 1.5; 30 1.5; 32 1.5; 35 1.5; 37 1.4; 40 1.4; 42 1.4; 45 1.5; 49 1.5; 52 1.5; 56 1.4; 59 1.4; 64 1.3; 68 1.3; 73 1.2; 78 1.2; 83 1.1; 89 1.0; 95 0.7; 102 0.3; 109 0.1; 117 0.0; 125 -0.2; 134 -0.3; 143 -0.5; 153 -0.6; 164 0.1; 175 0.3; 188 -0.1; 201 -0.0; 215 0.2; 230 0.7; 246 1.1; 263 1.5; 282 2.1; 301 2.6; 323 2.9; 345 3.0; 369 3.0; 395 2.8; 423 2.6; 452 2.2; 484 1.7; 518 1.2; 554 1.0; 593 1.0; 635 0.7; 679 0.4; 726 0.3; 777 0.3; 832 0.3; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -1.7; 1636 -2.1; 1751 -2.7; 1873 -3.2; 2004 -2.9; 2145 -2.9; 2295 -3.0; 2455 -2.1; 2627 -1.4; 2811 -0.9; 3008 -0.1; 3219 0.4; 3444 0.6; 3685 0.5; 3943 0.7; 4219 0.7; 4514 1.7; 4830 3.8; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096989832632929dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.68 | 1.8 dB  |
| Peaking | 369 Hz  | 1.76 | 3.2 dB  |
| Peaking | 2052 Hz | 1.69 | -3.5 dB |
| Peaking | 3184 Hz | 4.73 | 0.9 dB  |
| Peaking | 5666 Hz | 2.86 | 7.0 dB  |
| Peaking | 83 Hz   | 1.88 | 0.9 dB  |
| Peaking | 134 Hz  | 1.09 | -0.9 dB |
| Peaking | 288 Hz  | 5.12 | 0.7 dB  |
| Peaking | 6591 Hz | 7.85 | 2.3 dB  |
| Peaking | 7639 Hz | 2.27 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)
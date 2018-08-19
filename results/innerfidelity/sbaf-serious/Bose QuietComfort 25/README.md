# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.3; 23 -1.5; 25 -1.7; 26 -1.7; 28 -1.6; 30 -1.4; 32 -1.2; 35 -0.8; 37 -0.6; 40 -0.5; 42 -0.5; 45 -0.7; 49 -0.9; 52 -1.0; 56 -1.3; 59 -1.4; 64 -1.5; 68 -1.6; 73 -1.6; 78 -1.7; 83 -1.6; 89 -1.6; 95 -1.6; 102 -1.5; 109 -1.4; 117 -1.3; 125 -1.3; 134 -1.3; 143 -1.3; 153 -1.2; 164 -1.1; 175 -0.8; 188 -0.8; 201 -0.9; 215 -0.8; 230 -0.6; 246 -0.5; 263 -0.4; 282 -0.3; 301 -0.1; 323 0.1; 345 0.3; 369 0.6; 395 0.7; 423 1.1; 452 1.3; 484 1.4; 518 1.5; 554 1.8; 593 2.0; 635 2.0; 679 1.8; 726 1.8; 777 1.6; 832 1.2; 890 0.7; 952 0.3; 1019 0.1; 1090 0.5; 1167 0.4; 1248 0.3; 1336 -0.6; 1429 -0.5; 1529 -2.1; 1636 -3.4; 1751 -4.7; 1873 -5.7; 2004 -6.1; 2145 -5.4; 2295 -4.7; 2455 -4.1; 2627 -3.6; 2811 -4.1; 3008 -4.9; 3219 -6.0; 3444 -6.1; 3685 -4.7; 3943 -2.4; 4219 0.0; 4514 2.1; 4830 4.4; 5168 5.9; 5530 5.9; 5917 2.2; 6331 0.7; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096989832632928dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 103 Hz  | 0.2  | -1.5 dB |
| Peaking | 596 Hz  | 0.77 | 2.6 dB  |
| Peaking | 1968 Hz | 2.46 | -6.1 dB |
| Peaking | 3390 Hz | 2.69 | -6.5 dB |
| Peaking | 5148 Hz | 3.25 | 7.3 dB  |
| Peaking | 47 Hz   | 3.27 | 0.5 dB  |
| Peaking | 968 Hz  | 6.48 | -0.8 dB |
| Peaking | 1226 Hz | 4.31 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)
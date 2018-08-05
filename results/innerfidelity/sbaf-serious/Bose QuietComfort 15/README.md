# Bose QuietComfort 15

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.7; 23 -1.9; 25 -2.2; 26 -2.4; 28 -2.7; 30 -2.9; 32 -3.0; 35 -3.1; 37 -3.1; 40 -3.2; 42 -3.2; 45 -3.2; 49 -3.1; 52 -3.1; 56 -3.0; 59 -2.9; 64 -2.7; 68 -2.7; 73 -2.7; 78 -2.8; 83 -2.9; 89 -3.2; 95 -3.5; 102 -3.6; 109 -3.8; 117 -3.9; 125 -4.2; 134 -4.2; 143 -4.3; 153 -4.2; 164 -3.9; 175 -3.6; 188 -3.6; 201 -3.5; 215 -3.3; 230 -3.0; 246 -2.9; 263 -2.8; 282 -2.4; 301 -2.1; 323 -1.8; 345 -1.5; 369 -1.2; 395 -1.0; 423 -0.6; 452 -0.3; 484 -0.2; 518 -0.0; 554 0.3; 593 0.7; 635 0.9; 679 0.9; 726 1.1; 777 1.3; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.9; 1248 -1.3; 1336 -1.5; 1429 -1.4; 1529 -1.9; 1636 -2.4; 1751 -2.9; 1873 -3.0; 2004 -2.7; 2145 -2.2; 2295 -2.0; 2455 -1.7; 2627 -0.8; 2811 0.4; 3008 1.3; 3219 2.5; 3444 5.6; 3685 5.5; 3943 -0.8; 4219 -5.3; 4514 -4.7; 4830 -2.2; 5168 1.0; 5530 0.5; 5917 -4.1; 6331 -3.8; 6775 -1.6; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.69 | -2.8 dB |
| Peaking | 153 Hz  | 0.86 | -4.0 dB |
| Peaking | 1917 Hz | 2.08 | -3.2 dB |
| Peaking | 3628 Hz | 4.35 | 10.3 dB |
| Peaking | 4195 Hz | 4.03 | -8.9 dB |
| Peaking | 284 Hz  | 3.14 | -0.7 dB |
| Peaking | 711 Hz  | 2.22 | 1.7 dB  |
| Peaking | 5369 Hz | 7.57 | 5.2 dB  |
| Peaking | 6107 Hz | 3.89 | -5.5 dB |
| Peaking | 7253 Hz | 5.25 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)
# Bose QuietComfort 15

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.7; 23 -1.9; 25 -2.3; 26 -2.4; 28 -2.7; 30 -2.9; 32 -3.0; 35 -3.2; 37 -3.2; 40 -3.3; 42 -3.3; 45 -3.4; 49 -3.4; 52 -3.3; 56 -3.3; 59 -3.3; 64 -3.3; 68 -3.3; 73 -3.4; 78 -3.6; 83 -3.7; 89 -4.0; 95 -4.2; 102 -4.2; 109 -4.2; 117 -4.1; 125 -4.2; 134 -4.1; 143 -4.1; 153 -4.0; 164 -3.6; 175 -3.4; 188 -3.4; 201 -3.3; 215 -3.1; 230 -2.9; 246 -2.8; 263 -2.7; 282 -2.3; 301 -2.1; 323 -1.8; 345 -1.5; 369 -1.2; 395 -0.9; 423 -0.6; 452 -0.3; 484 -0.2; 518 -0.0; 554 0.3; 593 0.7; 635 0.9; 679 0.9; 726 1.1; 777 1.3; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.9; 1248 -1.3; 1336 -1.5; 1429 -1.4; 1529 -1.9; 1636 -2.4; 1751 -2.9; 1873 -3.0; 2004 -2.7; 2145 -2.2; 2295 -2.0; 2455 -1.7; 2627 -0.8; 2811 0.4; 3008 1.3; 3219 2.5; 3444 5.6; 3685 5.5; 3943 -0.8; 4219 -5.3; 4514 -4.7; 4830 -2.2; 5168 1.0; 5530 0.5; 5917 -4.1; 6331 -3.8; 6775 -1.6; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999529967255dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.44 | -2.9 dB |
| Peaking | 153 Hz  | 0.84 | -3.0 dB |
| Peaking | 1914 Hz | 2.1  | -3.2 dB |
| Peaking | 3604 Hz | 4.41 | 10.1 dB |
| Peaking | 4179 Hz | 4.09 | -8.8 dB |
| Peaking | 282 Hz  | 3    | -0.7 dB |
| Peaking | 710 Hz  | 2.23 | 1.7 dB  |
| Peaking | 5334 Hz | 7.88 | 5.0 dB  |
| Peaking | 6085 Hz | 4.12 | -5.3 dB |
| Peaking | 7236 Hz | 5.55 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)
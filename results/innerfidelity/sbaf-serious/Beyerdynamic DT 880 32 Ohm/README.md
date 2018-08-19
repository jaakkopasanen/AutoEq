# Beyerdynamic DT 880 32 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.4; 32 5.1; 35 4.6; 37 4.3; 40 3.9; 42 3.7; 45 3.4; 49 3.1; 52 2.8; 56 2.5; 59 2.2; 64 1.8; 68 1.8; 73 2.0; 78 1.8; 83 1.0; 89 0.2; 95 -0.3; 102 -0.7; 109 -0.9; 117 -1.2; 125 -1.5; 134 -1.8; 143 -2.0; 153 -2.2; 164 -2.2; 175 -2.4; 188 -2.5; 201 -2.6; 215 -2.6; 230 -2.4; 246 -2.4; 263 -2.5; 282 -2.3; 301 -2.2; 323 -2.2; 345 -2.1; 369 -2.0; 395 -1.9; 423 -1.6; 452 -1.1; 484 -1.1; 518 -1.2; 554 -1.0; 593 -0.8; 635 -0.7; 679 -0.6; 726 -0.5; 777 -0.1; 832 -0.2; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.6; 1429 0.2; 1529 -0.2; 1636 -0.6; 1751 -1.1; 1873 -1.3; 2004 -1.1; 2145 -1.1; 2295 -0.9; 2455 -0.3; 2627 -0.8; 2811 -1.0; 3008 -1.0; 3219 -1.0; 3444 -0.6; 3685 -0.5; 3943 -0.7; 4219 -0.7; 4514 0.3; 4830 2.5; 5168 5.7; 5530 6.0; 5917 5.5; 6331 0.2; 6775 -1.5; 7249 -1.9; 7756 -2.6; 8299 -4.0; 8880 -5.0; 9502 -3.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.52 | 6.2 dB  |
| Peaking | 76 Hz    | 4.15 | 1.4 dB  |
| Peaking | 201 Hz   | 0.57 | -2.9 dB |
| Peaking | 5506 Hz  | 5.49 | 7.6 dB  |
| Peaking | 8535 Hz  | 2.96 | -5.0 dB |
| Peaking | 1351 Hz  | 1.82 | 1.5 dB  |
| Peaking | 1782 Hz  | 2.04 | -1.6 dB |
| Peaking | 3938 Hz  | 1.23 | -1.1 dB |
| Peaking | 5057 Hz  | 9.99 | 2.3 dB  |
| Peaking | 10725 Hz | 5.68 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)
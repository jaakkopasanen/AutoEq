# Beyerdynamic DT 150 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 2.1; 22 1.6; 23 1.4; 25 1.1; 26 0.9; 28 0.7; 30 0.5; 32 0.3; 35 0.0; 37 -0.1; 40 -0.2; 42 -0.3; 45 -0.3; 49 -0.3; 52 -0.2; 56 0.1; 59 0.5; 64 0.6; 68 0.2; 73 -0.5; 78 -0.8; 83 -1.5; 89 -3.1; 95 -4.1; 102 -4.9; 109 -5.3; 117 -5.6; 125 -5.8; 134 -6.0; 143 -6.1; 153 -5.9; 164 -5.2; 175 -5.5; 188 -5.4; 201 -4.9; 215 -4.2; 230 -3.6; 246 -2.6; 263 -1.8; 282 -0.7; 301 0.2; 323 1.0; 345 1.2; 369 1.3; 395 1.0; 423 0.8; 452 0.7; 484 0.6; 518 0.5; 554 0.6; 593 0.7; 635 0.6; 679 0.4; 726 0.3; 777 0.4; 832 0.2; 890 0.1; 952 0.0; 1019 0.1; 1090 0.5; 1167 0.5; 1248 0.6; 1336 0.2; 1429 -0.4; 1529 -0.9; 1636 -1.4; 1751 -1.9; 1873 -2.3; 2004 -2.7; 2145 -3.1; 2295 -3.0; 2455 -2.2; 2627 -1.3; 2811 -0.5; 3008 0.8; 3219 1.5; 3444 2.4; 3685 2.7; 3943 1.3; 4219 -1.7; 4514 -3.0; 4830 -1.5; 5168 0.0; 5530 -0.3; 5917 1.4; 6331 5.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -2.4; 9502 -3.6; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.6; 14260 -2.3; 15258 -1.4; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.229687217881098dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 150 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 1.39 | -6.7 dB |
| Peaking | 2142 Hz | 3.35 | -3.0 dB |
| Peaking | 3527 Hz | 3.7  | 5.1 dB  |
| Peaking | 6072 Hz | 0.91 | -5.6 dB |
| Peaking | 6485 Hz | 3.04 | 10.3 dB |
| Peaking | 20 Hz   | 2.02 | 2.0 dB  |
| Peaking | 68 Hz   | 3.25 | 1.4 dB  |
| Peaking | 101 Hz  | 3.25 | -2.4 dB |
| Peaking | 216 Hz  | 1.79 | -5.8 dB |
| Peaking | 239 Hz  | 0.73 | 4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20150%20250%20Ohm/Beyerdynamic%20DT%20150%20250%20Ohm.png)
# Beyerdynamic DT 880 600 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.5; 26 5.3; 28 4.9; 30 4.5; 32 4.2; 35 3.9; 37 3.7; 40 3.4; 42 3.2; 45 3.0; 49 2.7; 52 2.4; 56 2.0; 59 1.8; 64 1.5; 68 1.6; 73 1.9; 78 1.4; 83 0.6; 89 -0.0; 95 -0.4; 102 -0.8; 109 -1.0; 117 -1.2; 125 -1.6; 134 -1.8; 143 -2.0; 153 -2.2; 164 -2.2; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.6; 230 -2.5; 246 -2.5; 263 -2.4; 282 -2.4; 301 -2.2; 323 -2.2; 345 -2.1; 369 -2.0; 395 -1.9; 423 -1.6; 452 -1.2; 484 -1.2; 518 -1.3; 554 -1.2; 593 -0.9; 635 -0.8; 679 -0.8; 726 -0.6; 777 -0.3; 832 -0.4; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.7; 1336 0.6; 1429 0.3; 1529 -0.1; 1636 -0.5; 1751 -0.9; 1873 -1.1; 2004 -0.8; 2145 -0.6; 2295 -0.2; 2455 0.5; 2627 0.3; 2811 0.1; 3008 0.4; 3219 0.6; 3444 1.0; 3685 1.1; 3943 1.1; 4219 0.4; 4514 0.5; 4830 1.3; 5168 1.3; 5530 -0.6; 5917 -2.0; 6331 -1.4; 6775 -1.2; 7249 -1.9; 7756 -3.7; 8299 -5.9; 8880 -7.2; 9502 -6.2; 10167 -2.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.5; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.44 | 6.2 dB  |
| Peaking | 74 Hz    | 3.62 | 1.2 dB  |
| Peaking | 194 Hz   | 1.52 | 0.8 dB  |
| Peaking | 202 Hz   | 0.65 | -3.5 dB |
| Peaking | 8826 Hz  | 3.88 | -7.9 dB |
| Peaking | 1255 Hz  | 3.34 | 1.0 dB  |
| Peaking | 1853 Hz  | 3.92 | -1.3 dB |
| Peaking | 4407 Hz  | 1.47 | 1.4 dB  |
| Peaking | 5962 Hz  | 7.16 | -2.3 dB |
| Peaking | 11021 Hz | 7.72 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20600%20Ohm/Beyerdynamic%20DT%20880%20600%20Ohm.png)
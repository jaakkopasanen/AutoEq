# Beyerdynamic DT 235

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.7; 40 5.0; 42 4.5; 45 3.9; 49 3.1; 52 2.5; 56 1.9; 59 1.6; 64 1.1; 68 0.6; 73 0.1; 78 -0.3; 83 -0.4; 89 -0.4; 95 -0.7; 102 -1.3; 109 -1.6; 117 -1.8; 125 -2.0; 134 -2.2; 143 -2.2; 153 -2.2; 164 -2.0; 175 -1.9; 188 -1.6; 201 -1.0; 215 -0.6; 230 -0.5; 246 -0.6; 263 -0.6; 282 -0.5; 301 -0.5; 323 -0.6; 345 -0.7; 369 -0.8; 395 -0.9; 423 -0.7; 452 -0.4; 484 -0.5; 518 -0.5; 554 -0.1; 593 0.1; 635 -0.1; 679 -0.5; 726 -0.8; 777 -0.9; 832 -1.1; 890 -1.1; 952 -0.4; 1019 -0.1; 1090 -0.2; 1167 0.2; 1248 0.5; 1336 0.7; 1429 -0.6; 1529 -2.7; 1636 -4.4; 1751 -4.1; 1873 -3.2; 2004 -1.7; 2145 -0.3; 2295 0.8; 2455 2.0; 2627 2.6; 2811 3.5; 3008 4.9; 3219 5.2; 3444 4.5; 3685 3.4; 3943 5.8; 4219 4.0; 4514 -0.6; 4830 -3.8; 5168 -2.2; 5530 0.3; 5917 3.6; 6331 5.0; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -5.2; 8880 -7.0; 9502 -6.5; 10167 -4.2; 10879 -1.3; 11640 -0.0; 12455 0.0; 13327 -0.8; 14260 -3.1; 15258 -2.2; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.38 | 7.2 dB  |
| Peaking | 1729 Hz  | 4.22 | -5.2 dB |
| Peaking | 3227 Hz  | 2.53 | 5.8 dB  |
| Peaking | 6569 Hz  | 5.87 | 6.5 dB  |
| Peaking | 9037 Hz  | 3.15 | -7.9 dB |
| Peaking | 137 Hz   | 1.55 | -2.5 dB |
| Peaking | 460 Hz   | 0.9  | -0.5 dB |
| Peaking | 4085 Hz  | 8.18 | 4.4 dB  |
| Peaking | 4796 Hz  | 7.17 | -5.7 dB |
| Peaking | 14687 Hz | 6.86 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)
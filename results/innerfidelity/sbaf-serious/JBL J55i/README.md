# JBL J55i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.2; 22 -4.2; 23 -4.2; 25 -4.2; 26 -4.2; 28 -4.2; 30 -4.2; 32 -4.2; 35 -4.2; 37 -4.2; 40 -4.2; 42 -4.2; 45 -4.2; 49 -4.2; 52 -4.3; 56 -4.4; 59 -4.4; 64 -4.6; 68 -4.7; 73 -4.9; 78 -5.0; 83 -5.2; 89 -5.5; 95 -5.7; 102 -5.8; 109 -5.9; 117 -6.2; 125 -6.5; 134 -6.7; 143 -6.9; 153 -7.0; 164 -6.9; 175 -6.7; 188 -6.8; 201 -7.0; 215 -7.0; 230 -6.9; 246 -6.6; 263 -6.3; 282 -5.7; 301 -5.3; 323 -5.1; 345 -4.7; 369 -4.1; 395 -3.6; 423 -2.7; 452 -1.9; 484 -1.1; 518 -0.2; 554 0.9; 593 1.8; 635 2.0; 679 1.7; 726 1.1; 777 0.7; 832 -0.0; 890 -0.4; 952 -0.4; 1019 0.2; 1090 0.8; 1167 1.6; 1248 1.9; 1336 1.4; 1429 -0.2; 1529 -1.7; 1636 -1.3; 1751 3.0; 1873 6.0; 2004 4.0; 2145 0.2; 2295 1.3; 2455 3.7; 2627 5.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.23 | -3.8 dB |
| Peaking | 197 Hz  | 0.48 | -6.8 dB |
| Peaking | 608 Hz  | 2.14 | 4.3 dB  |
| Peaking | 3318 Hz | 1.2  | 6.2 dB  |
| Peaking | 5635 Hz | 2.86 | 4.5 dB  |
| Peaking | 1266 Hz | 5.58 | 2.2 dB  |
| Peaking | 1621 Hz | 3.99 | -6.8 dB |
| Peaking | 1857 Hz | 3.49 | 8.3 dB  |
| Peaking | 2143 Hz | 6.64 | -6.0 dB |
| Peaking | 8398 Hz | 3.65 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J55i/JBL%20J55i.png)
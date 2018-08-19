# JBL J88i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.5; 22 3.1; 23 2.9; 25 2.6; 26 2.5; 28 2.2; 30 2.0; 32 1.8; 35 1.6; 37 1.4; 40 1.2; 42 1.1; 45 1.0; 49 0.8; 52 0.6; 56 0.5; 59 0.3; 64 0.1; 68 -0.0; 73 -0.4; 78 -0.6; 83 -0.8; 89 -1.1; 95 -1.4; 102 -1.6; 109 -1.8; 117 -2.0; 125 -2.4; 134 -2.7; 143 -2.9; 153 -3.2; 164 -3.0; 175 -2.9; 188 -3.2; 201 -3.3; 215 -3.5; 230 -3.5; 246 -3.6; 263 -3.5; 282 -3.2; 301 -2.9; 323 -2.1; 345 -1.3; 369 -0.3; 395 1.3; 423 3.5; 452 5.2; 484 5.6; 518 6.0; 554 6.0; 593 6.0; 635 5.4; 679 3.5; 726 2.1; 777 1.4; 832 0.7; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.0; 1167 -0.3; 1248 -0.8; 1336 -0.9; 1429 -1.1; 1529 -0.8; 1636 0.1; 1751 1.8; 1873 3.5; 2004 5.3; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J88i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 404 Hz  | 0.39 | -7.6 dB |
| Peaking | 523 Hz  | 1.33 | 13.5 dB |
| Peaking | 1445 Hz | 2.68 | -4.0 dB |
| Peaking | 2970 Hz | 0.6  | 7.6 dB  |
| Peaking | 18 Hz   | 0.87 | 3.4 dB  |
| Peaking | 51 Hz   | 0.77 | 0.8 dB  |
| Peaking | 3269 Hz | 4.16 | -1.1 dB |
| Peaking | 6215 Hz | 2.1  | 5.3 dB  |
| Peaking | 7545 Hz | 1.45 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J88i/JBL%20J88i.png)
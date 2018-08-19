# T-Peos Popular

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -8.4; 22 -8.4; 23 -8.4; 25 -8.3; 26 -8.3; 28 -8.2; 30 -8.1; 32 -8.0; 35 -7.9; 37 -7.8; 40 -7.6; 42 -7.6; 45 -7.4; 49 -7.3; 52 -7.2; 56 -7.1; 59 -7.0; 64 -6.9; 68 -6.8; 73 -6.7; 78 -6.6; 83 -6.6; 89 -6.5; 95 -6.4; 102 -6.2; 109 -6.0; 117 -5.8; 125 -5.6; 134 -5.5; 143 -5.2; 153 -5.0; 164 -4.7; 175 -4.4; 188 -4.1; 201 -3.8; 215 -3.4; 230 -3.1; 246 -2.8; 263 -2.4; 282 -2.0; 301 -1.7; 323 -1.4; 345 -1.0; 369 -0.7; 395 -0.4; 423 0.0; 452 0.4; 484 0.5; 518 0.7; 554 1.0; 593 1.4; 635 1.5; 679 1.4; 726 1.5; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.3; 1090 -0.6; 1167 -0.1; 1248 -1.2; 1336 -2.2; 1429 -3.0; 1529 -4.2; 1636 -5.2; 1751 -6.0; 1873 -6.6; 2004 -7.0; 2145 -7.2; 2295 -6.4; 2455 -4.4; 2627 -2.0; 2811 0.3; 3008 2.8; 3219 4.3; 3444 5.4; 3685 5.3; 3943 4.2; 4219 1.6; 4514 -0.9; 4830 -3.5; 5168 -5.9; 5530 -6.0; 5917 -2.2; 6331 0.5; 6775 2.3; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -1.9; 9502 -2.9; 10167 -2.5; 10879 -0.7; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.597089652318436dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Popular ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.3  | -8.2 dB |
| Peaking | 134 Hz  | 0.99 | -3.1 dB |
| Peaking | 2067 Hz | 2.1  | -8.8 dB |
| Peaking | 3494 Hz | 2.39 | 7.7 dB  |
| Peaking | 5244 Hz | 5.17 | -7.9 dB |
| Peaking | 702 Hz  | 1.53 | 2.3 dB  |
| Peaking | 1558 Hz | 5.16 | -1.6 dB |
| Peaking | 5847 Hz | 2.91 | -1.6 dB |
| Peaking | 6748 Hz | 4.07 | 3.9 dB  |
| Peaking | 9639 Hz | 4.62 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Popular/T-Peos%20Popular.png)
# Beyerdynamic T5p sn2866

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.2; 22 1.8; 23 1.7; 25 1.4; 26 1.3; 28 1.2; 30 1.0; 32 0.9; 35 0.8; 37 0.7; 40 0.7; 42 0.6; 45 0.6; 49 0.6; 52 0.7; 56 0.8; 59 0.8; 64 0.9; 68 0.9; 73 1.2; 78 1.4; 83 1.4; 89 1.0; 95 0.2; 102 -1.3; 109 -2.3; 117 -3.0; 125 -3.9; 134 -4.2; 143 -4.1; 153 -3.6; 164 -2.3; 175 -2.6; 188 -3.2; 201 -3.1; 215 -2.7; 230 -2.2; 246 -1.7; 263 -1.3; 282 -0.8; 301 -0.5; 323 -0.2; 345 0.0; 369 0.2; 395 0.2; 423 0.3; 452 0.2; 484 -0.1; 518 -0.4; 554 -0.3; 593 1.1; 635 4.0; 679 2.1; 726 1.2; 777 1.3; 832 0.5; 890 -0.7; 952 -0.4; 1019 0.2; 1090 0.0; 1167 -1.6; 1248 -2.8; 1336 -2.4; 1429 -1.8; 1529 -3.4; 1636 -3.8; 1751 -4.3; 1873 -3.2; 2004 -2.6; 2145 -4.2; 2295 -3.4; 2455 -1.4; 2627 0.5; 2811 0.6; 3008 1.3; 3219 2.0; 3444 3.0; 3685 3.7; 3943 5.2; 4219 2.6; 4514 3.5; 4830 6.0; 5168 5.8; 5530 2.2; 5917 0.2; 6331 0.1; 6775 1.9; 7249 1.3; 7756 -2.2; 8299 -4.9; 8880 -4.3; 9502 -1.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099856830925147dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sn2866 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 133 Hz  | 3.67 | -4.3 dB |
| Peaking | 201 Hz  | 3.14 | -2.9 dB |
| Peaking | 1895 Hz | 1.7  | -5.0 dB |
| Peaking | 4281 Hz | 1.27 | 5.1 dB  |
| Peaking | 8479 Hz | 5.31 | -6.4 dB |
| Peaking | 14 Hz   | 0.58 | 2.4 dB  |
| Peaking | 79 Hz   | 3.88 | 1.8 dB  |
| Peaking | 389 Hz  | 0.08 | -0.2 dB |
| Peaking | 649 Hz  | 5.64 | 4.0 dB  |
| Peaking | 2833 Hz | 3.29 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sn2866/Beyerdynamic%20T5p%20sn2866.png)
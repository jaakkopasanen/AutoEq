# Havi B3 Pro1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.7; 52 5.5; 56 5.1; 59 4.8; 64 4.5; 68 4.2; 73 3.8; 78 3.5; 83 3.1; 89 2.9; 95 2.5; 102 2.2; 109 2.0; 117 1.9; 125 1.5; 134 1.3; 143 1.1; 153 0.9; 164 0.8; 175 0.7; 188 0.5; 201 0.4; 215 0.3; 230 0.3; 246 0.2; 263 0.1; 282 0.1; 301 -0.0; 323 -0.1; 345 -0.1; 369 -0.2; 395 -0.3; 423 -0.3; 452 -0.3; 484 -0.5; 518 -0.5; 554 -0.6; 593 -0.4; 635 -0.3; 679 -0.4; 726 -0.4; 777 -0.2; 832 -0.1; 890 -0.0; 952 -0.0; 1019 0.1; 1090 0.4; 1167 0.8; 1248 0.4; 1336 0.3; 1429 1.2; 1529 1.1; 1636 0.9; 1751 1.3; 1873 1.5; 2004 1.7; 2145 2.1; 2295 2.6; 2455 3.5; 2627 4.2; 2811 5.0; 3008 5.8; 3219 6.0; 3444 5.8; 3685 4.7; 3943 3.6; 4219 3.7; 4514 5.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Havi B3 Pro1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.51 | 6.5 dB  |
| Peaking | 3034 Hz | 1.99 | 4.9 dB  |
| Peaking | 5852 Hz | 1.56 | 6.6 dB  |
| Peaking | 7639 Hz | 3.43 | -2.5 dB |
| Peaking | 9104 Hz | 1.18 | -1.1 dB |
| Peaking | 478 Hz  | 1.05 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Havi%20B3%20Pro1/Havi%20B3%20Pro1.png)
# Beyerdynamic T5p sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.0; 23 -0.9; 25 -0.8; 26 -0.7; 28 -0.5; 30 -0.3; 32 -0.1; 35 0.2; 37 0.4; 40 0.6; 42 0.8; 45 1.0; 49 1.1; 52 1.2; 56 1.6; 59 1.9; 64 2.6; 68 3.0; 73 3.2; 78 2.5; 83 1.3; 89 -0.2; 95 -1.5; 102 -2.3; 109 -2.5; 117 -2.5; 125 -2.2; 134 -1.9; 143 -1.5; 153 -0.9; 164 0.0; 175 -0.7; 188 -0.7; 201 -0.3; 215 0.1; 230 0.5; 246 0.8; 263 1.2; 282 1.5; 301 1.7; 323 1.9; 345 2.1; 369 2.3; 395 2.2; 423 2.4; 452 2.5; 484 2.3; 518 2.4; 554 2.9; 593 3.6; 635 5.2; 679 5.0; 726 2.1; 777 2.0; 832 2.0; 890 1.4; 952 1.2; 1019 -0.0; 1090 0.0; 1167 0.5; 1248 0.1; 1336 -1.7; 1429 -2.0; 1529 -0.8; 1636 -0.7; 1751 -1.1; 1873 0.1; 2004 -0.4; 2145 -1.9; 2295 -2.1; 2455 -0.6; 2627 0.8; 2811 1.1; 3008 1.9; 3219 2.9; 3444 3.7; 3685 4.1; 3943 4.2; 4219 3.3; 4514 4.6; 4830 6.0; 5168 6.0; 5530 3.5; 5917 0.0; 6331 -0.0; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099890931350995dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 1.83 | 5.3 dB  |
| Peaking | 103 Hz  | 1.47 | -4.5 dB |
| Peaking | 375 Hz  | 1.45 | 2.4 dB  |
| Peaking | 650 Hz  | 4.32 | 4.8 dB  |
| Peaking | 4604 Hz | 2.22 | 5.6 dB  |
| Peaking | 20 Hz   | 1.99 | -1.1 dB |
| Peaking | 1399 Hz | 7.01 | -2.5 dB |
| Peaking | 2250 Hz | 6.5  | -2.8 dB |
| Peaking | 3386 Hz | 4.54 | 2.2 dB  |
| Peaking | 6115 Hz | 0.56 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sample%201/Beyerdynamic%20T5p%20sample%201.png)
# Stax 4070

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 3.1; 22 1.6; 23 1.0; 25 0.1; 26 -0.2; 28 -0.5; 30 -0.6; 32 -0.5; 35 -0.3; 37 -0.1; 40 0.2; 42 0.4; 45 0.6; 49 0.9; 52 1.0; 56 1.1; 59 1.2; 64 1.2; 68 1.1; 73 0.9; 78 0.8; 83 0.7; 89 0.5; 95 0.4; 102 0.3; 109 0.3; 117 0.2; 125 -0.0; 134 -0.1; 143 -0.2; 153 -0.3; 164 -0.4; 175 -0.3; 188 -0.6; 201 -0.7; 215 -0.7; 230 -0.7; 246 -0.8; 263 -0.9; 282 -1.0; 301 -1.0; 323 -1.1; 345 -0.7; 369 0.1; 395 1.3; 423 2.1; 452 1.9; 484 1.4; 518 1.3; 554 1.5; 593 1.9; 635 2.0; 679 1.7; 726 1.4; 777 1.3; 832 0.8; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -2.2; 1529 -3.2; 1636 -3.9; 1751 -4.2; 1873 -4.0; 2004 -3.6; 2145 -3.0; 2295 -2.4; 2455 -2.0; 2627 -2.3; 2811 -3.0; 3008 -3.8; 3219 -4.0; 3444 -4.4; 3685 -5.5; 3943 -6.3; 4219 -7.1; 4514 -6.4; 4830 -4.2; 5168 -1.9; 5530 -1.1; 5917 -1.5; 6331 -0.8; 6775 2.4; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.8; 9502 -2.8; 10167 -1.4; 10879 -0.6; 11640 -0.6; 12455 -0.6; 13327 -0.4; 14260 -0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.5; 20000 -3.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2172353580027817dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax 4070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 2.36 | 1.3 dB  |
| Peaking | 625 Hz  | 1.73 | 2.3 dB  |
| Peaking | 1777 Hz | 1.79 | -3.8 dB |
| Peaking | 4040 Hz | 2.32 | -6.4 dB |
| Peaking | 8432 Hz | 2.42 | -1.3 dB |
| Peaking | 17 Hz   | 3.13 | 3.0 dB  |
| Peaking | 310 Hz  | 1.38 | -1.5 dB |
| Peaking | 421 Hz  | 4.92 | 2.4 dB  |
| Peaking | 7086 Hz | 5.08 | 3.8 dB  |
| Peaking | 9395 Hz | 5.93 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%204070/Stax%204070.png)
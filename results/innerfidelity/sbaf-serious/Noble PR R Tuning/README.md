# Noble PR R Tuning

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.8; 59 5.6; 64 5.3; 68 5.1; 73 4.8; 78 4.5; 83 4.2; 89 3.8; 95 3.5; 102 3.2; 109 3.0; 117 2.8; 125 2.5; 134 2.3; 143 2.1; 153 1.9; 164 1.8; 175 1.7; 188 1.6; 201 1.4; 215 1.4; 230 1.4; 246 1.3; 263 1.3; 282 1.3; 301 1.3; 323 1.3; 345 1.4; 369 1.4; 395 1.4; 423 1.6; 452 1.6; 484 1.6; 518 1.6; 554 1.7; 593 1.8; 635 1.8; 679 1.7; 726 1.6; 777 1.6; 832 1.3; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.5; 1336 -2.2; 1429 -2.9; 1529 -3.5; 1636 -4.1; 1751 -4.5; 1873 -4.6; 2004 -4.4; 2145 -4.3; 2295 -4.0; 2455 -3.1; 2627 -2.1; 2811 -0.9; 3008 1.0; 3219 2.3; 3444 3.1; 3685 2.8; 3943 1.7; 4219 -0.5; 4514 -2.3; 4830 -2.8; 5168 -2.0; 5530 -0.6; 5917 2.4; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -2.5; 9502 -3.2; 10167 -2.8; 10879 -1.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR R Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.11 | 6.3 dB  |
| Peaking | 1952 Hz | 1.77 | -5.2 dB |
| Peaking | 3408 Hz | 5.28 | 4.6 dB  |
| Peaking | 6495 Hz | 7.18 | 5.9 dB  |
| Peaking | 9612 Hz | 3.93 | -3.6 dB |
| Peaking | 148 Hz  | 1.38 | -0.8 dB |
| Peaking | 680 Hz  | 0.9  | 2.0 dB  |
| Peaking | 1357 Hz | 1.81 | -1.4 dB |
| Peaking | 4777 Hz | 3.87 | -5.4 dB |
| Peaking | 4826 Hz | 1.52 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20R%20Tuning/Noble%20PR%20R%20Tuning.png)
# Noble PR R Tuning

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.9; 89 5.4; 95 4.9; 102 4.3; 109 3.7; 117 3.2; 125 2.5; 134 2.0; 143 1.7; 153 1.4; 164 1.2; 175 1.2; 188 1.1; 201 1.0; 215 1.0; 230 1.0; 246 1.0; 263 1.1; 282 1.1; 301 1.1; 323 1.2; 345 1.3; 369 1.3; 395 1.3; 423 1.5; 452 1.6; 484 1.5; 518 1.6; 554 1.7; 593 1.8; 635 1.8; 679 1.7; 726 1.6; 777 1.6; 832 1.3; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.5; 1336 -2.2; 1429 -2.9; 1529 -3.5; 1636 -4.1; 1751 -4.5; 1873 -4.6; 2004 -4.4; 2145 -4.3; 2295 -4.0; 2455 -3.1; 2627 -2.1; 2811 -0.9; 3008 1.0; 3219 2.3; 3444 3.1; 3685 2.8; 3943 1.7; 4219 -0.5; 4514 -2.3; 4830 -2.8; 5168 -2.0; 5530 -0.6; 5917 2.4; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -2.5; 9502 -3.2; 10167 -2.8; 10879 -1.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR R Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.36 | 6.5 dB  |
| Peaking | 1953 Hz | 1.77 | -5.2 dB |
| Peaking | 3409 Hz | 5.27 | 4.6 dB  |
| Peaking | 6494 Hz | 7.21 | 5.9 dB  |
| Peaking | 9611 Hz | 3.94 | -3.6 dB |
| Peaking | 5 Hz    | 1.39 | 0.7 dB  |
| Peaking | 85 Hz   | 3.04 | 1.3 dB  |
| Peaking | 156 Hz  | 1.71 | -1.2 dB |
| Peaking | 613 Hz  | 1.36 | 2.0 dB  |
| Peaking | 4822 Hz | 6.68 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20R%20Tuning/Noble%20PR%20R%20Tuning.png)
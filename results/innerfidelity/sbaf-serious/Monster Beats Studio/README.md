# Monster Beats Studio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.5; 25 3.1; 26 1.6; 28 -1.3; 30 -3.9; 32 -5.5; 35 -6.6; 37 -6.8; 40 -6.8; 42 -6.6; 45 -6.3; 49 -6.1; 52 -6.0; 56 -5.8; 59 -5.7; 64 -5.6; 68 -5.4; 73 -5.3; 78 -5.5; 83 -5.9; 89 -6.4; 95 -6.8; 102 -7.0; 109 -7.3; 117 -7.3; 125 -7.4; 134 -7.5; 143 -7.7; 153 -7.6; 164 -7.6; 175 -7.7; 188 -7.7; 201 -7.6; 215 -7.7; 230 -7.4; 246 -7.4; 263 -7.3; 282 -7.0; 301 -7.0; 323 -7.0; 345 -6.7; 369 -6.3; 395 -6.5; 423 -6.4; 452 -6.1; 484 -5.8; 518 -5.5; 554 -5.0; 593 -3.9; 635 -2.5; 679 -1.7; 726 -0.6; 777 0.4; 832 0.9; 890 1.0; 952 0.5; 1019 -0.2; 1090 -1.0; 1167 -2.2; 1248 -3.5; 1336 -4.9; 1429 -5.7; 1529 -6.4; 1636 -7.1; 1751 -7.3; 1873 -7.0; 2004 -6.4; 2145 -5.8; 2295 -4.8; 2455 -3.6; 2627 -2.3; 2811 -1.2; 3008 0.4; 3219 1.9; 3444 2.0; 3685 -0.9; 3943 -1.0; 4219 -1.7; 4514 -6.0; 4830 -5.0; 5168 -0.8; 5530 -2.9; 5917 -2.6; 6331 -1.5; 6775 -1.2; 7249 -2.9; 7756 -5.7; 8299 -8.5; 8880 -9.6; 9502 -8.3; 10167 -5.4; 10879 -1.9; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.76 | 11.9 dB  |
| Peaking | 34 Hz   | 0.92 | -8.8 dB  |
| Peaking | 198 Hz  | 0.48 | -7.9 dB  |
| Peaking | 1790 Hz | 2.32 | -7.6 dB  |
| Peaking | 8824 Hz | 3.01 | -10.2 dB |
| Peaking | 505 Hz  | 2.09 | -2.6 dB  |
| Peaking | 850 Hz  | 1.89 | 3.9 dB   |
| Peaking | 1356 Hz | 3.73 | -2.3 dB  |
| Peaking | 3289 Hz | 7.21 | 3.8 dB   |
| Peaking | 4603 Hz | 8.7  | -6.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Studio/Monster%20Beats%20Studio.png)
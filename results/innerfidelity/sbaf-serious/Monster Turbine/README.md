# Monster Turbine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 -11.4; 22 -11.3; 23 -11.3; 25 -11.2; 26 -11.1; 28 -11.0; 30 -10.9; 32 -10.8; 35 -10.7; 37 -10.6; 40 -10.4; 42 -10.3; 45 -10.2; 49 -10.0; 52 -9.9; 56 -9.7; 59 -9.6; 64 -9.5; 68 -9.4; 73 -9.3; 78 -9.2; 83 -9.1; 89 -9.0; 95 -9.0; 102 -8.8; 109 -8.5; 117 -8.3; 125 -8.0; 134 -7.9; 143 -7.6; 153 -7.4; 164 -7.1; 175 -6.7; 188 -6.4; 201 -6.0; 215 -5.6; 230 -5.2; 246 -4.9; 263 -4.5; 282 -4.0; 301 -3.6; 323 -3.2; 345 -2.8; 369 -2.4; 395 -2.1; 423 -1.5; 452 -1.1; 484 -0.9; 518 -0.6; 554 -0.1; 593 0.4; 635 0.6; 679 0.7; 726 0.8; 777 1.0; 832 0.9; 890 0.6; 952 0.3; 1019 -0.2; 1090 -0.9; 1167 -0.3; 1248 -0.9; 1336 -1.4; 1429 -1.6; 1529 -2.4; 1636 -3.1; 1751 -3.7; 1873 -4.0; 2004 -4.4; 2145 -5.0; 2295 -5.5; 2455 -5.7; 2627 -6.0; 2811 -5.7; 3008 -4.4; 3219 -3.0; 3444 -1.6; 3685 -1.4; 3943 -2.3; 4219 -4.3; 4514 -5.8; 4830 -5.7; 5168 -3.6; 5530 -1.0; 5917 1.7; 6331 3.4; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -2.1; 10879 -2.5; 11640 -1.4; 12455 -1.0; 13327 -1.9; 14260 -1.8; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1905356003340195dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.21 | -11.0 dB |
| Peaking | 155 Hz   | 0.8  | -3.7 dB  |
| Peaking | 2397 Hz  | 1.78 | -6.1 dB  |
| Peaking | 4713 Hz  | 4.61 | -6.0 dB  |
| Peaking | 6464 Hz  | 5.23 | 5.2 dB   |
| Peaking | 298 Hz   | 2.07 | -0.8 dB  |
| Peaking | 724 Hz   | 1.63 | 1.8 dB   |
| Peaking | 1653 Hz  | 4.62 | -1.2 dB  |
| Peaking | 9170 Hz  | 1.52 | 2.3 dB   |
| Peaking | 10603 Hz | 1.48 | -3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Turbine/Monster%20Turbine.png)
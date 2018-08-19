# NuForce Primo 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.7; 22 5.6; 23 5.5; 25 5.4; 26 5.3; 28 5.2; 30 5.1; 32 5.0; 35 4.8; 37 4.7; 40 4.6; 42 4.5; 45 4.4; 49 4.1; 52 4.0; 56 3.7; 59 3.5; 64 3.3; 68 3.1; 73 2.8; 78 2.6; 83 2.3; 89 2.0; 95 1.7; 102 1.4; 109 1.3; 117 1.1; 125 0.8; 134 0.6; 143 0.4; 153 0.2; 164 0.0; 175 -0.1; 188 -0.2; 201 -0.3; 215 -0.3; 230 -0.3; 246 -0.4; 263 -0.3; 282 -0.2; 301 -0.2; 323 -0.2; 345 -0.1; 369 -0.0; 395 0.1; 423 0.3; 452 0.4; 484 0.4; 518 0.4; 554 0.7; 593 0.9; 635 1.0; 679 0.9; 726 0.9; 777 1.1; 832 0.9; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.6; 1429 -2.3; 1529 -3.0; 1636 -3.6; 1751 -4.0; 1873 -4.1; 2004 -3.7; 2145 -2.6; 2295 -0.9; 2455 1.5; 2627 3.7; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 3.9; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999755221dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.72 | 5.3 dB  |
| Peaking | 58 Hz   | 1.22 | 2.2 dB  |
| Peaking | 739 Hz  | 2.15 | 1.2 dB  |
| Peaking | 1889 Hz | 1.63 | -8.2 dB |
| Peaking | 3438 Hz | 0.86 | 8.4 dB  |
| Peaking | 220 Hz  | 1.84 | -0.6 dB |
| Peaking | 2828 Hz | 5.85 | 2.1 dB  |
| Peaking | 3608 Hz | 1.57 | -1.2 dB |
| Peaking | 5817 Hz | 2.36 | 4.2 dB  |
| Peaking | 7456 Hz | 1.24 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20Primo%208/NuForce%20Primo%208.png)
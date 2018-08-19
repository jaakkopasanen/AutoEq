# NuForce NE700M 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -12.3; 22 -12.1; 23 -12.0; 25 -11.8; 26 -11.7; 28 -11.5; 30 -11.3; 32 -11.1; 35 -10.8; 37 -10.6; 40 -10.4; 42 -10.2; 45 -10.0; 49 -9.7; 52 -9.5; 56 -9.2; 59 -9.0; 64 -8.9; 68 -8.8; 73 -8.6; 78 -8.4; 83 -8.3; 89 -8.2; 95 -8.1; 102 -7.8; 109 -7.5; 117 -7.3; 125 -7.1; 134 -7.0; 143 -6.6; 153 -6.4; 164 -6.1; 175 -5.7; 188 -5.5; 201 -5.2; 215 -4.8; 230 -4.4; 246 -4.1; 263 -3.7; 282 -3.3; 301 -3.0; 323 -2.6; 345 -2.2; 369 -1.9; 395 -1.6; 423 -1.1; 452 -0.8; 484 -0.6; 518 -0.4; 554 0.0; 593 0.5; 635 0.5; 679 0.6; 726 0.8; 777 1.0; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.6; 1529 -3.3; 1636 -3.9; 1751 -4.4; 1873 -4.7; 2004 -5.0; 2145 -5.6; 2295 -6.2; 2455 -6.7; 2627 -7.0; 2811 -6.7; 3008 -4.9; 3219 -2.7; 3444 -0.9; 3685 -0.5; 3943 -1.1; 4219 -2.7; 4514 -4.2; 4830 -4.6; 5168 -3.7; 5530 -1.7; 5917 0.9; 6331 2.8; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.1; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -2.4; 15258 -4.8; 16326 -2.9; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6337684352338853dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce NE700M 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -11.9 dB |
| Peaking | 153 Hz   | 0.84 | -3.3 dB  |
| Peaking | 1739 Hz  | 3.15 | -2.9 dB  |
| Peaking | 2555 Hz  | 2.24 | -6.9 dB  |
| Peaking | 15333 Hz | 4.37 | -5.4 dB  |
| Peaking | 738 Hz   | 2.01 | 1.7 dB   |
| Peaking | 3692 Hz  | 4.31 | 3.4 dB   |
| Peaking | 4823 Hz  | 2.31 | -5.1 dB  |
| Peaking | 6453 Hz  | 3.84 | 5.3 dB   |
| Peaking | 18048 Hz | 3.94 | 0.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20NE700M%202013/NuForce%20NE700M%202013.png)
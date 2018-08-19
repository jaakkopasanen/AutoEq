# Beyerdynamic T70 250 Ohm sn01111

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 4.6; 23 4.5; 25 4.3; 26 4.2; 28 4.0; 30 3.8; 32 3.7; 35 3.5; 37 3.4; 40 3.2; 42 3.1; 45 2.9; 49 2.7; 52 2.6; 56 2.5; 59 2.3; 64 2.1; 68 2.0; 73 1.9; 78 1.6; 83 1.5; 89 1.4; 95 1.2; 102 1.1; 109 0.9; 117 0.6; 125 -0.0; 134 -0.6; 143 -1.0; 153 -1.1; 164 -0.3; 175 -0.3; 188 -0.8; 201 -0.7; 215 -0.5; 230 -0.2; 246 -0.0; 263 0.0; 282 0.1; 301 0.1; 323 -0.1; 345 -0.2; 369 -0.4; 395 -0.5; 423 -0.4; 452 0.3; 484 0.2; 518 0.4; 554 0.6; 593 0.6; 635 0.4; 679 0.3; 726 0.2; 777 0.3; 832 0.2; 890 0.1; 952 0.0; 1019 0.1; 1090 0.1; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.5; 1636 -0.4; 1751 0.1; 1873 0.8; 2004 1.5; 2145 2.7; 2295 3.8; 2455 4.4; 2627 4.1; 2811 3.9; 3008 4.1; 3219 4.1; 3444 3.9; 3685 5.2; 3943 6.0; 4219 5.5; 4514 4.7; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.8; 7249 -1.5; 7756 -5.0; 8299 -7.5; 8880 -8.4; 9502 -7.5; 10167 -5.0; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999571206119dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sn01111 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.56 | 4.4 dB   |
| Peaking | 2488 Hz  | 3.73 | 3.6 dB   |
| Peaking | 3917 Hz  | 2.07 | 4.5 dB   |
| Peaking | 5974 Hz  | 2.25 | 7.2 dB   |
| Peaking | 8628 Hz  | 2.69 | -11.0 dB |
| Peaking | 150 Hz   | 3.88 | -1.5 dB  |
| Peaking | 396 Hz   | 3.38 | -0.7 dB  |
| Peaking | 551 Hz   | 2.46 | 0.6 dB   |
| Peaking | 1536 Hz  | 3.86 | -1.1 dB  |
| Peaking | 11556 Hz | 6.21 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sn01111/Beyerdynamic%20T70%20250%20Ohm%20sn01111.png)
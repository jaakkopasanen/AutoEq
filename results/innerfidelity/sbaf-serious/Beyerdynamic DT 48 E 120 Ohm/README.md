# Beyerdynamic DT 48 E 120 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 2.7; 73 -3.8; 78 -7.1; 83 -6.3; 89 -4.0; 95 -2.8; 102 -3.9; 109 -4.2; 117 -3.7; 125 -3.3; 134 -2.9; 143 -2.5; 153 -1.9; 164 -1.6; 175 -2.7; 188 -2.2; 201 -1.9; 215 -1.5; 230 -1.0; 246 -0.7; 263 -0.2; 282 0.3; 301 0.8; 323 1.1; 345 1.4; 369 1.6; 395 2.1; 423 2.8; 452 3.4; 484 4.0; 518 4.7; 554 5.6; 593 6.0; 635 6.0; 679 5.5; 726 4.6; 777 3.5; 832 2.3; 890 1.6; 952 0.9; 1019 -0.4; 1090 -1.8; 1167 -3.2; 1248 -3.9; 1336 -4.4; 1429 -5.0; 1529 -5.5; 1636 -6.3; 1751 -6.5; 1873 -6.2; 2004 -6.0; 2145 -5.5; 2295 -4.1; 2455 -2.0; 2627 0.2; 2811 1.6; 3008 2.1; 3219 2.4; 3444 3.5; 3685 4.7; 3943 6.0; 4219 6.1; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.6; 7249 -1.0; 7756 -5.6; 8299 -8.3; 8880 -7.6; 9502 -4.4; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.3; 15258 -5.6; 16326 -9.4; 17469 -11.3; 18692 -9.9; 20000 -4.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.290266020691886dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E 120 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.58 | 7.5 dB   |
| Peaking | 1800 Hz  | 1.05 | -17.6 dB |
| Peaking | 4215 Hz  | 0.15 | 11.3 dB  |
| Peaking | 8498 Hz  | 2.88 | -16.7 dB |
| Peaking | 17416 Hz | 0.95 | -16.4 dB |
| Peaking | 63 Hz    | 2.31 | 7.6 dB   |
| Peaking | 78 Hz    | 4.32 | -10.7 dB |
| Peaking | 114 Hz   | 2.24 | -3.9 dB  |
| Peaking | 193 Hz   | 1.64 | -2.5 dB  |
| Peaking | 599 Hz   | 3.08 | 4.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20120%20Ohm/Beyerdynamic%20DT%2048%20E%20120%20Ohm.png)
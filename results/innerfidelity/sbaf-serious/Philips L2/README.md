# Philips L2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.5; 22 -4.1; 23 -4.4; 25 -4.8; 26 -4.9; 28 -5.2; 30 -5.4; 32 -5.6; 35 -5.8; 37 -5.8; 40 -5.9; 42 -6.0; 45 -6.0; 49 -5.9; 52 -5.8; 56 -5.7; 59 -5.6; 64 -5.4; 68 -5.2; 73 -4.9; 78 -4.8; 83 -4.6; 89 -4.4; 95 -4.4; 102 -4.5; 109 -4.6; 117 -4.9; 125 -5.3; 134 -5.3; 143 -5.0; 153 -4.8; 164 -4.2; 175 -4.1; 188 -4.2; 201 -4.1; 215 -3.8; 230 -3.5; 246 -3.4; 263 -3.2; 282 -2.8; 301 -2.4; 323 -2.2; 345 -1.9; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.7; 484 -0.5; 518 -0.2; 554 0.3; 593 0.8; 635 1.1; 679 1.1; 726 1.0; 777 0.9; 832 0.6; 890 0.2; 952 0.0; 1019 -0.1; 1090 0.0; 1167 0.3; 1248 -0.7; 1336 -2.1; 1429 -3.5; 1529 -4.8; 1636 -5.9; 1751 -6.3; 1873 -6.7; 2004 -6.8; 2145 -6.5; 2295 -6.4; 2455 -6.3; 2627 -5.5; 2811 -4.9; 3008 -3.9; 3219 -2.7; 3444 -1.5; 3685 -0.9; 3943 0.2; 4219 1.6; 4514 3.1; 4830 4.3; 5168 5.5; 5530 4.1; 5917 0.4; 6331 -1.7; 6775 -2.7; 7249 -3.0; 7756 -2.3; 8299 -1.7; 8880 -1.1; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.7; 18692 -3.2; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips L2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 5 Hz     | 1.29 | -3.0 dB |
| Peaking | 40 Hz    | 0.5  | -5.7 dB |
| Peaking | 165 Hz   | 0.96 | -3.6 dB |
| Peaking | 2137 Hz  | 1.59 | -7.5 dB |
| Peaking | 4983 Hz  | 5.03 | 6.7 dB  |
| Peaking | 679 Hz   | 3.15 | 1.6 dB  |
| Peaking | 1326 Hz  | 1.44 | 2.6 dB  |
| Peaking | 1551 Hz  | 3.08 | -3.8 dB |
| Peaking | 7207 Hz  | 4.23 | -3.5 dB |
| Peaking | 19008 Hz | 2.27 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20L2/Philips%20L2.png)
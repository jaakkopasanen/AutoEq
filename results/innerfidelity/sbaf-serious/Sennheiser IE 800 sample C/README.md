# Sennheiser IE 800 sample C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.6; 22 -2.8; 23 -2.8; 25 -2.9; 26 -3.0; 28 -3.0; 30 -3.1; 32 -3.1; 35 -3.2; 37 -3.2; 40 -3.3; 42 -3.4; 45 -3.5; 49 -3.5; 52 -3.6; 56 -3.7; 59 -3.8; 64 -3.9; 68 -4.0; 73 -4.1; 78 -4.3; 83 -4.4; 89 -4.5; 95 -4.6; 102 -4.7; 109 -4.6; 117 -4.6; 125 -4.6; 134 -4.5; 143 -4.5; 153 -4.4; 164 -4.3; 175 -4.1; 188 -3.9; 201 -3.7; 215 -3.5; 230 -3.2; 246 -3.0; 263 -2.8; 282 -2.4; 301 -2.2; 323 -1.9; 345 -1.6; 369 -1.4; 395 -1.2; 423 -0.8; 452 -0.5; 484 -0.4; 518 -0.2; 554 0.2; 593 0.5; 635 0.6; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.4; 1429 -0.4; 1529 -0.7; 1636 -0.6; 1751 -0.2; 1873 0.6; 2004 1.6; 2145 2.8; 2295 4.0; 2455 5.7; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.5; 5168 4.4; 5530 2.5; 5917 1.6; 6331 4.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -2.7; 9502 -5.6; 10167 -7.2; 10879 -6.0; 11640 -2.4; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999993319dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.31 | -3.1 dB |
| Peaking | 150 Hz   | 0.73 | -3.0 dB |
| Peaking | 2674 Hz  | 3.44 | 4.1 dB  |
| Peaking | 4251 Hz  | 1.21 | 6.0 dB  |
| Peaking | 10163 Hz | 3.76 | -8.7 dB |
| Peaking | 684 Hz   | 2.2  | 1.1 dB  |
| Peaking | 1535 Hz  | 2.89 | -1.7 dB |
| Peaking | 5789 Hz  | 7.85 | -2.6 dB |
| Peaking | 6467 Hz  | 8.2  | 3.6 dB  |
| Peaking | 24000 Hz | 1.51 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20C/Sennheiser%20IE%20800%20sample%20C.png)
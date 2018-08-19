# Sennheiser IE 800 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.8; 22 -4.9; 23 -5.0; 25 -5.0; 26 -5.1; 28 -5.1; 30 -5.2; 32 -5.2; 35 -5.2; 37 -5.3; 40 -5.3; 42 -5.3; 45 -5.3; 49 -5.3; 52 -5.3; 56 -5.3; 59 -5.3; 64 -5.3; 68 -5.3; 73 -5.4; 78 -5.4; 83 -5.4; 89 -5.5; 95 -5.5; 102 -5.5; 109 -5.3; 117 -5.2; 125 -5.1; 134 -5.0; 143 -4.9; 153 -4.7; 164 -4.5; 175 -4.3; 188 -4.0; 201 -3.9; 215 -3.6; 230 -3.3; 246 -3.0; 263 -2.8; 282 -2.5; 301 -2.2; 323 -1.9; 345 -1.6; 369 -1.4; 395 -1.2; 423 -0.8; 452 -0.6; 484 -0.5; 518 -0.3; 554 0.1; 593 0.4; 635 0.5; 679 0.6; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.6; 1429 -0.8; 1529 -0.9; 1636 -0.8; 1751 -0.4; 1873 0.3; 2004 1.1; 2145 2.2; 2295 3.4; 2455 4.8; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 3.5; 4830 2.0; 5168 1.5; 5530 1.0; 5917 3.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -2.7; 10167 -3.1; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999979698dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.27 | -5.0 dB |
| Peaking | 150 Hz  | 0.74 | -2.7 dB |
| Peaking | 3286 Hz | 1.64 | 7.0 dB  |
| Peaking | 6416 Hz | 7.08 | 5.0 dB  |
| Peaking | 9886 Hz | 4.29 | -3.7 dB |
| Peaking | 722 Hz  | 1.96 | 1.2 dB  |
| Peaking | 1586 Hz | 2.02 | -1.9 dB |
| Peaking | 2560 Hz | 3.96 | 2.5 dB  |
| Peaking | 3872 Hz | 1.66 | -2.1 dB |
| Peaking | 4068 Hz | 5.17 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20A/Sennheiser%20IE%20800%20sample%20A.png)
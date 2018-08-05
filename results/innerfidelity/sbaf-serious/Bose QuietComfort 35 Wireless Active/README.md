# Bose QuietComfort 35 Wireless Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 -5.5; 22 -4.7; 23 -4.4; 25 -3.8; 26 -3.6; 28 -3.3; 30 -3.1; 32 -2.9; 35 -2.9; 37 -2.8; 40 -2.8; 42 -2.7; 45 -2.6; 49 -2.4; 52 -2.3; 56 -2.1; 59 -1.9; 64 -1.6; 68 -1.4; 73 -1.3; 78 -1.3; 83 -1.3; 89 -1.4; 95 -1.6; 102 -1.7; 109 -1.8; 117 -1.9; 125 -2.0; 134 -2.1; 143 -2.0; 153 -1.9; 164 -1.7; 175 -1.4; 188 -1.5; 201 -1.5; 215 -1.2; 230 -1.1; 246 -0.9; 263 -0.7; 282 -0.4; 301 -0.3; 323 -0.1; 345 0.1; 369 0.3; 395 0.4; 423 0.6; 452 0.8; 484 0.7; 518 0.7; 554 0.9; 593 1.0; 635 0.9; 679 0.7; 726 0.5; 777 0.5; 832 0.3; 890 0.0; 952 -0.1; 1019 0.1; 1090 0.4; 1167 1.2; 1248 2.0; 1336 2.2; 1429 2.6; 1529 3.1; 1636 2.1; 1751 1.7; 1873 1.4; 2004 0.1; 2145 -0.9; 2295 -1.3; 2455 -1.5; 2627 -2.5; 2811 -2.6; 3008 -1.9; 3219 -0.6; 3444 0.6; 3685 -0.9; 3943 -2.3; 4219 -2.3; 4514 -1.8; 4830 -0.2; 5168 3.2; 5530 5.5; 5917 -0.1; 6331 -1.1; 6775 0.5; 7249 1.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 8 Hz    |  0.07 | -3.0 dB |
| Peaking | 1494 Hz |  2.3  | 3.1 dB  |
| Peaking | 2636 Hz |  3.4  | -2.9 dB |
| Peaking | 4242 Hz |  5.42 | -2.7 dB |
| Peaking | 5418 Hz | 10.7  | 6.7 dB  |
| Peaking | 19 Hz   |  1.84 | -2.9 dB |
| Peaking | 73 Hz   |  1.44 | 1.3 dB  |
| Peaking | 148 Hz  |  1.07 | -0.9 dB |
| Peaking | 490 Hz  |  1.63 | 1.1 dB  |
| Peaking | 2126 Hz |  7.65 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wireless%20Active/Bose%20QuietComfort%2035%20Wireless%20Active.png)
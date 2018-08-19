# Techfusion Ecoofers

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -14.9; 22 -14.9; 23 -14.9; 25 -14.9; 26 -15.0; 28 -15.0; 30 -15.0; 32 -15.0; 35 -15.0; 37 -15.0; 40 -14.9; 42 -14.9; 45 -14.9; 49 -14.9; 52 -14.9; 56 -14.9; 59 -14.9; 64 -14.9; 68 -14.9; 73 -14.9; 78 -14.9; 83 -14.9; 89 -15.0; 95 -15.0; 102 -14.9; 109 -14.6; 117 -14.5; 125 -14.4; 134 -14.2; 143 -14.0; 153 -13.8; 164 -13.4; 175 -13.1; 188 -12.7; 201 -12.3; 215 -11.9; 230 -11.4; 246 -11.0; 263 -10.6; 282 -9.9; 301 -9.5; 323 -8.9; 345 -8.3; 369 -7.7; 395 -7.2; 423 -6.4; 452 -5.8; 484 -5.3; 518 -4.7; 554 -3.9; 593 -3.2; 635 -2.5; 679 -2.1; 726 -1.3; 777 -0.6; 832 -0.5; 890 -0.3; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.9; 1751 -1.9; 1873 -2.8; 2004 -2.8; 2145 -2.7; 2295 -2.6; 2455 -2.5; 2627 -2.9; 2811 -3.0; 3008 -3.3; 3219 -1.9; 3444 0.3; 3685 1.2; 3943 1.0; 4219 -0.2; 4514 -1.2; 4830 -1.6; 5168 -1.8; 5530 -2.5; 5917 -4.1; 6331 -5.3; 6775 -4.3; 7249 -2.6; 7756 -0.7; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.4; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.0; 16326 -1.4; 17469 -2.8; 18692 -1.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3752381134001737dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Techfusion Ecoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.09 | -15.4 dB |
| Peaking | 1279 Hz  | 0.33 | 7.1 dB   |
| Peaking | 2216 Hz  | 0.99 | -7.7 dB  |
| Peaking | 6296 Hz  | 3.17 | -6.1 dB  |
| Peaking | 24000 Hz | 2.15 | 0.1 dB   |
| Peaking | 3062 Hz  | 4.7  | -3.7 dB  |
| Peaking | 3651 Hz  | 1.95 | 3.3 dB   |
| Peaking | 4538 Hz  | 3.65 | -2.5 dB  |
| Peaking | 17657 Hz | 2.9  | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Techfusion%20Ecoofers/Techfusion%20Ecoofers.png)
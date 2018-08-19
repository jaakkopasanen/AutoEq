# Sennheiser HD 580 (HD600 headband)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.6; 40 5.1; 42 4.8; 45 4.4; 49 4.0; 52 3.7; 56 3.5; 59 3.3; 64 2.8; 68 2.3; 73 2.0; 78 1.8; 83 1.6; 89 0.9; 95 0.4; 102 0.0; 109 -0.2; 117 -0.4; 125 -0.7; 134 -0.9; 143 -1.0; 153 -1.2; 164 -1.2; 175 -1.0; 188 -1.2; 201 -1.2; 215 -1.1; 230 -1.1; 246 -0.9; 263 -0.9; 282 -0.7; 301 -0.6; 323 -0.5; 345 -0.4; 369 -0.2; 395 -0.2; 423 0.0; 452 0.1; 484 -0.0; 518 -0.0; 554 0.1; 593 0.4; 635 0.4; 679 0.2; 726 0.2; 777 0.2; 832 0.0; 890 -0.2; 952 -0.2; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -0.8; 1336 -1.3; 1429 -1.6; 1529 -1.9; 1636 -2.2; 1751 -2.3; 1873 -2.1; 2004 -1.9; 2145 -1.7; 2295 -1.5; 2455 -1.4; 2627 -1.3; 2811 -1.4; 3008 -1.3; 3219 -1.6; 3444 -1.9; 3685 -1.4; 3943 -0.7; 4219 -0.7; 4514 -1.3; 4830 -0.7; 5168 1.1; 5530 2.6; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 580 (HD600 headband) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.48 | 6.3 dB  |
| Peaking | 149 Hz  | 0.91 | -2.0 dB |
| Peaking | 1717 Hz | 2.32 | -1.9 dB |
| Peaking | 4684 Hz | 0.71 | -2.0 dB |
| Peaking | 6187 Hz | 3.48 | 7.6 dB  |
| Peaking | 652 Hz  | 2.34 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20580%20(HD600%20headband)/Sennheiser%20HD%20580%20(HD600%20headband).png)
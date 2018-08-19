# Polk Hinge

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 10 -84; 20 -11.9; 22 -12.2; 23 -12.3; 25 -12.5; 26 -12.6; 28 -12.7; 30 -12.7; 32 -12.8; 35 -12.9; 37 -12.9; 40 -12.9; 42 -13.0; 45 -13.0; 49 -13.0; 52 -13.1; 56 -13.2; 59 -13.3; 64 -13.3; 68 -13.3; 73 -13.3; 78 -13.4; 83 -13.5; 89 -13.6; 95 -14.0; 102 -14.3; 109 -14.4; 117 -14.9; 125 -15.1; 134 -15.2; 143 -15.4; 153 -15.1; 164 -14.6; 175 -14.5; 188 -14.0; 201 -13.2; 215 -12.3; 230 -11.2; 246 -10.2; 263 -9.1; 282 -8.1; 301 -8.2; 323 -8.4; 345 -8.1; 369 -8.0; 395 -8.1; 423 -8.3; 452 -8.5; 484 -8.5; 518 -8.3; 554 -7.8; 593 -7.0; 635 -6.3; 679 -5.9; 726 -5.1; 777 -3.9; 832 -2.9; 890 -1.7; 952 -0.6; 1019 0.1; 1090 -0.5; 1167 -2.3; 1248 -4.2; 1336 -5.5; 1429 -6.7; 1529 -7.8; 1636 -7.7; 1751 -6.8; 1873 -6.9; 2004 -8.2; 2145 -8.0; 2295 -6.7; 2455 -5.5; 2627 -4.6; 2811 -3.8; 3008 -3.5; 3219 -3.7; 3444 -2.9; 3685 -1.3; 3943 -0.9; 4219 -3.0; 4514 -5.1; 4830 -5.0; 5168 -2.6; 5530 -0.8; 5917 -0.3; 6331 -1.3; 6775 -3.7; 7249 -4.6; 7756 -3.6; 8299 -0.9; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.19835227774535663dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Hinge ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.28 | -11.4 dB |
| Peaking | 161 Hz   | 0.78 | -9.8 dB  |
| Peaking | 498 Hz   | 1.91 | -5.6 dB  |
| Peaking | 2008 Hz  | 1.15 | -7.5 dB  |
| Peaking | 18 Hz    | 1.05 | -2.0 dB  |
| Peaking | 1037 Hz  | 5.08 | 4.0 dB   |
| Peaking | 1474 Hz  | 5.37 | -2.3 dB  |
| Peaking | 7245 Hz  | 5.61 | -4.6 dB  |
| Peaking | 24000 Hz | 2.41 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Hinge/Polk%20Hinge.png)
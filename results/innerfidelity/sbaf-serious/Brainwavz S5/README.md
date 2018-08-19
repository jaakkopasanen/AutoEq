# Brainwavz S5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 10 -84; 20 -9.1; 22 -9.2; 23 -9.3; 25 -9.4; 26 -9.4; 28 -9.5; 30 -9.6; 32 -9.6; 35 -9.7; 37 -9.7; 40 -9.8; 42 -9.8; 45 -9.9; 49 -10.0; 52 -10.0; 56 -10.1; 59 -10.1; 64 -10.2; 68 -10.3; 73 -10.4; 78 -10.5; 83 -10.6; 89 -10.7; 95 -10.8; 102 -10.8; 109 -10.6; 117 -10.6; 125 -10.5; 134 -10.4; 143 -10.3; 153 -10.1; 164 -9.9; 175 -9.6; 188 -9.3; 201 -9.0; 215 -8.6; 230 -8.3; 246 -7.9; 263 -7.5; 282 -7.0; 301 -6.6; 323 -6.1; 345 -5.6; 369 -5.2; 395 -4.7; 423 -4.2; 452 -3.7; 484 -3.4; 518 -2.9; 554 -2.3; 593 -1.6; 635 -1.2; 679 -0.9; 726 -0.5; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.2; 1167 0.3; 1248 0.4; 1336 0.0; 1429 -0.2; 1529 -0.1; 1636 -0.1; 1751 0.0; 1873 0.5; 2004 0.8; 2145 1.2; 2295 1.5; 2455 2.1; 2627 2.1; 2811 1.8; 3008 1.5; 3219 0.9; 3444 -0.4; 3685 -2.3; 3943 -4.0; 4219 -6.3; 4514 -7.9; 4830 -9.2; 5168 -10.9; 5530 -11.9; 5917 -9.5; 6331 -6.8; 6775 -4.4; 7249 -3.4; 7756 -4.4; 8299 -6.9; 8880 -9.0; 9502 -8.0; 10167 -3.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -0.5; 14260 -4.6; 15258 -6.1; 16326 -4.3; 17469 -2.6; 18692 -2.5; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.30956013592939dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.26 | -9.2 dB  |
| Peaking | 140 Hz   | 0.73 | -5.6 dB  |
| Peaking | 294 Hz   | 1.28 | -3.1 dB  |
| Peaking | 5368 Hz  | 2.79 | -11.2 dB |
| Peaking | 15822 Hz | 0.33 | -3.3 dB  |
| Peaking | 2879 Hz  | 1.47 | 3.4 dB   |
| Peaking | 4256 Hz  | 2.99 | -3.6 dB  |
| Peaking | 9124 Hz  | 3.34 | -10.9 dB |
| Peaking | 11467 Hz | 0.91 | 6.5 dB   |
| Peaking | 15012 Hz | 2.79 | -6.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S5/Brainwavz%20S5.png)
# Beats Mixr 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.6; 22 -1.1; 23 -1.4; 25 -1.8; 26 -2.0; 28 -2.2; 30 -2.4; 32 -2.6; 35 -2.8; 37 -2.9; 40 -3.1; 42 -3.1; 45 -3.2; 49 -3.3; 52 -3.5; 56 -3.6; 59 -3.7; 64 -3.9; 68 -4.0; 73 -4.2; 78 -4.2; 83 -4.3; 89 -4.6; 95 -4.9; 102 -5.1; 109 -5.2; 117 -4.9; 125 -4.8; 134 -5.1; 143 -5.3; 153 -5.6; 164 -5.4; 175 -5.3; 188 -5.6; 201 -5.6; 215 -5.5; 230 -5.2; 246 -4.6; 263 -3.5; 282 -2.3; 301 -1.3; 323 -0.8; 345 0.6; 369 2.2; 395 3.1; 423 4.2; 452 4.2; 484 3.4; 518 3.1; 554 2.5; 593 2.2; 635 1.7; 679 1.2; 726 0.8; 777 0.7; 832 0.4; 890 0.1; 952 0.1; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.6; 1429 0.4; 1529 0.2; 1636 -0.1; 1751 -0.2; 1873 -0.2; 2004 -0.4; 2145 -0.7; 2295 -1.0; 2455 -1.1; 2627 -1.5; 2811 -1.6; 3008 -1.0; 3219 -0.4; 3444 0.8; 3685 2.2; 3943 3.1; 4219 4.2; 4514 2.6; 4830 0.5; 5168 3.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.084225018767812dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Mixr 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.93 | -1.7 dB |
| Peaking | 104 Hz  | 0.61 | -3.9 dB |
| Peaking | 219 Hz  | 1.2  | -4.1 dB |
| Peaking | 434 Hz  | 1.7  | 5.8 dB  |
| Peaking | 5830 Hz | 3.05 | 6.5 dB  |
| Peaking | 2794 Hz | 2.35 | -2.4 dB |
| Peaking | 4258 Hz | 2.78 | 4.3 dB  |
| Peaking | 4802 Hz | 7.93 | -4.8 dB |
| Peaking | 8119 Hz | 3.61 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Mixr%202014/Beats%20Mixr%202014.png)
# Meze 11 Deco

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -11.7; 22 -11.7; 23 -11.7; 25 -11.7; 26 -11.8; 28 -11.8; 30 -11.8; 32 -11.9; 35 -11.9; 37 -11.9; 40 -11.9; 42 -11.9; 45 -11.9; 49 -12.0; 52 -12.0; 56 -12.1; 59 -12.1; 64 -12.2; 68 -12.3; 73 -12.4; 78 -12.5; 83 -12.6; 89 -12.6; 95 -12.8; 102 -12.7; 109 -12.6; 117 -12.5; 125 -12.5; 134 -12.4; 143 -12.3; 153 -12.1; 164 -11.9; 175 -11.6; 188 -11.3; 201 -11.0; 215 -10.6; 230 -10.1; 246 -9.8; 263 -9.4; 282 -8.9; 301 -8.5; 323 -8.0; 345 -7.4; 369 -7.0; 395 -6.5; 423 -5.8; 452 -5.3; 484 -4.9; 518 -4.4; 554 -3.8; 593 -3.2; 635 -2.2; 679 -1.9; 726 -1.5; 777 -0.5; 832 -0.1; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.4; 1336 0.4; 1429 0.1; 1529 -0.5; 1636 -1.9; 1751 -3.5; 1873 -4.4; 2004 -4.1; 2145 -3.2; 2295 -1.9; 2455 0.0; 2627 1.6; 2811 3.4; 3008 5.4; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 4.9; 4830 4.2; 5168 3.8; 5530 2.4; 5917 -1.0; 6331 -6.6; 6775 -6.6; 7249 -2.5; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999999703621dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Deco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.19 | -10.7 dB |
| Peaking | 177 Hz  | 0.4  | -9.0 dB  |
| Peaking | 2050 Hz | 1.72 | -13.0 dB |
| Peaking | 2772 Hz | 0.57 | 10.2 dB  |
| Peaking | 6574 Hz | 4.66 | -11.7 dB |
| Peaking | 809 Hz  | 7.01 | 1.0 dB   |
| Peaking | 2693 Hz | 5.79 | -1.6 dB  |
| Peaking | 3004 Hz | 5.01 | 0.9 dB   |
| Peaking | 7351 Hz | 0.82 | 1.3 dB   |
| Peaking | 9741 Hz | 1    | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Deco/Meze%2011%20Deco.png)
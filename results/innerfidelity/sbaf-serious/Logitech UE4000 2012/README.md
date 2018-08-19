# Logitech UE4000 2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.3; 22 0.1; 23 0.0; 25 -0.1; 26 -0.1; 28 -0.2; 30 -0.3; 32 -0.4; 35 -0.5; 37 -0.6; 40 -0.6; 42 -0.7; 45 -0.7; 49 -0.8; 52 -0.8; 56 -0.9; 59 -1.0; 64 -1.1; 68 -1.2; 73 -1.5; 78 -1.7; 83 -1.9; 89 -2.0; 95 -2.0; 102 -2.0; 109 -2.1; 117 -2.8; 125 -2.9; 134 -2.4; 143 -2.2; 153 -2.4; 164 -2.5; 175 -1.9; 188 -2.3; 201 -2.5; 215 -2.3; 230 -1.9; 246 -1.3; 263 -0.6; 282 0.3; 301 0.8; 323 1.5; 345 2.4; 369 2.6; 395 2.5; 423 2.6; 452 2.4; 484 1.9; 518 1.6; 554 1.4; 593 1.2; 635 0.8; 679 0.2; 726 -0.1; 777 -0.0; 832 -0.2; 890 -0.2; 952 0.3; 1019 -0.1; 1090 0.1; 1167 0.4; 1248 0.9; 1336 1.3; 1429 1.7; 1529 2.3; 1636 2.9; 1751 3.7; 1873 4.8; 2004 5.8; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999979dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE4000 2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 1.36 | 0.3 dB  |
| Peaking | 224 Hz  | 3.41 | -1.0 dB |
| Peaking | 354 Hz  | 0.26 | -5.1 dB |
| Peaking | 397 Hz  | 0.89 | 7.5 dB  |
| Peaking | 2996 Hz | 0.6  | 7.5 dB  |
| Peaking | 12 Hz   | 1.22 | 0.4 dB  |
| Peaking | 2077 Hz | 2.69 | 2.6 dB  |
| Peaking | 2364 Hz | 0.93 | -1.6 dB |
| Peaking | 6177 Hz | 1.91 | 5.8 dB  |
| Peaking | 7520 Hz | 1.43 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE4000%202012/Logitech%20UE4000%202012.png)
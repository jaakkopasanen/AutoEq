# Logitech UE 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.3; 22 1.2; 23 1.1; 25 1.1; 26 1.0; 28 1.0; 30 0.9; 32 0.8; 35 0.7; 37 0.6; 40 0.5; 42 0.5; 45 0.4; 49 0.2; 52 0.1; 56 -0.2; 59 -0.4; 64 -0.7; 68 -0.9; 73 -1.2; 78 -1.4; 83 -1.7; 89 -2.0; 95 -2.3; 102 -2.6; 109 -2.7; 117 -2.9; 125 -3.2; 134 -3.4; 143 -3.6; 153 -3.8; 164 -3.9; 175 -4.0; 188 -4.2; 201 -4.3; 215 -4.3; 230 -4.4; 246 -4.5; 263 -4.5; 282 -4.5; 301 -4.6; 323 -4.7; 345 -4.7; 369 -4.8; 395 -4.9; 423 -4.9; 452 -5.0; 484 -5.1; 518 -5.1; 554 -5.0; 593 -4.6; 635 -4.1; 679 -3.6; 726 -2.7; 777 -1.7; 832 -1.0; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.0; 1167 -0.0; 1248 -0.2; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.9; 1751 -2.2; 1873 -2.3; 2004 -2.4; 2145 -2.5; 2295 -2.2; 2455 -1.2; 2627 0.5; 2811 3.0; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 5.3; 4830 5.5; 5168 5.7; 5530 5.5; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.5; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715981dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.88 | 1.3 dB  |
| Peaking | 288 Hz  | 0.45 | -5.1 dB |
| Peaking | 2254 Hz | 2.2  | -5.7 dB |
| Peaking | 3349 Hz | 1.38 | 7.7 dB  |
| Peaking | 5782 Hz | 3.29 | 4.5 dB  |
| Peaking | 283 Hz  | 2.14 | 0.8 dB  |
| Peaking | 616 Hz  | 1.45 | -3.0 dB |
| Peaking | 880 Hz  | 1.17 | 2.9 dB  |
| Peaking | 1631 Hz | 3.41 | -1.4 dB |
| Peaking | 9230 Hz | 3.99 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%20900/Logitech%20UE%20900.png)
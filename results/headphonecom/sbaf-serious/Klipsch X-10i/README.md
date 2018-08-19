# Klipsch X-10i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.6; 22 -1.7; 23 -1.7; 25 -1.8; 26 -1.8; 28 -1.9; 30 -2.0; 32 -2.0; 35 -2.0; 37 -2.1; 40 -2.1; 42 -2.2; 45 -2.3; 49 -2.5; 52 -2.6; 56 -2.8; 59 -2.9; 64 -3.2; 68 -3.4; 73 -3.5; 78 -3.6; 83 -3.8; 89 -4.0; 95 -4.2; 102 -4.3; 109 -4.3; 117 -4.5; 125 -4.6; 134 -4.7; 143 -4.9; 153 -4.8; 164 -5.0; 175 -4.9; 188 -4.8; 201 -4.8; 215 -4.6; 230 -4.5; 246 -4.4; 263 -4.2; 282 -4.0; 301 -3.8; 323 -3.5; 345 -3.2; 369 -2.9; 395 -2.6; 423 -2.3; 452 -2.1; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.8; 635 -0.4; 679 -0.1; 726 0.1; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.6; 1529 -1.9; 1636 -1.9; 1751 -1.8; 1873 -1.6; 2004 -1.4; 2145 -1.3; 2295 -1.2; 2455 -1.2; 2627 -1.3; 2811 -1.4; 3008 -0.5; 3219 1.7; 3444 4.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.8; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999813384082dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X-10i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.34 | -1.9 dB |
| Peaking | 150 Hz  | 0.75 | -3.4 dB |
| Peaking | 290 Hz  | 1.33 | -2.0 dB |
| Peaking | 2558 Hz | 1.12 | -4.3 dB |
| Peaking | 4322 Hz | 1.25 | 8.5 dB  |
| Peaking | 823 Hz  | 2.8  | 1.0 dB  |
| Peaking | 1518 Hz | 5.06 | -1.1 dB |
| Peaking | 4646 Hz | 5.45 | -2.1 dB |
| Peaking | 6317 Hz | 1.84 | 4.4 dB  |
| Peaking | 7602 Hz | 1.73 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20X-10i/Klipsch%20X-10i.png)
# Logitech UE 6000 passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.1; 23 -2.1; 25 -2.2; 26 -2.2; 28 -2.3; 30 -2.3; 32 -2.3; 35 -2.3; 37 -2.2; 40 -2.2; 42 -2.1; 45 -2.1; 49 -2.0; 52 -1.9; 56 -1.8; 59 -1.7; 64 -1.7; 68 -1.6; 73 -1.6; 78 -1.5; 83 -1.5; 89 -1.4; 95 -1.5; 102 -1.4; 109 -1.3; 117 -1.6; 125 -1.6; 134 -1.5; 143 -1.7; 153 -1.6; 164 -0.6; 175 -0.2; 188 -0.8; 201 -0.9; 215 -0.6; 230 -0.1; 246 0.3; 263 0.8; 282 1.4; 301 1.8; 323 2.0; 345 2.3; 369 2.5; 395 2.5; 423 2.6; 452 2.5; 484 2.1; 518 1.8; 554 1.6; 593 1.5; 635 1.0; 679 0.6; 726 0.3; 777 0.3; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.4; 1336 0.5; 1429 0.7; 1529 0.9; 1636 1.4; 1751 1.9; 1873 2.7; 2004 4.0; 2145 5.1; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.4; 4514 4.7; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999268dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 6000 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.65 | -2.2 dB |
| Peaking | 409 Hz  | 0.78 | 5.9 dB  |
| Peaking | 1007 Hz | 0.1  | -3.8 dB |
| Peaking | 2835 Hz | 0.83 | 9.5 dB  |
| Peaking | 5712 Hz | 2.3  | 5.7 dB  |
| Peaking | 97 Hz   | 0.75 | 0.2 dB  |
| Peaking | 1614 Hz | 3.84 | -0.8 dB |
| Peaking | 2914 Hz | 6.06 | -1.0 dB |
| Peaking | 5815 Hz | 0.21 | 0.5 dB  |
| Peaking | 7929 Hz | 4.92 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%206000%20passive/Logitech%20UE%206000%20passive.png)
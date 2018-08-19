# Bose QuietComfort 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.3; 23 -4.4; 25 -4.6; 26 -4.7; 28 -4.7; 30 -4.7; 32 -4.7; 35 -4.6; 37 -4.6; 40 -4.4; 42 -4.4; 45 -4.3; 49 -4.2; 52 -4.1; 56 -4.1; 59 -4.0; 64 -4.1; 68 -4.2; 73 -4.2; 78 -4.3; 83 -4.5; 89 -4.6; 95 -4.8; 102 -4.8; 109 -4.8; 117 -4.9; 125 -5.0; 134 -5.0; 143 -5.0; 153 -5.0; 164 -4.8; 175 -4.6; 188 -4.5; 201 -4.2; 215 -3.9; 230 -3.6; 246 -3.2; 263 -2.8; 282 -2.5; 301 -2.2; 323 -1.9; 345 -1.5; 369 -1.2; 395 -1.0; 423 -0.7; 452 -0.6; 484 -0.6; 518 -0.5; 554 -0.3; 593 -0.2; 635 -0.3; 679 -0.5; 726 -0.5; 777 -0.5; 832 -0.2; 890 -0.0; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.7; 1429 0.0; 1529 0.9; 1636 1.1; 1751 2.2; 1873 3.5; 2004 4.6; 2145 5.5; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 5.8; 3219 5.6; 3444 4.9; 3685 3.7; 3943 2.5; 4219 1.4; 4514 2.0; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999994905dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.41 | -4.3 dB |
| Peaking | 149 Hz  | 0.7  | -4.4 dB |
| Peaking | 2605 Hz | 1.75 | 6.6 dB  |
| Peaking | 5882 Hz | 2.43 | 6.6 dB  |
| Peaking | 7915 Hz | 2.15 | -1.8 dB |
| Peaking | 1308 Hz | 3.38 | -1.6 dB |
| Peaking | 2018 Hz | 7.1  | 1.3 dB  |
| Peaking | 4117 Hz | 7.68 | -3.0 dB |
| Peaking | 4228 Hz | 2.99 | 2.5 dB  |
| Peaking | 4430 Hz | 9.85 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%203/Bose%20QuietComfort%203.png)
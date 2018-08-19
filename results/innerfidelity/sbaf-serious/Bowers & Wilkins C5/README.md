# Bowers & Wilkins C5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 10 -84; 20 -14.0; 22 -13.8; 23 -13.7; 25 -13.6; 26 -13.5; 28 -13.3; 30 -13.1; 32 -13.0; 35 -12.7; 37 -12.5; 40 -12.3; 42 -12.1; 45 -11.9; 49 -11.7; 52 -11.5; 56 -11.3; 59 -11.1; 64 -11.0; 68 -10.8; 73 -10.7; 78 -10.5; 83 -10.4; 89 -10.3; 95 -10.1; 102 -9.9; 109 -9.6; 117 -9.3; 125 -9.0; 134 -8.8; 143 -8.6; 153 -8.3; 164 -8.0; 175 -7.5; 188 -7.2; 201 -6.9; 215 -6.5; 230 -6.0; 246 -5.6; 263 -5.3; 282 -4.8; 301 -4.3; 323 -3.9; 345 -3.5; 369 -3.1; 395 -2.7; 423 -2.2; 452 -1.8; 484 -1.6; 518 -1.2; 554 -0.8; 593 -0.2; 635 0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.4; 1336 -0.7; 1429 -1.2; 1529 -1.6; 1636 -2.0; 1751 -2.3; 1873 -2.3; 2004 -2.2; 2145 -2.3; 2295 -2.5; 2455 -2.5; 2627 -2.8; 2811 -3.3; 3008 -3.6; 3219 -3.7; 3444 -3.1; 3685 -2.9; 3943 -2.8; 4219 -3.8; 4514 -4.6; 4830 -4.7; 5168 -4.1; 5530 -3.6; 5917 -2.8; 6331 -2.0; 6775 -1.1; 7249 -0.3; 7756 -0.2; 8299 -0.4; 8880 -0.6; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.2; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6989573214680428dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins C5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.6dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.58 | -10.2 dB |
| Peaking | 85 Hz   | 0.29 | -8.9 dB  |
| Peaking | 701 Hz  | 0.94 | 2.2 dB   |
| Peaking | 2620 Hz | 0.83 | -2.9 dB  |
| Peaking | 4900 Hz | 2.75 | -3.6 dB  |
| Peaking | 1692 Hz | 4.73 | -0.7 dB  |
| Peaking | 2442 Hz | 1.69 | 0.6 dB   |
| Peaking | 3094 Hz | 5.85 | -1.0 dB  |
| Peaking | 7505 Hz | 8.17 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20C5/Bowers%20&%20Wilkins%20C5.png)
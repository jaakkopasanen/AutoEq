# Philips SHE3590

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -11.2; 22 -11.1; 23 -11.1; 25 -10.9; 26 -10.8; 28 -10.7; 30 -10.5; 32 -10.3; 35 -10.1; 37 -9.9; 40 -9.7; 42 -9.5; 45 -9.3; 49 -9.1; 52 -8.9; 56 -8.7; 59 -8.6; 64 -8.4; 68 -8.2; 73 -8.1; 78 -8.0; 83 -7.9; 89 -7.8; 95 -7.6; 102 -7.4; 109 -7.1; 117 -6.9; 125 -6.7; 134 -6.5; 143 -6.2; 153 -6.0; 164 -5.7; 175 -5.3; 188 -5.1; 201 -4.8; 215 -4.4; 230 -4.0; 246 -3.7; 263 -3.4; 282 -2.9; 301 -2.7; 323 -2.3; 345 -1.9; 369 -1.6; 395 -1.3; 423 -0.9; 452 -0.6; 484 -0.4; 518 -0.2; 554 0.1; 593 0.5; 635 0.7; 679 0.5; 726 0.6; 777 0.7; 832 0.8; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.5; 1336 -2.3; 1429 -3.1; 1529 -3.9; 1636 -4.5; 1751 -5.2; 1873 -5.7; 2004 -6.3; 2145 -7.0; 2295 -8.0; 2455 -8.4; 2627 -8.2; 2811 -6.6; 3008 -3.8; 3219 -1.1; 3444 0.8; 3685 1.3; 3943 0.8; 4219 -1.0; 4514 -2.8; 4830 -4.4; 5168 -5.3; 5530 -5.0; 5917 -3.2; 6331 -1.9; 6775 -0.7; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3857840485111852dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.2  | -11.0 dB |
| Peaking | 148 Hz  | 0.88 | -3.1 dB  |
| Peaking | 2431 Hz | 1.62 | -9.4 dB  |
| Peaking | 3575 Hz | 3.09 | 5.6 dB   |
| Peaking | 5208 Hz | 3.89 | -5.4 dB  |
| Peaking | 290 Hz  | 1.61 | -0.8 dB  |
| Peaking | 870 Hz  | 0.85 | 2.1 dB   |
| Peaking | 1649 Hz | 1.3  | -2.3 dB  |
| Peaking | 2158 Hz | 3.83 | 1.7 dB   |
| Peaking | 7417 Hz | 6.23 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SHE3590/Philips%20SHE3590.png)
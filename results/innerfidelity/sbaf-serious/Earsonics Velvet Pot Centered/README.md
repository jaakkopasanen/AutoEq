# Earsonics Velvet Pot Centered

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.2; 22 -1.4; 23 -1.5; 25 -1.7; 26 -1.8; 28 -2.0; 30 -2.1; 32 -2.2; 35 -2.4; 37 -2.4; 40 -2.4; 42 -2.4; 45 -2.5; 49 -2.5; 52 -2.5; 56 -2.5; 59 -2.5; 64 -2.5; 68 -2.5; 73 -2.5; 78 -2.4; 83 -2.3; 89 -2.2; 95 -2.0; 102 -1.7; 109 -1.3; 117 -0.9; 125 -0.4; 134 0.1; 143 0.7; 153 1.4; 164 2.1; 175 3.0; 188 3.8; 201 4.5; 215 5.2; 230 5.7; 246 5.8; 263 5.7; 282 5.4; 301 4.9; 323 4.5; 345 4.0; 369 3.5; 395 3.0; 423 2.7; 452 2.3; 484 1.9; 518 1.6; 554 1.6; 593 1.6; 635 1.5; 679 1.2; 726 1.1; 777 1.1; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.3; 1429 -1.6; 1529 -1.8; 1636 -1.7; 1751 -1.2; 1873 -0.3; 2004 1.1; 2145 2.7; 2295 3.5; 2455 4.6; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.1; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999964643dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot Centered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.66 | -1.6 dB |
| Peaking | 102 Hz  | 0.61 | -3.0 dB |
| Peaking | 239 Hz  | 0.95 | 7.1 dB  |
| Peaking | 1580 Hz | 1.82 | -4.6 dB |
| Peaking | 3511 Hz | 0.78 | 7.2 dB  |
| Peaking | 1868 Hz | 8.86 | -0.6 dB |
| Peaking | 2645 Hz | 3.15 | 1.2 dB  |
| Peaking | 3447 Hz | 2.56 | -1.1 dB |
| Peaking | 6153 Hz | 2.57 | 5.2 dB  |
| Peaking | 7305 Hz | 1.42 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20Centered/Earsonics%20Velvet%20Pot%20Centered.png)
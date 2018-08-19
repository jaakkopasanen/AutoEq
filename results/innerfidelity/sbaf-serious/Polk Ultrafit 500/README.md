# Polk Ultrafit 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 5.3; 68 4.7; 73 4.1; 78 3.4; 83 2.9; 89 2.2; 95 1.6; 102 1.2; 109 0.8; 117 0.4; 125 -0.5; 134 -0.5; 143 -1.0; 153 -1.4; 164 -1.9; 175 -2.2; 188 -2.6; 201 -3.0; 215 -3.1; 230 -3.6; 246 -3.8; 263 -4.0; 282 -4.2; 301 -4.3; 323 -4.6; 345 -4.8; 369 -4.8; 395 -5.2; 423 -5.4; 452 -4.6; 484 -4.8; 518 -5.1; 554 -4.7; 593 -4.4; 635 -4.0; 679 -3.9; 726 -3.4; 777 -2.6; 832 -1.9; 890 -1.2; 952 -0.5; 1019 0.3; 1090 1.0; 1167 1.8; 1248 2.7; 1336 3.3; 1429 4.0; 1529 4.7; 1636 5.5; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Ultrafit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.44 | 6.9 dB  |
| Peaking | 469 Hz  | 0.33 | -6.3 dB |
| Peaking | 1764 Hz | 0.77 | 8.1 dB  |
| Peaking | 3945 Hz | 1.56 | 3.9 dB  |
| Peaking | 5814 Hz | 3.55 | 4.1 dB  |
| Peaking | 56 Hz   | 1.04 | -1.2 dB |
| Peaking | 59 Hz   | 2.45 | 2.0 dB  |
| Peaking | 6567 Hz | 7.92 | 2.0 dB  |
| Peaking | 7997 Hz | 2.26 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Ultrafit%20500/Polk%20Ultrafit%20500.png)
# Etymotic Mk5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.8; 59 5.6; 64 5.3; 68 5.1; 73 4.8; 78 4.5; 83 4.2; 89 3.9; 95 3.5; 102 3.2; 109 3.1; 117 2.9; 125 2.7; 134 2.5; 143 2.4; 153 2.2; 164 2.0; 175 1.9; 188 1.8; 201 1.8; 215 1.7; 230 1.7; 246 1.6; 263 1.6; 282 1.8; 301 1.8; 323 1.8; 345 1.8; 369 1.9; 395 1.8; 423 1.9; 452 2.0; 484 1.9; 518 2.0; 554 2.1; 593 2.2; 635 2.2; 679 2.0; 726 1.9; 777 1.8; 832 1.4; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -1.4; 1248 -2.0; 1336 -2.8; 1429 -3.7; 1529 -4.6; 1636 -5.3; 1751 -5.8; 1873 -6.1; 2004 -6.3; 2145 -6.3; 2295 -6.1; 2455 -5.2; 2627 -4.0; 2811 -2.8; 3008 -1.3; 3219 -0.4; 3444 -0.3; 3685 -0.8; 3943 -0.7; 4219 -0.0; 4514 1.6; 4830 2.9; 5168 3.5; 5530 3.1; 5917 2.9; 6331 3.1; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Mk5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.36 | 6.3 dB  |
| Peaking | 648 Hz  | 0.65 | 2.5 dB  |
| Peaking | 1615 Hz | 1.46 | -4.5 dB |
| Peaking | 2213 Hz | 2.22 | -4.7 dB |
| Peaking | 5608 Hz | 2.18 | 4.0 dB  |
| Peaking | 3255 Hz | 7.52 | 1.1 dB  |
| Peaking | 3938 Hz | 8    | -1.1 dB |
| Peaking | 6789 Hz | 9.18 | 2.2 dB  |
| Peaking | 7704 Hz | 2.28 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20Mk5/Etymotic%20Mk5.png)
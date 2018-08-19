# Etymotic ER-6i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 5.9; 22 5.8; 23 5.7; 25 5.6; 26 5.5; 28 5.4; 30 5.4; 32 5.3; 35 5.2; 37 5.1; 40 5.0; 42 4.9; 45 4.8; 49 4.6; 52 4.5; 56 4.3; 59 4.1; 64 3.7; 68 3.5; 73 3.2; 78 3.0; 83 2.8; 89 2.6; 95 2.4; 102 2.2; 109 2.0; 117 1.9; 125 1.6; 134 1.4; 143 1.2; 153 1.1; 164 0.9; 175 0.8; 188 0.7; 201 0.7; 215 0.6; 230 0.6; 246 0.6; 263 0.6; 282 0.6; 301 0.7; 323 0.8; 345 0.8; 369 0.8; 395 0.8; 423 0.7; 452 0.8; 484 0.8; 518 0.9; 554 1.1; 593 1.3; 635 1.2; 679 1.3; 726 1.3; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -1.9; 1429 -2.5; 1529 -3.0; 1636 -3.5; 1751 -4.1; 1873 -4.4; 2004 -4.4; 2145 -4.3; 2295 -3.9; 2455 -3.2; 2627 -2.4; 2811 -1.4; 3008 -0.1; 3219 1.4; 3444 2.5; 3685 2.8; 3943 2.0; 4219 0.8; 4514 0.2; 4830 0.9; 5168 2.8; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.018213211458009dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.35 | 3.7 dB  |
| Peaking | 2010 Hz | 1.8  | -5.0 dB |
| Peaking | 3532 Hz | 4.65 | 3.6 dB  |
| Peaking | 6002 Hz | 3.98 | 6.7 dB  |
| Peaking | 21 Hz   | 1.12 | 2.6 dB  |
| Peaking | 46 Hz   | 1.92 | 0.7 dB  |
| Peaking | 710 Hz  | 1.26 | 1.6 dB  |
| Peaking | 1365 Hz | 2.45 | -0.9 dB |
| Peaking | 8193 Hz | 5.49 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-6i/Etymotic%20ER-6i.png)
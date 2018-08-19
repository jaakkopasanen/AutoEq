# Spider realvoice

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.7; 22 -4.7; 23 -4.7; 25 -4.6; 26 -4.6; 28 -4.5; 30 -4.5; 32 -4.4; 35 -4.3; 37 -4.3; 40 -4.2; 42 -4.1; 45 -4.1; 49 -4.0; 52 -4.0; 56 -3.9; 59 -3.9; 64 -3.9; 68 -3.8; 73 -3.9; 78 -3.9; 83 -3.9; 89 -3.9; 95 -3.9; 102 -3.9; 109 -3.7; 117 -3.6; 125 -3.5; 134 -3.4; 143 -3.3; 153 -3.2; 164 -3.1; 175 -2.8; 188 -2.7; 201 -2.5; 215 -2.2; 230 -1.9; 246 -1.9; 263 -1.8; 282 -1.5; 301 -1.3; 323 -1.1; 345 -0.9; 369 -0.7; 395 -0.6; 423 -0.4; 452 -0.2; 484 -0.1; 518 0.0; 554 0.3; 593 0.5; 635 0.5; 679 0.9; 726 1.0; 777 0.7; 832 0.6; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.0; 1751 -2.0; 1873 -1.7; 2004 -1.2; 2145 -0.4; 2295 0.7; 2455 2.3; 2627 3.8; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 4.6; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678133dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider realvoice ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.2  | -4.5 dB |
| Peaking | 140 Hz  | 0.84 | -2.1 dB |
| Peaking | 1838 Hz | 1.95 | -4.1 dB |
| Peaking | 3297 Hz | 1.3  | 6.8 dB  |
| Peaking | 5794 Hz | 3.42 | 4.8 dB  |
| Peaking | 709 Hz  | 2.61 | 1.2 dB  |
| Peaking | 1397 Hz | 5.08 | -0.6 dB |
| Peaking | 8381 Hz | 3.82 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20realvoice/Spider%20realvoice.png)
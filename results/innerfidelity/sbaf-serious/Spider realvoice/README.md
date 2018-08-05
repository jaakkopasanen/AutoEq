# Spider realvoice

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.7; 22 -4.6; 23 -4.6; 25 -4.5; 26 -4.5; 28 -4.4; 30 -4.3; 32 -4.2; 35 -4.0; 37 -3.9; 40 -3.8; 42 -3.7; 45 -3.5; 49 -3.3; 52 -3.2; 56 -2.9; 59 -2.8; 64 -2.6; 68 -2.4; 73 -2.3; 78 -2.3; 83 -2.2; 89 -2.3; 95 -2.5; 102 -2.8; 109 -3.0; 117 -3.2; 125 -3.5; 134 -3.7; 143 -3.8; 153 -3.7; 164 -3.6; 175 -3.4; 188 -3.1; 201 -2.9; 215 -2.6; 230 -2.2; 246 -2.2; 263 -2.1; 282 -1.7; 301 -1.5; 323 -1.3; 345 -1.0; 369 -0.8; 395 -0.7; 423 -0.4; 452 -0.2; 484 -0.2; 518 -0.0; 554 0.2; 593 0.5; 635 0.5; 679 0.9; 726 1.0; 777 0.7; 832 0.6; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.0; 1751 -2.0; 1873 -1.7; 2004 -1.2; 2145 -0.4; 2295 0.7; 2455 2.3; 2627 3.8; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 4.6; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider realvoice ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.83 | -3.9 dB |
| Peaking | 42 Hz   | 0.97 | -2.0 dB |
| Peaking | 154 Hz  | 0.97 | -3.5 dB |
| Peaking | 3400 Hz | 2.41 | 6.4 dB  |
| Peaking | 5633 Hz | 2.66 | 5.8 dB  |
| Peaking | 720 Hz  | 2.25 | 1.3 dB  |
| Peaking | 1738 Hz | 1.88 | -2.9 dB |
| Peaking | 2736 Hz | 5.08 | 2.5 dB  |
| Peaking | 6556 Hz | 7.23 | 2.1 dB  |
| Peaking | 7809 Hz | 2.5  | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20realvoice/Spider%20realvoice.png)
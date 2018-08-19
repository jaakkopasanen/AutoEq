# Sony MDR-EX1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.6; 22 4.3; 23 4.2; 25 4.0; 26 3.9; 28 3.7; 30 3.6; 32 3.4; 35 3.3; 37 3.1; 40 3.0; 42 2.9; 45 2.7; 49 2.5; 52 2.3; 56 2.1; 59 2.0; 64 1.6; 68 1.3; 73 1.0; 78 0.8; 83 0.5; 89 0.2; 95 -0.1; 102 -0.4; 109 -0.5; 117 -0.7; 125 -1.0; 134 -1.2; 143 -1.4; 153 -1.6; 164 -1.7; 175 -1.7; 188 -1.7; 201 -1.9; 215 -1.9; 230 -1.8; 246 -1.8; 263 -1.8; 282 -1.6; 301 -1.5; 323 -1.4; 345 -1.3; 369 -1.2; 395 -1.2; 423 -0.9; 452 -0.7; 484 -0.6; 518 -0.5; 554 -0.1; 593 0.3; 635 0.5; 679 0.4; 726 0.6; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.1; 1636 -3.6; 1751 -3.8; 1873 -3.6; 2004 -3.1; 2145 -2.4; 2295 -1.3; 2455 0.3; 2627 1.7; 2811 3.1; 3008 5.1; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.0; 4219 1.8; 4514 -1.2; 4830 -5.0; 5168 -6.3; 5530 -3.7; 5917 -0.3; 6331 1.3; 6775 1.3; 7249 -1.0; 7756 -4.0; 8299 -4.8; 8880 -2.7; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999994864746dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.98 | 4.4 dB  |
| Peaking | 1835 Hz | 1.91 | -4.9 dB |
| Peaking | 3446 Hz | 2.13 | 7.9 dB  |
| Peaking | 4898 Hz | 4.62 | -3.2 dB |
| Peaking | 5133 Hz | 5.07 | -5.5 dB |
| Peaking | 61 Hz   | 1.54 | 1.2 dB  |
| Peaking | 211 Hz  | 0.62 | -2.0 dB |
| Peaking | 759 Hz  | 1.91 | 1.5 dB  |
| Peaking | 6540 Hz | 5.4  | 2.8 dB  |
| Peaking | 8107 Hz | 5.17 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)
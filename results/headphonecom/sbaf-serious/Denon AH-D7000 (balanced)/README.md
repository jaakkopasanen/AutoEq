# Denon AH-D7000 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.3; 26 4.9; 28 4.0; 30 3.1; 32 2.3; 35 1.5; 37 1.2; 40 1.1; 42 1.1; 45 0.9; 49 0.3; 52 0.1; 56 0.3; 59 0.5; 64 0.5; 68 0.3; 73 0.3; 78 0.3; 83 0.2; 89 0.3; 95 0.4; 102 0.6; 109 0.7; 117 0.8; 125 0.8; 134 0.8; 143 0.8; 153 0.9; 164 1.1; 175 1.1; 188 1.2; 201 1.3; 215 1.5; 230 1.6; 246 1.8; 263 2.0; 282 2.3; 301 2.6; 323 2.9; 345 3.1; 369 3.2; 395 3.3; 423 3.2; 452 2.8; 484 2.2; 518 1.6; 554 1.0; 593 0.6; 635 0.4; 679 0.1; 726 -0.5; 777 -0.9; 832 -0.8; 890 0.9; 952 0.4; 1019 -0.0; 1090 0.1; 1167 0.4; 1248 0.9; 1336 1.2; 1429 1.2; 1529 1.3; 1636 1.6; 1751 2.1; 1873 2.2; 2004 2.0; 2145 2.1; 2295 2.8; 2455 3.3; 2627 3.7; 2811 3.4; 3008 2.6; 3219 1.5; 3444 0.5; 3685 0.6; 3943 0.9; 4219 1.1; 4514 -0.0; 4830 -1.7; 5168 -0.8; 5530 -0.3; 5917 -2.1; 6331 -2.6; 6775 -1.8; 7249 -2.1; 7756 -0.5; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.82 | 6.4 dB  |
| Peaking | 470 Hz  |  0.7  | 4.5 dB  |
| Peaking | 678 Hz  |  1.37 | -3.9 dB |
| Peaking | 2510 Hz |  1.75 | 3.3 dB  |
| Peaking | 6338 Hz |  2.8  | -2.7 dB |
| Peaking | 1906 Hz |  2.64 | 1.0 dB  |
| Peaking | 2107 Hz |  5.38 | -1.4 dB |
| Peaking | 4795 Hz | 16.2  | -1.7 dB |
| Peaking | 8385 Hz |  6.99 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000%20(balanced)/Denon%20AH-D7000%20(balanced).png)
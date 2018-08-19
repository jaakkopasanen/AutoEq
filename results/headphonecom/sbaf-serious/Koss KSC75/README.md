# Koss KSC75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.5; 40 4.7; 42 4.0; 45 3.1; 49 2.1; 52 1.4; 56 0.4; 59 -0.2; 64 -1.0; 68 -1.6; 73 -2.3; 78 -2.8; 83 -3.2; 89 -3.3; 95 -3.5; 102 -4.0; 109 -4.3; 117 -4.5; 125 -4.6; 134 -4.6; 143 -4.8; 153 -4.8; 164 -4.7; 175 -4.6; 188 -4.6; 201 -4.4; 215 -4.2; 230 -4.0; 246 -3.7; 263 -3.4; 282 -3.0; 301 -2.8; 323 -2.6; 345 -2.3; 369 -2.0; 395 -1.7; 423 -1.5; 452 -1.3; 484 -1.0; 518 -0.9; 554 -0.5; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.1; 777 0.2; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.4; 1529 -2.1; 1636 -2.6; 1751 -3.1; 1873 -3.6; 2004 -4.0; 2145 -4.3; 2295 -4.1; 2455 -3.4; 2627 -2.2; 2811 -0.6; 3008 1.1; 3219 1.7; 3444 2.0; 3685 0.7; 3943 4.6; 4219 6.0; 4514 0.3; 4830 -6.7; 5168 -3.0; 5530 1.3; 5917 1.7; 6331 2.3; 6775 1.1; 7249 0.8; 7756 0.3; 8299 -0.4; 8880 -2.7; 9502 -5.4; 10167 -5.9; 10879 -1.9; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 29 Hz   |  0.77 | 7.6 dB  |
| Peaking | 127 Hz  |  0.53 | -5.6 dB |
| Peaking | 2065 Hz |  2.71 | -4.7 dB |
| Peaking | 4098 Hz | 10.11 | 7.2 dB  |
| Peaking | 9868 Hz |  5.97 | -6.9 dB |
| Peaking | 769 Hz  |  2.29 | 0.9 dB  |
| Peaking | 3242 Hz |  6.78 | 2.4 dB  |
| Peaking | 4900 Hz |  9.84 | -9.4 dB |
| Peaking | 5871 Hz |  2.54 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)
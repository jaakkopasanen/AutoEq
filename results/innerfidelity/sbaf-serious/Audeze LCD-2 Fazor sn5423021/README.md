# Audeze LCD-2 Fazor sn5423021

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.7; 40 5.4; 42 5.2; 45 4.9; 49 4.9; 52 4.7; 56 4.3; 59 3.9; 64 3.3; 68 3.0; 73 2.9; 78 2.9; 83 2.8; 89 2.6; 95 2.5; 102 2.1; 109 2.0; 117 2.0; 125 1.8; 134 1.6; 143 1.4; 153 1.3; 164 1.2; 175 1.0; 188 0.9; 201 0.9; 215 0.8; 230 0.9; 246 0.8; 263 0.7; 282 0.7; 301 0.7; 323 0.6; 345 0.5; 369 0.5; 395 0.5; 423 0.5; 452 0.5; 484 0.4; 518 0.4; 554 0.7; 593 1.0; 635 1.0; 679 1.0; 726 1.0; 777 0.8; 832 0.5; 890 0.2; 952 0.1; 1019 0.1; 1090 0.2; 1167 0.1; 1248 0.2; 1336 -0.4; 1429 -1.1; 1529 -1.6; 1636 -1.8; 1751 -1.4; 1873 -0.6; 2004 0.2; 2145 0.4; 2295 1.1; 2455 1.8; 2627 2.6; 2811 3.2; 3008 3.9; 3219 4.4; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Fazor sn5423021 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.29 | 6.1 dB  |
| Peaking | 655 Hz  | 2.24 | 0.9 dB  |
| Peaking | 1653 Hz | 2.89 | -2.8 dB |
| Peaking | 4386 Hz | 1.16 | 6.9 dB  |
| Peaking | 66 Hz   | 4.59 | -0.5 dB |
| Peaking | 3498 Hz | 3.13 | 0.9 dB  |
| Peaking | 4338 Hz | 3.45 | -1.1 dB |
| Peaking | 6360 Hz | 2.99 | 4.5 dB  |
| Peaking | 7362 Hz | 1.6  | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Fazor%20sn5423021/Audeze%20LCD-2%20Fazor%20sn5423021.png)
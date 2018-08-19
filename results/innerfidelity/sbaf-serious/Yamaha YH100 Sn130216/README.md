# Yamaha YH100 Sn130216

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.7; 37 5.6; 40 5.5; 42 5.4; 45 5.3; 49 5.2; 52 5.1; 56 5.1; 59 5.0; 64 4.9; 68 4.8; 73 4.6; 78 4.5; 83 4.4; 89 4.1; 95 3.8; 102 3.6; 109 3.5; 117 3.4; 125 3.1; 134 2.9; 143 2.8; 153 2.7; 164 2.5; 175 2.5; 188 2.4; 201 2.2; 215 2.2; 230 2.2; 246 2.2; 263 2.1; 282 2.2; 301 2.3; 323 2.2; 345 2.1; 369 2.0; 395 1.9; 423 1.9; 452 1.8; 484 1.5; 518 1.3; 554 1.3; 593 1.2; 635 0.9; 679 0.5; 726 0.2; 777 -0.0; 832 -0.5; 890 -0.6; 952 -0.1; 1019 0.3; 1090 1.3; 1167 2.7; 1248 4.8; 1336 6.0; 1429 6.0; 1529 6.0; 1636 6.0; 1751 6.0; 1873 5.7; 2004 3.8; 2145 2.2; 2295 1.2; 2455 4.1; 2627 4.8; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH100 Sn130216 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.68 | 4.0 dB  |
| Peaking | 60 Hz   | 0.39 | 4.1 dB  |
| Peaking | 338 Hz  | 1.57 | 1.4 dB  |
| Peaking | 1525 Hz | 2.64 | 5.8 dB  |
| Peaking | 4145 Hz | 1.03 | 6.7 dB  |
| Peaking | 921 Hz  | 3.16 | -1.9 dB |
| Peaking | 1273 Hz | 7.33 | 1.9 dB  |
| Peaking | 4259 Hz | 5.71 | -1.2 dB |
| Peaking | 6364 Hz | 2.53 | 4.6 dB  |
| Peaking | 7489 Hz | 1.77 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH100%20Sn130216/Yamaha%20YH100%20Sn130216.png)
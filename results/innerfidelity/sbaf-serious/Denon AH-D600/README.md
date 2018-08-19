# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -4.0; 25 -4.1; 26 -4.1; 28 -4.1; 30 -4.2; 32 -4.2; 35 -4.1; 37 -4.1; 40 -4.1; 42 -4.0; 45 -3.9; 49 -3.7; 52 -3.4; 56 -3.2; 59 -3.1; 64 -3.3; 68 -3.6; 73 -4.3; 78 -4.8; 83 -4.9; 89 -5.1; 95 -5.4; 102 -5.4; 109 -5.5; 117 -5.5; 125 -5.6; 134 -5.6; 143 -5.5; 153 -5.3; 164 -4.1; 175 -4.1; 188 -3.6; 201 -2.6; 215 -1.4; 230 0.3; 246 1.7; 263 2.3; 282 2.1; 301 1.3; 323 0.6; 345 0.2; 369 0.3; 395 0.2; 423 0.6; 452 0.9; 484 0.4; 518 -0.0; 554 -0.1; 593 -0.1; 635 0.0; 679 -0.2; 726 -0.1; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.2; 1429 -1.9; 1529 -2.5; 1636 -2.9; 1751 -3.2; 1873 -3.1; 2004 -2.5; 2145 -1.6; 2295 -1.6; 2455 -1.7; 2627 -1.3; 2811 -0.9; 3008 0.1; 3219 1.3; 3444 2.7; 3685 4.6; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.1; 5917 2.6; 6331 1.1; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -3.7; 9502 -4.8; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.0; 18692 -3.7; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734476dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.49 | -4.1 dB |
| Peaking | 121 Hz  | 1.52 | -5.3 dB |
| Peaking | 2028 Hz | 1.42 | -3.6 dB |
| Peaking | 4510 Hz | 1.68 | 7.2 dB  |
| Peaking | 9292 Hz | 6.29 | -6.1 dB |
| Peaking | 186 Hz  | 3    | -2.1 dB |
| Peaking | 261 Hz  | 3.14 | 3.7 dB  |
| Peaking | 450 Hz  | 6.05 | 1.0 dB  |
| Peaking | 1056 Hz | 1.79 | 0.7 dB  |
| Peaking | 1559 Hz | 4.64 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)
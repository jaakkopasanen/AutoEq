# Sony XBA-Z5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.8; 23 -3.9; 25 -4.0; 26 -4.1; 28 -4.2; 30 -4.3; 32 -4.4; 35 -4.5; 37 -4.6; 40 -4.7; 42 -4.8; 45 -4.9; 49 -5.0; 52 -5.1; 56 -5.3; 59 -5.5; 64 -5.7; 68 -5.9; 73 -6.0; 78 -6.3; 83 -6.5; 89 -6.7; 95 -6.9; 102 -7.0; 109 -7.0; 117 -7.1; 125 -7.2; 134 -7.3; 143 -7.3; 153 -7.2; 164 -7.1; 175 -7.0; 188 -6.8; 201 -6.6; 215 -6.3; 230 -6.0; 246 -5.7; 263 -5.4; 282 -5.0; 301 -4.6; 323 -4.2; 345 -3.8; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.4; 484 -2.2; 518 -1.9; 554 -1.4; 593 -0.9; 635 -0.6; 679 -0.2; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.6; 1429 -0.7; 1529 -0.8; 1636 -0.8; 1751 -0.4; 1873 0.1; 2004 0.8; 2145 1.4; 2295 1.7; 2455 2.3; 2627 3.0; 2811 3.6; 3008 3.9; 3219 4.9; 3444 5.2; 3685 4.3; 3943 2.3; 4219 0.3; 4514 -0.8; 4830 -0.7; 5168 0.9; 5530 3.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.3; 10167 -4.3; 10879 -5.2; 11640 -3.9; 12455 -2.2; 13327 -2.0; 14260 -2.2; 15258 -0.6; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.992082740227448dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.27 | -4.3 dB |
| Peaking | 174 Hz   | 0.64 | -4.7 dB |
| Peaking | 3180 Hz  | 2.82 | 5.3 dB  |
| Peaking | 6273 Hz  | 4.97 | 6.5 dB  |
| Peaking | 11112 Hz | 2.79 | -5.3 dB |
| Peaking | 777 Hz   | 3.41 | 1.4 dB  |
| Peaking | 1539 Hz  | 4.16 | -1.1 dB |
| Peaking | 4525 Hz  | 1.55 | 1.9 dB  |
| Peaking | 4592 Hz  | 4.46 | -4.4 dB |
| Peaking | 14087 Hz | 6.95 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20XBA-Z5/Sony%20XBA-Z5.png)
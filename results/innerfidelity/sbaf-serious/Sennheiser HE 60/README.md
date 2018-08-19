# Sennheiser HE 60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.8; 40 5.7; 42 5.7; 45 5.7; 49 5.7; 52 5.8; 56 5.8; 59 5.7; 64 5.3; 68 5.2; 73 4.5; 78 3.1; 83 2.3; 89 2.1; 95 2.1; 102 2.1; 109 2.1; 117 2.1; 125 1.9; 134 1.8; 143 1.7; 153 1.6; 164 1.5; 175 1.4; 188 1.4; 201 1.3; 215 1.2; 230 1.2; 246 1.1; 263 1.1; 282 1.1; 301 1.1; 323 1.1; 345 1.2; 369 1.1; 395 1.0; 423 1.0; 452 1.0; 484 0.9; 518 1.1; 554 1.6; 593 2.2; 635 2.2; 679 1.5; 726 1.4; 777 1.8; 832 1.9; 890 1.5; 952 0.4; 1019 0.0; 1090 0.3; 1167 0.2; 1248 0.4; 1336 0.3; 1429 -0.1; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -1.0; 2004 -0.8; 2145 -0.1; 2295 0.0; 2455 0.6; 2627 0.8; 2811 0.6; 3008 0.8; 3219 0.6; 3444 1.8; 3685 2.1; 3943 2.0; 4219 1.2; 4514 0.7; 4830 -0.6; 5168 -2.3; 5530 -3.2; 5917 -3.9; 6331 -1.8; 6775 1.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.8; 9502 -2.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.2; 20000 -4.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HE 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.27 | 6.0 dB  |
| Peaking | 59 Hz   | 3.14 | 1.6 dB  |
| Peaking | 629 Hz  | 1.52 | 1.9 dB  |
| Peaking | 3787 Hz | 3.61 | 2.5 dB  |
| Peaking | 5678 Hz | 5.4  | -4.4 dB |
| Peaking | 87 Hz   | 5.17 | -1.2 dB |
| Peaking | 254 Hz  | 1.54 | 0.4 dB  |
| Peaking | 1764 Hz | 3.84 | -1.3 dB |
| Peaking | 7069 Hz | 9.7  | 2.5 dB  |
| Peaking | 9256 Hz | 9.21 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HE%2060/Sennheiser%20HE%2060.png)
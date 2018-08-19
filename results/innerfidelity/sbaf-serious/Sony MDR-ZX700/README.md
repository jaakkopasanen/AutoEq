# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 4.8; 52 3.8; 56 2.5; 59 1.7; 64 0.5; 68 -0.2; 73 -0.8; 78 -1.3; 83 -1.6; 89 -1.8; 95 -2.4; 102 -2.9; 109 -2.8; 117 -2.8; 125 -3.5; 134 -3.8; 143 -3.9; 153 -3.8; 164 -2.8; 175 -2.6; 188 -3.3; 201 -3.4; 215 -3.3; 230 -3.2; 246 -3.2; 263 -3.0; 282 -2.8; 301 -2.6; 323 -3.6; 345 -3.2; 369 -2.6; 395 -2.3; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.2; 635 0.2; 679 0.5; 726 0.5; 777 0.7; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -1.1; 1336 -2.0; 1429 -3.1; 1529 -4.2; 1636 -5.6; 1751 -6.9; 1873 -7.6; 2004 -7.4; 2145 -6.4; 2295 -5.0; 2455 -3.6; 2627 -2.6; 2811 -1.8; 3008 -0.7; 3219 0.1; 3444 1.4; 3685 3.7; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.3; 5530 3.7; 5917 3.9; 6331 5.4; 6775 3.9; 7249 1.3; 7756 -2.0; 8299 -7.5; 8880 -10.7; 9502 -9.6; 10167 -4.3; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.66 | 7.5 dB   |
| Peaking | 1958 Hz | 1.98 | -8.3 dB  |
| Peaking | 4365 Hz | 2.28 | 7.1 dB   |
| Peaking | 6530 Hz | 3.27 | 5.2 dB   |
| Peaking | 8935 Hz | 4.16 | -13.0 dB |
| Peaking | 49 Hz   | 2.96 | 3.9 dB   |
| Peaking | 123 Hz  | 1.16 | -1.9 dB  |
| Peaking | 177 Hz  | 0.35 | -1.8 dB  |
| Peaking | 338 Hz  | 0.94 | -1.5 dB  |
| Peaking | 774 Hz  | 1.44 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)
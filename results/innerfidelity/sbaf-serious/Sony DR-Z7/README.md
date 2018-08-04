# Sony DR-Z7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 5.3; 134 4.4; 143 3.9; 153 3.9; 164 3.9; 175 4.0; 188 3.3; 201 3.0; 215 2.9; 230 3.0; 246 3.1; 263 2.9; 282 3.1; 301 3.1; 323 3.1; 345 3.2; 369 3.3; 395 3.3; 423 3.5; 452 3.5; 484 3.0; 518 2.8; 554 2.9; 593 3.1; 635 2.7; 679 2.1; 726 1.7; 777 1.4; 832 1.0; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -2.2; 1429 -3.2; 1529 -4.0; 1636 -4.9; 1751 -5.8; 1873 -6.2; 2004 -6.2; 2145 -5.7; 2295 -4.7; 2455 -3.0; 2627 -1.6; 2811 -0.1; 3008 1.3; 3219 2.1; 3444 2.6; 3685 2.6; 3943 2.7; 4219 1.7; 4514 1.1; 4830 2.3; 5168 4.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony DR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.25 | 6.4 dB  |
| Peaking | 523 Hz  | 0.95 | 2.7 dB  |
| Peaking | 1957 Hz | 1.49 | -7.4 dB |
| Peaking | 3283 Hz | 2.21 | 4.2 dB  |
| Peaking | 5859 Hz | 3.35 | 6.7 dB  |
| Peaking | 14 Hz   | 0.75 | 1.1 dB  |
| Peaking | 42 Hz   | 0.98 | -0.7 dB |
| Peaking | 117 Hz  | 2.55 | 2.0 dB  |
| Peaking | 134 Hz  | 2.09 | -1.4 dB |
| Peaking | 8134 Hz | 5.28 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20DR-Z7/Sony%20DR-Z7.png)
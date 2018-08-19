# Popclik EVOLO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.2; 23 -10.2; 25 -10.3; 26 -10.4; 28 -10.5; 30 -10.6; 32 -10.7; 35 -10.8; 37 -10.8; 40 -10.8; 42 -10.8; 45 -10.8; 49 -10.8; 52 -10.8; 56 -10.8; 59 -10.9; 64 -10.9; 68 -10.9; 73 -10.9; 78 -11.0; 83 -11.0; 89 -11.0; 95 -11.0; 102 -10.9; 109 -10.7; 117 -10.5; 125 -10.4; 134 -10.2; 143 -10.0; 153 -9.8; 164 -9.5; 175 -9.2; 188 -8.9; 201 -8.5; 215 -8.1; 230 -7.7; 246 -7.3; 263 -6.9; 282 -6.4; 301 -5.9; 323 -5.5; 345 -4.9; 369 -4.5; 395 -4.0; 423 -3.5; 452 -3.0; 484 -2.7; 518 -2.3; 554 -1.7; 593 -1.1; 635 -0.7; 679 -0.5; 726 -0.2; 777 0.1; 832 0.1; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.4; 1636 -3.2; 1751 -3.8; 1873 -4.0; 2004 -4.2; 2145 -4.5; 2295 -4.7; 2455 -4.5; 2627 -4.3; 2811 -3.7; 3008 -2.0; 3219 -0.3; 3444 1.5; 3685 2.1; 3943 1.7; 4219 0.2; 4514 -1.3; 4830 -2.3; 5168 -3.5; 5530 -5.9; 5917 -8.5; 6331 -7.2; 6775 -3.3; 7249 -0.4; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.223298403514627dB` and instead set Global volume in the UI for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclik EVOLO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.24 | -10.5 dB |
| Peaking | 177 Hz  | 0.68 | -4.6 dB  |
| Peaking | 2309 Hz | 1.73 | -5.2 dB  |
| Peaking | 3669 Hz | 4.17 | 4.2 dB   |
| Peaking | 5975 Hz | 4.88 | -9.1 dB  |
| Peaking | 377 Hz  | 1.55 | -0.9 dB  |
| Peaking | 847 Hz  | 1.12 | 1.5 dB   |
| Peaking | 1661 Hz | 4.59 | -1.5 dB  |
| Peaking | 5000 Hz | 4.58 | -0.8 dB  |
| Peaking | 7622 Hz | 6.02 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclik%20EVOLO/Popclik%20EVOLO.png)
# Polk UltraFit 2000 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.5; 73 4.5; 78 3.7; 83 3.0; 89 2.2; 95 1.5; 102 1.0; 109 0.8; 117 0.6; 125 0.4; 134 0.4; 143 0.4; 153 0.5; 164 0.7; 175 1.0; 188 1.2; 201 1.4; 215 1.7; 230 2.0; 246 2.3; 263 2.5; 282 2.9; 301 3.3; 323 4.1; 345 4.4; 369 4.6; 395 5.0; 423 5.7; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 6.0; 635 6.0; 679 6.0; 726 6.0; 777 6.0; 832 6.0; 890 4.2; 952 1.7; 1019 -0.6; 1090 -1.7; 1167 -2.1; 1248 -2.6; 1336 -3.0; 1429 -3.1; 1529 -3.2; 1636 -3.4; 1751 -3.8; 1873 -3.9; 2004 -3.7; 2145 -3.1; 2295 -1.9; 2455 -0.3; 2627 1.2; 2811 2.4; 3008 3.6; 3219 3.7; 3444 3.2; 3685 2.2; 3943 2.0; 4219 2.7; 4514 4.1; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -3.2; 8880 -5.1; 9502 -4.7; 10167 -1.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB   |
| Peaking | 663 Hz  | 0.76 | 8.8 dB   |
| Peaking | 1431 Hz | 0.95 | -8.0 dB  |
| Peaking | 5923 Hz | 0.77 | 7.7 dB   |
| Peaking | 8834 Hz | 2.39 | -10.0 dB |
| Peaking | 66 Hz   | 3.54 | 2.3 dB   |
| Peaking | 124 Hz  | 1.74 | -1.6 dB  |
| Peaking | 2160 Hz | 3.35 | -2.9 dB  |
| Peaking | 3144 Hz | 1.39 | 3.4 dB   |
| Peaking | 3922 Hz | 3.44 | -4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20UltraFit%202000%20sample%20A/Polk%20UltraFit%202000%20sample%20A.png)
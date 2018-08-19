# Flare Audio Reference R1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.6; 56 4.4; 59 3.5; 64 2.2; 68 1.2; 73 0.0; 78 -0.9; 83 -1.6; 89 -2.3; 95 -2.8; 102 -3.6; 109 -4.1; 117 -4.4; 125 -4.8; 134 -4.9; 143 -5.1; 153 -5.2; 164 -5.3; 175 -5.3; 188 -5.4; 201 -5.5; 215 -5.5; 230 -5.6; 246 -5.6; 263 -5.7; 282 -5.7; 301 -5.7; 323 -5.7; 345 -5.6; 369 -5.6; 395 -5.7; 423 -5.7; 452 -6.0; 484 -6.5; 518 -7.0; 554 -7.2; 593 -7.3; 635 -7.4; 679 -7.4; 726 -6.9; 777 -6.1; 832 -5.0; 890 -3.4; 952 -1.6; 1019 0.7; 1090 3.0; 1167 5.6; 1248 6.0; 1336 6.0; 1429 6.0; 1529 6.0; 1636 3.2; 1751 -1.6; 1873 -4.3; 2004 -4.7; 2145 -1.8; 2295 0.8; 2455 3.4; 2627 5.3; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Flare Audio Reference R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.45 | 10.1 dB  |
| Peaking | 104 Hz  | 0.59 | -8.8 dB  |
| Peaking | 1272 Hz | 1.86 | 17.8 dB  |
| Peaking | 1392 Hz | 0.31 | -13.8 dB |
| Peaking | 3607 Hz | 0.77 | 14.8 dB  |
| Peaking | 1565 Hz | 7.61 | 5.3 dB   |
| Peaking | 1937 Hz | 4.49 | -5.7 dB  |
| Peaking | 2631 Hz | 3.79 | 4.2 dB   |
| Peaking | 5891 Hz | 2.14 | 7.3 dB   |
| Peaking | 6050 Hz | 0.85 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Flare%20Audio%20Reference%20R1/Flare%20Audio%20Reference%20R1.png)
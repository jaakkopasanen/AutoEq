# Koss KSC75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.3; 49 4.3; 52 3.6; 56 2.8; 59 2.2; 64 1.2; 68 0.6; 73 -0.2; 78 -0.8; 83 -1.4; 89 -2.0; 95 -2.4; 102 -2.9; 109 -3.1; 117 -3.2; 125 -3.3; 134 -3.5; 143 -3.4; 153 -3.5; 164 -3.3; 175 -3.1; 188 -3.0; 201 -2.9; 215 -2.8; 230 -2.6; 246 -2.5; 263 -2.3; 282 -2.0; 301 -1.8; 323 -1.6; 345 -1.4; 369 -1.2; 395 -1.0; 423 -0.7; 452 -0.5; 484 -0.4; 518 -0.4; 554 -0.0; 593 0.2; 635 0.1; 679 0.2; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -1.0; 1429 -1.7; 1529 -2.5; 1636 -3.1; 1751 -3.7; 1873 -4.5; 2004 -4.8; 2145 -5.3; 2295 -5.8; 2455 -5.6; 2627 -4.7; 2811 -3.6; 3008 -2.9; 3219 -2.9; 3444 -0.0; 3685 6.0; 3943 5.6; 4219 -0.6; 4514 -7.2; 4830 -9.2; 5168 -4.2; 5530 -0.2; 5917 1.8; 6331 1.7; 6775 2.0; 7249 1.4; 7756 -0.2; 8299 -3.0; 8880 -5.6; 9502 -6.7; 10167 -5.3; 10879 -1.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 1.55 | 7.4 dB   |
| Peaking | 2740 Hz | 0.94 | -15.8 dB |
| Peaking | 3975 Hz | 1.12 | 23.5 dB  |
| Peaking | 4648 Hz | 3.69 | -21.2 dB |
| Peaking | 9409 Hz | 3.2  | -9.8 dB  |
| Peaking | 20 Hz   | 3.05 | 2.8 dB   |
| Peaking | 52 Hz   | 1.96 | 3.5 dB   |
| Peaking | 137 Hz  | 0.58 | -3.8 dB  |
| Peaking | 806 Hz  | 1.43 | 1.4 dB   |
| Peaking | 6211 Hz | 6.06 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)
# Philips SME3580

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 10 -84; 20 -12.8; 22 -12.6; 23 -12.5; 25 -12.3; 26 -12.2; 28 -12.0; 30 -11.8; 32 -11.6; 35 -11.3; 37 -11.1; 40 -10.8; 42 -10.6; 45 -10.4; 49 -10.1; 52 -9.9; 56 -9.7; 59 -9.5; 64 -9.4; 68 -9.2; 73 -9.0; 78 -8.9; 83 -8.8; 89 -8.6; 95 -8.5; 102 -8.3; 109 -8.0; 117 -7.7; 125 -7.6; 134 -7.3; 143 -7.1; 153 -6.8; 164 -6.5; 175 -6.2; 188 -5.9; 201 -5.5; 215 -5.2; 230 -4.7; 246 -4.4; 263 -4.0; 282 -3.6; 301 -3.3; 323 -2.9; 345 -2.5; 369 -2.1; 395 -1.8; 423 -1.3; 452 -1.0; 484 -0.8; 518 -0.5; 554 -0.2; 593 0.3; 635 0.4; 679 0.5; 726 0.5; 777 0.7; 832 0.7; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.6; 1336 -2.4; 1429 -3.2; 1529 -4.0; 1636 -4.7; 1751 -5.2; 1873 -5.7; 2004 -6.1; 2145 -6.9; 2295 -7.6; 2455 -7.9; 2627 -7.6; 2811 -6.2; 3008 -3.7; 3219 -1.5; 3444 0.3; 3685 0.6; 3943 -0.2; 4219 -2.2; 4514 -4.7; 4830 -6.9; 5168 -7.7; 5530 -6.9; 5917 -3.5; 6331 -1.2; 6775 1.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.0; 10167 -1.0; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.8137220160184007dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SME3580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.18 | -12.5 dB |
| Peaking | 155 Hz  | 0.82 | -3.4 dB  |
| Peaking | 2238 Hz | 2    | -8.1 dB  |
| Peaking | 5233 Hz | 4.49 | -8.4 dB  |
| Peaking | 6969 Hz | 4.23 | 2.5 dB   |
| Peaking | 808 Hz  | 1.53 | 1.9 dB   |
| Peaking | 1562 Hz | 3.23 | -1.1 dB  |
| Peaking | 2166 Hz | 3.5  | 3.9 dB   |
| Peaking | 2743 Hz | 1.13 | -4.2 dB  |
| Peaking | 3509 Hz | 3.31 | 6.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SME3580/Philips%20SME3580.png)
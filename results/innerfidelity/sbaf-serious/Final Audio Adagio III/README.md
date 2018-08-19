# Final Audio Adagio III

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -10.6; 22 -10.6; 23 -10.6; 25 -10.6; 26 -10.6; 28 -10.6; 30 -10.6; 32 -10.6; 35 -10.6; 37 -10.7; 40 -10.7; 42 -10.7; 45 -10.8; 49 -10.8; 52 -10.9; 56 -11.0; 59 -11.1; 64 -11.2; 68 -11.4; 73 -11.5; 78 -11.7; 83 -11.8; 89 -11.9; 95 -12.1; 102 -12.1; 109 -12.1; 117 -12.1; 125 -12.1; 134 -12.1; 143 -12.0; 153 -11.9; 164 -11.7; 175 -11.5; 188 -11.3; 201 -11.0; 215 -10.6; 230 -10.2; 246 -9.8; 263 -9.4; 282 -8.8; 301 -8.3; 323 -7.8; 345 -7.1; 369 -6.5; 395 -5.8; 423 -4.9; 452 -4.1; 484 -3.4; 518 -2.6; 554 -1.6; 593 -0.3; 635 0.5; 679 1.1; 726 1.8; 777 2.4; 832 2.3; 890 1.5; 952 0.7; 1019 -0.2; 1090 -0.9; 1167 -1.1; 1248 -0.8; 1336 -0.7; 1429 -0.5; 1529 -0.4; 1636 -0.5; 1751 -0.6; 1873 -0.8; 2004 -1.2; 2145 -1.9; 2295 -2.8; 2455 -3.3; 2627 -3.1; 2811 -1.9; 3008 0.6; 3219 2.9; 3444 4.7; 3685 5.0; 3943 4.2; 4219 2.1; 4514 -0.1; 4830 -1.8; 5168 -2.3; 5530 -0.6; 5917 3.2; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.448570352289454dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Adagio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.23 | -10.7 dB |
| Peaking | 191 Hz   | 0.79 | -6.9 dB  |
| Peaking | 3643 Hz  | 3.19 | 11.8 dB  |
| Peaking | 3698 Hz  | 1.07 | -5.9 dB  |
| Peaking | 6410 Hz  | 5.44 | 7.2 dB   |
| Peaking | 365 Hz   | 2.42 | -1.7 dB  |
| Peaking | 754 Hz   | 2.43 | 4.1 dB   |
| Peaking | 2474 Hz  | 6.78 | -2.2 dB  |
| Peaking | 10550 Hz | 1.71 | 0.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Adagio%20III/Final%20Audio%20Adagio%20III.png)
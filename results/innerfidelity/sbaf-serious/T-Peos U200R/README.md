# T-Peos U200R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.4; 22 -5.4; 23 -5.4; 25 -5.4; 26 -5.5; 28 -5.4; 30 -5.4; 32 -5.4; 35 -5.4; 37 -5.4; 40 -5.4; 42 -5.4; 45 -5.4; 49 -5.4; 52 -5.5; 56 -5.6; 59 -5.6; 64 -5.7; 68 -5.7; 73 -5.9; 78 -6.0; 83 -6.1; 89 -6.3; 95 -6.4; 102 -6.5; 109 -6.4; 117 -6.4; 125 -6.5; 134 -6.5; 143 -6.5; 153 -6.5; 164 -6.4; 175 -6.3; 188 -6.1; 201 -6.0; 215 -5.8; 230 -5.6; 246 -5.4; 263 -5.1; 282 -4.7; 301 -4.5; 323 -4.1; 345 -3.8; 369 -3.4; 395 -3.1; 423 -2.7; 452 -2.3; 484 -2.0; 518 -1.6; 554 -1.2; 593 -0.6; 635 -0.3; 679 -0.1; 726 0.1; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -1.0; 1429 -1.7; 1529 -2.2; 1636 -2.6; 1751 -2.8; 1873 -2.7; 2004 -2.4; 2145 -1.8; 2295 -0.8; 2455 1.0; 2627 2.6; 2811 3.8; 3008 5.6; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.2; 4219 1.9; 4514 -1.8; 4830 -5.2; 5168 -4.0; 5530 0.3; 5917 4.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -1.9; 10167 -0.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999997757681dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos U200R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.2  | -5.3 dB  |
| Peaking | 189 Hz   | 0.74 | -3.9 dB  |
| Peaking | 3571 Hz  | 1.86 | 13.4 dB  |
| Peaking | 5127 Hz  | 1.21 | -24.6 dB |
| Peaking | 5909 Hz  | 1.51 | 20.8 dB  |
| Peaking | 868 Hz   | 1.79 | 1.8 dB   |
| Peaking | 1899 Hz  | 1.77 | -2.4 dB  |
| Peaking | 2726 Hz  | 4.3  | 2.3 dB   |
| Peaking | 9399 Hz  | 5.57 | -2.0 dB  |
| Peaking | 12443 Hz | 1.15 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20U200R/T-Peos%20U200R.png)
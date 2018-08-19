# T-Peos Rich 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.1; 23 -4.0; 25 -4.0; 26 -4.1; 28 -4.1; 30 -4.1; 32 -4.1; 35 -4.1; 37 -4.2; 40 -4.3; 42 -4.3; 45 -4.3; 49 -4.5; 52 -4.6; 56 -4.7; 59 -4.7; 64 -5.0; 68 -5.1; 73 -5.2; 78 -5.4; 83 -5.6; 89 -5.8; 95 -5.9; 102 -6.1; 109 -6.0; 117 -6.0; 125 -6.1; 134 -6.1; 143 -6.1; 153 -6.1; 164 -5.9; 175 -5.8; 188 -5.6; 201 -5.4; 215 -5.2; 230 -4.9; 246 -4.6; 263 -4.4; 282 -4.0; 301 -3.6; 323 -3.4; 345 -3.0; 369 -2.6; 395 -2.2; 423 -1.7; 452 -1.4; 484 -1.1; 518 -0.8; 554 -0.3; 593 0.2; 635 0.4; 679 0.5; 726 0.7; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.3; 1636 -3.9; 1751 -4.4; 1873 -4.8; 2004 -5.0; 2145 -5.0; 2295 -4.5; 2455 -3.0; 2627 -1.4; 2811 0.3; 3008 2.4; 3219 3.9; 3444 4.8; 3685 4.3; 3943 2.8; 4219 -0.3; 4514 -3.5; 4830 -7.0; 5168 -8.2; 5530 -6.0; 5917 -2.3; 6331 -0.0; 6775 0.5; 7249 -1.0; 7756 -3.7; 8299 -5.8; 8880 -5.9; 9502 -4.3; 10167 -1.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.906624723765252dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Rich 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.27 | -4.1 dB  |
| Peaking | 167 Hz   | 0.75 | -4.2 dB  |
| Peaking | 1920 Hz  | 2.92 | -5.7 dB  |
| Peaking | 8622 Hz  | 3.2  | -6.1 dB  |
| Peaking | 24000 Hz | 2.29 | -3.8 dB  |
| Peaking | 742 Hz   | 2.7  | 1.7 dB   |
| Peaking | 2384 Hz  | 3.87 | -2.8 dB  |
| Peaking | 3548 Hz  | 2.39 | 7.3 dB   |
| Peaking | 5076 Hz  | 3.22 | -10.4 dB |
| Peaking | 6524 Hz  | 3.85 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Rich%20200/T-Peos%20Rich%20200.png)
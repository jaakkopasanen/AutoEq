# Ivery IS-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.9; 22 -11.0; 23 -11.0; 25 -11.1; 26 -11.1; 28 -11.2; 30 -11.2; 32 -11.2; 35 -11.3; 37 -11.3; 40 -11.4; 42 -11.5; 45 -11.6; 49 -11.7; 52 -11.7; 56 -11.9; 59 -12.0; 64 -12.1; 68 -12.2; 73 -12.4; 78 -12.6; 83 -12.7; 89 -12.9; 95 -13.0; 102 -13.1; 109 -13.1; 117 -13.1; 125 -13.1; 134 -13.1; 143 -13.0; 153 -12.9; 164 -12.8; 175 -12.6; 188 -12.4; 201 -12.1; 215 -11.8; 230 -11.4; 246 -11.1; 263 -10.7; 282 -10.2; 301 -9.8; 323 -9.3; 345 -8.7; 369 -8.3; 395 -7.8; 423 -7.1; 452 -6.5; 484 -6.0; 518 -5.5; 554 -4.7; 593 -3.9; 635 -3.4; 679 -2.9; 726 -2.1; 777 -1.2; 832 -1.1; 890 -0.9; 952 -0.6; 1019 0.5; 1090 1.4; 1167 1.4; 1248 1.5; 1336 1.6; 1429 1.8; 1529 2.2; 1636 2.6; 1751 3.3; 1873 4.1; 2004 5.3; 2145 6.0; 2295 6.0; 2455 6.0; 2627 5.8; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.5; 4219 3.5; 4514 2.1; 4830 1.9; 5168 2.2; 5530 2.3; 5917 1.7; 6331 -0.6; 6775 -4.2; 7249 -8.0; 7756 -8.3; 8299 -5.6; 8880 -1.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.0; 13327 -2.1; 14260 -0.6; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999895dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ivery IS-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.13 | -8.7 dB  |
| Peaking | 367 Hz   | 0.21 | -9.7 dB  |
| Peaking | 1719 Hz  | 0.28 | 9.4 dB   |
| Peaking | 7530 Hz  | 3.13 | -12.2 dB |
| Peaking | 22 Hz    | 1.12 | -1.5 dB  |
| Peaking | 1536 Hz  | 2.49 | -2.3 dB  |
| Peaking | 2812 Hz  | 0.51 | 1.3 dB   |
| Peaking | 4628 Hz  | 5.45 | -3.1 dB  |
| Peaking | 13215 Hz | 4.56 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ivery%20IS-1/Ivery%20IS-1.png)
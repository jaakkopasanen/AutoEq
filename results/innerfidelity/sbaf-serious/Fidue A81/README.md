# Fidue A81

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -1.9; 22 -2.3; 23 -2.5; 25 -2.8; 26 -3.0; 28 -3.2; 30 -3.4; 32 -3.6; 35 -3.9; 37 -4.0; 40 -4.3; 42 -4.4; 45 -4.6; 49 -4.8; 52 -5.0; 56 -5.2; 59 -5.4; 64 -5.6; 68 -5.8; 73 -6.0; 78 -6.3; 83 -6.5; 89 -6.7; 95 -7.0; 102 -7.0; 109 -7.1; 117 -7.1; 125 -7.2; 134 -7.3; 143 -7.3; 153 -7.2; 164 -7.1; 175 -6.9; 188 -6.8; 201 -6.6; 215 -6.3; 230 -6.0; 246 -5.8; 263 -5.5; 282 -5.1; 301 -4.8; 323 -4.4; 345 -3.9; 369 -3.5; 395 -3.2; 423 -2.7; 452 -2.2; 484 -1.9; 518 -1.6; 554 -1.1; 593 -0.6; 635 -0.3; 679 -0.2; 726 0.0; 777 0.4; 832 0.5; 890 0.3; 952 0.1; 1019 0.1; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.0; 1529 -2.7; 1636 -3.2; 1751 -3.7; 1873 -4.1; 2004 -4.5; 2145 -5.1; 2295 -5.8; 2455 -6.0; 2627 -6.1; 2811 -5.2; 3008 -3.2; 3219 -1.4; 3444 -0.1; 3685 -0.2; 3943 -1.6; 4219 -4.7; 4514 -8.4; 4830 -11.7; 5168 -9.9; 5530 -4.9; 5917 -1.2; 6331 0.6; 6775 1.2; 7249 0.5; 7756 -2.1; 8299 -5.8; 8880 -8.3; 9502 -7.7; 10167 -5.6; 10879 -4.0; 11640 -2.3; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.283878638762828dB` and instead set Global volume in the UI for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A81 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.42 | -5.5 dB  |
| Peaking | 202 Hz   | 0.84 | -3.8 dB  |
| Peaking | 2299 Hz  | 2.09 | -6.0 dB  |
| Peaking | 4890 Hz  | 5.4  | -12.3 dB |
| Peaking | 22100 Hz | 1.61 | -6.4 dB  |
| Peaking | 830 Hz   | 2.18 | 1.4 dB   |
| Peaking | 1606 Hz  | 4.16 | -1.4 dB  |
| Peaking | 7005 Hz  | 3.5  | 5.1 dB   |
| Peaking | 9073 Hz  | 2.13 | -10.2 dB |
| Peaking | 10509 Hz | 0.33 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A81/Fidue%20A81.png)
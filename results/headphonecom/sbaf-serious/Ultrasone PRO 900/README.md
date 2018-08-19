# Ultrasone PRO 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 3.0; 22 2.2; 23 1.8; 25 1.0; 26 0.7; 28 0.1; 30 -0.5; 32 -1.1; 35 -1.8; 37 -2.1; 40 -2.6; 42 -2.7; 45 -2.6; 49 -2.5; 52 -2.7; 56 -3.1; 59 -3.3; 64 -3.7; 68 -4.3; 73 -4.9; 78 -5.4; 83 -5.8; 89 -6.2; 95 -6.5; 102 -6.8; 109 -7.1; 117 -7.2; 125 -7.1; 134 -7.1; 143 -7.0; 153 -6.9; 164 -6.3; 175 -6.1; 188 -5.7; 201 -4.8; 215 -3.3; 230 -2.1; 246 -0.5; 263 1.5; 282 2.8; 301 1.6; 323 -0.7; 345 -1.9; 369 -2.5; 395 -2.9; 423 -3.0; 452 -2.7; 484 -1.8; 518 1.1; 554 0.6; 593 -0.4; 635 -1.3; 679 -1.2; 726 -1.1; 777 -0.9; 832 -0.9; 890 -0.7; 952 -0.3; 1019 0.1; 1090 0.7; 1167 1.4; 1248 1.4; 1336 0.2; 1429 -0.4; 1529 -1.1; 1636 -1.7; 1751 -2.1; 1873 -1.8; 2004 -0.4; 2145 1.8; 2295 0.4; 2455 -2.5; 2627 -4.3; 2811 -4.9; 3008 -5.4; 3219 -5.5; 3444 -5.7; 3685 -6.5; 3943 -7.3; 4219 -8.1; 4514 -8.5; 4830 -8.3; 5168 -6.8; 5530 -8.2; 5917 -8.2; 6331 -7.4; 6775 -6.5; 7249 -3.5; 7756 -2.2; 8299 -0.6; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.9; 12455 -4.6; 13327 -8.1; 14260 -10.9; 15258 -12.0; 16326 -11.0; 17469 -8.9; 18692 -7.7; 20000 -8.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.09557276638022dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 95 Hz    |  1.12 | -6.3 dB  |
| Peaking | 159 Hz   |  2.47 | -4.6 dB  |
| Peaking | 419 Hz   |  5.96 | -3.0 dB  |
| Peaking | 4550 Hz  |  1.35 | -8.7 dB  |
| Peaking | 16279 Hz |  1.32 | -12.4 dB |
| Peaking | 20 Hz    |  3.18 | 2.3 dB   |
| Peaking | 279 Hz   |  7.77 | 4.6 dB   |
| Peaking | 2172 Hz  | 10.64 | 4.3 dB   |
| Peaking | 9966 Hz  |  1.93 | 5.7 dB   |
| Peaking | 16693 Hz |  0.14 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)
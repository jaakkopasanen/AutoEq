# Shure SRH940

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.5; 37 5.1; 40 4.4; 42 3.9; 45 3.4; 49 2.7; 52 2.4; 56 1.9; 59 1.7; 64 1.3; 68 1.2; 73 1.4; 78 1.9; 83 2.4; 89 3.2; 95 3.5; 102 2.6; 109 1.8; 117 1.2; 125 1.0; 134 0.6; 143 0.2; 153 -0.3; 164 -0.4; 175 -1.4; 188 -2.5; 201 -3.1; 215 -3.5; 230 -3.6; 246 -3.8; 263 -3.8; 282 -3.5; 301 -3.3; 323 -4.1; 345 -4.4; 369 -3.6; 395 -3.2; 423 -2.7; 452 -2.5; 484 -2.2; 518 -1.9; 554 -1.4; 593 -0.8; 635 -0.5; 679 -0.4; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.6; 1429 -1.3; 1529 -1.8; 1636 -2.4; 1751 -2.9; 1873 -3.1; 2004 -3.1; 2145 -3.0; 2295 -2.9; 2455 -2.0; 2627 -2.1; 2811 -2.1; 3008 -1.8; 3219 -1.7; 3444 -2.0; 3685 -2.0; 3943 -2.0; 4219 -2.6; 4514 -2.3; 4830 -1.8; 5168 -0.6; 5530 1.1; 5917 1.3; 6331 1.1; 6775 0.8; 7249 -1.0; 7756 -3.6; 8299 -6.8; 8880 -9.2; 9502 -9.2; 10167 -5.9; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 -0.8; 14260 -3.4; 15258 -2.3; 16326 -0.1; 17469 0.0; 18692 -1.5; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.94 | 6.5 dB   |
| Peaking | 98 Hz    | 2.55 | 3.1 dB   |
| Peaking | 283 Hz   | 1.13 | -4.4 dB  |
| Peaking | 2240 Hz  | 1.35 | -3.0 dB  |
| Peaking | 9147 Hz  | 4.21 | -10.6 dB |
| Peaking | 902 Hz   | 2.26 | 1.1 dB   |
| Peaking | 4449 Hz  | 3.7  | -2.1 dB  |
| Peaking | 6143 Hz  | 2.83 | 3.6 dB   |
| Peaking | 11758 Hz | 4.08 | 3.2 dB   |
| Peaking | 18420 Hz | 0.16 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)
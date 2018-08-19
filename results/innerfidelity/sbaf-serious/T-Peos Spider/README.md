# T-Peos Spider

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -8.7; 22 -8.7; 23 -8.7; 25 -8.6; 26 -8.6; 28 -8.6; 30 -8.6; 32 -8.6; 35 -8.5; 37 -8.5; 40 -8.4; 42 -8.4; 45 -8.4; 49 -8.4; 52 -8.4; 56 -8.3; 59 -8.3; 64 -8.3; 68 -8.4; 73 -8.4; 78 -8.4; 83 -8.4; 89 -8.4; 95 -8.5; 102 -8.4; 109 -8.2; 117 -8.0; 125 -7.9; 134 -7.8; 143 -7.6; 153 -7.4; 164 -7.1; 175 -6.8; 188 -6.5; 201 -6.2; 215 -5.8; 230 -5.4; 246 -5.0; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.4; 345 -2.9; 369 -2.5; 395 -2.2; 423 -1.6; 452 -1.2; 484 -1.0; 518 -0.6; 554 -0.2; 593 0.3; 635 0.5; 679 0.6; 726 0.8; 777 0.9; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.7; 1429 -2.5; 1529 -3.2; 1636 -3.9; 1751 -4.4; 1873 -4.8; 2004 -4.9; 2145 -4.9; 2295 -4.3; 2455 -2.6; 2627 -0.8; 2811 1.1; 3008 3.3; 3219 4.8; 3444 5.8; 3685 5.4; 3943 4.0; 4219 1.2; 4514 -2.0; 4830 -5.2; 5168 -8.0; 5530 -6.6; 5917 -2.0; 6331 0.7; 6775 1.9; 7249 1.3; 7756 -0.3; 8299 -2.7; 8880 -4.3; 9502 -4.0; 10167 -2.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.907608630581183dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Spider ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.18 | -9.0 dB  |
| Peaking | 2084 Hz  | 1.08 | -17.6 dB |
| Peaking | 3112 Hz  | 0.43 | 14.9 dB  |
| Peaking | 5147 Hz  | 3.43 | -15.9 dB |
| Peaking | 9200 Hz  | 2.23 | -8.3 dB  |
| Peaking | 1408 Hz  | 1.46 | -4.3 dB  |
| Peaking | 1493 Hz  | 0.7  | 3.1 dB   |
| Peaking | 2560 Hz  | 4.89 | -2.3 dB  |
| Peaking | 15005 Hz | 1.59 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Spider/T-Peos%20Spider.png)
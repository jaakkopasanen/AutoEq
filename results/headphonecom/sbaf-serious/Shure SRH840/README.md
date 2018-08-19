# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.5; 23 5.2; 25 4.3; 26 3.9; 28 2.9; 30 2.1; 32 1.5; 35 0.7; 37 0.1; 40 -0.9; 42 -1.6; 45 -2.5; 49 -3.2; 52 -3.4; 56 -3.3; 59 -3.1; 64 -3.2; 68 -3.7; 73 -4.8; 78 -5.7; 83 -6.4; 89 -7.1; 95 -7.5; 102 -7.9; 109 -7.9; 117 -7.8; 125 -7.6; 134 -7.4; 143 -7.2; 153 -6.6; 164 -5.6; 175 -5.4; 188 -4.8; 201 -3.9; 215 -3.2; 230 -2.8; 246 -2.5; 263 -2.2; 282 -2.2; 301 -4.3; 323 -4.4; 345 -3.6; 369 -3.2; 395 -2.8; 423 -2.5; 452 -2.3; 484 -2.1; 518 -1.8; 554 -1.6; 593 -1.3; 635 -1.0; 679 -0.6; 726 -0.4; 777 -0.0; 832 0.1; 890 0.3; 952 0.2; 1019 -0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.0; 1429 -0.8; 1529 -1.6; 1636 -2.6; 1751 -3.4; 1873 -3.8; 2004 -4.1; 2145 -4.5; 2295 -4.4; 2455 -4.2; 2627 -3.2; 2811 -2.9; 3008 -2.5; 3219 -1.9; 3444 -1.5; 3685 -1.0; 3943 -1.0; 4219 -1.5; 4514 -3.1; 4830 -2.8; 5168 -0.6; 5530 2.2; 5917 3.7; 6331 3.5; 6775 3.4; 7249 1.3; 7756 -1.7; 8299 -6.8; 8880 -11.0; 9502 -10.4; 10167 -3.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.25 | 6.6 dB   |
| Peaking | 112 Hz  | 0.62 | -7.7 dB  |
| Peaking | 2286 Hz | 1.64 | -4.6 dB  |
| Peaking | 6417 Hz | 3.97 | 5.6 dB   |
| Peaking | 8939 Hz | 4.98 | -13.0 dB |
| Peaking | 255 Hz  | 2.05 | 4.6 dB   |
| Peaking | 307 Hz  | 1.57 | -4.4 dB  |
| Peaking | 1050 Hz | 1.95 | 1.3 dB   |
| Peaking | 4723 Hz | 7.66 | -3.8 dB  |
| Peaking | 9836 Hz | 0.44 | 0.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)
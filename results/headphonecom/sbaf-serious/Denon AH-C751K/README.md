# Denon AH-C751K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 10 -84; 20 -8.1; 22 -8.2; 23 -8.3; 25 -8.4; 26 -8.4; 28 -8.5; 30 -8.6; 32 -8.6; 35 -8.5; 37 -8.5; 40 -8.4; 42 -8.4; 45 -8.6; 49 -8.8; 52 -8.9; 56 -8.9; 59 -8.9; 64 -8.9; 68 -8.9; 73 -8.8; 78 -8.8; 83 -8.8; 89 -8.7; 95 -8.6; 102 -8.4; 109 -8.2; 117 -7.9; 125 -7.7; 134 -7.3; 143 -7.0; 153 -7.7; 164 -8.1; 175 -7.8; 188 -7.3; 201 -6.9; 215 -6.4; 230 -6.1; 246 -5.6; 263 -5.1; 282 -4.7; 301 -4.2; 323 -3.7; 345 -3.2; 369 -2.7; 395 -2.3; 423 -1.9; 452 -1.5; 484 -1.2; 518 -0.8; 554 -0.4; 593 -0.1; 635 0.3; 679 0.4; 726 0.5; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -2.0; 1429 -2.8; 1529 -3.6; 1636 -4.3; 1751 -4.8; 1873 -5.6; 2004 -6.3; 2145 -6.8; 2295 -7.2; 2455 -7.9; 2627 -8.9; 2811 -9.6; 3008 -9.1; 3219 -7.0; 3444 -4.9; 3685 -3.6; 3943 -3.9; 4219 -5.3; 4514 -7.0; 4830 -8.3; 5168 -9.6; 5530 -11.2; 5917 -11.0; 6331 -8.9; 6775 -7.5; 7249 -7.8; 7756 -9.6; 8299 -11.1; 8880 -10.0; 9502 -5.5; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -3.0; 16326 -0.7; 17469 0.0; 18692 0.0; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7699641242002412dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C751K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.3  | -9.1 dB  |
| Peaking | 188 Hz   | 1.14 | -3.7 dB  |
| Peaking | 2494 Hz  | 1.69 | -7.7 dB  |
| Peaking | 6469 Hz  | 1.17 | -10.0 dB |
| Peaking | 24000 Hz | 2.32 | -8.2 dB  |
| Peaking | 3868 Hz  | 4.47 | 4.0 dB   |
| Peaking | 6056 Hz  | 1.02 | -3.5 dB  |
| Peaking | 6832 Hz  | 3.89 | 6.5 dB   |
| Peaking | 8749 Hz  | 3.61 | -7.1 dB  |
| Peaking | 10336 Hz | 2.26 | 6.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C751K/Denon%20AH-C751K.png)
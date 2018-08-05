# Lenntek Sonix 3 Headset

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.8; 83 5.6; 89 5.3; 95 4.9; 102 4.4; 109 3.9; 117 3.2; 125 2.5; 134 2.1; 143 1.7; 153 1.5; 164 1.3; 175 1.2; 188 1.2; 201 1.0; 215 0.9; 230 1.0; 246 1.0; 263 1.0; 282 1.1; 301 1.2; 323 1.2; 345 1.3; 369 1.4; 395 1.5; 423 1.4; 452 1.4; 484 1.4; 518 1.3; 554 1.5; 593 1.6; 635 1.6; 679 1.4; 726 1.3; 777 1.3; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.2; 1336 -1.7; 1429 -2.5; 1529 -3.4; 1636 -4.5; 1751 -5.5; 1873 -6.1; 2004 -6.7; 2145 -6.8; 2295 -5.9; 2455 -4.0; 2627 -1.8; 2811 0.4; 3008 2.2; 3219 3.1; 3444 3.6; 3685 3.0; 3943 0.7; 4219 -3.6; 4514 -5.1; 4830 -1.5; 5168 3.1; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.5; 8299 -3.0; 8880 -1.8; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Sonix 3 Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.36 | 6.5 dB  |
| Peaking | 2063 Hz | 2.1  | -8.2 dB |
| Peaking | 3382 Hz | 2.43 | 5.9 dB  |
| Peaking | 4436 Hz | 5.55 | -8.4 dB |
| Peaking | 5786 Hz | 3.93 | 7.4 dB  |
| Peaking | 90 Hz   | 2.27 | 1.2 dB  |
| Peaking | 151 Hz  | 1.45 | -1.3 dB |
| Peaking | 584 Hz  | 1.19 | 1.6 dB  |
| Peaking | 6724 Hz | 6.47 | 2.2 dB  |
| Peaking | 8233 Hz | 5.17 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Lenntek%20Sonix%203%20Headset/Lenntek%20Sonix%203%20Headset.png)
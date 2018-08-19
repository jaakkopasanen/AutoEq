# Polk UltraFit 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.2; 23 -10.2; 25 -10.2; 26 -10.2; 28 -10.2; 30 -10.2; 32 -10.2; 35 -10.2; 37 -10.2; 40 -10.3; 42 -10.3; 45 -10.3; 49 -10.3; 52 -10.4; 56 -10.4; 59 -10.5; 64 -10.6; 68 -10.6; 73 -10.7; 78 -10.7; 83 -10.9; 89 -10.9; 95 -11.0; 102 -10.9; 109 -10.9; 117 -10.7; 125 -10.7; 134 -10.6; 143 -10.4; 153 -10.2; 164 -10.0; 175 -9.7; 188 -9.4; 201 -9.1; 215 -8.7; 230 -8.3; 246 -8.0; 263 -7.6; 282 -7.1; 301 -6.6; 323 -6.2; 345 -5.7; 369 -5.2; 395 -4.8; 423 -4.2; 452 -3.7; 484 -3.3; 518 -2.9; 554 -2.3; 593 -1.6; 635 -1.2; 679 -1.0; 726 -0.7; 777 -0.0; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.4; 1529 -1.9; 1636 -2.4; 1751 -2.6; 1873 -2.5; 2004 -2.5; 2145 -2.5; 2295 -1.9; 2455 -0.8; 2627 -0.3; 2811 0.5; 3008 1.4; 3219 2.3; 3444 4.4; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999752452863dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk UltraFit 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.5  | -9.8 dB |
| Peaking | 50 Hz   | 0.29 | -9.4 dB |
| Peaking | 191 Hz  | 0.64 | -4.9 dB |
| Peaking | 2059 Hz | 2    | -3.8 dB |
| Peaking | 4572 Hz | 1.33 | 7.2 dB  |
| Peaking | 848 Hz  | 2.37 | 1.7 dB  |
| Peaking | 2169 Hz | 0.07 | -0.2 dB |
| Peaking | 6285 Hz | 4.17 | 2.8 dB  |
| Peaking | 6697 Hz | 4.13 | 1.2 dB  |
| Peaking | 7509 Hz | 2.09 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20UltraFit%20300/Polk%20UltraFit%20300.png)
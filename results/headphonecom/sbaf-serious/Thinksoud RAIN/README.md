# Thinksoud RAIN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 -10.0; 22 -10.2; 23 -10.2; 25 -10.3; 26 -10.4; 28 -10.5; 30 -10.6; 32 -10.6; 35 -10.7; 37 -10.7; 40 -10.8; 42 -10.9; 45 -11.0; 49 -11.1; 52 -11.2; 56 -11.3; 59 -11.4; 64 -11.6; 68 -11.8; 73 -11.8; 78 -12.0; 83 -12.0; 89 -12.2; 95 -12.2; 102 -12.2; 109 -12.2; 117 -12.2; 125 -12.2; 134 -12.1; 143 -12.1; 153 -12.0; 164 -11.8; 175 -11.6; 188 -11.4; 201 -11.1; 215 -10.8; 230 -10.4; 246 -10.1; 263 -9.7; 282 -9.3; 301 -8.8; 323 -8.3; 345 -7.7; 369 -7.2; 395 -6.6; 423 -6.2; 452 -5.6; 484 -5.1; 518 -4.6; 554 -4.0; 593 -3.5; 635 -2.9; 679 -2.4; 726 -1.9; 777 -1.4; 832 -1.2; 890 -0.8; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.3; 1248 0.4; 1336 0.4; 1429 0.3; 1529 0.3; 1636 0.3; 1751 0.5; 1873 0.8; 2004 1.1; 2145 1.2; 2295 1.1; 2455 0.5; 2627 -0.6; 2811 -0.6; 3008 1.0; 3219 3.1; 3444 4.3; 3685 4.4; 3943 3.0; 4219 0.6; 4514 -2.0; 4830 -4.8; 5168 -7.5; 5530 -5.2; 5917 0.2; 6331 3.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.683371396892506dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksoud RAIN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.22 | -9.8 dB  |
| Peaking | 153 Hz  | 0.59 | -6.5 dB  |
| Peaking | 332 Hz  | 1.01 | -3.4 dB  |
| Peaking | 4785 Hz | 1.08 | 6.3 dB   |
| Peaking | 5097 Hz | 4.27 | -14.4 dB |
| Peaking | 1143 Hz | 2.35 | 1.1 dB   |
| Peaking | 2783 Hz | 7.09 | -2.8 dB  |
| Peaking | 3540 Hz | 5.3  | 2.9 dB   |
| Peaking | 6506 Hz | 5.27 | 5.8 dB   |
| Peaking | 6803 Hz | 1.2  | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksoud%20RAIN/Thinksoud%20RAIN.png)
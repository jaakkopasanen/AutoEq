# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 -11.6; 22 -11.5; 23 -11.4; 25 -11.1; 26 -10.9; 28 -10.5; 30 -10.2; 32 -10.1; 35 -10.5; 37 -11.0; 40 -11.3; 42 -11.2; 45 -10.4; 49 -9.0; 52 -8.0; 56 -7.8; 59 -8.5; 64 -10.3; 68 -11.6; 73 -12.6; 78 -13.2; 83 -13.4; 89 -13.5; 95 -13.5; 102 -13.3; 109 -12.9; 117 -12.3; 125 -11.7; 134 -10.8; 143 -10.3; 153 -9.9; 164 -9.3; 175 -9.6; 188 -8.9; 201 -8.0; 215 -7.0; 230 -6.2; 246 -5.2; 263 -4.4; 282 -3.8; 301 -3.0; 323 -2.2; 345 -1.7; 369 -1.6; 395 -1.4; 423 -1.1; 452 -0.8; 484 -0.3; 518 0.5; 554 1.1; 593 1.7; 635 3.3; 679 4.7; 726 5.3; 777 4.9; 832 3.8; 890 2.7; 952 1.2; 1019 -0.5; 1090 -1.8; 1167 -2.9; 1248 -4.1; 1336 -5.2; 1429 -6.1; 1529 -6.9; 1636 -7.4; 1751 -7.4; 1873 -7.2; 2004 -6.8; 2145 -5.9; 2295 -4.5; 2455 -2.9; 2627 -1.3; 2811 0.4; 3008 2.6; 3219 4.9; 3444 5.8; 3685 1.1; 3943 -3.2; 4219 -2.8; 4514 -2.9; 4830 -4.2; 5168 -6.1; 5530 -9.5; 5917 -6.7; 6331 0.1; 6775 2.0; 7249 1.3; 7756 0.1; 8299 -1.8; 8880 -4.1; 9502 -6.1; 10167 -5.2; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -3.2; 15258 -4.8; 16326 -2.1; 17469 -0.0; 18692 -0.3; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.154179294734525dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 1.19 | -11.4 dB |
| Peaking | 17 Hz    | 0.18 | -8.1 dB  |
| Peaking | 113 Hz   | 0.86 | -9.6 dB  |
| Peaking | 1717 Hz  | 2.78 | -8.4 dB  |
| Peaking | 10221 Hz | 0.45 | -2.5 dB  |
| Peaking | 736 Hz   | 2.49 | 7.5 dB   |
| Peaking | 3314 Hz  | 4.19 | 10.1 dB  |
| Peaking | 5795 Hz  | 0.88 | -35.3 dB |
| Peaking | 6438 Hz  | 0.84 | 32.9 dB  |
| Peaking | 9494 Hz  | 6.3  | -5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)
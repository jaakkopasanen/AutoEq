# Ultrasone ZINO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.5; 30 4.8; 32 4.0; 35 3.0; 37 2.3; 40 1.6; 42 1.1; 45 0.6; 49 -0.0; 52 -0.4; 56 -0.7; 59 -0.7; 64 -0.8; 68 -0.8; 73 -0.9; 78 -0.9; 83 -0.8; 89 -0.8; 95 -0.8; 102 -0.8; 109 -0.9; 117 -0.9; 125 -0.9; 134 -0.9; 143 -0.9; 153 -0.7; 164 -0.4; 175 -0.1; 188 0.3; 201 0.8; 215 1.4; 230 1.8; 246 1.2; 263 1.2; 282 1.7; 301 2.1; 323 2.7; 345 3.2; 369 3.7; 395 4.2; 423 4.8; 452 5.2; 484 5.7; 518 6.0; 554 6.0; 593 6.0; 635 6.0; 679 6.0; 726 6.0; 777 6.0; 832 6.0; 890 4.5; 952 1.9; 1019 -0.7; 1090 -2.8; 1167 -4.6; 1248 -6.5; 1336 -7.8; 1429 -8.9; 1529 -9.6; 1636 -11.2; 1751 -12.5; 1873 -13.6; 2004 -14.4; 2145 -14.7; 2295 -10.1; 2455 -5.3; 2627 -5.8; 2811 -5.9; 3008 -4.7; 3219 -4.1; 3444 -3.8; 3685 -2.3; 3943 0.5; 4219 -4.3; 4514 -4.2; 4830 -1.5; 5168 -0.5; 5530 -2.4; 5917 -5.1; 6331 -4.8; 6775 -0.6; 7249 -0.6; 7756 -2.5; 8299 -6.0; 8880 -9.5; 9502 -11.1; 10167 -9.8; 10879 -6.3; 11640 -2.4; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -4.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone ZINO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 25 Hz    |  2.07 | 6.7 dB   |
| Peaking | 661 Hz   |  1    | 9.0 dB   |
| Peaking | 1803 Hz  |  1.3  | -15.5 dB |
| Peaking | 20101 Hz |  3.77 | -3.4 dB  |
| Peaking | 9551 Hz  |  3.49 | -11.8 dB |
| Peaking | 104 Hz   |  0.85 | -1.5 dB  |
| Peaking | 784 Hz   |  1    | 5.5 dB   |
| Peaking | 652 Hz   |  2.25 | -5.5 dB  |
| Peaking | 1152 Hz  |  2.42 | -4.6 dB  |
| Peaking | 7256 Hz  | 10.96 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20ZINO/Ultrasone%20ZINO.png)
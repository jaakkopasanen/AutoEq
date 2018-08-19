# V-Moda Crossfade Wireless Wired Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.9; 22 2.1; 23 1.7; 25 1.1; 26 0.7; 28 0.2; 30 -0.3; 32 -0.8; 35 -1.4; 37 -1.8; 40 -2.2; 42 -2.4; 45 -2.8; 49 -3.1; 52 -3.3; 56 -3.5; 59 -3.6; 64 -3.6; 68 -3.4; 73 -3.2; 78 -3.9; 83 -5.0; 89 -5.5; 95 -5.3; 102 -4.7; 109 -5.3; 117 -6.0; 125 -6.3; 134 -6.4; 143 -6.5; 153 -6.4; 164 -5.7; 175 -5.7; 188 -5.5; 201 -5.0; 215 -4.2; 230 -3.3; 246 -2.2; 263 -1.2; 282 0.3; 301 1.4; 323 2.7; 345 4.0; 369 5.6; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.9; 635 5.4; 679 4.5; 726 3.7; 777 3.0; 832 2.1; 890 1.2; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.1; 1248 -1.5; 1336 -2.0; 1429 -2.4; 1529 -2.7; 1636 -2.9; 1751 -2.9; 1873 -2.4; 2004 -2.0; 2145 -2.0; 2295 -2.4; 2455 -2.1; 2627 -1.0; 2811 -1.5; 3008 -2.1; 3219 -3.0; 3444 -4.2; 3685 -3.7; 3943 -1.3; 4219 0.2; 4514 3.5; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.8; 9502 -4.3; 10167 -3.3; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000009426183dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Wired Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 178 Hz  |  0.52 | -10.2 dB |
| Peaking | 445 Hz  |  0.65 | 13.1 dB  |
| Peaking | 1929 Hz |  0.32 | -4.9 dB  |
| Peaking | 5569 Hz |  1.94 | 9.8 dB   |
| Peaking | 9330 Hz |  4.1  | -5.2 dB  |
| Peaking | 18 Hz   |  1.27 | 3.9 dB   |
| Peaking | 45 Hz   |  2.08 | -1.2 dB  |
| Peaking | 2705 Hz |  3.53 | 2.1 dB   |
| Peaking | 3581 Hz |  4.37 | -3.3 dB  |
| Peaking | 4735 Hz | 10.54 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Wired%20Mode/V-Moda%20Crossfade%20Wireless%20Wired%20Mode.png)
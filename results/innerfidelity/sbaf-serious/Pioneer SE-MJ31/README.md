# Pioneer SE-MJ31

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.4; 72 3.9; 79 2.2; 87 0.8; 96 -0.1; 106 -0.6; 116 -0.7; 128 -1.0; 141 -1.2; 155 -1.2; 170 -1.0; 187 -0.6; 206 -0.5; 227 -0.3; 249 -0.2; 274 0.1; 302 0.1; 332 -0.0; 365 0.2; 402 0.1; 442 -0.0; 486 -0.2; 535 -0.5; 588 -0.4; 647 -0.6; 712 -0.8; 783 -0.7; 861 -0.3; 947 0.3; 1042 -0.4; 1146 -2.0; 1261 -4.2; 1387 -6.7; 1526 -6.4; 1678 -7.6; 1846 -7.5; 2031 -4.2; 2234 -0.6; 2457 1.8; 2703 4.0; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.2; 7010 -2.8; 7711 -1.1; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -0.7; 18182 -1.3; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-MJ31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.37 | 8.4 dB   |
| Peaking | 112 Hz   | 0.8  | -6.7 dB  |
| Peaking | 1713 Hz  | 1.78 | -11.8 dB |
| Peaking | 3601 Hz  | 0.73 | 8.3 dB   |
| Peaking | 7331 Hz  | 5.59 | -6.4 dB  |
| Peaking | 986 Hz   | 5.81 | 1.6 dB   |
| Peaking | 1349 Hz  | 9.41 | -2.0 dB  |
| Peaking | 3902 Hz  | 6.37 | -1.0 dB  |
| Peaking | 5949 Hz  | 6.55 | 2.9 dB   |
| Peaking | 20057 Hz | 0.24 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-MJ31/Pioneer%20SE-MJ31.png)
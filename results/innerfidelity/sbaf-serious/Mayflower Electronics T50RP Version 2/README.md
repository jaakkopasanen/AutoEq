# Mayflower Electronics T50RP Version 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.8; 28 0.9; 31 1.2; 34 1.5; 37 1.7; 41 1.8; 45 1.9; 49 1.9; 54 1.8; 60 1.2; 66 1.1; 72 1.1; 79 1.2; 87 0.5; 96 -1.7; 106 -4.0; 116 -5.2; 128 -5.8; 141 -5.6; 155 -4.8; 170 -4.8; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.9; 274 -4.5; 302 -4.1; 332 -3.6; 365 -2.4; 402 -1.4; 442 -1.0; 486 -1.2; 535 -0.4; 588 0.7; 647 1.5; 712 1.4; 783 0.4; 861 -0.5; 947 -0.4; 1042 -0.3; 1146 -1.7; 1261 -2.6; 1387 -3.8; 1526 -5.2; 1678 -5.6; 1846 -5.9; 2031 -6.7; 2234 -7.4; 2457 -7.8; 2703 -7.9; 2973 -9.2; 3270 -9.2; 3597 -8.4; 3957 -8.0; 4353 -7.4; 4788 -5.0; 5267 -2.1; 5793 -1.9; 6373 -3.6; 7010 -2.3; 7711 -5.0; 8482 -12.4; 9330 -15.1; 10263 -8.0; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.0dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mayflower Electronics T50RP Version 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 2    | -6.2 dB  |
| Peaking | 206 Hz   | 0.23 | 5.8 dB   |
| Peaking | 232 Hz   | 0.73 | -10.4 dB |
| Peaking | 2718 Hz  | 0.8  | -9.4 dB  |
| Peaking | 9141 Hz  | 4.98 | -16.1 dB |
| Peaking | 1507 Hz  | 6.24 | -1.5 dB  |
| Peaking | 4342 Hz  | 3.35 | -3.1 dB  |
| Peaking | 5308 Hz  | 2.83 | 3.2 dB   |
| Peaking | 10121 Hz | 4.92 | -5.3 dB  |
| Peaking | 11060 Hz | 3.11 | 4.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Mayflower%20Electronics%20T50RP%20Version%202/Mayflower%20Electronics%20T50RP%20Version%202.png)
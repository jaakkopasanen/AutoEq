# Yamaha HP3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.4; 60 4.7; 66 4.1; 72 3.6; 79 3.0; 87 2.5; 96 1.8; 106 1.3; 116 1.1; 128 0.6; 141 0.1; 155 -0.2; 170 -0.4; 187 -0.6; 206 -0.7; 227 -0.7; 249 -0.6; 274 -0.6; 302 -0.5; 332 -0.4; 365 -0.3; 402 -0.2; 442 0.0; 486 -0.2; 535 -0.1; 588 0.1; 647 0.2; 712 0.1; 783 0.2; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.7; 1387 1.0; 1526 1.7; 1678 3.0; 1846 4.9; 2031 6.0; 2234 6.0; 2457 5.7; 2703 4.1; 2973 5.2; 3270 6.0; 3597 6.0; 3957 5.2; 4353 5.2; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.57 | 6.9 dB  |
| Peaking | 969 Hz  | 0.05 | -0.8 dB |
| Peaking | 2080 Hz | 1.99 | 5.8 dB  |
| Peaking | 3566 Hz | 1.73 | 5.0 dB  |
| Peaking | 5672 Hz | 2.43 | 5.8 dB  |
| Peaking | 20 Hz   | 0.37 | 1.7 dB  |
| Peaking | 34 Hz   | 1.51 | -2.3 dB |
| Peaking | 170 Hz  | 1.04 | -0.8 dB |
| Peaking | 565 Hz  | 1.3  | 0.7 dB  |
| Peaking | 7961 Hz | 6.81 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP3/Yamaha%20HP3.png)
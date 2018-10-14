# Ultrasone PRO 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.4; 34 4.5; 37 3.8; 41 3.0; 45 2.5; 49 2.4; 54 2.3; 60 3.0; 66 3.0; 72 2.1; 79 1.8; 87 1.6; 96 1.7; 106 2.1; 116 2.4; 128 2.6; 141 3.0; 155 3.6; 170 4.6; 187 5.5; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 4.8; 365 2.4; 402 1.1; 442 0.7; 486 0.5; 535 0.5; 588 1.6; 647 3.1; 712 1.8; 783 1.1; 861 0.5; 947 0.1; 1042 0.1; 1146 0.7; 1261 0.6; 1387 0.4; 1526 -0.4; 1678 0.1; 1846 1.9; 2031 4.3; 2234 4.3; 2457 1.8; 2703 3.7; 2973 3.9; 3270 2.2; 3597 2.1; 3957 3.4; 4353 6.0; 4788 5.6; 5267 5.9; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.4; 18182 -1.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.57 | 6.2 dB  |
| Peaking | 233 Hz   | 1.17 | 6.4 dB  |
| Peaking | 2252 Hz  | 2.53 | 3.6 dB  |
| Peaking | 4626 Hz  | 2.52 | 5.4 dB  |
| Peaking | 6142 Hz  | 4.51 | 4.4 dB  |
| Peaking | 458 Hz   | 3.53 | -1.6 dB |
| Peaking | 648 Hz   | 6.49 | 2.6 dB  |
| Peaking | 1572 Hz  | 7.53 | -1.7 dB |
| Peaking | 8769 Hz  | 4.5  | -1.4 dB |
| Peaking | 17639 Hz | 4.31 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)
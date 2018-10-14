# Klipsch Reference ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.1; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.6; 41 -8.7; 45 -8.6; 49 -8.6; 54 -8.6; 60 -8.6; 66 -8.6; 72 -8.5; 79 -8.4; 87 -8.5; 96 -8.4; 106 -8.1; 116 -7.5; 128 -7.1; 141 -7.5; 155 -7.5; 170 -6.9; 187 -6.7; 206 -6.0; 227 -6.0; 249 -5.6; 274 -5.1; 302 -4.3; 332 -3.4; 365 -2.2; 402 -0.8; 442 0.6; 486 1.7; 535 2.1; 588 2.6; 647 2.8; 712 2.7; 783 2.4; 861 1.6; 947 0.6; 1042 -0.4; 1146 -0.9; 1261 -1.4; 1387 -2.7; 1526 -4.1; 1678 -4.9; 1846 -5.2; 2031 -5.0; 2234 -5.0; 2457 -4.7; 2703 -4.6; 2973 -4.5; 3270 -3.6; 3597 -1.8; 3957 0.4; 4353 2.5; 4788 5.6; 5267 1.2; 5793 -0.8; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -0.4; 11289 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.43 | -8.6 dB |
| Peaking | 123 Hz  | 1.03 | -4.5 dB |
| Peaking | 236 Hz  | 2.35 | -3.8 dB |
| Peaking | 2267 Hz | 1.41 | -5.9 dB |
| Peaking | 4726 Hz | 4.88 | 6.4 dB  |
| Peaking | 326 Hz  | 2.68 | -2.1 dB |
| Peaking | 621 Hz  | 1.25 | 3.9 dB  |
| Peaking | 1559 Hz | 3.46 | -2.2 dB |
| Peaking | 5697 Hz | 6.7  | -2.4 dB |
| Peaking | 6607 Hz | 6.87 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)
# Ultrasone HFi-2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.1; 25 4.3; 28 2.9; 31 1.6; 34 0.6; 37 -0.3; 41 -1.3; 45 -1.9; 49 -2.2; 54 -2.7; 60 -3.3; 66 -3.5; 72 -3.7; 79 -4.4; 87 -4.8; 96 -4.8; 106 -4.9; 116 -4.8; 128 -4.7; 141 -4.5; 155 -4.3; 170 -3.8; 187 -3.6; 206 -3.0; 227 -3.6; 249 -4.4; 274 -3.6; 302 -2.9; 332 -2.2; 365 -1.6; 402 -1.4; 442 -1.0; 486 -1.1; 535 -0.1; 588 0.3; 647 -0.2; 712 -0.3; 783 -0.3; 861 -0.2; 947 0.2; 1042 -0.2; 1146 0.3; 1261 0.3; 1387 0.3; 1526 0.5; 1678 0.2; 1846 -0.6; 2031 -0.1; 2234 2.3; 2457 6.0; 2703 4.7; 2973 2.1; 3270 -0.4; 3597 -0.2; 3957 0.5; 4353 -0.3; 4788 4.1; 5267 5.2; 5793 1.4; 6373 -8.6; 7010 -4.5; 7711 0.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.4; 13660 -5.7; 15026 -8.6; 16529 -6.9; 18182 -2.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.23 | 6.7 dB   |
| Peaking | 106 Hz   | 0.39 | -5.0 dB  |
| Peaking | 5333 Hz  | 0.43 | 2.9 dB   |
| Peaking | 6582 Hz  | 7.53 | -12.7 dB |
| Peaking | 15328 Hz | 1.85 | -10.0 dB |
| Peaking | 187 Hz   | 4.53 | 0.5 dB   |
| Peaking | 2105 Hz  | 3.76 | -4.3 dB  |
| Peaking | 2450 Hz  | 3.21 | 8.5 dB   |
| Peaking | 3776 Hz  | 1.12 | -4.1 dB  |
| Peaking | 5175 Hz  | 4.79 | 6.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-2400/Ultrasone%20HFi-2400.png)
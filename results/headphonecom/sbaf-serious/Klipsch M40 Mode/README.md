# Klipsch M40 Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.5; 25 -0.8; 28 -1.0; 31 -1.1; 34 -1.1; 37 -1.1; 41 -1.0; 45 -0.9; 49 -0.8; 54 -0.7; 60 -0.7; 66 -0.6; 72 -0.6; 79 -0.6; 87 -0.6; 96 -0.7; 106 -0.7; 116 -0.6; 128 -0.8; 141 -0.8; 155 -0.8; 170 -0.7; 187 -0.7; 206 -0.7; 227 -0.7; 249 -0.5; 274 -0.4; 302 0.2; 332 0.8; 365 0.7; 402 0.6; 442 0.7; 486 0.6; 535 0.9; 588 1.0; 647 1.2; 712 1.1; 783 1.1; 861 0.7; 947 0.2; 1042 -0.3; 1146 -1.1; 1261 -2.1; 1387 -3.6; 1526 -5.3; 1678 -5.2; 1846 -2.8; 2031 0.8; 2234 3.4; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch M40 Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.99 | -1.0 dB  |
| Peaking | 202 Hz  | 0.66 | -1.5 dB  |
| Peaking | 427 Hz  | 0.54 | 1.4 dB   |
| Peaking | 1606 Hz | 2.06 | -10.0 dB |
| Peaking | 3147 Hz | 0.68 | 7.8 dB   |
| Peaking | 2462 Hz | 4.44 | 2.0 dB   |
| Peaking | 3142 Hz | 1.44 | -1.3 dB  |
| Peaking | 6299 Hz | 2.02 | 5.9 dB   |
| Peaking | 7341 Hz | 1.44 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20M40%20Mode/Klipsch%20M40%20Mode.png)
# Monoprice 8320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.5; 87 5.1; 96 4.5; 106 4.1; 116 3.9; 128 3.5; 141 3.0; 155 2.6; 170 2.4; 187 2.1; 206 1.8; 227 1.6; 249 1.4; 274 1.2; 302 1.1; 332 1.0; 365 0.9; 402 0.8; 442 1.0; 486 0.8; 535 0.9; 588 1.2; 647 1.2; 712 0.9; 783 0.8; 861 0.6; 947 0.6; 1042 -0.3; 1146 -1.1; 1261 -2.0; 1387 -3.0; 1526 -4.3; 1678 -5.6; 1846 -7.0; 2031 -8.5; 2234 -9.8; 2457 -8.6; 2703 -5.6; 2973 -2.1; 3270 0.8; 3597 1.4; 3957 0.0; 4353 -3.0; 4788 -1.2; 5267 -1.5; 5793 2.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice 8320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.31 | 6.4 dB   |
| Peaking | 699 Hz  | 1.68 | 1.3 dB   |
| Peaking | 2125 Hz | 2.13 | -10.2 dB |
| Peaking | 5525 Hz | 5.46 | -4.9 dB  |
| Peaking | 6162 Hz | 4.47 | 8.2 dB   |
| Peaking | 937 Hz  | 6.5  | 0.7 dB   |
| Peaking | 1481 Hz | 4.47 | -1.3 dB  |
| Peaking | 2565 Hz | 5.4  | -2.6 dB  |
| Peaking | 3479 Hz | 2.66 | 3.9 dB   |
| Peaking | 4362 Hz | 6.78 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208320/Monoprice%208320.png)
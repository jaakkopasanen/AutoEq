# Aurisonic Rockets
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.6; 28 1.5; 31 1.4; 34 1.2; 37 1.1; 41 0.9; 45 0.8; 49 0.6; 54 0.4; 60 0.1; 66 -0.2; 72 -0.5; 79 -0.9; 87 -1.3; 96 -1.8; 106 -2.0; 116 -2.2; 128 -2.5; 141 -2.8; 155 -3.0; 170 -3.0; 187 -3.2; 206 -3.2; 227 -3.0; 249 -3.1; 274 -2.9; 302 -2.8; 332 -2.5; 365 -2.3; 402 -2.0; 442 -1.5; 486 -1.3; 535 -1.0; 588 -0.4; 647 -0.1; 712 0.1; 783 0.5; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.8; 1526 -1.4; 1678 -1.8; 1846 -1.6; 2031 -1.0; 2234 -0.3; 2457 1.2; 2703 2.9; 2973 5.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurisonic Rockets GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurisonic Rockets ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.23 | 2.0 dB  |
| Peaking | 181 Hz  | 0.43 | -3.7 dB |
| Peaking | 740 Hz  | 1.58 | 1.3 dB  |
| Peaking | 1877 Hz | 1.65 | -3.7 dB |
| Peaking | 3989 Hz | 0.98 | 7.3 dB  |
| Peaking | 3071 Hz | 6.94 | 1.7 dB  |
| Peaking | 4102 Hz | 3.55 | -0.9 dB |
| Peaking | 6352 Hz | 2.31 | 4.8 dB  |
| Peaking | 7220 Hz | 0.71 | -1.5 dB |
| Peaking | 7476 Hz | 2.83 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurisonic%20Rockets/Aurisonic%20Rockets.png)
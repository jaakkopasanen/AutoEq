# AKG K267 Tiesto Studio Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.7; 28 3.8; 31 3.9; 34 4.0; 37 4.2; 41 4.3; 45 4.5; 49 4.8; 54 5.0; 60 4.8; 66 4.6; 72 4.5; 79 4.6; 87 3.7; 96 2.4; 106 1.6; 116 0.8; 128 0.1; 141 0.0; 155 0.2; 170 0.6; 187 -0.1; 206 0.1; 227 0.0; 249 0.3; 274 0.8; 302 1.8; 332 2.5; 365 2.2; 402 1.4; 442 0.8; 486 0.4; 535 0.3; 588 0.6; 647 0.5; 712 0.3; 783 0.5; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.3; 1261 -1.3; 1387 -2.6; 1526 -2.2; 1678 -1.2; 1846 -0.1; 2031 0.7; 2234 1.5; 2457 3.1; 2703 3.0; 2973 3.8; 3270 4.1; 3597 4.7; 3957 5.7; 4353 6.0; 4788 6.0; 5267 2.6; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Studio Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Studio Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.66 | 4.0 dB  |
| Peaking | 68 Hz   | 1.79 | 3.2 dB  |
| Peaking | 1462 Hz | 3.83 | -3.4 dB |
| Peaking | 3950 Hz | 1.32 | 5.8 dB  |
| Peaking | 6171 Hz | 6.2  | 4.2 dB  |
| Peaking | 136 Hz  | 3.41 | -1.0 dB |
| Peaking | 343 Hz  | 3.64 | 2.5 dB  |
| Peaking | 700 Hz  | 2.2  | 0.4 dB  |
| Peaking | 6751 Hz | 8.36 | 1.4 dB  |
| Peaking | 8061 Hz | 2.36 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Studio%20Setting/AKG%20K267%20Tiesto%20Studio%20Setting.png)
# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.6; 28 5.5; 31 5.4; 34 5.3; 37 5.2; 41 5.0; 45 4.8; 49 4.7; 54 4.5; 60 4.2; 66 3.9; 72 3.6; 79 3.2; 87 2.8; 96 2.3; 106 2.0; 116 1.8; 128 1.5; 141 1.3; 155 1.1; 170 0.9; 187 0.9; 206 0.8; 227 0.9; 249 0.9; 274 1.0; 302 1.1; 332 1.2; 365 1.4; 402 1.5; 442 1.7; 486 1.6; 535 1.7; 588 2.0; 647 2.0; 712 1.8; 783 1.7; 861 1.1; 947 0.5; 1042 -0.4; 1146 -1.1; 1261 -1.9; 1387 -3.0; 1526 -4.1; 1678 -4.6; 1846 -4.2; 2031 -2.8; 2234 -0.4; 2457 2.8; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.6; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.38 | 5.7 dB  |
| Peaking | 670 Hz  | 0.84 | 2.5 dB  |
| Peaking | 1800 Hz | 1.28 | -8.7 dB |
| Peaking | 2970 Hz | 1.2  | 9.1 dB  |
| Peaking | 5603 Hz | 2.79 | 4.8 dB  |
| Peaking | 3320 Hz | 4.83 | -1.5 dB |
| Peaking | 3958 Hz | 1.63 | 1.5 dB  |
| Peaking | 6545 Hz | 5.16 | 3.6 dB  |
| Peaking | 6765 Hz | 1.38 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE315/Shure%20SE315.png)
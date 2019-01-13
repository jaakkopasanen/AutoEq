# Shure SE530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.7; 28 2.6; 31 2.4; 34 2.3; 37 2.2; 41 2.0; 45 1.8; 49 1.7; 54 1.3; 60 0.9; 66 0.6; 72 0.3; 79 -0.1; 87 -0.5; 96 -0.8; 106 -1.1; 116 -1.3; 128 -1.6; 141 -1.9; 155 -2.1; 170 -2.3; 187 -2.5; 206 -2.5; 227 -2.6; 249 -2.6; 274 -2.6; 302 -2.3; 332 -2.1; 365 -1.8; 402 -1.6; 442 -1.5; 486 -1.5; 535 -1.0; 588 -0.7; 647 -0.4; 712 0.0; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.2; 1526 -1.9; 1678 -2.5; 1846 -2.9; 2031 -3.1; 2234 -2.5; 2457 -0.9; 2703 0.8; 2973 2.4; 3270 4.1; 3597 5.4; 3957 5.4; 4353 4.3; 4788 4.3; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | 2.9 dB  |
| Peaking | 209 Hz  | 0.67 | -2.8 dB |
| Peaking | 2012 Hz | 2.11 | -4.1 dB |
| Peaking | 3658 Hz | 2.03 | 5.6 dB  |
| Peaking | 5814 Hz | 3.26 | 5.7 dB  |
| Peaking | 846 Hz  | 2.87 | 0.9 dB  |
| Peaking | 1534 Hz | 6.8  | -0.6 dB |
| Peaking | 8249 Hz | 4.56 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE530/Shure%20SE530.png)
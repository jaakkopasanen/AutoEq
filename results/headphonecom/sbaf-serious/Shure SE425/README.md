# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.4; 28 5.1; 31 4.8; 34 4.5; 37 4.3; 41 4.0; 45 3.6; 49 3.3; 54 2.9; 60 2.4; 66 1.9; 72 1.5; 79 1.0; 87 0.5; 96 0.1; 106 -0.3; 116 -0.6; 128 -0.9; 141 -1.5; 155 -1.7; 170 -1.9; 187 -2.0; 206 -2.1; 227 -2.1; 249 -2.1; 274 -2.1; 302 -1.8; 332 -1.9; 365 -1.6; 402 -1.4; 442 -1.2; 486 -1.0; 535 -0.7; 588 -0.4; 647 -0.1; 712 0.3; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.7; 1678 -2.0; 1846 -2.1; 2031 -2.2; 2234 -2.1; 2457 -1.5; 2703 -0.3; 2973 1.3; 3270 3.1; 3597 4.3; 3957 4.3; 4353 3.7; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.46 | 5.8 dB  |
| Peaking | 46 Hz   | 2.05 | 2.9 dB  |
| Peaking | 2420 Hz | 0.94 | -3.7 dB |
| Peaking | 3565 Hz | 1.84 | 5.9 dB  |
| Peaking | 5701 Hz | 2.94 | 6.2 dB  |
| Peaking | 34 Hz   | 3    | 0.8 dB  |
| Peaking | 76 Hz   | 1.84 | 1.1 dB  |
| Peaking | 225 Hz  | 0.57 | -2.3 dB |
| Peaking | 802 Hz  | 1.63 | 1.3 dB  |
| Peaking | 7952 Hz | 7.43 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE425/Shure%20SE425.png)
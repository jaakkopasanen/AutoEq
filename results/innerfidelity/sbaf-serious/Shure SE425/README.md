# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.6; 31 5.3; 34 5.1; 37 4.8; 41 4.4; 45 4.1; 49 3.8; 54 3.4; 60 2.9; 66 2.5; 72 2.0; 79 1.5; 87 1.0; 96 0.5; 106 -0.0; 116 -0.3; 128 -0.7; 141 -1.1; 155 -1.3; 170 -1.5; 187 -1.6; 206 -1.7; 227 -1.7; 249 -1.8; 274 -1.8; 302 -1.6; 332 -1.5; 365 -1.4; 402 -1.2; 442 -0.9; 486 -0.8; 535 -0.6; 588 -0.1; 647 0.2; 712 0.2; 783 0.5; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.5; 1387 -1.0; 1526 -1.5; 1678 -1.9; 1846 -2.0; 2031 -2.0; 2234 -2.1; 2457 -1.3; 2703 -0.2; 2973 1.6; 3270 2.8; 3597 3.4; 3957 3.5; 4353 3.0; 4788 3.7; 5267 5.8; 5793 6.0; 6373 4.6; 7010 1.6; 7711 0.3; 8482 0.0
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
| Peaking | 24 Hz   | 1.3  | 6.1 dB  |
| Peaking | 49 Hz   | 1.93 | 2.9 dB  |
| Peaking | 2227 Hz | 1.28 | -3.3 dB |
| Peaking | 3473 Hz | 1.87 | 4.4 dB  |
| Peaking | 5736 Hz | 3.35 | 6.1 dB  |
| Peaking | 75 Hz   | 1.7  | 1.2 dB  |
| Peaking | 236 Hz  | 0.57 | -2.0 dB |
| Peaking | 771 Hz  | 1.56 | 1.2 dB  |
| Peaking | 8018 Hz | 4.24 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE425/Shure%20SE425.png)
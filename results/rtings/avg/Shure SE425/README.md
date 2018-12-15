# Shure SE425

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.6; 106 5.0; 116 3.9; 128 3.0; 141 2.2; 155 1.5; 170 1.0; 187 0.5; 206 0.1; 227 -0.2; 249 -0.3; 274 -0.4; 302 -0.4; 332 -0.4; 365 -0.3; 402 -0.2; 442 -0.0; 486 0.2; 535 0.6; 588 1.1; 647 1.5; 712 1.7; 783 1.8; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.8; 1261 -1.1; 1387 -1.2; 1526 -1.1; 1678 -0.9; 1846 -0.7; 2031 -0.4; 2234 0.2; 2457 0.9; 2703 1.8; 2973 1.9; 3270 1.3; 3597 0.3; 3957 0.1; 4353 1.2; 4788 3.7; 5267 5.6; 5793 5.6; 6373 3.4; 7010 -0.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.31 | 7.2 dB  |
| Peaking | 715 Hz  | 0.88 | 5.6 dB  |
| Peaking | 835 Hz  | 0.17 | -4.5 dB |
| Peaking | 2738 Hz | 1.6  | 4.4 dB  |
| Peaking | 5462 Hz | 2.92 | 7.7 dB  |
| Peaking | 16 Hz   | 1.01 | 1.8 dB  |
| Peaking | 44 Hz   | 0.9  | -1.1 dB |
| Peaking | 94 Hz   | 2.33 | 1.3 dB  |
| Peaking | 165 Hz  | 1.59 | -0.8 dB |
| Peaking | 1712 Hz | 5.84 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE425/Shure%20SE425.png)
# Shure SE425

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.5; 116 4.4; 128 3.5; 141 2.7; 155 2.1; 170 1.6; 187 1.1; 206 0.6; 227 0.3; 249 0.3; 274 0.3; 302 0.4; 332 0.5; 365 0.7; 402 0.8; 442 1.1; 486 1.4; 535 1.8; 588 2.2; 647 2.5; 712 2.5; 783 2.3; 861 1.6; 947 0.6; 1042 -0.3; 1146 -0.6; 1261 -0.9; 1387 -1.2; 1526 -1.4; 1678 -1.2; 1846 -0.6; 2031 -0.0; 2234 0.7; 2457 1.4; 2703 2.6; 2973 3.5; 3270 3.9; 3597 3.5; 3957 2.5; 4353 2.5; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
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

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 54 Hz   |  0.29 | 7.1 dB  |
| Peaking | 673 Hz  |  0.81 | 7.0 dB  |
| Peaking | 998 Hz  |  0.15 | -5.4 dB |
| Peaking | 3012 Hz |  1.28 | 6.7 dB  |
| Peaking | 5656 Hz |  2.1  | 8.0 dB  |
| Peaking | 18 Hz   |  1.17 | 1.8 dB  |
| Peaking | 47 Hz   |  0.4  | -0.9 dB |
| Peaking | 96 Hz   |  2.46 | 1.7 dB  |
| Peaking | 798 Hz  |  5.93 | 0.3 dB  |
| Peaking | 6426 Hz | 12.88 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Shure%20SE425/Shure%20SE425.png)
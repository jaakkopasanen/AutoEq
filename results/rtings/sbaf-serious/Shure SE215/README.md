# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.9; 28 2.6; 31 2.4; 34 2.2; 37 2.0; 41 1.7; 45 1.5; 49 1.3; 54 0.9; 60 0.4; 66 -0.1; 72 -0.4; 79 -0.7; 87 -1.2; 96 -1.8; 106 -2.6; 116 -3.3; 128 -4.0; 141 -4.6; 155 -5.0; 170 -5.2; 187 -5.5; 206 -5.6; 227 -5.6; 249 -5.4; 274 -5.1; 302 -4.8; 332 -4.4; 365 -3.9; 402 -3.3; 442 -2.8; 486 -2.1; 535 -1.5; 588 -0.9; 647 -0.2; 712 0.3; 783 0.6; 861 0.6; 947 0.4; 1042 -0.3; 1146 -1.3; 1261 -1.6; 1387 -2.4; 1526 -3.0; 1678 -3.5; 1846 -3.7; 2031 -3.8; 2234 -3.1; 2457 -1.5; 2703 0.6; 2973 2.4; 3270 3.5; 3597 3.2; 3957 0.7; 4353 -3.7; 4788 -6.1; 5267 -1.1; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.7; 10263 -2.4; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 214 Hz  | 0.87 | -6.1 dB |
| Peaking | 1940 Hz | 1.89 | -4.7 dB |
| Peaking | 3449 Hz | 2.18 | 6.0 dB  |
| Peaking | 4747 Hz | 3.24 | -9.7 dB |
| Peaking | 6017 Hz | 4.04 | 8.7 dB  |
| Peaking | 20 Hz   | 0.78 | 3.2 dB  |
| Peaking | 46 Hz   | 1.39 | 0.8 dB  |
| Peaking | 122 Hz  | 2.83 | -1.1 dB |
| Peaking | 802 Hz  | 3.41 | 1.8 dB  |
| Peaking | 9963 Hz | 7.14 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Shure%20SE215/Shure%20SE215.png)
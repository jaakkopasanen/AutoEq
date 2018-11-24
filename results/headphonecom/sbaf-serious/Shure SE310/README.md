# Shure SE310

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.2; 25 5.2; 28 5.1; 31 4.9; 34 4.8; 37 4.8; 41 4.6; 45 4.3; 49 4.1; 54 3.9; 60 3.7; 66 3.3; 72 2.8; 79 2.5; 87 2.2; 96 1.9; 106 1.6; 116 1.4; 128 1.1; 141 0.8; 155 0.6; 170 0.4; 187 0.3; 206 0.2; 227 0.2; 249 0.1; 274 0.1; 302 0.2; 332 0.4; 365 0.6; 402 0.7; 442 0.9; 486 1.1; 535 1.2; 588 1.4; 647 1.4; 712 1.4; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.8; 1526 -3.6; 1678 -4.2; 1846 -4.1; 2031 -3.7; 2234 -2.6; 2457 -0.7; 2703 2.1; 2973 5.2; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.0; 4788 5.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE310 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.65 | 4.1 dB  |
| Peaking | 43 Hz   | 0.56 | 3.4 dB  |
| Peaking | 1906 Hz | 1.8  | -6.2 dB |
| Peaking | 3424 Hz | 1.63 | 7.1 dB  |
| Peaking | 5732 Hz | 3.05 | 5.2 dB  |
| Peaking | 693 Hz  | 1.38 | 1.8 dB  |
| Peaking | 1225 Hz | 4.02 | -0.7 dB |
| Peaking | 1461 Hz | 5.89 | -1.0 dB |
| Peaking | 6582 Hz | 7.9  | 2.1 dB  |
| Peaking | 7841 Hz | 2.29 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE310/Shure%20SE310.png)
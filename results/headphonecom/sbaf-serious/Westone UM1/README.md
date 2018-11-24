# Westone UM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.4; 49 4.9; 54 4.4; 60 3.8; 66 3.3; 72 2.8; 79 2.3; 87 1.9; 96 1.4; 106 1.0; 116 0.7; 128 0.5; 141 -0.1; 155 -0.3; 170 -0.5; 187 -0.6; 206 -0.7; 227 -0.8; 249 -0.8; 274 -0.8; 302 -0.7; 332 -0.5; 365 -0.4; 402 -0.2; 442 -0.2; 486 -0.1; 535 0.1; 588 0.6; 647 0.8; 712 0.9; 783 0.8; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.3; 1526 -1.8; 1678 -1.8; 1846 -1.3; 2031 -0.5; 2234 0.6; 2457 2.2; 2703 3.8; 2973 5.4; 3270 6.0; 3597 6.0; 3957 5.9; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.45 | 6.3 dB  |
| Peaking | 183 Hz  | 0.59 | -1.4 dB |
| Peaking | 711 Hz  | 1.9  | 1.2 dB  |
| Peaking | 1712 Hz | 1.61 | -3.7 dB |
| Peaking | 3955 Hz | 0.95 | 7.2 dB  |
| Peaking | 3029 Hz | 5.52 | 1.2 dB  |
| Peaking | 4054 Hz | 3.51 | -1.1 dB |
| Peaking | 6268 Hz | 2.6  | 4.9 dB  |
| Peaking | 7407 Hz | 1.53 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM1/Westone%20UM1.png)
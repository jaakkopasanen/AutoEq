# Shure SE315

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.9; 106 5.1; 116 4.3; 128 3.5; 141 2.8; 155 2.3; 170 1.9; 187 1.4; 206 1.1; 227 0.9; 249 0.8; 274 0.7; 302 0.8; 332 0.9; 365 1.1; 402 1.2; 442 1.4; 486 1.7; 535 1.9; 588 2.1; 647 2.2; 712 2.2; 783 2.0; 861 1.5; 947 0.7; 1042 -0.6; 1146 -2.0; 1261 -3.0; 1387 -4.0; 1526 -4.5; 1678 -4.0; 1846 -2.3; 2031 0.3; 2234 3.4; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.39 | 6.7 dB  |
| Peaking | 732 Hz  | 1.39 | 3.1 dB  |
| Peaking | 1603 Hz | 1.32 | -9.0 dB |
| Peaking | 2665 Hz | 1.07 | 9.1 dB  |
| Peaking | 5476 Hz | 2.46 | 4.8 dB  |
| Peaking | 16 Hz   | 1.05 | 1.9 dB  |
| Peaking | 40 Hz   | 1.04 | -1.2 dB |
| Peaking | 95 Hz   | 2.56 | 1.5 dB  |
| Peaking | 204 Hz  | 1.73 | -0.9 dB |
| Peaking | 8431 Hz | 3.74 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Shure%20SE315/Shure%20SE315.png)
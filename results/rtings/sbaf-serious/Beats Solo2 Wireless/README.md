# Beats Solo2 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -5.4; 23 -5.8; 25 -6.1; 28 -6.5; 31 -6.8; 34 -7.0; 37 -7.1; 41 -7.2; 45 -7.3; 49 -7.5; 54 -7.6; 60 -7.7; 66 -7.7; 72 -7.7; 79 -7.6; 87 -7.7; 96 -7.7; 106 -7.8; 116 -7.9; 128 -7.9; 141 -7.9; 155 -7.7; 170 -7.5; 187 -7.3; 206 -6.9; 227 -6.4; 249 -5.7; 274 -4.9; 302 -3.9; 332 -3.1; 365 -2.4; 402 -1.1; 442 -0.6; 486 -0.3; 535 0.2; 588 0.6; 647 1.2; 712 1.4; 783 1.2; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.4; 1387 -2.2; 1526 -2.9; 1678 -3.5; 1846 -3.4; 2031 -2.8; 2234 -2.2; 2457 -1.7; 2703 -1.9; 2973 -2.5; 3270 -2.5; 3597 -2.6; 3957 -0.7; 4353 -0.5; 4788 -3.0; 5267 0.2; 5793 1.9; 6373 -0.6; 7010 -1.2; 7711 -1.7; 8482 -3.9; 9330 -4.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 49 Hz   |  0.38 | -7.5 dB |
| Peaking | 177 Hz  |  1.09 | -5.0 dB |
| Peaking | 1748 Hz |  2.77 | -3.6 dB |
| Peaking | 3223 Hz |  2.56 | -2.5 dB |
| Peaking | 8877 Hz |  4.88 | -4.8 dB |
| Peaking | 280 Hz  |  2.69 | -1.2 dB |
| Peaking | 754 Hz  |  1.07 | 2.8 dB  |
| Peaking | 1143 Hz |  1.08 | -1.5 dB |
| Peaking | 5757 Hz | 12.25 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Solo2%20Wireless/Beats%20Solo2%20Wireless.png)
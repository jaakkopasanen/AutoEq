# Beats Studio Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 2.5; 28 1.3; 31 0.4; 34 -0.2; 37 -0.6; 41 -0.9; 45 -1.1; 49 -1.3; 54 -1.5; 60 -1.8; 66 -2.0; 72 -2.1; 79 -2.1; 87 -2.2; 96 -2.4; 106 -2.5; 116 -2.5; 128 -2.3; 141 -2.1; 155 -1.8; 170 -1.5; 187 -1.1; 206 -0.5; 227 0.2; 249 1.1; 274 2.2; 302 3.5; 332 5.2; 365 6.0; 402 6.0; 442 6.0; 486 5.1; 535 2.4; 588 1.7; 647 1.4; 712 0.6; 783 -0.2; 861 -0.5; 947 -0.1; 1042 -0.0; 1146 -0.5; 1261 -0.9; 1387 -1.0; 1526 -0.9; 1678 -0.9; 1846 -0.2; 2031 1.0; 2234 2.4; 2457 3.5; 2703 4.5; 2973 4.1; 3270 3.2; 3597 2.8; 3957 1.6; 4353 2.7; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -2.3; 10263 -2.5; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.64 | 6.3 dB  |
| Peaking | 273 Hz  |  0.17 | -3.6 dB |
| Peaking | 393 Hz  |  1.11 | 9.9 dB  |
| Peaking | 2724 Hz |  2.31 | 5.0 dB  |
| Peaking | 5486 Hz |  2.68 | 6.8 dB  |
| Peaking | 550 Hz  | 11.32 | -1.0 dB |
| Peaking | 1059 Hz |  4.13 | 1.1 dB  |
| Peaking | 1465 Hz |  1.11 | -0.8 dB |
| Peaking | 3380 Hz |  0.18 | 0.4 dB  |
| Peaking | 9736 Hz |  3.64 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Studio%20Wireless/Beats%20Studio%20Wireless.png)
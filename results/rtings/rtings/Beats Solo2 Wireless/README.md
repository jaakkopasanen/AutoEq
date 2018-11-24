# Beats Solo2 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.1; 49 -7.1; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.7; 79 -7.8; 87 -8.0; 96 -8.1; 106 -8.3; 116 -8.4; 128 -8.4; 141 -8.4; 155 -8.3; 170 -8.2; 187 -7.9; 206 -7.4; 227 -6.9; 249 -6.3; 274 -5.5; 302 -4.7; 332 -4.0; 365 -3.4; 402 -2.2; 442 -1.8; 486 -1.5; 535 -1.0; 588 -0.4; 647 0.1; 712 0.5; 783 0.7; 861 0.6; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.6; 1387 -2.2; 1526 -2.5; 1678 -3.1; 1846 -3.4; 2031 -3.3; 2234 -2.7; 2457 -2.2; 2703 -2.5; 2973 -3.5; 3270 -4.3; 3597 -4.8; 3957 -1.9; 4353 -0.5; 4788 -2.8; 5267 -0.2; 5793 0.5; 6373 -3.1; 7010 -3.7; 7711 -2.8; 8482 -4.3; 9330 -5.5; 10263 -2.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.34 | -6.6 dB |
| Peaking | 134 Hz  | 0.92 | -4.9 dB |
| Peaking | 238 Hz  | 1.51 | -3.4 dB |
| Peaking | 2706 Hz | 0.89 | -3.5 dB |
| Peaking | 8890 Hz | 3.09 | -5.1 dB |
| Peaking | 349 Hz  | 4.07 | -0.7 dB |
| Peaking | 800 Hz  | 1.94 | 1.8 dB  |
| Peaking | 1563 Hz | 2.87 | -1.4 dB |
| Peaking | 5662 Hz | 6.74 | 2.8 dB  |
| Peaking | 6648 Hz | 6.92 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20Solo2%20Wireless/Beats%20Solo2%20Wireless.png)
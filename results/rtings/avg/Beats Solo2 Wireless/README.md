# Beats Solo2 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.1; 49 -7.1; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.7; 79 -7.8; 87 -8.0; 96 -8.1; 106 -8.3; 116 -8.4; 128 -8.4; 141 -8.4; 155 -8.3; 170 -8.2; 187 -7.9; 206 -7.4; 227 -6.9; 249 -6.3; 274 -5.5; 302 -4.7; 332 -4.0; 365 -3.4; 402 -2.2; 442 -1.8; 486 -1.5; 535 -1.0; 588 -0.4; 647 0.1; 712 0.5; 783 0.7; 861 0.6; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.6; 1387 -2.2; 1526 -2.5; 1678 -3.1; 1846 -3.4; 2031 -3.3; 2234 -2.6; 2457 -2.2; 2703 -2.7; 2973 -4.0; 3270 -5.0; 3597 -5.8; 3957 -3.1; 4353 -1.8; 4788 -4.6; 5267 -2.7; 5793 -2.0; 6373 -4.4; 7010 -4.6; 7711 -4.2; 8482 -5.0; 9330 -4.1; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.34 | -6.6 dB |
| Peaking | 134 Hz   | 0.92 | -4.9 dB |
| Peaking | 238 Hz   | 1.5  | -3.4 dB |
| Peaking | 3181 Hz  | 0.82 | -4.0 dB |
| Peaking | 7973 Hz  | 2.25 | -4.3 dB |
| Peaking | 424 Hz   | 1.15 | -0.6 dB |
| Peaking | 827 Hz   | 1.18 | 2.4 dB  |
| Peaking | 1709 Hz  | 0.85 | -2.0 dB |
| Peaking | 2479 Hz  | 3.73 | 2.7 dB  |
| Peaking | 11134 Hz | 4.79 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo2%20Wireless/Beats%20Solo2%20Wireless.png)
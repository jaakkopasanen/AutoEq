# Beats Solo3 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -5.4; 23 -5.8; 25 -6.1; 28 -6.5; 31 -6.8; 34 -7.0; 37 -7.1; 41 -7.2; 45 -7.3; 49 -7.4; 54 -7.6; 60 -7.7; 66 -7.7; 72 -7.7; 79 -7.6; 87 -7.6; 96 -7.7; 106 -7.8; 116 -7.9; 128 -7.9; 141 -7.9; 155 -7.7; 170 -7.5; 187 -7.3; 206 -6.9; 227 -6.4; 249 -5.7; 274 -4.8; 302 -3.9; 332 -3.1; 365 -2.4; 402 -1.9; 442 -1.9; 486 -1.2; 535 -0.4; 588 0.3; 647 1.0; 712 1.4; 783 1.3; 861 0.9; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.7; 1387 -2.6; 1526 -3.4; 1678 -3.8; 1846 -4.1; 2031 -3.7; 2234 -3.3; 2457 -3.0; 2703 -3.6; 2973 -4.3; 3270 -4.4; 3597 -4.6; 3957 -3.2; 4353 -3.4; 4788 -4.1; 5267 -1.0; 5793 1.1; 6373 -0.5; 7010 -1.5; 7711 -2.3; 8482 -5.0; 9330 -6.0; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-15**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.36 | -7.4 dB |
| Peaking | 178 Hz   | 1.02 | -4.8 dB |
| Peaking | 1764 Hz  | 2.63 | -3.6 dB |
| Peaking | 3398 Hz  | 1.63 | -4.5 dB |
| Peaking | 9025 Hz  | 4.65 | -6.6 dB |
| Peaking | 269 Hz   | 3.44 | -0.8 dB |
| Peaking | 728 Hz   | 2.59 | 2.5 dB  |
| Peaking | 4736 Hz  | 8.87 | -2.6 dB |
| Peaking | 5767 Hz  | 7.28 | 2.7 dB  |
| Peaking | 11165 Hz | 7.38 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)
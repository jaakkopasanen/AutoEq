# Beats Studio3 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.1; 28 1.4; 31 0.8; 34 0.2; 37 -0.3; 41 -0.8; 45 -1.3; 49 -1.7; 54 -2.4; 60 -3.2; 66 -3.8; 72 -4.0; 79 -4.0; 87 -3.8; 96 -3.5; 106 -3.1; 116 -2.7; 128 -2.5; 141 -2.6; 155 -2.8; 170 -3.2; 187 -3.5; 206 -3.8; 227 -4.1; 249 -4.6; 274 -4.9; 302 -5.1; 332 -5.5; 365 -5.6; 402 -4.8; 442 -3.5; 486 -1.9; 535 -0.2; 588 1.0; 647 1.5; 712 0.8; 783 0.6; 861 0.2; 947 -0.2; 1042 0.3; 1146 0.7; 1261 0.6; 1387 0.8; 1526 1.2; 1678 1.4; 1846 1.5; 2031 1.7; 2234 2.6; 2457 3.4; 2703 2.8; 2973 0.0; 3270 -1.5; 3597 -1.1; 3957 1.8; 4353 4.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.4; 7010 2.0; 7711 0.3; 8482 0.0; 9330 -1.6; 10263 -4.1; 11289 -3.9; 12418 -1.6; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.39 | 4.4 dB  |
| Peaking | 68 Hz    | 0.54 | -4.9 dB |
| Peaking | 314 Hz   | 1.75 | -5.4 dB |
| Peaking | 5273 Hz  | 2.16 | 6.9 dB  |
| Peaking | 10662 Hz | 3.08 | -5.1 dB |
| Peaking | 416 Hz   | 4.44 | -1.8 dB |
| Peaking | 623 Hz   | 3.11 | 2.5 dB  |
| Peaking | 1472 Hz  | 2.89 | 0.4 dB  |
| Peaking | 2674 Hz  | 1.71 | 4.1 dB  |
| Peaking | 3272 Hz  | 3.58 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)
# Razer Kraken USB

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 4.9; 31 3.8; 34 2.8; 37 1.9; 41 0.8; 45 -0.2; 49 -1.2; 54 -2.4; 60 -3.7; 66 -5.0; 72 -6.0; 79 -6.9; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.2; 141 -7.9; 155 -7.5; 170 -6.9; 187 -6.1; 206 -5.1; 227 -4.4; 249 -4.6; 274 -5.5; 302 -6.7; 332 -7.6; 365 -8.1; 402 -8.3; 442 -8.0; 486 -8.5; 535 -8.5; 588 -6.9; 647 -5.4; 712 -4.3; 783 -2.9; 861 -1.4; 947 -0.3; 1042 0.2; 1146 0.9; 1261 1.7; 1387 2.7; 1526 3.8; 1678 4.4; 1846 4.3; 2031 4.6; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.6; 6373 -1.3; 7010 -2.7; 7711 -2.5; 8482 -5.9; 9330 -8.1; 10263 -3.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken USB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken USB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.86 | 7.0 dB   |
| Peaking | 103 Hz   | 0.73 | -8.6 dB  |
| Peaking | 481 Hz   | 0.98 | -8.9 dB  |
| Peaking | 4135 Hz  | 0.34 | 7.8 dB   |
| Peaking | 8716 Hz  | 1.64 | -12.7 dB |
| Peaking | 233 Hz   | 2.98 | 3.7 dB   |
| Peaking | 238 Hz   | 1.66 | -2.3 dB  |
| Peaking | 5685 Hz  | 5.17 | 3.0 dB   |
| Peaking | 6550 Hz  | 7.86 | -4.8 dB  |
| Peaking | 11017 Hz | 9.9  | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)
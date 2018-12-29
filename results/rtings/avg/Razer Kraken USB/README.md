# Razer Kraken USB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 4.9; 31 3.8; 34 2.8; 37 1.9; 41 0.8; 45 -0.2; 49 -1.2; 54 -2.4; 60 -3.7; 66 -5.0; 72 -6.0; 79 -6.9; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.2; 141 -7.9; 155 -7.5; 170 -6.9; 187 -6.1; 206 -5.1; 227 -4.4; 249 -4.6; 274 -5.5; 302 -6.7; 332 -7.6; 365 -8.1; 402 -8.3; 442 -8.0; 486 -8.5; 535 -8.5; 588 -6.9; 647 -5.4; 712 -4.3; 783 -2.9; 861 -1.4; 947 -0.3; 1042 0.2; 1146 0.9; 1261 1.7; 1387 2.7; 1526 3.8; 1678 4.4; 1846 4.3; 2031 4.6; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.0; 6373 -2.5; 7010 -3.6; 7711 -3.9; 8482 -6.5; 9330 -6.8; 10263 -1.8; 11289 0.0; 12418 0.0; 13660 -0.5; 15026 -0.1; 16529 0.0; 18182 0.0; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken USB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken USB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.84 | 7.0 dB   |
| Peaking | 102 Hz   | 0.72 | -8.6 dB  |
| Peaking | 479 Hz   | 1.02 | -8.8 dB  |
| Peaking | 4120 Hz  | 0.38 | 8.3 dB   |
| Peaking | 8244 Hz  | 1.48 | -12.4 dB |
| Peaking | 237 Hz   | 5.91 | 1.4 dB   |
| Peaking | 330 Hz   | 5.76 | -1.1 dB  |
| Peaking | 5473 Hz  | 5.94 | 3.1 dB   |
| Peaking | 6400 Hz  | 7.99 | -4.0 dB  |
| Peaking | 10915 Hz | 9.2  | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)
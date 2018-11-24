# Razer Kraken USB

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.0; 31 3.8; 34 2.7; 37 1.8; 41 0.6; 45 -0.5; 49 -1.5; 54 -2.7; 60 -4.0; 66 -5.1; 72 -6.0; 79 -6.7; 87 -7.3; 96 -7.6; 106 -7.7; 116 -7.7; 128 -7.6; 141 -7.3; 155 -6.9; 170 -6.2; 187 -5.5; 206 -4.6; 227 -3.9; 249 -4.0; 274 -4.8; 302 -5.8; 332 -6.6; 365 -7.1; 402 -7.2; 442 -6.8; 486 -7.3; 535 -7.3; 588 -5.8; 647 -4.4; 712 -3.5; 783 -2.4; 861 -1.2; 947 -0.3; 1042 0.2; 1146 1.1; 1261 2.0; 1387 2.7; 1526 3.4; 1678 4.0; 1846 4.4; 2031 5.0; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 1.3; 7010 -0.2; 7711 -1.4; 8482 -5.5; 9330 -6.6; 10263 -0.7; 11289 0.0
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
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.96 | 7.2 dB   |
| Peaking | 100 Hz  | 0.71 | -8.1 dB  |
| Peaking | 481 Hz  | 0.99 | -7.6 dB  |
| Peaking | 3504 Hz | 0.41 | 6.9 dB   |
| Peaking | 8796 Hz | 2.6  | -10.4 dB |
| Peaking | 168 Hz  | 2.17 | -1.8 dB  |
| Peaking | 226 Hz  | 1.16 | 1.9 dB   |
| Peaking | 322 Hz  | 3.06 | -1.7 dB  |
| Peaking | 5801 Hz | 5.1  | 2.4 dB   |
| Peaking | 6557 Hz | 7.59 | -3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)
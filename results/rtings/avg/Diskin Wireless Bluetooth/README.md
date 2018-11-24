# Diskin Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 0.1; 28 -2.4; 31 -4.0; 34 -4.6; 37 -4.6; 41 -3.9; 45 -3.3; 49 -2.7; 54 -2.1; 60 -1.7; 66 -1.6; 72 -1.5; 79 -1.5; 87 -1.6; 96 -1.8; 106 -2.0; 116 -2.2; 128 -2.4; 141 -2.6; 155 -2.7; 170 -2.7; 187 -2.7; 206 -2.5; 227 -2.4; 249 -2.4; 274 -2.4; 302 -2.3; 332 -2.0; 365 -1.5; 402 -1.1; 442 0.1; 486 1.7; 535 2.6; 588 3.0; 647 3.0; 712 2.6; 783 2.1; 861 1.4; 947 0.6; 1042 -0.4; 1146 -1.1; 1261 -2.1; 1387 -3.2; 1526 -4.0; 1678 -3.8; 1846 -2.6; 2031 -1.2; 2234 0.1; 2457 1.8; 2703 2.7; 2973 2.2; 3270 1.5; 3597 1.7; 3957 2.4; 4353 3.3; 4788 5.5; 5267 6.0; 5793 5.5; 6373 3.9; 7010 1.6; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Diskin Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Diskin Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 2.42 | -4.6 dB |
| Peaking | 236 Hz  | 0.41 | -3.1 dB |
| Peaking | 610 Hz  | 1.47 | 5.1 dB  |
| Peaking | 1543 Hz | 2.92 | -4.8 dB |
| Peaking | 5162 Hz | 1.94 | 6.2 dB  |
| Peaking | 85 Hz   | 2.23 | 0.2 dB  |
| Peaking | 1896 Hz | 4.64 | -0.9 dB |
| Peaking | 2682 Hz | 3.71 | 2.7 dB  |
| Peaking | 6048 Hz | 2.89 | 3.1 dB  |
| Peaking | 6478 Hz | 1.21 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Diskin%20Wireless%20Bluetooth/Diskin%20Wireless%20Bluetooth.png)
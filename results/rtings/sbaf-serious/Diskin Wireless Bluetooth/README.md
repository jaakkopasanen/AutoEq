# Diskin Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.3; 25 0.3; 28 -2.2; 31 -3.9; 34 -4.7; 37 -4.7; 41 -4.1; 45 -3.5; 49 -3.0; 54 -2.5; 60 -2.0; 66 -1.8; 72 -1.5; 79 -1.3; 87 -1.3; 96 -1.4; 106 -1.5; 116 -1.7; 128 -1.9; 141 -2.0; 155 -2.1; 170 -2.1; 187 -2.1; 206 -2.0; 227 -1.9; 249 -1.8; 274 -1.7; 302 -1.5; 332 -1.1; 365 -0.5; 402 -0.1; 442 1.2; 486 2.9; 535 3.8; 588 4.1; 647 4.0; 712 3.5; 783 2.6; 861 1.6; 947 0.6; 1042 -0.3; 1146 -0.9; 1261 -1.8; 1387 -3.2; 1526 -4.4; 1678 -4.2; 1846 -2.6; 2031 -0.8; 2234 0.5; 2457 2.3; 2703 3.5; 2973 3.8; 3270 4.1; 3597 4.8; 3957 4.9; 4353 4.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -0.2; 10263 0.0
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
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 2.22 | -4.7 dB |
| Peaking | 283 Hz  | 0.38 | -2.7 dB |
| Peaking | 596 Hz  | 1.4  | 6.5 dB  |
| Peaking | 1575 Hz | 2.48 | -5.7 dB |
| Peaking | 4387 Hz | 1.01 | 6.2 dB  |
| Peaking | 56 Hz   | 3.45 | -0.6 dB |
| Peaking | 2712 Hz | 5.53 | 1.4 dB  |
| Peaking | 4239 Hz | 6.26 | -1.6 dB |
| Peaking | 6307 Hz | 2.53 | 4.6 dB  |
| Peaking | 7527 Hz | 1.57 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Diskin%20Wireless%20Bluetooth/Diskin%20Wireless%20Bluetooth.png)
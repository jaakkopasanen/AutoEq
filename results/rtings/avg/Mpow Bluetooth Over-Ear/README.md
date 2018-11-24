# Mpow Bluetooth Over-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.6; 28 -4.9; 31 -5.0; 34 -5.1; 37 -5.1; 41 -5.0; 45 -5.1; 49 -5.2; 54 -5.4; 60 -5.8; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.3; 96 -7.8; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.4; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.3; 227 -8.9; 249 -8.4; 274 -7.7; 302 -7.2; 332 -6.6; 365 -4.9; 402 -2.9; 442 -1.2; 486 -0.6; 535 0.2; 588 1.2; 647 2.5; 712 3.4; 783 3.2; 861 1.8; 947 0.6; 1042 -0.4; 1146 -0.9; 1261 -0.9; 1387 -0.9; 1526 -1.0; 1678 -1.3; 1846 -1.7; 2031 -1.9; 2234 -1.6; 2457 -2.0; 2703 -3.0; 2973 -4.2; 3270 -5.2; 3597 -4.8; 3957 -2.4; 4353 -0.5; 4788 1.7; 5267 0.2; 5793 2.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -2.3; 12418 -5.5; 13660 -5.5; 15026 -5.8; 16529 -3.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 61 Hz    | 0.36 | -5.6 dB |
| Peaking | 192 Hz   | 1.02 | -7.6 dB |
| Peaking | 3239 Hz  | 2.46 | -5.5 dB |
| Peaking | 6306 Hz  | 3.76 | 6.2 dB  |
| Peaking | 14139 Hz | 1.71 | -6.6 dB |
| Peaking | 23 Hz    | 1.96 | -0.9 dB |
| Peaking | 322 Hz   | 3.53 | -2.8 dB |
| Peaking | 741 Hz   | 1.43 | 6.2 dB  |
| Peaking | 1040 Hz  | 1.02 | -2.9 dB |
| Peaking | 18227 Hz | 4.37 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)
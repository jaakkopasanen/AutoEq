# V-Moda Crossfade Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.5; 28 -0.8; 31 -1.8; 34 -2.5; 37 -3.0; 41 -3.6; 45 -3.9; 49 -4.2; 54 -4.4; 60 -4.5; 66 -4.1; 72 -4.1; 79 -5.1; 87 -5.9; 96 -6.0; 106 -5.4; 116 -5.9; 128 -6.2; 141 -6.3; 155 -6.2; 170 -5.3; 187 -5.2; 206 -4.4; 227 -3.2; 249 -1.9; 274 -0.2; 302 1.8; 332 3.4; 365 4.8; 402 5.5; 442 5.3; 486 5.4; 535 5.2; 588 4.9; 647 4.5; 712 3.5; 783 2.7; 861 1.5; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.0; 1387 -1.4; 1526 -1.7; 1678 -1.6; 1846 -1.1; 2031 -0.4; 2234 -0.7; 2457 -1.0; 2703 -0.1; 2973 -0.6; 3270 -1.8; 3597 -4.0; 3957 -1.7; 4353 0.7; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -4.2; 10263 -4.4; 11289 -0.7; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 2.05 | -2.1 dB |
| Peaking | 148 Hz  | 0.52 | -7.2 dB |
| Peaking | 421 Hz  | 1.15 | 8.9 dB  |
| Peaking | 5746 Hz | 3.28 | 7.4 dB  |
| Peaking | 9780 Hz | 4.06 | -5.6 dB |
| Peaking | 19 Hz   | 2.79 | 3.5 dB  |
| Peaking | 684 Hz  | 3.23 | 1.9 dB  |
| Peaking | 1413 Hz | 1.36 | -2.1 dB |
| Peaking | 3657 Hz | 4.57 | -4.6 dB |
| Peaking | 4818 Hz | 7.81 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Bluetooth/V-Moda%20Crossfade%20Wireless%20Bluetooth.png)
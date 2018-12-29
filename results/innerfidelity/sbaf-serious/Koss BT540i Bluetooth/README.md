# Koss BT540i Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.3; 23 -6.8; 25 -7.2; 28 -7.6; 31 -8.0; 34 -8.3; 37 -8.5; 41 -8.7; 45 -8.9; 49 -8.9; 54 -8.9; 60 -9.0; 66 -9.0; 72 -9.0; 79 -9.1; 87 -9.0; 96 -9.0; 106 -8.7; 116 -8.5; 128 -8.3; 141 -8.3; 155 -8.4; 170 -7.5; 187 -7.2; 206 -7.4; 227 -6.9; 249 -6.1; 274 -5.2; 302 -3.8; 332 -3.3; 365 -2.3; 402 -1.0; 442 0.1; 486 0.7; 535 1.3; 588 1.8; 647 1.4; 712 0.7; 783 0.4; 861 0.1; 947 -0.0; 1042 0.1; 1146 -0.1; 1261 -0.5; 1387 -1.0; 1526 -1.3; 1678 -2.0; 1846 -2.4; 2031 -2.6; 2234 -3.3; 2457 -3.8; 2703 -4.6; 2973 -5.1; 3270 -4.5; 3597 -2.8; 3957 -0.3; 4353 1.7; 4788 5.7; 5267 3.7; 5793 2.9; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -1.2; 10263 -0.0; 11289 0.0; 12418 -0.4; 13660 -0.9; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss BT540i Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.41 | -6.8 dB |
| Peaking | 186 Hz  | 0.37 | -7.2 dB |
| Peaking | 522 Hz  | 0.91 | 5.5 dB  |
| Peaking | 3272 Hz | 1.05 | -7.4 dB |
| Peaking | 4865 Hz | 1.7  | 8.9 dB  |
| Peaking | 1135 Hz | 6.37 | 0.5 dB  |
| Peaking | 4979 Hz | 9.56 | 2.0 dB  |
| Peaking | 5469 Hz | 8.66 | -3.0 dB |
| Peaking | 6536 Hz | 4.45 | 3.3 dB  |
| Peaking | 8034 Hz | 1.32 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Bluetooth/Koss%20BT540i%20Bluetooth.png)
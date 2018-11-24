# Mpow Bluetooth Over-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.1; 37 -5.2; 41 -5.2; 45 -5.4; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.3; 72 -6.5; 79 -6.6; 87 -6.9; 96 -7.4; 106 -7.9; 116 -8.3; 128 -8.7; 141 -8.8; 155 -9.0; 170 -9.0; 187 -8.9; 206 -8.8; 227 -8.4; 249 -7.8; 274 -7.0; 302 -6.3; 332 -5.6; 365 -3.9; 402 -1.8; 442 -0.1; 486 0.6; 535 1.4; 588 2.3; 647 3.5; 712 4.3; 783 3.7; 861 2.0; 947 0.7; 1042 -0.4; 1146 -0.7; 1261 -0.7; 1387 -0.9; 1526 -1.3; 1678 -1.6; 1846 -1.7; 2031 -1.5; 2234 -1.1; 2457 -1.6; 2703 -2.1; 2973 -2.6; 3270 -2.7; 3597 -1.6; 3957 -0.0; 4353 0.8; 4788 3.3; 5267 3.2; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.57 | -3.4 dB |
| Peaking | 230 Hz  |  0.5  | -4.7 dB |
| Peaking | 462 Hz  |  0.17 | -8.7 dB |
| Peaking | 629 Hz  |  0.64 | 14.0 dB |
| Peaking | 5841 Hz |  2.54 | 7.0 dB  |
| Peaking | 1049 Hz |  5.67 | -1.2 dB |
| Peaking | 2573 Hz |  1.26 | 1.2 dB  |
| Peaking | 3121 Hz |  3.33 | -2.2 dB |
| Peaking | 4748 Hz | 10.12 | 1.5 dB  |
| Peaking | 7945 Hz |  5.38 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)
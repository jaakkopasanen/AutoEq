# Anker SoundBuds Curve

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -8.6; 23 -8.5; 25 -8.4; 28 -8.1; 31 -7.8; 34 -7.5; 37 -7.2; 41 -6.8; 45 -6.4; 49 -6.0; 54 -5.7; 60 -5.5; 66 -5.4; 72 -5.2; 79 -5.1; 87 -5.3; 96 -5.6; 106 -6.1; 116 -6.7; 128 -7.2; 141 -7.4; 155 -7.1; 170 -6.3; 187 -5.2; 206 -3.4; 227 -1.4; 249 -0.3; 274 -0.5; 302 -1.0; 332 -1.2; 365 -1.2; 402 -1.2; 442 -1.0; 486 -0.7; 535 -0.4; 588 -0.1; 647 0.4; 712 1.0; 783 1.1; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.8; 1526 -1.2; 1678 -1.3; 1846 -1.2; 2031 -1.1; 2234 -0.8; 2457 -0.7; 2703 -1.0; 2973 -1.2; 3270 -0.7; 3597 -0.1; 3957 -1.1; 4353 -3.1; 4788 -3.6; 5267 -3.4; 5793 -2.7; 6373 -1.3; 7010 1.3; 7711 0.3; 8482 -0.8; 9330 -3.6; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Curve GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Curve ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.63 | -7.0 dB |
| Peaking | 46 Hz    | 0.48 | -4.1 dB |
| Peaking | 141 Hz   | 1.67 | -6.1 dB |
| Peaking | 4947 Hz  | 2.42 | -3.8 dB |
| Peaking | 22142 Hz | 2.03 | -0.7 dB |
| Peaking | 252 Hz   | 4.48 | 2.2 dB  |
| Peaking | 782 Hz   | 1.24 | 3.7 dB  |
| Peaking | 809 Hz   | 0.51 | -2.5 dB |
| Peaking | 7407 Hz  | 3.03 | 1.8 dB  |
| Peaking | 9216 Hz  | 6.45 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Anker%20SoundBuds%20Curve/Anker%20SoundBuds%20Curve.png)
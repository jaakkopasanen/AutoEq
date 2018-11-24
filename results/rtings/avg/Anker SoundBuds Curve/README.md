# Anker SoundBuds Curve

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -9.0; 23 -8.8; 25 -8.6; 28 -8.3; 31 -7.9; 34 -7.5; 37 -7.1; 41 -6.6; 45 -6.1; 49 -5.7; 54 -5.4; 60 -5.3; 66 -5.3; 72 -5.2; 79 -5.3; 87 -5.6; 96 -6.1; 106 -6.6; 116 -7.2; 128 -7.7; 141 -8.0; 155 -7.7; 170 -7.0; 187 -5.8; 206 -3.9; 227 -1.9; 249 -0.9; 274 -1.2; 302 -1.8; 332 -2.1; 365 -2.3; 402 -2.3; 442 -2.1; 486 -1.9; 535 -1.6; 588 -1.2; 647 -0.7; 712 0.1; 783 0.6; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.8; 1678 -0.9; 1846 -1.2; 2031 -1.5; 2234 -1.3; 2457 -1.1; 2703 -1.8; 2973 -2.8; 3270 -3.3; 3597 -3.3; 3957 -3.5; 4353 -4.4; 4788 -5.2; 5267 -6.4; 5793 -6.6; 6373 -5.1; 7010 -1.8; 7711 0.3; 8482 -0.3; 9330 -2.4; 10263 -0.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.9; 16529 -1.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Curve GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Curve ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.59 | -7.7 dB |
| Peaking | 41 Hz   | 0.41 | -3.8 dB |
| Peaking | 141 Hz  | 1.52 | -6.7 dB |
| Peaking | 435 Hz  | 2.74 | -1.8 dB |
| Peaking | 5044 Hz | 1.38 | -6.1 dB |
| Peaking | 247 Hz  | 7.42 | 1.7 dB  |
| Peaking | 831 Hz  | 5    | 1.3 dB  |
| Peaking | 4512 Hz | 2.19 | 5.0 dB  |
| Peaking | 5077 Hz | 1.01 | -4.3 dB |
| Peaking | 7633 Hz | 4.07 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Curve/Anker%20SoundBuds%20Curve.png)
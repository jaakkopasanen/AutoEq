# Anker SoundBuds Sport

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.3; 45 3.4; 49 1.7; 54 -0.2; 60 -2.0; 66 -3.4; 72 -4.4; 79 -5.4; 87 -6.4; 96 -7.2; 106 -8.1; 116 -8.8; 128 -9.5; 141 -10.0; 155 -10.2; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.7; 332 -8.0; 365 -7.2; 402 -6.4; 442 -5.6; 486 -4.7; 535 -3.6; 588 -2.5; 647 -1.3; 712 -0.3; 783 0.5; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 -0.2; 1526 -0.0; 1678 0.1; 1846 0.1; 2031 0.1; 2234 0.7; 2457 1.4; 2703 1.5; 2973 1.1; 3270 0.8; 3597 0.9; 3957 1.3; 4353 1.6; 4788 2.7; 5267 3.5; 5793 3.8; 6373 2.2; 7010 0.3; 7711 -3.2; 8482 -4.6; 9330 -1.9; 10263 0.0; 11289 0.0; 12418 -0.3; 13660 -6.0; 15026 -9.0; 16529 -5.2; 18182 -2.7; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1    | 8.6 dB   |
| Peaking | 168 Hz   | 0.52 | -11.5 dB |
| Peaking | 8414 Hz  | 2.95 | -9.4 dB  |
| Peaking | 11579 Hz | 0.47 | 15.5 dB  |
| Peaking | 14594 Hz | 0.72 | -20.7 dB |
| Peaking | 17 Hz    | 2.78 | 2.5 dB   |
| Peaking | 808 Hz   | 3.17 | 2.8 dB   |
| Peaking | 4884 Hz  | 1.13 | -2.0 dB  |
| Peaking | 5492 Hz  | 2.75 | 3.3 dB   |
| Peaking | 24000 Hz | 2.06 | 0.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)
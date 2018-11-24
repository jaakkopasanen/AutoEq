# Anker SoundBuds Life

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.4; 31 -7.5; 34 -7.4; 37 -7.3; 41 -6.9; 45 -6.6; 49 -6.2; 54 -6.0; 60 -5.9; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.7; 116 -7.1; 128 -7.3; 141 -7.5; 155 -7.7; 170 -7.9; 187 -8.1; 206 -7.2; 227 -5.8; 249 -4.4; 274 -2.9; 302 -2.2; 332 -2.3; 365 -2.6; 402 -2.7; 442 -2.4; 486 -2.0; 535 -1.3; 588 -0.6; 647 -0.0; 712 0.4; 783 0.7; 861 0.9; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.4; 1526 -2.9; 1678 -3.7; 1846 -4.5; 2031 -4.9; 2234 -4.7; 2457 -4.7; 2703 -5.5; 2973 -7.0; 3270 -7.7; 3597 -7.3; 3957 -7.2; 4353 -8.2; 4788 -9.2; 5267 -10.3; 5793 -8.1; 6373 -5.4; 7010 -3.4; 7711 -3.2; 8482 -2.8; 9330 -0.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.5; 16529 -1.4; 18182 -0.8; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.23 | -7.0 dB |
| Peaking | 170 Hz   | 1.1  | -6.2 dB |
| Peaking | 1886 Hz  | 2.19 | -3.5 dB |
| Peaking | 3207 Hz  | 2    | -5.3 dB |
| Peaking | 5199 Hz  | 1.99 | -9.1 dB |
| Peaking | 296 Hz   | 3.66 | 1.8 dB  |
| Peaking | 399 Hz   | 1.49 | -1.4 dB |
| Peaking | 790 Hz   | 2.71 | 2.0 dB  |
| Peaking | 10609 Hz | 3.81 | 1.1 dB  |
| Peaking | 20471 Hz | 1.62 | -6.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Anker%20SoundBuds%20Life/Anker%20SoundBuds%20Life.png)
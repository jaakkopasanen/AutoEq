# Anker SoundBuds Sport

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.3; 45 3.4; 49 1.7; 54 -0.2; 60 -2.0; 66 -3.4; 72 -4.4; 79 -5.4; 87 -6.4; 96 -7.2; 106 -8.1; 116 -8.8; 128 -9.5; 141 -10.0; 155 -10.2; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.7; 332 -8.0; 365 -7.2; 402 -6.4; 442 -5.6; 486 -4.7; 535 -3.6; 588 -2.5; 647 -1.3; 712 -0.3; 783 0.5; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 -0.2; 1526 -0.0; 1678 0.1; 1846 0.1; 2031 0.1; 2234 0.6; 2457 1.4; 2703 1.8; 2973 1.6; 3270 1.5; 3597 1.9; 3957 2.5; 4353 2.9; 4788 4.5; 5267 6.0; 5793 5.9; 6373 3.5; 7010 0.9; 7711 -2.8; 8482 -5.5; 9330 -4.6; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 -2.7; 15026 -6.4; 16529 -2.2; 18182 0.0; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1    | 8.7 dB   |
| Peaking | 168 Hz   | 0.52 | -11.5 dB |
| Peaking | 6229 Hz  | 0.96 | 7.6 dB   |
| Peaking | 8325 Hz  | 2.39 | -10.9 dB |
| Peaking | 15047 Hz | 3.65 | -7.5 dB  |
| Peaking | 167 Hz   | 1.51 | 2.3 dB   |
| Peaking | 247 Hz   | 0.46 | -1.8 dB  |
| Peaking | 780 Hz   | 1.95 | 3.2 dB   |
| Peaking | 4928 Hz  | 1.86 | -1.8 dB  |
| Peaking | 5311 Hz  | 3.99 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)
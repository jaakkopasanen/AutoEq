# Anker SoundBuds Sport

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.2; 45 3.2; 49 1.3; 54 -0.5; 60 -2.3; 66 -3.6; 72 -4.4; 79 -5.2; 87 -6.0; 96 -6.8; 106 -7.6; 116 -8.3; 128 -8.9; 141 -9.4; 155 -9.6; 170 -9.7; 187 -9.9; 206 -10.1; 227 -10.0; 249 -9.5; 274 -8.7; 302 -7.9; 332 -7.0; 365 -6.2; 402 -5.4; 442 -4.4; 486 -3.4; 535 -2.4; 588 -1.4; 647 -0.3; 712 0.6; 783 1.0; 861 1.0; 947 0.5; 1042 -0.2; 1146 -0.2; 1261 -0.1; 1387 -0.2; 1526 -0.4; 1678 -0.3; 1846 0.2; 2031 0.5; 2234 1.1; 2457 1.9; 2703 2.4; 2973 2.7; 3270 3.3; 3597 4.0; 3957 3.7; 4353 3.0; 4788 4.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.7; 8482 -5.1; 9330 -3.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -3.2; 16529 -0.1; 18182 0.0; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 1.09 | 8.5 dB   |
| Peaking | 166 Hz   | 0.56 | -10.8 dB |
| Peaking | 3406 Hz  | 1.2  | 2.8 dB   |
| Peaking | 5977 Hz  | 2.11 | 6.2 dB   |
| Peaking | 8450 Hz  | 3.78 | -7.4 dB  |
| Peaking | 70 Hz    | 3.41 | -1.0 dB  |
| Peaking | 169 Hz   | 1.88 | 1.9 dB   |
| Peaking | 252 Hz   | 0.88 | -1.7 dB  |
| Peaking | 742 Hz   | 2.28 | 3.0 dB   |
| Peaking | 14844 Hz | 5.81 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)
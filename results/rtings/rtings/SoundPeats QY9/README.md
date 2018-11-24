# SoundPeats QY9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.4; 28 2.8; 31 2.3; 34 1.8; 37 1.4; 41 1.0; 45 0.5; 49 0.1; 54 -0.4; 60 -1.3; 66 -2.0; 72 -2.6; 79 -3.4; 87 -4.2; 96 -5.1; 106 -6.0; 116 -6.8; 128 -7.6; 141 -8.3; 155 -8.8; 170 -9.3; 187 -9.8; 206 -10.1; 227 -10.2; 249 -10.0; 274 -9.6; 302 -9.2; 332 -8.7; 365 -8.1; 402 -7.4; 442 -6.6; 486 -5.6; 535 -4.4; 588 -3.2; 647 -1.9; 712 -1.1; 783 -0.8; 861 -0.8; 947 -0.4; 1042 0.4; 1146 1.1; 1261 1.6; 1387 2.0; 1526 3.2; 1678 4.4; 1846 5.7; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.0; 2973 2.6; 3270 1.7; 3597 1.2; 3957 0.1; 4353 -1.5; 4788 -2.1; 5267 -2.5; 5793 -3.5; 6373 -4.3; 7010 -2.5; 7711 -1.3; 8482 -3.0; 9330 -3.6; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -0.5; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 14 Hz   | 0.37 | 5.1 dB   |
| Peaking | 218 Hz  | 0.51 | -10.7 dB |
| Peaking | 2596 Hz | 0.77 | 9.6 dB   |
| Peaking | 3081 Hz | 3.15 | -3.3 dB  |
| Peaking | 5260 Hz | 0.86 | -6.7 dB  |
| Peaking | 416 Hz  | 2.99 | -0.8 dB  |
| Peaking | 681 Hz  | 3.85 | 1.3 dB   |
| Peaking | 1364 Hz | 6.18 | -0.8 dB  |
| Peaking | 9155 Hz | 5.42 | -4.6 dB  |
| Peaking | 9734 Hz | 1.91 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SoundPeats%20QY9/SoundPeats%20QY9.png)
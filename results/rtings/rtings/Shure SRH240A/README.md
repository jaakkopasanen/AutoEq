# Shure SRH240A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.4; 66 4.5; 72 3.8; 79 3.2; 87 2.5; 96 2.1; 106 1.8; 116 1.5; 128 1.4; 141 1.5; 155 1.7; 170 2.1; 187 2.8; 206 3.3; 227 3.8; 249 4.0; 274 3.8; 302 3.1; 332 1.8; 365 1.3; 402 0.6; 442 -0.6; 486 -1.8; 535 -2.3; 588 -2.4; 647 -2.0; 712 -1.4; 783 -0.9; 861 -0.5; 947 -0.2; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.4; 1526 -0.8; 1678 -1.1; 1846 -1.2; 2031 -0.6; 2234 0.6; 2457 1.8; 2703 2.3; 2973 2.1; 3270 1.7; 3597 2.5; 3957 3.5; 4353 4.4; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -3.7; 11289 -2.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.58 | 6.7 dB  |
| Peaking | 257 Hz   | 1.68 | 4.1 dB  |
| Peaking | 564 Hz   | 1.86 | -3.0 dB |
| Peaking | 5279 Hz  | 1.54 | 6.6 dB  |
| Peaking | 10342 Hz | 3.29 | -4.7 dB |
| Peaking | 58 Hz    | 0.94 | -1.6 dB |
| Peaking | 58 Hz    | 2.01 | 2.6 dB  |
| Peaking | 1833 Hz  | 3.21 | -2.0 dB |
| Peaking | 2738 Hz  | 2.69 | 2.1 dB  |
| Peaking | 3175 Hz  | 3.6  | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Shure%20SRH240A/Shure%20SRH240A.png)
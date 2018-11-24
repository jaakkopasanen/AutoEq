# Shure SRH240A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.1; 66 4.3; 72 3.8; 79 3.4; 87 2.9; 96 2.5; 106 2.3; 116 2.0; 128 1.9; 141 2.1; 155 2.3; 170 2.8; 187 3.4; 206 3.8; 227 4.3; 249 4.6; 274 4.5; 302 3.9; 332 2.8; 365 2.3; 402 1.7; 442 0.5; 486 -0.6; 535 -1.1; 588 -1.3; 647 -1.0; 712 -0.6; 783 -0.4; 861 -0.3; 947 -0.2; 1042 0.2; 1146 0.5; 1261 0.3; 1387 -0.4; 1526 -1.1; 1678 -1.5; 1846 -1.1; 2031 -0.2; 2234 1.1; 2457 2.2; 2703 2.9; 2973 3.1; 3270 3.6; 3597 4.6; 3957 4.7; 4353 4.4; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.53 | 6.5 dB  |
| Peaking | 260 Hz  | 1.36 | 4.4 dB  |
| Peaking | 565 Hz  | 2.12 | -2.2 dB |
| Peaking | 1707 Hz | 4.03 | -2.5 dB |
| Peaking | 4656 Hz | 1.15 | 6.0 dB  |
| Peaking | 54 Hz   | 4.13 | 0.8 dB  |
| Peaking | 2710 Hz | 4.2  | 1.1 dB  |
| Peaking | 4435 Hz | 7.36 | -1.6 dB |
| Peaking | 6404 Hz | 2.73 | 4.4 dB  |
| Peaking | 7377 Hz | 1.6  | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Shure%20SRH240A/Shure%20SRH240A.png)
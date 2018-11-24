# Shure SRH240

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 5.1; 302 2.8; 332 1.4; 365 0.4; 402 -0.5; 442 -1.4; 486 -2.1; 535 -2.4; 588 -2.2; 647 -1.8; 712 -1.3; 783 -0.9; 861 -0.6; 947 -0.3; 1042 0.1; 1146 0.0; 1261 -0.5; 1387 -1.2; 1526 -1.6; 1678 -1.7; 1846 -1.4; 2031 -1.1; 2234 -1.0; 2457 -1.2; 2703 -1.3; 2973 -0.8; 3270 -0.4; 3597 -0.3; 3957 -0.3; 4353 0.1; 4788 0.4; 5267 1.9; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.5; 9330 -2.6; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 105 Hz  | 0.1  | 6.6 dB  |
| Peaking | 508 Hz  | 1.23 | -7.4 dB |
| Peaking | 1596 Hz | 0.62 | -2.7 dB |
| Peaking | 6159 Hz | 3.85 | 6.7 dB  |
| Peaking | 9183 Hz | 4.29 | -3.3 dB |
| Peaking | 15 Hz   | 0.91 | 1.2 dB  |
| Peaking | 63 Hz   | 0.68 | -0.5 dB |
| Peaking | 262 Hz  | 2.29 | 2.9 dB  |
| Peaking | 315 Hz  | 2.26 | -2.4 dB |
| Peaking | 496 Hz  | 5.07 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH240/Shure%20SRH240.png)
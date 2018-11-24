# Audio-Technica ATH-AD700X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.8; 60 5.3; 66 4.8; 72 4.4; 79 4.0; 87 3.6; 96 3.1; 106 2.5; 116 2.1; 128 1.7; 141 1.4; 155 1.2; 170 1.0; 187 0.8; 206 0.8; 227 0.9; 249 1.1; 274 1.3; 302 1.4; 332 1.3; 365 1.3; 402 1.2; 442 1.1; 486 1.1; 535 1.1; 588 1.3; 647 1.3; 712 1.1; 783 0.7; 861 0.4; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.3; 1678 -1.1; 1846 -0.1; 2031 1.2; 2234 3.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 1.9; 4353 2.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -4.3; 10263 -3.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.46 | 6.5 dB  |
| Peaking | 435 Hz  |  1.34 | 1.2 dB  |
| Peaking | 2889 Hz |  2.44 | 6.5 dB  |
| Peaking | 5645 Hz |  2.27 | 6.3 dB  |
| Peaking | 9550 Hz |  4.56 | -5.6 dB |
| Peaking | 675 Hz  |  3.99 | 0.8 dB  |
| Peaking | 1607 Hz |  2.24 | -2.2 dB |
| Peaking | 2354 Hz |  8.19 | 2.7 dB  |
| Peaking | 3613 Hz |  9.27 | 2.5 dB  |
| Peaking | 4132 Hz | 13.39 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)
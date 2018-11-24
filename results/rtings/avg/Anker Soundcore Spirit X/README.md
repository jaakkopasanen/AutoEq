# Anker Soundcore Spirit X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -5.1; 23 -5.0; 25 -5.0; 28 -4.9; 31 -4.9; 34 -4.8; 37 -4.6; 41 -4.5; 45 -4.3; 49 -4.2; 54 -4.0; 60 -4.1; 66 -4.1; 72 -4.0; 79 -4.0; 87 -3.9; 96 -3.9; 106 -3.9; 116 -3.9; 128 -3.8; 141 -3.6; 155 -3.4; 170 -3.1; 187 -2.4; 206 -1.4; 227 -0.2; 249 0.7; 274 1.1; 302 0.9; 332 0.3; 365 -0.2; 402 -0.6; 442 -0.8; 486 -0.8; 535 -0.6; 588 -0.2; 647 0.3; 712 0.8; 783 1.2; 861 1.0; 947 0.4; 1042 -0.4; 1146 -1.3; 1261 -1.9; 1387 -2.3; 1526 -2.5; 1678 -2.6; 1846 -2.7; 2031 -2.6; 2234 -1.9; 2457 -1.2; 2703 -1.1; 2973 -1.8; 3270 -2.8; 3597 -3.5; 3957 -4.2; 4353 -4.9; 4788 -5.2; 5267 -5.9; 5793 -6.3; 6373 -4.5; 7010 -0.5; 7711 0.3; 8482 -0.6; 9330 -3.0; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker Soundcore Spirit X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker Soundcore Spirit X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.38 | -5.0 dB |
| Peaking | 124 Hz   | 1.58 | -2.8 dB |
| Peaking | 1697 Hz  | 2.09 | -2.7 dB |
| Peaking | 5009 Hz  | 1.65 | -6.2 dB |
| Peaking | 24000 Hz | 2.09 | -0.2 dB |
| Peaking | 280 Hz   | 2.41 | 2.9 dB  |
| Peaking | 473 Hz   | 0.42 | -1.3 dB |
| Peaking | 782 Hz   | 2.12 | 2.6 dB  |
| Peaking | 7477 Hz  | 7.16 | 3.0 dB  |
| Peaking | 9361 Hz  | 9.8  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20Soundcore%20Spirit%20X/Anker%20Soundcore%20Spirit%20X.png)
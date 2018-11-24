# Audio-Technica ATH-M20x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.3; 31 3.3; 34 2.4; 37 1.7; 41 0.9; 45 0.2; 49 -0.4; 54 -1.2; 60 -1.9; 66 -2.4; 72 -2.6; 79 -2.6; 87 -2.5; 96 -2.5; 106 -2.7; 116 -2.8; 128 -2.8; 141 -2.3; 155 -1.5; 170 -0.4; 187 0.8; 206 2.3; 227 3.5; 249 3.8; 274 2.7; 302 1.4; 332 0.7; 365 0.1; 402 -0.4; 442 -0.8; 486 -1.0; 535 -1.1; 588 -1.0; 647 -0.9; 712 -0.6; 783 -0.3; 861 -0.1; 947 -0.0; 1042 0.2; 1146 0.0; 1261 -0.5; 1387 -1.1; 1526 -1.8; 1678 -2.4; 1846 -3.3; 2031 -3.9; 2234 -3.3; 2457 -1.9; 2703 -0.5; 2973 0.2; 3270 1.2; 3597 4.3; 3957 5.8; 4353 4.8; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.4; 7711 -1.1; 8482 -1.8; 9330 -1.4; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.8  | 7.1 dB  |
| Peaking | 114 Hz  | 0.31 | -4.1 dB |
| Peaking | 237 Hz  | 1.72 | 7.1 dB  |
| Peaking | 2048 Hz | 2.29 | -4.6 dB |
| Peaking | 4765 Hz | 1.71 | 7.0 dB  |
| Peaking | 1028 Hz | 2.51 | 1.1 dB  |
| Peaking | 3041 Hz | 0.29 | -1.0 dB |
| Peaking | 4973 Hz | 0.36 | 1.3 dB  |
| Peaking | 6322 Hz | 4.93 | 4.3 dB  |
| Peaking | 7915 Hz | 1.67 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)
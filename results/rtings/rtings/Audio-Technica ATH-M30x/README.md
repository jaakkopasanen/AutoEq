# Audio-Technica ATH-M30x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.5; 28 -0.3; 31 -0.9; 34 -1.4; 37 -1.8; 41 -2.1; 45 -2.3; 49 -2.4; 54 -2.4; 60 -2.3; 66 -2.2; 72 -2.0; 79 -1.8; 87 -1.9; 96 -2.2; 106 -2.5; 116 -2.7; 128 -2.7; 141 -2.3; 155 -1.7; 170 -0.9; 187 0.2; 206 1.7; 227 3.1; 249 4.0; 274 4.1; 302 2.6; 332 1.5; 365 0.6; 402 -0.1; 442 -0.5; 486 -0.7; 535 -0.8; 588 -0.8; 647 -0.8; 712 -0.6; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.1; 1146 -0.3; 1261 -0.8; 1387 -1.5; 1526 -2.4; 1678 -3.4; 1846 -4.3; 2031 -4.8; 2234 -3.7; 2457 -2.3; 2703 -0.9; 2973 -0.2; 3270 1.5; 3597 2.8; 3957 1.9; 4353 4.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.3; 7010 0.9; 7711 -0.8; 8482 -2.0; 9330 -3.9; 10263 -5.8; 11289 -5.8; 12418 -3.9; 13660 -1.1; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 140 Hz   | 0.35 | -3.2 dB |
| Peaking | 254 Hz   | 1.82 | 7.0 dB  |
| Peaking | 1994 Hz  | 2.25 | -5.3 dB |
| Peaking | 5304 Hz  | 1.61 | 7.5 dB  |
| Peaking | 10427 Hz | 1.76 | -7.1 dB |
| Peaking | 15 Hz    | 0.42 | 2.7 dB  |
| Peaking | 40 Hz    | 1.34 | -2.3 dB |
| Peaking | 1048 Hz  | 5.19 | 0.8 dB  |
| Peaking | 12215 Hz | 4.85 | -1.2 dB |
| Peaking | 14637 Hz | 1.93 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)
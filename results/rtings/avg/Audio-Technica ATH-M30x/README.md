# Audio-Technica ATH-M30x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.5; 28 -0.3; 31 -0.9; 34 -1.4; 37 -1.8; 41 -2.1; 45 -2.3; 49 -2.4; 54 -2.4; 60 -2.3; 66 -2.2; 72 -2.0; 79 -1.8; 87 -1.9; 96 -2.2; 106 -2.5; 116 -2.7; 128 -2.7; 141 -2.3; 155 -1.7; 170 -0.9; 187 0.2; 206 1.7; 227 3.1; 249 4.0; 274 4.1; 302 2.6; 332 1.5; 365 0.6; 402 -0.1; 442 -0.5; 486 -0.7; 535 -0.8; 588 -0.8; 647 -0.8; 712 -0.6; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.1; 1146 -0.3; 1261 -0.8; 1387 -1.5; 1526 -2.4; 1678 -3.4; 1846 -4.3; 2031 -4.8; 2234 -3.7; 2457 -2.3; 2703 -1.1; 2973 -0.7; 3270 0.8; 3597 1.8; 3957 0.7; 4353 3.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.8; 7010 0.0; 7711 -2.2; 8482 -2.7; 9330 -2.6; 10263 -4.0; 11289 -6.6; 12418 -7.1; 13660 -4.4; 15026 -2.6; 16529 -1.8; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 139 Hz   | 0.35 | -3.2 dB |
| Peaking | 254 Hz   | 1.83 | 7.0 dB  |
| Peaking | 1981 Hz  | 2.34 | -5.1 dB |
| Peaking | 5339 Hz  | 2.22 | 7.9 dB  |
| Peaking | 11759 Hz | 1.28 | -7.1 dB |
| Peaking | 14 Hz    | 0.36 | 2.8 dB  |
| Peaking | 38 Hz    | 1.29 | -2.5 dB |
| Peaking | 1046 Hz  | 5.28 | 0.8 dB  |
| Peaking | 7729 Hz  | 3.82 | -4.4 dB |
| Peaking | 7898 Hz  | 1.78 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)
# Audio Technica ATH-IM02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.8; 28 1.7; 31 1.5; 34 1.4; 37 1.2; 41 1.0; 45 0.9; 49 0.7; 54 0.4; 60 0.1; 66 -0.3; 72 -0.6; 79 -1.0; 87 -1.4; 96 -1.9; 106 -2.2; 116 -2.4; 128 -2.7; 141 -3.0; 155 -3.2; 170 -3.3; 187 -3.4; 206 -3.4; 227 -3.3; 249 -3.3; 274 -3.1; 302 -3.0; 332 -2.8; 365 -2.5; 402 -2.2; 442 -1.8; 486 -1.6; 535 -1.2; 588 -0.5; 647 -0.2; 712 0.0; 783 0.4; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.0; 1526 -1.6; 1678 -2.1; 1846 -2.4; 2031 -2.6; 2234 -2.2; 2457 -0.6; 2703 2.7; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.0; 4788 2.3; 5267 0.2; 5793 0.7; 6373 2.8; 7010 1.8; 7711 -0.8; 8482 -0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.6; 15026 -0.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.56 | 2.1 dB  |
| Peaking | 192 Hz  | 0.63 | -3.7 dB |
| Peaking | 2218 Hz | 1.81 | -5.8 dB |
| Peaking | 3067 Hz | 1.8  | 7.9 dB  |
| Peaking | 3985 Hz | 4.52 | 2.9 dB  |
| Peaking | 828 Hz  | 2.45 | 1.0 dB  |
| Peaking | 1585 Hz | 5.6  | -0.8 dB |
| Peaking | 5412 Hz | 6.54 | -2.3 dB |
| Peaking | 6537 Hz | 3.66 | 3.4 dB  |
| Peaking | 7627 Hz | 4.29 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)
# Audio-Technica ATH-M30x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.7; 28 -0.2; 31 -0.9; 34 -1.5; 37 -1.9; 41 -2.3; 45 -2.6; 49 -2.8; 54 -2.8; 60 -2.6; 66 -2.4; 72 -2.0; 79 -1.6; 87 -1.5; 96 -1.8; 106 -2.0; 116 -2.2; 128 -2.2; 141 -1.7; 155 -1.1; 170 -0.3; 187 0.8; 206 2.2; 227 3.6; 249 4.6; 274 4.7; 302 3.4; 332 2.4; 365 1.6; 402 1.0; 442 0.6; 486 0.5; 535 0.4; 588 0.3; 647 0.2; 712 0.2; 783 0.1; 861 -0.1; 947 -0.1; 1042 0.1; 1146 -0.0; 1261 -0.6; 1387 -1.5; 1526 -2.7; 1678 -3.8; 1846 -4.2; 2031 -4.4; 2234 -3.2; 2457 -1.8; 2703 -0.3; 2973 0.8; 3270 3.3; 3597 5.0; 3957 3.1; 4353 4.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -1.6; 9330 -2.4; 10263 -2.4; 11289 -1.3; 12418 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 94 Hz   |  0.43 | -2.6 dB |
| Peaking | 258 Hz  |  1.8  | 6.1 dB  |
| Peaking | 1990 Hz |  1.78 | -6.4 dB |
| Peaking | 6046 Hz |  0.73 | 9.9 dB  |
| Peaking | 8720 Hz |  1.22 | -9.0 dB |
| Peaking | 19 Hz   |  1.16 | 3.6 dB  |
| Peaking | 43 Hz   |  0.59 | -1.6 dB |
| Peaking | 82 Hz   |  2.51 | 1.7 dB  |
| Peaking | 3464 Hz | 11.58 | 2.6 dB  |
| Peaking | 3990 Hz |  7.89 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)
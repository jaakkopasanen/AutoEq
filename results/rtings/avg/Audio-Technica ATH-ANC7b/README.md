# Audio-Technica ATH-ANC7b

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.1; 25 4.6; 28 4.0; 31 3.4; 34 3.0; 37 2.6; 41 2.1; 45 1.8; 49 1.5; 54 1.2; 60 0.8; 66 0.4; 72 0.0; 79 -0.3; 87 -0.7; 96 -1.1; 106 -1.5; 116 -1.8; 128 -2.0; 141 -2.2; 155 -2.3; 170 -2.2; 187 -2.0; 206 -1.7; 227 -1.5; 249 -1.3; 274 -1.2; 302 -1.1; 332 -1.0; 365 -1.0; 402 -1.1; 442 -1.1; 486 -1.0; 535 -0.5; 588 0.1; 647 0.8; 712 1.1; 783 0.1; 861 -1.2; 947 -0.9; 1042 2.0; 1146 5.2; 1261 4.8; 1387 5.0; 1526 5.9; 1678 5.8; 1846 6.0; 2031 6.0; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.4; 5793 4.1; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.5  | 6.6 dB  |
| Peaking | 152 Hz  |  0.8  | -2.6 dB |
| Peaking | 465 Hz  |  1.54 | -2.0 dB |
| Peaking | 901 Hz  |  4.51 | -5.0 dB |
| Peaking | 2297 Hz |  0.41 | 6.7 dB  |
| Peaking | 1126 Hz | 15.86 | 2.0 dB  |
| Peaking | 2371 Hz |  2.63 | -1.0 dB |
| Peaking | 6574 Hz |  1.33 | 6.1 dB  |
| Peaking | 7698 Hz |  1.33 | -6.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7b/Audio-Technica%20ATH-ANC7b.png)
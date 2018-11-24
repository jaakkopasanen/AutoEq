# Audio-Technica ATH-ANC23

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.3; 49 4.9; 54 4.3; 60 3.6; 66 3.0; 72 2.5; 79 2.0; 87 1.3; 96 0.5; 106 -0.4; 116 -1.4; 128 -2.3; 141 -3.1; 155 -3.7; 170 -4.2; 187 -4.7; 206 -5.2; 227 -5.5; 249 -5.6; 274 -5.5; 302 -5.5; 332 -5.4; 365 -5.3; 402 -5.1; 442 -4.7; 486 -4.1; 535 -3.3; 588 -2.3; 647 -1.0; 712 -0.9; 783 -0.6; 861 -0.4; 947 -0.1; 1042 0.1; 1146 0.3; 1261 -0.0; 1387 -1.3; 1526 -2.8; 1678 -3.4; 1846 -2.8; 2031 -1.6; 2234 -0.1; 2457 1.2; 2703 1.7; 2973 1.3; 3270 0.9; 3597 0.4; 3957 -1.1; 4353 -3.1; 4788 -3.8; 5267 -4.2; 5793 -4.0; 6373 -2.2; 7010 -0.0; 7711 -0.6; 8482 -3.9; 9330 -3.8; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC23 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC23 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 31 Hz   |  0.48 | 6.6 dB  |
| Peaking | 246 Hz  |  0.67 | -6.5 dB |
| Peaking | 1684 Hz |  5.58 | -3.5 dB |
| Peaking | 5256 Hz |  3.41 | -4.8 dB |
| Peaking | 8890 Hz |  6.78 | -4.9 dB |
| Peaking | 461 Hz  |  2.98 | -1.4 dB |
| Peaking | 820 Hz  |  1.53 | 1.1 dB  |
| Peaking | 2860 Hz |  3.35 | 2.2 dB  |
| Peaking | 4381 Hz |  8.15 | -1.8 dB |
| Peaking | 7268 Hz | 11.4  | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC23/Audio-Technica%20ATH-ANC23.png)
# Audio-Technica ATH-M60x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.7; 28 1.4; 31 1.1; 34 0.9; 37 0.7; 41 0.5; 45 0.3; 49 0.0; 54 -0.1; 60 -0.2; 66 -0.3; 72 -0.2; 79 -0.3; 87 -0.3; 96 -0.4; 106 -0.7; 116 -0.8; 128 -0.9; 141 -1.0; 155 -1.1; 170 -1.1; 187 -1.0; 206 -0.8; 227 -0.5; 249 0.0; 274 0.7; 302 1.7; 332 3.2; 365 5.4; 402 6.0; 442 6.0; 486 5.9; 535 3.9; 588 2.2; 647 1.3; 712 0.8; 783 0.4; 861 0.2; 947 0.1; 1042 0.0; 1146 0.1; 1261 0.1; 1387 -0.1; 1526 -0.3; 1678 -0.7; 1846 -0.4; 2031 0.4; 2234 1.7; 2457 3.3; 2703 3.9; 2973 4.9; 3270 5.8; 3597 5.8; 3957 1.6; 4353 -1.4; 4788 1.7; 5267 5.3; 5793 6.0; 6373 4.4; 7010 1.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.6; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.88 | 2.3 dB  |
| Peaking | 354 Hz  |  0.4  | -3.1 dB |
| Peaking | 425 Hz  |  1.41 | 9.6 dB  |
| Peaking | 3121 Hz |  2.77 | 6.2 dB  |
| Peaking | 5782 Hz |  4.84 | 6.5 dB  |
| Peaking | 1804 Hz |  2.73 | -1.5 dB |
| Peaking | 2041 Hz |  0.71 | 0.6 dB  |
| Peaking | 2384 Hz |  8    | 1.2 dB  |
| Peaking | 4340 Hz |  8.73 | -4.1 dB |
| Peaking | 5160 Hz | 11.61 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)
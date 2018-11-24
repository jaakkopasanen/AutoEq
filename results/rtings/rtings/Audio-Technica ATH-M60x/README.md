# Audio-Technica ATH-M60x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.5; 28 1.3; 31 1.1; 34 0.9; 37 0.9; 41 0.7; 45 0.5; 49 0.4; 54 0.2; 60 0.1; 66 -0.1; 72 -0.2; 79 -0.5; 87 -0.7; 96 -0.9; 106 -1.1; 116 -1.3; 128 -1.5; 141 -1.6; 155 -1.7; 170 -1.7; 187 -1.6; 206 -1.3; 227 -1.0; 249 -0.5; 274 -0.0; 302 0.8; 332 2.3; 365 4.5; 402 6.0; 442 6.0; 486 5.2; 535 2.8; 588 1.1; 647 0.3; 712 -0.0; 783 -0.1; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 -0.3; 1846 -0.5; 2031 -0.1; 2234 1.3; 2457 2.9; 2703 3.3; 2973 3.9; 3270 4.0; 3597 3.8; 3957 0.4; 4353 -1.4; 4788 1.9; 5267 4.9; 5793 5.5; 6373 1.8; 7010 -1.5; 7711 0.0; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 -3.8; 16529 -3.0; 18182 -0.3; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 2.01 | 1.9 dB  |
| Peaking | 428 Hz   | 3.33 | 7.0 dB  |
| Peaking | 3106 Hz  | 2.13 | 4.2 dB  |
| Peaking | 14557 Hz | 1.11 | 2.2 dB  |
| Peaking | 15496 Hz | 2.2  | -6.5 dB |
| Peaking | 156 Hz   | 1.27 | -2.0 dB |
| Peaking | 1837 Hz  | 4.01 | -1.3 dB |
| Peaking | 4321 Hz  | 6.2  | -4.9 dB |
| Peaking | 5726 Hz  | 2.67 | 7.0 dB  |
| Peaking | 6839 Hz  | 3.5  | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)
# Audio Technica ATH-AD700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.2; 96 4.4; 106 4.1; 116 3.7; 128 3.3; 141 2.8; 155 2.4; 170 2.5; 187 2.0; 206 1.8; 227 1.7; 249 1.5; 274 1.5; 302 1.5; 332 1.5; 365 1.6; 402 1.7; 442 1.6; 486 1.7; 535 1.5; 588 1.6; 647 1.6; 712 1.5; 783 1.1; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.2; 1261 -0.1; 1387 -0.1; 1526 0.1; 1678 0.7; 1846 0.7; 2031 0.6; 2234 0.5; 2457 0.2; 2703 -0.4; 2973 -1.2; 3270 -0.9; 3597 2.7; 3957 5.2; 4353 -0.0; 4788 1.4; 5267 4.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.3; 8482 -4.0; 9330 -5.9; 10263 -2.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.33 | 6.4 dB  |
| Peaking | 532 Hz   | 1.33 | 1.4 dB  |
| Peaking | 5975 Hz  | 2.25 | 4.9 dB  |
| Peaking | 6081 Hz  | 2.71 | 1.9 dB  |
| Peaking | 9008 Hz  | 3.26 | -7.1 dB |
| Peaking | 3149 Hz  | 4.92 | -2.8 dB |
| Peaking | 3865 Hz  | 5.71 | 6.5 dB  |
| Peaking | 4379 Hz  | 6.05 | -3.8 dB |
| Peaking | 11156 Hz | 7.73 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD700/Audio%20Technica%20ATH-AD700.png)
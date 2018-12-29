# Audio Technica ATH-A900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.1; 49 4.4; 54 3.6; 60 3.3; 66 4.0; 72 4.6; 79 3.4; 87 2.5; 96 2.6; 106 3.2; 116 3.0; 128 3.0; 141 3.1; 155 3.4; 170 4.2; 187 4.3; 206 4.7; 227 4.9; 249 4.6; 274 3.3; 302 1.4; 332 -0.4; 365 -1.9; 402 -2.4; 442 -2.1; 486 -1.7; 535 -1.2; 588 -0.8; 647 -0.4; 712 -0.5; 783 0.2; 861 0.8; 947 -0.0; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -1.0; 1678 -0.8; 1846 -0.8; 2031 -0.6; 2234 0.4; 2457 1.8; 2703 2.5; 2973 2.6; 3270 3.5; 3597 4.5; 3957 4.2; 4353 3.3; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.6; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.38 | 6.1 dB  |
| Peaking | 173 Hz   | 2.45 | 3.1 dB  |
| Peaking | 237 Hz   | 4.55 | 4.0 dB  |
| Peaking | 3573 Hz  | 2.52 | 3.8 dB  |
| Peaking | 5632 Hz  | 2.77 | 6.3 dB  |
| Peaking | 419 Hz   | 2.96 | -3.1 dB |
| Peaking | 1373 Hz  | 4.86 | -1.8 dB |
| Peaking | 1959 Hz  | 2.89 | -1.3 dB |
| Peaking | 2565 Hz  | 4.58 | 1.5 dB  |
| Peaking | 16777 Hz | 4.35 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A900/Audio%20Technica%20ATH-A900.png)
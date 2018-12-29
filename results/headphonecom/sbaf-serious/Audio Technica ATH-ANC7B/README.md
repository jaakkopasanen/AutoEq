# Audio Technica ATH-ANC7B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 4.4; 31 1.9; 34 -0.4; 37 -2.3; 41 -4.2; 45 -5.3; 49 -5.5; 54 -4.9; 60 -4.0; 66 -3.5; 72 -3.2; 79 -3.1; 87 -3.0; 96 -2.9; 106 -2.7; 116 -2.6; 128 -2.5; 141 -2.5; 155 -2.6; 170 -2.3; 187 -2.2; 206 -1.9; 227 -1.7; 249 -1.4; 274 -1.2; 302 -1.0; 332 -0.6; 365 -0.7; 402 -0.6; 442 -1.0; 486 -1.5; 535 -2.2; 588 -3.1; 647 -4.0; 712 -4.2; 783 -3.3; 861 -1.5; 947 -0.1; 1042 -0.6; 1146 -2.2; 1261 -1.3; 1387 -0.5; 1526 1.0; 1678 2.0; 1846 -0.5; 2031 0.6; 2234 1.6; 2457 3.1; 2703 5.0; 2973 4.9; 3270 4.7; 3597 3.4; 3957 4.0; 4353 4.8; 4788 4.4; 5267 -0.7; 5793 1.4; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.5; 10263 -3.2; 11289 -2.0; 12418 -0.2; 13660 -1.5; 15026 -4.4; 16529 -4.0; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.69 | 16.4 dB  |
| Peaking | 39 Hz    | 0.63 | -15.1 dB |
| Peaking | 3338 Hz  | 0.72 | 8.4 dB   |
| Peaking | 4003 Hz  | 0.1  | -3.7 dB  |
| Peaking | 6617 Hz  | 6.36 | 5.0 dB   |
| Peaking | 675 Hz   | 0.97 | 3.1 dB   |
| Peaking | 679 Hz   | 2.42 | -5.6 dB  |
| Peaking | 2020 Hz  | 6.26 | -1.7 dB  |
| Peaking | 12774 Hz | 5.15 | 2.9 dB   |
| Peaking | 15615 Hz | 3.72 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ANC7B/Audio%20Technica%20ATH-ANC7B.png)
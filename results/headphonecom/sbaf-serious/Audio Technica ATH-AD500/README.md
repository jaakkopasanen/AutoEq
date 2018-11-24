# Audio Technica ATH-AD500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.1; 87 4.1; 96 3.5; 106 2.7; 116 2.3; 128 1.9; 141 1.7; 155 1.5; 170 1.4; 187 1.3; 206 1.3; 227 1.4; 249 1.1; 274 1.1; 302 1.3; 332 1.2; 365 1.6; 402 1.8; 442 1.6; 486 1.5; 535 1.5; 588 1.6; 647 1.5; 712 1.6; 783 1.2; 861 0.8; 947 0.3; 1042 -0.3; 1146 -0.5; 1261 -0.8; 1387 -1.0; 1526 -0.7; 1678 0.9; 1846 2.0; 2031 2.2; 2234 1.9; 2457 1.4; 2703 1.4; 2973 2.5; 3270 2.8; 3597 2.7; 3957 -3.5; 4353 -4.2; 4788 -3.0; 5267 -2.0; 5793 5.7; 6373 4.3; 7010 -1.1; 7711 -4.4; 8482 -7.2; 9330 -8.0; 10263 -5.7; 11289 -2.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.36 | 6.4 dB   |
| Peaking | 3614 Hz  | 1.57 | 11.8 dB  |
| Peaking | 4164 Hz  | 1.94 | -14.1 dB |
| Peaking | 6063 Hz  | 5.28 | 9.3 dB   |
| Peaking | 8999 Hz  | 2.62 | -8.9 dB  |
| Peaking | 34 Hz    | 2.68 | -0.3 dB  |
| Peaking | 620 Hz   | 0.98 | 1.8 dB   |
| Peaking | 1540 Hz  | 1.17 | -2.9 dB  |
| Peaking | 1881 Hz  | 2.95 | 3.7 dB   |
| Peaking | 12517 Hz | 4.85 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)
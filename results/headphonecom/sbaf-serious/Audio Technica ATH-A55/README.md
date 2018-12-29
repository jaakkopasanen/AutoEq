# Audio Technica ATH-A55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 5.2; 274 2.2; 302 0.3; 332 -1.0; 365 -1.2; 402 -0.8; 442 -0.3; 486 0.1; 535 0.3; 588 0.3; 647 0.5; 712 0.5; 783 0.4; 861 0.8; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.5; 1387 -0.6; 1526 -0.3; 1678 1.1; 1846 1.6; 2031 1.5; 2234 0.5; 2457 0.4; 2703 2.2; 2973 3.0; 3270 4.4; 3597 6.0; 3957 1.2; 4353 -3.7; 4788 0.5; 5267 5.2; 5793 6.0; 6373 3.1; 7010 0.7; 7711 -2.3; 8482 -2.7; 9330 -1.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 60 Hz   | 0.27 | 6.8 dB   |
| Peaking | 1222 Hz | 3.95 | -0.8 dB  |
| Peaking | 3683 Hz | 1.62 | 21.2 dB  |
| Peaking | 4234 Hz | 1.39 | -22.1 dB |
| Peaking | 5504 Hz | 2.92 | 11.5 dB  |
| Peaking | 19 Hz   | 2.28 | 1.3 dB   |
| Peaking | 232 Hz  | 1.89 | 4.3 dB   |
| Peaking | 328 Hz  | 1.86 | -4.8 dB  |
| Peaking | 1860 Hz | 6.86 | 1.5 dB   |
| Peaking | 8157 Hz | 7.01 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A55/Audio%20Technica%20ATH-A55.png)
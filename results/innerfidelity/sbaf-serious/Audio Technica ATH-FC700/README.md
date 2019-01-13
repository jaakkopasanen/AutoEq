# Audio Technica ATH-FC700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 5.1; 72 4.3; 79 3.9; 87 3.0; 96 2.0; 106 1.4; 116 1.0; 128 0.5; 141 0.1; 155 -0.1; 170 -0.0; 187 0.1; 206 0.1; 227 0.3; 249 -0.2; 274 -0.4; 302 -0.2; 332 -0.5; 365 -0.7; 402 -0.4; 442 -0.2; 486 -0.2; 535 -0.2; 588 0.2; 647 0.4; 712 0.5; 783 0.6; 861 0.3; 947 0.1; 1042 0.1; 1146 -0.1; 1261 -0.0; 1387 -0.4; 1526 -1.7; 1678 -2.6; 1846 -3.3; 2031 -3.4; 2234 -3.0; 2457 -1.6; 2703 -0.4; 2973 0.8; 3270 1.8; 3597 3.2; 3957 4.6; 4353 4.0; 4788 4.9; 5267 5.3; 5793 -1.8; 6373 -2.5; 7010 -8.0; 7711 -6.9; 8482 -3.8; 9330 -1.4; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.9; 16529 -4.8; 18182 -3.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-FC700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.65 | 6.9 dB   |
| Peaking | 2052 Hz  | 2.05 | -4.6 dB  |
| Peaking | 4707 Hz  | 1.3  | 6.8 dB   |
| Peaking | 7159 Hz  | 2.74 | -10.9 dB |
| Peaking | 17072 Hz | 2.5  | -5.6 dB  |
| Peaking | 35 Hz    | 1.29 | -3.9 dB  |
| Peaking | 72 Hz    | 0.14 | 3.3 dB   |
| Peaking | 134 Hz   | 0.87 | -3.6 dB  |
| Peaking | 346 Hz   | 1.03 | -2.3 dB  |
| Peaking | 12475 Hz | 2.51 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-FC700/Audio%20Technica%20ATH-FC700.png)
# Audio Technica ATH-Pro700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 5.7; 402 3.3; 442 1.4; 486 0.5; 535 0.3; 588 0.3; 647 0.3; 712 0.5; 783 0.2; 861 -0.0; 947 -0.1; 1042 0.1; 1146 0.8; 1261 1.0; 1387 2.0; 1526 2.8; 1678 4.0; 1846 5.5; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-Pro700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-Pro700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.24 | 6.4 dB  |
| Peaking | 269 Hz  | 1.47 | 4.1 dB  |
| Peaking | 2073 Hz | 2.22 | 4.9 dB  |
| Peaking | 3525 Hz | 1.47 | 5.2 dB  |
| Peaking | 5639 Hz | 2.76 | 4.8 dB  |
| Peaking | 21 Hz   | 2.1  | 0.9 dB  |
| Peaking | 362 Hz  | 5.43 | 2.6 dB  |
| Peaking | 492 Hz  | 2    | -1.8 dB |
| Peaking | 940 Hz  | 3.68 | -1.0 dB |
| Peaking | 8339 Hz | 4.09 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-Pro700/Audio%20Technica%20ATH-Pro700.png)
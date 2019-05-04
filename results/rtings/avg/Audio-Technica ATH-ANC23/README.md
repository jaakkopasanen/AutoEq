# Audio-Technica ATH-ANC23
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.3; 41 -1.8; 45 -2.2; 49 -2.6; 54 -3.0; 60 -3.5; 66 -4.0; 72 -4.4; 79 -4.9; 87 -5.5; 96 -6.0; 106 -6.5; 116 -7.0; 128 -7.5; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.6; 206 -8.7; 227 -8.8; 249 -8.9; 274 -9.1; 302 -9.2; 332 -9.2; 365 -9.2; 402 -9.0; 442 -8.7; 486 -8.3; 535 -7.5; 588 -6.4; 647 -5.1; 712 -4.7; 783 -4.1; 861 -3.5; 947 -3.2; 1042 -2.9; 1146 -3.0; 1261 -3.4; 1387 -4.4; 1526 -5.5; 1678 -6.2; 1846 -6.0; 2031 -5.3; 2234 -4.2; 2457 -3.0; 2703 -2.6; 2973 -3.2; 3270 -4.4; 3597 -5.4; 3957 -6.1; 4353 -7.0; 4788 -8.6; 5267 -10.5; 5793 -10.7; 6373 -7.9; 7010 -6.3; 7711 -6.6; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC23 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC23 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.42 | 6.2 dB  |
| Peaking | 590 Hz  | 0.23 | -4.6 dB |
| Peaking | 950 Hz  | 0.91 | 7.9 dB  |
| Peaking | 2740 Hz | 2.14 | 5.0 dB  |
| Peaking | 5463 Hz | 4.51 | -4.8 dB |
| Peaking | 656 Hz  | 4.4  | 1.2 dB  |
| Peaking | 934 Hz  | 1.07 | -1.3 dB |
| Peaking | 1328 Hz | 1.35 | 2.1 dB  |
| Peaking | 1630 Hz | 2.99 | -1.8 dB |
| Peaking | 7082 Hz | 9.35 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC23/Audio-Technica%20ATH-ANC23.png)
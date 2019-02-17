# Audio-Technica ATH-ANC70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.2; 96 -1.7; 106 -2.3; 116 -2.8; 128 -3.3; 141 -3.6; 155 -3.8; 170 -4.0; 187 -4.1; 206 -4.0; 227 -4.0; 249 -3.9; 274 -3.7; 302 -3.6; 332 -3.5; 365 -3.2; 402 -2.9; 442 -2.5; 486 -2.1; 535 -1.6; 588 -1.2; 647 -1.1; 712 -1.5; 783 -2.6; 861 -4.1; 947 -5.6; 1042 -7.5; 1146 -9.2; 1261 -10.1; 1387 -9.7; 1526 -8.7; 1678 -7.5; 1846 -7.5; 2031 -7.5; 2234 -6.3; 2457 -6.5; 2703 -6.8; 2973 -7.9; 3270 -8.4; 3597 -6.4; 3957 -3.9; 4353 -2.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -9.0; 13660 -10.2; 15026 -9.3; 16529 -6.6; 18182 -7.1; 20000 -18.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.34 | 6.4 dB   |
| Peaking | 735 Hz   | 0.83 | 8.6 dB   |
| Peaking | 1154 Hz  | 1.07 | -8.0 dB  |
| Peaking | 5243 Hz  | 2.47 | 7.1 dB   |
| Peaking | 20233 Hz | 1.32 | -12.2 dB |
| Peaking | 3229 Hz  | 3.73 | -5.1 dB  |
| Peaking | 3358 Hz  | 1.41 | 2.3 dB   |
| Peaking | 13965 Hz | 2.09 | -4.1 dB  |
| Peaking | 17539 Hz | 1.89 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)
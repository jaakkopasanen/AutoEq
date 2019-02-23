# Audio-Technica ATH-M50xBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.5; 25 -8.8; 28 -9.2; 31 -9.6; 34 -9.7; 37 -9.8; 41 -9.9; 45 -9.7; 49 -9.3; 54 -8.7; 60 -8.3; 66 -8.5; 72 -9.1; 79 -9.7; 87 -10.4; 96 -10.9; 106 -11.2; 116 -11.3; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.7; 187 -10.0; 206 -9.2; 227 -8.2; 249 -7.1; 274 -5.9; 302 -3.3; 332 -2.2; 365 -1.3; 402 -1.1; 442 -1.0; 486 -1.3; 535 -1.9; 588 -2.6; 647 -3.1; 712 -3.7; 783 -3.7; 861 -3.7; 947 -4.8; 1042 -5.5; 1146 -6.1; 1261 -6.7; 1387 -7.3; 1526 -8.0; 1678 -8.5; 1846 -8.2; 2031 -8.2; 2234 -8.1; 2457 -7.6; 2703 -8.2; 2973 -8.5; 3270 -7.7; 3597 -6.1; 3957 -7.0; 4353 -10.1; 4788 -7.2; 5267 -3.5; 5793 -0.5; 6373 -1.5; 7010 -3.9; 7711 -6.4; 8482 -8.2; 9330 -9.0; 10263 -10.0; 11289 -11.4; 12418 -10.8; 13660 -8.7; 15026 -8.6; 16529 -8.5; 18182 -6.9; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50xBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50xBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.39 | -2.9 dB |
| Peaking | 167 Hz   | 0.58 | -7.1 dB |
| Peaking | 392 Hz   | 0.82 | 8.6 dB  |
| Peaking | 6106 Hz  | 2.13 | 11.1 dB |
| Peaking | 7469 Hz  | 0.3  | -5.2 dB |
| Peaking | 852 Hz   | 6.31 | 1.2 dB  |
| Peaking | 1610 Hz  | 2.99 | -1.3 dB |
| Peaking | 3881 Hz  | 2.94 | 3.5 dB  |
| Peaking | 4364 Hz  | 6.16 | -5.3 dB |
| Peaking | 11474 Hz | 6.81 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50xBT/Audio-Technica%20ATH-M50xBT.png)
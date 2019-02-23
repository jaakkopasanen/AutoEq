# Superlux HD 681 EVO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.6; 25 -9.1; 28 -9.8; 31 -10.3; 34 -10.7; 37 -10.9; 41 -11.2; 45 -11.3; 49 -11.3; 54 -11.2; 60 -11.1; 66 -10.9; 72 -10.7; 79 -10.4; 87 -10.3; 96 -10.2; 106 -10.2; 116 -10.1; 128 -9.7; 141 -9.0; 155 -8.1; 170 -7.5; 187 -7.2; 206 -6.8; 227 -6.5; 249 -6.2; 274 -5.9; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.8; 442 -4.8; 486 -4.8; 535 -4.3; 588 -4.4; 647 -4.1; 712 -4.6; 783 -5.0; 861 -5.3; 947 -5.2; 1042 -4.7; 1146 -4.2; 1261 -4.1; 1387 -4.3; 1526 -5.3; 1678 -7.1; 1846 -8.9; 2031 -10.0; 2234 -9.5; 2457 -8.6; 2703 -7.9; 2973 -7.7; 3270 -6.7; 3597 -3.5; 3957 -0.5; 4353 -2.3; 4788 -5.4; 5267 -6.3; 5793 -7.0; 6373 -6.6; 7010 -6.8; 7711 -9.6; 8482 -11.7; 9330 -12.0; 10263 -11.2; 11289 -10.3; 12418 -11.1; 13660 -11.7; 15026 -7.9; 16529 -6.5; 18182 -6.9; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.64 | -5.2 dB |
| Peaking | 2170 Hz  | 4.02 | -3.9 dB |
| Peaking | 4047 Hz  | 5.23 | 7.1 dB  |
| Peaking | 9166 Hz  | 2.48 | -5.5 dB |
| Peaking | 13184 Hz | 2.36 | -5.0 dB |
| Peaking | 122 Hz   | 2.88 | -1.6 dB |
| Peaking | 523 Hz   | 0.7  | 2.2 dB  |
| Peaking | 1352 Hz  | 2.25 | 3.9 dB  |
| Peaking | 1638 Hz  | 1.28 | -2.3 dB |
| Peaking | 10866 Hz | 5.19 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)
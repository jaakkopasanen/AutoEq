# Superlux HD 681 EVO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.6; 25 -10.1; 28 -10.8; 31 -11.3; 34 -11.7; 37 -12.0; 41 -12.2; 45 -12.3; 49 -12.3; 54 -12.2; 60 -12.1; 66 -11.9; 72 -11.7; 79 -11.4; 87 -11.3; 96 -11.2; 106 -11.2; 116 -11.1; 128 -10.7; 141 -10.1; 155 -9.1; 170 -8.6; 187 -8.2; 206 -7.8; 227 -7.5; 249 -7.2; 274 -6.9; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.8; 442 -5.8; 486 -5.8; 535 -5.3; 588 -5.4; 647 -5.1; 712 -5.6; 783 -6.0; 861 -6.4; 947 -6.2; 1042 -5.7; 1146 -5.2; 1261 -5.1; 1387 -5.3; 1526 -6.3; 1678 -8.1; 1846 -9.9; 2031 -11.0; 2234 -10.5; 2457 -9.6; 2703 -8.9; 2973 -8.8; 3270 -7.7; 3597 -4.5; 3957 -0.5; 4353 -3.1; 4788 -6.4; 5267 -7.3; 5793 -8.0; 6373 -7.6; 7010 -7.8; 7711 -10.6; 8482 -12.7; 9330 -13.0; 10263 -12.2; 11289 -11.4; 12418 -12.1; 13660 -12.7; 15026 -8.9; 16529 -6.0; 18182 -7.5; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.45 | -6.6 dB |
| Peaking | 2217 Hz  | 2.37 | -5.1 dB |
| Peaking | 4031 Hz  | 7.07 | 7.6 dB  |
| Peaking | 9176 Hz  | 1.75 | -6.6 dB |
| Peaking | 13334 Hz | 2.26 | -6.0 dB |
| Peaking | 123 Hz   | 4.02 | -1.2 dB |
| Peaking | 488 Hz   | 1.14 | 0.9 dB  |
| Peaking | 1327 Hz  | 3.28 | 1.8 dB  |
| Peaking | 1825 Hz  | 5.48 | -1.5 dB |
| Peaking | 19902 Hz | 2.08 | -7.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)
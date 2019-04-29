# Sony MH750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.6; 28 -9.7; 31 -9.8; 34 -9.8; 37 -9.8; 41 -9.7; 45 -9.6; 49 -9.5; 54 -9.4; 60 -9.3; 66 -9.2; 72 -9.2; 79 -9.1; 87 -9.0; 96 -8.9; 106 -8.9; 116 -8.7; 128 -8.5; 141 -8.3; 155 -8.1; 170 -7.7; 187 -7.3; 206 -6.9; 227 -6.5; 249 -6.1; 274 -5.6; 302 -5.1; 332 -4.7; 365 -4.2; 402 -3.8; 442 -3.4; 486 -3.0; 535 -2.6; 588 -2.2; 647 -1.8; 712 -1.3; 783 -0.9; 861 -0.6; 947 -0.5; 1042 -0.8; 1146 -1.5; 1261 -2.2; 1387 -2.5; 1526 -2.5; 1678 -1.8; 1846 -1.3; 2031 -1.1; 2234 -1.2; 2457 -1.8; 2703 -2.6; 2973 -3.2; 3270 -3.7; 3597 -3.5; 3957 -2.6; 4353 -1.6; 4788 -0.9; 5267 -0.6; 5793 -1.0; 6373 -2.8; 7010 -5.2; 7711 -3.2; 8482 -3.2; 9330 -3.2; 10263 -3.2; 11289 -3.2; 12418 -3.2; 13660 -3.2; 15026 -4.8; 16529 -7.0; 18182 -3.8; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.16 | -6.5 dB |
| Peaking | 796 Hz   | 0.98 | 2.9 dB  |
| Peaking | 2106 Hz  | 3.32 | 1.8 dB  |
| Peaking | 14985 Hz | 1    | 1.3 dB  |
| Peaking | 16163 Hz | 1.95 | -5.1 dB |
| Peaking | 1000 Hz  | 5.09 | 0.6 dB  |
| Peaking | 1346 Hz  | 4.27 | -0.7 dB |
| Peaking | 3397 Hz  | 3.53 | -1.5 dB |
| Peaking | 5286 Hz  | 1.96 | 3.0 dB  |
| Peaking | 6998 Hz  | 5.67 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MH750/Sony%20MH750.png)
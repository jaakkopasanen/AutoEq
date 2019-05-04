# Polk Audio UltraFocus 8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.2; 25 -10.6; 28 -9.9; 31 -9.3; 34 -8.9; 37 -8.5; 41 -8.1; 45 -7.8; 49 -7.6; 54 -7.4; 60 -7.2; 66 -7.0; 72 -6.9; 79 -6.8; 87 -6.7; 96 -6.6; 106 -6.6; 116 -6.6; 128 -6.7; 141 -6.5; 155 -6.5; 170 -6.6; 187 -6.6; 206 -6.6; 227 -6.6; 249 -6.5; 274 -6.5; 302 -6.2; 332 -5.9; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.5; 535 -5.4; 588 -5.4; 647 -5.2; 712 -5.3; 783 -5.3; 861 -5.2; 947 -4.9; 1042 -5.1; 1146 -5.0; 1261 -5.1; 1387 -5.3; 1526 -5.9; 1678 -6.4; 1846 -6.7; 2031 -6.7; 2234 -6.3; 2457 -5.2; 2703 -4.1; 2973 -3.5; 3270 -4.0; 3597 -5.4; 3957 -7.4; 4353 -7.9; 4788 -8.4; 5267 -6.7; 5793 -3.8; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -7.0; 12418 -7.7; 13660 -7.5; 15026 -7.2; 16529 -7.4; 18182 -7.6; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 3174 Hz  | 2.31 | 6.1 dB  |
| Peaking | 4084 Hz  | 0.98 | -5.4 dB |
| Peaking | 6415 Hz  | 3.43 | 7.4 dB  |
| Peaking | 16179 Hz | 0.67 | -2.2 dB |
| Peaking | 14 Hz    | 0.53 | -7.6 dB |
| Peaking | 124 Hz   | 1.01 | -0.8 dB |
| Peaking | 235 Hz   | 2.1  | -0.9 dB |
| Peaking | 1965 Hz  | 5.98 | -1.0 dB |
| Peaking | 9859 Hz  | 5.91 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)
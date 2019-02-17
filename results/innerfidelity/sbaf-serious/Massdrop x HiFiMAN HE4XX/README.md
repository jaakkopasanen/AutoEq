# Massdrop x HiFiMAN HE4XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.8; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.5; 45 -2.6; 49 -2.7; 54 -2.9; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.3; 87 -4.6; 96 -4.9; 106 -5.1; 116 -5.1; 128 -5.5; 141 -5.5; 155 -5.8; 170 -5.9; 187 -6.0; 206 -6.1; 227 -5.9; 249 -5.7; 274 -5.6; 302 -5.8; 332 -6.2; 365 -6.4; 402 -6.1; 442 -5.5; 486 -4.9; 535 -5.5; 588 -5.3; 647 -5.4; 712 -5.6; 783 -4.5; 861 -4.6; 947 -4.5; 1042 -4.0; 1146 -3.6; 1261 -3.1; 1387 -3.3; 1526 -3.1; 1678 -2.6; 1846 -2.3; 2031 -2.6; 2234 -3.2; 2457 -4.3; 2703 -5.1; 2973 -5.4; 3270 -4.9; 3597 -4.3; 3957 -4.4; 4353 -7.4; 4788 -6.5; 5267 -3.3; 5793 -3.2; 6373 -7.4; 7010 -10.2; 7711 -9.6; 8482 -10.4; 9330 -10.3; 10263 -4.5; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x HiFiMAN HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x HiFiMAN HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.24 | 3.7 dB  |
| Peaking | 240 Hz   | 0.34 | -1.9 dB |
| Peaking | 1985 Hz  | 1.09 | 3.1 dB  |
| Peaking | 2763 Hz  | 1.63 | -2.5 dB |
| Peaking | 8109 Hz  | 2.31 | -6.9 dB |
| Peaking | 3861 Hz  | 4.54 | 2.0 dB  |
| Peaking | 4473 Hz  | 4.11 | -4.3 dB |
| Peaking | 5531 Hz  | 3.9  | 3.9 dB  |
| Peaking | 6753 Hz  | 7.18 | -3.1 dB |
| Peaking | 10912 Hz | 5.82 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20HiFiMAN%20HE4XX/Massdrop%20x%20HiFiMAN%20HE4XX.png)
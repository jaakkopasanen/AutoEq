# Bose QuietComfort 35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -5.9; 25 -5.7; 28 -5.4; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.6; 45 -5.7; 49 -5.7; 54 -5.6; 60 -5.6; 66 -5.5; 72 -5.4; 79 -5.3; 87 -5.3; 96 -5.3; 106 -5.2; 116 -5.2; 128 -5.2; 141 -5.1; 155 -5.0; 170 -4.9; 187 -4.7; 206 -4.5; 227 -4.4; 249 -4.2; 274 -4.1; 302 -3.9; 332 -3.7; 365 -3.5; 402 -3.4; 442 -3.4; 486 -3.3; 535 -3.1; 588 -2.7; 647 -2.4; 712 -2.0; 783 -1.6; 861 -1.1; 947 -0.8; 1042 -0.6; 1146 -0.5; 1261 -1.1; 1387 -2.6; 1526 -4.3; 1678 -6.4; 1846 -8.6; 2031 -9.0; 2234 -7.4; 2457 -6.5; 2703 -7.0; 2973 -6.5; 3270 -4.7; 3597 -5.1; 3957 -5.9; 4353 -4.8; 4788 -3.3; 5267 -0.6; 5793 -4.9; 6373 -8.1; 7010 -4.1; 7711 -3.5; 8482 -3.8; 9330 -3.8; 10263 -3.8; 11289 -4.5; 12418 -8.3; 13660 -7.5; 15026 -6.7; 16529 -4.9; 18182 -3.8; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.11 | -1.9 dB |
| Peaking | 1269 Hz  |  0.94 | 6.8 dB  |
| Peaking | 1883 Hz  |  1.3  | -8.9 dB |
| Peaking | 13465 Hz |  2.09 | -4.5 dB |
| Peaking | 20889 Hz |  1.89 | -2.4 dB |
| Peaking | 2332 Hz  | 10.67 | 0.9 dB  |
| Peaking | 3998 Hz  |  5.82 | -1.4 dB |
| Peaking | 5313 Hz  |  5.78 | 5.0 dB  |
| Peaking | 6263 Hz  |  4.35 | -6.9 dB |
| Peaking | 7135 Hz  |  2.25 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035/Bose%20QuietComfort%2035.png)
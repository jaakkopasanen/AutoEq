# Monoprice Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.9; 25 -3.4; 28 -4.0; 31 -4.5; 34 -4.9; 37 -5.2; 41 -5.6; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.8; 87 -8.3; 96 -8.8; 106 -9.2; 116 -9.7; 128 -10.0; 141 -10.1; 155 -10.2; 170 -10.2; 187 -10.0; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.3; 365 -9.2; 402 -9.1; 442 -9.4; 486 -9.8; 535 -9.5; 588 -8.8; 647 -8.7; 712 -8.7; 783 -8.3; 861 -6.5; 947 -4.5; 1042 -3.3; 1146 -4.0; 1261 -4.8; 1387 -3.9; 1526 -3.8; 1678 -4.7; 1846 -4.8; 2031 -3.9; 2234 -3.8; 2457 -2.9; 2703 -1.7; 2973 -1.9; 3270 -2.7; 3597 -2.0; 3957 -0.5; 4353 -1.1; 4788 -1.0; 5267 -2.6; 5793 -4.5; 6373 -1.1; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -7.0; 16529 -8.1; 18182 -6.4; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.93 | 3.8 dB  |
| Peaking | 150 Hz   | 0.66 | -4.3 dB |
| Peaking | 620 Hz   | 0.79 | -3.8 dB |
| Peaking | 1055 Hz  | 2.03 | 3.9 dB  |
| Peaking | 3841 Hz  | 0.92 | 4.7 dB  |
| Peaking | 3445 Hz  | 4.94 | -2.4 dB |
| Peaking | 4699 Hz  | 1.19 | 3.2 dB  |
| Peaking | 6176 Hz  | 1.63 | -5.5 dB |
| Peaking | 6536 Hz  | 5.61 | 6.5 dB  |
| Peaking | 16384 Hz | 2.21 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Noise%20Cancelling/Monoprice%20Noise%20Cancelling.png)
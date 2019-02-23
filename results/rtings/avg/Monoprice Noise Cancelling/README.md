# Monoprice Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.1; 25 -3.5; 28 -4.1; 31 -4.6; 34 -5.0; 37 -5.3; 41 -5.6; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.4; 116 -9.8; 128 -10.1; 141 -10.2; 155 -10.3; 170 -10.3; 187 -10.1; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.3; 302 -9.2; 332 -9.2; 365 -9.2; 402 -9.1; 442 -9.3; 486 -9.7; 535 -9.4; 588 -8.6; 647 -8.5; 712 -8.5; 783 -8.1; 861 -6.3; 947 -4.4; 1042 -3.1; 1146 -3.8; 1261 -4.5; 1387 -3.6; 1526 -3.5; 1678 -4.5; 1846 -4.4; 2031 -3.4; 2234 -2.8; 2457 -1.9; 2703 -1.0; 2973 -1.7; 3270 -2.9; 3597 -2.1; 3957 -0.8; 4353 -1.3; 4788 -0.5; 5267 -2.1; 5793 -4.5; 6373 -2.0; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -7.3; 16529 -8.2; 18182 -6.7; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.03 | 3.4 dB  |
| Peaking | 148 Hz   | 0.67 | -4.5 dB |
| Peaking | 591 Hz   | 0.78 | -3.6 dB |
| Peaking | 1048 Hz  | 2.58 | 3.7 dB  |
| Peaking | 3528 Hz  | 0.76 | 4.5 dB  |
| Peaking | 2751 Hz  | 5    | 1.7 dB  |
| Peaking | 3314 Hz  | 3.3  | -2.8 dB |
| Peaking | 4193 Hz  | 1.74 | 1.4 dB  |
| Peaking | 8578 Hz  | 3.9  | -1.2 dB |
| Peaking | 16433 Hz | 1.82 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Noise%20Cancelling/Monoprice%20Noise%20Cancelling.png)
# Anker SoundBuds Curve
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.0; 25 -9.8; 28 -9.4; 31 -9.1; 34 -8.7; 37 -8.2; 41 -7.7; 45 -7.3; 49 -6.9; 54 -6.5; 60 -6.4; 66 -6.4; 72 -6.4; 79 -6.5; 87 -6.8; 96 -7.2; 106 -7.8; 116 -8.4; 128 -8.9; 141 -9.1; 155 -8.9; 170 -8.1; 187 -6.9; 206 -5.1; 227 -3.1; 249 -2.0; 274 -2.4; 302 -3.0; 332 -3.3; 365 -3.4; 402 -3.4; 442 -3.2; 486 -3.1; 535 -2.8; 588 -2.4; 647 -1.8; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.9; 1042 -1.3; 1146 -1.7; 1261 -1.9; 1387 -1.9; 1526 -2.0; 1678 -2.1; 1846 -2.4; 2031 -2.6; 2234 -2.5; 2457 -2.3; 2703 -3.0; 2973 -4.0; 3270 -4.4; 3597 -4.5; 3957 -4.7; 4353 -5.5; 4788 -6.3; 5267 -7.6; 5793 -7.8; 6373 -6.2; 7010 -3.2; 7711 -1.2; 8482 -2.8; 9330 -4.9; 10263 -1.9; 11289 -1.2; 12418 -1.2; 13660 -1.2; 15026 -2.1; 16529 -2.5; 18182 -1.2; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Curve GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Curve ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.37 | -7.3 dB |
| Peaking | 43 Hz    | 0.17 | -2.9 dB |
| Peaking | 140 Hz   | 1.68 | -5.6 dB |
| Peaking | 5104 Hz  | 1.21 | -6.0 dB |
| Peaking | 20881 Hz | 1.77 | -1.1 dB |
| Peaking | 252 Hz   | 3.69 | 2.9 dB  |
| Peaking | 588 Hz   | 0.48 | -1.7 dB |
| Peaking | 818 Hz   | 1.78 | 2.7 dB  |
| Peaking | 5910 Hz  | 7.19 | -1.6 dB |
| Peaking | 7533 Hz  | 7.69 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Curve/Anker%20SoundBuds%20Curve.png)
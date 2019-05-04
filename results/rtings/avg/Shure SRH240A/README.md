# Shure SRH240A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.4; 60 -2.4; 66 -3.2; 72 -3.9; 79 -4.5; 87 -5.1; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.3; 141 -6.2; 155 -6.0; 170 -5.6; 187 -5.0; 206 -4.4; 227 -4.0; 249 -3.8; 274 -4.0; 302 -4.8; 332 -6.0; 365 -6.6; 402 -7.3; 442 -8.5; 486 -9.7; 535 -10.3; 588 -10.3; 647 -10.0; 712 -9.5; 783 -9.0; 861 -8.5; 947 -8.2; 1042 -7.9; 1146 -7.8; 1261 -8.0; 1387 -8.4; 1526 -8.9; 1678 -9.2; 1846 -9.4; 2031 -9.0; 2234 -8.1; 2457 -7.0; 2703 -6.3; 2973 -6.4; 3270 -6.7; 3597 -6.3; 3957 -5.3; 4353 -4.4; 4788 -4.0; 5267 -2.1; 5793 -0.9; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -9.4; 11289 -12.3; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -7.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.59 | 6.6 dB  |
| Peaking | 599 Hz   | 2.22 | -4.2 dB |
| Peaking | 1725 Hz  | 1.8  | -2.9 dB |
| Peaking | 5836 Hz  | 2.48 | 6.2 dB  |
| Peaking | 11205 Hz | 4.06 | -6.6 dB |
| Peaking | 116 Hz   | 1.68 | -1.3 dB |
| Peaking | 249 Hz   | 1.94 | 2.9 dB  |
| Peaking | 471 Hz   | 4.6  | -1.3 dB |
| Peaking | 13455 Hz | 5.24 | 0.9 dB  |
| Peaking | 17868 Hz | 3.28 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH240A/Shure%20SRH240A.png)
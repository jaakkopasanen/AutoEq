# Shure SRH240A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.1; 66 -2.0; 72 -2.7; 79 -3.3; 87 -4.0; 96 -4.4; 106 -4.7; 116 -5.0; 128 -5.1; 141 -5.0; 155 -4.8; 170 -4.4; 187 -3.7; 206 -3.2; 227 -2.7; 249 -2.5; 274 -2.7; 302 -3.4; 332 -4.7; 365 -5.2; 402 -5.9; 442 -7.1; 486 -8.3; 535 -8.8; 588 -8.9; 647 -8.5; 712 -7.9; 783 -7.4; 861 -7.0; 947 -6.7; 1042 -6.4; 1146 -6.3; 1261 -6.4; 1387 -6.9; 1526 -7.3; 1678 -7.6; 1846 -7.7; 2031 -7.1; 2234 -5.8; 2457 -4.7; 2703 -4.4; 2973 -4.9; 3270 -5.5; 3597 -5.1; 3957 -4.3; 4353 -3.4; 4788 -2.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.5; 11289 -9.9; 12418 -7.2; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.58 | 6.7 dB  |
| Peaking | 256 Hz   | 1.69 | 4.1 dB  |
| Peaking | 563 Hz   | 1.96 | -3.1 dB |
| Peaking | 5534 Hz  | 1.95 | 6.5 dB  |
| Peaking | 11006 Hz | 3.17 | -3.8 dB |
| Peaking | 57 Hz    | 1.94 | 2.7 dB  |
| Peaking | 58 Hz    | 0.95 | -1.7 dB |
| Peaking | 1836 Hz  | 3.27 | -1.9 dB |
| Peaking | 2684 Hz  | 2.62 | 2.3 dB  |
| Peaking | 3195 Hz  | 3.44 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH240A/Shure%20SRH240A.png)
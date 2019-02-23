# Shure SRH240
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -1.2; 106 -1.4; 116 -1.4; 128 -1.6; 141 -1.6; 155 -1.2; 170 -0.9; 187 -0.9; 206 -1.2; 227 -1.7; 249 -2.3; 274 -3.5; 302 -5.7; 332 -7.1; 365 -8.2; 402 -9.0; 442 -9.9; 486 -10.6; 535 -10.9; 588 -10.7; 647 -10.3; 712 -9.9; 783 -9.4; 861 -9.1; 947 -8.8; 1042 -8.5; 1146 -8.5; 1261 -9.0; 1387 -9.7; 1526 -10.1; 1678 -10.2; 1846 -9.9; 2031 -9.6; 2234 -9.6; 2457 -9.8; 2703 -9.9; 2973 -9.3; 3270 -8.9; 3597 -8.8; 3957 -8.8; 4353 -8.5; 4788 -8.1; 5267 -6.7; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.0; 9330 -11.2; 10263 -9.8; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.3  | 6.7 dB  |
| Peaking | 204 Hz  | 1.48 | 5.9 dB  |
| Peaking | 833 Hz  | 0.17 | -3.9 dB |
| Peaking | 6279 Hz | 4.04 | 8.0 dB  |
| Peaking | 9225 Hz | 3.93 | -5.1 dB |
| Peaking | 16 Hz   | 2.19 | 1.3 dB  |
| Peaking | 268 Hz  | 7.04 | 1.6 dB  |
| Peaking | 504 Hz  | 2.11 | -2.0 dB |
| Peaking | 1036 Hz | 2.43 | 1.9 dB  |
| Peaking | 4724 Hz | 5.29 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -5.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH240/Shure%20SRH240.png)
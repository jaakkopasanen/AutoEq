# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -10.1; 25 -10.5; 28 -11.0; 31 -11.5; 34 -11.8; 37 -12.1; 41 -12.4; 45 -12.6; 49 -12.7; 54 -12.6; 60 -12.7; 66 -13.0; 72 -13.4; 79 -13.4; 87 -12.8; 96 -11.3; 106 -10.3; 116 -10.6; 128 -12.2; 141 -13.0; 155 -13.0; 170 -11.6; 187 -12.3; 206 -11.5; 227 -10.7; 249 -10.9; 274 -9.6; 302 -8.3; 332 -7.2; 365 -6.6; 402 -6.3; 442 -6.4; 486 -6.5; 535 -6.7; 588 -6.6; 647 -6.6; 712 -6.4; 783 -6.1; 861 -5.4; 947 -5.4; 1042 -6.4; 1146 -6.4; 1261 -6.3; 1387 -7.2; 1526 -8.6; 1678 -10.3; 1846 -12.2; 2031 -13.7; 2234 -14.0; 2457 -12.0; 2703 -9.1; 2973 -6.9; 3270 -5.2; 3597 -5.0; 3957 -6.3; 4353 -10.0; 4788 -7.0; 5267 -5.1; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -6.6; 8482 -11.5; 9330 -12.9; 10263 -10.0; 11289 -6.1; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.51 | -6.9 dB |
| Peaking | 180 Hz  | 1.36 | -4.7 dB |
| Peaking | 2105 Hz | 2.72 | -8.8 dB |
| Peaking | 6338 Hz | 4.53 | 7.2 dB  |
| Peaking | 9120 Hz | 3.56 | -8.1 dB |
| Peaking | 15 Hz   | 1.46 | -0.6 dB |
| Peaking | 388 Hz  | 5.12 | 1.1 dB  |
| Peaking | 915 Hz  | 5.19 | 1.3 dB  |
| Peaking | 3473 Hz | 4.56 | 2.5 dB  |
| Peaking | 4388 Hz | 8.21 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)
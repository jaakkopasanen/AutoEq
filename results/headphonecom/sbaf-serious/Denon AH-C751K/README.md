# Denon AH-C751K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.7; 31 -9.8; 34 -9.7; 37 -9.7; 41 -9.6; 45 -9.7; 49 -10.0; 54 -10.1; 60 -10.1; 66 -10.0; 72 -10.0; 79 -9.9; 87 -9.9; 96 -9.8; 106 -9.5; 116 -9.1; 128 -8.7; 141 -8.1; 155 -9.1; 170 -9.1; 187 -8.5; 206 -7.9; 227 -7.3; 249 -6.6; 274 -6.1; 302 -5.3; 332 -4.6; 365 -3.9; 402 -3.3; 442 -2.8; 486 -2.3; 535 -1.8; 588 -1.3; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.4; 1146 -1.9; 1261 -2.6; 1387 -3.6; 1526 -4.8; 1678 -5.6; 1846 -6.6; 2031 -7.6; 2234 -8.2; 2457 -9.1; 2703 -10.4; 2973 -10.5; 3270 -7.7; 3597 -5.0; 3957 -5.1; 4353 -7.3; 4788 -9.3; 5267 -11.3; 5793 -12.6; 6373 -9.9; 7010 -8.6; 7711 -10.6; 8482 -12.3; 9330 -8.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C751K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C751K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 0.21 | -3.9 dB |
| Peaking | 701 Hz   | 0.63 | 6.4 dB  |
| Peaking | 2527 Hz  | 2.47 | -4.7 dB |
| Peaking | 6531 Hz  | 1.37 | -4.9 dB |
| Peaking | 22050 Hz | 2.32 | -2.8 dB |
| Peaking | 3932 Hz  | 3.41 | 5.4 dB  |
| Peaking | 5727 Hz  | 0.83 | -3.9 dB |
| Peaking | 6888 Hz  | 4.31 | 5.2 dB  |
| Peaking | 8632 Hz  | 4.74 | -5.3 dB |
| Peaking | 9452 Hz  | 1.56 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C751K/Denon%20AH-C751K.png)
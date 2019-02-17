# Denon AH-C351K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.2; 25 -8.3; 28 -8.4; 31 -8.5; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.0; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.1; 155 -12.2; 170 -12.2; 187 -12.4; 206 -12.2; 227 -12.2; 249 -12.0; 274 -11.8; 302 -12.1; 332 -11.8; 365 -11.4; 402 -11.0; 442 -10.6; 486 -10.1; 535 -9.6; 588 -9.0; 647 -8.5; 712 -7.9; 783 -7.4; 861 -7.0; 947 -6.8; 1042 -6.4; 1146 -6.0; 1261 -5.7; 1387 -5.5; 1526 -5.6; 1678 -5.7; 1846 -4.8; 2031 -3.5; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -3.0; 5267 -5.5; 5793 -10.8; 6373 -9.3; 7010 -5.5; 7711 -6.2; 8482 -8.4; 9330 -10.8; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.7; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C351K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C351K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 0.21 | -1.8 dB |
| Peaking | 225 Hz   | 0.47 | -4.6 dB |
| Peaking | 3262 Hz  | 1.03 | 7.1 dB  |
| Peaking | 5973 Hz  | 5.61 | -7.8 dB |
| Peaking | 15606 Hz | 3.1  | -2.9 dB |
| Peaking | 3129 Hz  | 5.52 | -2.0 dB |
| Peaking | 3500 Hz  | 2.05 | 2.2 dB  |
| Peaking | 3563 Hz  | 5.43 | -2.2 dB |
| Peaking | 9039 Hz  | 1.47 | 1.5 dB  |
| Peaking | 9172 Hz  | 4.45 | -6.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C351K/Denon%20AH-C351K.png)
# Denon AH-C351K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.7; 28 -7.8; 31 -7.9; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.9; 128 -11.2; 141 -11.5; 155 -11.6; 170 -11.7; 187 -11.8; 206 -11.6; 227 -11.6; 249 -11.4; 274 -11.2; 302 -11.5; 332 -11.2; 365 -10.8; 402 -10.4; 442 -10.0; 486 -9.6; 535 -9.0; 588 -8.5; 647 -7.9; 712 -7.3; 783 -6.8; 861 -6.4; 947 -6.2; 1042 -5.9; 1146 -5.4; 1261 -5.1; 1387 -4.9; 1526 -5.1; 1678 -5.1; 1846 -4.2; 2031 -3.0; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -5.0; 5793 -10.2; 6373 -8.7; 7010 -4.9; 7711 -6.2; 8482 -7.8; 9330 -10.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -7.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C351K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C351K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 151 Hz   | 0.45 | -4.6 dB |
| Peaking | 353 Hz   | 1.02 | -2.0 dB |
| Peaking | 3452 Hz  | 0.75 | 6.8 dB  |
| Peaking | 5935 Hz  | 5.66 | -8.5 dB |
| Peaking | 9181 Hz  | 4.92 | -5.1 dB |
| Peaking | 25 Hz    | 1.54 | -0.7 dB |
| Peaking | 1790 Hz  | 2.51 | -3.1 dB |
| Peaking | 2196 Hz  | 1.06 | 2.5 dB  |
| Peaking | 3145 Hz  | 2.48 | -1.8 dB |
| Peaking | 15636 Hz | 4.24 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C351K/Denon%20AH-C351K.png)
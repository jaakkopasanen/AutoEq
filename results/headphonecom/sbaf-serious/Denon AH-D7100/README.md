# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.3; 25 -13.3; 28 -13.2; 31 -13.1; 34 -13.0; 37 -12.8; 41 -12.6; 45 -12.3; 49 -12.1; 54 -11.6; 60 -10.7; 66 -10.6; 72 -11.1; 79 -11.7; 87 -12.6; 96 -13.7; 106 -13.9; 116 -13.9; 128 -13.8; 141 -13.5; 155 -12.9; 170 -11.4; 187 -11.1; 206 -9.3; 227 -6.7; 249 -3.7; 274 -0.9; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -1.1; 486 -1.9; 535 -2.8; 588 -3.6; 647 -4.6; 712 -5.1; 783 -5.4; 861 -5.8; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.4; 1387 -8.2; 1526 -9.3; 1678 -10.0; 1846 -9.8; 2031 -9.1; 2234 -7.7; 2457 -5.4; 2703 -3.9; 2973 -3.8; 3270 -2.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.7; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -11.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.8; 18182 -13.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.74 | -6.6 dB |
| Peaking | 141 Hz   | 0.75 | -8.7 dB |
| Peaking | 323 Hz   | 1.2  | 10.1 dB |
| Peaking | 4522 Hz  | 1.85 | 7.2 dB  |
| Peaking | 18090 Hz | 2.18 | -8.1 dB |
| Peaking | 508 Hz   | 3.29 | 1.3 dB  |
| Peaking | 1841 Hz  | 1.68 | -5.0 dB |
| Peaking | 2761 Hz  | 1.82 | 2.7 dB  |
| Peaking | 6536 Hz  | 4.84 | 2.0 dB  |
| Peaking | 9042 Hz  | 6.25 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)
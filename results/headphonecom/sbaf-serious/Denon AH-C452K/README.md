# Denon AH-C452K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.0; 25 -12.9; 28 -12.8; 31 -12.6; 34 -12.4; 37 -12.2; 41 -12.0; 45 -11.9; 49 -11.7; 54 -11.5; 60 -11.3; 66 -11.1; 72 -11.0; 79 -10.8; 87 -10.6; 96 -10.3; 106 -9.9; 116 -9.6; 128 -9.3; 141 -8.9; 155 -8.5; 170 -7.9; 187 -7.4; 206 -6.6; 227 -6.2; 249 -6.6; 274 -6.0; 302 -5.2; 332 -4.5; 365 -3.7; 402 -3.1; 442 -2.7; 486 -2.2; 535 -1.7; 588 -1.2; 647 -0.8; 712 -0.6; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.5; 1146 -2.1; 1261 -1.6; 1387 -2.0; 1526 -3.9; 1678 -5.2; 1846 -5.7; 2031 -6.1; 2234 -6.7; 2457 -7.4; 2703 -8.4; 2973 -8.2; 3270 -5.6; 3597 -3.1; 3957 -3.3; 4353 -5.6; 4788 -8.1; 5267 -11.0; 5793 -13.1; 6373 -8.0; 7010 -5.5; 7711 -6.6; 8482 -10.3; 9330 -9.5; 10263 -2.2; 11289 -1.3; 12418 -1.3; 13660 -1.3; 15026 -1.3; 16529 -1.3; 18182 -1.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C452K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C452K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.2  | -11.5 dB |
| Peaking | 156 Hz   | 0.74 | -3.2 dB  |
| Peaking | 2411 Hz  | 2.04 | -5.7 dB  |
| Peaking | 6116 Hz  | 1.19 | -8.7 dB  |
| Peaking | 22050 Hz | 2.34 | -6.2 dB  |
| Peaking | 3843 Hz  | 6.46 | 3.4 dB   |
| Peaking | 5639 Hz  | 5.31 | -5.2 dB  |
| Peaking | 6948 Hz  | 2.97 | 5.9 dB   |
| Peaking | 9024 Hz  | 2.96 | -10.0 dB |
| Peaking | 10400 Hz | 2.09 | 5.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB  |
| Peaking | 16000 Hz | 1.41 | 1.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C452K/Denon%20AH-C452K.png)
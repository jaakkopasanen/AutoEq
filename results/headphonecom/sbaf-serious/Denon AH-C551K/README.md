# Denon AH-C551K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.7; 25 -11.8; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.0; 41 -12.0; 45 -12.1; 49 -12.1; 54 -12.2; 60 -12.4; 66 -12.6; 72 -12.6; 79 -12.6; 87 -12.6; 96 -12.5; 106 -12.4; 116 -12.1; 128 -11.9; 141 -11.6; 155 -11.1; 170 -10.5; 187 -10.9; 206 -10.7; 227 -10.1; 249 -9.3; 274 -8.5; 302 -7.7; 332 -6.9; 365 -6.0; 402 -5.2; 442 -4.4; 486 -3.6; 535 -2.8; 588 -2.1; 647 -1.4; 712 -0.9; 783 -0.5; 861 -0.6; 947 -0.7; 1042 -1.2; 1146 -1.6; 1261 -2.1; 1387 -2.9; 1526 -4.5; 1678 -5.9; 1846 -6.9; 2031 -7.8; 2234 -8.8; 2457 -10.3; 2703 -12.3; 2973 -12.1; 3270 -8.1; 3597 -5.0; 3957 -5.1; 4353 -7.4; 4788 -9.8; 5267 -12.4; 5793 -13.3; 6373 -9.4; 7010 -7.9; 7711 -10.1; 8482 -12.3; 9330 -8.2; 10263 -1.2; 11289 -1.0; 12418 -1.0; 13660 -1.0; 15026 -3.5; 16529 -1.1; 18182 -1.0; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.26 | -11.4 dB |
| Peaking | 195 Hz   | 0.84 | -4.9 dB  |
| Peaking | 2564 Hz  | 2.02 | -9.4 dB  |
| Peaking | 6285 Hz  | 1.13 | -10.3 dB |
| Peaking | 20894 Hz | 2.34 | -8.3 dB  |
| Peaking | 3925 Hz  | 3.63 | 5.1 dB   |
| Peaking | 5895 Hz  | 1.05 | -4.8 dB  |
| Peaking | 6748 Hz  | 3.5  | 8.1 dB   |
| Peaking | 8724 Hz  | 3.38 | -8.0 dB  |
| Peaking | 10359 Hz | 2.05 | 6.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.1 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -8.7 dB  |
| Peaking | 250 Hz   | 1.41 | -7.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C551K/Denon%20AH-C551K.png)
# Beats Solo3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.4; 28 -7.6; 31 -7.8; 34 -8.0; 37 -8.0; 41 -8.1; 45 -8.1; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.6; 72 -8.7; 79 -8.8; 87 -9.0; 96 -9.1; 106 -9.2; 116 -9.4; 128 -9.4; 141 -9.4; 155 -9.4; 170 -9.2; 187 -8.9; 206 -8.5; 227 -8.0; 249 -7.4; 274 -6.7; 302 -5.9; 332 -5.2; 365 -4.6; 402 -4.1; 442 -4.2; 486 -3.7; 535 -2.9; 588 -2.1; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.5; 947 -1.0; 1042 -1.6; 1146 -2.4; 1261 -3.3; 1387 -4.0; 1526 -4.4; 1678 -4.9; 1846 -5.6; 2031 -5.8; 2234 -5.8; 2457 -5.6; 2703 -6.2; 2973 -7.1; 3270 -8.1; 3597 -8.8; 3957 -6.4; 4353 -5.6; 4788 -7.2; 5267 -5.6; 5793 -4.0; 6373 -4.6; 7010 -6.1; 7711 -6.8; 8482 -6.9; 9330 -5.7; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.42 | -2.6 dB |
| Peaking | 158 Hz  | 1.03 | -2.9 dB |
| Peaking | 777 Hz  | 1.1  | 5.4 dB  |
| Peaking | 3382 Hz | 2.43 | -3.1 dB |
| Peaking | 5764 Hz | 8.29 | 1.9 dB  |
| Peaking | 230 Hz  | 6.66 | -0.4 dB |
| Peaking | 1947 Hz | 2.58 | -1.7 dB |
| Peaking | 2103 Hz | 1.41 | 0.9 dB  |
| Peaking | 6291 Hz | 8.9  | 1.1 dB  |
| Peaking | 7921 Hz | 3.33 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)
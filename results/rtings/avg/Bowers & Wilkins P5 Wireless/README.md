# Bowers & Wilkins P5 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.0; 31 -7.0; 34 -6.9; 37 -6.7; 41 -6.5; 45 -6.4; 49 -6.4; 54 -6.3; 60 -6.3; 66 -6.4; 72 -6.3; 79 -6.3; 87 -6.2; 96 -6.3; 106 -6.3; 116 -6.2; 128 -6.1; 141 -5.9; 155 -5.7; 170 -5.7; 187 -5.6; 206 -5.3; 227 -5.2; 249 -5.1; 274 -4.8; 302 -4.3; 332 -3.7; 365 -2.6; 402 -1.7; 442 -1.1; 486 -0.8; 535 -0.6; 588 -0.5; 647 -0.7; 712 -1.0; 783 -1.4; 861 -1.9; 947 -2.6; 1042 -3.4; 1146 -4.0; 1261 -4.6; 1387 -5.7; 1526 -6.8; 1678 -7.4; 1846 -6.6; 2031 -4.0; 2234 -2.2; 2457 -1.7; 2703 -1.3; 2973 -1.2; 3270 -1.5; 3597 -1.8; 3957 -3.0; 4353 -4.3; 4788 -4.2; 5267 -3.3; 5793 -3.1; 6373 -3.4; 7010 -0.8; 7711 -2.8; 8482 -3.1; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -7.9; 18182 -12.0; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.07 | -3.4 dB  |
| Peaking | 546 Hz   | 0.99 | 4.8 dB   |
| Peaking | 1678 Hz  | 2.01 | -5.7 dB  |
| Peaking | 2488 Hz  | 1.76 | 3.4 dB   |
| Peaking | 18488 Hz | 1.4  | -10.0 dB |
| Peaking | 24 Hz    | 2.23 | -0.5 dB  |
| Peaking | 3660 Hz  | 3.47 | 1.3 dB   |
| Peaking | 4403 Hz  | 3.38 | -2.1 dB  |
| Peaking | 7009 Hz  | 9.55 | 2.6 dB   |
| Peaking | 14494 Hz | 2.83 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Wireless/Bowers%20&%20Wilkins%20P5%20Wireless.png)
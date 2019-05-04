# Bowers & Wilkins P5 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.6; 28 -6.7; 31 -6.7; 34 -6.6; 37 -6.5; 41 -6.3; 45 -6.2; 49 -6.1; 54 -6.1; 60 -6.1; 66 -6.1; 72 -6.1; 79 -6.0; 87 -6.0; 96 -5.9; 106 -5.9; 116 -5.8; 128 -5.8; 141 -5.6; 155 -5.4; 170 -5.3; 187 -5.2; 206 -5.1; 227 -5.0; 249 -4.9; 274 -4.7; 302 -4.2; 332 -3.5; 365 -2.5; 402 -1.5; 442 -0.9; 486 -0.7; 535 -0.5; 588 -0.5; 647 -0.6; 712 -0.9; 783 -1.4; 861 -1.9; 947 -2.6; 1042 -3.4; 1146 -4.1; 1261 -4.7; 1387 -5.9; 1526 -7.0; 1678 -7.5; 1846 -6.7; 2031 -4.3; 2234 -2.9; 2457 -2.5; 2703 -1.7; 2973 -1.1; 3270 -1.1; 3597 -1.5; 3957 -2.6; 4353 -4.0; 4788 -4.5; 5267 -3.6; 5793 -3.0; 6373 -2.3; 7010 -0.7; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -7.7; 18182 -11.6; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.06 | -3.2 dB |
| Peaking | 542 Hz   | 1.08 | 4.7 dB  |
| Peaking | 1618 Hz  | 2.29 | -5.1 dB |
| Peaking | 2914 Hz  | 2.3  | 2.6 dB  |
| Peaking | 18462 Hz | 1.42 | -9.8 dB |
| Peaking | 596 Hz   | 0.17 | 0.2 dB  |
| Peaking | 3632 Hz  | 5.79 | 0.8 dB  |
| Peaking | 4666 Hz  | 3.9  | -2.0 dB |
| Peaking | 6896 Hz  | 7.49 | 2.8 dB  |
| Peaking | 14515 Hz | 2.97 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P5%20Wireless/Bowers%20&%20Wilkins%20P5%20Wireless.png)
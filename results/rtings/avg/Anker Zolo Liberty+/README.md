# Anker Zolo Liberty+
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.6; 45 -6.8; 49 -7.1; 54 -7.4; 60 -7.9; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.5; 96 -9.8; 106 -9.9; 116 -9.9; 128 -9.7; 141 -9.3; 155 -8.9; 170 -8.5; 187 -8.1; 206 -7.1; 227 -5.6; 249 -4.4; 274 -3.3; 302 -2.5; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.5; 486 -1.4; 535 -1.1; 588 -0.9; 647 -0.7; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.2; 1042 -2.3; 1146 -3.4; 1261 -4.0; 1387 -4.3; 1526 -4.4; 1678 -4.5; 1846 -4.6; 2031 -4.6; 2234 -4.2; 2457 -3.5; 2703 -3.5; 2973 -4.6; 3270 -6.3; 3597 -7.3; 3957 -7.1; 4353 -6.3; 4788 -5.7; 5267 -4.9; 5793 -4.5; 6373 -5.8; 7010 -10.5; 7711 -13.9; 8482 -10.4; 9330 -5.3; 10263 -5.1; 11289 -6.9; 12418 -7.0; 13660 -5.6; 15026 -5.8; 16529 -8.7; 18182 -8.6; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker Zolo Liberty+ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker Zolo Liberty+ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 103 Hz   | 0.76 | -5.3 dB |
| Peaking | 180 Hz   | 2.39 | -2.0 dB |
| Peaking | 504 Hz   | 0.6  | 4.8 dB  |
| Peaking | 7705 Hz  | 4.62 | -9.8 dB |
| Peaking | 17385 Hz | 1.63 | -4.7 dB |
| Peaking | 864 Hz   | 4.24 | 1.7 dB  |
| Peaking | 2665 Hz  | 2.07 | 6.0 dB  |
| Peaking | 3048 Hz  | 0.98 | -5.3 dB |
| Peaking | 5683 Hz  | 2.69 | 2.8 dB  |
| Peaking | 11961 Hz | 7.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20Zolo%20Liberty+/Anker%20Zolo%20Liberty+.png)
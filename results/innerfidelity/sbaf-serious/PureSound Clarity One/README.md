# PureSound Clarity One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.5; 28 -6.2; 31 -6.7; 34 -7.1; 37 -7.5; 41 -7.9; 45 -8.3; 49 -8.6; 54 -9.0; 60 -9.4; 66 -9.8; 72 -10.1; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.1; 116 -11.1; 128 -11.2; 141 -11.1; 155 -11.0; 170 -10.8; 187 -10.4; 206 -10.1; 227 -9.6; 249 -9.1; 274 -8.5; 302 -7.9; 332 -7.3; 365 -6.6; 402 -5.9; 442 -5.0; 486 -4.5; 535 -3.8; 588 -2.8; 647 -2.1; 712 -1.7; 783 -1.0; 861 -0.8; 947 -0.5; 1042 -0.5; 1146 -0.6; 1261 -0.9; 1387 -1.5; 1526 -2.5; 1678 -3.1; 1846 -3.1; 2031 -2.7; 2234 -2.5; 2457 -2.0; 2703 -2.2; 2973 -2.7; 3270 -3.4; 3597 -3.8; 3957 -3.9; 4353 -5.4; 4788 -6.1; 5267 -6.6; 5793 -10.1; 6373 -14.1; 7010 -9.1; 7711 -5.2; 8482 -3.6; 9330 -4.5; 10263 -4.7; 11289 -1.5; 12418 -0.5; 13660 -0.5; 15026 -1.2; 16529 -4.0; 18182 -2.4; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PureSound Clarity One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PureSound Clarity One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.37 | -6.7 dB  |
| Peaking | 151 Hz   | 0.64 | -6.1 dB  |
| Peaking | 311 Hz   | 1.08 | -3.0 dB  |
| Peaking | 6219 Hz  | 1.76 | -11.7 dB |
| Peaking | 17011 Hz | 2.58 | -3.8 dB  |
| Peaking | 1842 Hz  | 3.16 | -2.1 dB  |
| Peaking | 8032 Hz  | 4.91 | 2.4 dB   |
| Peaking | 10175 Hz | 3.74 | -3.6 dB  |
| Peaking | 11962 Hz | 1.27 | 2.6 dB   |
| Peaking | 12498 Hz | 0.34 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PureSound%20Clarity%20One/PureSound%20Clarity%20One.png)
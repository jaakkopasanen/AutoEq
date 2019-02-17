# HiFiMAN Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.5; 34 -1.9; 37 -2.2; 41 -2.5; 45 -2.6; 49 -2.7; 54 -2.9; 60 -3.0; 66 -3.1; 72 -3.3; 79 -3.6; 87 -4.2; 96 -4.6; 106 -4.8; 116 -4.8; 128 -5.0; 141 -5.1; 155 -5.2; 170 -5.3; 187 -5.4; 206 -5.4; 227 -5.6; 249 -5.8; 274 -5.8; 302 -6.0; 332 -5.7; 365 -5.0; 402 -4.9; 442 -5.2; 486 -6.0; 535 -6.4; 588 -6.1; 647 -6.3; 712 -5.7; 783 -3.7; 861 -4.9; 947 -6.0; 1042 -4.8; 1146 -3.2; 1261 -3.0; 1387 -4.0; 1526 -3.7; 1678 -4.4; 1846 -4.5; 2031 -4.1; 2234 -4.6; 2457 -4.3; 2703 -4.6; 2973 -5.0; 3270 -4.4; 3597 -3.8; 3957 -4.4; 4353 -6.4; 4788 -5.5; 5267 -2.7; 5793 -2.2; 6373 -4.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.21 | 5.6 dB  |
| Peaking | 48 Hz   | 0.06 | 0.6 dB  |
| Peaking | 1203 Hz | 6.12 | 2.7 dB  |
| Peaking | 2138 Hz | 0.66 | 2.1 dB  |
| Peaking | 5704 Hz | 4.76 | 4.2 dB  |
| Peaking | 401 Hz  | 5.53 | 1.2 dB  |
| Peaking | 752 Hz  | 1.75 | -1.5 dB |
| Peaking | 791 Hz  | 6.86 | 3.4 dB  |
| Peaking | 3669 Hz | 6.4  | 1.5 dB  |
| Peaking | 4472 Hz | 9.02 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X/HiFiMAN%20Edition%20X.png)
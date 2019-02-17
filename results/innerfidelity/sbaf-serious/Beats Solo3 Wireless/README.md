# Beats Solo3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -7.9; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.2; 66 -9.3; 72 -9.4; 79 -9.6; 87 -9.8; 96 -10.2; 106 -10.6; 116 -10.4; 128 -10.5; 141 -10.8; 155 -11.0; 170 -10.5; 187 -10.7; 206 -10.5; 227 -10.1; 249 -9.6; 274 -8.8; 302 -8.1; 332 -7.4; 365 -6.8; 402 -5.6; 442 -5.1; 486 -4.9; 535 -4.4; 588 -3.4; 647 -2.8; 712 -2.4; 783 -1.9; 861 -2.1; 947 -2.2; 1042 -2.5; 1146 -2.8; 1261 -3.2; 1387 -3.8; 1526 -4.2; 1678 -4.3; 1846 -4.1; 2031 -3.5; 2234 -3.3; 2457 -3.0; 2703 -3.3; 2973 -3.8; 3270 -4.6; 3597 -5.1; 3957 -3.2; 4353 -4.2; 4788 -5.0; 5267 -2.6; 5793 -0.5; 6373 -1.6; 7010 -1.1; 7711 -2.1; 8482 -2.4; 9330 -2.4; 10263 -2.4; 11289 -2.4; 12418 -2.4; 13660 -2.4; 15026 -2.4; 16529 -2.4; 18182 -2.5; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.32 | -5.7 dB |
| Peaking | 140 Hz  | 0.83 | -4.4 dB |
| Peaking | 251 Hz  | 1.19 | -4.0 dB |
| Peaking | 1665 Hz | 3.46 | -1.9 dB |
| Peaking | 3499 Hz | 2.72 | -2.4 dB |
| Peaking | 495 Hz  | 3.87 | -0.7 dB |
| Peaking | 773 Hz  | 2.66 | 1.3 dB  |
| Peaking | 4850 Hz | 5.93 | -3.6 dB |
| Peaking | 5714 Hz | 2.4  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)
# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.0; 25 -6.0; 28 -6.2; 31 -6.3; 34 -6.4; 37 -6.4; 41 -6.5; 45 -6.7; 49 -6.8; 54 -7.0; 60 -7.5; 66 -8.0; 72 -8.4; 79 -8.9; 87 -9.4; 96 -10.0; 106 -10.6; 116 -11.1; 128 -11.6; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.2; 206 -12.1; 227 -11.9; 249 -11.7; 274 -11.3; 302 -10.8; 332 -10.2; 365 -9.6; 402 -8.9; 442 -8.2; 486 -7.4; 535 -6.5; 588 -5.6; 647 -4.6; 712 -3.7; 783 -3.3; 861 -3.2; 947 -3.6; 1042 -4.3; 1146 -4.8; 1261 -4.9; 1387 -4.9; 1526 -4.8; 1678 -4.8; 1846 -4.7; 2031 -4.4; 2234 -3.2; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -0.9; 3597 -1.6; 3957 -2.3; 4353 -3.2; 4788 -3.4; 5267 -3.9; 5793 -5.4; 6373 -9.5; 7010 -11.3; 7711 -9.1; 8482 -8.7; 9330 -11.8; 10263 -13.4; 11289 -12.1; 12418 -12.1; 13660 -11.4; 15026 -5.5; 16529 -4.0; 18182 -4.0; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 139 Hz   | 0.57 | -7.1 dB |
| Peaking | 285 Hz   | 1.21 | -3.5 dB |
| Peaking | 3201 Hz  | 1.73 | 4.1 dB  |
| Peaking | 6828 Hz  | 5.9  | -5.6 dB |
| Peaking | 11100 Hz | 1.21 | -9.6 dB |
| Peaking | 26 Hz    | 1.39 | -1.4 dB |
| Peaking | 802 Hz   | 2.95 | 2.2 dB  |
| Peaking | 1749 Hz  | 1.21 | -1.4 dB |
| Peaking | 2573 Hz  | 4.4  | 1.6 dB  |
| Peaking | 16002 Hz | 4.35 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)
# Sennheiser HD1 In-Ear Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.1; 25 -6.2; 28 -6.3; 31 -6.3; 34 -6.4; 37 -6.5; 41 -6.6; 45 -6.7; 49 -6.8; 54 -7.0; 60 -7.5; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.3; 96 -9.8; 106 -10.5; 116 -11.0; 128 -11.6; 141 -12.1; 155 -12.3; 170 -12.3; 187 -12.3; 206 -12.1; 227 -11.9; 249 -11.6; 274 -11.3; 302 -10.8; 332 -10.2; 365 -9.5; 402 -8.9; 442 -8.1; 486 -7.3; 535 -6.3; 588 -5.3; 647 -4.3; 712 -3.5; 783 -3.0; 861 -3.0; 947 -3.3; 1042 -3.8; 1146 -4.3; 1261 -4.5; 1387 -4.7; 1526 -4.7; 1678 -4.6; 1846 -4.6; 2031 -4.2; 2234 -2.9; 2457 -1.7; 2703 -0.7; 2973 -0.5; 3270 -0.9; 3597 -1.6; 3957 -2.3; 4353 -3.1; 4788 -3.2; 5267 -3.8; 5793 -6.0; 6373 -9.3; 7010 -10.7; 7711 -8.3; 8482 -7.5; 9330 -10.7; 10263 -14.3; 11289 -14.5; 12418 -13.3; 13660 -10.9; 15026 -4.5; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.23 | -2.5 dB  |
| Peaking | 196 Hz   | 0.64 | -7.5 dB  |
| Peaking | 3148 Hz  | 2    | 3.7 dB   |
| Peaking | 6768 Hz  | 5.26 | -5.8 dB  |
| Peaking | 11300 Hz | 1.58 | -11.9 dB |
| Peaking | 406 Hz   | 2.28 | -1.1 dB  |
| Peaking | 786 Hz   | 2    | 2.4 dB   |
| Peaking | 1800 Hz  | 1.33 | -1.7 dB  |
| Peaking | 2506 Hz  | 2.85 | 1.4 dB   |
| Peaking | 15016 Hz | 3.18 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -7.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)
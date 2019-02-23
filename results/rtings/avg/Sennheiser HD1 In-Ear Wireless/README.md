# Sennheiser HD1 In-Ear Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -5.9; 25 -6.0; 28 -6.1; 31 -6.1; 34 -6.2; 37 -6.3; 41 -6.4; 45 -6.5; 49 -6.6; 54 -6.8; 60 -7.3; 66 -7.8; 72 -8.1; 79 -8.6; 87 -9.1; 96 -9.6; 106 -10.2; 116 -10.8; 128 -11.4; 141 -11.8; 155 -12.1; 170 -12.1; 187 -12.1; 206 -11.9; 227 -11.7; 249 -11.4; 274 -11.1; 302 -10.5; 332 -9.9; 365 -9.3; 402 -8.6; 442 -7.9; 486 -7.0; 535 -6.1; 588 -5.1; 647 -4.1; 712 -3.3; 783 -2.8; 861 -2.8; 947 -3.0; 1042 -3.6; 1146 -4.1; 1261 -4.3; 1387 -4.5; 1526 -4.5; 1678 -4.4; 1846 -4.4; 2031 -3.9; 2234 -2.7; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -0.7; 3597 -1.4; 3957 -2.1; 4353 -2.8; 4788 -3.0; 5267 -3.6; 5793 -5.8; 6373 -9.1; 7010 -10.5; 7711 -8.1; 8482 -7.2; 9330 -10.5; 10263 -14.1; 11289 -14.2; 12418 -13.1; 13660 -10.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 192 Hz   | 0.66 | -6.0 dB |
| Peaking | 785 Hz   | 1.49 | 4.3 dB  |
| Peaking | 3275 Hz  | 0.96 | 6.0 dB  |
| Peaking | 6755 Hz  | 5.96 | -5.0 dB |
| Peaking | 11240 Hz | 1.91 | -9.0 dB |
| Peaking | 31 Hz    | 1.06 | 0.9 dB  |
| Peaking | 1169 Hz  | 2.45 | 0.3 dB  |
| Peaking | 2105 Hz  | 1.61 | -0.9 dB |
| Peaking | 2554 Hz  | 4.39 | 1.5 dB  |
| Peaking | 14933 Hz | 2.82 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)
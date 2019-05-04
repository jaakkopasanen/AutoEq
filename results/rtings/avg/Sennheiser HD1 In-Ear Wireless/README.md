# Sennheiser HD1 In-Ear Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.5; 25 -10.6; 28 -10.7; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.4; 60 -11.6; 66 -11.8; 72 -12.0; 79 -12.2; 87 -12.4; 96 -12.6; 106 -12.8; 116 -12.9; 128 -12.9; 141 -12.9; 155 -12.7; 170 -12.5; 187 -12.2; 206 -11.8; 227 -11.4; 249 -11.1; 274 -10.8; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.3; 442 -7.6; 486 -6.9; 535 -5.9; 588 -5.0; 647 -4.0; 712 -3.3; 783 -2.7; 861 -2.6; 947 -3.0; 1042 -3.5; 1146 -4.0; 1261 -4.2; 1387 -4.4; 1526 -4.5; 1678 -4.5; 1846 -4.4; 2031 -4.2; 2234 -3.3; 2457 -1.9; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.5; 4353 -2.2; 4788 -3.1; 5267 -3.6; 5793 -4.6; 6373 -7.5; 7010 -10.3; 7711 -8.6; 8482 -6.8; 9330 -9.0; 10263 -13.6; 11289 -14.8; 12418 -12.9; 13660 -9.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD1 In-Ear Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD1 In-Ear Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.23 | -3.9 dB |
| Peaking | 146 Hz   | 0.68 | -4.4 dB |
| Peaking | 320 Hz   | 1.25 | -2.6 dB |
| Peaking | 2065 Hz  | 0.21 | 4.1 dB  |
| Peaking | 11049 Hz | 1.55 | -9.8 dB |
| Peaking | 808 Hz   | 2.52 | 2.0 dB  |
| Peaking | 2033 Hz  | 0.85 | -4.2 dB |
| Peaking | 2917 Hz  | 1.35 | 4.8 dB  |
| Peaking | 6905 Hz  | 5.32 | -5.7 dB |
| Peaking | 9456 Hz  | 0.2  | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD1%20In-Ear%20Wireless/Sennheiser%20HD1%20In-Ear%20Wireless.png)
# Sennheiser PXC 550 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.0; 25 -4.7; 28 -5.5; 31 -6.0; 34 -6.4; 37 -6.6; 41 -6.7; 45 -6.7; 49 -6.6; 54 -6.3; 60 -6.2; 66 -6.1; 72 -6.1; 79 -6.3; 87 -6.5; 96 -6.8; 106 -7.2; 116 -7.6; 128 -7.9; 141 -8.1; 155 -8.2; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.9; 249 -7.7; 274 -7.4; 302 -7.0; 332 -6.8; 365 -6.6; 402 -6.7; 442 -7.0; 486 -7.3; 535 -7.5; 588 -7.3; 647 -7.0; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.6; 1042 -6.0; 1146 -6.4; 1261 -6.2; 1387 -7.5; 1526 -9.3; 1678 -10.9; 1846 -11.3; 2031 -12.1; 2234 -11.3; 2457 -9.8; 2703 -9.1; 2973 -8.9; 3270 -8.4; 3597 -9.1; 3957 -6.5; 4353 -0.5; 4788 -6.7; 5267 -11.2; 5793 -7.0; 6373 -5.5; 7010 -7.0; 7711 -9.7; 8482 -13.0; 9330 -14.4; 10263 -12.0; 11289 -9.6; 12418 -12.0; 13660 -15.8; 15026 -13.7; 16529 -8.0; 18182 -7.3; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 3.38 | 2.1 dB  |
| Peaking | 1735 Hz  | 3.25 | -2.7 dB |
| Peaking | 2167 Hz  | 2.11 | -4.8 dB |
| Peaking | 12821 Hz | 0.73 | -7.9 dB |
| Peaking | 19995 Hz | 2.69 | -7.5 dB |
| Peaking | 181 Hz   | 0.72 | -2.4 dB |
| Peaking | 6763 Hz  | 3.37 | 4.2 dB  |
| Peaking | 9212 Hz  | 1.6  | -4.9 dB |
| Peaking | 11185 Hz | 4.02 | 6.2 dB  |
| Peaking | 17358 Hz | 4.43 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)
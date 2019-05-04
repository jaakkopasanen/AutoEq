# Sennheiser PXC 550 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.2; 25 -2.9; 28 -3.7; 31 -4.3; 34 -4.7; 37 -4.9; 41 -5.0; 45 -5.0; 49 -4.9; 54 -4.7; 60 -4.5; 66 -4.4; 72 -4.4; 79 -4.5; 87 -4.7; 96 -5.1; 106 -5.4; 116 -5.9; 128 -6.3; 141 -6.7; 155 -7.0; 170 -7.2; 187 -7.2; 206 -7.0; 227 -6.7; 249 -6.3; 274 -5.9; 302 -5.5; 332 -5.2; 365 -5.0; 402 -5.0; 442 -5.4; 486 -5.8; 535 -5.9; 588 -5.8; 647 -5.5; 712 -5.0; 783 -4.6; 861 -4.2; 947 -4.2; 1042 -4.6; 1146 -4.9; 1261 -4.9; 1387 -6.1; 1526 -8.0; 1678 -9.5; 1846 -10.2; 2031 -11.0; 2234 -10.6; 2457 -9.2; 2703 -8.2; 2973 -7.4; 3270 -6.7; 3597 -7.3; 3957 -4.4; 4353 -0.5; 4788 -5.4; 5267 -9.8; 5793 -5.3; 6373 -3.1; 7010 -5.6; 7711 -9.0; 8482 -11.1; 9330 -11.1; 10263 -9.8; 11289 -9.0; 12418 -10.7; 13660 -13.6; 15026 -11.6; 16529 -6.7; 18182 -6.5; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2096 Hz  | 1.2  | -10.3 dB |
| Peaking | 2182 Hz  | 0.37 | 5.8 dB   |
| Peaking | 8893 Hz  | 2.91 | -5.9 dB  |
| Peaking | 13795 Hz | 2.18 | -7.6 dB  |
| Peaking | 17 Hz    | 1.12 | 5.9 dB   |
| Peaking | 71 Hz    | 1.98 | 2.0 dB   |
| Peaking | 4430 Hz  | 5.53 | 10.4 dB  |
| Peaking | 5190 Hz  | 2.23 | -9.8 dB  |
| Peaking | 6169 Hz  | 3.55 | 7.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)
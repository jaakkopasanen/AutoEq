# V-Moda Crossfade Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -5.1; 25 -6.0; 28 -7.3; 31 -8.3; 34 -9.0; 37 -9.5; 41 -10.1; 45 -10.4; 49 -10.7; 54 -10.9; 60 -11.0; 66 -10.6; 72 -10.6; 79 -11.6; 87 -12.4; 96 -12.5; 106 -11.9; 116 -12.4; 128 -12.7; 141 -12.8; 155 -12.7; 170 -11.8; 187 -11.7; 206 -10.9; 227 -9.7; 249 -8.4; 274 -6.7; 302 -4.7; 332 -3.1; 365 -1.7; 402 -1.0; 442 -1.2; 486 -1.1; 535 -1.3; 588 -1.6; 647 -2.0; 712 -3.0; 783 -3.8; 861 -5.0; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -7.5; 1387 -7.9; 1526 -8.2; 1678 -8.1; 1846 -7.6; 2031 -6.9; 2234 -7.2; 2457 -7.4; 2703 -6.6; 2973 -7.1; 3270 -8.3; 3597 -10.5; 3957 -8.2; 4353 -5.8; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -10.7; 10263 -10.9; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 2.06 | -2.1 dB |
| Peaking | 149 Hz  | 0.52 | -7.2 dB |
| Peaking | 418 Hz  | 1.15 | 8.9 dB  |
| Peaking | 5750 Hz | 3.22 | 7.4 dB  |
| Peaking | 9773 Hz | 3.83 | -5.6 dB |
| Peaking | 441 Hz  | 6.58 | -1.4 dB |
| Peaking | 670 Hz  | 2.1  | 1.9 dB  |
| Peaking | 1385 Hz | 1.3  | -2.2 dB |
| Peaking | 3657 Hz | 4.58 | -4.6 dB |
| Peaking | 4822 Hz | 7.87 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 7.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Bluetooth/V-Moda%20Crossfade%20Wireless%20Bluetooth.png)
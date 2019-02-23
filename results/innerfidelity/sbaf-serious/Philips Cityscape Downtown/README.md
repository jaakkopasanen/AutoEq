# Philips Cityscape Downtown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.0; 25 -7.1; 28 -7.1; 31 -7.2; 34 -7.1; 37 -7.1; 41 -7.1; 45 -7.0; 49 -7.0; 54 -6.9; 60 -6.9; 66 -6.8; 72 -6.8; 79 -6.8; 87 -7.0; 96 -7.1; 106 -7.1; 116 -7.0; 128 -7.0; 141 -7.1; 155 -7.6; 170 -7.3; 187 -7.9; 206 -8.1; 227 -8.2; 249 -8.4; 274 -8.3; 302 -8.4; 332 -8.4; 365 -8.5; 402 -8.7; 442 -9.1; 486 -9.8; 535 -10.2; 588 -10.3; 647 -10.7; 712 -11.2; 783 -11.4; 861 -11.8; 947 -12.0; 1042 -12.0; 1146 -11.7; 1261 -11.4; 1387 -11.2; 1526 -10.7; 1678 -9.8; 1846 -8.7; 2031 -7.0; 2234 -5.2; 2457 -2.9; 2703 -1.4; 2973 -1.8; 3270 -0.5; 3597 -2.8; 3957 -6.3; 4353 -7.6; 4788 -5.7; 5267 -1.8; 5793 -0.5; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Cityscape Downtown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Cityscape Downtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 279 Hz   | 0    | -0.5 dB |
| Peaking | 1164 Hz  | 0.52 | -5.9 dB |
| Peaking | 2982 Hz  | 1.33 | 9.1 dB  |
| Peaking | 4309 Hz  | 3.78 | -5.3 dB |
| Peaking | 5742 Hz  | 2.98 | 6.4 dB  |
| Peaking | 222 Hz   | 3.86 | -0.6 dB |
| Peaking | 6758 Hz  | 8.28 | 2.3 dB  |
| Peaking | 7325 Hz  | 2.07 | -1.3 dB |
| Peaking | 14902 Hz | 0.24 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -6.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Cityscape%20Downtown/Philips%20Cityscape%20Downtown.png)
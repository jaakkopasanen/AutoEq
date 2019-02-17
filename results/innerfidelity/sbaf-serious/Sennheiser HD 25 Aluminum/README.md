# Sennheiser HD 25 Aluminum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.3; 25 -10.5; 28 -10.8; 31 -11.0; 34 -11.1; 37 -11.2; 41 -11.3; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.2; 66 -11.2; 72 -11.1; 79 -10.6; 87 -10.5; 96 -11.8; 106 -13.1; 116 -13.7; 128 -13.7; 141 -13.2; 155 -12.3; 170 -11.9; 187 -11.1; 206 -10.1; 227 -9.1; 249 -7.9; 274 -6.4; 302 -5.5; 332 -4.8; 365 -4.3; 402 -4.0; 442 -3.9; 486 -4.5; 535 -4.8; 588 -4.8; 647 -5.1; 712 -5.5; 783 -5.5; 861 -6.0; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.3; 1526 -9.3; 1678 -10.3; 1846 -10.8; 2031 -11.0; 2234 -10.3; 2457 -8.9; 2703 -7.4; 2973 -6.1; 3270 -5.7; 3597 -6.1; 3957 -6.0; 4353 -4.4; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.4; 8482 -12.8; 9330 -11.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25 Aluminum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 Aluminum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.62 | -4.9 dB |
| Peaking | 131 Hz  | 1.69 | -6.6 dB |
| Peaking | 1958 Hz | 2.29 | -5.3 dB |
| Peaking | 5782 Hz | 1.79 | 7.5 dB  |
| Peaking | 8584 Hz | 3.76 | -9.0 dB |
| Peaking | 208 Hz  | 2.15 | -2.7 dB |
| Peaking | 388 Hz  | 0.91 | 3.2 dB  |
| Peaking | 1505 Hz | 4.53 | -1.1 dB |
| Peaking | 4100 Hz | 6.58 | -1.9 dB |
| Peaking | 4770 Hz | 8.78 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025%20Aluminum/Sennheiser%20HD%2025%20Aluminum.png)
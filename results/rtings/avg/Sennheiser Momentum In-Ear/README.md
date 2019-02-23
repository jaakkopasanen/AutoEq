# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.8; 31 -5.9; 34 -6.0; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.4; 54 -6.6; 60 -7.1; 66 -7.6; 72 -8.0; 79 -8.5; 87 -9.0; 96 -9.6; 106 -10.2; 116 -10.7; 128 -11.2; 141 -11.6; 155 -11.8; 170 -11.9; 187 -11.8; 206 -11.7; 227 -11.5; 249 -11.3; 274 -10.9; 302 -10.4; 332 -9.8; 365 -9.2; 402 -8.5; 442 -7.8; 486 -7.0; 535 -6.1; 588 -5.2; 647 -4.2; 712 -3.3; 783 -2.9; 861 -2.8; 947 -3.2; 1042 -3.9; 1146 -4.4; 1261 -4.5; 1387 -4.5; 1526 -4.4; 1678 -4.4; 1846 -4.3; 2031 -4.0; 2234 -2.8; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.9; 4353 -2.8; 4788 -3.0; 5267 -3.5; 5793 -5.0; 6373 -9.1; 7010 -10.9; 7711 -8.7; 8482 -8.3; 9330 -11.4; 10263 -13.0; 11289 -11.7; 12418 -11.7; 13660 -11.0; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.67 | -5.8 dB |
| Peaking | 779 Hz   | 1.62 | 4.2 dB  |
| Peaking | 3312 Hz  | 0.92 | 6.2 dB  |
| Peaking | 6804 Hz  | 6.22 | -5.1 dB |
| Peaking | 10958 Hz | 1.37 | -6.9 dB |
| Peaking | 29 Hz    | 0.95 | 1.2 dB  |
| Peaking | 2087 Hz  | 3.33 | -1.7 dB |
| Peaking | 2419 Hz  | 2.68 | 1.6 dB  |
| Peaking | 3813 Hz  | 4.75 | -0.7 dB |
| Peaking | 15605 Hz | 5.13 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)
# Ultimate Ears UE700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.5; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.9; 37 -5.0; 41 -5.1; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.4; 96 -7.9; 106 -8.0; 116 -8.2; 128 -8.5; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.4; 249 -9.3; 274 -9.2; 302 -9.1; 332 -9.0; 365 -8.8; 402 -8.6; 442 -8.3; 486 -8.2; 535 -7.9; 588 -7.3; 647 -7.1; 712 -7.0; 783 -6.8; 861 -7.0; 947 -7.2; 1042 -7.4; 1146 -7.6; 1261 -7.8; 1387 -8.2; 1526 -8.5; 1678 -8.6; 1846 -8.2; 2031 -7.5; 2234 -6.6; 2457 -5.0; 2703 -2.8; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -2.0; 5267 -1.1; 5793 -1.3; 6373 -2.4; 7010 -4.8; 7711 -7.6; 8482 -10.8; 9330 -11.6; 10263 -8.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 230 Hz   | 0.73 | -3.1 dB |
| Peaking | 1919 Hz  | 1.23 | -4.4 dB |
| Peaking | 3255 Hz  | 1.18 | 7.5 dB  |
| Peaking | 5872 Hz  | 2.1  | 4.0 dB  |
| Peaking | 8907 Hz  | 2.98 | -6.9 dB |
| Peaking | 36 Hz    | 0.1  | 2.2 dB  |
| Peaking | 53 Hz    | 1.37 | 0.3 dB  |
| Peaking | 110 Hz   | 0.62 | -2.4 dB |
| Peaking | 403 Hz   | 1.68 | -0.9 dB |
| Peaking | 11147 Hz | 7.96 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)
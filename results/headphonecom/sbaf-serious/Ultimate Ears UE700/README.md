# Ultimate Ears UE700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.9; 25 -4.9; 28 -5.0; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.6; 49 -5.7; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.1; 87 -7.4; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.5; 141 -8.8; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.2; 227 -9.3; 249 -9.3; 274 -9.2; 302 -9.0; 332 -8.8; 365 -8.4; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.5; 588 -7.0; 647 -6.8; 712 -6.7; 783 -6.5; 861 -6.6; 947 -6.8; 1042 -7.1; 1146 -7.3; 1261 -7.6; 1387 -8.0; 1526 -8.4; 1678 -8.5; 1846 -8.2; 2031 -7.5; 2234 -6.5; 2457 -4.9; 2703 -2.9; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -1.3; 5793 -1.0; 6373 -2.5; 7010 -5.1; 7711 -9.0; 8482 -14.1; 9330 -15.1; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 216 Hz   | 0.77 | -3.0 dB  |
| Peaking | 1941 Hz  | 1.25 | -5.6 dB  |
| Peaking | 3283 Hz  | 0.88 | 8.0 dB   |
| Peaking | 5959 Hz  | 3.33 | 3.5 dB   |
| Peaking | 8876 Hz  | 3.71 | -11.3 dB |
| Peaking | 25 Hz    | 1.32 | 1.7 dB   |
| Peaking | 47 Hz    | 2.31 | 0.8 dB   |
| Peaking | 769 Hz   | 4.35 | 0.5 dB   |
| Peaking | 10840 Hz | 8.5  | 1.9 dB   |
| Peaking | 18065 Hz | 3.63 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)
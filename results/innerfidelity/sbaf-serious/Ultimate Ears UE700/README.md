# Ultimate Ears UE700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.7; 25 -3.8; 28 -3.9; 31 -4.0; 34 -4.1; 37 -4.2; 41 -4.3; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.6; 96 -7.1; 106 -7.2; 116 -7.4; 128 -7.7; 141 -8.1; 155 -8.3; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.5; 249 -8.5; 274 -8.4; 302 -8.3; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.5; 486 -7.4; 535 -7.1; 588 -6.5; 647 -6.3; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.4; 1526 -7.7; 1678 -7.8; 1846 -7.4; 2031 -6.7; 2234 -5.8; 2457 -4.1; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -0.5; 5793 -0.6; 6373 -1.6; 7010 -4.1; 7711 -6.9; 8482 -10.0; 9330 -10.8; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.52 | 2.7 dB  |
| Peaking | 52 Hz   | 1.06 | 1.1 dB  |
| Peaking | 205 Hz  | 0.57 | -2.2 dB |
| Peaking | 4598 Hz | 0.97 | 7.0 dB  |
| Peaking | 8944 Hz | 3.14 | -6.8 dB |
| Peaking | 777 Hz  | 1.73 | 1.1 dB  |
| Peaking | 1852 Hz | 1.2  | -2.7 dB |
| Peaking | 2897 Hz | 2.87 | 3.6 dB  |
| Peaking | 4623 Hz | 4.28 | -1.6 dB |
| Peaking | 6013 Hz | 4.85 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)
# Yamaha HP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.3; 41 -1.9; 45 -2.5; 49 -3.1; 54 -3.5; 60 -4.2; 66 -4.9; 72 -5.4; 79 -6.0; 87 -6.5; 96 -7.2; 106 -7.7; 116 -7.8; 128 -8.4; 141 -8.9; 155 -9.2; 170 -9.3; 187 -9.5; 206 -9.6; 227 -9.6; 249 -9.6; 274 -9.6; 302 -9.5; 332 -9.4; 365 -9.3; 402 -9.2; 442 -8.9; 486 -9.1; 535 -9.0; 588 -8.9; 647 -8.8; 712 -8.9; 783 -8.7; 861 -8.9; 947 -8.9; 1042 -9.0; 1146 -8.8; 1261 -8.3; 1387 -7.9; 1526 -7.2; 1678 -5.9; 1846 -4.0; 2031 -2.6; 2234 -2.8; 2457 -3.3; 2703 -4.9; 2973 -3.8; 3270 -2.0; 3597 -1.9; 3957 -3.8; 4353 -3.8; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.55 | 7.2 dB  |
| Peaking | 285 Hz  | 0.15 | -3.2 dB |
| Peaking | 2100 Hz | 2.75 | 5.3 dB  |
| Peaking | 3415 Hz | 3.45 | 4.3 dB  |
| Peaking | 5682 Hz | 2.75 | 6.6 dB  |
| Peaking | 74 Hz   | 1.75 | 0.4 dB  |
| Peaking | 184 Hz  | 1.34 | -0.6 dB |
| Peaking | 505 Hz  | 1.49 | 0.6 dB  |
| Peaking | 6541 Hz | 7.67 | 2.1 dB  |
| Peaking | 7677 Hz | 2.31 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP3/Yamaha%20HP3.png)
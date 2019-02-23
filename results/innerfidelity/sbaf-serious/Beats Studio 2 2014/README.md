# Beats Studio 2 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -4.7; 25 -6.2; 28 -7.9; 31 -8.8; 34 -9.4; 37 -9.6; 41 -9.6; 45 -9.7; 49 -9.7; 54 -9.8; 60 -9.8; 66 -9.9; 72 -10.0; 79 -10.2; 87 -10.5; 96 -10.7; 106 -10.6; 116 -10.3; 128 -10.1; 141 -9.7; 155 -9.5; 170 -9.1; 187 -8.7; 206 -8.3; 227 -7.7; 249 -7.1; 274 -6.3; 302 -5.3; 332 -4.0; 365 -2.8; 402 -0.8; 442 -0.5; 486 -0.5; 535 -1.8; 588 -3.9; 647 -7.4; 712 -10.2; 783 -11.3; 861 -11.3; 947 -10.3; 1042 -10.0; 1146 -9.8; 1261 -10.4; 1387 -9.7; 1526 -9.1; 1678 -8.6; 1846 -7.2; 2031 -6.1; 2234 -5.3; 2457 -4.8; 2703 -5.1; 2973 -6.4; 3270 -9.1; 3597 -8.7; 3957 -6.6; 4353 -4.0; 4788 -1.0; 5267 -0.9; 5793 -2.2; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -11.2; 10263 -11.2; 11289 -7.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio 2 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 288 Hz  | 0.15 | -4.8 dB |
| Peaking | 422 Hz  | 1.51 | 11.5 dB |
| Peaking | 5631 Hz | 1.78 | 6.6 dB  |
| Peaking | 9647 Hz | 3.17 | -6.4 dB |
| Peaking | 39 Hz   | 3.34 | -0.9 dB |
| Peaking | 568 Hz  | 3.52 | 4.1 dB  |
| Peaking | 751 Hz  | 1.69 | -3.8 dB |
| Peaking | 2478 Hz | 2.01 | 3.6 dB  |
| Peaking | 3414 Hz | 4.42 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 6.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%202014/Beats%20Studio%202%202014.png)
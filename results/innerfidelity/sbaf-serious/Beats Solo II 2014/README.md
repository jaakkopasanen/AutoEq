# Beats Solo II 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.1; 25 -8.3; 28 -8.4; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.7; 128 -10.8; 141 -11.0; 155 -11.3; 170 -11.1; 187 -11.1; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.3; 302 -9.5; 332 -8.7; 365 -8.3; 402 -7.9; 442 -7.1; 486 -7.0; 535 -6.6; 588 -6.0; 647 -4.6; 712 -3.9; 783 -3.6; 861 -4.1; 947 -3.5; 1042 -3.4; 1146 -3.9; 1261 -4.0; 1387 -4.3; 1526 -4.3; 1678 -4.2; 1846 -3.6; 2031 -2.9; 2234 -2.4; 2457 -1.8; 2703 -1.3; 2973 -1.6; 3270 -2.4; 3597 -2.9; 3957 -2.3; 4353 -2.6; 4788 -5.1; 5267 -2.0; 5793 -0.5; 6373 -1.3; 7010 -2.2; 7711 -2.8; 8482 -3.0; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo II 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo II 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.39 | -4.7 dB |
| Peaking | 109 Hz  | 0.67 | -3.5 dB |
| Peaking | 240 Hz  | 0.65 | -5.9 dB |
| Peaking | 2723 Hz | 3.99 | 2.0 dB  |
| Peaking | 5974 Hz | 5.83 | 2.8 dB  |
| Peaking | 567 Hz  | 2.57 | -2.0 dB |
| Peaking | 656 Hz  | 1.68 | 1.8 dB  |
| Peaking | 1501 Hz | 3.31 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo%20II%202014/Beats%20Solo%20II%202014.png)
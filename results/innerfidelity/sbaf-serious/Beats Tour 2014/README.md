# Beats Tour 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.4; 25 -11.7; 28 -12.1; 31 -12.3; 34 -12.6; 37 -12.7; 41 -12.9; 45 -13.2; 49 -13.4; 54 -13.5; 60 -13.8; 66 -13.9; 72 -14.1; 79 -14.3; 87 -14.6; 96 -14.8; 106 -14.7; 116 -14.7; 128 -14.6; 141 -14.5; 155 -14.3; 170 -14.1; 187 -13.7; 206 -13.3; 227 -12.8; 249 -12.3; 274 -11.7; 302 -11.1; 332 -10.6; 365 -10.0; 402 -9.3; 442 -8.5; 486 -8.0; 535 -7.4; 588 -6.5; 647 -6.0; 712 -5.6; 783 -5.1; 861 -5.1; 947 -5.2; 1042 -5.3; 1146 -5.5; 1261 -5.5; 1387 -6.0; 1526 -6.3; 1678 -6.4; 1846 -6.1; 2031 -5.5; 2234 -5.0; 2457 -3.6; 2703 -2.7; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -3.8; 5267 -3.6; 5793 -2.9; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Tour 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Tour 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.39 | -6.0 dB |
| Peaking | 133 Hz  | 0.87 | -4.8 dB |
| Peaking | 258 Hz  | 1.49 | -2.9 dB |
| Peaking | 3466 Hz | 1.63 | 6.4 dB  |
| Peaking | 6314 Hz | 5.59 | 4.2 dB  |
| Peaking | 266 Hz  | 3.47 | 0.8 dB  |
| Peaking | 434 Hz  | 0.88 | -1.8 dB |
| Peaking | 748 Hz  | 0.83 | 2.5 dB  |
| Peaking | 1740 Hz | 2.36 | -1.4 dB |
| Peaking | 8394 Hz | 3.66 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Tour%202014/Beats%20Tour%202014.png)
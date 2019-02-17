# Accidentally Extraordinary Bamboo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.9; 25 -3.5; 28 -4.3; 31 -5.0; 34 -5.6; 37 -6.1; 41 -6.7; 45 -7.3; 49 -7.9; 54 -8.5; 60 -9.2; 66 -9.8; 72 -10.4; 79 -11.1; 87 -11.7; 96 -12.4; 106 -12.8; 116 -13.2; 128 -13.7; 141 -14.0; 155 -14.4; 170 -14.6; 187 -14.6; 206 -14.7; 227 -14.5; 249 -14.3; 274 -13.9; 302 -13.5; 332 -12.9; 365 -12.2; 402 -11.4; 442 -10.5; 486 -9.9; 535 -9.1; 588 -8.0; 647 -7.4; 712 -5.9; 783 -5.8; 861 -5.5; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -8.4; 1387 -9.8; 1526 -11.7; 1678 -13.3; 1846 -14.3; 2031 -14.2; 2234 -13.3; 2457 -11.0; 2703 -8.1; 2973 -4.8; 3270 -1.8; 3597 -0.5; 3957 -0.7; 4353 -2.6; 4788 -3.6; 5267 -4.2; 5793 -6.6; 6373 -12.4; 7010 -12.8; 7711 -8.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary Bamboo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary Bamboo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.38 | 4.7 dB   |
| Peaking | 175 Hz  | 0.58 | -8.7 dB  |
| Peaking | 2034 Hz | 2.02 | -10.0 dB |
| Peaking | 3715 Hz | 1.62 | 7.8 dB   |
| Peaking | 6734 Hz | 5.02 | -9.1 dB  |
| Peaking | 79 Hz   | 3.28 | -0.7 dB  |
| Peaking | 359 Hz  | 2.02 | -1.4 dB  |
| Peaking | 827 Hz  | 1.87 | 3.3 dB   |
| Peaking | 864 Hz  | 3    | -0.5 dB  |
| Peaking | 1558 Hz | 4.61 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%20Bamboo/Accidentally%20Extraordinary%20Bamboo.png)
# Accidentally Extraordinary Bamboo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -2.0; 34 -2.6; 37 -3.1; 41 -3.8; 45 -4.3; 49 -4.9; 54 -5.5; 60 -6.2; 66 -6.8; 72 -7.4; 79 -8.1; 87 -8.7; 96 -9.4; 106 -9.8; 116 -10.2; 128 -10.7; 141 -11.0; 155 -11.4; 170 -11.6; 187 -11.6; 206 -11.7; 227 -11.5; 249 -11.3; 274 -10.9; 302 -10.5; 332 -9.9; 365 -9.2; 402 -8.4; 442 -7.5; 486 -6.9; 535 -6.1; 588 -5.0; 647 -4.4; 712 -2.9; 783 -2.8; 861 -2.5; 947 -3.1; 1042 -3.7; 1146 -4.3; 1261 -5.4; 1387 -6.8; 1526 -8.7; 1678 -10.3; 1846 -11.3; 2031 -11.3; 2234 -10.3; 2457 -8.0; 2703 -5.1; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -1.2; 5793 -3.6; 6373 -9.5; 7010 -9.8; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary Bamboo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary Bamboo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.52 | 6.4 dB  |
| Peaking | 197 Hz  | 0.45 | -5.9 dB |
| Peaking | 832 Hz  | 0.91 | 5.9 dB  |
| Peaking | 1951 Hz | 1.64 | -8.1 dB |
| Peaking | 3625 Hz | 1.56 | 8.2 dB  |
| Peaking | 2385 Hz | 5.86 | -0.8 dB |
| Peaking | 3092 Hz | 3.93 | 1.9 dB  |
| Peaking | 3639 Hz | 3.56 | -2.4 dB |
| Peaking | 5326 Hz | 2.57 | 3.9 dB  |
| Peaking | 6630 Hz | 4.74 | -7.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%20Bamboo/Accidentally%20Extraordinary%20Bamboo.png)
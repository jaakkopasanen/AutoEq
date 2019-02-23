# VSonic VSD3S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.7; 45 -6.9; 49 -7.2; 54 -7.5; 60 -7.7; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.1; 96 -9.4; 106 -9.7; 116 -9.8; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.3; 187 -10.2; 206 -10.1; 227 -9.9; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.2; 442 -7.8; 486 -7.6; 535 -7.2; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.5; 861 -5.4; 947 -5.4; 1042 -5.4; 1146 -5.2; 1261 -5.1; 1387 -5.3; 1526 -5.6; 1678 -5.6; 1846 -5.1; 2031 -4.6; 2234 -4.0; 2457 -3.1; 2703 -2.5; 2973 -1.6; 3270 -0.8; 3597 -0.5; 3957 -1.4; 4353 -4.1; 4788 -5.6; 5267 -6.9; 5793 -7.8; 6373 -5.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -9.4; 10263 -9.8; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.31 | 2.0 dB  |
| Peaking | 158 Hz  |  0.62 | -4.1 dB |
| Peaking | 3212 Hz |  1.68 | 6.0 dB  |
| Peaking | 6907 Hz | 10.32 | 2.3 dB  |
| Peaking | 9882 Hz |  4.1  | -4.2 dB |
| Peaking | 23 Hz   |  1.27 | 0.5 dB  |
| Peaking | 909 Hz  |  1.75 | 1.4 dB  |
| Peaking | 2965 Hz |  4.3  | -1.7 dB |
| Peaking | 4689 Hz |  0.99 | 2.3 dB  |
| Peaking | 5343 Hz |  2.64 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3S/VSonic%20VSD3S.png)
# VSonic VSD3S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.2; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.2; 54 -7.5; 60 -7.8; 66 -8.2; 72 -8.5; 79 -8.8; 87 -9.2; 96 -9.5; 106 -9.7; 116 -9.9; 128 -10.0; 141 -10.3; 155 -10.3; 170 -10.3; 187 -10.3; 206 -10.2; 227 -9.9; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.3; 442 -7.8; 486 -7.6; 535 -7.2; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.5; 861 -5.4; 947 -5.4; 1042 -5.4; 1146 -5.3; 1261 -5.2; 1387 -5.3; 1526 -5.7; 1678 -5.6; 1846 -5.2; 2031 -4.6; 2234 -4.0; 2457 -3.1; 2703 -2.5; 2973 -1.6; 3270 -0.8; 3597 -0.5; 3957 -1.5; 4353 -4.1; 4788 -5.7; 5267 -7.0; 5793 -7.8; 6373 -5.3; 7010 -3.7; 7711 -5.1; 8482 -6.1; 9330 -9.4; 10263 -9.9; 11289 -7.2; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD3S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 132 Hz  | 0.56 | -4.4 dB |
| Peaking | 300 Hz  | 0.99 | -1.9 dB |
| Peaking | 3422 Hz | 1.81 | 5.2 dB  |
| Peaking | 5394 Hz | 4.45 | -3.6 dB |
| Peaking | 9951 Hz | 4.42 | -5.5 dB |
| Peaking | 19 Hz   | 1.89 | 1.4 dB  |
| Peaking | 868 Hz  | 2.66 | 0.5 dB  |
| Peaking | 1657 Hz | 5.52 | -0.8 dB |
| Peaking | 5972 Hz | 8.37 | -1.3 dB |
| Peaking | 6962 Hz | 5.63 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3S/VSonic%20VSD3S.png)
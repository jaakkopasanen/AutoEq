# Meze 11 Deco
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.2; 25 -15.2; 28 -15.3; 31 -15.3; 34 -15.4; 37 -15.4; 41 -15.4; 45 -15.4; 49 -15.5; 54 -15.5; 60 -15.6; 66 -15.7; 72 -15.9; 79 -16.0; 87 -16.1; 96 -16.3; 106 -16.2; 116 -16.0; 128 -15.9; 141 -15.8; 155 -15.5; 170 -15.2; 187 -14.8; 206 -14.3; 227 -13.7; 249 -13.2; 274 -12.6; 302 -12.0; 332 -11.3; 365 -10.5; 402 -9.9; 442 -8.9; 486 -8.4; 535 -7.6; 588 -6.8; 647 -5.5; 712 -5.2; 783 -3.9; 861 -3.7; 947 -3.7; 1042 -3.4; 1146 -3.2; 1261 -3.1; 1387 -3.3; 1526 -4.0; 1678 -6.0; 1846 -7.8; 2031 -7.5; 2234 -6.0; 2457 -3.5; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.1; 6373 -10.6; 7010 -7.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 11 Deco GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Deco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.29 | -7.7 dB |
| Peaking | 142 Hz  | 0.42 | -8.0 dB |
| Peaking | 904 Hz  | 1.28 | 4.3 dB  |
| Peaking | 4158 Hz | 1.21 | 7.1 dB  |
| Peaking | 6555 Hz | 7.43 | -8.2 dB |
| Peaking | 1407 Hz | 3.03 | 2.5 dB  |
| Peaking | 1604 Hz | 3.32 | 1.1 dB  |
| Peaking | 1882 Hz | 2.09 | -4.5 dB |
| Peaking | 2773 Hz | 3.95 | 3.3 dB  |
| Peaking | 9336 Hz | 2.67 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Deco/Meze%2011%20Deco.png)
# Plugged Crown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.9; 25 -6.1; 28 -6.4; 31 -6.7; 34 -7.0; 37 -7.3; 41 -7.5; 45 -7.8; 49 -8.1; 54 -8.3; 60 -8.7; 66 -9.0; 72 -9.3; 79 -9.4; 87 -9.3; 96 -9.6; 106 -10.7; 116 -11.7; 128 -12.5; 141 -12.8; 155 -12.9; 170 -12.7; 187 -13.6; 206 -13.7; 227 -13.3; 249 -13.5; 274 -13.6; 302 -13.3; 332 -12.7; 365 -11.8; 402 -10.7; 442 -8.9; 486 -8.2; 535 -6.7; 588 -4.7; 647 -3.4; 712 -3.1; 783 -3.7; 861 -5.0; 947 -6.1; 1042 -6.5; 1146 -7.2; 1261 -7.5; 1387 -7.6; 1526 -7.5; 1678 -8.2; 1846 -8.6; 2031 -8.0; 2234 -6.9; 2457 -5.5; 2703 -4.5; 2973 -2.9; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plugged Crown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plugged Crown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 133 Hz  | 2.73 | -1.0 dB |
| Peaking | 260 Hz  | 0.45 | -7.6 dB |
| Peaking | 660 Hz  | 1.58 | 7.3 dB  |
| Peaking | 1859 Hz | 1.77 | -3.1 dB |
| Peaking | 4295 Hz | 1.1  | 7.1 dB  |
| Peaking | 20 Hz   | 2.24 | 1.3 dB  |
| Peaking | 3443 Hz | 3.51 | 1.0 dB  |
| Peaking | 4267 Hz | 3.35 | -1.1 dB |
| Peaking | 6282 Hz | 2.87 | 4.5 dB  |
| Peaking | 7427 Hz | 1.57 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plugged%20Crown/Plugged%20Crown.png)
# Philips ActionFit SHQ5200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.6; 31 -2.6; 34 -3.5; 37 -4.3; 41 -5.3; 45 -6.1; 49 -6.7; 54 -7.5; 60 -8.1; 66 -8.7; 72 -9.2; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.5; 116 -10.7; 128 -10.8; 141 -10.9; 155 -10.9; 170 -10.7; 187 -10.5; 206 -10.4; 227 -10.1; 249 -9.7; 274 -9.3; 302 -9.0; 332 -8.1; 365 -6.9; 402 -7.2; 442 -9.2; 486 -8.6; 535 -8.0; 588 -7.4; 647 -7.1; 712 -7.1; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.1; 1387 -6.0; 1526 -5.6; 1678 -5.3; 1846 -4.1; 2031 -3.7; 2234 -2.7; 2457 -3.8; 2703 -3.7; 2973 -2.4; 3270 -0.8; 3597 -0.5; 3957 -1.2; 4353 -3.7; 4788 -3.7; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips ActionFit SHQ5200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ActionFit SHQ5200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.75 | 7.1 dB  |
| Peaking | 123 Hz  | 0.36 | -4.8 dB |
| Peaking | 363 Hz  | 4.31 | 1.9 dB  |
| Peaking | 3279 Hz | 1.16 | 5.1 dB  |
| Peaking | 5922 Hz | 4.07 | 5.2 dB  |
| Peaking | 454 Hz  | 8.85 | -1.2 dB |
| Peaking | 2186 Hz | 2.75 | 1.5 dB  |
| Peaking | 2711 Hz | 3.48 | -2.0 dB |
| Peaking | 3526 Hz | 6.13 | 1.5 dB  |
| Peaking | 8467 Hz | 3.45 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ActionFit%20SHQ5200/Philips%20ActionFit%20SHQ5200.png)
# Philips ActionFit SHQ5200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.6; 31 -4.6; 34 -5.5; 37 -6.3; 41 -7.2; 45 -8.0; 49 -8.7; 54 -9.4; 60 -10.1; 66 -10.7; 72 -11.2; 79 -11.6; 87 -12.0; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.7; 141 -12.9; 155 -12.8; 170 -12.7; 187 -12.5; 206 -12.4; 227 -12.1; 249 -11.7; 274 -11.2; 302 -10.9; 332 -10.1; 365 -8.9; 402 -9.1; 442 -11.1; 486 -10.5; 535 -10.0; 588 -9.3; 647 -9.1; 712 -9.0; 783 -8.6; 861 -8.4; 947 -8.4; 1042 -8.4; 1146 -8.2; 1261 -8.0; 1387 -8.0; 1526 -7.6; 1678 -7.3; 1846 -6.1; 2031 -5.6; 2234 -4.7; 2457 -5.8; 2703 -5.7; 2973 -4.4; 3270 -2.2; 3597 -0.9; 3957 -3.0; 4353 -5.7; 4788 -5.7; 5267 -2.3; 5793 -1.0; 6373 -1.5; 7010 -4.4; 7711 -6.6; 8482 -6.9; 9330 -6.9; 10263 -6.9; 11289 -6.9; 12418 -6.9; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips ActionFit SHQ5200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ActionFit SHQ5200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.92 | 7.6 dB  |
| Peaking | 124 Hz  | 0.43 | -6.2 dB |
| Peaking | 630 Hz  | 0.97 | -1.4 dB |
| Peaking | 3495 Hz | 3.6  | 6.1 dB  |
| Peaking | 5950 Hz | 3.9  | 6.5 dB  |
| Peaking | 385 Hz  | 6.1  | 2.6 dB  |
| Peaking | 435 Hz  | 4.53 | -1.9 dB |
| Peaking | 2208 Hz | 5.35 | 1.7 dB  |
| Peaking | 4531 Hz | 9.72 | -1.5 dB |
| Peaking | 8185 Hz | 5.65 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ActionFit%20SHQ5200/Philips%20ActionFit%20SHQ5200.png)
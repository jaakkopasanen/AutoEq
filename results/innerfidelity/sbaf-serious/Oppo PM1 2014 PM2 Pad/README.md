# Oppo PM1 2014 PM2 Pad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.6; 28 -4.8; 31 -5.0; 34 -5.1; 37 -5.2; 41 -5.3; 45 -5.3; 49 -5.2; 54 -5.0; 60 -4.9; 66 -5.5; 72 -6.1; 79 -6.7; 87 -7.3; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.5; 141 -8.7; 155 -8.8; 170 -8.9; 187 -9.0; 206 -9.0; 227 -8.8; 249 -9.1; 274 -9.6; 302 -9.8; 332 -9.6; 365 -7.9; 402 -6.4; 442 -6.9; 486 -7.7; 535 -8.1; 588 -8.0; 647 -8.2; 712 -8.6; 783 -8.6; 861 -8.7; 947 -7.0; 1042 -6.6; 1146 -7.1; 1261 -7.4; 1387 -8.1; 1526 -8.5; 1678 -8.9; 1846 -8.7; 2031 -8.3; 2234 -7.9; 2457 -7.0; 2703 -6.0; 2973 -4.7; 3270 -4.3; 3597 -4.6; 3957 -4.0; 4353 -3.8; 4788 -2.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.2; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 PM2 Pad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 PM2 Pad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 90 Hz   | 0.18 | 3.0 dB  |
| Peaking | 164 Hz  | 0.55 | -3.4 dB |
| Peaking | 280 Hz  | 0.29 | -2.4 dB |
| Peaking | 1763 Hz | 2.86 | -2.4 dB |
| Peaking | 5506 Hz | 2.21 | 6.5 dB  |
| Peaking | 322 Hz  | 4.2  | -1.7 dB |
| Peaking | 403 Hz  | 4.64 | 2.4 dB  |
| Peaking | 763 Hz  | 4.68 | -1.2 dB |
| Peaking | 3219 Hz | 4.47 | 1.8 dB  |
| Peaking | 9029 Hz | 4.86 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20PM2%20Pad/Oppo%20PM1%202014%20PM2%20Pad.png)
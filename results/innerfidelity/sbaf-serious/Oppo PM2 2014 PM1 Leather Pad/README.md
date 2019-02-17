# Oppo PM2 2014 PM1 Leather Pad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.4; 28 -2.5; 31 -2.6; 34 -2.7; 37 -2.8; 41 -2.8; 45 -2.8; 49 -2.8; 54 -2.8; 60 -2.4; 66 -2.9; 72 -3.9; 79 -4.0; 87 -4.6; 96 -5.1; 106 -5.3; 116 -5.6; 128 -5.9; 141 -6.1; 155 -6.1; 170 -6.3; 187 -6.7; 206 -7.2; 227 -7.5; 249 -7.5; 274 -7.2; 302 -6.3; 332 -5.7; 365 -6.2; 402 -6.3; 442 -6.4; 486 -7.0; 535 -7.4; 588 -7.4; 647 -7.7; 712 -6.9; 783 -6.4; 861 -7.1; 947 -6.5; 1042 -6.6; 1146 -6.6; 1261 -6.2; 1387 -6.6; 1526 -6.5; 1678 -6.4; 1846 -5.9; 2031 -5.2; 2234 -4.4; 2457 -3.4; 2703 -2.5; 2973 -1.5; 3270 -1.2; 3597 -0.9; 3957 -0.5; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Leather Pad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Leather Pad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.4  | 4.2 dB  |
| Peaking | 61 Hz   | 1.77 | 2.1 dB  |
| Peaking | 231 Hz  | 4.07 | -1.3 dB |
| Peaking | 1044 Hz | 0.61 | -0.8 dB |
| Peaking | 4154 Hz | 1.01 | 6.8 dB  |
| Peaking | 338 Hz  | 6.5  | 1.0 dB  |
| Peaking | 2879 Hz | 4.09 | 1.0 dB  |
| Peaking | 4289 Hz | 3.12 | -1.2 dB |
| Peaking | 6257 Hz | 2.56 | 4.1 dB  |
| Peaking | 7919 Hz | 1.56 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Leather%20Pad/Oppo%20PM2%202014%20PM1%20Leather%20Pad.png)
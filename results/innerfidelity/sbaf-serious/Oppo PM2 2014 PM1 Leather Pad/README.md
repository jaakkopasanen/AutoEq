# Oppo PM2 2014 PM1 Leather Pad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -4.0; 28 -4.1; 31 -4.2; 34 -4.3; 37 -4.4; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.4; 60 -3.9; 66 -4.5; 72 -5.5; 79 -5.6; 87 -6.2; 96 -6.7; 106 -6.9; 116 -7.2; 128 -7.5; 141 -7.7; 155 -7.7; 170 -7.9; 187 -8.2; 206 -8.7; 227 -9.0; 249 -9.1; 274 -8.8; 302 -7.9; 332 -7.3; 365 -7.7; 402 -7.9; 442 -8.0; 486 -8.6; 535 -8.9; 588 -9.0; 647 -9.2; 712 -8.5; 783 -8.0; 861 -8.6; 947 -8.1; 1042 -8.2; 1146 -8.1; 1261 -7.8; 1387 -8.1; 1526 -8.0; 1678 -8.0; 1846 -7.5; 2031 -6.8; 2234 -6.0; 2457 -5.0; 2703 -4.1; 2973 -3.1; 3270 -2.7; 3597 -2.5; 3957 -1.9; 4353 -2.5; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -9.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Leather Pad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Leather Pad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.29 | 2.8 dB  |
| Peaking | 172 Hz   | 0.62 | -2.5 dB |
| Peaking | 2822 Hz  | 0.22 | -3.3 dB |
| Peaking | 3447 Hz  | 1.04 | 6.7 dB  |
| Peaking | 5799 Hz  | 2.52 | 6.8 dB  |
| Peaking | 247 Hz   | 3.45 | -1.4 dB |
| Peaking | 464 Hz   | 0.79 | 1.8 dB  |
| Peaking | 546 Hz   | 1.75 | -2.5 dB |
| Peaking | 8918 Hz  | 4.15 | -3.8 dB |
| Peaking | 10416 Hz | 1.1  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Leather%20Pad/Oppo%20PM2%202014%20PM1%20Leather%20Pad.png)
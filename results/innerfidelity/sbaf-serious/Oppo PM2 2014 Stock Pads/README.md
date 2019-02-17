# Oppo PM2 2014 Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.7; 25 -2.9; 28 -3.2; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.6; 45 -3.6; 49 -3.6; 54 -3.7; 60 -3.5; 66 -3.9; 72 -4.6; 79 -5.0; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.4; 141 -6.6; 155 -6.7; 170 -6.7; 187 -7.1; 206 -7.6; 227 -7.8; 249 -7.9; 274 -7.4; 302 -6.7; 332 -5.9; 365 -6.1; 402 -6.1; 442 -6.2; 486 -7.0; 535 -7.5; 588 -7.4; 647 -7.4; 712 -6.8; 783 -6.4; 861 -7.0; 947 -6.5; 1042 -6.7; 1146 -6.8; 1261 -6.9; 1387 -7.6; 1526 -8.2; 1678 -8.7; 1846 -8.6; 2031 -8.1; 2234 -7.3; 2457 -6.2; 2703 -5.2; 2973 -4.1; 3270 -3.9; 3597 -4.3; 3957 -3.9; 4353 -4.4; 4788 -3.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.9; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.93 | 3.8 dB  |
| Peaking | 57 Hz   | 2.06 | 2.4 dB  |
| Peaking | 1847 Hz | 1.67 | -2.8 dB |
| Peaking | 3120 Hz | 1.97 | 2.7 dB  |
| Peaking | 5696 Hz | 2.93 | 6.6 dB  |
| Peaking | 240 Hz  | 1.57 | -2.7 dB |
| Peaking | 386 Hz  | 0.76 | 2.1 dB  |
| Peaking | 556 Hz  | 2.01 | -2.3 dB |
| Peaking | 6598 Hz | 9.89 | 1.9 dB  |
| Peaking | 8538 Hz | 2.64 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20Stock%20Pads/Oppo%20PM2%202014%20Stock%20Pads.png)
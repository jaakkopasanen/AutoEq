# Beats Solo3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.7; 25 -7.9; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.2; 66 -9.3; 72 -9.4; 79 -9.6; 87 -9.8; 96 -10.2; 106 -10.6; 116 -10.4; 128 -10.5; 141 -10.8; 155 -11.0; 170 -10.5; 187 -10.7; 206 -10.5; 227 -10.1; 249 -9.6; 274 -8.8; 302 -8.1; 332 -7.4; 365 -6.8; 402 -5.6; 442 -5.1; 486 -4.9; 535 -4.4; 588 -3.4; 647 -2.8; 712 -2.4; 783 -1.9; 861 -2.1; 947 -2.2; 1042 -2.5; 1146 -2.8; 1261 -3.2; 1387 -3.8; 1526 -4.2; 1678 -4.3; 1846 -4.1; 2031 -3.5; 2234 -3.3; 2457 -3.0; 2703 -3.3; 2973 -3.8; 3270 -4.6; 3597 -5.1; 3957 -3.2; 4353 -4.2; 4788 -5.0; 5267 -2.6; 5793 -0.5; 6373 -1.6; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.83 | -1.2 dB |
| Peaking | 65 Hz   | 0.4  | -2.5 dB |
| Peaking | 196 Hz  | 0.56 | -5.0 dB |
| Peaking | 740 Hz  | 0.64 | 3.7 dB  |
| Peaking | 6008 Hz | 3.75 | 4.6 dB  |
| Peaking | 412 Hz  | 7.72 | 0.3 dB  |
| Peaking | 1635 Hz | 2.74 | -1.3 dB |
| Peaking | 2404 Hz | 1.81 | 1.4 dB  |
| Peaking | 3445 Hz | 9.16 | -1.1 dB |
| Peaking | 8402 Hz | 4.43 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)
# Phiaton PS 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.8; 25 -4.8; 28 -4.8; 31 -4.9; 34 -5.1; 37 -5.2; 41 -5.3; 45 -5.4; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.4; 72 -6.7; 79 -7.0; 87 -7.3; 96 -7.6; 106 -7.9; 116 -8.1; 128 -8.4; 141 -8.6; 155 -8.7; 170 -8.9; 187 -9.0; 206 -9.1; 227 -8.9; 249 -8.9; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.0; 402 -7.7; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.6; 647 -6.2; 712 -6.1; 783 -5.9; 861 -5.9; 947 -6.1; 1042 -6.4; 1146 -6.7; 1261 -7.0; 1387 -7.5; 1526 -7.9; 1678 -8.1; 1846 -7.9; 2031 -7.4; 2234 -6.6; 2457 -5.2; 2703 -2.9; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -3.0; 5267 -3.2; 5793 -4.2; 6373 -6.1; 7010 -7.8; 7711 -9.2; 8482 -10.8; 9330 -13.4; 10263 -13.2; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.64 | 1.9 dB  |
| Peaking | 193 Hz   | 0.75 | -2.7 dB |
| Peaking | 2038 Hz  | 1.48 | -5.3 dB |
| Peaking | 3264 Hz  | 1    | 8.1 dB  |
| Peaking | 9384 Hz  | 2.49 | -8.3 dB |
| Peaking | 790 Hz   | 2.62 | 1.0 dB  |
| Peaking | 1460 Hz  | 4.92 | -0.7 dB |
| Peaking | 5572 Hz  | 7    | 0.8 dB  |
| Peaking | 7096 Hz  | 4.76 | -1.3 dB |
| Peaking | 11933 Hz | 5.74 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)
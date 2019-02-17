# Sennheiser EH150
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -2.4; 535 -4.4; 588 -5.4; 647 -6.0; 712 -5.9; 783 -6.3; 861 -6.5; 947 -6.6; 1042 -6.5; 1146 -6.3; 1261 -6.3; 1387 -6.5; 1526 -6.5; 1678 -6.2; 1846 -5.2; 2031 -4.3; 2234 -3.1; 2457 -1.8; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -5.1; 4788 -4.0; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH150 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.23 | 6.2 dB  |
| Peaking | 229 Hz  | 1.07 | 3.5 dB  |
| Peaking | 401 Hz  | 2.78 | 4.0 dB  |
| Peaking | 3126 Hz | 1.8  | 6.6 dB  |
| Peaking | 5892 Hz | 3.74 | 5.8 dB  |
| Peaking | 2433 Hz | 1.72 | 5.6 dB  |
| Peaking | 2797 Hz | 0.81 | -5.9 dB |
| Peaking | 4278 Hz | 2.17 | 7.5 dB  |
| Peaking | 4510 Hz | 7.17 | -7.8 dB |
| Peaking | 8111 Hz | 5.9  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.4 dB  |
| Peaking | 250 Hz   | 1.41 | 5.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH150/Sennheiser%20EH150.png)
# Sennheiser Amperior
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.6; 31 -3.3; 34 -3.9; 37 -4.5; 41 -5.3; 45 -6.0; 49 -6.5; 54 -7.0; 60 -7.0; 66 -6.3; 72 -7.2; 79 -9.2; 87 -10.1; 96 -10.4; 106 -10.8; 116 -11.5; 128 -11.7; 141 -11.9; 155 -11.9; 170 -11.4; 187 -11.3; 206 -11.2; 227 -10.7; 249 -9.1; 274 -8.0; 302 -7.8; 332 -6.7; 365 -5.4; 402 -4.5; 442 -4.4; 486 -4.4; 535 -4.6; 588 -4.6; 647 -4.8; 712 -5.0; 783 -5.2; 861 -5.4; 947 -5.7; 1042 -6.3; 1146 -6.8; 1261 -7.2; 1387 -7.9; 1526 -8.8; 1678 -10.0; 1846 -10.2; 2031 -10.3; 2234 -9.7; 2457 -8.4; 2703 -6.6; 2973 -5.5; 3270 -5.1; 3597 -5.2; 3957 -5.7; 4353 -5.2; 4788 -6.1; 5267 -6.3; 5793 -2.6; 6373 -0.6; 7010 -3.6; 7711 -6.0; 8482 -11.2; 9330 -9.4; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.3  | 5.7 dB  |
| Peaking | 138 Hz  | 1.06 | -6.5 dB |
| Peaking | 1894 Hz | 2.7  | -4.9 dB |
| Peaking | 6333 Hz | 4.61 | 6.4 dB  |
| Peaking | 8657 Hz | 5.77 | -6.4 dB |
| Peaking | 33 Hz   | 2.64 | 0.3 dB  |
| Peaking | 223 Hz  | 3.34 | -2.3 dB |
| Peaking | 496 Hz  | 1.11 | 2.5 dB  |
| Peaking | 2781 Hz | 0.85 | -1.3 dB |
| Peaking | 3211 Hz | 2.4  | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)
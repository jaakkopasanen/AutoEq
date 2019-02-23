# Sennheiser PX 200 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.7; 34 -2.1; 37 -2.5; 41 -2.9; 45 -3.3; 49 -3.6; 54 -4.1; 60 -4.5; 66 -4.8; 72 -5.2; 79 -5.5; 87 -5.8; 96 -4.9; 106 -5.0; 116 -6.2; 128 -6.4; 141 -6.7; 155 -7.3; 170 -7.5; 187 -7.8; 206 -7.9; 227 -7.5; 249 -6.8; 274 -7.2; 302 -7.8; 332 -7.6; 365 -7.8; 402 -8.1; 442 -8.4; 486 -8.6; 535 -8.7; 588 -8.6; 647 -8.4; 712 -8.9; 783 -8.8; 861 -8.8; 947 -9.2; 1042 -9.5; 1146 -9.9; 1261 -10.5; 1387 -11.6; 1526 -11.9; 1678 -11.2; 1846 -11.8; 2031 -11.4; 2234 -9.8; 2457 -8.5; 2703 -6.8; 2973 -5.2; 3270 -4.2; 3597 -3.7; 3957 -3.9; 4353 -6.4; 4788 -6.9; 5267 -4.8; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.35 | 6.6 dB  |
| Peaking | 1278 Hz | 0.15 | -1.8 dB |
| Peaking | 1714 Hz | 1.33 | -4.1 dB |
| Peaking | 3349 Hz | 2.29 | 5.2 dB  |
| Peaking | 6161 Hz | 3.97 | 7.4 dB  |
| Peaking | 84 Hz   | 1.97 | -0.7 dB |
| Peaking | 100 Hz  | 6.04 | 1.9 dB  |
| Peaking | 202 Hz  | 2.16 | -1.0 dB |
| Peaking | 250 Hz  | 3.99 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)
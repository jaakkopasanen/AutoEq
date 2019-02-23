# Sennheiser PX 100 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.3; 28 -2.2; 31 -3.0; 34 -3.6; 37 -4.1; 41 -4.7; 45 -5.3; 49 -5.8; 54 -6.4; 60 -6.9; 66 -7.4; 72 -7.9; 79 -8.3; 87 -8.7; 96 -8.9; 106 -8.9; 116 -9.3; 128 -9.6; 141 -9.9; 155 -10.0; 170 -10.1; 187 -9.9; 206 -9.9; 227 -9.7; 249 -9.5; 274 -9.1; 302 -8.6; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.4; 486 -7.3; 535 -6.8; 588 -6.6; 647 -6.4; 712 -6.2; 783 -6.2; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -7.0; 1387 -7.7; 1526 -8.5; 1678 -9.3; 1846 -9.5; 2031 -8.8; 2234 -6.8; 2457 -3.9; 2703 -2.4; 2973 -2.3; 3270 -4.3; 3597 -2.6; 3957 -3.8; 4353 -9.4; 4788 -7.3; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1    | 6.0 dB  |
| Peaking | 155 Hz  | 0.66 | -3.8 dB |
| Peaking | 1868 Hz | 2.54 | -4.2 dB |
| Peaking | 2787 Hz | 2.61 | 5.2 dB  |
| Peaking | 5986 Hz | 4.56 | 6.8 dB  |
| Peaking | 759 Hz  | 2.18 | 0.8 dB  |
| Peaking | 3828 Hz | 7.19 | 4.4 dB  |
| Peaking | 4487 Hz | 4.81 | -5.5 dB |
| Peaking | 5306 Hz | 7.44 | 3.2 dB  |
| Peaking | 9193 Hz | 6.45 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)
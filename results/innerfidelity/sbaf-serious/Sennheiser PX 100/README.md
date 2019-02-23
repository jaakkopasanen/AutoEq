# Sennheiser PX 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.6; 25 -4.2; 28 -4.9; 31 -5.4; 34 -5.9; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.5; 54 -7.8; 60 -8.2; 66 -8.5; 72 -8.9; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.1; 116 -10.2; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.5; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.7; 365 -8.3; 402 -8.1; 442 -7.6; 486 -7.4; 535 -7.3; 588 -6.9; 647 -6.7; 712 -6.8; 783 -6.6; 861 -6.8; 947 -6.9; 1042 -7.1; 1146 -7.3; 1261 -7.8; 1387 -8.7; 1526 -9.7; 1678 -10.5; 1846 -10.5; 2031 -9.2; 2234 -7.4; 2457 -5.1; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -1.8; 3957 -9.1; 4353 -12.3; 4788 -6.6; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 149 Hz  | 0.63 | -4.1 dB  |
| Peaking | 1828 Hz | 2.01 | -5.7 dB  |
| Peaking | 3231 Hz | 1.83 | 9.0 dB   |
| Peaking | 4246 Hz | 4.44 | -12.0 dB |
| Peaking | 5715 Hz | 3.08 | 6.9 dB   |
| Peaking | 20 Hz   | 1.87 | 3.8 dB   |
| Peaking | 326 Hz  | 3.07 | -0.4 dB  |
| Peaking | 717 Hz  | 2.1  | 0.5 dB   |
| Peaking | 6646 Hz | 8.03 | 2.1 dB   |
| Peaking | 7783 Hz | 2.23 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100/Sennheiser%20PX%20100.png)
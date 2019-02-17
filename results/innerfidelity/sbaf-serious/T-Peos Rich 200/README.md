# T-Peos Rich 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.1; 25 -9.1; 28 -9.1; 31 -9.1; 34 -9.2; 37 -9.2; 41 -9.3; 45 -9.4; 49 -9.5; 54 -9.7; 60 -9.8; 66 -10.1; 72 -10.2; 79 -10.5; 87 -10.7; 96 -11.0; 106 -11.1; 116 -11.0; 128 -11.2; 141 -11.1; 155 -11.1; 170 -10.9; 187 -10.6; 206 -10.4; 227 -10.0; 249 -9.6; 274 -9.2; 302 -8.6; 332 -8.3; 365 -7.6; 402 -7.1; 442 -6.5; 486 -6.2; 535 -5.6; 588 -4.9; 647 -4.6; 712 -4.4; 783 -4.2; 861 -4.4; 947 -4.7; 1042 -5.2; 1146 -5.7; 1261 -6.3; 1387 -7.2; 1526 -8.3; 1678 -9.1; 1846 -9.8; 2031 -10.1; 2234 -9.8; 2457 -8.0; 2703 -5.8; 2973 -2.9; 3270 -0.8; 3597 -0.5; 3957 -2.3; 4353 -6.8; 4788 -11.6; 5267 -12.8; 5793 -8.5; 6373 -4.9; 7010 -5.1; 7711 -8.5; 8482 -11.1; 9330 -9.9; 10263 -6.3; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Rich 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Rich 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.27 | -4.1 dB  |
| Peaking | 167 Hz   | 0.75 | -4.2 dB  |
| Peaking | 1920 Hz  | 2.92 | -5.7 dB  |
| Peaking | 8626 Hz  | 2.98 | -6.1 dB  |
| Peaking | 22050 Hz | 2.32 | -3.6 dB  |
| Peaking | 743 Hz   | 2.73 | 1.7 dB   |
| Peaking | 2390 Hz  | 3.84 | -2.8 dB  |
| Peaking | 3557 Hz  | 2.36 | 7.3 dB   |
| Peaking | 5087 Hz  | 3.16 | -10.4 dB |
| Peaking | 6542 Hz  | 3.77 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Rich%20200/T-Peos%20Rich%20200.png)
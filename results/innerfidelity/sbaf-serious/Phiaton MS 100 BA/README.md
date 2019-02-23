# Phiaton MS 100 BA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.8; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.5; 41 -6.7; 45 -7.0; 49 -7.1; 54 -7.4; 60 -7.8; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.7; 106 -10.0; 116 -10.3; 128 -10.5; 141 -10.8; 155 -11.0; 170 -11.1; 187 -11.1; 206 -11.2; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.2; 365 -10.0; 402 -9.6; 442 -9.1; 486 -8.8; 535 -8.3; 588 -7.6; 647 -7.1; 712 -6.9; 783 -6.4; 861 -6.5; 947 -6.5; 1042 -6.7; 1146 -6.9; 1261 -7.1; 1387 -7.5; 1526 -8.0; 1678 -8.4; 1846 -8.2; 2031 -7.8; 2234 -6.9; 2457 -4.7; 2703 -3.1; 2973 -2.0; 3270 -1.4; 3597 -1.0; 3957 -0.7; 4353 -1.3; 4788 -0.9; 5267 -0.5; 5793 -1.5; 6373 -5.7; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 100 BA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 100 BA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.71 | 1.2 dB  |
| Peaking | 149 Hz  | 0.63 | -4.2 dB |
| Peaking | 321 Hz  | 1.22 | -2.1 dB |
| Peaking | 1852 Hz | 2.17 | -3.5 dB |
| Peaking | 3904 Hz | 1.1  | 6.5 dB  |
| Peaking | 814 Hz  | 3.2  | 0.8 dB  |
| Peaking | 2847 Hz | 3.54 | 1.3 dB  |
| Peaking | 5250 Hz | 0.52 | -0.9 dB |
| Peaking | 5526 Hz | 3.95 | 4.8 dB  |
| Peaking | 5871 Hz | 1.79 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20100%20BA/Phiaton%20MS%20100%20BA.png)
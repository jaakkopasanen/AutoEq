# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -0.8; 79 -1.1; 87 -1.9; 96 -2.8; 106 -3.4; 116 -3.8; 128 -4.3; 141 -4.7; 155 -5.1; 170 -5.3; 187 -5.5; 206 -5.8; 227 -5.8; 249 -5.8; 274 -5.7; 302 -5.9; 332 -5.8; 365 -5.6; 402 -5.5; 442 -5.1; 486 -5.1; 535 -4.9; 588 -4.6; 647 -4.6; 712 -4.7; 783 -4.1; 861 -5.0; 947 -5.4; 1042 -5.7; 1146 -5.9; 1261 -6.1; 1387 -6.5; 1526 -7.5; 1678 -8.4; 1846 -9.2; 2031 -9.8; 2234 -10.3; 2457 -9.8; 2703 -9.9; 2973 -9.7; 3270 -9.5; 3597 -9.6; 3957 -9.0; 4353 -8.5; 4788 -7.0; 5267 -5.0; 5793 -5.2; 6373 -5.3; 7010 -4.8; 7711 -6.7; 8482 -10.6; 9330 -10.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.46 | 6.7 dB  |
| Peaking | 863 Hz  | 0.82 | 2.8 dB  |
| Peaking | 3044 Hz | 0.57 | -5.2 dB |
| Peaking | 6293 Hz | 0.94 | 4.7 dB  |
| Peaking | 8748 Hz | 4.22 | -6.9 dB |
| Peaking | 38 Hz   | 2.7  | -0.7 dB |
| Peaking | 77 Hz   | 3.26 | 1.2 dB  |
| Peaking | 179 Hz  | 1.4  | -0.6 dB |
| Peaking | 1385 Hz | 6.56 | 0.7 dB  |
| Peaking | 2042 Hz | 5.48 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)
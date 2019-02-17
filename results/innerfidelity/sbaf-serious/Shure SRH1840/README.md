# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.3; 66 -1.7; 72 -1.7; 79 -2.0; 87 -2.9; 96 -3.7; 106 -4.3; 116 -4.7; 128 -5.2; 141 -5.6; 155 -6.0; 170 -6.2; 187 -6.5; 206 -6.7; 227 -6.7; 249 -6.7; 274 -6.7; 302 -6.8; 332 -6.7; 365 -6.6; 402 -6.4; 442 -6.1; 486 -6.0; 535 -5.8; 588 -5.5; 647 -5.6; 712 -5.6; 783 -5.1; 861 -5.9; 947 -6.4; 1042 -6.6; 1146 -6.9; 1261 -7.0; 1387 -7.5; 1526 -8.4; 1678 -9.3; 1846 -10.1; 2031 -10.7; 2234 -11.2; 2457 -10.7; 2703 -10.8; 2973 -10.6; 3270 -10.5; 3597 -10.5; 3957 -9.9; 4353 -9.4; 4788 -8.0; 5267 -6.0; 5793 -6.2; 6373 -6.2; 7010 -5.7; 7711 -7.6; 8482 -11.5; 9330 -11.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.56 | 6.7 dB  |
| Peaking | 962 Hz   | 0.96 | 2.5 dB  |
| Peaking | 3062 Hz  | 0.48 | -6.3 dB |
| Peaking | 6681 Hz  | 0.81 | 5.1 dB  |
| Peaking | 8769 Hz  | 3.9  | -8.1 dB |
| Peaking | 37 Hz    | 3.23 | -0.6 dB |
| Peaking | 78 Hz    | 2.52 | 1.2 dB  |
| Peaking | 211 Hz   | 0.81 | -0.9 dB |
| Peaking | 572 Hz   | 1.96 | 0.6 dB  |
| Peaking | 10320 Hz | 7.29 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)
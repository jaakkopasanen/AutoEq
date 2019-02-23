# Bose AE2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.2; 25 -12.2; 28 -12.2; 31 -12.1; 34 -12.0; 37 -11.8; 41 -11.6; 45 -11.4; 49 -11.1; 54 -10.7; 60 -10.2; 66 -9.8; 72 -9.4; 79 -9.1; 87 -8.7; 96 -8.5; 106 -8.2; 116 -7.9; 128 -8.3; 141 -9.3; 155 -10.0; 170 -7.8; 187 -9.0; 206 -8.7; 227 -8.2; 249 -6.8; 274 -5.7; 302 -5.9; 332 -5.2; 365 -4.5; 402 -4.2; 442 -4.0; 486 -4.3; 535 -4.6; 588 -4.8; 647 -5.5; 712 -6.5; 783 -7.2; 861 -8.0; 947 -8.2; 1042 -7.8; 1146 -7.2; 1261 -6.4; 1387 -6.0; 1526 -5.6; 1678 -5.3; 1846 -4.9; 2031 -4.6; 2234 -3.8; 2457 -4.4; 2703 -5.4; 2973 -6.9; 3270 -7.2; 3597 -7.1; 3957 -7.3; 4353 -7.2; 4788 -4.3; 5267 -0.5; 5793 -3.5; 6373 -6.1; 7010 -8.7; 7711 -8.1; 8482 -8.8; 9330 -9.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose AE2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.55 | -5.9 dB |
| Peaking | 156 Hz   | 3    | -2.4 dB |
| Peaking | 2235 Hz  | 2.21 | 3.4 dB  |
| Peaking | 5358 Hz  | 3.48 | 10.9 dB |
| Peaking | 5565 Hz  | 0.88 | -4.8 dB |
| Peaking | 212 Hz   | 4.68 | -2.2 dB |
| Peaking | 448 Hz   | 1.09 | 2.7 dB  |
| Peaking | 906 Hz   | 2.65 | -2.6 dB |
| Peaking | 9254 Hz  | 5.51 | -3.0 dB |
| Peaking | 10287 Hz | 1.93 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20AE2/Bose%20AE2.png)
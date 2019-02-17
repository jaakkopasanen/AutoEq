# Meze 11 Neo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.7; 25 -3.3; 28 -4.0; 31 -4.5; 34 -5.0; 37 -5.5; 41 -6.0; 45 -6.5; 49 -6.9; 54 -7.4; 60 -7.9; 66 -8.4; 72 -8.9; 79 -9.4; 87 -9.9; 96 -10.4; 106 -10.7; 116 -10.9; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.6; 187 -11.5; 206 -11.4; 227 -11.1; 249 -10.9; 274 -10.6; 302 -10.2; 332 -9.7; 365 -9.2; 402 -8.7; 442 -8.0; 486 -7.5; 535 -6.9; 588 -6.0; 647 -5.5; 712 -5.1; 783 -4.7; 861 -4.7; 947 -4.8; 1042 -5.1; 1146 -5.3; 1261 -5.7; 1387 -6.3; 1526 -7.0; 1678 -7.6; 1846 -8.0; 2031 -8.2; 2234 -8.4; 2457 -7.7; 2703 -6.7; 2973 -4.5; 3270 -2.5; 3597 -1.5; 3957 -2.1; 4353 -4.3; 4788 -5.0; 5267 -3.7; 5793 -2.2; 6373 -0.5; 7010 -2.4; 7711 -4.7; 8482 -4.9; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 11 Neo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Neo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.51 | 3.3 dB  |
| Peaking | 159 Hz   | 0.51 | -6.9 dB |
| Peaking | 2162 Hz  | 2.01 | -3.9 dB |
| Peaking | 3540 Hz  | 3.69 | 4.5 dB  |
| Peaking | 6378 Hz  | 4.98 | 4.8 dB  |
| Peaking | 164 Hz   | 0.96 | 1.7 dB  |
| Peaking | 270 Hz   | 0.36 | -1.6 dB |
| Peaking | 761 Hz   | 1.17 | 2.3 dB  |
| Peaking | 1551 Hz  | 4.21 | -0.9 dB |
| Peaking | 22050 Hz | 1.71 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Neo/Meze%2011%20Neo.png)
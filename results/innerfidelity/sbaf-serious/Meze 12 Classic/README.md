# Meze 12 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.3; 28 -5.9; 31 -6.3; 34 -6.7; 37 -7.1; 41 -7.6; 45 -8.0; 49 -8.4; 54 -8.8; 60 -9.2; 66 -9.6; 72 -10.1; 79 -10.5; 87 -10.9; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.9; 141 -12.0; 155 -12.0; 170 -12.0; 187 -11.8; 206 -11.6; 227 -11.3; 249 -11.0; 274 -10.6; 302 -10.1; 332 -9.6; 365 -9.1; 402 -8.5; 442 -7.8; 486 -7.4; 535 -6.8; 588 -6.0; 647 -5.4; 712 -4.8; 783 -4.6; 861 -4.8; 947 -4.9; 1042 -5.3; 1146 -5.6; 1261 -6.0; 1387 -6.7; 1526 -7.5; 1678 -8.1; 1846 -8.6; 2031 -9.1; 2234 -9.4; 2457 -8.9; 2703 -7.5; 2973 -5.1; 3270 -2.7; 3597 -1.7; 3957 -2.5; 4353 -4.5; 4788 -5.3; 5267 -4.1; 5793 -2.7; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 12 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 110 Hz  | 0.6  | -6.0 dB |
| Peaking | 250 Hz  | 1.11 | -3.4 dB |
| Peaking | 2207 Hz | 1.81 | -4.9 dB |
| Peaking | 3515 Hz | 3.54 | 4.8 dB  |
| Peaking | 6418 Hz | 5.33 | 5.0 dB  |
| Peaking | 18 Hz   | 2.47 | 1.7 dB  |
| Peaking | 445 Hz  | 2    | -0.9 dB |
| Peaking | 776 Hz  | 1.57 | 1.5 dB  |
| Peaking | 1559 Hz | 4.26 | -0.9 dB |
| Peaking | 8073 Hz | 5.38 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2012%20Classic/Meze%2012%20Classic.png)
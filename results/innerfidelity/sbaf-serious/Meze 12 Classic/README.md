# Meze 12 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.1; 25 -4.6; 28 -5.1; 31 -5.6; 34 -6.0; 37 -6.4; 41 -6.9; 45 -7.2; 49 -7.6; 54 -8.0; 60 -8.5; 66 -8.8; 72 -9.3; 79 -9.7; 87 -10.2; 96 -10.5; 106 -10.8; 116 -10.9; 128 -11.1; 141 -11.2; 155 -11.3; 170 -11.2; 187 -11.1; 206 -10.9; 227 -10.6; 249 -10.3; 274 -9.8; 302 -9.4; 332 -8.9; 365 -8.3; 402 -7.7; 442 -7.1; 486 -6.6; 535 -6.0; 588 -5.2; 647 -4.7; 712 -4.1; 783 -3.9; 861 -4.0; 947 -4.2; 1042 -4.5; 1146 -4.9; 1261 -5.3; 1387 -6.0; 1526 -6.7; 1678 -7.4; 1846 -7.9; 2031 -8.3; 2234 -8.7; 2457 -8.2; 2703 -6.8; 2973 -4.4; 3270 -2.0; 3597 -1.0; 3957 -1.7; 4353 -3.8; 4788 -4.5; 5267 -3.4; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 12 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.9  | 2.7 dB  |
| Peaking | 141 Hz  | 0.64 | -5.8 dB |
| Peaking | 2280 Hz | 2.84 | -3.8 dB |
| Peaking | 3564 Hz | 2.84 | 5.5 dB  |
| Peaking | 6234 Hz | 4.61 | 5.5 dB  |
| Peaking | 142 Hz  | 1.27 | 1.7 dB  |
| Peaking | 307 Hz  | 0.32 | -1.8 dB |
| Peaking | 769 Hz  | 0.95 | 3.7 dB  |
| Peaking | 1683 Hz | 3.2  | -1.3 dB |
| Peaking | 8137 Hz | 4.73 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2012%20Classic/Meze%2012%20Classic.png)
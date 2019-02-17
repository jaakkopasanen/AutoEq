# Focal Spirit One Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.1; 25 -10.0; 28 -10.0; 31 -10.0; 34 -9.9; 37 -9.8; 41 -9.7; 45 -9.7; 49 -9.6; 54 -9.5; 60 -9.4; 66 -9.3; 72 -9.2; 79 -9.2; 87 -9.6; 96 -10.8; 106 -11.1; 116 -10.6; 128 -10.4; 141 -10.9; 155 -10.9; 170 -10.7; 187 -10.9; 206 -10.7; 227 -10.3; 249 -10.1; 274 -9.6; 302 -9.2; 332 -8.7; 365 -8.3; 402 -7.9; 442 -8.0; 486 -8.1; 535 -7.9; 588 -7.2; 647 -6.7; 712 -6.1; 783 -6.0; 861 -6.4; 947 -6.6; 1042 -6.3; 1146 -5.9; 1261 -5.8; 1387 -6.0; 1526 -6.3; 1678 -6.4; 1846 -6.3; 2031 -6.1; 2234 -5.8; 2457 -5.3; 2703 -5.3; 2973 -6.0; 3270 -6.7; 3597 -6.9; 3957 -5.7; 4353 -4.3; 4788 -3.6; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.9; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.7  | -3.2 dB |
| Peaking | 49 Hz   | 1.09 | -1.4 dB |
| Peaking | 103 Hz  | 3.37 | -2.0 dB |
| Peaking | 188 Hz  | 0.81 | -4.2 dB |
| Peaking | 5746 Hz | 2.99 | 6.7 dB  |
| Peaking | 1111 Hz | 1.54 | 0.6 dB  |
| Peaking | 2614 Hz | 4.17 | 1.3 dB  |
| Peaking | 3611 Hz | 3.12 | -1.9 dB |
| Peaking | 4160 Hz | 3.12 | 1.2 dB  |
| Peaking | 9873 Hz | 3.9  | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20Classic/Focal%20Spirit%20One%20Classic.png)
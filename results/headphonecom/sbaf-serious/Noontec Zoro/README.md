# Noontec Zoro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.2; 28 -8.5; 31 -8.8; 34 -9.0; 37 -9.1; 41 -9.3; 45 -9.5; 49 -9.6; 54 -9.7; 60 -9.9; 66 -10.2; 72 -10.4; 79 -10.6; 87 -10.7; 96 -11.0; 106 -11.2; 116 -11.2; 128 -11.2; 141 -11.5; 155 -11.9; 170 -11.6; 187 -11.8; 206 -11.8; 227 -11.6; 249 -11.4; 274 -10.9; 302 -10.5; 332 -10.5; 365 -10.4; 402 -10.0; 442 -9.9; 486 -9.8; 535 -9.6; 588 -9.2; 647 -8.6; 712 -8.0; 783 -7.3; 861 -6.8; 947 -6.6; 1042 -6.6; 1146 -6.7; 1261 -6.7; 1387 -7.5; 1526 -8.1; 1678 -8.0; 1846 -6.9; 2031 -5.1; 2234 -3.0; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -2.2; 7010 -4.0; 7711 -7.5; 8482 -11.1; 9330 -11.0; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 68 Hz    | 0.28 | -2.0 dB |
| Peaking | 265 Hz   | 0.31 | -4.0 dB |
| Peaking | 1659 Hz  | 1.99 | -6.2 dB |
| Peaking | 3416 Hz  | 0.4  | 7.6 dB  |
| Peaking | 8824 Hz  | 2.62 | -9.1 dB |
| Peaking | 201 Hz   | 5.37 | -0.3 dB |
| Peaking | 2518 Hz  | 6.39 | 1.4 dB  |
| Peaking | 4051 Hz  | 1.1  | -0.8 dB |
| Peaking | 5737 Hz  | 2.65 | 1.4 dB  |
| Peaking | 14254 Hz | 1.62 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)
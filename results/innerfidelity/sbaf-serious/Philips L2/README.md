# Philips L2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.8; 25 -9.2; 28 -9.7; 31 -10.0; 34 -10.2; 37 -10.4; 41 -10.5; 45 -10.6; 49 -10.5; 54 -10.5; 60 -10.4; 66 -10.3; 72 -10.1; 79 -9.9; 87 -9.7; 96 -9.6; 106 -9.5; 116 -9.5; 128 -9.8; 141 -9.3; 155 -8.9; 170 -8.3; 187 -8.4; 206 -8.3; 227 -7.9; 249 -7.7; 274 -7.3; 302 -6.7; 332 -6.5; 365 -6.1; 402 -5.7; 442 -5.2; 486 -4.9; 535 -4.4; 588 -3.7; 647 -3.3; 712 -3.4; 783 -3.5; 861 -4.0; 947 -4.4; 1042 -4.5; 1146 -4.2; 1261 -5.4; 1387 -7.3; 1526 -9.2; 1678 -10.5; 1846 -11.1; 2031 -11.2; 2234 -10.8; 2457 -10.7; 2703 -9.7; 2973 -8.5; 3270 -6.8; 3597 -5.5; 3957 -4.2; 4353 -2.0; 4788 -0.6; 5267 -0.5; 5793 -2.8; 6373 -6.2; 7010 -7.5; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips L2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips L2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 39 Hz    |  0.69 | -3.1 dB |
| Peaking | 130 Hz   |  0.43 | -2.5 dB |
| Peaking | 961 Hz   |  0.55 | 5.0 dB  |
| Peaking | 1940 Hz  |  1.1  | -8.1 dB |
| Peaking | 4832 Hz  |  2.78 | 7.3 dB  |
| Peaking | 1122 Hz  |  2.49 | -1.4 dB |
| Peaking | 1179 Hz  |  5.23 | 2.5 dB  |
| Peaking | 5578 Hz  | 10.16 | 2.6 dB  |
| Peaking | 6809 Hz  |  3.47 | -2.0 dB |
| Peaking | 19122 Hz |  2.13 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20L2/Philips%20L2.png)
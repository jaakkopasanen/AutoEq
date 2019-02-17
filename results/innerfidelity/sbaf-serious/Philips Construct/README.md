# Philips Construct
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.6; 25 -7.6; 28 -7.7; 31 -7.7; 34 -7.7; 37 -7.6; 41 -7.5; 45 -7.3; 49 -7.2; 54 -6.9; 60 -6.5; 66 -6.3; 72 -6.5; 79 -7.3; 87 -8.3; 96 -8.9; 106 -8.6; 116 -8.7; 128 -8.8; 141 -8.4; 155 -7.6; 170 -7.1; 187 -6.4; 206 -5.4; 227 -4.3; 249 -3.0; 274 -1.8; 302 -1.1; 332 -1.2; 365 -2.0; 402 -3.4; 442 -4.7; 486 -6.0; 535 -6.9; 588 -7.2; 647 -7.5; 712 -7.7; 783 -7.4; 861 -7.3; 947 -6.9; 1042 -6.0; 1146 -5.1; 1261 -3.9; 1387 -3.2; 1526 -2.6; 1678 -1.8; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Construct GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Construct ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.52 | -1.3 dB |
| Peaking | 123 Hz  | 1.37 | -2.9 dB |
| Peaking | 315 Hz  | 1.55 | 6.4 dB  |
| Peaking | 723 Hz  | 0.99 | -3.6 dB |
| Peaking | 2837 Hz | 0.51 | 6.9 dB  |
| Peaking | 66 Hz   | 5.48 | 1.1 dB  |
| Peaking | 1882 Hz | 4.34 | 0.9 dB  |
| Peaking | 2915 Hz | 2.05 | -0.9 dB |
| Peaking | 6258 Hz | 1.83 | 6.2 dB  |
| Peaking | 7399 Hz | 1.37 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Construct/Philips%20Construct.png)